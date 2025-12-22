#!/usr/bin/env python3
"""
Debug detalhado da proteção de hashtags
"""

import re

text = "# Introduction to BMAD Translator"

print(f"Original: {text}\n")

# Simula a proteção
header_replacements = {}
def protect_headers(match):
    level = len(match.group(1))
    print(f"  Match found! Groups: {match.groups()}")
    print(f"    Group 1 (hashtags): '{match.group(1)}' (len={level})")
    print(f"    Group 2 (content): '{match.group(2)}'")
    header_replacements[f"⟨H{level}⟩"] = match.group(1)
    result = f"⟨H{level}⟩{match.group(2)}"
    print(f"    Replacement: '{result}'")
    return result

protected = re.sub(r'^(#{1,6})\s+(.+)$', protect_headers, text, flags=re.MULTILINE)
print(f"\nProtected: {protected}")
print(f"Header replacements: {header_replacements}\n")

# Simula Argos (só traduz o texto, mantém marcadores)
import argostranslate.translate
translated = argostranslate.translate.translate(protected, 'en', 'pt')
print(f"Após Argos: {translated}\n")

# Simula restauração
def restore_headers(match):
    print(f"  Restore match! Groups: {match.groups()}")
    marker = match.group(1)
    content = match.group(2)
    hashes = header_replacements.get(marker, '# ')
    print(f"    Marker: {marker}, Hashes: {hashes}, Content: {content}")
    result = f"{hashes} {content}"
    print(f"    Result: {result}")
    return result

restored = re.sub(r'⟨(H\d)⟩\s*(.+)$', restore_headers, translated, flags=re.MULTILINE)
print(f"\nRestored: {restored}")
