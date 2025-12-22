#!/usr/bin/env python3
"""
Debug: testa tradução de README com múltiplas seções para identificar
onde as quebras de linha estão sendo perdidas.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'translate' / 'src'))

from bmad_translate.core.translator import BMADTranslator
from bmad_translate.config.settings import Settings

# Texto de teste simplificado similar ao README
test_text = """# Main Title

Description text here.

---

## Complete Documentation

👉 **[Link](./path.md)** - Description here

**Quick Links:**

- Item 1
- Item 2
"""

print("="*60)
print("TESTE: Preservação de quebras de linha")
print("="*60)

translator = BMADTranslator(Settings())

print("\nORIGINAL:")
print(test_text)
print("\n" + "="*60)

result = translator._translate_text(test_text, from_lang='en', to_lang='pt', protect=False)

print("\nTRADUZIDO:")
print(result)
print("\n" + "="*60)

# Verifica problemas
issues = []
if "**\n\n**" not in result and "**\n**" in result:
    issues.append("❌ Quebras duplas entre bolds perdidas")
if "]\n\n**" not in result and "**" in result and "]" in result:
    issues.append("❌ Quebras após links perdidas")

if issues:
    print("\nPROBLEMAS ENCONTRADOS:")
    for issue in issues:
        print(f"  {issue}")
else:
    print("\n✅ Todas as quebras preservadas!")
