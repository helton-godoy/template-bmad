#!/usr/bin/env python3
"""
Debug detalhado para múltiplos níveis
"""

import re
import argostranslate.translate

# Simula proteção de vários níveis
text = """# Main Title
## Secondary Title
### Third Level"""

print("ORIGINAL:")
print(text)
print("\n" + "="*60 + "\n")

header_replacements = {}
def protect_headers(match):
    level = len(match.group(1))
    print(f"Protecting: '{match.group(0)}' -> Level {level}")
    header_replacements[f"[H{level}]"] = match.group(1)
    result = f"[H{level}] {match.group(2)}"
    print(f"  Result: '{result}'")
    return result

protected = re.sub(r'^(#{1,6})\s+(.+)$', protect_headers, text, flags=re.MULTILINE)
print(f"\nPROTECTED:")
print(protected)
print(f"\nReplacements: {header_replacements}")
print("\n" + "="*60 + "\n")

# Traduz
translated = argostranslate.translate.translate(protected, 'en', 'pt')
print("TRANSLATED:")
print(translated)
print("\n" + "="*60 + "\n")

# Restaura
def restore_headers(match):
    marker = match.group(1)
    content = match.group(2)
    hashes = header_replacements.get(f"[{marker}]", '#')
    print(f"Restoring: [{marker}] '{content}' -> '{hashes} {content}'")
    return f"{hashes} {content}"

restored = re.sub(r'\[(H\d)\]\s*(.+)$', restore_headers, translated, flags=re.MULTILINE)
print("\nRESTORED:")
print(restored)
