# Reorganização do Repositório de Tradução - README

## Visão Geral

Este repositório foi reorganizado para prevenir loops de execução, melhorar rastreabilidade e criar uma estrutura intuitiva para scripts de tradução.

## Estrutura de Diretórios

```
translate/
├── scripts/                    # Scripts organizados por categoria
│   ├── validation/            # Validação de qualidade
│   │   ├── 00_validate_installation.py
│   │   └── 02_validate_translations.py
│   ├── analysis/              # Análise de traduções
│   │   └── analyze_translations.py
│   ├── correction/            # Correções
│   │   ├── auto/              # Correções automáticas
│   │   ├── manual/            # Assistência para correções manuais
│   │   └── pipelines/         # Pipelines de correção
│   └── utils/                 # Utilitários compartilhados
│       ├── state_manager.py   # ⭐ Sistema de estado persistente
│       ├── lock_system.sh     # Sistema de locks
│       ├── bmad_translate_status.py  # Comando de status
│       └── model_management.py
├── config/                    # Configurações centralizadas
│   ├── script_versions.yaml
│   ├── correction_rules.yaml
│   └── environment_vars.sh
└── data/                      # Dados e estado
    ├── state/                 # ⭐ Estado persistente
    ├── cache/                 # Cache de resultados
    ├── logs/                  # Logs estruturados
    ├── reports/               # Relatórios gerados
    └── backups/               # Backups automáticos
```

## Componentes Principais

### 1. Sistema de Estado Persistente (`state_manager.py`)

Previne loops entre diferentes sessões de agentes LLM rastreando:

- Arquivos processados com checksums SHA256
- Execuções de scripts com timestamps
- Resultados de validações

**Uso:**

```bash
# Verificar status
python3 translate/scripts/utils/state_manager.py status

# Listar arquivos não processados
python3 translate/scripts/utils/state_manager.py unprocessed
```

### 2. Sistema de Locks (`lock_system.sh`)

Previne execuções simultâneas do mesmo script.

**Uso:**

```bash
source translate/scripts/utils/lock_system.sh

# Adquirir lock
acquire_lock "meu_script"

# Verificar lock
check_lock "meu_script"

# Limpar locks antigos
cleanup_old_locks 3600
```

### 3. Comando de Status (`bmad_translate_status.py`)

Visualização completa do status do projeto.

**Uso:**

```bash
python3 translate/scripts/utils/bmad_translate_status.py
```

**Saída:**

```
╔══════════════════════════════════════════════════════════════╗
║         BMAD Translation Project - Status Report             ║
╚══════════════════════════════════════════════════════════════╝

📊 Progresso Geral
  [████████████████████████████████████████] 100.0%
  ✅ Processados: 200/200
  ⏳ Pendentes: 0

📝 Próximas Ações Sugeridas
  1. Tudo em dia! ✨
```

## Uso Rápido

### Verificar Status do Projeto

```bash
cd /home/helton/git/template-bmad
python3 translate/scripts/utils/bmad_translate_status.py
```

### Executar Análise de Traduções

```bash
python3 translate/scripts/analysis/analyze_translations.py stats
```

### Validar Instalação

```bash
python3 translate/scripts/validation/00_validate_installation.py
```

## Regras Anti-Loop para Agentes LLM

**SEMPRE:**

1. ✅ Verificar status antes de executar qualquer pipeline
2. ✅ Consultar arquivos não processados antes de processar tudo
3. ✅ Atualizar estado após modificações
4. ✅ Verificar se script foi executado recentemente

**NUNCA:**

1. ❌ Executar o mesmo script mais de 2x seguidas
2. ❌ Processar arquivos já marcados como processados
3. ❌ Ignorar verificações de estado

## Configurações

### Variáveis de Ambiente

Carregue as variáveis de ambiente:

```bash
source translate/config/environment_vars.sh
```

### Regras de Correção

Edite `translate/config/correction_rules.yaml` para ajustar regras de correção.

### Versões de Scripts

Consulte `translate/config/script_versions.yaml` para versões e dependências.

## Migração de Scripts Antigos

Os scripts foram reorganizados da seguinte forma:

| Script Original | Novo Local |
|----------------|------------|
| `validation/validator.py` | `scripts/validation/02_validate_translations.py` |
| `scripts/validate_installation.py` | `scripts/validation/00_validate_installation.py` |
| `review_translations.py` | `scripts/analysis/analyze_translations.py` |
| `scripts/warmup_models.py` | `scripts/utils/model_management.py` |

**Nota:** Os scripts originais foram mantidos para compatibilidade, mas devem ser considerados deprecated.

## Próximos Passos

1. Implementar pipelines de correção em `scripts/correction/pipelines/`
2. Mover scripts do `archive/` para categorias apropriadas
3. Criar testes de integração
4. Configurar git hooks opcionais

## Suporte

Para problemas ou dúvidas, consulte:

- `docs/troubleshooting.md` (a ser criado)
- `implementation_plan.md` (plano detalhado)
- `implementation_examples.md` (exemplos de código)
