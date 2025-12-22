# BMAD Translation Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Template completo para tradução de documentação usando o método BMAD (Business Model Agile Development), com sistema anti-loop para agentes LLM e ferramentas de automação.

## 🎯 Características Principais

- ✅ **Sistema de Estado Persistente** - Rastreia arquivos processados e previne loops
- ✅ **Interface Makefile** - Comandos centralizados e intuitivos
- ✅ **Prevenção de Loops** - Sistema anti-loop para agentes LLM
- ✅ **Análise de Traduções** - Ferramentas de análise e relatórios
- ✅ **Validação Automática** - Validação de qualidade e completude
- ✅ **Documentação Completa** - Guias para desenvolvedores e agentes LLM

## 🚀 Quick Start

```bash
# 1. Clonar repositório
git clone https://github.com/helton-godoy/template-bmad.git
cd template-bmad

# 2. Ver status do projeto
make status

# 3. Ver todos os comandos disponíveis
make help

# 4. Instalar dependências
make install

# 5. Analisar traduções
make analyze
```

## 📁 Estrutura do Projeto

```
template-bmad/
├── Makefile                    # ⭐ Interface principal
├── AGENTS.md                   # 🤖 Guia para agentes LLM
├── translate/                  # 📦 Módulo de tradução
│   ├── scripts/                # Scripts organizados
│   │   ├── validation/         # Validação
│   │   ├── analysis/           # Análise
│   │   ├── correction/         # Correções
│   │   └── utils/              # Utilitários
│   ├── src/                    # Código fonte
│   ├── tests/                  # Testes
│   └── docs/                   # Documentação
├── config/                     # Configurações
└── data/                       # Dados e estado
```

## 💻 Comandos Principais

### Status e Informações

```bash
make status          # Status completo do projeto
make info            # Informações detalhadas
make help            # Lista todos os comandos
```

### Análise

```bash
make analyze         # Análise de traduções
make analyze-report  # Relatório completo
make analyze-csv     # Exportar para CSV
make unprocessed     # Listar não processados
```

### Validação

```bash
make validate        # Validação completa
make validate-install # Validar dependências
```

### Manutenção

```bash
make clean           # Limpar temporários
make clean-all       # Limpeza completa
make cache-clean     # Limpar cache
make locks-clean     # Limpar locks órfãos
```

## 🤖 Para Agentes LLM

Este projeto inclui um guia completo para agentes LLM em [`AGENTS.md`](AGENTS.md) com:

- ⚠️ **Regras Anti-Loop** - Como evitar execuções repetitivas
- 📋 **Estrutura do Projeto** - Onde encontrar cada componente
- 🛠️ **Ferramentas Disponíveis** - Comandos e scripts
- 🔄 **Fluxo de Trabalho** - Processo recomendado
- 🎯 **Checklist** - Verificações antes de agir

**Leia [`AGENTS.md`](AGENTS.md) antes de trabalhar no projeto!**

## 📚 Documentação

- **README Principal**: [`translate/docs/README.md`](translate/docs/README.md)
- **Guia para Agentes**: [`AGENTS.md`](AGENTS.md)
- **Plano de Implementação**: Veja artifacts no diretório `.gemini`
- **Walkthrough**: Documentação da implementação

## 🛠️ Sistema de Estado

O projeto usa um sistema de estado persistente para rastrear:

- Arquivos processados (com checksums SHA256)
- Execuções de scripts (com timestamps)
- Resultados de validações

**Arquivo de estado**: `translate/data/state/execution_state.json`

## 🔒 Prevenção de Loops

O sistema previne loops através de:

1. **Estado Persistente** - Rastreia o que já foi processado
2. **Checksums** - Detecta mudanças em arquivos
3. **Timestamps** - Evita reexecuções recentes
4. **Locks** - Previne execuções simultâneas

## 📊 Análise de Traduções

```bash
# Estatísticas gerais
make analyze

# Relatório completo em Markdown
make analyze-report

# Exportar dados para CSV
make analyze-csv

# Listar arquivos não processados
make unprocessed
```

## 🧪 Testes

```bash
# Testar sistema de estado
make test-state

# Testar sistema de locks
make test-locks

# Executar todos os testes
make test
```

## 📦 Dependências

- Python 3.8+
- Bash 4.0+
- jq
- parallel (opcional)
- argostranslate

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Helton Godoy**

- GitHub: [@helton-godoy](https://github.com/helton-godoy)

## 🙏 Agradecimentos

- Projeto BMAD (Business Model Agile Development)
- Comunidade de tradução open source
- Contribuidores e testadores

---

**⭐ Se este projeto foi útil, considere dar uma estrela!**
