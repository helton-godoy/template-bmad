#!/usr/bin/env python3
"""
Testa diferentes estratégias de marcadores para títulos
"""

import argostranslate.translate

test_markers = [
    ("⟨H1⟩Introduction to BMAD", "Unicode angle brackets"),
    ("[H1] Introduction to BMAD", "Square brackets"),
    ("__H1__ Introduction to BMAD", "Underscores"),
    ("BMADH1TAG Introduction to BMAD", "Text tag"),
    ("<!--H1--> Introduction to BMAD", "HTML comment"),
]

print("="*60)
print("Testando marcadores que Argos preserva")
print("="*60)

for marker_text, description in test_markers:
    translated = argostranslate.translate.translate(marker_text, 'en', 'pt')
    preserved = marker_text.split()[0] in translated
    status = '✅' if preserved else '❌'
    print(f"\n{status} {description}")
    print(f"   Input:  {marker_text}")
    print(f"   Output: {translated}")
    print(f"   Preservou marcador? {preserved}")
