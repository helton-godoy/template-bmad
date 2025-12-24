"""
Testes unitários para o BMADTranslator
"""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import Mock, patch

from bmad_translate.core.translator import BMADTranslator, TranslationResult
from bmad_translate.config.settings import Settings


@pytest.mark.unit
class TestBMADTranslator:
    """Testes unitários para BMADTranslator."""
    
    def test_init_with_default_settings(self):
        """Testa inicialização com configurações padrão."""
        translator = BMADTranslator()
        
        assert translator.settings is not None
        assert translator.protector is not None
        assert translator.logger is not None
        assert not translator._argos_initialized
    
    def test_init_with_custom_settings(self, test_settings):
        """Testa inicialização com configurações personalizadas."""
        translator = BMADTranslator(test_settings)
        
        assert translator.settings == test_settings
        assert translator.settings.get_target_language() == 'pt'
    
    def test_validate_path_valid(self, temp_dir):
        """Testa validação de path válido."""
        translator = BMADTranslator()
        
        # Cria um arquivo de teste
        test_file = temp_dir / "test.md"
        test_file.write_text("# Test")
        
        validated_path = translator._validate_path(str(test_file))
        assert validated_path == str(test_file.resolve())
    
    def test_validate_path_invalid(self, temp_dir):
        """Testa validação de path inválido."""
        translator = BMADTranslator()
        
        # Tenta acessar arquivo fora do diretório permitido
        with pytest.raises(ValueError):
            translator._validate_path("../../../etc/passwd")
    
    def test_sanitize_input_normal(self):
        """Testa sanitização de input normal."""
        translator = BMADTranslator()
        
        text = "Este é um texto normal para traduzir."
        sanitized = translator._sanitize_input(text)
        
        assert sanitized == text
    
    def test_sanitize_input_too_long(self, test_settings):
        """Testa sanitização de input muito longo."""
        translator = BMADTranslator(test_settings)
        
        # Cria texto maior que o limite
        max_length = test_settings.get_max_text_length()
        long_text = "x" * (max_length + 100)
        
        sanitized = translator._sanitize_input(long_text)
        
        assert len(sanitized) <= max_length
    
    def test_sanitize_input_empty(self):
        """Testa sanitização de input vazio."""
        translator = BMADTranslator()
        
        sanitized = translator._sanitize_input("")
        assert sanitized == ""
    
    def test_sanitize_input_null_bytes(self):
        """Testa sanitização de input com null bytes."""
        translator = BMADTranslator()
        
        text = "Texto\x00com\x00null\x00bytes"
        sanitized = translator._sanitize_input(text)
        
        assert "\x00" not in sanitized
    
    @patch('bmad_translate.core.translator.argostranslate.translate.translate')
    def test_translate_text_success(self, mock_translate, test_settings):
        """Testa tradução de texto com sucesso."""
        mock_translate.return_value = "Texto traduzido"
        
        translator = BMADTranslator(test_settings)
        translator._argos_initialized = True
        
        result = translator._translate_text("Text to translate")
        
        assert result == "Texto traduzido"
        mock_translate.assert_called_once_with("Text to translate", 'en', 'pt')
    
    def test_translate_text_empty(self, test_settings):
        """Testa tradução de texto vazio."""
        translator = BMADTranslator(test_settings)
        translator._argos_initialized = True
        
        result = translator._translate_text("")
        assert result == ""
    
    def test_translate_text_error_fallback(self, test_settings):
        """Testa fallback em caso de erro na tradução."""
        translator = BMADTranslator(test_settings)
        translator._argos_initialized = True
        
        # Simula erro
        with patch('bmad_translate.core.translator.argostranslate.translate.translate',
                  side_effect=Exception("Erro de tradução")):
            result = translator._translate_text("Original text")
            
            # Deve retornar o texto original em caso de erro
            assert result == "Original text"
    
    def test_collect_files(self, temp_dir, test_settings):
        """Testa coleta de arquivos."""
        translator = BMADTranslator(test_settings)
        
        # Cria arquivos de teste
        files = {
            "test.md": "# Test Markdown",
            "test.yaml": "name: test",
            "test.json": '{"key": "value"}',
            "test.txt": "Not supported",
            "ignore.py": "# Should be ignored",
            "subdir/test2.md": "# Subdir file"
        }
        
        for filename, content in files.items():
            if "/" in filename:
                # Cria subdiretório
                subdir = temp_dir / filename.split("/")[0]
                subdir.mkdir(exist_ok=True)
                file_path = subdir / filename.split("/")[1]
            else:
                file_path = temp_dir / filename
            file_path.write_text(content)
        
        collected = translator.collect_files(str(temp_dir))
        
        # Deve coletar apenas arquivos suportados e não ignorados
        collected_names = [os.path.basename(f) for f in collected]
        
        assert "test.md" in collected_names
        assert "test.yaml" in collected_names
        assert "test.json" in collected_names
        assert "test.txt" not in collected_names  # Não suportado
        assert "ignore.py" not in collected_names  # Ignorado
        assert len(collected) >= 4  # Pelo menos os arquivos suportados
    
    def test_has_translatable_content_true(self):
        """Testa detecção de conteúdo traduzível (verdadeiro)."""
        translator = BMADTranslator()
        
        # Configura placeholders vazios
        translator.protector.placeholders = {}
        
        paragraph = "This is a normal paragraph with translatable content."
        result = translator._has_translatable_content(paragraph)
        
        assert result is True
    
    def test_has_translatable_content_false_empty(self):
        """Testa detecção de conteúdo traduzível (falso - vazio)."""
        translator = BMADTranslator()
        translator.protector.placeholders = {}
        
        paragraph = ""
        result = translator._has_translatable_content(paragraph)
        
        assert result is False
    
    def test_has_translatable_content_false_placeholder_only(self):
        """Testa detecção de conteúdo traduzível (falso - apenas placeholder)."""
        translator = BMADTranslator()
        
        # Configura placeholder
        translator.protector.placeholders = {"__BMAD_P_0__": "protected content"}
        
        paragraph = "__BMAD_P_0__"
        result = translator._has_translatable_content(paragraph)
        
        assert result is False
    
    def test_recursive_translate_data_dict(self, test_settings):
        """Testa tradução recursiva de dicionário."""
        translator = BMADTranslator(test_settings)
        translator._argos_initialized = True
        
        with patch.object(translator, '_translate_text', return_value="Traduzido") as mock_translate:
            data = {
                "title": "Original Title",
                "description": "Original Description", 
                "code": "not_translatable",
                "nested": {
                    "name": "Nested Name"
                }
            }
            
            result = translator._recursive_translate_data(data)
            
            # Campos traduzíveis devem ser traduzidos
            assert result["title"] == "Traduzido"
            assert result["description"] == "Traduzido"
            assert result["nested"]["name"] == "Traduzido"
            
            # Campos não traduzíveis devem ser preservados
            assert result["code"] == "not_translatable"
    
    def test_recursive_translate_data_list(self, test_settings):
        """Testa tradução recursiva de lista."""
        translator = BMADTranslator(test_settings)
        translator._argos_initialized = True
        
        with patch.object(translator, '_translate_text', return_value="Traduzido") as mock_translate:
            data = [
                {"title": "Title 1"},
                {"title": "Title 2"},
                {"not_translatable": "preserve"}
            ]
            
            result = translator._recursive_translate_data(data)
            
            # Itens com campos traduzíveis devem ser traduzidos
            assert result[0]["title"] == "Traduzido"
            assert result[1]["title"] == "Traduzido"
            assert result[2]["not_translatable"] == "preserve"
    
    def test_get_file_type(self):
        """Testa detecção de tipo de arquivo."""
        translator = BMADTranslator()
        
        assert translator._get_file_type("test.md") == "markdown"
        assert translator._get_file_type("test.yaml") == "yaml"
        assert translator._get_file_type("test.yml") == "yaml"
        assert translator._get_file_type("test.json") == "json"
        assert translator._get_file_type("test.jsonc") == "json"
        assert translator._get_file_type("test.toml") == "toml"
        assert translator._get_file_type("test.txt") == "unknown"
    
    def test_strip_json_comments(self):
        """Testa remoção de comentários JSON."""
        translator = BMADTranslator()
        
        # JSON com comentários
        json_with_comments = """{
  // Este é um comentário de linha
  "name": "test",
  /* Este é um comentário de bloco */
  "value": 123,
  "url": "https://example.com" // URL deve ser preservada
}"""
        
        cleaned = translator._strip_json_comments(json_with_comments)
        
        # Comentários devem ser removidos, URLs preservadas
        assert "//" not in cleaned
        assert "/*" not in cleaned
        assert "https://example.com" in cleaned
        assert '"name": "test"' in cleaned
    
    def test_repr(self, test_settings):
        """Testa representação string do objeto."""
        translator = BMADTranslator(test_settings)
        
        repr_str = repr(translator)
        assert "BMADTranslator" in repr_str
        assert "pt" in repr_str  # idioma alvo


@pytest.fixture
def test_settings():
    """Configurações de teste."""
    settings = Settings()
    settings.update_setting('translation.target_language', 'pt')
    settings.update_setting('translation.output_suffix', '_test')
    settings.update_setting('translation.max_text_length', 1000)
    settings.update_setting('security.enable_path_validation', False)
    return settings
