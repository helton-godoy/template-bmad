# Execução de teste seletiva e direcionada

## Princípio

Faça apenas os testes de que precisa, quando precisar. Use tags/grep para cortar suites por prioridade de risco (não por estrutura de diretórios), filtro por padrões de especificações ou git diff para focar em áreas impactadas e combinar metadados de prioridade (P0-P3) com detecção de alterações para otimizar a execução pré-compromisso vs. CI. Documentar a estratégia de seleção claramente para que as equipes entendam quando a regressão completa é obrigatória.

## Racional

Executar todo o conjunto de testes em cada commit desperdiça tempo e recursos. A seleção de teste inteligente fornece feedback rápido (testes de fumaça em minutos, regressão completa em horas) mantendo a confiança. A filosofia "32+ maneiras de testes seletivos" equilibra velocidade com cobertura: loops rápidos para desenvolvedores, validação abrangente antes da implantação. A seleção mal documentada leva a confusão sobre quando os testes são executados e por quê.

## Exemplos de padrões

### Exemplo 1: Execução baseada em etiquetas com níveis prioritários

**Context**: Organizar testes por prioridade de risco e fase de execução usando padrões grep/tag.

**Implementation**:

```typescript
// tests/e2e/checkout.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Tag-based test organization
 * - @smoke: Critical path tests (run on every commit, < 5 min)
 * - @regression: Full test suite (run pre-merge, < 30 min)
 * - @p0: Critical business functions (payment, auth, data integrity)
 * - @p1: Core features (primary user journeys)
 * - @p2: Secondary features (supporting functionality)
 * - @p3: Nice-to-have (cosmetic, non-critical)
 */

test.describe('Checkout Flow', () => {
  // P0 + Smoke: Must run on every commit
  test('@smoke @p0 should complete purchase with valid payment', async ({ page }) => {
    await page.goto('/checkout');
    await page.getByTestId('card-number').fill('4242424242424242');
    await page.getByTestId('submit-payment').click();

    await expect(page.getByTestId('order-confirmation')).toBeVisible();
  });

  // P0 but not smoke: Run pre-merge
  test('@regression @p0 should handle payment decline gracefully', async ({ page }) => {
    await page.goto('/checkout');
    await page.getByTestId('card-number').fill('4000000000000002'); // Decline card
    await page.getByTestId('submit-payment').click();

    await expect(page.getByTestId('payment-error')).toBeVisible();
    await expect(page.getByTestId('payment-error')).toContainText('declined');
  });

  // P1 + Smoke: Important but not critical
  test('@smoke @p1 should apply discount code', async ({ page }) => {
    await page.goto('/checkout');
    await page.getByTestId('promo-code').fill('SAVE10');
    await page.getByTestId('apply-promo').click();

    await expect(page.getByTestId('discount-applied')).toBeVisible();
  });

  // P2: Run in full regression only
  test('@regression @p2 should remember saved payment methods', async ({ page }) => {
    await page.goto('/checkout');
    await expect(page.getByTestId('saved-cards')).toBeVisible();
  });

  // P3: Low priority, run nightly or weekly
  test('@nightly @p3 should display checkout page analytics', async ({ page }) => {
    await page.goto('/checkout');
    const analyticsEvents = await page.evaluate(() => (window as any).__ANALYTICS__);
    expect(analyticsEvents).toBeDefined();
  });
});

```

**package.json scripts**:

```json
{
  "scripts": {
    "test": "playwright test",
    "test:smoke": "playwright test --grep '@smoke'",
    "test:p0": "playwright test --grep '@p0'",
    "test:p0-p1": "playwright test --grep '@p0|@p1'",
    "test:regression": "playwright test --grep '@regression'",
    "test:nightly": "playwright test --grep '@nightly'",
    "test:not-slow": "playwright test --grep-invert '@slow'",
    "test:critical-smoke": "playwright test --grep '@smoke.*@p0'"
  }
}

```

**Cypress equivalente**:

```javascript
// cypress/e2e/checkout.cy.ts
describe('Checkout Flow', { tags: ['@checkout'] }, () => {
  it('should complete purchase', { tags: ['@smoke', '@p0'] }, () => {
    cy.visit('/checkout');
    cy.get('[data-cy="card-number"]').type('4242424242424242');
    cy.get('[data-cy="submit-payment"]').click();
    cy.get('[data-cy="order-confirmation"]').should('be.visible');
  });

  it('should handle decline', { tags: ['@regression', '@p0'] }, () => {
    cy.visit('/checkout');
    cy.get('[data-cy="card-number"]').type('4000000000000002');
    cy.get('[data-cy="submit-payment"]').click();
    cy.get('[data-cy="payment-error"]').should('be.visible');
  });
});

// cypress.config.ts
export default defineConfig({
  e2e: {
    env: {
      grepTags: process.env.GREP_TAGS || '',
      grepFilterSpecs: true,
    },
    setupNodeEvents(on, config) {
      require('@cypress/grep/src/plugin')(config);
      return config;
    },
  },
});

```

