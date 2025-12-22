#!/usr/bin/env python3
"""
Rastrea passo-a-passo onde quebras de linha são perdidas
"""

import sys
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'src'))

from bmad_translate.core.translator import BMADTranslator
from bmad_translate.config.settings import Settings
import argostranslate.translate

test = """**[Link](./path.md)** - Description

**Quick Links:**"""

print("="*60)
print("RASTREIO PASSO-A-PASSO")
print("="*60)

translator = BMADTranslator(Settings())

print(f"\n1. ORIGINAL:\n{repr(test)}\n")

# Passo 2: Proteção de hashtags
header_replacements = {}
def protect_headers(match):
    level = len(match.group(1))
    header_replacements[f"[H{level}]"] = match.group(1)
    return f"[H{level}] {match.group(2)}"

protected_headers = re.sub(r'^(#{1,6})\s+(.+)$', protect_headers, test, flags=re.MULTILINE)
print(f"2. APÓS PROTEÇÃO HEADERS:\n{repr(protected_headers)}\n")

# Passo 3: Preparação (guillemets)
prepped = re.sub(r'(\*\*|__)(?=[^\s])(.+?)(?<=[^\s])\1', r'«\2»', protected_headers)
print(f"3. APÓS PREP (** -> «»):\n{repr(prepped)}\n")

# Passo 4: Tradução
translated = argostranslate.translate.translate(prepped, 'en', 'pt')
print(f"4. APÓS ARGOS:\n{repr(translated)}\n")

# Passo 5: Restauração títulos
def restore_headers(match):
    marker_level = match.group(1)
    content = match.group(2)
    marker_key = f"[{marker_level}]"
    hashes = header_replacements.get(marker_key, '#')
    return f"{hashes} {content}"

restored_headers = re.sub(r'\[(H\d)\]\s*(.+)$', restore_headers, translated, flags=re.MULTILINE)
print(f"5. APÓS RESTAURAÇÃO HEADERS:\n{repr(restored_headers)}\n")

# Passo 6: Restauração guillemets
restored_bold = re.sub(r'«(.+?)»', r'**\1**', restored_headers)
print(f"6. APÓS RESTAURAÇÃO GUILLEMETS:\n{repr(restored_bold)}\n")

# Passo 7: Fix markdown spacing
final = translator._fix_markdown_spacing(restored_bold)
print(f"7. APÓS _fix_markdown_spacing:\n{repr(final)}\n")

print("="*60)
if '\n\n' in test and '\n\n' not in final:
    print("❌ QUEBRA PERDIDA!")
    # Encontrar em qual passo
    steps = [test, protected_headers, prepped, translated, restored_headers, restored_bold, final]
    for i in range(len(steps)-1):
        if '\n\n' in steps[i] and '\n\n' not in steps[i+1]:
            print(f"   Perdida entre passo {i+1} e {i+2}")
            break
else:
    print("✅ QUEBRAS PRESERVADAS")
