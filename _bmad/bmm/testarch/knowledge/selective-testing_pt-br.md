# Execução de Teste Seletiva e Direcionada

## Princípio

Execute apenas os testes que você precisa, quando você precisa deles. Use tags/grep para fatiar suítes por prioridade de risco (não estrutura de diretório), filtre por padrões de spec ou git diff para focar em áreas impactadas, e combine metadados de prioridade (P0-P3) com detecção de mudança para otimizar execução de pré-commit vs. CI. Documente a estratégia de seleção claramente para que times entendam quando a regressão completa é obrigatória.

## Motivação

Executar a suíte de teste inteira em cada commit desperdiça tempo e recursos. Seleção de teste inteligente fornece feedback rápido (smoke tests em minutos, regressão completa em horas) enquanto mantém confiança. A filosofia de "32+ maneiras de teste seletivo" equilibra velocidade com cobertura: loops rápidos para desenvolvedores, validação abrangente antes do deploy. Seleção mal documentada leva a confusão sobre quando testes rodam e porquê.

## Exemplos de Padrões

### Exemplo 1: Execução Baseada em Tag com Níveis de Prioridade

**Contexto**: Organizar testes por prioridade de risco e estágio de execução usando padrões grep/tag.

**Implementação**:

```typescript
// tests/e2e/checkout.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Organização de teste baseada em tag
 * - @smoke: Testes de caminho crítico (rodar em cada commit, < 5 min)
 * - @regression: Suíte de teste completa (rodar pré-merge, < 30 min)
 * - @p0: Funções de negócio críticas (pagamento, auth, integridade de dados)
 * - @p1: Funcionalidades principais (jornadas de usuário primárias)
 * - @p2: Funcionalidades secundárias (funcionalidade de suporte)
 * - @p3: Bom ter (cosmético, não crítico)
 */

test.describe('Fluxo de Checkout', () => {
  // P0 + Smoke: Deve rodar em cada commit
  test('@smoke @p0 deve completar compra com pagamento válido', async ({ page }) => {
    await page.goto('/checkout');
    await page.getByTestId('card-number').fill('4242424242424242');
    await page.getByTestId('submit-payment').click();

    await expect(page.getByTestId('order-confirmation')).toBeVisible();
  });

  // P0 mas não smoke: Rodar pré-merge
  test('@regression @p0 deve tratar recusa de pagamento graciosamente', async ({ page }) => {
    await page.goto('/checkout');
    await page.getByTestId('card-number').fill('4000000000000002'); // Cartão recusado
    await page.getByTestId('submit-payment').click();

    await expect(page.getByTestId('payment-error')).toBeVisible();
    await expect(page.getByTestId('payment-error')).toContainText('recusado');
  });

  // P1 + Smoke: Importante mas não crítico
  test('@smoke @p1 deve aplicar código de desconto', async ({ page }) => {
    await page.goto('/checkout');
    await page.getByTestId('promo-code').fill('SAVE10');
    await page.getByTestId('apply-promo').click();

    await expect(page.getByTestId('discount-applied')).toBeVisible();
  });

  // P2: Rodar em regressão completa apenas
  test('@regression @p2 deve lembrar métodos de pagamento salvos', async ({ page }) => {
    await page.goto('/checkout');
    await expect(page.getByTestId('saved-cards')).toBeVisible();
  });

  // P3: Baixa prioridade, rodar noturno ou semanal
  test('@nightly @p3 deve exibir analytics da página de checkout', async ({ page }) => {
    await page.goto('/checkout');
    const analyticsEvents = await page.evaluate(() => (window as any).__ANALYTICS__);
    expect(analyticsEvents).toBeDefined();
  });
});
```

**scripts package.json**:

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

**Equivalente Cypress**:

```javascript
// cypress/e2e/checkout.cy.ts
describe('Fluxo de Checkout', { tags: ['@checkout'] }, () => {
  it('deve completar compra', { tags: ['@smoke', '@p0'] }, () => {
    cy.visit('/checkout');
    cy.get('[data-cy="card-number"]').type('4242424242424242');
    cy.get('[data-cy="submit-payment"]').click();
    cy.get('[data-cy="order-confirmation"]').should('be.visible');
  });

  it('deve tratar recusa', { tags: ['@regression', '@p0'] }, () => {
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

**Uso**:

```bash
# Playwright
npm run test:smoke                    # Rodar todos testes @smoke
npm run test:p0                       # Rodar todos testes P0
npm run test -- --grep "@smoke.*@p0"  # Rodar testes com AMBAS tags

