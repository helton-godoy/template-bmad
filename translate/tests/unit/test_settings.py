import sys
import unittest
from unittest.mock import MagicMock, patch, mock_open

# Mocking all external dependencies to allow importing Settings/BMADTranslator
# We MUST use the SAME mock objects throughout the process
mock_yaml = MagicMock()
sys.modules['yaml'] = mock_yaml
mock_argos = MagicMock()
sys.modules['argostranslate'] = mock_argos
sys.modules['argostranslate.package'] = MagicMock()
mock_translate = MagicMock()
sys.modules['argostranslate.translate'] = mock_translate

from bmad_translate.config.settings import Settings

class TestSettings(unittest.TestCase):
    def setUp(self):
        # Reset the mock for each test
        mock_yaml.safe_load.reset_mock()

    @patch('builtins.open', new_callable=mock_open, read_data="key: value")
    @patch('pathlib.Path.exists')
    def test_init_loads_settings(self, mock_exists, mock_file):
        mock_exists.return_value = True
        mock_yaml.safe_load.return_value = {'key': 'value'}

        # We need to make sure we don't use the cached settings if any
        settings = Settings("dummy_config.yaml")

        self.assertEqual(settings.config_path, "dummy_config.yaml")
        mock_yaml.safe_load.assert_called_once()
        self.assertEqual(settings.get('key'), 'value')

    @patch('builtins.open', new_callable=mock_open, read_data="security:\n  enable_path_validation: true")
    @patch('pathlib.Path.exists')
    def test_get_security_settings(self, mock_exists, mock_file):
        mock_exists.return_value = True
        security_data = {'enable_path_validation': True, 'allowed_base_dir': '/tmp'}
        mock_yaml.safe_load.return_value = {'security': security_data}

        settings = Settings("dummy_config.yaml")
        result = settings.get_security_settings()

        self.assertEqual(result, security_data)

    @patch('builtins.open', new_callable=mock_open, read_data="")
    @patch('pathlib.Path.exists')
    def test_get_security_settings_empty(self, mock_exists, mock_file):
        mock_exists.return_value = True
        mock_yaml.safe_load.return_value = {}

        settings = Settings("dummy_config.yaml")
        result = settings.get_security_settings()

        self.assertEqual(result, {})

    @patch('builtins.open', new_callable=mock_open, read_data="translatable_keys: [a, b]")
    @patch('pathlib.Path.exists')
    def test_get_translatable_keys(self, mock_exists, mock_file):
        mock_exists.return_value = True
        keys = ['title', 'description']
        mock_yaml.safe_load.return_value = {'translatable_keys': keys}

        settings = Settings("dummy_config.yaml")
        result = settings.get_translatable_keys()

        self.assertEqual(result, keys)

    @patch('builtins.open', new_callable=mock_open, read_data="logging:\n  level: INFO")
    @patch('pathlib.Path.exists')
    def test_get_logging_settings(self, mock_exists, mock_file):
        mock_exists.return_value = True
        logging_data = {'level': 'INFO', 'format': '%(message)s'}
        mock_yaml.safe_load.return_value = {'logging': logging_data}

        settings = Settings("dummy_config.yaml")
        result = settings.get_logging_settings()

        self.assertEqual(result, logging_data)

    @patch('builtins.open', new_callable=mock_open, read_data="performance:\n  enable_cache: true")
    @patch('pathlib.Path.exists')
    def test_get_performance_settings(self, mock_exists, mock_file):
        mock_exists.return_value = True
        perf_data = {'enable_cache': True, 'cache_size_mb': 100}
        mock_yaml.safe_load.return_value = {'performance': perf_data}

        settings = Settings("dummy_config.yaml")
        result = settings.get_performance_settings()

        self.assertEqual(result, perf_data)

    @patch('builtins.open', new_callable=mock_open, read_data="translation:\n  target_language: es")
    @patch('pathlib.Path.exists')
    def test_get_translation_settings(self, mock_exists, mock_file):
        mock_exists.return_value = True
        trans_data = {'target_language': 'es', 'output_suffix': '_es'}
        mock_yaml.safe_load.return_value = {'translation': trans_data}

        settings = Settings("dummy_config.yaml")
        result = settings.get_translation_settings()

        self.assertEqual(result, trans_data)

if __name__ == '__main__':
    unittest.main()
