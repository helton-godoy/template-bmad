<!-- Powered by BMAD-CORE™ -->

# Desenvolvimento conduzido a ensaios de aceitação (ATDD)

**ID do fluxo de trabalho**: `_bmad/bmm/testarch/atdd`
**Versão**: 4.0 (BMad v6)

---

## Overview

Generates failing acceptance tests BEFORE implementation following TDD's red-green-refactor cycle. This workflow creates comprehensive test coverage at appropriate levels (E2E, API, Component) with supporting infrastructure (fixtures, factories, mocks) and provides an implementation checklist to guide development.

**Core Principle**: Tests fail first (red phase), then guide development to green, then enable confident refactoring.

---

## Requisitos de pré-voo

**Crítico:** Verifique estes requisitos antes de prosseguir. Se algum falhar, HALT e notificar o usuário.

- ✅ História aprovada com critérios claros de aceitação
- ✅ Desenvolvimento sandbox/environment pronto
- ✅ Existe um andaime de framework (correr o fluxo de trabalho `framework` se faltar)
- ✅ Configuração do framework de teste disponível (playwright. config.ts ou cipreste.config.ts)

---

## Step 1: Load Story Context and Requirements

### Actions

1. **Read Story Markdown**
   - Load story file from `{story_file}` variable
   - Extract acceptance criteria (all testable requirements)
   - Identify affected systems and components
   - Note any technical constraints or dependencies

2. **Load Framework Configuration**
   - Read framework config (playwright.config.ts or cypress.config.ts)
   - Identify test directory structure
   - Check existing fixture patterns
   - Note test runner capabilities

3. **Load Existing Test Patterns**
   - Search `{test_dir}` for similar tests
   - Identify reusable fixtures and helpers
   - Check data factory patterns
   - Note naming conventions

4. **Check Playwright Utils Flag**

   Read `{config_source}` and check `config.tea_use_playwright_utils`.

5. **Load Knowledge Base Fragments**

   **Critical:** Consult `{project-root}/_bmad/bmm/testarch/tea-index.csv` to load:

   **Core Patterns (Always load):**
   - `data-factories.md` - Factory patterns using faker (override patterns, nested factories, API seeding, 498 lines, 5 examples)
   - `component-tdd.md` - Component test strategies (red-green-refactor, provider isolation, accessibility, visual regression, 480 lines, 4 examples)
   - `test-quality.md` - Test design principles (deterministic tests, isolated with cleanup, explicit assertions, length limits, execution time optimization, 658 lines, 5 examples)
   - `test-healing-patterns.md` - Common failure patterns and healing strategies (stale selectors, race conditions, dynamic data, network errors, hard waits, 648 lines, 5 examples)
   - `selector-resilience.md` - Selector best practices (data-testid > ARIA > text > CSS hierarchy, dynamic patterns, anti-patterns, 541 lines, 4 examples)
   - `timing-debugging.md` - Race condition prevention and async debugging (network-first, deterministic waiting, anti-patterns, 370 lines, 3 examples)

   **If `config.tea_use_playwright_utils: true` (All Utilities):**
   - `overview.md` - Playwright utils for ATDD patterns
   - `api-request.md` - API test examples with schema validation
   - `network-recorder.md` - HAR record/playback for UI acceptance tests
   - `auth-session.md` - Auth setup for acceptance tests
   - `intercept-network-call.md` - Network interception in ATDD scenarios
   - `recurse.md` - Polling for async acceptance criteria
   - `log.md` - Logging in ATDD tests
   - `file-utils.md` - File download validation in acceptance tests
   - `network-error-monitor.md` - Catch silent failures in ATDD
   - `fixtures-composition.md` - Composing utilities for ATDD

   **If `config.tea_use_playwright_utils: false`:**
   - `fixture-architecture.md` - Test fixture patterns with auto-cleanup (pure function → fixture → mergeTests composition, 406 lines, 5 examples)
   - `network-first.md` - Route interception patterns (intercept before navigate, HAR capture, deterministic waiting, 489 lines, 5 examples)

**Halt Condition:** If story has no acceptance criteria or framework is missing, HALT with message: "ATDD requires clear acceptance criteria and test framework setup"

---

## Passo 1.5: Seleção do modo de geração (NOVA - Fase 2.5)

### Acções

1. **Detect Generation Mode**

Determinar o modo com base na complexidade do cenário:

**Modo de Geração de IA (DEFAULT)**:
- Critérios claros de aceitação com padrões padrão
   - Uses: Ensaios gerados por IA a partir de requisitos
- Apropriado para: CRUD, autenticação, navegação, testes de API
- Aproximação mais rápida

**Modo de gravação (OPTIONAL - UI complexa)**:
- Interações complexas de IU (drag-drop, assistentes, fluxos de várias páginas)
   - Uses: Gravação de teste interativa com Playwright MCP
- Apropriado para: fluxos de trabalho visuais, requisitos obscuros
- Apenas se config.tea use mcp enhances for true E MCP disponíveis

2. **Modo de Geração de IA (DEFAULT - Continue para o Passo 2)**

Para cenários padrão:
- Continuar com o fluxo de trabalho existente (Passo 2: Selecione Níveis de Teste e Estratégia)
- A IA gera testes baseados em critérios de aceitação fr