# Cypress (com plugin @cypress/grep)
npx cypress run --env grepTags="@smoke"
npx cypress run --env grepTags="@p0+@smoke"  # Lógica E
npx cypress run --env grepTags="@p0 @p1"     # Lógica OU
```

**Pontos Chave**:

- **Múltiplas tags por teste**: Combine prioridade (@p0) com estágio (@smoke)
- **Lógica E/OU**: Grep suporta filtragem complexa
- **Nomeação clara**: Tags documentam importância do teste
- **Feedback rápido**: @smoke roda < 5 min, suíte completa < 30 min
- **Integração CI**: Jobs diferentes rodam combinações de tag diferentes

---

### Exemplo 2: Padrão de Filtro de Spec (Seleção Baseada em Arquivo)

**Contexto**: Rodar testes por padrão de caminho de arquivo ou diretório para execução direcionada.

**Implementação**:

```bash
#!/bin/bash
# scripts/selective-spec-runner.sh
# Rodar testes baseados em padrões de arquivo spec

set -e

PATTERN=${1:-"**/*.spec.ts"}
TEST_ENV=${TEST_ENV:-local}

echo "🎯 Runner Seletivo de Spec"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Padrão: $PATTERN"
echo "Ambiente: $TEST_ENV"
echo ""

# Exemplos de padrão e seus casos de uso
case "$PATTERN" in
  "**/checkout*")
    echo "📦 Rodando testes relacionados a checkout"
    npx playwright test --grep-files="**/checkout*"
    ;;
  "**/auth*"|"**/login*"|"**/signup*")
    echo "🔐 Rodando testes de autenticação"
    npx playwright test --grep-files="**/auth*|**/login*|**/signup*"
    ;;
  "tests/e2e/**")
    echo "🌐 Rodando todos testes E2E"
    npx playwright test tests/e2e/
    ;;
  "tests/integration/**")
    echo "🔌 Rodando todos testes de integração"
    npx playwright test tests/integration/
    ;;
  "tests/component/**")
    echo "🧩 Rodando todos testes de componente"
    npx playwright test tests/component/
    ;;
  *)
    echo "🔍 Rodando testes correspondendo ao padrão: $PATTERN"
    npx playwright test "$PATTERN"
    ;;
esac
```

**Config Playwright para filtragem de arquivo**:

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  // ... outra config

  // Organização baseada em projeto
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

**Correspondência de padrão avançada**:

```typescript
// scripts/run-by-component.ts
/**
 * Rodar testes relacionados a componente(s) específico(s)
 * Uso: npm run test:component UserProfile,Settings
 */

import { execSync } from 'child_process';

const components = process.argv[2]?.split(',') || [];

if (components.length === 0) {
  console.error('❌ Nenhum componente especificado');
  console.log('Uso: npm run test:component UserProfile,Settings');
  process.exit(1);
}

// Converter nomes de componente para padrões glob
const patterns = components.map((comp) => `**/*${comp}*.spec.ts`).join(' ');

console.log(`🧩 Rodando testes para componentes: ${components.join(', ')}`);
console.log(`Padrões: ${patterns}`);

try {
  execSync(`npx playwright test ${patterns}`, {
    stdio: 'inherit',
    env: { ...process.env, CI: 'false' },
  });
} catch (error) {
  process.exit(1);
}
```

**scripts package.json**:

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

**Pontos Chave**:

- **Padrões Glob**: Curingas correspondem a caminhos de arquivo flexivelmente
- **Isolamento de projeto**: Projetos separados têm configs diferentes
- **Alvo de componente**: Rodar testes para features específicas
- **Baseado em diretório**: Organizar testes por tipo (e2e, integração, componente)
- **Otimização CI**: Rodar subconjuntos em jobs CI paralelos

---

### Exemplo 3: Seleção de Teste Baseada em Diff (Apenas Arquivos Alterados)

**Contexto**: Rodar apenas testes afetados por mudanças de código para velocidade máxima.

**Implementação**:

```bash
#!/bin/bash
# scripts/test-changed-files.sh
# Seleção de teste inteligente baseada em git diff

set -e

BASE_BRANCH=${BASE_BRANCH:-main}
TEST_ENV=${TEST_ENV:-local}

echo "🔍 Seletor de Teste de Arquivo Alterado"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Branch base: $BASE_BRANCH"
echo "Ambiente: $TEST_ENV"
echo ""

