#!/usr/bin/env python3
"""
Testa se Argos remove/modifica emojis
"""

import argostranslate.translate

test_cases = [
    "👉 **[Link](./path.md)** - Description",
    "## 🤝 Community",
    "🚀 Getting Started",
    "## 📚 Documentation",
]

print("="*60)
print("TESTE: Argos e Emojis")
print("="*60)

for test in test_cases:
    translated = argostranslate.translate.translate(test, 'en', 'pt')
    
    print(f"\nInput:  {repr(test)}")
    print(f"Output: {repr(translated)}")
    
    # Verifica se emojis foram preservados
    input_emojis = [c for c in test if ord(c) > 127]
    output_emojis = [c for c in translated if ord(c) > 127]
    
    if len(input_emojis) != len(output_emojis):
        print(f"❌ Emojis perdidos! Input: {input_emojis}, Output: {output_emojis}")
    else:
        print(f"✅ Emojis preservados")