**Usage**:

```bash

# Playwright
npm run test:smoke                    # Run all @smoke tests
npm run test:p0                       # Run all P0 tests
npm run test -- --grep "@smoke.*@p0"  # Run tests with BOTH tags

# Cypress (with @cypress/grep plugin)
npx cypress run --env grepTags="@smoke"
npx cypress run --env grepTags="@p0+@smoke"  # AND logic
npx cypress run --env grepTags="@p0 @p1"     # OR logic

```

**Key Pontos**:

- **Multiple tags por teste**: Combine prioridade (@ p0) com fase (@ smoke)
- **AND/OR lógica**: Grep suporta filtragem complexa
- **Clear nome**: Importância do teste do documento de etiquetas
- **Fast feedback**: @smoke corre < 5 min, suite completa < 30 min
- **CI integração**: Diferentes tarefas executam combinações de tags diferentes

---

### Example 2: Spec Filter Pattern (File-Based Selection)

**Context**: Run tests by file path pattern or directory for targeted execution.

**Implementation**:

```bash
# !/bin/bash

# scripts/selective-spec-runner.sh

# Run tests based on spec file patterns

set -e

PATTERN=${1:-"**/*.spec.ts"}
TEST_ENV=${TEST_ENV:-local}

echo "🎯 Selective Spec Runner"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Pattern: $PATTERN"
echo "Environment: $TEST_ENV"
echo ""

# Pattern examples and their use cases
case "$PATTERN" in
  "**/checkout*")
    echo "📦 Running checkout-related tests"
    npx playwright test --grep-files="**/checkout*"
    ;;
  "**/auth*"|"**/login*"|"**/signup*")
    echo "🔐 Running authentication tests"
    npx playwright test --grep-files="**/auth*|**/login*|**/signup*"
    ;;
  "tests/e2e/**")
    echo "🌐 Running all E2E tests"
    npx playwright test tests/e2e/
    ;;
  "tests/integration/**")
    echo "🔌 Running all integration tests"
    npx playwright test tests/integration/
    ;;
  "tests/component/**")
    echo "🧩 Running all component tests"
    npx playwright test tests/component/
    ;;
  *)
    echo "🔍 Running tests matching pattern: $PATTERN"
    npx playwright test "$PATTERN"
    ;;
esac

```

**Playwright config for file filtering**:

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  // ... other config

  // Project-based organization
  projects: [
    {
      name: 'smoke',
      testMatch: /.*smoke.*\.spec\.ts/,
      retries: 0,
    },
    {
      name: 'e2e',
      testMatch: /tests\/e2e\/.*\.spec\.ts/,
      retries: 2,
    },
    {
      name: 'integration',
      testMatch: /tests\/integration\/.*\.spec\.ts/,
      retries: 1,
    },
    {
      name: 'component',
      testMatch: /tests\/component\/.*\.spec\.ts/,
      use: { ...devices['Desktop Chrome'] },
    },
  ],
});

```

**Advanced pattern matching**:

```typescript
// scripts/run-by-component.ts
/**
 * Run tests related to specific component(s)
 * Usage: npm run test:component UserProfile,Settings
 */

import { execSync } from 'child_process';

const components = process.argv[2]?.split(',') || [];

if (components.length === 0) {
  console.error('❌ No components specified');
  console.log('Usage: npm run test:component UserProfile,Settings');
  process.exit(1);
}

// Convert component names to glob patterns
const patterns = components.map((comp) => `**/*${comp}*.spec.ts`).join(' ');

console.log(`🧩 Running tests for components: ${components.join(', ')}`);
console.log(`Patterns: ${patterns}`);

try {
  execSync(`npx playwright test ${patterns}`, {
    stdio: 'inherit',
    env: { ...process.env, CI: 'false' },
  });
} catch (error) {
  process.exit(1);
}