# Obter arquivos alterados
CHANGED_FILES=$(git diff --name-only $BASE_BRANCH...HEAD)

if [ -z "$CHANGED_FILES" ]; then
  echo "✅ Nenhum arquivo alterado. Pulando testes."
  exit 0
fi

echo "Arquivos alterados:"
echo "$CHANGED_FILES" | sed 's/^/  - /'
echo ""

# Arrays para coletar specs de teste
DIRECT_TEST_FILES=()
RELATED_TEST_FILES=()
RUN_ALL_TESTS=false

# Processar cada arquivo alterado
while IFS= read -r file; do
  case "$file" in
    # Arquivos de teste alterados: rodá-los diretamente
    *.spec.ts|*.spec.js|*.test.ts|*.test.js|*.cy.ts|*.cy.js)
      DIRECT_TEST_FILES+=("$file")
      ;;

    # Mudanças de config crítica: rodar TODOS os testes
    package.json|package-lock.json|playwright.config.ts|cypress.config.ts|tsconfig.json|.github/workflows/*)
      echo "⚠️  Arquivo crítico alterado: $file"
      RUN_ALL_TESTS=true
      break
      ;;

    # Mudanças de componente: encontrar testes relacionados
    src/components/*.tsx|src/components/*.jsx)
      COMPONENT_NAME=$(basename "$file" | sed 's/\.[^.]*$//')
      echo "🧩 Componente alterado: $COMPONENT_NAME"

      # Encontrar testes correspondendo nome do componente
      FOUND_TESTS=$(find tests -name "*${COMPONENT_NAME}*.spec.ts" -o -name "*${COMPONENT_NAME}*.cy.ts" 2>/dev/null || true)
      if [ -n "$FOUND_TESTS" ]; then
        while IFS= read -r test_file; do
          RELATED_TEST_FILES+=("$test_file")
        done <<< "$FOUND_TESTS"
      fi
      ;;

    # Mudanças de utilitário/lib: rodar testes de integração + unitários
    src/utils/*|src/lib/*|src/helpers/*)
      echo "⚙️  Arquivo utilitário alterado: $file"
      RELATED_TEST_FILES+=($(find tests/unit tests/integration -name "*.spec.ts" 2>/dev/null || true))
      ;;

    # Mudanças de API: rodar testes de integração + e2e
    src/api/*|src/services/*|src/controllers/*)
      echo "🔌 Arquivo de API alterado: $file"
      RELATED_TEST_FILES+=($(find tests/integration tests/e2e -name "*.spec.ts" 2>/dev/null || true))
      ;;

    # Mudanças de tipo: rodar todos testes TypeScript
    *.d.ts|src/types/*)
      echo "📝 Definição de tipo alterada: $file"
      RUN_ALL_TESTS=true
      break
      ;;

    # Apenas documentação: pular testes
    *.md|docs/*|README*)
      echo "📄 Documentação alterada: $file (sem testes necessários)"
      ;;

    *)
      echo "❓ Mudança não classificada: $file (rodando smoke tests)"
      RELATED_TEST_FILES+=($(find tests -name "*smoke*.spec.ts" 2>/dev/null || true))
      ;;
  esac
done <<< "$CHANGED_FILES"

# Executar testes baseados em análise
if [ "$RUN_ALL_TESTS" = true ]; then
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "🚨 Rodando suíte de teste COMPLETA (mudanças críticas detectadas)"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  npm run test
  exit $?
fi

# Combinar e deduplicar arquivos de teste
ALL_TEST_FILES=(${DIRECT_TEST_FILES[@]} ${RELATED_TEST_FILES[@]})
UNIQUE_TEST_FILES=($(echo "${ALL_TEST_FILES[@]}" | tr ' ' '\n' | sort -u))

if [ ${#UNIQUE_TEST_FILES[@]} -eq 0 ]; then
  echo ""
  echo "✅ Nenhum teste encontrado para arquivos alterados. Rodando smoke tests."
  npm run test:smoke
  exit $?
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎯 Rodando ${#UNIQUE_TEST_FILES[@]} arquivo(s) de teste"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

for test_file in "${UNIQUE_TEST_FILES[@]}"; do
  echo "  - $test_file"
done

echo ""
npm run test -- "${UNIQUE_TEST_FILES[@]}"
```

**Integração GitHub Actions**:

```yaml
# .github/workflows/test-changed.yml
name: Testar Arquivos Alterados
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  detect-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Histórico completo para diff preciso

      - name: Obter arquivos alterados
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

      - name: Rodar testes para arquivos alterados
        if: steps.changed-files.outputs.any_changed == 'true'
        run: |
          echo "Arquivos alterados: ${{ steps.changed-files.outputs.all_changed_files }}"
          bash scripts/test-changed-files.sh
        env:
          BASE_BRANCH: ${{ github.base_ref }}
          TEST_ENV: staging
```

**Pontos Chave**:

- **Mapeamento inteligente**: Mudanças de código → testes relacionados
- **Detecção de arquivo crítico**: Mudanças de config = suíte completa
- **Mapeamento de componente**: Mudanças de UI → testes de componente + E2E
- **Feedback rápido**: Rodar apenas o que é necessário (< 2 min típico)
- **Rede de segurança**: Mudanças não reconhecidas rodam smoke tests

---

### Exemplo 4: Regras de Promoção (Pré-Commit → CI → Staging → Produção)

**Contexto**: Estratégia de execução de teste progressiva através de estágios de deploy.

**Implementação**:

```typescript
// scripts/test-promotion-strategy.ts
/**
 * Estratégia de Promoção de Teste
 * Define quais testes rodam em cada estágio do ciclo de vida de desenvolvimento
 */

