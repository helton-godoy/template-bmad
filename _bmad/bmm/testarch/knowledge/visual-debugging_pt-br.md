# Depuração Visual e Ergonomia do Desenvolvedor

## Princípio

Loops de feedback rápidos e artefatos transparentes de depuração são fundamentais para manter a confiabilidade do teste e confiança do desenvolvedor. Ferramentas de depuração visual (observadores de rastreamento, capturas de tela, vídeos, arquivos HAR) transformam falhas de teste crípticas em insights acionáveis, reduzindo o tempo de triagem de horas para minutos.

## Racional

**The Problem**: Falhas de CI frequentemente fornecem um contexto mínimo – um tempo limite, um erro de seleção ou um erro de rede – obrigando os desenvolvedores a reproduzir problemas localmente (se puderem). Isso perde tempo e desencoraja a manutenção do teste.

**The Solution**: Capture artefatos de depuração ricos **only em falha** para equilibrar os custos de armazenamento com valor diagnóstico. Ferramentas modernas como Playwright Trace Viewer, Cypress Debug UI e gravações HAR fornecem depuração interativa de viagens no tempo que revela exatamente o que o teste viu em cada passo.

**Why Esta questão**:

- Reduz o tempo de triagem de falhas em 80-90% (contexto visual vs logs somente)
- Activa a depuração sem reprodução local
- Melhora a confiança de manutenção do teste (causa raiz de falha clara)
- Condições de tempo de captura/corrida difíceis de reproduzir localmente

## Exemplos de padrões

### Exemplo 1: Configuração do Visualizador de Rastros (Padrão de Produção)

**Context**: Capture traços apenas na primeira repetição (equilibra armazenamento e diagnósticos)

**Implementation**:

```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    // Visual debugging artifacts (space-efficient)
    trace: 'on-first-retry', // Only when test fails once
    screenshot: 'only-on-failure', // Not on success
    video: 'retain-on-failure', // Delete on pass

    // Context for debugging
    baseURL: process.env.BASE_URL || 'http://localhost:3000',

    // Timeout context
    actionTimeout: 15_000, // 15s for clicks/fills
    navigationTimeout: 30_000, // 30s for page loads
  },

  // CI-specific artifact retention
  reporter: [
    ['html', { outputFolder: 'playwright-report', open: 'never' }],
    ['junit', { outputFile: 'results.xml' }],
    ['list'], // Console output
  ],

  // Failure handling
  retries: process.env.CI ? 2 : 0, // Retry in CI to capture trace
  workers: process.env.CI ? 1 : undefined,
});

```

**Opening e Usando Visualizador de Trace**:

```bash

# After test failure in CI, download trace artifact

# Then open locally:
npx playwright show-trace path/to/trace.zip

# Or serve trace viewer:
npx playwright show-report

```

**Key Funcionalidades para Usar no Visualizador de Rastros**:

1. **Timeline**: Veja cada ação (clique, navegue, asserção) com timing
2. **Snapshots**: Passe a linha do tempo para ver o estado DOM naquele momento
3. **Network Tab**: Inspecione todas as chamadas de API, cabeçalhos, cargas, timing
4. **Console Tab**: Ver mensagens do console.log/error
5. **Source Tab**: Ver código de teste com marcadores de execução
6. **Metadata**: Navegador, SO, duração do teste, capturas de tela

**Why Esta obra**:

- `on-first-retry` evita capturar vestígios de passes flácidos (armazenamento de salvas)
- Capturas de tela + vídeo dar contexto visual sem deixar rastros
- A linha do tempo interativa torna óbvios problemas de tempo (condições de corrida, API lenta)

---

### Example 2: HAR File Recording for Network Debugging

**Context**: Capture all network activity for reproducible API debugging

**Implementation**:

```typescript
// tests/e2e/checkout-with-har.spec.ts
import { test, expect } from '@playwright/test';
import path from 'path';

test.describe('Checkout Flow with HAR Recording', () => {
  test('should complete payment with full network capture', async ({ page, context }) => {
    // Start HAR recording BEFORE navigation
    await context.routeFromHAR(path.join(__dirname, '../fixtures/checkout.har'), {
      url: '**/api/**', // Only capture API calls
      update: true, // Update HAR if file exists
    });

    await page.goto('/checkout');

    // Interact with page
    await page.getByTestId('payment-method').selectOption('credit-card');
    await page.getByTestId('card-number').fill('4242424242424242');
    await page.getByTestId('submit-payment').click();

    // Wait for payment confirmation
    await expect(page.getByTestId('success-message')).toBeVisible();

    // HAR file saved to fixtures/checkout.har
    // Contains all network requests/responses for replay
  });
});

```

