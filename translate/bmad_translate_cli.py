#!/usr/bin/env python3
"""
BMAD Translation CLI - Ponto de entrada principal

Consolida todas as ferramentas de tradução em um único CLI:
- Tradução batch (Argos base)
- Smart Translator (Argos + chunking)
- Hybrid Translator (Argos + Ollama) - experimental
- Ollama Translator - para chunks pequenos
"""

import sys
import argparse
from pathlib import Path

# Adiciona src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from bmad_translate.core.translator import BMADTranslator

def translate_batch(args):
    """Tradução em batch com Argos (rápido, 95% qualidade)"""
    from translate.batch import BatchTranslator
    
    translator = BatchTranslator()
    files = args.files or translator.discover_files(args.dir)
    
    translator.translate_all(
        files=files,
        protect=True,  # Sempre usar proteções
        verbose=args.verbose
    )

def translate_smart(args):
    """Smart Translator com chunking e validação"""
    from translate.smart import SmartTranslator
    
    translator = SmartTranslator(
        max_tokens=args.chunk_size,
        save_partial=args.save_partial
    )
    
    translator.translate_file(
        args.input,
        args.output,
        verbose=args.verbose
    )

def translate_hybrid(args):
    """Hybrid Translator (Argos + Ollama) - experimental"""
    from translate.hybrid import HybridTranslator
    
    translator = HybridTranslator(
        ollama_model=args.model,
        max_tokens=args.chunk_size
    )
    
    translator.translate_file(
        args.input,
        args.output
    )

def translate_ollama(args):
    """Ollama Translator - apenas chunks pequenos"""
    from translate.ollama import OllamaTranslator
    
    translator = OllamaTranslator(model=args.model)
    
    translator.translate_file(
        args.input,
        args.output
    )

def main():
    parser = argparse.ArgumentParser(
        description='BMAD Translation CLI - Sistema completo de tradução',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Exemplos:
  # Tradução batch de múltiplos arquivos (recomendado)
  %(prog)s batch --dir _bmad/bmm/docs
  
  # Smart translator com chunking (arquivos grandes)
  %(prog)s smart arquivo.md --save-partial
  
  # Hybrid com Ollama (experimental, máxima qualidade)
  %(prog)s hybrid arquivo.md -m gemma3:4b
  
  # Ollama puro (apenas arquivos pequenos)
  %(prog)s ollama arquivo.md -m llama3.2:3b
'''
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Comando a executar')
    
    # Batch translator
    batch_parser = subparsers.add_parser(
        'batch',
        help='Tradução em batch (rápido, 95% qualidade)'
    )
    batch_parser.add_argument('--dir', default='_bmad/bmm/docs', help='Diretório para traduzir')
    batch_parser.add_argument('--files', nargs='+', help='Arquivos específicos')
    batch_parser.add_argument('-v', '--verbose', action='store_true', help='Modo verboso')
    batch_parser.set_defaults(func=translate_batch)
    
    # Smart translator
    smart_parser = subparsers.add_parser(
        'smart',
        help='Smart translator com chunking e validação'
    )
    smart_parser.add_argument('input', help='Arquivo de entrada')
    smart_parser.add_argument('-o', '--output', help='Arquivo de saída')
    smart_parser.add_argument('-c', '--chunk-size', type=int, default=600, help='Tamanho do chunk')
    smart_parser.add_argument('-s', '--save-partial', action='store_true', help='Salvar parcial')
    smart_parser.add_argument('-v', '--verbose', action='store_true', help='Modo verboso')
    smart_parser.set_defaults(func=translate_smart)
    
    # Hybrid translator
    hybrid_parser = subparsers.add_parser(
        'hybrid',
        help='Hybrid translator (Argos + Ollama) - experimental'
    )
    hybrid_parser.add_argument('input', help='Arquivo de entrada')
    hybrid_parser.add_argument('-o', '--output', help='Arquivo de saída')
    hybrid_parser.add_argument('-m', '--model', default='llama3.2:3b', help='Modelo Ollama')
    hybrid_parser.add_argument('-c', '--chunk-size', type=int, default=500, help='Tamanho do chunk')
    hybrid_parser.set_defaults(func=translate_hybrid)
    
    # Ollama translator
    ollama_parser = subparsers.add_parser(
        'ollama',
        help='Ollama translator - apenas arquivos pequenos'
    )
    ollama_parser.add_argument('input', help='Arquivo de entrada')
    ollama_parser.add_argument('-o', '--output', help='Arquivo de saída')
    ollama_parser.add_argument('-m', '--model', default='llama3.2:3b', help='Modelo Ollama')
    ollama_parser.set_defaults(func=translate_ollama)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    return args.func(args)

if __name__ == "__main__":
    sys.exit(main())
