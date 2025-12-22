#!/usr/bin/env python3
"""
Re-traduz arquivo demo para validar correções
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'src'))

from bmad_translate.core.translator import BMADTranslator
from bmad_translate.config.settings import Settings

def main():
    translator = BMADTranslator(Settings())
    
    print("="*60)
    print("Re-traduzindo demo_production.md")
    print("="*60 + "\n")
    
    result = translator.translate_file('demo_production.md')
    
    if result.success:
        print(f"✅ Tradução concluída!")
        print(f"   Arquivo: {result.target_file}")
        print(f"   Placeholders: {result.placeholders_count}")
    else:
        print(f"❌ Erro: {result.error_message}")
    
    return 0 if result.success else 1

if __name__ == "__main__":
    sys.exit(main())