export type TestStage = 'pre-commit' | 'ci-pr' | 'ci-merge' | 'staging' | 'production';

export type TestPromotion = {
  stage: TestStage;
  description: string;
  testCommand: string;
  timebudget: string; // minutos
  required: boolean;
  failureAction: 'block' | 'warn' | 'alert';
};

export const TEST_PROMOTION_RULES: Record<TestStage, TestPromotion> = {
  'pre-commit': {
    stage: 'pre-commit',
    description: 'Verificações locais do desenvolvedor antes do commit git',
    testCommand: 'npm run test:smoke',
    timebudget: '2',
    required: true,
    failureAction: 'block',
  },
  'ci-pr': {
    stage: 'ci-pr',
    description: 'Verificações CI na criação/atualização de pull request',
    testCommand: 'npm run test:changed && npm run test:p0-p1',
    timebudget: '10',
    required: true,
    failureAction: 'block',
  },
  'ci-merge': {
    stage: 'ci-merge',
    description: 'Regressão completa antes de mergear para main',
    testCommand: 'npm run test:regression',
    timebudget: '30',
    required: true,
    failureAction: 'block',
  },
  staging: {
    stage: 'staging',
    description: 'Validação pós-deploy em ambiente staging',
    testCommand: 'npm run test:e2e -- --grep "@smoke"',
    timebudget: '15',
    required: true,
    failureAction: 'block',
  },
  production: {
    stage: 'production',
    description: 'Testes smoke de produção pós-deploy',
    testCommand: 'npm run test:e2e:prod -- --grep "@smoke.*@p0"',
    timebudget: '5',
    required: false,
    failureAction: 'alert',
  },
};

/**
 * Obter testes para rodar para um estágio específico
 */
export function getTestsForStage(stage: TestStage): TestPromotion {
  return TEST_PROMOTION_RULES[stage];
}

/**
 * Validar se testes podem ser promovidos para próximo estágio
 */
export function canPromote(currentStage: TestStage, testsPassed: boolean): boolean {
  const promotion = TEST_PROMOTION_RULES[currentStage];

  if (!promotion.required) {
    return true; // Testes não obrigatórios não bloqueiam promoção
  }

  return testsPassed;
}
```

**Hook pré-commit Husky**:

```bash
#!/bin/bash
# .husky/pre-commit
# Rodar testes smoke antes de permitir commit

echo "🔍 Rodando testes pré-commit..."

npm run test:smoke

if [ $? -ne 0 ]; then
  echo ""
  echo "❌ Testes pré-commit falharam!"
  echo "Por favor corrija falhas antes de commitar."
  echo ""
  echo "Para pular (NÃO recomendado): git commit --no-verify"
  exit 1
fi

