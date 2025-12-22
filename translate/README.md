# BMAD Translation System

Um sistema completo de tradução offline para documentação BMAD, com suporte a Markdown, YAML, JSON e TOML.

## 🚀 Características

- **Tradução Offline**: Usa Argos Translate para tradução local sem dependência de internet
- **Proteção de Conteúdo**: Preserva código técnico, URLs, metadados e estruturas
- **Refinamento Gramatical**: Integração com LanguageTool para correção pós-tradução
- **Múltiplos Formatos**: Suporte nativo para Markdown, YAML, JSON e TOML
- **Segurança**: Validação de path traversal e sanitização de input
- **Configuração Flexível**: Arquivos YAML para configurações personalizadas
- **Logging Estruturado**: Logs detalhados com filtro de segurança
- **Validação**: Verificação automática de integridade de arquivos

 📋 **Índice:**

- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso Rápido](#uso-rápido)
- [API Reference](#api-reference)
- [Configurações Avançadas](#configurações-avançadas)
- [Desenvolvimento](#desenvolvimento)
- [Troubleshooting](#troubleshooting)

## 🛠️ Instalação

### Pré-requisitos

- Python 3.8+
- Java Runtime Environment (para LanguageTool)
- Git

### Setup Automatizado

#### Linux/macOS

```bash
# Execute o script de setup
./setup_linux.sh
```

#### Windows

```powershell
# Execute o script PowerShell
.\setup_windows.ps1
```

### Setup Manual

1. **Crie ambiente virtual**

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate  # Windows
```

1. **Instale dependências**

```bash
pip install -r requirements.txt
```

1. **Baixe modelos de tradução**

```bash
python scripts/warmup_models.py
```

## ⚙️ Configuração

O sistema usa arquivos YAML no diretório `config/` para configuração:

### Arquivos de Configuração

- `config/default_settings.yaml` - Configurações principais
- `config/protection_patterns.yaml` - Padrões de proteção de conteúdo
- `config/language_mappings.yaml` - Mapeamentos de idiomas

### Configurações Principais

```yaml
# config/default_settings.yaml
translation:
  target_language: "pt"           # Idioma de destino
  output_suffix: "_pt-br"          # Sufixo para arquivos traduzidos
  max_text_length: 5000             # Tamanho máximo por tradução
  safe_chunk_size: 3000             # Tamanho ideal do batch

security:
  enable_path_validation: true        # Validação de segurança
  enable_input_sanitization: true    # Sanitização de input

logging:
  level: "INFO"                     # Nível de log
  enable_secure_filter: true         # Filtro de segurança
```

## 🚀 Uso Rápido

### Interface de Linha de Comando

```bash
# Traduz um diretório completo
python -m bmad_translate.cli translate-all

# Gera manifests localizados
python -m bmad_translate.cli generate

# Ativa idioma português
python -m bmad_translate.cli activate

# Restaura idioma original
python -m bmad_translate.cli restore
```

### Uso Programático

```python
from bmad_translate import BMADTranslator, Settings

# Configurações personalizadas
settings = Settings()
settings.update_setting('translation.target_language', 'pt')

# Inicializa tradutor
translator = BMADTranslator(settings)

# Traduz um arquivo
result = translator.translate_file('docs/guide.md')
if result.success:
    print(f"Traduzido: {result.target_file}")
else:
    print(f"Erro: {result.error_message}")

# Traduz diretório completo
results = translator.translate_directory('docs/')
for result in results:
    if result.success:
        print(f"✓ {result.source_file} -> {result.target_file}")
    else:
        print(f"✗ {result.source_file}: {result.error_message}")
```

### Refinamento de Tradução

```python
from bmad_translate import BMADRefiner

with BMADRefiner() as refiner:
    # Refina um arquivo
    modified = refiner.refine_file('docs/guide_pt-br.md')
    
    # Refine diretório completo
    results = refiner.refine_directory('docs/')
```

## 📚 API Reference

### BMADTranslator

Classe principal para tradução de arquivos.

**Métodos:**

```python
def translate_file(filepath: str) -> TranslationResult:
    """Traduz um único arquivo."""
    
def translate_directory(base_dir: str = '.') -> List[TranslationResult]:
    """Traduz todos os arquivos em um diretório."""
    
def collect_files(base_dir: str = '.') -> List[str]:
    """Coleta arquivos suportados para tradução."""
```

#### TranslationResult

```python
@dataclass
class TranslationResult:
    success: bool                     # Se a tradução foi bem-sucedida
    source_file: str                  # Caminho do arquivo original
    target_file: str                  # Caminho do arquivo traduzido
    error_message: Optional[str]        # Mensagem de erro (se aplicável)
    placeholders_count: int            # Número de placeholders protegidos
    content_length: int               # Tamanho do conteúdo traduzido
```

### BMADRefiner

Classe para refinamento gramatical de traduções.

**Métodos:**

```python
def refine_file(filepath: str) -> bool:
    """Refina um arquivo traduzido."""
    
def refine_directory(base_dir: str = '.') -> Dict[str, bool]:
    """Refine todos os arquivos em um diretório."""
    
def refine_text(text: str) -> str:
    """Refine um texto específico."""
```

### ContentProtector

Classe para proteção de conteúdo técnico.

**Métodos:**

```python
def protect_content(content: str) -> str:
    """Protege conteúdo substituindo padrões técnicos."""
    
def restore_content(protected_text: str) -> str:
    """Restaura placeholders originais."""
    
def add_custom_pattern(pattern: str, description: str = "") -> None:
    """Adiciona padrão de proteção personalizado."""
```

### FileValidator

Classe para validação de arquivos.

**Métodos:**

```python
def validate_file(filepath: str) -> ValidationResult:
    """Valida um arquivo específico."""
    
def validate_directory(base_dir: str = '.') -> List[ValidationResult]:
    """Valida todos os arquivos em um diretório."""
    
def get_validation_summary(results: List[ValidationResult]) -> Dict[str, Any]:
    """Gera resumo estatístico da validação."""
```

## 🔧 Configurações Avançadas

### Padrões de Proteção Personalizados

Você pode adicionar padrões personalizados de proteção:

```python
from bmad_translate import ContentProtector

protector = ContentProtector()
protector.add_custom_pattern(
    r'CUSTOM_PATTERN_HERE',
    "Descrição do padrão personalizado"
)
```

### Mapeamento de Idiomas

Adicione novos idiomas em `config/language_mappings.yaml`:

```yaml
languages:
  fr:
    name: "Français"
    code: "fr"
    argos_code: "fr"
    languagetool_code: "fr"
    is_target: true

translation_pairs:
  en-fr:
    source: "en"
    target: "fr"
    description: "Inglês para Francês"
    supported_by: ["argos"]
```

### Configurações de Performance

```yaml
performance:
  enable_cache: true                 # Habilita cache de traduções
  cache_size_mb: 100                # Tamanho máximo do cache
  translation_timeout: 30             # Timeout em segundos
  max_retries: 3                    # Número máximo de tentativas
```

## 🧪 Testes

### Executar Suite de Testes

```bash
# Instale dependências de desenvolvimento
pip install -r requirements-dev.txt

# Execute todos os testes
pytest tests/

# Execute com coverage
pytest tests/ --cov=src/bmad_translate --cov-report=html

# Execute testes específicos
pytest tests/unit/test_translator.py
pytest tests/integration/test_workflow.py
```

### Estrutura de Testes

```shell
tests/
├── unit/                    # Testes unitários
│   ├── test_translator.py
│   ├── test_refiner.py
│   └── test_protector.py
├── integration/             # Testes de integração
│   └── test_workflow.py
├── fixtures/               # Arquivos de teste
│   ├── sample.md
│   ├── sample.yaml
│   └── expected_results/
└── performance/            # Testes de performance
    └── test_large_files.py
```

## 🏗️ Desenvolvimento

### Estrutura do Projeto

```shell
translate/
├── src/bmad_translate/        # Código fonte
│   ├── core/                # Módulos principais
│   ├── cli/                 # Interface de linha de comando
│   ├── config/              # Gerenciamento de configurações
│   └── models/              # Gerenciamento de modelos
├── config/                  # Arquivos de configuração
├── scripts/                 # Scripts utilitários
├── tests/                   # Suite de testes
├── docs/                    # Documentação técnica
└── data/                    # Dados e cache
    ├── models/              # Modelos baixados
    ├── cache/               # Cache temporário
    └── logs/                # Logs do sistema
```

### Contribuindo

1. **Fork** o projeto
2. **Crie branch** para sua feature: `git checkout -b feature/nova-funcionalidade`
3. **Faça commit** das mudanças: `git commit -am 'Adiciona nova funcionalidade'`
4. **Push** para o branch: `git push origin feature/nova-funcionalidade`
5. **Abra Pull Request**

### Código de Conduta

- Seja respeitoso e inclusivo
- Forneça feedback construtivo
- Mantenha a documentação atualizada
- Siga as convenções de código do projeto

## 🔍 Troubleshooting

### Problemas Comuns

#### Erro: "LanguageTool não disponível"

**Solução**: Instale Java Runtime Environment

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install default-jre

# macOS com Homebrew
brew install openjdk

# Windows
# Baixe e instale Java Runtime Environment
```

#### Erro: "Pacote de idioma não encontrado"

**Solução**: Execute o warmup de modelos

```bash
python scripts/warmup_models.py
```

#### Erro: "Path Traversal detectado"

**Solução**: Verifique se está tentando acessar arquivos fora do diretório permitido nas configurações de segurança.

#### Performance lenta

**Solução**: Ajuste as configurações de performance:

```yaml
performance:
  safe_chunk_size: 1500          # Reduza o tamanho do chunk
  enable_cache: true             # Habilite cache
  translation_timeout: 60          # Aumente o timeout
```

### Logs e Debug

Habilite logging detalhado:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Ou via configuração
settings.update_setting('logging.level', 'DEBUG')
```

### Logs Importantes

- `data/logs/translation.log` - Logs principais de tradução
- `data/logs/errors.log` - Logs de erro específicos
- `translate_secure.log` - Logs com filtro de segurança

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Suporte

- **Issues**: [GitHub Issues](https://github.com/your-org/bmad-translate/issues)
- **Discussões**: [GitHub Discussions](https://github.com/your-org/bmad-translate/discussions)
- **Documentação**: [Wiki do Projeto](https://github.com/your-org/bmad-translate/wiki)

## 🎯 Roadmap

- [ ] Suporte a mais idiomas
- [ ] Interface web
- [ ] Plugin para VS Code
- [ ] Integração com CI/CD
- [ ] Métricas de qualidade de tradução
- [ ] Cache distribuído
- [ ] API REST

---

**BMAD Translation System** - Tradução inteligente para documentação técnica 🚀