```

**package.json scripts**:

```json
{
  "scripts": {
    "test:checkout": "playwright test **/checkout*.spec.ts",
    "test:auth": "playwright test **/auth*.spec.ts **/login*.spec.ts",
    "test:e2e": "playwright test tests/e2e/",
    "test:integration": "playwright test tests/integration/",
    "test:component": "ts-node scripts/run-by-component.ts",
    "test:project": "playwright test --project",
    "test:smoke-project": "playwright test --project smoke"
  }
}

```

**Key Points**:

- **Glob patterns**: Wildcards match file paths flexibly
- **Project isolation**: Separate projects have different configs
- **Component targeting**: Run tests for specific features
- **Directory-based**: Organize tests by type (e2e, integration, component)
- **CI optimization**: Run subsets in parallel CI jobs

---

### Exemplo 3: Seleção de teste baseada em diferenças (apenas arquivos alterados)

**Context**: Execute apenas testes afetados por alterações de código para a velocidade máxima.

**Implementation**:

```bash
# !/bin/bash

# scripts/test-changed-files.sh

# Intelligent test selection based on git diff

set -e

BASE_BRANCH=${BASE_BRANCH:-main}
TEST_ENV=${TEST_ENV:-local}

echo "🔍 Changed File Test Selector"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Base branch: $BASE_BRANCH"
echo "Environment: $TEST_ENV"
echo ""

# Get changed files
CHANGED_FILES=$(git diff --name-only $BASE_BRANCH...HEAD)

if [-z "$CHANGED_FILES"]; then
  echo "✅ No files changed. Skipping tests."
  exit 0
fi

echo "Changed files:"
echo "$CHANGED_FILES" | sed 's/^/  - /'
echo ""

# Arrays to collect test specs
DIRECT_TEST_FILES=()
RELATED_TEST_FILES=()
RUN_ALL_TESTS=false

# Process each changed file
while IFS= read -r file; do
  case "$file" in
    # Changed test files: run them directly
    *.spec.ts|*.spec.js|*.test.ts|*.test.js|*.cy.ts|*.cy.js)
      DIRECT_TEST_FILES+=("$file")
      ;;

    # Critical config changes: run ALL tests
    package.json|package-lock.json|playwright.config.ts|cypress.config.ts|tsconfig.json|.github/workflows/*)
      echo "⚠️  Critical file changed: $file"
      RUN_ALL_TESTS=true
      break
      ;;

    # Component changes: find related tests
    src/components/*.tsx|src/components/*.jsx)
      COMPONENT_NAME=$(basename "$file" | sed 's/\.[^.]*$//')
      echo "🧩 Component changed: $COMPONENT_NAME"

      # Find tests matching component name
      FOUND_TESTS=$(find tests -name "*${COMPONENT_NAME}*.spec.ts" -o -name "*${COMPONENT_NAME}*.cy.ts" 2>/dev/null || true)
      if [-n "$FOUND_TESTS"]; then
        while IFS= read -r test_file; do
          RELATED_TEST_FILES+=("$test_file")
        done <<< "$FOUND_TESTS"
      fi
      ;;

    # Utility/lib changes: run integration + unit tests
    src/utils/*|src/lib/*|src/helpers/*)
      echo "⚙️  Utility file changed: $file"
      RELATED_TEST_FILES+=($(find tests/unit tests/integration -name "*.spec.ts" 2>/dev/null || true))
      ;;

    # API changes: run integration + e2e tests
    src/api/*|src/services/*|src/controllers/*)
      echo "🔌 API file changed: $file"
      RELATED_TEST_FILES+=($(find tests/integration tests/e2e -name "*.spec.ts" 2>/dev/null || true))
      ;;

    # Type changes: run all TypeScript tests
    *.d.ts|src/types/*)
      echo "📝 Type definition changed: $file"
      RUN_ALL_TESTS=true
      break
      ;;

    # Documentation only: skip tests
    *.md|docs/*|README*)
      echo "📄 Documentation changed: $file (no tests needed)"
      ;;

    *)
      echo "❓ Unclassified change: $file (running smoke tests)"
      RELATED_TEST_FILES+=($(find tests -name "*smoke*.spec.ts" 2>/dev/null || true))
      ;;
  esac
done <<< "$CHANGED_FILES"

# Execute tests based on analysis
if ["$RUN_ALL_TESTS" = true]; then
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "🚨 Running FULL test suite (critical changes detected)"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  npm run test
  exit $?
fi

# Combine and deduplicate test files
ALL_TEST_FILES=(${DIRECT_TEST_FILES[@]} ${RELATED_TEST_FILES[@]})
UNIQUE_TEST_FILES=($(echo "${ALL_TEST_FILES[@]}" | tr ' ' '\n' | sort -u))

if [${#UNIQUE_TEST_FILES[@]} -eq 0]; then
  echo ""
  echo "✅ No tests found for changed files. Running smoke tests."
  npm run test:smoke
  exit $?
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎯 Running ${#UNIQUE_TEST_FILES[@]} test file(s)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

for test_file in "${UNIQUE_TEST_FILES[@]}"; do
  echo "  - $test_file"
done

echo ""
npm run test -- "${UNIQUE_TEST_FILES[@]}"

```

**GitHub Integração das acções**:

```yaml

# .github/workflows/test-changed.yml
name: Test Changed Files
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  detect-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Full history for accurate diff

      - name: Get changed files
        id: changed-files
        uses: tj-actions/changed-files@v40
        with:
          files: |
            src/**
            tests/**
            *.config.ts
          files_ignore: |
            **/*.md
            docs/**

      - name: Run tests for changed files
        if: steps.changed-files.outputs.any_changed == 'true'
        run: |
          echo "Changed files: ${{ steps.changed-files.outputs.all_changed_files }}"
          bash scripts/test-changed-files.sh
        env:
          BASE_BRANCH: ${{ github.base_ref }}
          TEST_ENV: staging

```

**Key Pontos**:

- **Intelligent mapeamento**: Alterações de código → testes relacionados
- **Critical detecção de ficheiros**: Alterações de configuração = pacote completo
- **Component mapping**: Alterações da interface → testes de componente + E2E
- **Fast feedback**: Executar apenas o que é necessário (< 2 min típico)
- **Safety net**: Alterações não reconhecidas executar testes de fumaça

---

### Example 4: Promotion Rules (Pre-Commit → CI → Staging → Production)

**Context**: Progressive test execution strategy across deployment stages.

**Implementation**:

```typescript
// scripts/test-promotion-strategy.ts
/**
 * Test Promotion Strategy
 * Defines which tests run at each stage of the development lifecycle
 */

