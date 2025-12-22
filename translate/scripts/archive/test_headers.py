#!/usr/bin/env python3
"""
Teste direto usando _translate_text para validar proteção de hashtags
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'src'))

from bmad_translate.core.translator import BMADTranslator
from bmad_translate.config.settings import Settings

def test_header():
    """Testa título H1 usando método _translate_text."""
    translator = BMADTranslator(Settings())
    
    original = "# Introduction to BMAD Translator"
    print(f"Original: {original}")
    
    translated = translator._translate_text(original, from_lang='en', to_lang='pt', protect=False)
    print(f"Traduzido: {translated}")
    print(f"Hashtag presente? {'✅ SIM' if translated.startswith('#') else '❌ NÃO'}")
    
    return translated.startswith('#')

def test_multiple_headers():
    """Testa múltiplos níveis de títulos."""
    translator = BMADTranslator(Settings())
    
    test_cases = [
        "# Main Title",
        "## Secondary Title",
        "### Third Level",
    ]
    
    print("\n" + "="*60)
    print("Testando múltiplos níveis de títulos")
    print("="*60)
    
    results = []
    for test in test_cases:
        translated = translator._translate_text(test, from_lang='en', to_lang='pt', protect=False)
        level = test.count('#', 0, 6)
        has_hash = translated.startswith('#' * level)
        status = '✅' if has_hash else '❌'
        print(f"\n{status} {test}")
        print(f"   → {translated}")
        results.append(has_hash)
    
    return all(results)

if __name__ == "__main__":
    print("="*60)
    print("TESTE: Proteção de Hashtags em Títulos")
    print("="*60 + "\n")
    
    test1 = test_header()
    test2 = test_multiple_headers()
    
    print("\n" + "="*60)
    if test1 and test2:
        print("✅ TODOS OS TESTES PASSARAM!")
    else:
        print("❌ ALGUNS TESTES FALHARAM")
    print("="*60)
