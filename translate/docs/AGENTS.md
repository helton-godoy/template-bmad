# AGENTS.md - Guia para Agentes LLM

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

## 📁 Estrutura do Projeto

### Diretórios Principais

```shell
/home/helton/git/template-bmad/
├── Makefile                    # ⭐ COMANDOS CENTRALIZADOS
├── translate/
│   ├── scripts/                # Scripts organizados
│   │   ├── validation/         # Validação de qualidade
│   │   ├── analysis/           # Análise de traduções
│   │   ├── correction/         # Correções
│   │   │   ├── auto/           # Correções automáticas
│   │   │   ├── manual/         # Correções manuais
│   │   │   └── pipelines/      # Pipelines de correção
│   │   └── utils/              # ⭐ UTILITÁRIOS CRÍTICOS
│   ├── config/                 # Configurações
│   ├── data/                   # Dados e estado
│   │   ├── state/              # ⭐ ESTADO PERSISTENTE
│   │   ├── cache/              # Cache de resultados
│   │   ├── logs/               # Logs estruturados
│   │   └── reports/            # Relatórios gerados
│   └── docs/                   # Documentação
└── _bmad/                      # ⭐ ARQUIVOS TRADUZIDOS
```

---

## 🛠️ Ferramentas Disponíveis

### 1. Makefile (Interface Principal)

**Localização:** `/home/helton/git/template-bmad/Makefile`

**Uso:**

```bash
make help          # Ver todos os comandos
make status        # Status do projeto
make analyze       # Analisar traduções
make unprocessed   # Listar não processados
make clean-all     # Limpeza completa
```

**Quando usar:** SEMPRE que precisar executar qualquer operação no projeto

---

### 2. Sistema de Estado Persistente

**Localização:** `translate/scripts/utils/state_manager.py`

**Propósito:** Rastrear o que já foi processado para PREVENIR LOOPS

**Uso:**

```bash
# Verificar status
python3 translate/scripts/utils/state_manager.py status

# Listar não processados
python3 translate/scripts/utils/state_manager.py unprocessed
```

**Arquivo de estado:** `translate/data/state/execution_state.json`

**Quando consultar:**

- ✅ ANTES de processar qualquer arquivo
- ✅ ANTES de executar qualquer pipeline
- ✅ ANTES de executar scripts de correção
- ✅ Quando precisar saber o progresso

**Estrutura do estado:**

```json
{
  "version": "1.0.0",
  "last_updated": "ISO timestamp",
  "files_processed": {
    "caminho/arquivo.md": {
      "checksum": "sha256...",
      "processed_at": "ISO timestamp",
      "status": "completed",
      "scripts_applied": ["script1", "script2"]
    }
  },
  "script_executions": {
    "nome_script": {
      "last_run": "ISO timestamp",
      "run_count": 3,
      "files_affected": 45
    }
  }
}
```

---

### 3. Sistema de Locks

**Localização:** `translate/scripts/utils/lock_system.sh`

**Propósito:** Prevenir execuções simultâneas

**Uso:**

```bash
source translate/scripts/utils/lock_system.sh

# Adquirir lock
acquire_lock "nome_operacao"

# Verificar lock
check_lock "nome_operacao"

# Limpar locks órfãos
cleanup_old_locks 3600
```

**Quando usar:**

- ✅ Ao executar scripts que modificam arquivos
- ✅ Ao executar pipelines
- ✅ Ao executar operações longas

---

### 4. Comando de Status Visual

**Localização:** `translate/scripts/utils/bmad_translate_status.py`

**Propósito:** Visualização completa do status do projeto

**Uso:**

```bash
make status
# OU
python3 translate/scripts/utils/bmad_translate_status.py
```

**Informações fornecidas:**

- Progresso geral (% processado)
- Arquivos processados vs pendentes
- Últimas execuções (24h)
- Avisos
- Próximas ações sugeridas

**Quando usar:**

- ✅ SEMPRE no início de uma nova sessão
- ✅ Antes de executar qualquer pipeline
- ✅ Para decidir próximas ações

---

## 📋 Scripts Disponíveis

### Validação