**Using HAR for Deterministic Mocking**:

```typescript
// tests/e2e/checkout-replay-har.spec.ts
import { test, expect } from '@playwright/test';
import path from 'path';

test('should replay checkout flow from HAR', async ({ page, context }) => {
  // Replay network from HAR (no real API calls)
  await context.routeFromHAR(path.join(__dirname, '../fixtures/checkout.har'), {
    url: '**/api/**',
    update: false, // Read-only mode
  });

  await page.goto('/checkout');

  // Same test, but network responses come from HAR file
  await page.getByTestId('payment-method').selectOption('credit-card');
  await page.getByTestId('card-number').fill('4242424242424242');
  await page.getByTestId('submit-payment').click();

  await expect(page.getByTestId('success-message')).toBeVisible();
});

```

**Key Points**:

- **`update: true`** records new HAR or updates existing (for flaky API debugging)
- **`update: false`** replays from HAR (deterministic, no real API)
- Filter by URL pattern (`**/api/**`) to avoid capturing static assets
- HAR files are human-readable JSON (easy to inspect/modify)

**When to Use HAR**:

- Debugging flaky tests caused by API timing/responses
- Creating deterministic mocks for integration tests
- Analyzing third-party API behavior (Stripe, Auth0)
- Reproducing production issues locally (record HAR in staging)

---

### Exemplo 3: Captura personalizada de artefatos (Logs Console + Rede em falha)

**Context**: Capture o contexto de depuração adicional automaticamente na falha do teste

**Implementation**:

```typescript
// playwright/support/fixtures/debug-fixture.ts
import { test as base } from '@playwright/test';
import fs from 'fs';
import path from 'path';

type DebugFixture = {
  captureDebugArtifacts: () => Promise<void>;
};

export const test = base.extend<DebugFixture>({
  captureDebugArtifacts: async ({ page }, use, testInfo) => {
    const consoleLogs: string[] = [];
    const networkRequests: Array<{ url: string; status: number; method: string }> = [];

    // Capture console messages
    page.on('console', (msg) => {
      consoleLogs.push(`[${msg.type()}] ${msg.text()}`);
    });

    // Capture network requests
    page.on('request', (request) => {
      networkRequests.push({
        url: request.url(),
        method: request.method(),
        status: 0, // Will be updated on response
      });
    });

    page.on('response', (response) => {
      const req = networkRequests.find((r) => r.url === response.url());
      if (req) req.status = response.status();
    });

    await use(async () => {
      // This function can be called manually in tests
      // But it also runs automatically on failure via afterEach
    });

    // After test completes, save artifacts if failed
    if (testInfo.status !== testInfo.expectedStatus) {
      const artifactDir = path.join(testInfo.outputDir, 'debug-artifacts');
      fs.mkdirSync(artifactDir, { recursive: true });

      // Save console logs
      fs.writeFileSync(path.join(artifactDir, 'console.log'), consoleLogs.join('\n'), 'utf-8');

      // Save network summary
      fs.writeFileSync(path.join(artifactDir, 'network.json'), JSON.stringify(networkRequests, null, 2), 'utf-8');

      console.log(`Debug artifacts saved to: ${artifactDir}`);
    }
  },
});

```

**Usage em testes**:

```typescript
// tests/e2e/payment-with-debug.spec.ts
import { test, expect } from '../support/fixtures/debug-fixture';

test('payment flow captures debug artifacts on failure', async ({ page, captureDebugArtifacts }) => {
  await page.goto('/checkout');

  // Test will automatically capture console + network on failure
  await page.getByTestId('submit-payment').click();
  await expect(page.getByTestId('success-message')).toBeVisible({ timeout: 5000 });

  // If this fails, console.log and network.json saved automatically
});

```

**CI Integration (Ações do GitHub)**:

