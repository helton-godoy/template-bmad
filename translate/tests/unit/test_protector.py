import sys
from unittest.mock import MagicMock, patch, mock_open

import pytest
from bmad_translate.core.protector import ContentProtector

class TestContentProtector:

    def test_load_protection_patterns_fallback(self):
        """Testa se os padrões de fallback são carregados em caso de erro."""
        # Patcheia o yaml dentro do módulo protector
        with patch('bmad_translate.core.protector.yaml.safe_load') as mock_safe_load:
            mock_safe_load.side_effect = Exception("YAML Error")

            with patch('bmad_translate.core.protector.Path.exists', return_value=True):
                with patch('builtins.open', mock_open(read_data="dummy content")):
                    protector = ContentProtector()
                    patterns = protector.get_patterns()

                    # Verifica se os padrões de fallback foram carregados
                    assert len(patterns) == 7
                    assert patterns[0]['description'] == 'Frontmatter YAML'

    def test_load_protection_patterns_success(self):
        """Testa o carregamento bem-sucedido de padrões de um arquivo YAML."""
        mock_data = {
            'protection_patterns': {
                'general': [
                    {'pattern': r'CUSTOM_PATTERN', 'description': 'Custom Description'}
                ]
            }
        }

        with patch('bmad_translate.core.protector.yaml.safe_load') as mock_safe_load:
            mock_safe_load.return_value = mock_data

            with patch('bmad_translate.core.protector.Path.exists', return_value=True):
                with patch('builtins.open', mock_open(read_data="yaml data")):
                    protector = ContentProtector()
                    patterns = protector.get_patterns()

                    assert len(patterns) == 1
                    assert patterns[0]['pattern'] == r'CUSTOM_PATTERN'
                    assert patterns[0]['description'] == 'Custom Description'

    def test_load_protection_patterns_mixed_structure(self):
        """Testa o carregamento de padrões com estruturas mistas no YAML."""
        mock_data = {
            'protection_patterns': {
                'list_category': [
                    {'pattern': r'P1', 'description': 'D1'},
                    {'pattern': r'P2', 'description': 'D2'}
                ],
                'dict_category': {'pattern': r'P3', 'description': 'D3'},
                'invalid_category': 'just a string'
            }
        }

        with patch('bmad_translate.core.protector.yaml.safe_load') as mock_safe_load:
            mock_safe_load.return_value = mock_data

            with patch('bmad_translate.core.protector.Path.exists', return_value=True):
                with patch('builtins.open', mock_open(read_data="yaml data")):
                    protector = ContentProtector()
                    patterns = protector.get_patterns()

                    assert len(patterns) == 3
                    descriptions = [p['description'] for p in patterns]
                    assert 'D1' in descriptions
                    assert 'D2' in descriptions
                    assert 'D3' in descriptions

    def test_load_protection_patterns_file_not_found(self):
        """Testa se os padrões de fallback são carregados quando o arquivo não existe."""
        with patch('bmad_translate.core.protector.Path.exists', return_value=False):
            protector = ContentProtector()
            patterns = protector.get_patterns()

            assert len(patterns) == 7
            assert patterns[0]['description'] == 'Frontmatter YAML'
