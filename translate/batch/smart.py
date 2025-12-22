#!/usr/bin/env python3
"""
Sistema Avançado de Tradução com Chunking e Validação Automática
Suporta: Markdown, YAML, TOML, CSV
Preserva: Formatação, estrutura, code blocks, tabelas, indentação
"""

import argparse
import re
import logging
import sys
from pathlib import Path
from typing import List, Tuple, Dict
import argostranslate.translate
import argostranslate.package

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MarkdownChunker:
    """Divide Markdown em chunks preservando contexto"""
    
    def __init__(self, max_tokens: int = 800):
        self.max_tokens = max_tokens
    
    def estimate_tokens(self, text: str) -> int:
        """Estima quantidade de tokens (aproximadamente)"""
        return len(text.split())
    
    def chunk_by_sections(self, content: str) -> List[Tuple[str, Dict]]:
        """
        Divide Markdown por seções lógicas (títulos)
        Retorna: [(chunk_text, metadata), ...]
        """
        chunks = []
        current_chunk = []
        current_tokens = 0
        current_level = 0
        
        for line in content.split('\n'):
            line_tokens = self.estimate_tokens(line)
            
            # Detecta título
            header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
            
            if header_match:
                level = len(header_match.group(1))
                
                # Se título principal e já tem conteúdo, fecha chunk
                if level <= 2 and current_chunk and current_tokens > 200:
                    chunks.append(('\n'.join(current_chunk), {
                        'type': 'section',
                        'level': current_level,
                        'tokens': current_tokens
                    }))
                    current_chunk = []
                    current_tokens = 0
                
                current_level = level
            
            # Adiciona linha ao chunk atual
            current_chunk.append(line)
            current_tokens += line_tokens
            
            # Se excedeu limite, fecha chunk
            if current_tokens >= self.max_tokens:
                chunks.append(('\n'.join(current_chunk), {
                    'type': 'section',
                    'level': current_level,
                    'tokens': current_tokens
                }))
                current_chunk = []
                current_tokens = 0
        
        # Adiciona último chunk
        if current_chunk:
            chunks.append(('\n'.join(current_chunk), {
                'type': 'section',
                'level': current_level,
                'tokens': current_tokens
            }))
        
        logger.info(f"Documento dividido em {len(chunks)} chunks")
        return chunks


class FormattingValidator:
    """Valida e corrige formatação Markdown"""
    
    @staticmethod
    def validate_chunk(original: str, translated: str) -> Dict[str, bool]:
        """Valida preservação de formatação"""
        checks = {
            'tables': '|' in original and '|' in translated,
            'headers': '#' in original and '#' in translated,
            'code_blocks': '```' in original and '```' in translated,
            'bold': '**' in original and '**' in translated,
            'links': '[' in original and '[' in translated,
            'lists': re.search(r'^\s*[-*]', original, re.M) and re.search(r'^\s*[-*]', translated, re.M),
        }
        return checks
    
    @staticmethod
    def fix_indentation(original: str, translated: str) -> str:
        """Corrige indentação de listas preservando do original"""
        # Detecta padrões de indentação no original
        original_lines = original.split('\n')
        translated_lines = translated.split('\n')
        
        fixed_lines = []
        orig_idx = 0
        
        for trans_line in translated_lines:
            # Se é item de lista (começa com -)
            if re.match(r'^(\s*)[-*]\s', trans_line):
                # Procura linha correspondente no original
                while orig_idx < len(original_lines):
                    orig_line = original_lines[orig_idx]
                    if re.match(r'^(\s*)[-*]\s', orig_line):
                        # Extrai indentação do original
                        orig_indent = re.match(r'^(\s*)[-*]\s', orig_line).group(1)
                        # Aplica ao traduzido
                        trans_content = re.sub(r'^(\s*)[-*]\s', '', trans_line)
                        fixed_line = f"{orig_indent}- {trans_content}"
                        fixed_lines.append(fixed_line)
                        orig_idx += 1
                        break
                    orig_idx += 1
            else:
                fixed_lines.append(trans_line)
        
        return '\n'.join(fixed_lines)
    
    @staticmethod
    def fix_tables(original: str, translated: str) -> str:
        """Corrige tabelas se foram destruídas"""
        # Se original tem tabelas mas traduzido não
        if '|' in original and '|' not in translated:
            logger.warning("Tabela perdida na tradução, tentando reconstruir...")
            
            # Extrai linhas de tabela do original
            orig_lines = original.split('\n')
            trans_lines = translated.split('\n')
            
            fixed_lines = []
            for i, orig_line in enumerate(orig_lines):
                if '|' in orig_line and i < len(trans_lines):
                    # Preserva estrutura de tabela do original
                    # Mas traduz conteúdo das células
                    cells_orig = [c.strip() for c in orig_line.split('|')]
                    cells_trans = trans_lines[i].split() if i < len(trans_lines) else []
                    
                    # Reconstrói tabela
                    if len(cells_trans) > 0:
                        # Mapeia células traduzidas para estrutura original
                        fixed_line = '| ' + ' | '.join(cells_trans[:len(cells_orig)-2]) + ' |'
                        fixed_lines.append(fixed_line)
                    else:
                        fixed_lines.append(orig_line)  # Fallback: mantém original
                elif i < len(trans_lines):
                    fixed_lines.append(trans_lines[i])
            
            return '\n'.join(fixed_lines)
        
        return translated


