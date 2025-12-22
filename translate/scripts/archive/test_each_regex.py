#!/usr/bin/env python3
"""
Testa cada regex de _fix_markdown_spacing individualmente
"""

import re

text = '**[Link](./path.md)** - Descrição\n\n**Links rápidos:**'

print("ORIGINAL:")
print(repr(text))
print("\n" + "="*60 + "\n")

# Linha 301 - Bold interno
result1 = re.sub(r'(\*\*|__)\s+([^\s*](?:(?!\*\*|__).)*?[^\s*])\s+\1', r'\1\2\1', text)
print(f"Linha 301 (bold interno):\n{repr(result1)}")
print(f"Quebra OK? {'\n\n' in result1}\n")

# Linha 304 - Itálico
result2 = re.sub(r'([^\s*])(\*|_)\s+([^\s].*?)\s+\2', r'\1\2\3\2', result1)
print(f"Linha 304 (itálico):\n{repr(result2)}")
print(f"Quebra OK? {'\n\n' in result2}\n")

# Linha 308 - Abertura bold
result3 = re.sub(r'(?:^|(?<=\s))\*\*\s+', '**', result2)
print(f"Linha 308 (abertura bold):\n{repr(result3)}")
print(f"Quebra OK? {'\n\n' in result3}\n")

# Linha 313 - Fechamento bold (CORRIGIDA)
result4 = re.sub(r'(?<=\S)[ ]+\*\*(?=[.,!?:;]|$|\*\*)', '**', result3)
print(f"Linha 313 (fechamento bold - corrigida):\n{repr(result4)}")
print(f"Quebra OK? {'\n\n' in result4}\n")

# Linha 316 - Links
result5 = re.sub(r'\[\s+(.*?)\s+\]', r'[\1]', result4)
print(f"Linha 316 (links):\n{repr(result5)}")
print(f"Quebra OK? {'\n\n' in result5}\n")

print("="*60)
if '\n\n' not in result5:
    print("❌ QUEBRA PERDIDA!")
    # Encontrar qual regex causou
    results = [text, result1, result2, result3, result4, result5]
    for i in range(len(results)-1):
        if '\n\n' in results[i] and '\n\n' not in results[i+1]:
            linha = [301, 304, 308, 313, 316][i]
            print(f"   Culpado: Linha {linha}")
            print(f"   Antes:  {repr(results[i])}")
            print(f"   Depois: {repr(results[i+1])}")
            break
else:
    print("✅ TODAS AS QUEBRAS PRESERVADAS!")
