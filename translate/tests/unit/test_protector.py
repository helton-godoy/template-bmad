import sys
from unittest.mock import MagicMock

# Mock dependencies before importing the module under test
sys.modules['yaml'] = MagicMock()
sys.modules['argostranslate'] = MagicMock()
sys.modules['argostranslate.package'] = MagicMock()
sys.modules['argostranslate.translate'] = MagicMock()

import unittest
from bmad_translate.core.protector import ContentProtector

class TestContentProtector(unittest.TestCase):
    def setUp(self):
        # Limpa o estado entre os testes se necessário
        # ContentProtector carrega padrões no __init__
        self.protector = ContentProtector()

    def test_validate_patterns_default(self):
        """Testa que os padrões padrão são válidos."""
        invalid = self.protector.validate_patterns()
        self.assertEqual(len(invalid), 0, f"Padrões padrão inválidos: {invalid}")

    def test_validate_patterns_valid_custom(self):
        """Testa a validação com um padrão personalizado válido."""
        self.protector.add_custom_pattern(r'[0-9]+', "Apenas números")
        invalid = self.protector.validate_patterns()
        self.assertEqual(len(invalid), 0, "Padrão válido foi marcado como inválido")

    def test_validate_patterns_invalid_custom(self):
        """Testa a validação com um padrão personalizado inválido."""
        # Padrão com parênteses não fechado é inválido em regex
        invalid_pattern = r'(abc'
        self.protector.add_custom_pattern(invalid_pattern, "Padrão inválido")
        invalid = self.protector.validate_patterns()

        self.assertEqual(len(invalid), 1)
        self.assertIn(f"Padrão {len(self.protector.patterns)-1}", invalid[0])
        self.assertIn(invalid_pattern, invalid[0])
        self.assertIn("Erro", invalid[0])

if __name__ == '__main__':
    unittest.main()