```yaml

# .github/workflows/e2e.yml
name: E2E Tests with Artifacts
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version-file: '.nvmrc'

      - name: Install dependencies
        run: npm ci

      - name: Run Playwright tests
        run: npm run test:e2e
        continue-on-error: true # Capture artifacts even on failure

      - name: Upload test artifacts on failure
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: playwright-artifacts
          path: |
            test-results/
            playwright-report/
          retention-days: 30

```

**Key Pontos**:

- Fixtures capturam automaticamente o contexto sem código de teste poluente
- Só salva artefatos em falhas (eficiente de armazenamento)
- O IC envia artefactos para análise post mortem.
- `continue-on-error: true` garante upload de artefato mesmo quando os testes falham

---

### Example 4: Accessibility Debugging Integration (axe-core in Trace Viewer)

**Context**: Catch accessibility regressions during visual debugging

**Implementation**:

```typescript
// playwright/support/fixtures/a11y-fixture.ts
import { test as base } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

type A11yFixture = {
  checkA11y: () => Promise<void>;
};

export const test = base.extend<A11yFixture>({
  checkA11y: async ({ page }, use) => {
    await use(async () => {
      // Run axe accessibility scan
      const results = await new AxeBuilder({ page }).analyze();

      // Attach results to test report (visible in trace viewer)
      if (results.violations.length > 0) {
        console.log(`Found ${results.violations.length} accessibility violations:`);
        results.violations.forEach((violation) => {
          console.log(`- [${violation.impact}] ${violation.id}: ${violation.description}`);
          console.log(`  Help: ${violation.helpUrl}`);
        });

        throw new Error(`Accessibility violations found: ${results.violations.length}`);
      }
    });
  },
});

```

**Usage with Visual Debugging**:

```typescript
// tests/e2e/checkout-a11y.spec.ts
import { test, expect } from '../support/fixtures/a11y-fixture';

test('checkout page is accessible', async ({ page, checkA11y }) => {
  await page.goto('/checkout');

  // Verify page loaded
  await expect(page.getByRole('heading', { name: 'Checkout' })).toBeVisible();

  // Run accessibility check
  await checkA11y();

  // If violations found, test fails and trace captures:
  // - Screenshot showing the problematic element
  // - Console log with violation details
  // - Network tab showing any failed resource loads
});

```

**Trace Viewer Benefits**:

- **Screenshot shows visual context** of accessibility issue (contrast, missing labels)
- **Console tab shows axe-core violations** with impact level and helpUrl
- **DOM snapshot** allows inspecting ARIA attributes at failure point
- **Network tab** reveals if icon fonts or images failed (common a11y issue)

**Cypress Equivalent**:

```javascript
// cypress/support/commands.ts
import 'cypress-axe';

Cypress.Commands.add('checkA11y', (context = null, options = {}) => {
  cy.injectAxe(); // Inject axe-core
  cy.checkA11y(context, options, (violations) => {
    if (violations.length) {
      cy.task('log', `Found ${violations.length} accessibility violations`);
      violations.forEach((violation) => {
        cy.task('log', `- [${violation.impact}] ${violation.id}: ${violation.description}`);
      });
    }
  });
});

// tests/e2e/checkout-a11y.cy.ts
describe('Checkout Accessibility', () => {
  it('should have no a11y violations', () => {
    cy.visit('/checkout');
    cy.injectAxe();
    cy.checkA11y();
    // On failure, Cypress UI shows:
    // - Screenshot of page
    // - Console log with violation details
    // - Network tab with API calls
  });
});

```

**Key Points**:

- Accessibility checks integrate seamlessly with visual debugging
- Violations are captured in trace viewer/Cypress UI automatically
- Provides actionable links (helpUrl) to fix issues
- Screenshots show visual context (contrast, layout)

---

### Exemplo 5: Fluxo de trabalho de depuração de viagens no tempo (Inspector Playwright)

**Context**: Depurar testes interativos com execução gradual

**Implementation**:

```typescript
// tests/e2e/checkout-debug.spec.ts
import { test, expect } from '@playwright/test';

test('debug checkout flow step-by-step', async ({ page }) => {
  // Set breakpoint by uncommenting this:
  // await page.pause()

  await page.goto('/checkout');

  // Use Playwright Inspector to:
  // 1. Step through each action
  // 2. Inspect DOM at each step
  // 3. View network calls per action
  // 4. Take screenshots manually

  await page.getByTestId('payment-method').selectOption('credit-card');

  // Pause here to inspect form state
  // await page.pause()

  await page.getByTestId('card-number').fill('4242424242424242');
  await page.getByTestId('submit-payment').click();

  await expect(page.getByTestId('success-message')).toBeVisible();
});

```

