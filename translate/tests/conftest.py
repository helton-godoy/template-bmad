"""
Configuração do pytest para o BMAD Translation System
"""

import pytest
import sys
import tempfile
import shutil
from pathlib import Path

# Adiciona o src ao path para importar módulos
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from bmad_translate.config.settings import Settings


@pytest.fixture(scope="session")
def temp_dir():
    """Cria um diretório temporário para testes."""
    temp_path = Path(tempfile.mkdtemp())
    yield temp_path
    shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture(scope="session")
def test_settings():
    """Configurações de teste."""
    settings = Settings()
    
    # Configurações específicas para testes
    settings.update_setting('translation.target_language', 'pt')
    settings.update_setting('translation.output_suffix', '_test')
    settings.update_setting('logging.level', 'DEBUG')
    settings.update_setting('security.enable_path_validation', False)
    
    return settings


@pytest.fixture
def sample_markdown_content():
    """Conteúdo Markdown de teste."""
    return """---
title: "Test Document"
description: "This is a test document"
---

# Main Title

This is a paragraph to translate.

## Subsection

- Item 1
- Item 2
- Item 3

```python
print("Hello World")
```

[Link to Google](https://google.com)

**Bold text** and *italic text*.
"""


@pytest.fixture
def sample_yaml_content():
    """Conteúdo YAML de teste."""
    return """name: "test-project"
version: "1.0.0"
description: "A test project for translation"
type: "package"

dependencies:
  - name: "yaml"
    version: "6.0"
  - name: "json"
    version: "2.0"

metadata:
  author: "Test Author"
  license: "MIT"
"""


@pytest.fixture
def sample_json_content():
    """Conteúdo JSON de teste."""
    return """{
  "name": "test-project",
  "version": "1.0.0",
  "description": "A test project for translation",
  "type": "package",
  "dependencies": [
    {
      "name": "yaml",
      "version": "6.0"
    },
    {
      "name": "json", 
      "version": "2.0"
    }
  ],
  "metadata": {
    "author": "Test Author",
    "license": "MIT"
  }
}"""


@pytest.fixture
def expected_translated_markdown():
    """Conteúdo Markdown esperado após tradução."""
    return """---
title: "Documento de Teste"
description: "Este é um documento de teste"
---

# Título Principal

Este é um parágrafo para traduzir.

## Subseção

- Item 1
- Item 2
- Item 3

```python
print("Hello World")
```

[Link to Google](https://google.com)

**Texto em negrito** e *texto em itálico*.
"""


@pytest.fixture
def create_test_files(temp_dir):
    """Cria arquivos de teste no diretório temporário."""
    def _create_files(content_dict):
        created_files = []
        for filename, content in content_dict.items():
            file_path = temp_dir / filename
            file_path.write_text(content, encoding='utf-8')
            created_files.append(file_path)
        return created_files
    
    return _create_files


# Marcadores para testes
pytest.mark.unit = pytest.mark.unit
pytest.mark.integration = pytest.mark.integration
pytest.mark.performance = pytest.mark.performance
pytest.mark.slow = pytest.mark.slow
