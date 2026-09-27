"""
Testes unitários para a classe Settings.
"""

import pytest
import yaml
import os
from pathlib import Path
from unittest.mock import patch, mock_open
from bmad_translate.config.settings import Settings

@pytest.fixture
def dummy_config_path(tmp_path):
    config = {
        'translation': {
            'target_language': 'en',
            'output_suffix': '_en',
            'max_text_length': 1000,
            'safe_chunk_size': 500
        },
        'supported_extensions': ['.md', '.txt'],
        'skip_directories': ['node_modules'],
        'translatable_keys': ['title'],
        'security': {
            'allowed_base_dir': '/tmp',
            'enable_path_validation': False,
            'enable_input_sanitization': False
        },
        'logging': {
            'level': 'DEBUG'
        },
        'performance': {
            'enable_cache': False,
            'cache_size_mb': 50,
            'translation_timeout': 10,
            'max_retries': 5
        }
    }
    config_file = tmp_path / "test_settings.yaml"
    with open(config_file, 'w') as f:
        yaml.dump(config, f)
    return str(config_file)

class TestSettings:

    def test_get_top_level(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        assert settings.get('supported_extensions') == ['.md', '.txt']

    def test_get_nested(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        assert settings.get('translation.target_language') == 'en'
        assert settings.get('security.enable_path_validation') is False

    def test_get_default_value(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        assert settings.get('non_existent', 'default') == 'default'
        assert settings.get('translation.non_existent', 'default') == 'default'

    def test_get_broken_path(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        # 'supported_extensions' is a list, not a dict
        assert settings.get('supported_extensions.something', 'default') == 'default'

    def test_get_translation_settings(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        ts = settings.get_translation_settings()
        assert ts['target_language'] == 'en'

    def test_get_supported_extensions(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        assert settings.get_supported_extensions() == ['.md', '.txt']

    def test_get_skip_directories(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        assert settings.get_skip_directories() == ['node_modules']

    def test_get_translatable_keys(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        assert settings.get_translatable_keys() == ['title']

    def test_get_security_settings(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        ss = settings.get_security_settings()
        assert ss['allowed_base_dir'] == '/tmp'

    def test_get_logging_settings(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        ls = settings.get_logging_settings()
        assert ls['level'] == 'DEBUG'

    def test_get_performance_settings(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        ps = settings.get_performance_settings()
        assert ps['max_retries'] == 5

    def test_value_getters(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        assert settings.get_target_language() == 'en'
        assert settings.get_output_suffix() == '_en'
        assert settings.get_max_text_length() == 1000
        assert settings.get_safe_chunk_size() == 500
        assert settings.get_allowed_base_dir() == '/tmp'
        assert settings.is_path_validation_enabled() is False
        assert settings.is_input_sanitization_enabled() is False
        assert settings.is_cache_enabled() is False
        assert settings.get_cache_size_mb() == 50
        assert settings.get_translation_timeout() == 10
        assert settings.get_max_retries() == 5

    def test_update_setting(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        settings.update_setting('translation.target_language', 'fr')
        assert settings.get_target_language() == 'fr'

        settings.update_setting('new.nested.key', 'value')
        assert settings.get('new.nested.key') == 'value'

    def test_save_and_reload(self, dummy_config_path, tmp_path):
        settings = Settings(dummy_config_path)
        save_path = str(tmp_path / "saved_settings.yaml")
        settings.update_setting('translation.target_language', 'es')
        settings.save_settings(save_path)

        new_settings = Settings(save_path)
        assert new_settings.get_target_language() == 'es'

        settings.update_setting('translation.target_language', 'it')
        settings.save_settings(save_path)
        new_settings.reload()
        assert new_settings.get_target_language() == 'it'

    def test_init_default_path(self):
        with patch.object(Settings, '_get_default_config_path', return_value='fake_default.yaml'):
            with patch('builtins.open', mock_open(read_data='key: value')):
                settings = Settings()
                assert settings.config_path == 'fake_default.yaml'
                assert settings.get('key') == 'value'

    def test_load_settings_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            Settings('non_existent_file.yaml')

    def test_load_settings_yaml_error(self, tmp_path):
        bad_yaml = tmp_path / "bad.yaml"
        bad_yaml.write_text("invalid: yaml: :")
        with pytest.raises(ValueError, match="Erro ao processar arquivo YAML"):
            Settings(str(bad_yaml))

    def test_repr(self, dummy_config_path):
        settings = Settings(dummy_config_path)
        assert f"Settings(config_path='{dummy_config_path}')" in repr(settings)
