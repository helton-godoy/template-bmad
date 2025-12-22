#!/usr/bin/env python3
"""
Script de debug para rastrear conversão de guillemets.
"""

import sys
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'src'))

from bmad_translate.core.translator import BMADTranslator
from bmad_translate.config.settings import Settings

def step_by_step_translation(text):
    """Traduz texto mostrando cada passo."""
    print(f"\n{'='*60}")
    print(f"PASSO A PASSO: {text[:50]}...")
    print(f"{'='*60}\n")
    
    translator = BMADTranslator(Settings())
    
    # Passo 1: Preparação (guillemets)
    prepped = re.sub(r'(\*\*|__)(?=[^\s])(.+?)(?<=[^\s])\1', r'«\2»', text)
    print(f"1. Após prep (** -> «»):\n   {prepped}\n")
    
    # Passo 2: Tradução
    import argostranslate.translate
    translated = argostranslate.translate.translate(prepped, 'en', 'pt')
    print(f"2. Após tradução Argos:\n   {translated}\n")
    
    # Passo 3: Restauração (linhas 250-252)
    restored_italic = re.sub(r'‹(.+?)›', r'*\1*', translated)
    restored_bold = re.sub(r'«(.+?)»', r'**\1**', restored_italic)
    print(f"3. Após restauração (« -> **):\n   {restored_bold}\n")
    
    # Passo 4: Fix markdown spacing
    final = translator._fix_markdown_spacing(restored_bold)
    print(f"4. Após _fix_markdown_spacing:\n   {final}\n")
    
    return final

# Teste
result = step_by_step_translation("We value **precision** and **quality**.")
print(f"\nRESULTADO FINAL: {result}")
