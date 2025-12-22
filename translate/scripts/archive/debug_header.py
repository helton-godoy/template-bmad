#!/usr/bin/env python3
"""
Debug: Rastreio de hashtag removido em títulos H1
"""

import sys
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'src'))

from bmad_translate.core.translator import BMADTranslator
from bmad_translate.config.settings import Settings
import argostranslate.translate

def test_header_translation():
    """Testa tradução de título H1."""
    print("="*60)
    print("DEBUG: Tradução de Título H1")
    print("="*60)
    
    # Texto de teste
    original = "# Introduction to BMAD Translator"
    print(f"\n1. ORIGINAL:\n   {original}\n")
    
    # Passo 1: Proteção
    translator = BMADTranslator(Settings())
    protected = translator.protector.protect_content(original)
    print(f"2. APÓS PROTEÇÃO:\n   {protected}")
    print(f"   Placeholders: {translator.protector.get_placeholders()}\n")
    
    # Passo 2: Preparação (guillemets)
    prepped = re.sub(r'(\*\*|__)(?=[^\s])(.+?)(?<=[^\s])\1', r'«\2»', protected)
    print(f"3. APÓS PREP (** -> «»):\n   {prepped}\n")
    
    # Passo 3: Tradução
    translated = argostranslate.translate.translate(prepped, 'en', 'pt')
    print(f"4. APÓS TRADUÇÃO ARGOS:\n   {translated}\n")
    
    # Passo 4: Restauração guillemets
    restored_italic = re.sub(r'‹(.+?)›', r'*\1*', translated)
    restored_bold = re.sub(r'«(.+?)»', r'**\1**', restored_italic)
    print(f"5. APÓS RESTAURAÇÃO (« -> **):\n   {restored_bold}\n")
    
    # Passo 5: Restauração proteção
    final_protected = translator.protector.restore_content(restored_bold)
    print(f"6. APÓS RESTAURAÇÃO PROTEÇÃO:\n   {final_protected}\n")
    
    # Passo 6: Fix markdown spacing
    final = translator._fix_markdown_spacing(final_protected)
    print(f"7. APÓS _fix_markdown_spacing:\n   {final}\n")
    
    print("="*60)
    print(f"RESULTADO FINAL: {final}")
    print(f"HASHTAG PRESENTE? {'✅ SIM' if final.startswith('#') else '❌ NÃO'}")
    print("="*60)

if __name__ == "__main__":
    test_header_translation()
