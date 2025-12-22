#!/usr/bin/env python3
"""
Sistema Híbrido de Tradução: Argos + Ollama
Pipeline: Argos (speed) → Ollama (quality) → Output perfeito
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import List, Tuple, Dict
import argostranslate.translate
import ollama

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MarkdownChunker:
    """Divide Markdown em chunks preservando contexto"""
    
    def __init__(self, max_tokens: int = 500):  # Menor para Ollama processar
        self.max_tokens = max_tokens
    
    def estimate_tokens(self, text: str) -> int:
        """Estima tokens"""
        return len(text.split())
    
    def chunk_by_sections(self, content: str) -> List[Tuple[str, Dict]]:
        """Divide por seções com tamanho controlado"""
        chunks = []
        current_chunk = []
        current_tokens = 0
        
        for line in content.split('\n'):
            line_tokens = self.estimate_tokens(line)
            
            # Detecta título principal
            if line.startswith('##') and current_chunk and current_tokens > 100:
                chunks.append(('\n'.join(current_chunk), {'tokens': current_tokens}))
                current_chunk = []
                current_tokens = 0
            
            current_chunk.append(line)
            current_tokens += line_tokens
            
            # Força quebra se muito grande
            if current_tokens >= self.max_tokens:
                chunks.append(('\n'.join(current_chunk), {'tokens': current_tokens}))
                current_chunk = []
                current_tokens = 0
        
        if current_chunk:
            chunks.append(('\n'.join(current_chunk), {'tokens': current_tokens}))
        
        logger.info(f"📦 Dividido em {len(chunks)} chunks")
        return chunks


class HybridTranslator:
    """Tradutor híbrido: Argos (velocidade) + Ollama (qualidade)"""
    
    def __init__(self, ollama_model: str = "llama3.2:3b", max_tokens: int = 500):
        self.ollama_model = ollama_model
        self.chunker = MarkdownChunker(max_tokens)
        logger.info(f"🤖 Modelo Ollama: {ollama_model}")
    
    def translate_with_argos(self, text: str) -> str:
        """Fase 1: Tradução rápida com Argos"""
        return argostranslate.translate.translate(text, 'en', 'pt')
    
    def validate_and_fix_with_ollama(self, original: str, translated: str) -> str:
        """Fase 2: Validação e correção com Ollama"""
        
        prompt = f"""Você é um validador de tradução Markdown especializado.

TAREFA: Analise a tradução abaixo e CORRIJA apenas os problemas de formatação e tradução.

REGRAS DE CORREÇÃO:
1. Se hashtags têm espaços extras (## #), corrija para (##)
2. Se indentação de listas foi perdida, restaure do original
3. Se tabelas foram destruídas, reconstrua preservando pipes |
4. Se tradução está incorreta, melhore
5. Mantenha TODOS os links, code blocks e URLs
6. NÃO adicione explicações ou comentários
7. Retorne APENAS o Markdown corrigido

ORIGINAL (Inglês):
{original}

TRADUÇÃO (Português - pode ter erros):
{translated}

CORRIJA a tradução acima e retorne APENAS o Markdown corrigido em português:"""

        try:
            response = ollama.chat(
                model=self.ollama_model,
                messages=[{'role': 'user', 'content': prompt}],
                options={
                    'temperature': 0.1,
                    'top_p': 0.9,
                }
            )
            
            corrected = response['message']['content']
            
            # Validação básica: se resposta muito diferente, mantém tradução Argos
            if len(corrected) < len(translated) * 0.5:
                logger.warning("⚠️  Ollama retornou texto muito curto, mantendo Argos")
                return translated
            
            return corrected
            
        except Exception as e:
            logger.error(f"❌ Erro no Ollama: {e}, mantendo tradução Argos")
            return translated
    
    def translate_chunk(self, chunk: str, chunk_num: int, total: int) -> str:
        """Pipeline completo: Argos → Ollama → Output"""
        
        logger.info(f"\n{'='*70}")
        logger.info(f"Chunk {chunk_num}/{total}")
        logger.info(f"{'='*70}")
        
        # Fase 1: Argos (rápido)
        logger.info("⚡ Fase 1: Traduzindo com Argos...")
        argos_translation = self.translate_with_argos(chunk)
       
        logger.info(f"✅ Argos: {len(argos_translation)} chars")
        
        # Fase 2: Ollama (qualidade)
        logger.info("🤖 Fase 2: Validando e corrigindo com Ollama...")
        final_translation = self.validate_and_fix_with_ollama(chunk, argos_translation)
        
        logger.info(f"✅ Ollama: {len(final_translation)} chars")
        
        # Comparação
        improvement = len(final_translation) - len(argos_translation)
        if improvement > 0:
            logger.info(f"📈 Melhoria: +{improvement} chars (Ollama expandiu)")
        elif improvement < 0:
            logger.info(f"📉 Redução: {improvement} chars (Ollama otimizou)")
        else:
            logger.info(f"🎯 Tamanho mantido (sem mudanças)")
        
        return final_translation
    
    def translate_file(self, input_path: Path, output_path: Path = None) -> bool:
        """Traduz arquivo completo com pipeline híbrido"""
        
        try:
            # Lê arquivo
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            logger.info(f"\n{'='*70}")
            logger.info(f"📄 Arquivo: {input_path.name}")
            logger.info(f"📏 Tamanho: {len(content)} chars")
            logger.info(f"{'='*70}\n")
            
            # Define saída
            if output_path is None:
                output_path = input_path.parent / f"{input_path.stem}_hybrid_pt-br{input_path.suffix}"
            
            # Chunking
            chunks = self.chunker.chunk_by_sections(content)
            
            # Traduz cada chunk com pipeline híbrido
            translated_chunks = []
            for i, (chunk, metadata) in enumerate(chunks, 1):
                translated = self.translate_chunk(chunk, i, len(chunks))
                translated_chunks.append(translated)
            
            # Junta resultado
            final_content = '\n\n'.join(translated_chunks)
            
            # Salva
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            
            logger.info(f"\n{'='*70}")
            logger.info(f"✅ CONCLUÍDO!")
            logger.info(f"💾 Salvo em: {output_path}")
            logger.info(f"📏 Tamanho final: {len(final_content)} chars")
            logger.info(f"📊 Original: {len(content)} → Final: {len(final_content)}")
            logger.info(f"{'='*70}\n")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro: {e}")
            return False


def main():
    parser = argparse.ArgumentParser(
        description='Sistema Híbrido: Argos (velocidade) + Ollama (qualidade)'
    )
    parser.add_argument('input', help='Arquivo de entrada')
    parser.add_argument('-o', '--output', help='Arquivo de saída (opcional)')
    parser.add_argument('-m', '--model', default='llama3.2:3b',
                       help='Modelo Ollama (padrão: llama3.2:3b)')
    parser.add_argument('-c', '--chunk-size', type=int, default=500,
                       help='Tamanho do chunk em tokens (padrão: 500)')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Modo verboso')
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else None
    
    if not input_path.exists():
        logger.error(f"❌ Arquivo não encontrado: {input_path}")
        return 1
    
    # Cria tradutor híbrido
    translator = HybridTranslator(
        ollama_model=args.model,
        max_tokens=args.chunk_size
    )
    
    # Traduz
    success = translator.translate_file(input_path, output_path)
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
