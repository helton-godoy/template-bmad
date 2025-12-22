#!/usr/bin/env python3
"""
Testa se Argos preserva tabelas Markdown
"""

import argostranslate.translate

test_table = """| Column 1 | Column 2 |
| -------- | -------- |
| Value A  | Value B  |
| Value C  | Value D  |"""

print("="*60)
print("TESTE: Argos e Tabelas Markdown")
print("="*60)

print("\nOriginal:")
print(test_table)

translated = argostranslate.translate.translate(test_table, 'en', 'pt')

print("\nTraduzido:")
print(translated)

if '|' in test_table and '|' not in translated:
    print("\n❌ PROBLEMA: Pipes removidos! Tabela destruída!")
else:
    print("\n✅ Pipes preservados")
