#!/usr/bin/env python3
"""
Testa cada regex individualmente para identificar qual está removendo o espaço.
"""

import re

text_inicial = "Valorizamos **precisão** e **qualidade**."
print(f"INICIAL: {text_inicial}\n")

# Linha 277
text1 = re.sub(r'(\*\*|__)\s+([^\s].*?)\s+\1', r'\1\2\1', text_inicial)
print(f"Linha 277 (remove espaços DENTRO):  {text1}")

# Linha 280
text2 = re.sub(r'([^\s*])(\*|_)\s+([^\s].*?)\s+\2', r'\1\2\3\2', text1)
print(f"Linha 280 (itálico):                {text2}")

# Linha 284  
text3 = re.sub(r'(?:^|(?<=\s))\*\*\s+', '**', text2)
print(f"Linha 284 (abertura extra):         {text3}")

# Linha 289 (MODIFICADA)
text4 = re.sub(r'(?<=\S)\s+\*\*(?=[.,!?:;]|$|\*\*)', '**', text3)
print(f"Linha 289 (fechamento antes pont):  {text4}")

# Teste: Essa é a ORIGINAL que está quebrando
text_original_288 = re.sub(r'(?<=\S)\s+\*\*(?=[\s.,!?:;]|$)', '**', text_inicial)
print(f"\nORIGINAL linha 288:                  {text_original_288}")

# Vamos testar se "e" está sendo capturado
import sys
print(f"\nCaractere após '** ': '{text_inicial[25]}' (ord={ord(text_inicial[25])})")
print(f"Está em [\\s.,!?:;]? {text_inicial[25] in ' .,!?:;'}")
