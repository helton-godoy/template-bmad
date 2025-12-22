#!/usr/bin/env python3
"""
Script de debug para entender o comportamento do Argos com guillemets.
"""

import argostranslate.translate

# Testa vários formatos
test_cases = [
    "Welcome to the «production environment» of the BMAD System.",
    "This validates our commitment to «precision» and «cultural adaptation».",
    "We value «precision» and «quality».",
    "Use «workflow», «framework», and «setup».",
]

print("="*60)
print("DEBUG: Como Argos trata guillemets")
print("="*60)

for test in test_cases:
    translated = argostranslate.translate.translate(test, 'en', 'pt')
    print(f"\nInput:  {test}")
    print(f"Output: {translated}")
    print(f"---")

# Testa com espaços extras
print("\n" + "="*60)
print("DEBUG: Testando com espaços ao redor dos guillemets")
print("="*60)

test_with_spaces = [
    "Welcome to the « production environment » of the BMAD System.",
    "We value « precision » and « quality ».",
]

for test in test_with_spaces:
    translated = argostranslate.translate.translate(test, 'en', 'pt')
    print(f"\nInput:  {test}")
    print(f"Output: {translated}")
    print(f"---")
