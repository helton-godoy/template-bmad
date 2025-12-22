#!/usr/bin/env python3
"""
Testa se Argos preserva indentação de listas
"""

import argostranslate.translate

test_list = """1. **First item:**
   - Sub-item A
   - Sub-item B
   - Sub-item C
2. **Second item:**
   - Sub-item D
   - Sub-item E"""

print("="*60)
print("TESTE: Argos e Indentação de Listas")
print("="*60)

print("\nOriginal:")
print(test_list)

translated = argostranslate.translate.translate(test_list, 'en', 'pt')

print("\nTraduzido:")
print(translated)

# Check if leading spaces are preserved
if '   -' in test_list and '   -' not in translated:
    print("\n❌ PROBLEMA: Indentação removida!")
else:
    print("\n✅ Indentação preservada")