echo "✅ Testes pré-commit passaram"
```

**Workflow GitHub Actions**:

```yaml
# .github/workflows/test-promotion.yml
name: Estratégia de Promoção de Teste
on:
  pull_request:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  # Estágio 1: Testes PR (alterados + P0-P1)
  pr-tests:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
      - name: Rodar testes nível PR
        run: |
          npm run test:changed
          npm run test:p0-p1

  # Estágio 2: Regressão completa (pré-merge)
  regression-tests:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
      - name: Rodar regressão completa
        run: npm run test:regression

  # Estágio 3: Validação staging (pós-deploy)
  staging-smoke:
    if: github.event_name == 'workflow_dispatch'
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4
      - name: Rodar smoke tests staging
        run: npm run test:e2e -- --grep "@smoke"
        env:
          TEST_ENV: staging

  # Estágio 4: Smoke produção (pós-deploy, não bloqueante)
  production-smoke:
    if: github.event_name == 'workflow_dispatch'
    runs-on: ubuntu-latest
    timeout-minutes: 5
    continue-on-error: true # Não falhar deploy se smoke tests falharem
    steps:
      - uses: actions/checkout@v4
      - name: Rodar smoke tests produção
        run: npm run test:e2e:prod -- --grep "@smoke.*@p0"
        env:
          TEST_ENV: production

      - name: Alertar na falha
        if: failure()
        uses: 8398a7/action-slack@v3
        with:
          status: ${{ job.status }}
          text: '🚨 Smoke tests de produção falharam!'
          webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

**Documentação de estratégia de seleção**:

````markdown
# Estratégia de Seleção de Teste

## Estágios de Promoção de Teste

| Estágio    | Testes Rodados      | Orçamento de Tempo | Bloqueia Deploy | Ação de Falha  |
| ---------- | ------------------- | ------------------ | --------------- | -------------- |
| Pré-Commit | Smoke (@smoke)      | 2 min              | ✅ Sim          | Bloquear commit|
| CI PR      | Alterados + P0-P1   | 10 min             | ✅ Sim          | Bloquear merge |
| CI Merge   | Regressão completa  | 30 min             | ✅ Sim          | Bloquear deploy|
| Staging    | E2E smoke           | 15 min             | ✅ Sim          | Rollback       |
| Produção   | Smoke crítico apenas| 5 min              | ❌ Não          | Alertar time   |

## Quando Regressão Completa Roda

Suíte de regressão completa (`npm run test:regression`) roda nestes cenários:

- ✅ Antes de mergear para `main` (Estágio CI Merge)
- ✅ Builds noturnas (workflow agendado)
- ✅ Gatilho manual (workflow_dispatch)
- ✅ Teste de Release Candidate

Regressão completa NÃO roda em:

- ❌ Todo commit de PR (muito lento)
- ❌ Hooks pré-commit (muito lento)
- ❌ Deploys de produção (bloqueia deploy)

## Cenários de Override

Pular testes (apenas emergência):

```bash
git commit --no-verify  # Pular hook pré-commit
gh pr merge --admin     # Forçar merge (requer admin)
```
````

**Pontos Chave**:
- **Validação progressiva**: Mais testes em cada estágio
- **Orçamentos de tempo**: Expectativas claras por estágio
- **Bloquear vs. alertar**: Testes de produção não bloqueiam deploy
- **Documentação**: Time sabe quando regressão completa roda
- **Overrides de emergência**: Documentados mas desencorajados

---

## Checklist de Estratégia de Seleção de Teste

Antes de implementar teste seletivo, verifique:

- [ ] **Estratégia de tag definida**: @smoke, @p0-p3, @regression documentados
- [ ] **Orçamentos de tempo definidos**: Cada estágio tem timeout claro (smoke < 5 min, full < 30 min)
- [ ] **Mapeamento de arquivo alterado**: Mudanças de código → lógica de seleção de teste implementada
- [ ] **Regras de promoção documentadas**: README explica quando regressão completa roda
- [ ] **Integração CI**: GitHub Actions usa estratégia seletiva
- [ ] **Paridade local**: Desenvolvedores podem rodar mesmas seleções localmente
- [ ] **Overrides de emergência**: Mecanismos de pular documentados (--no-verify, admin merge)
- [ ] **Métricas rastreadas**: Monitorar tempo de execução de teste e precisão de seleção

## Pontos de Integração

- Usado em workflows: `*ci` (setup CI/CD), `*automate` (geração de teste com tags)
- Fragmentos relacionados: `ci-burn-in.md`, `test-priorities-matrix.md`, `test-quality.md`
- Ferramentas de seleção: Playwright --grep, Cypress @cypress/grep, git diff

_Fonte: Blog 32+ estratégias de teste seletivo, filosofia de teste Murat, otimização CI SEON_