export type TestStage = 'pre-commit' | 'ci-pr' | 'ci-merge' | 'staging' | 'production';

export type TestPromotion = {
  stage: TestStage;
  description: string;
  testCommand: string;
  timebudget: string; // minutes
  required: boolean;
  failureAction: 'block' | 'warn' | 'alert';
};

export const TEST_PROMOTION_RULES: Record<TestStage, TestPromotion> = {
  'pre-commit': {
    stage: 'pre-commit',
    description: 'Local developer checks before git commit',
    testCommand: 'npm run test:smoke',
    timebudget: '2',
    required: true,
    failureAction: 'block',
  },
  'ci-pr': {
    stage: 'ci-pr',
    description: 'CI checks on pull request creation/update',
    testCommand: 'npm run test:changed && npm run test:p0-p1',
    timebudget: '10',
    required: true,
    failureAction: 'block',
  },
  'ci-merge': {
    stage: 'ci-merge',
    description: 'Full regression before merge to main',
    testCommand: 'npm run test:regression',
    timebudget: '30',
    required: true,
    failureAction: 'block',
  },
  staging: {
    stage: 'staging',
    description: 'Post-deployment validation in staging environment',
    testCommand: 'npm run test:e2e -- --grep "@smoke"',
    timebudget: '15',
    required: true,
    failureAction: 'block',
  },
  production: {
    stage: 'production',
    description: 'Production smoke tests post-deployment',
    testCommand: 'npm run test:e2e:prod -- --grep "@smoke.*@p0"',
    timebudget: '5',
    required: false,
    failureAction: 'alert',
  },
};

/**
 * Get tests to run for a specific stage
 */
export function getTestsForStage(stage: TestStage): TestPromotion {
  return TEST_PROMOTION_RULES[stage];
}

/**
 * Validate if tests can be promoted to next stage
 */
export function canPromote(currentStage: TestStage, testsPassed: boolean): boolean {
  const promotion = TEST_PROMOTION_RULES[currentStage];

  if (!promotion.required) {
    return true; // Non-required tests don't block promotion
  }

  return testsPassed;
}

```

**Husky pre-commit hook**:

```bash
# !/bin/bash

# .husky/pre-commit

# Run smoke tests before allowing commit

echo "🔍 Running pre-commit tests..."

npm run test:smoke

if [$? -ne 0]; then
  echo ""
  echo "❌ Pre-commit tests failed!"
  echo "Please fix failures before committing."
  echo ""
  echo "To skip (NOT recommended): git commit --no-verify"
  exit 1
fi

echo "✅ Pre-commit tests passed"