class IncrementalTranslator:
    """Tradutor incremental com validação e correção"""
    
    def __init__(self, from_lang: str = 'en', to_lang: str = 'pt', max_tokens: int = 800):
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.chunker = MarkdownChunker(max_tokens)
        self.validator = FormattingValidator()
        self._ensure_argos_ready()
    
    def _ensure_argos_ready(self):
        """Garante que pacote de idioma está instalado"""
        available_packages = argostranslate.package.get_available_packages()
        package_to_install = None
        
        for pkg in available_packages:
            if pkg.from_code == self.from_lang and pkg.to_code == self.to_lang:
                package_to_install = pkg
                break
        
        if package_to_install:
            installed_packages = argostranslate.package.get_installed_packages()
            if not any(p.from_code == self.from_lang and p.to_code == self.to_lang 
                      for p in installed_packages):
                logger.info(f"Instalando pacote {self.from_lang} → {self.to_lang}")
                argostranslate.package.install_from_path(package_to_install.download())
    
    def translate_chunk(self, chunk: str, metadata: Dict, retry: int = 0) -> str:
        """Traduz um chunk com retry e validação"""
        try:
            logger.info(f"Traduzindo chunk ({metadata.get('tokens', 0)} tokens)...")
            
            # Traduz
            translated = argostranslate.translate.translate(chunk, self.from_lang, self.to_lang)
            
            # Valida formatação
            validation = self.validator.validate_chunk(chunk, translated)
            failed_checks = [k for k, v in validation.items() if not v]
            
            if failed_checks:
                logger.warning(f"Validação falhou: {', '.join(failed_checks)}")
                
                # Tentaaplicar correções
                if 'indentation' in failed_checks or 'lists' ==failed_checks:
                    translated = self.validator.fix_indentation(chunk, translated)
                    logger.info("✓ Indentação corrigida")
                
                if 'tables' in failed_checks:
                    translated = self.validator.fix_tables(chunk, translated)
                    logger.info("✓ Tabelas corrigidas")
            
            return translated
            
        except Exception as e:
            logger.error(f"Erro na tradução: {e}")
            if retry < 2:
                logger.info(f"Tentativa {retry + 1}/3...")
                return self.translate_chunk(chunk, metadata, retry + 1)
            else:
                logger.error("Falha após 3 tentativas, retornando original")
                return chunk
    
    def translate_file(self, input_path: Path, output_path: Path = None, 
                       save_partial: bool = True) -> bool:
        """Traduz arquivo completo com chunking"""
        try:
            # Lê arquivo
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            logger.info(f"Arquivo: {input_path.name} ({len(content)} chars)")
            
            # Define saída
            if output_path is None:
                output_path = input_path.parent / f"{input_path.stem}_pt-br{input_path.suffix}"
            
            # Divide em chunks
            chunks = self.chunker.chunk_by_sections(content)
            
            # Traduz cada chunk
            translated_chunks = []
            for i, (chunk, metadata) in enumerate(chunks, 1):
                logger.info(f"Chunk {i}/{len(chunks)}")
                translated = self.translate_chunk(chunk, metadata)
                translated_chunks.append(translated)
                
                # Salva parcial se habilitado
                if save_partial and i % 5 == 0:
                    partial_path = output_path.parent / f"{output_path.stem}_partial{output_path.suffix}"
                    with open(partial_path, 'w', encoding='utf-8') as f:
                        f.write('\n\n'.join(translated_chunks))
                    logger.info(f"✓ Progresso salvo ({i}/{len(chunks)} chunks)")
            
            # Junta e salva resultado final
            final_translation = '\n\n'.join(translated_chunks)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_translation)
            
            logger.info(f"✅ Tradução completa salva em: {output_path}")
            logger.info(f"Tamanho final: {len(final_translation)} chars")
            
            return True
            
        except Exception as e:
            logger.error(f"Erro ao traduzir arquivo: {e}")
            return False


def main():
    parser = argparse.ArgumentParser(
        description='Sistema Avançado de Tradução com Chunking e Validação'
    )
    parser.add_argument('input', help='Arquivo de entrada')
    parser.add_argument('-o', '--output', help='Arquivo de saída (opcional)')
    parser.add_argument('-f', '--from-lang', default='en', help='Idioma origem (padrão: en)')
    parser.add_argument('-t', '--to-lang', default='pt', help='Idioma destino (padrão: pt)')
    parser.add_argument('-c', '--chunk-size', type=int, default=800, 
                       help='Tamanho máximo do chunk em tokens (padrão: 800)')
    parser.add_argument('-s', '--save-partial', action='store_true',
                       help='Salvar progresso parcial a cada 5 chunks')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Modo verboso (debug)')
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else None
    
    if not input_path.exists():
        logger.error(f"Arquivo não encontrado: {input_path}")
        return 1
    
    # Cria tradutor
    translator = IncrementalTranslator(
        from_lang=args.from_lang,
        to_lang=args.to_lang,
        max_tokens=args.chunk_size
    )
    
    # Traduz
    success = translator.translate_file(input_path, output_path, args.save_partial)
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
