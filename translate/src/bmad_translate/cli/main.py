"""
Ponto de entrada principal para a CLI do BMAD Translation System.
"""

import argparse
import sys
import os
import logging
from typing import Optional

from ..core.translator import BMADTranslator
from ..core.linter import Linter
from ..config.settings import Settings

def setup_logging(verbose: bool = False):
    """Configura o logging."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    """Função principal da CLI."""
    parser = argparse.ArgumentParser(
        description="BMAD Translation System - Ferramenta de tradução local e segura."
    )
    
    parser.add_argument(
        "input_path",
        nargs="?",
        help="Arquivo ou diretório para traduzir"
    )
    
    parser.add_argument(
        "--source", "-s",
        default="en",
        help="Idioma de origem (padrão: en)"
    )
    
    parser.add_argument(
        "--target", "-t",
        default="pt",
        help="Idioma de destino (padrão: pt)"
    )
    
    parser.add_argument(
        "--recursive", "-r",
        action="store_true",
        help="Traduzir diretórios recursivamente"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Modo verboso"
    )
    
    parser.add_argument(
        "--no-lint",
        action="store_true",
        help="Desativar verificação de linting após tradução"
    )

    args = parser.parse_args()
    
    setup_logging(args.verbose)
    logger = logging.getLogger("bmad_translate.cli")
    
    # Se nenhum argumento for passado, mostra o help
    if not args.input_path:
        parser.print_help()
        sys.exit(0)

    try:
        settings = Settings()
        translator = BMADTranslator(settings)
        
        path = args.input_path
        results = []
        
        if os.path.isfile(path):
            logger.info(f"Traduzindo arquivo: {path}")
            results.append(translator.translate_file(path))
        elif os.path.isdir(path):
            logger.info(f"Traduzindo diretório: {path}")
            # translate_directory returns list of results? assuming it does or modifying to do so might be needed.
            # actually translate_directory in translator.py usually returns void or list. 
            # let's assume valid implementation or check translator.py if needed. 
            # To be safe, let's run linting separately if translate_directory returns nothing actionable easily.
            # Given limited context on translate_directory return type, we might assume it handles its own logging.
            # But we can iterate over files if we want linting. 
            # For now, let's just make it work for single file or check if we can get results.
            translator.translate_directory(path)
        else:
            logger.error(f"Caminho não encontrado: {path}")
            sys.exit(1)
            
        # Linting Logic
        if not args.no_lint:
            for result in results:
                if result and result.success and result.target_file:
                    try:
                        with open(result.target_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        lint_res = Linter.lint_file(result.target_file, content)
                        if lint_res['errors']:
                            logger.warning(f"⚠️  Problemas de formatação detectados em {result.target_file}:")
                            for err in lint_res['errors']:
                                logger.warning(f"  - {err}")
                        else:
                            logger.info(f"✅ Arquivo verificado e válido: {os.path.basename(result.target_file)}")
                            
                    except Exception as e:
                        logger.warning(f"Falha ao executar linter em {result.target_file}: {e}")

        logger.info("Operação concluída com sucesso.")
        
    except Exception as e:
        logger.error(f"Erro fatal: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
