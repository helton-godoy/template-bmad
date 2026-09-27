import pytest
import re
from bmad_translate.core.linter import Linter

@pytest.mark.unit
class TestLinter:
    """Testes unitários para a classe Linter."""

    def test_check_yaml_valid(self):
        """Testa YAML válido."""
        content = "name: test\nvalue: 123"
        errors = Linter.check_yaml(content)
        assert len(errors) == 0

    def test_check_yaml_invalid(self):
        """Testa YAML inválido."""
        content = "name: : test"
        errors = Linter.check_yaml(content)
        assert len(errors) > 0
        assert "Erro de sintaxe YAML" in errors[0]

    def test_check_markdown_valid(self):
        """Testa Markdown válido."""
        content = """---
title: Test
---
# Hello
**bold text**
```python
print("hi")
```
"""
        errors = Linter.check_markdown(content)
        assert len(errors) == 0

    def test_check_markdown_unclosed_frontmatter(self):
        """Testa Markdown com frontmatter não fechado."""
        content = "--- \ntitle: Test\n# Content"
        errors = Linter.check_markdown(content)
        assert any("Frontmatter não fechado" in e for e in errors)

    def test_check_markdown_invalid_frontmatter_yaml(self):
        """Testa Markdown com YAML inválido no frontmatter."""
        content = "---\ntitle: : Test\n---\n# Content"
        errors = Linter.check_markdown(content)
        assert any("Frontmatter: Erro de sintaxe YAML" in e for e in errors)

    def test_check_markdown_unclosed_code_block(self):
        """Testa Markdown com bloco de código não fechado."""
        content = "# Title\n```python\nprint(1)"
        errors = Linter.check_markdown(content)
        assert any("Número ímpar de delimitadores de bloco de código" in e for e in errors)

    def test_check_markdown_invalid_bold_spacing(self):
        """Testa Markdown com espaçamento inválido em negrito."""
        # Espaço no início: ** text**
        content = "This is ** invalid** bold."
        errors = Linter.check_markdown(content)
        assert any("Espaçamento inválido em negrito detectado" in e for e in errors)

        # Espaço no fim: **text **
        content2 = "This is **invalid ** bold."
        errors = Linter.check_markdown(content2)
        assert any("Espaçamento inválido em negrito detectado" in e for e in errors)

        # Espaço em ambos: ** text **
        content3 = "This is ** invalid ** bold."
        errors = Linter.check_markdown(content3)
        assert any("Espaçamento inválido em negrito detectado" in e for e in errors)

    def test_check_markdown_multiple_errors(self):
        """Testa Markdown com múltiplos erros."""
        content = "```\n** error **"
        errors = Linter.check_markdown(content)
        assert len(errors) == 2
        assert any("Número ímpar" in e for e in errors)
        assert any("Espaçamento inválido" in e for e in errors)

    def test_lint_file_markdown(self):
        """Testa lint_file para arquivo Markdown."""
        filepath = "test.md"
        content = "# Title\n```"
        result = Linter.lint_file(filepath, content)
        assert result['file'] == filepath
        assert len(result['errors']) > 0
        assert "Número ímpar de delimitadores de bloco de código" in result['errors'][0]

    def test_lint_file_markdown_alias(self):
        """Testa lint_file para extensão .markdown."""
        filepath = "test.markdown"
        content = "---"
        result = Linter.lint_file(filepath, content)
        assert result['file'] == filepath
        assert any("Frontmatter não fechado" in e for e in result['errors'])

    def test_lint_file_yaml(self):
        """Testa lint_file para arquivo YAML."""
        filepath = "test.yaml"
        content = "key: : value"
        result = Linter.lint_file(filepath, content)
        assert result['file'] == filepath
        assert len(result['errors']) > 0
        assert "Erro de sintaxe YAML" in result['errors'][0]

    def test_lint_file_yaml_alias(self):
        """Testa lint_file para extensão .yml."""
        filepath = "test.yml"
        content = "key: : value"
        result = Linter.lint_file(filepath, content)
        assert result['file'] == filepath
        assert len(result['errors']) > 0
        assert "Erro de sintaxe YAML" in result['errors'][0]

    def test_lint_file_unsupported_extension(self):
        """Testa lint_file para extensão não suportada."""
        filepath = "test.txt"
        content = "Some content"
        result = Linter.lint_file(filepath, content)
        assert result['file'] == filepath
        assert len(result['errors']) == 0
