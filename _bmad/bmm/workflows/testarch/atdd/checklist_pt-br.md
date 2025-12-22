# Lista de Verificação da Validação do Fluxo de Trabalho ATDD

Use esta lista de verificação para validar que o fluxo de trabalho ATDD foi executado corretamente e todas as entregas atendem aos padrões de qualidade.

## Pré-requisitos

Antes de iniciar este fluxo de trabalho, verifique:

- [ ] História aprovada com critérios claros de aceitação (a AC deve ser testada)
- [ ] Desenvolvimento sandbox / ambiente pronto
- [ ] Framework scaffolding existe (correr `framework` fluxo de trabalho se faltando)
- [ ] Configuração do framework de teste disponível (playwright. config.ts ou cipreste.config.ts)
- [ ] Package.json tem dependências de teste instaladas (Playwright ou Cypress)

**Halt se faltar:** Critérios de aceitação de andaimes ou histórias

---

## Step 1: Story Context and Requirements

- [ ] Story markdown file loaded and parsed successfully
- [ ] All acceptance criteria identified and extracted
- [ ] Affected systems and components identified
- [ ] Technical constraints documented
- [ ] Framework configuration loaded (playwright.config.ts or cypress.config.ts)
- [ ] Test directory structure identified from config
- [ ] Existing fixture patterns reviewed for consistency
- [ ] Similar test patterns searched and found in `{test_dir}`
- [ ] Knowledge base fragments loaded:
  - [ ] `fixture-architecture.md`
  - [ ] `data-factories.md`
  - [ ] `component-tdd.md`
  - [ ] `network-first.md`
  - [ ] `test-quality.md`

---

## Passo 2: Seleção e estratégia do nível de teste

- [ ] Cada critério de aceitação analisado para o nível de teste adequado
- [ ] Estrutura de seleção de nível de teste aplicada (E2E vs API vs Componente vs Unidade)
- [ ] Testes E2E: Viagens críticas do utilizador e integração multi-sistema identificadas
- [ ] Testes API: Lógica empresarial e contratos de serviços identificados
- [ ] Testes de componentes: Comportamento do componente de IU e interações identificadas
- [ ] Testes unitários: pura lógica e casos de borda identificados (se aplicável)
- [ ] Cobertura duplicada evitada (mesmo comportamento não testado em múltiplos níveis desnecessariamente)
- [ ] Testes priorizados usando framework P0-P3 (se existe documento de projeto de teste)
- [ ] Nível de ensaio primário definido na variável `primary_level` (normalmente E2E ou API)
- [ ] Níveis de ensaio documentados na lista ATDD

---

## Step 3: Failing Tests Generated

### Test File Structure Created

- [ ] Test files organized in appropriate directories:
  - [ ] `tests/e2e/` for end-to-end tests
  - [ ] `tests/api/` for API tests
  - [ ] `tests/component/` for component tests
  - [ ] `tests/support/` for infrastructure (fixtures, factories, helpers)

### E2E Tests (If Applicable)

- [ ] E2E test files created in `tests/e2e/`
- [ ] All tests follow Given-When-Then format
- [ ] Tests use `data-testid` selectors (not CSS classes or fragile selectors)
- [ ] One assertion per test (atomic test design)
- [ ] No hard waits or sleeps (explicit waits only)
- [ ] Network-first pattern applied (route interception BEFORE navigation)
- [ ] Tests fail initially (RED phase verified by local test run)
- [ ] Failure messages are clear and actionable

### API Tests (If Applicable)

- [ ] API test files created in `tests/api/`
- [ ] Tests follow Given-When-Then format
- [ ] API contracts validated (request/response structure)
- [ ] HTTP status codes verified
- [ ] Response body validation includes all required fields
- [ ] Error cases tested (400, 401, 403, 404, 500)
- [ ] Tests fail initially (RED phase verified)

### Component Tests (If Applicable)

- [ ] Component test files created in `tests/component/`
- [ ] Tests follow Given-When-Then format
- [ ] Component mounting works correctly
- [ ] Interaction testing covers user actions (click, hover, keyboard)
- [ ] State management within component validated
- [ ] Props and events tested
- [ ] Tests fail initially (RED phase verified)

### Test Quality Validation

- [ ] All tests use Given-When-Then structure with clear comments
- [ ] All tests have descriptive names explaining what they test
- [ ] No duplicate tests (same behavior tested multiple times)
- [ ] No flaky patterns (race conditions, timing issues)
- [ ] No test interdependencies (tests can run in any order)
- [ ] Tests are deterministic (same input always produces same result)

---

## Etapa 4: Infraestrutura de dados construída

### Fábricas de Dados Criadas

- [ ] Arquivos de fábrica criados em `tests/support/factories/`
- [ ] Todas as fábricas usam `@faker-js/faker` para geração aleatória de dados (sem valores codificados)
- [ ] O suporte das fábricas substitui para cenários de teste específicos
- [ ] Fábricas geram objetos completos válidos correspondentes aos contratos de API
- [ ] Funções de ajuda para criação a granel fornecidas (por exemplo, `createUsers(count)`)
- [ ] As exportações de fábrica são devidamente digitadas (TypeScript)

### Ferramentas de Teste Criadas

- [ ] Arquivos de fixação criados no `tests/support/fixtures/`
- [ ] Todos os acessórios usam o padrão `test.extend()` da Playwright
- [ ] Fixações têm fase de configuração (arranjar pré-condições de teste)
- [ ] Fixtures fornecem dados para testes via `await use(data)`
- [ ] Fixtures têm fase de ruptura com limpeza automática (delete dados criados)
- [ ] Fixtures são composable (pode usar outros fixtures se necessário)
- Não.