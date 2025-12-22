#!/usr/bin/env python3
"""
Testa se Argos está removendo quebras de linha
"""

import argostranslate.translate

test_cases = [
    "**[Link](./path.md)** - Description\n\n**Quick Links:**",
    "Text here.\n\nNext paragraph.",
    "Item 1\n\nItem 2",
]

print("="*60)
print("TESTE: Argos e quebras de linha")
print("="*60)

for i, test in enumerate(test_cases, 1):
    translated = argostranslate.translate.translate(test, 'en', 'pt')
    
    print(f"\n[Test {i}]")
    print(f"Input:  {repr(test)}")
    print(f"Output: {repr(translated)}")
    
    if '\n\n' in test and '\n\n' not in translated:
        print("❌ Quebra dupla perdida!")
    else:
        print("✅ OK")
