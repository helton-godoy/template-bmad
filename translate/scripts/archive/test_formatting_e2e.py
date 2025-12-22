#!/usr/bin/env python3
"""
Script de teste end-to-end para validar formatação de negritos na tradução.
"""

import sys
import re
from pathlib import Path

# Adiciona o diretório src ao path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from bmad_translate.core.translator import BMADTranslator
from bmad_translate.config.settings import Settings

def test_case(description, input_text, expected_pattern):
    """Testa um caso específico de tradução."""
    print(f"\n{'='*60}")
    print(f"📝 {description}")
    print(f"{'='*60}")
    print(f"Input:  {input_text}")
    
    # Inicializa tradutor
    settings = Settings()
    translator = BMADTranslator(settings)
    
    # Traduz
    translated = translator._translate_text(input_text, from_lang='en', to_lang='pt', protect=False)
    
    print(f"Output: {translated}")
    
    # Valida padrão
    if re.search(expected_pattern, translated):
        print("✅ PASSOU - Padrão esperado encontrado")
        return True
    else:
        print(f"❌ FALHOU - Padrão esperado: {expected_pattern}")
        
        # Verifica problema específico: negritos colados
        if re.search(r'\*\*\w+\*\*[a-záéíóúâêôãõç]\*\*', translated):
            print("⚠️  Problema detectado: Negritos colados sem espaços")
        
        return False

def main():
    """Executa suite de testes."""
    print("\n" + "="*60)
    print("🧪 TESTE END-TO-END: FORMATAÇÃO DE NEGRITOS")
    print("="*60)
    
    test_cases = [
        {
            "description": "Múltiplos negritos com espaçamento normal",
            "input": "We value **precision** and **quality**.",
            "expected_pattern": r"\*\*\w+\*\*\s+\w+\s+\*\*\w+\*\*"
        },
        {
            "description": "Negrito com múltiplas palavras",
            "input": "The **production environment** is ready.",
            "expected_pattern": r"\*\*[\w\s]+\*\*"
        },
        {
            "description": "Múltiplos negritos com pontuação",
            "input": "Use **workflow**, **framework**, and **setup**.",
            "expected_pattern": r"\*\*\w+\*\*,\s+\*\*\w+\*\*,"
        },
        {
            "description": "Negrito no início da frase",
            "input": "**Important:** Read the documentation.",
            "expected_pattern": r"^\*\*\w+\*\*:"
        },
        {
            "description": "Negrito no final da frase",
            "input": "This is very **important**.",
            "expected_pattern": r"\*\*\w+\*\*\."
        },
        {
            "description": "Caso real do demo_production.md",
            "input": "This demonstration validates our commitment to **precision** and **cultural adaptation**.",
            "expected_pattern": r"\*\*\w+\*\*\s+\w+\s+\*\*[\w\s]+\*\*"
        }
    ]
    
    passed = 0
    failed = 0
    
    for test in test_cases:
        try:
            if test_case(test["description"], test["input"], test["expected_pattern"]):
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ ERRO: {str(e)}")
            failed += 1
    
    # Resumo
    print(f"\n{'='*60}")
    print(f"📊 RESUMO DOS TESTES")
    print(f"{'='*60}")
    print(f"✅ Passou: {passed}/{passed + failed}")
    print(f"❌ Falhou: {failed}/{passed + failed}")
    
    if failed > 0:
        print(f"\n⚠️  ATENÇÃO: {failed} teste(s) falharam!")
        print("Consulte translation_analysis.md para soluções propostas.")
        return 1
    else:
        print("\n🎉 Todos os testes passaram!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
