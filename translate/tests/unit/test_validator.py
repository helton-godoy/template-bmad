"""
Testes unitários para o FileValidator
"""

import pytest
import os
import json
import yaml
from pathlib import Path
from unittest.mock import Mock, patch
from bmad_translate.core.validator import FileValidator, ValidationResult, TOML_AVAILABLE
from bmad_translate.config.settings import Settings


@pytest.mark.unit
class TestFileValidator:
    """Testes unitários para FileValidator."""

    def test_init_with_default_settings(self):
        """Testa inicialização com configurações padrão."""
        validator = FileValidator()
        assert validator.settings is not None
        assert validator.logger is not None

    def test_init_with_custom_settings(self, test_settings):
        """Testa inicialização com configurações personalizadas."""
        validator = FileValidator(test_settings)
        assert validator.settings == test_settings

    def test_get_file_type(self):
        """Testa detecção de tipo de arquivo."""
        validator = FileValidator()
        assert validator._get_file_type("test.yaml") == "yaml"
        assert validator._get_file_type("test.yml") == "yaml"
        assert validator._get_file_type("test.json") == "json"
        assert validator._get_file_type("test.jsonc") == "json"
        assert validator._get_file_type("test.toml") == "toml"
        assert validator._get_file_type("test.md") == "markdown"
        assert validator._get_file_type("test.markdown") == "markdown"
        assert validator._get_file_type("test.txt") == "unknown"

    def test_validate_encoding_utf8(self, temp_dir):
        """Testa validação de codificação UTF-8."""
        validator = FileValidator()
        test_file = temp_dir / "utf8.txt"
        test_file.write_text("Texto em UTF-8", encoding="utf-8")

        is_valid, encoding, errors = validator._validate_encoding(str(test_file))
        assert is_valid is True
        assert encoding == "utf-8"
        assert not errors

    def test_validate_encoding_latin1(self, temp_dir):
        """Testa validação de codificação Latin-1."""
        validator = FileValidator()
        test_file = temp_dir / "latin1.txt"
        # "Ação" em Latin-1
        test_file.write_bytes(b"A\xe7\xe3o")

        is_valid, encoding, errors = validator._validate_encoding(str(test_file))
        assert is_valid is True
        assert encoding == "latin-1"
        assert any("codificação latin-1" in e.lower() for e in errors)

    def test_validate_yaml_valid(self, temp_dir):
        """Testa validação de YAML válido."""
        validator = FileValidator()
        test_file = temp_dir / "valid.yaml"
        content = "name: test\nversion: 1.0.0\npath: /tmp"
        test_file.write_text(content)

        is_valid, errors, warnings = validator._validate_yaml(str(test_file))
        assert is_valid is True
        assert not errors
        assert not warnings

    def test_validate_yaml_invalid(self, temp_dir):
        """Testa validação de YAML inválido."""
        validator = FileValidator()
        test_file = temp_dir / "invalid.yaml"
        content = "name: test\n  invalid: indent"
        test_file.write_text(content)

        is_valid, errors, warnings = validator._validate_yaml(str(test_file))
        assert is_valid is False
        assert any("sintaxe YAML" in e for e in errors)

    def test_check_yaml_structure_warnings(self):
        """Testa avisos de estrutura YAML."""
        validator = FileValidator()
        warnings = []
        data = {
            "name": "test",
            "long_key": "x" * 1001,
            "_private": "secret",
            "key with space": "value"
        }
        # missing: path, description, type, version
        validator._check_yaml_structure(data, warnings)

        assert any("Campos comuns ausentes" in w for w in warnings)
        assert any("Chaves com nomes suspeitos" in w for w in warnings)
        assert any("Valor muito longo" in w for w in warnings)

    def test_validate_json_valid(self, temp_dir):
        """Testa validação de JSON válido."""
        validator = FileValidator()
        test_file = temp_dir / "valid.json"
        content = '{"name": "test", "version": "1.0.0"}'
        test_file.write_text(content)

        is_valid, errors, warnings = validator._validate_json(str(test_file))
        assert is_valid is True
        assert not errors

    def test_validate_json_invalid(self, temp_dir):
        """Testa validação de JSON inválido."""
        validator = FileValidator()
        test_file = temp_dir / "invalid.json"
        content = '{"name": "test", "version": }'
        test_file.write_text(content)

        is_valid, errors, warnings = validator._validate_json(str(test_file))
        assert is_valid is False
        assert any("sintaxe JSON" in e for e in errors)

    def test_strip_json_comments(self):
        """Testa remoção de comentários em JSONC."""
        validator = FileValidator()
        content = """{
            // linha
            "a": 1, /* bloco */
            "url": "http://example.com"
        }"""
        stripped = validator._strip_json_comments(content)
        assert "// linha" not in stripped
        assert "/* bloco */" not in stripped
        assert "http://example.com" in stripped

    def test_get_json_depth(self):
        """Testa cálculo de profundidade JSON."""
        validator = FileValidator()
        data = {"a": {"b": {"c": [1, 2, 3]}}}
        assert validator._get_json_depth(data) == 3
        assert validator._get_json_depth([[[1]]]) == 3
        assert validator._get_json_depth(1) == 0

    @pytest.mark.skipif(not TOML_AVAILABLE, reason="tomllib/tomli not available")
    def test_validate_toml_valid(self, temp_dir):
        """Testa validação de TOML válido."""
        validator = FileValidator()
        test_file = temp_dir / "valid.toml"
        content = "[package]\nname = 'test'"
        test_file.write_text(content)

        is_valid, errors, warnings = validator._validate_toml(str(test_file))
        assert is_valid is True
        assert not errors

    def test_validate_markdown_valid(self, temp_dir):
        """Testa validação de Markdown válido."""
        validator = FileValidator()
        test_file = temp_dir / "valid.md"
        content = "---\ntitle: test\n---\n# Header\n[Link](http://example.com)"
        test_file.write_text(content)

        is_valid, errors, warnings = validator._validate_markdown(str(test_file))
        assert is_valid is True
        assert not errors

    def test_validate_markdown_invalid_frontmatter(self, temp_dir):
        """Testa Markdown com frontmatter inválido."""
        validator = FileValidator()
        test_file = temp_dir / "invalid_fm.md"
        content = "---\ntitle: test\n# Not closed"
        test_file.write_text(content)

        is_valid, errors, warnings = validator._validate_markdown(str(test_file))
        assert any("Frontmatter não fechado" in e for e in errors)

    def test_check_markdown_links_warnings(self):
        """Testa avisos de links Markdown."""
        validator = FileValidator()
        warnings = []
        content = "[Empty]() and [Spaces](my file.md)"
        validator._check_markdown_links(content, warnings)
        assert any("Link vazio" in w for w in warnings)
        assert any("URL com espaços" in w for w in warnings)

    def test_check_markdown_headers_warnings(self):
        """Testa avisos de pulo de nível de header."""
        validator = FileValidator()
        warnings = []
        content = "# H1\n### H3"
        validator._check_markdown_headers(content, warnings)
        assert any("Pulo de nível" in w for w in warnings)

    def test_validate_file_not_found(self):
        """Testa validação de arquivo inexistente."""
        validator = FileValidator()
        result = validator.validate_file("non_existent.yaml")
        assert result.is_valid is False
        assert "não encontrado" in result.errors[0]

    def test_validate_file_integration(self, temp_dir):
        """Testa integração do validate_file."""
        validator = FileValidator()
        test_file = temp_dir / "test.json"
        test_file.write_text('{"name": "test"}')

        result = validator.validate_file(str(test_file))
        assert result.is_valid is True
        assert result.file_type == "json"
        assert result.file_size > 0
        assert result.encoding == "utf-8"

    def test_validate_directory(self, temp_dir, test_settings):
        """Testa validação de diretório."""
        validator = FileValidator(test_settings)
        (temp_dir / "a.yaml").write_text("name: a")
        (temp_dir / "b.json").write_text('{"name": "b"}')
        (temp_dir / "c.txt").write_text("not supported")

        results = validator.validate_directory(str(temp_dir))
        # Deve encontrar a.yaml e b.json (se .yaml e .json estiverem nas extensões suportadas)
        # Settings padrão geralmente suporta yaml, json, md, toml

        found_files = [os.path.basename(r.file_path) for r in results]
        assert "a.yaml" in found_files
        assert "b.json" in found_files
        assert "c.txt" not in found_files

    def test_get_validation_summary(self):
        """Testa geração de resumo de validação."""
        validator = FileValidator()
        results = [
            ValidationResult(True, "a.yaml", "yaml", [], [], 10, "utf-8"),
            ValidationResult(False, "b.json", "json", ["Error"], [], 20, "utf-8"),
            ValidationResult(True, "c.yaml", "yaml", [], ["Warn"], 15, "utf-8"),
        ]

        summary = validator.get_validation_summary(results)
        assert summary['total_files'] == 3
        assert summary['valid_files'] == 2
        assert summary['invalid_files'] == 1
        assert summary['total_errors'] == 1
        assert summary['total_warnings'] == 1
        assert summary['by_type']['yaml']['total'] == 2
        assert summary['by_type']['json']['total'] == 1

    def test_repr(self):
        """Testa representação string."""
        validator = FileValidator()
        assert "FileValidator" in repr(validator)