**Running with Inspector**:

```bash

# Open Playwright Inspector (GUI debugger)
npx playwright test --debug

# Or use headed mode with slowMo
npx playwright test --headed --slow-mo=1000

# Debug specific test
npx playwright test checkout-debug.spec.ts --debug

# Set environment variable for persistent debugging
PWDEBUG=1 npx playwright test

```

**Inspector Características**:

1. **Step-through execução**: Clique em "Next" para executar uma ação de cada vez
2. **DOM inspector**: Hover sobre elementos para ver selectores
3. **Network painel**: Veja chamadas de API com timing
4. **Console painel**: Ver console.log saída
5. **Pick localizador**: Clique no elemento no navegador para obter selector
6. * modo *Record**: Gravar as interacções para gerar o código de ensaio

**Common Padrões de depuração**:

```typescript
// Pattern 1: Debug selector issues
test('debug selector', async ({ page }) => {
  await page.goto('/dashboard');
  await page.pause(); // Inspector opens

  // In Inspector console, test selectors:
  // page.getByTestId('user-menu') ✅
  // page.getByRole('button', { name: 'Profile' }) ✅
  // page.locator('.btn-primary') ❌ (fragile)
});

// Pattern 2: Debug timing issues
test('debug network timing', async ({ page }) => {
  await page.goto('/dashboard');

  // Set up network listener BEFORE interaction
  const responsePromise = page.waitForResponse('**/api/users');
  await page.getByTestId('load-users').click();

  await page.pause(); // Check network panel for timing

  const response = await responsePromise;
  expect(response.status()).toBe(200);
});

// Pattern 3: Debug state changes
test('debug state mutation', async ({ page }) => {
  await page.goto('/cart');

  // Check initial state
  await expect(page.getByTestId('cart-count')).toHaveText('0');

  await page.pause(); // Inspect DOM

  await page.getByTestId('add-to-cart').click();

  await page.pause(); // Inspect DOM again (compare state)

  await expect(page.getByTestId('cart-count')).toHaveText('1');
});

```

**Key Pontos**:

- `page.pause()` abre Inspector nesse exato momento
- Inspetor mostra estado DOM, atividade de rede, console em ponto de pausa
- O recurso "Pick locator" ajuda a encontrar selectores robustos
- Modo de registro gera código de teste a partir de interações manuais

---

## Lista de Verificação de Depuração Visual

Antes de aplicar os testes à IC, garantir:

- [ ] * Configuração *Artifact**: `trace: 'on-first-retry'`, `screenshot: 'only-on-failure'`, `video: 'retain-on-failure'`
- [ ] **CI upload de artefato**: GitHub Actions/GitLab CI configurado para carregar `test-results/` e `playwright-report/`
- [ ] **HAR gravação**: Configurar para testes de API flácida (gravar uma vez, repetir deterministicamente)
- [ ] **Custom dispositivos de depuração**: Registros de console + resumo de rede capturados em falha
- [ ] **Accessibility integração**: violações do núcleo do machado visíveis no visualizador de traços
- [ ] **Trace viewer docs**: README explica como abrir os vestígios localmente (`npx playwright show-trace`)
- [ ] **Inspector fluxo de trabalho**: Documento `--debug` flag for interactive debugging
- [ ] **Storage optimization**: Artefactos suprimidos após 30 dias (política de retenção de IC)

## Pontos de Integração

- **Used em fluxos de trabalho**: `*framework` (configuração inicial), `*ci` (carregamento de artefato), `*test-review` (validação de configuração de artefato)
- **Related fragmentos**: `playwright-config.md` (configuração de artefatos), `ci-burn-in.md` (carregamento de artefatos CI), `test-quality.md` (melhores práticas de depuração)
- **Tools**: Visualizador de traços de dramaturgos, UI de depuração Cypress, arquivos HAR de machados

_Source: Playwright docs oficiais, Murat testing filosophy (visual debugging manifesto), SEON production debugging patterns
