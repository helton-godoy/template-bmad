#!/usr/bin/env python3
"""
Testa proteção de tabelas Markdown usando _translate_text
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'src'))

from bmad_translate.core.translator import BMADTranslator
from bmad_translate.config.settings import Settings

test_table = """| Column 1 | Column 2 |
| -------- | -------- |
| Value A  | Value B  |
| Value C  | Value D  |"""

print("="*60)
print("TESTE E2E: Proteção de Tabelas Markdown")
print("="*60)

translator = BMADTranslator(Settings())

print("\nOriginal:")
print(test_table)

result = translator._translate_text(test_table, from_lang='en', to_lang='pt', protect=False)

print("\nTraduzido:")
print(result)

if '|' in result:
    print("\n✅ SUCESSO: Pipes preservados! Tabela intacta!")
else:
    print("\n❌ FALHA: Pipes removidos! Tabela destruída!")
