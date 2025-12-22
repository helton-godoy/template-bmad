# AGENTS.md - Guia para Agentes LLM

## 🎯 RESUMO EXECUTIVO (LEIA PRIMEIRO)

### 📋 Mapa Rápido do Projeto

- **Interface principal**: `make help` (USE SEMPRE)
- **Status completo**: `make status`
- **Localização dos scripts**: `translate/scripts/`
- **Dados de estado**: `translate/data/state/`
- **Documentação principal**: `translate/docs/README.md`
- **Configurações**: `config/` (consolidado)
- **Logs**: `logs/` (centralizado)
- **AGENTS.md principal**: Este arquivo na raiz

### 🚨 REGRA DE OURO: Makefile Primeiro

**SEMPRE** use comandos `make` antes de executar scripts Python diretamente!

- ❌ `python3 translate/scripts/analysis/analyze_translations.py`
- ✅ `make analyze`
- ❌ `python3 translate/scripts/validation/02_validate_translations.py`
- ✅ `make validate`

### 📍 ESTRUTURA ATUALIZADA (LIMPA)

### 🏠 Raiz do Projeto

```bash
/home/helton/git/template-bmad/
├── Makefile                    # ⭐ INTERFACE PRINCIPAL
├── AGENTS.md                   # 🤖 Guia para agentes LLM
├── config/                     # ⚙️ Configurações consolidadas
├── data/                       # 📊 Dados e estado
├── logs/                       # 📄 Logs centralizados
├── backups/                    # 💾 Backups do projeto
└── translate/                   # 📦 Módulo principal
```

### 📦 Módulo translate/ (ORGANIZADO)

```bash
translate/
├── scripts/               # 🛠️ Scripts organizados
│   ├── validation/         # Validação
│   ├── analysis/           # Análise
│   ├── correction/         # Correções
│   └── utils/              # Utilitários
├── src/                  # 📦 Código fonte
│   └── bmad_translate/    # Aplicação principal
├── tests/                # 🧪 Testes
├── docs/                 # 📚 Documentação
└── validation/            # 📋 Validação de qualidade
```

### 📚 Documentação Completa

```bash
translate/docs/
├── README.md                     # 📖 Documentação principal
├── development/                  # Docs de desenvolvimento
├── examples/                     # Exemplos práticos
├── guides/                       # Guias de uso
├── api/                          # API docs
└── AGENTS.md                    # 🤖 Guia para agentes LLM
```

### 📊 Resumo Final da Reorganização

- **Data**: 22/12/2025
- **Status**: ✅ ESTRUTURA LIMPA IMPLEMENTADA
- **Duplicações removidas**: 20+ diretórios
- **Logs centralizados**: Em `logs/` único
- **Configurações consolidadas**: Em `config/`
- **Documentação completa**: Técnica e para agentes

### 📑 ÍNDICE RÁPIDO

