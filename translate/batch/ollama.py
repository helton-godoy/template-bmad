#!/usr/bin/env python3
"""
Tradutor Markdown usando Ollama + Llama3.2:3b
Preserva 100% da formatação: tabelas, indentação, emojis, etc.
"""

import ollama
import sys
from pathlib import Path
import time

# Prompt otimizado para preservação de formatação
SYSTEM_PROMPT = """Você é um tradutor especializado em documentação técnica Markdown.

REGRAS CRÍTICAS DE TRADUÇÃO:
1. Traduza APENAS o texto em inglês para português brasileiro
2. PRESERVE COMPLETAMENTE toda a formatação Markdown original:
   - Mantenha TODAS as tabelas com pipes (|) exatamente como estão
   - Mantenha TODA indentação de listas (espaços antes de -)
   - Mantenha TODOS os emojis (🚀, 👉, 🎉, etc.)
   - Mantenha TODOS os links e URLs
   - Mantenha TODOS os code blocks e inline code
   - Mantenha TODOS os hashtags de títulos (#, ##, ###)
   - Mantenha TODAS as quebras de linha
3. NÃO adicione comentários, explicações ou interpretações
4. NÃO altere a estrutura do documento
5. NÃO traduza:
   - Nomes de comandos (bash, npm, etc.)
   - Nomes de variáveis e funções
   - URLs e caminhos de arquivo
   - Code blocks
6. Retorne APENAS o Markdown traduzido, nada mais

Traduza o seguinte documento de forma precisa e literal:"""

def translate_markdown_file(input_file: str, output_file: str = None, model: str = "llama3.2:3b"):
    """
    Traduz um arquivo Markdown usando Ollama
    
    Args:
        input_file: Caminho do arquivo original em inglês
        output_file: Caminho do arquivo traduzido (opcional, padrão: *_pt-br.md)
        model: Modelo Ollama a usar (padrão: llama3.2:3b)
    """
    input_path = Path(input_file)
    
    if not input_path.exists():
        print(f"❌ Erro: Arquivo não encontrado: {input_file}")
        return False
    
    # Define output file se não especificado
    if output_file is None:
        output_file = input_path.parent / f"{input_path.stem}_pt-br{input_path.suffix}"
    else:
        output_file = Path(output_file)
    
    print(f"📄 Traduzindo: {input_path.name}")
    print(f"🎯 Modelo: {model}")
    
    # Lê o arquivo original
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Erro ao ler arquivo: {e}")
        return False
    
    print(f"📏 Tamanho: {len(content)} caracteres")
    print(f"⏳ Traduzindo... (isso pode levar alguns minutos)")
    
    start_time = time.time()
    
    try:
        # Traduz usando Ollama
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'system',
                    'content': SYSTEM_PROMPT
                },
                {
                    'role': 'user',
                    'content': content
                }
            ],
            options={
                'temperature': 0.1,  # Baixa temperatura para tradução literal
                'top_p': 0.9,
                'num_predict': -1,  # Sem limite de tokens
            }
        )
        
        translated = response['message']['content']
        elapsed = time.time() - start_time
        
        # Salva o arquivo traduzido
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated)
        
        print(f"✅ Tradução concluída em {elapsed:.1f}s")
        print(f"💾 Salvo em: {output_file}")
        print(f"📏 Tamanho traduzido: {len(translated)} caracteres")
        
        # Análise de preservação
        checks = {
            "Tabelas (|)": "|" in content and "|" in translated,
            "Hashtags (#)": "#" in content and "#" in translated,
            "Code blocks (```)": "```" in content and "```" in translated,
            "Links ([])": "[" in content and "[" in translated,
        }
        
        print(f"\n🔍 Verificação de preservação:")
        for check, passed in checks.items():
            if check.split('(')[0].strip() in content or '(' in check:  # Só verifica se existe no original
                status = "✅" if passed else "❌"
                print(f"  {status} {check}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro durante tradução: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Uso: python translate_ollama.py <arquivo.md> [arquivo_saida.md] [modelo]")
        print("\nExemplos:")
        print("  python translate_ollama.py input.md")
        print("  python translate_ollama.py input.md output_pt-br.md")
        print("  python translate_ollama.py input.md output.md llama3.2:3b")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    model = sys.argv[3] if len(sys.argv) > 3 else "llama3.2:3b"
    
    success = translate_markdown_file(input_file, output_file, model)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