| Script | Localização | Propósito |
|--------|-------------|-----------|
| Validar instalação | `scripts/validation/00_validate_installation.py` | Verifica dependências |
| Validar traduções | `scripts/validation/02_validate_translations.py` | Valida qualidade |

**Comando:** `make validate` ou `make validate-install`

---

### Análise

| Script | Localização | Propósito |
|--------|-------------|-----------|
| Analisar traduções | `scripts/analysis/analyze_translations.py` | Estatísticas e relatórios |

**Comandos:**

```bash
make analyze              # Estatísticas
make analyze-report       # Relatório completo
make analyze-csv          # CSV de pares
```

**Subcomandos do script:**

```bash
python3 scripts/analysis/analyze_translations.py stats
python3 scripts/analysis/analyze_translations.py report -o arquivo.md
python3 scripts/analysis/analyze_translations.py csv -o arquivo.csv
python3 scripts/analysis/analyze_translations.py list
```

---

### Utilitários

| Script | Localização | Propósito |
|--------|-------------|-----------|
| State Manager | `scripts/utils/state_manager.py` | Gerenciar estado |
| Lock System | `scripts/utils/lock_system.sh` | Gerenciar locks |
| Status | `scripts/utils/bmad_translate_status.py` | Status visual |
| Model Management | `scripts/utils/model_management.py` | Gerenciar modelos |

---

## 📄 Arquivos de Configuração

### 1. Versionamento de Scripts

**Localização:** `translate/config/script_versions.yaml`

**Conteúdo:**

- Versões de todos os scripts
- Dependências (Python, Bash, pacotes)
- Compatibilidade de formatos

**Quando consultar:** Para verificar versões e dependências

---

### 2. Regras de Correção

**Localização:** `translate/config/correction_rules.yaml`

**Conteúdo:**

- Padrões de artefatos a remover
- Regras de formatação
- Configurações de encoding
- Elementos a preservar

**Quando consultar:** Antes de implementar correções automáticas

---

### 3. Variáveis de Ambiente

**Localização:** `translate/config/environment_vars.sh`

**Uso:**

```bash
source translate/config/environment_vars.sh
# OU
make env
```

**Variáveis disponíveis:**

- `BMAD_TRANSLATE_ROOT`
- `BMAD_SCRIPTS_DIR`
- `BMAD_DATA_DIR`
- `BMAD_STATE_FILE`
- `BMAD_CACHE_DIR`
- etc.

---

## 📚 Documentação

### Documentação Principal

**Localização:** `translate/docs/README.md`

**Conteúdo:**

- Visão geral da reorganização
- Estrutura de diretórios
- Guia de uso dos componentes
- Regras anti-loop
- Exemplos práticos

**Comando:** `make docs-view`

---

### Plano de Implementação

**Localização:** `.gemini/antigravity/brain/.../implementation_plan.md`

**Conteúdo:**

- Análise crítica da proposta
- Estrutura otimizada
- Mudanças propostas
- Cronograma
- Riscos e mitigações

---

### Exemplos de Implementação

**Localização:** `.gemini/antigravity/brain/.../implementation_examples.md`

**Conteúdo:**

- Código completo dos componentes críticos
- Exemplos de uso
- Integração com agentes LLM

---

### Walkthrough

**Localização:** `.gemini/antigravity/brain/.../walkthrough.md`

**Conteúdo:**

- Resumo da implementação
- Componentes implementados
- Testes realizados
- Próximos passos

---

## 🔄 Fluxo de Trabalho Recomendado

### Para Novas Sessões

```bash
# 1. Verificar status
make status

# 2. Ver arquivos não processados
make unprocessed

# 3. Decidir ação baseado no status
# Se houver arquivos pendentes:
#   - Executar análise: make analyze
#   - Executar correções: make fix (quando implementado)
#   - Executar pipeline: make pipeline (quando implementado)
```

### Para Análise de Traduções

```bash
# 1. Estatísticas gerais
make analyze

# 2. Relatório detalhado
make analyze-report

# 3. CSV para análise externa
make analyze-csv
```

### Para Correções (Quando Implementado)