1. [Resumo Executivo](#-resumo-executivo-leia-primeiro) ⭐
2. [Estrutura Atualizada](#-estrutura-atualizada-limpa) 📍
3. [Ambiente e Setup](#-ambiente-e-setup) 🛠️
4. [Fluxo de Trabalho Padrão](#-fluxo-de-trabalho-padrão) 🔄
5. [Comandos Essenciais](#-comandos-essenciais) 💻
6. [Regras Anti-Loop](#️-regras-anti-loop-crítico) ⚠️
7. [Scripts e Ferramentas](#-scripts-e-ferramentas) 🛠️
8. [Configurações](#-configurações) ⚙️
9. [Dados e Logs](#-dados-e-logs) 📊
10. [Documentação](#-documentação) 📚
11. [Situações Comuns](#-situações-comuns) 🚨
12. [Boas Práticas](#-boas-práticas) 🎓
13. [Checklist de Verificação](#-checklist-de-verificação) 🔍
14. [Quando Consultar o Usuário](#-quando-consultar-o-usuário) 📞
15. [Resumo Rápido](#-resumo-rápido) 🎯

---

## 🎯 Propósito

Este documento fornece instruções claras para agentes LLM sobre onde encontrar informações, ferramentas e como evitar loops de execução no projeto BMAD Translation.

---

## ⚠️ REGRAS ANTI-LOOP (CRÍTICO)

### SEMPRE Faça Isso ANTES de Qualquer Ação

1. **Verifique o status atual:**

   ```bash
   make status
   # OU
   python3 translate/scripts/utils/bmad_translate_status.py
   ```

2. **Consulte arquivos não processados:**

   ```bash
   make unprocessed
   # OU
   python3 translate/scripts/utils/state_manager.py unprocessed
   ```

3. **Verifique se script foi executado recentemente:**
   - Consulte o estado em `translate/data/state/execution_state.json`
   - Use `make status` para ver últimas execuções (24h)

### NUNCA Faça Isso

- ❌ Executar o mesmo script mais de 2x seguidas sem mudanças
- ❌ Processar arquivos já marcados como processados (verifique checksum)
- ❌ Ignorar avisos de "já executado recentemente"
- ❌ Recriar lógicas que já existem em outros arquivos

### Detecção de Loops

Se você detectar que está:

- Executando o mesmo comando repetidamente
- Recebendo os mesmos resultados
- Não vendo progresso no estado

**PARE IMEDIATAMENTE** e:

1. Verifique `make status`
2. Consulte `translate/data/state/execution_state.json`
3. Pergunte ao usuário antes de continuar

---

## 📍 Estrutura Atualizada (LIMPA) {#-estrutura-atualizada-limpa}

### 🏠 Raiz do Projeto

```bash
/home/helton/git/template-bmad/
├── Makefile                    # ⭐ INTERFACE PRINCIPAL
├── AGENTS.md                   # 🤖 Guia para agentes LLM
├── config/                     # ⚙️ Configurações consolidadas
├── data/                       # 📊 Dados e estado
├── logs/                       # 📄 Logs centralizados
├── backups/                    # 💾 Backups do projeto
└── translate/                   # 📦 Módulo principal
```

### 📦 Módulo translate/ (ORGANIZADO)

```bash
translate/
├── scripts/               # 🛠️ Scripts organizados
│   ├── validation/         # Validação de qualidade
│   ├── analysis/           # Análise de traduções
│   ├── correction/         # Correções automáticas e manuais
│   └── utils/              # ⚙️ Utilitários críticos
├── src/                  # 📦 Código fonte da aplicação
│   └── bmad_translate/    # Aplicação principal BMAD
├── tests/                # 🧪 Suíte de testes
│   ├── unit/              # Testes unitários
│   ├── integration/       # Testes de integração
│   └── performance/        # Testes de performance
├── docs/                 # 📚 Documentação completa
│   ├── README.md          # Documentação principal
│   ├── development/       # Guias de desenvolvimento
│   ├── examples/          # Exemplos práticos
│   ├── guides/            # Guias de uso
│   └── api/              # Documentação da API
└── validation/            # 📋 Validação de qualidade
```

### 📚 Documentação Completa

```bash
translate/docs/
├── README.md                     # 📖 Documentação principal
├── development/                  # 🛠️ Docs de desenvolvimento
├── examples/                     # 💡 Exemplos práticos
├── guides/                       # 📋 Guias de uso
├── api/                          # 🔌 Documentação da API
└── AGENTS.md                    # 🤖 Guia para agentes LLM
```

---

## 🛠️ Ambiente e Setup {#-ambiente-e-setup}

### Setup Inicial de Sessão

```bash
# 1. Verificar ambiente (SEMPRE primeiro)
make status

# 2. Carregar variáveis de ambiente
source config/environment_vars.sh

# 3. Verificar arquivos pendentes
make unprocessed
```

### Comandos Rápidos do Dia a Dia

```bash
# Status completo
make status

# Ajuda com todos os comandos
make help

# Limpeza de cache/locks
make clean-all

# Teste do sistema
make test-state

# Ver documentação principal
make docs-view

# Ver documentação de desenvolvimento
make docs-dev

# Ver exemplos práticos
make docs-examples
```

---

## 🔄 Fluxo de Trabalho Padrão {#-fluxo-de-trabalho-padrão}

### Para Nova Sessão de Trabalho

1. **Status First**: `make status`
2. **Analisar pendências**: `make unprocessed`
3. **Decidir ação**: Baseado no status
4. **Executar**: Comando make apropriado
5. **Verificar**: `make status` novamente

### Para Análise de Traduções

```bash
# Análise rápida
make analyze

# Relatório completo
make analyze-report

# Dados para CSV
make analyze-csv
```

---

## 💻 Comandos Essenciais {#-comandos-essenciais}

### Comandos que TODO agente DEVE conhecer

| Comando | Para quê? | Quando usar? |
|---------|-------------|-------------|
| `make status` | Status completo do projeto | **SEMPRE** no início |
| `make help` | Lista todos os comandos | Quando não lembrar |
| `make unprocessed` | Lista arquivos não processados | Antes de processar |
| `make analyze` | Análise de traduções | Para estatísticas |
| `make validate` | Validação de qualidade | Para verificar qualidade |
| `make clean-all` | Limpeza completa | Quando necessário |
| `make docs-view` | Ver documentação principal | Abre translate/docs/README.md |
| `make docs-dev` | Documentação de desenvolvimento | Abre translate/docs/development/ |
| `make docs-examples` | Exemplos práticos | Abre translate/docs/examples/ |
| `make test-state` | Teste do sistema | Para verificar funcionalidades |
| `make info` | Informações do projeto | Para detalhes técnicos |

### Exemplos Práticos de Uso

```bash
# Exemplo 1: Iniciar análise de um arquivo específico
make status && make unprocessed && make analyze

# Exemplo 2: Fluxo completo de validação
make status && make validate && make status

# Exemplo 3: Limpeza e verificação
make clean-all && make status

# Exemplo 4: Acessar documentação
make docs-view  # Abre translate/docs/README.md
make docs-dev  # Abre translate/docs/development/
```

---

## ⚠️ REGRAS ANTI-LOOP (CRÍTICO) {#️-regras-anti-loop-crítico}

### VERIFICAÇÃO OBRIGATÓRIA ANTES DE QUALQUER AÇÃO

1. **make status** (SEMPRE)
2. **make unprocessed** (se for processar arquivos)
3. **Verificar execution_state.json** para execuções recentes

### SINAIS DE PERIGO - PARE IMEDIATAMENTE

- Mesmo comando repetido sem mudanças
- Mesmos resultados consecutivos
- Sem progresso no estado
- Script executado < 1 hora atrás

### PROCEDIMENTO DE EMERGÊNCIA

1. `make status`
2. `cat translate/data/state/execution_state.json`
3. Perguntar ao usuário antes de continuar

---

## 🛠️ Scripts e Ferramentas {#-scripts-e-ferramentas}

### Scripts Essenciais que TODO Agente Conhece

| Categoria | Comando Make | Script Direto | Quando Usar? |
|----------|---------------|---------------|--------------|
| **Status** | `make status` | `utils/state_manager.py` | **SEMPRE** primeiro |
| **Análise** | `make analyze` | `analysis/analyze_translations.py` | Para estatísticas |
| **Validação** | `make validate` | `validation/02_validate_translations.py` | Para qualidade |
| **Correção** | `make fix` | (correction/) | Para correções |
| **Limpeza** | `make clean-all` | - | Manutenção |

### Exemplos Práticos Imediatos

```bash
# EXEMPLO 1: Análise completa
make status && make unprocessed && make analyze

# EXEMPLO 2: Validação em lote
make status && for file in $(make unprocessed); do make validate "$file"; done

# EXEMPLO 3: Relatório e limpeza
make analyze-report && make clean-all && make status
```

---

## ⚙️ Configurações {#-configurações}

### Arquivos de Configuração Essenciais (CONSOLIDADOS)

| Arquivo | Localização | Para quê? |
|--------|-------------|-----------|
| `script_versions.yaml` | `config/script_versions.yaml` | Versões e dependências |
| `correction_rules.yaml` | `config/correction_rules.yaml` | Regras de correção |
| `environment_vars.sh` | `config/environment_vars.sh` | Variáveis de ambiente |

### Como Carregar Ambiente

```bash
# Método 1: Via Makefile
make env

# Método 2: Direto
source config/environment_vars.sh

# Verificar variáveis carregadas
echo $BMAD_SCRIPTS_DIR
echo $BMAD_DATA_DIR
```

---

## 📊 Dados e Logs {#-dados-e-logs}

### Estado do Projeto

**Arquivo**: `translate/data/state/execution_state.json`
**Quando consultar**: Antes de qualquer operação
**Como consultar**: `make status` (preferido) ou `cat` direto

### Logs Centralizados

**Localização**: `logs/` (único e central)
**Ver mais recentes**: `ls -lht logs/ | head -5`
**Acompanhar em tempo real**: `tail -f logs/latest.log`

---

## 📚 Documentação {#-documentação}

### Documentação Principal

**README principal**: `translate/docs/README.md`
**Quando acessar**: `make docs-view`
**Conteúdo**: Visão geral, instalação, uso

### Documentação de Desenvolvimento

**Localização**: `translate/docs/development/`
**Quando acessar**: `make docs-dev`
**Conteúdo**: Guias de desenvolvimento, arquitetura

### Exemplos Práticos

**Localização**: `translate/docs/examples/`
**Quando acessar**: `make docs-examples`
**Conteúdo**: Exemplos de uso, casos práticos

### AGENTS.md (Guia para Agentes)

**Localização**: `translate/docs/AGENTS.md`
**Quando acessar**: `make docs-view` (primeiro) ou direto
**Conteúdo**: Este arquivo completo - guia para agentes LLM

---

## 🚨 Situações Comuns {#-situações-comuns}

### Troubleshooting Rápido

| Situação | Comando | Solução |
|----------|---------|----------|
| "Não sei o que fazer" | `make status` | Ver "Próximas Ações" |
| "Preciso analisar" | `make analyze` | Gera estatísticas |
| "Arquivo não processado" | `make unprocessed` | Lista pendentes |
| "Acho que estou em loop" | `make status` | Ver execuções recentes |
| "Precisa limpar" | `make clean-all` | Limpeza completa |
| "Preciso da documentação" | `make docs-view` | Abre translate/docs/README.md |
| "Preciso exemplos" | `make docs-examples` | Abre translate/docs/examples/ |
| "Preciso docs dev" | `make docs-dev` | Abre translate/docs/development/ |

### Padrões de Resolução de Problemas

1. **Status First**: Sempre comece com `make status`
2. **Check State**: Verifique `execution_state.json`
3. **Ask User**: Se não tiver certeza, pergunte
4. **Document**: Consulte documentação antes de mudar

---

## 🎓 Boas Práticas {#-boas-práticas}

### Para Cada Operação

1. **make status** (obrigatório)
2. **Verificar estado** (anti-loop)
3. **Usar comando make** (não script direto)
4. **Verificar resultado** (pós-operação)
5. **Atualizar estado** (se necessário)

### Para Desenvolvimento

1. **make dev-setup** (setup completo)
2. **make test-state** (testar sistema)
3. **make docs-view** (consultar docs - AGENTS.md)
4. **make info** (informações do projeto)

### ERROS COMUNS A EVITAR

- ❌ Ignorar `make status`
- ❌ Executar script sem verificar estado
- ❌ Assumir sem consultar
- ❌ Modificar arquivos sem atualizar estado
- ❌ Usar caminhos antigos (removidos na reorganização)

---

## 🔍 Checklist de Verificação {#-checklist-de-verificação}

Antes de executar qualquer operação, verifique:

- [ ] Executei `make status`?
- [ ] Consultei arquivos não processados?
- [ ] Verifiquei se a operação já foi executada recentemente?
- [ ] Li as "Próximas Ações" do status?
- [ ] Entendi o que vou fazer e por quê?
- [ ] Sei onde está a ferramenta/script que preciso?
- [ ] Sei como atualizar o estado após a operação?

---

## 📞 Quando Consultar o Usuário {#-quando-consultar-o-usuário}

Consulte o usuário quando:

- ⚠️ Detectar possível loop de execução
- ⚠️ Não tiver certeza sobre qual ação tomar
- ⚠️ Encontrar inconsistências no estado
- ⚠️ Precisar executar operações destrutivas (reset, clean-all)
- ⚠️ Encontrar erros não documentados
- ⚠️ Precisar implementar funcionalidades novas
- ⚠️ Encontrar estrutura confusa ou duplicada

---

## 🎯 Resumo Rápido {#-resumo-rápido}

| Preciso... | Use... |
|------------|--------|
| Ver status | `make status` |
| Listar não processados | `make unprocessed` |
| Analisar traduções | `make analyze` |
| Ver todos os comandos | `make help` |
| Limpar cache/locks | `make clean-all` |
| Ver documentação principal | `make docs-view` |
| Ver documentação desenvolvimento | `make docs-dev` |
| Ver exemplos práticos | `make docs-examples` |
| Testar sistema | `make test-state` |
| Informações do projeto | `make info` |
| Ver guia para agentes | `make docs-view` (AGENTS.md) |
| Ver estrutura do projeto | `make info` |

---

## 📝 Notas Finais

- Este projeto usa **estado persistente** para prevenir loops
- **SEMPRE** verifique o status antes de agir
- Use o **Makefile** como interface principal
- Consulte a **documentação** quando em dúvida
- **Pergunte ao usuário** se não tiver certeza
- **Estrutura limpa**: Sem duplicações, organizada e intuitiva
- **AGENTS.md principal**: Este arquivo na raiz é a sua referência principal

**Lembre-se**: É melhor perguntar do que executar algo errado! 🎯

---

## 🔗 Referências Rápidas

- **AGENTS.md principal**: Este arquivo (raiz)
- **Documentação completa**: `translate/docs/`
- **Configurações consolidadas**: `config/`
- **Estado persistente**: `translate/data/state/execution_state.json`
- **Logs centralizados**: `logs/`
- **Histórico de mudanças**: `ESTRUTURA_LIMPA_FINAL.md`