```

**GitHub Actions workflow**:

```yaml

# .github/workflows/test-promotion.yml
name: Test Promotion Strategy
on:
  pull_request:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  # Stage 1: PR tests (changed + P0-P1)
  pr-tests:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
      - name: Run PR-level tests
        run: |
          npm run test:changed
          npm run test:p0-p1

  # Stage 2: Full regression (pre-merge)
  regression-tests:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
      - name: Run full regression
        run: npm run test:regression

  # Stage 3: Staging validation (post-deploy)
  staging-smoke:
    if: github.event_name == 'workflow_dispatch'
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4
      - name: Run staging smoke tests
        run: npm run test:e2e -- --grep "@smoke"
        env:
          TEST_ENV: staging

  # Stage 4: Production smoke (post-deploy, non-blocking)
  production-smoke:
    if: github.event_name == 'workflow_dispatch'
    runs-on: ubuntu-latest
    timeout-minutes: 5
    continue-on-error: true # Don't fail deployment if smoke tests fail
    steps:
      - uses: actions/checkout@v4
      - name: Run production smoke tests
        run: npm run test:e2e:prod -- --grep "@smoke.*@p0"
        env:
          TEST_ENV: production

      - name: Alert on failure
        if: failure()
        uses: 8398a7/action-slack@v3
        with:
          status: ${{ job.status }}
          text: '🚨 Production smoke tests failed!'
          webhook_url: ${{ secrets.SLACK_WEBHOOK }}

```

**Selection strategy documentation**:

````markdown

# Test Selection Strategy

## Test Promotion Stages

| Stage      | Tests Run           | Time Budget | Blocks Deploy | Failure Action |
| ---------- | ------------------- | ----------- | ------------- | -------------- |
| Pre-Commit | Smoke (@smoke)      | 2 min       | ✅ Yes        | Block commit   |
| CI PR      | Changed + P0-P1     | 10 min      | ✅ Yes        | Block merge    |
| CI Merge   | Full regression     | 30 min      | ✅ Yes        | Block deploy   |
| Staging    | E2E smoke           | 15 min      | ✅ Yes        | Rollback       |
| Production | Critical smoke only | 5 min       | ❌ No         | Alert team     |

## When Full Regression Runs

Full regression suite (`npm run test:regression`) runs in these scenarios:

- ✅ Before merging to `main` (CI Merge stage)
- ✅ Nightly builds (scheduled workflow)
- ✅ Manual trigger (workflow_dispatch)
- ✅ Release candidate testing

Full regression does NOT run on:

- ❌ Every PR commit (too slow)
- ❌ Pre-commit hooks (too slow)
- ❌ Production deployments (deploy-blocking)

## Override Scenarios

Skip tests (emergency only):

```bash
git commit --no-verify  # Skip pre-commit hook
gh pr merge --admin     # Force merge (requires admin)

```
````

```

**Key Points**:
- **Progressive validation**: More tests at each stage
- **Time budgets**: Clear expectations per stage
- **Blocking vs. alerting**: Production tests don't block deploy
- **Documentation**: Team knows when full regression runs
- **Emergency overrides**: Documented but discouraged

---

## Lista de Verificação da Estratégia de Seleção de Testes

Antes da execução dos ensaios selectivos, verificar:

- [ ] **Tag estratégia definida**: @smoke, @p0-p3, @regression documentada
- [ ] **Time budgets set**: Cada fase tem um tempo limite claro (fumo < 5 min, cheio < 30 min)
- [ ] **Changed mapeamento de arquivos**: Alterações de código → lógica de seleção de teste implementada
- [ ] **Promotion regras documentadas**: README explica quando a regressão completa corre
- [ ] **CI integração**: GitHub Actions utiliza estratégia seletiva
- [ ] *BMADPROTECT011FND parity**: Os desenvolvedores podem executar as mesmas seleções localmente
- [ ] **Emergency substitui**: Skip mechanisms documentado (--no-verify, admin merge)
- [ ] **Metrics rastreado**: Monitorar o tempo de execução do teste e precisão de seleção

## Pontos de Integração

- Usado em fluxos de trabalho: `*ci` (configuração IC/CD), `*automate` (geração de teste com etiquetas)
- Fragmentos relacionados: `ci-burn-in.md`, `test-priorities-matrix.md`, `test-quality.md`
- Ferramentas de seleção: Playwright --grep, Cypress @cypress/grep, git diff

_Source: 32+ estratégias de testes seletivos blog, filosofia de teste Murat, otimização SEON CI
«``
