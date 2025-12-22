# Revisão da Qualidade do Teste - Instruções v4.0

**Fluxo de trabalho:** `testarch-test-review`
**Puse:** Reveja a qualidade do teste usando a abrangente base de conhecimento da TEA e valide contra as melhores práticas para manutenção, determinismo, isolamento e prevenção de flakiness
**Agente:** Arquiteto de ensaio (TEA)
**Formato:** Puro Markdown v4.0 (sem blocos XML)

---

## Overview

This workflow performs comprehensive test quality reviews using TEA's knowledge base of best practices. It validates tests against proven patterns for fixture architecture, network-first safeguards, data factories, determinism, isolation, and flakiness prevention. The review generates actionable feedback with quality scoring.

**Key Capabilities:**

- **Knowledge-Based Review**: Applies patterns from tea-index.csv fragments
- **Quality Scoring**: 0-100 score based on violations and best practices
- **Multi-Scope**: Review single file, directory, or entire test suite
- **Pattern Detection**: Identifies flaky patterns, hard waits, race conditions
- **Best Practice Validation**: BDD format, test IDs, priorities, assertions
- **Actionable Feedback**: Critical issues (must fix) vs recommendations (should fix)
- **Integration**: Works with story files, test-design, acceptance criteria

---

## Pré-requisitos

**Obrigatório:**

- Arquivo(s) de teste(s) a rever (descoberto(s) automaticamente ou explicitamente fornecido)
- Configuração do framework de teste (playwright. config.ts, jest.config.js, etc.)

**Recomendado:**

- Arquivo de história com critérios de aceitação (para contexto)
- Documento de projecto de ensaio (para o contexto prioritário)
- Fragmentos de base de conhecimento disponíveis em tea-index.csv

**Condições de sal:**

- Se o caminho do arquivo de teste for inválido ou o arquivo não existir, pare e solicite correção
- Se test dir estiver vazio (sem testes encontrados), pare e notifique o usuário

---

## Passos de fluxo de trabalho

### Passo 1: Carregar Contexto e Base de Conhecimento

**Acções:**

1. Verifique a bandeira do dramaturgo-utils:
- Ler `{config_source}` e verificar `config.tea_use_playwright_utils`

2. Carregar fragmentos de conhecimento relevantes de `{project-root}/_bmad/bmm/testarch/tea-index.csv`:

**Padrões de cor (carga sempre):**
- `test-quality.md` - Definição de feito (testes determinísticos, isolados com limpeza, afirmações explícitas, <300 lines, <1.5 min, 658 lines, 5 examples)
   - `data-factories.md` - Factory functions with faker: overrides, nested factories, API-first setup (498 lines, 5 examples)
   - `test-levels-framework.md` - E2E vs API vs Component vs Unit appropriateness with decision matrix (467 lines, 4 examples)
   - `selective-testing.md` - Duplicate coverage detection with tag-based, spec filter, diff-based selection (727 lines, 4 examples)
   - `test-healing-patterns.md` - Common failure patterns: stale selectors, race conditions, dynamic data, network errors, hard waits (648 lines, 5 examples)
   - `selector-resilience.md` - Selector best practices (data-testid > ARIA > texto > hierarquia CSS, anti-padrãos, 541 linhas, 4 exemplos)
- `timing-debugging.md` - Prevenção de doenças raciais e técnicas de depuração async (370 linhas, 3 exemplos)

**Se `config.tea_use_playwright_utils: true` (Todos os Utilitários):**
- `overview.md` - O dramaturgo utiliza as melhores práticas
- `api-request.md` - Validar padrões de uso do apiRequest
- `network-recorder.md` - Reveja o registro HAR/reproduzir implementation
- `auth-session.md` - Verifique a gestão de fichas de autenticação
- `intercept-network-call.md` - Validar interceptação de rede
- `recurse.md` - Revisão dos padrões de votação
- `log.md` - Verificar as melhores práticas de registro
- `file-utils.md` - Validar padrões de operação de arquivos
- `burn-in.md` - Revisão da configuração de gravação
- `network-error-monitor.md` - Configuração de monitoramento de erros
- `fixtures-composition.md` - Validar mesclagemUso de testes

**Se `config.tea_use_playwright_utils: false`:**
- `fixture-architecture.md` - function → Fixação → mesclarComposição de testes com limpeza automática (406 linhas, 5 exemplos)
- `network-first.md` - Intercepção de rota antes de navegar para evitar condições de corrida (489 linhas, 5 exemplos)
- `playwright-config.md` - Configuração baseada no ambiente com validação rápida (722 linhas, 5 exemplos)
- `component-tdd.md` - Padrões Red-Green-Refactor com isolamento do provedor (480 linhas, 4 exemplos)
- `ci-burn-in.md` - Detecção de teste Flaky com lacete de queima de 10 iterações (678 linhas, 4 exemplos)

3. Determinar âmbito de revisão:
- **single**: Reveja um ficheiro de ensaio (`test_file_path` fornecido)
- **directório**: Rever todos os testes no directório (`test_dir` fornecido)
- **suite**: Reveja todo o conjunto de testes (descobrir todos os ficheiros de teste)

4. Auto-descobre artefatos relacionados (se `auto_discover_story: true`):
- Extrair o ID de teste do nome do ficheiro (por exemplo, `1.3-E2E-001.spec.ts` → história 1.3)
- Pesquisa de arquivo de história (`story-1.3.md`)
- Pesquisa de projeto de teste (`test-design-story-1.3.md` ou `test-design-epic-1.md`)

5. Leia o arquivo de história para o contexto (se disponível):
- Critérios de aceitação do extracto
- Extrair classificação de prioridade
- Extrair IDs de teste esperados

**Saída:** Completo kn