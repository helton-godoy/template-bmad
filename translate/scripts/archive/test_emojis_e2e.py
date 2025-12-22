#!/usr/bin/env python3
"""
Testa proteção de emojis usando _translate_text
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'src'))

from bmad_translate.core.translator import BMADTranslator
from bmad_translate.config.settings import Settings

test_cases = [
    ("👉 **[Link](./path.md)** - Description", "👉.*\\[.*\\]"),
    ("## 🤝 Community", "##\\s*🤝"),
    ("🚀 Getting Started", "🚀"),
    ("## 📚 Documentation", "##\\s*📚"),
]

print("="*60)
print("TESTE E2E: Proteção de Emojis")
print("="*60)

translator = BMADTranslator(Settings())

passed = 0
failed = 0

for test_input, pattern in test_cases:
    result = translator._translate_text(test_input, from_lang='en', to_lang='pt', protect=False)
    
    import re
    match = re.search(pattern, result)
    
    status = "✅" if match else "❌"
    print(f"\n{status} Input:  {test_input}")
    print(f"   Output: {result}")
    
    if match:
        passed += 1
    else:
        failed += 1
        print(f"   ⚠️  Esperava padrão: {pattern}")

print("\n" + "="*60)
print(f"Resultado: {passed}/{len(test_cases)} passaram")
if failed == 0:
    print("✅ TODOS OS TESTES PASSARAM!")
else:
    print(f"❌ {failed} teste(s) falharam")