```bash
# 1. Verificar o que precisa correção
make unprocessed

# 2. Executar correções automáticas
make fix

# 3. Verificar resultado
make status
```

---

## 🚨 Situações Comuns e Soluções

### "Não sei o que fazer a seguir"

```bash
make status
# Leia a seção "Próximas Ações Sugeridas"
```

### "Preciso saber quais arquivos processar"

```bash
make unprocessed
```

### "Executei algo mas não vejo mudanças"

```bash
# Verificar se já foi executado recentemente
make status

# Ver estado detalhado
cat translate/data/state/execution_state.json | jq .
```

### "Acho que estou em um loop"

```bash
# 1. PARE imediatamente
# 2. Verifique status
make status

# 3. Verifique logs
ls -lht translate/data/logs/

# 4. Consulte o usuário
```

### "Preciso resetar tudo"

```bash
# CUIDADO: Isso apaga todo o estado!
make state-reset
```

---

## 📊 Dados e Logs

### Estado Persistente

**Localização:** `translate/data/state/execution_state.json`

**Quando consultar:**

- Para ver o que já foi processado
- Para verificar checksums
- Para ver histórico de execuções

### Cache

**Localização:** `translate/data/cache/`

**Limpeza:**

```bash
make cache-clean  # Remove cache >24h
```

### Logs

**Localização:** `translate/data/logs/`

**Consulta:**

```bash
ls -lht translate/data/logs/ | head -10
tail -f translate/data/logs/latest.log
```

### Relatórios

**Localização:** `translate/data/reports/`

**Geração:**

```bash
make analyze-report  # Gera relatório de análise
```

---

## 🎓 Boas Práticas para Agentes

### DO (Faça)

✅ Sempre verifique `make status` antes de agir
✅ Consulte arquivos não processados antes de processar tudo
✅ Use o Makefile como interface principal
✅ Atualize o estado após modificações
✅ Verifique logs em caso de erro
✅ Consulte a documentação quando em dúvida
✅ Pergunte ao usuário se não tiver certeza

### DON'T (Não Faça)

❌ Executar scripts diretamente sem verificar estado
❌ Processar arquivos sem verificar se já foram processados
❌ Ignorar avisos de "já executado recentemente"
❌ Recriar funcionalidades que já existem
❌ Executar o mesmo comando repetidamente sem mudanças
❌ Modificar arquivos sem atualizar o estado
❌ Assumir que algo precisa ser feito sem verificar status

---

## 🔍 Checklist de Verificação

Antes de executar qualquer operação, verifique:

- [ ] Executei `make status`?
- [ ] Consultei arquivos não processados?
- [ ] Verifiquei se a operação já foi executada recentemente?
- [ ] Li as "Próximas Ações Sugeridas" do status?
- [ ] Entendi o que vou fazer e por quê?
- [ ] Sei onde está a ferramenta/script que preciso?
- [ ] Sei como atualizar o estado após a operação?

---

## 📞 Quando Consultar o Usuário

Consulte o usuário quando:

- ⚠️ Detectar possível loop de execução
- ⚠️ Não tiver certeza sobre qual ação tomar
- ⚠️ Encontrar inconsistências no estado
- ⚠️ Precisar executar operações destrutivas (reset, clean-all)
- ⚠️ Encontrar erros não documentados
- ⚠️ Precisar implementar funcionalidades novas

---

## 🎯 Resumo Rápido

| Preciso... | Use... |
|------------|--------|
| Ver status | `make status` |
| Listar não processados | `make unprocessed` |
| Analisar traduções | `make analyze` |
| Ver todos os comandos | `make help` |
| Limpar cache/locks | `make clean-all` |
| Ver documentação | `make docs-view` |
| Testar sistema | `make test-state` |
| Informações do projeto | `make info` |

---

## 📝 Notas Finais

- Este projeto usa **estado persistente** para prevenir loops
- **SEMPRE** verifique o status antes de agir
- Use o **Makefile** como interface principal
- Consulte a **documentação** quando em dúvida
- **Pergunte ao usuário** se não tiver certeza

**Lembre-se:** É melhor perguntar do que executar algo errado! 🎯
