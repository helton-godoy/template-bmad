# Verificação de Erros e Resiliência

## Princípio

Trate explicitamente falhas esperadas: intercepte erros de rede, assevere fallbacks de UI (mensagens de erro visíveis, repetições acionadas) e use o gerenciamento de exceções escopo para ignorar erros conhecidos durante a captura de regressões. Teste a lógica de repetição/backoff forçando falhas sequenciais (500 → timeout → sucesso) e valide o registro de telemetria. Registre erros capturados com contexto (pedir carga útil, usuário/sessão) mas redigir segredos para manter artefatos seguros para compartilhamento.

## Racional

Os testes falham por duas razões: erros genuínos ou mau manuseio de erros no teste em si. Sem padrões explícitos de manipulação de erros, testes tornam-se barulhentos (excepções não captadas causam falhas false) ou silenciosos (swallowing todos os erros esconde erros reais). Manuseamento de exceção escopo (Cypress.on('não pego: exceção'), page.on('pageerror')) permite que os testes ignorem erros documentados e esperados enquanto surgem inesperados. Teste de resiliência (lógica de repetição, degradação graciosa) garante que as aplicações manuseiam falhas graciosamente na produção.

## Exemplos de padrões

### Exemplo 1: Tratamento de exceção escopo (apenas erros esperados)

**Context**: Lidar com erros conhecidos (falhas de rede, esperado 500s) sem mascarar bugs inesperados.

**Implementation**:

```typescript
// tests/e2e/error-handling.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Scoped Error Handling Pattern
 * - Only ignore specific, documented errors
 * - Rethrow everything else to catch regressions
 * - Validate error UI and user experience
 */

test.describe('API Error Handling', () => {
  test('should display error message when API returns 500', async ({ page }) => {
    // Scope error handling to THIS test only
    const consoleErrors: string[] = [];
    page.on('pageerror', (error) => {
      // Only swallow documented NetworkError
      if (error.message.includes('NetworkError: Failed to fetch')) {
        consoleErrors.push(error.message);
        return; // Swallow this specific error
      }
      // Rethrow all other errors (catch regressions!)
      throw error;
    });

    // Arrange: Mock 500 error response
    await page.route('**/api/users', (route) =>
      route.fulfill({
        status: 500,
        contentType: 'application/json',
        body: JSON.stringify({
          error: 'Internal server error',
          code: 'INTERNAL_ERROR',
        }),
      }),
    );

    // Act: Navigate to page that fetches users
    await page.goto('/dashboard');

    // Assert: Error UI displayed
    await expect(page.getByTestId('error-message')).toBeVisible();
    await expect(page.getByTestId('error-message')).toContainText(/error.*loading|failed.*load/i);

    // Assert: Retry button visible
    await expect(page.getByTestId('retry-button')).toBeVisible();

    // Assert: NetworkError was thrown and caught
    expect(consoleErrors).toContainEqual(expect.stringContaining('NetworkError'));
  });

  test('should NOT swallow unexpected errors', async ({ page }) => {
    let unexpectedError: Error | null = null;

    page.on('pageerror', (error) => {
      // Capture but don't swallow - test should fail
      unexpectedError = error;
      throw error;
    });

    // Arrange: App has JavaScript error (bug)
    await page.addInitScript(() => {
      // Simulate bug in app code
      (window as any).buggyFunction = () => {
        throw new Error('UNEXPECTED BUG: undefined is not a function');
      };
    });

    await page.goto('/dashboard');

    // Trigger buggy function
    await page.evaluate(() => (window as any).buggyFunction());

    // Assert: Test fails because unexpected error was NOT swallowed
    expect(unexpectedError).not.toBeNull();
    expect(unexpectedError?.message).toContain('UNEXPECTED BUG');
  });
});

```

**Cypress equivalente**:

```javascript
// cypress/e2e/error-handling.cy.ts
describe('API Error Handling', () => {
  it('should display error message when API returns 500', () => {
    // Scoped to this test only
    cy.on('uncaught:exception', (err) => {
      // Only swallow documented NetworkError
      if (err.message.includes('NetworkError')) {
        return false; // Prevent test failure
      }
      // All other errors fail the test
      return true;
    });

    // Arrange: Mock 500 error
    cy.intercept('GET', '**/api/users', {
      statusCode: 500,
      body: {
        error: 'Internal server error',
        code: 'INTERNAL_ERROR',
      },
    }).as('getUsers');

    // Act
    cy.visit('/dashboard');
    cy.wait('@getUsers');

    // Assert: Error UI
    cy.get('[data-cy="error-message"]').should('be.visible');
    cy.get('[data-cy="error-message"]').should('contain', 'error loading');
    cy.get('[data-cy="retry-button"]').should('be.visible');
  });

  it('should NOT swallow unexpected errors', () => {
    // No exception handler - test should fail on unexpected errors

    cy.visit('/dashboard');

    // Trigger unexpected error
    cy.window().then((win) => {
      // This should fail the test
      win.eval('throw new Error("UNEXPECTED BUG")');
    });

    // Test fails (as expected) - validates error detection works
  });
});

```

**Key Pontos**:

- **Scoped handling**: page.on() / cy.on() escopo para testes específicos
- **Explicit allow- list**: Ignorar apenas os erros documentados
- **Rethrow inesperado**: Regressões de captura falhando em erros desconhecidos
- **Error validação da IU**: Usuário de asserção vê mensagem de erro
- **Logging**: Capturar erros para depuração, não engolir silenciosamente

---

### Example 2: Retry Validation Pattern (Network Resilience)

**Context**: Test that retry/backoff logic works correctly for transient failures.

**Implementation**:

```typescript
// tests/e2e/retry-resilience.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Retry Validation Pattern
 * - Force sequential failures (500 → 500 → 200)
 * - Validate retry attempts and backoff timing
 * - Assert telemetry captures retry events
 */

test.describe('Network Retry Logic', () => {
  test('should retry on 500 error and succeed', async ({ page }) => {
    let attemptCount = 0;
    const attemptTimestamps: number[] = [];

    // Mock API: Fail twice, succeed on third attempt
    await page.route('**/api/products', (route) => {
      attemptCount++;
      attemptTimestamps.push(Date.now());

      if (attemptCount <= 2) {
        // First 2 attempts: 500 error
        route.fulfill({
          status: 500,
          body: JSON.stringify({ error: 'Server error' }),
        });
      } else {
        // 3rd attempt: Success
        route.fulfill({
          status: 200,
          contentType: 'application/json',
          body: JSON.stringify({ products: [{ id: 1, name: 'Product 1' }] }),
        });
      }
    });

    // Act: Navigate (should retry automatically)
    await page.goto('/products');

    // Assert: Data eventually loads after retries
    await expect(page.getByTestId('product-list')).toBeVisible();
    await expect(page.getByTestId('product-item')).toHaveCount(1);

    // Assert: Exactly 3 attempts made
    expect(attemptCount).toBe(3);

    // Assert: Exponential backoff timing (1s → 2s between attempts)
    if (attemptTimestamps.length === 3) {
      const delay1 = attemptTimestamps[1] - attemptTimestamps[0];
      const delay2 = attemptTimestamps[2] - attemptTimestamps[1];

      expect(delay1).toBeGreaterThanOrEqual(900); // ~1 second
      expect(delay1).toBeLessThan(1200);
      expect(delay2).toBeGreaterThanOrEqual(1900); // ~2 seconds
      expect(delay2).toBeLessThan(2200);
    }

    // Assert: Telemetry logged retry events
    const telemetryEvents = await page.evaluate(() => (window as any).__TELEMETRY_EVENTS__ || []);
    expect(telemetryEvents).toContainEqual(
      expect.objectContaining({
        event: 'api_retry',
        attempt: 1,
        endpoint: '/api/products',
      }),
    );
    expect(telemetryEvents).toContainEqual(
      expect.objectContaining({
        event: 'api_retry',
        attempt: 2,
      }),
    );
  });

  test('should give up after max retries and show error', async ({ page }) => {
    let attemptCount = 0;

    // Mock API: Always fail (test retry limit)
    await page.route('**/api/products', (route) => {
      attemptCount++;
      route.fulfill({
        status: 500,
        body: JSON.stringify({ error: 'Persistent server error' }),
      });
    });

    // Act
    await page.goto('/products');

    // Assert: Max retries reached (3 attempts typical)
    expect(attemptCount).toBe(3);

    // Assert: Error UI displayed after exhausting retries
    await expect(page.getByTestId('error-message')).toBeVisible();
    await expect(page.getByTestId('error-message')).toContainText(/unable.*load|failed.*after.*retries/i);

    // Assert: Data not displayed
    await expect(page.getByTestId('product-list')).not.toBeVisible();
  });

  test('should NOT retry on 404 (non-retryable error)', async ({ page }) => {
    let attemptCount = 0;

    // Mock API: 404 error (should NOT retry)
    await page.route('**/api/products/999', (route) => {
      attemptCount++;
      route.fulfill({
        status: 404,
        body: JSON.stringify({ error: 'Product not found' }),
      });
    });

    await page.goto('/products/999');

    // Assert: Only 1 attempt (no retries on 404)
    expect(attemptCount).toBe(1);

    // Assert: 404 error displayed immediately
    await expect(page.getByTestId('not-found-message')).toBeVisible();
  });
});

```

**Cypress with retry interception**:

```javascript
// cypress/e2e/retry-resilience.cy.ts
describe('Network Retry Logic', () => {
  it('should retry on 500 and succeed on 3rd attempt', () => {
    let attemptCount = 0;

    cy.intercept('GET', '**/api/products', (req) => {
      attemptCount++;

      if (attemptCount <= 2) {
        req.reply({ statusCode: 500, body: { error: 'Server error' } });
      } else {
        req.reply({ statusCode: 200, body: { products: [{ id: 1, name: 'Product 1' }] } });
      }
    }).as('getProducts');

    cy.visit('/products');

    // Wait for final successful request
    cy.wait('@getProducts').its('response.statusCode').should('eq', 200);

    // Assert: Data loaded
    cy.get('[data-cy="product-list"]').should('be.visible');
    cy.get('[data-cy="product-item"]').should('have.length', 1);

    // Validate retry count
    cy.wrap(attemptCount).should('eq', 3);
  });
});

```

**Key Points**:

- **Sequential failures**: Test retry logic with 500 → 500 → 200
- **Backoff timing**: Validate exponential backoff delays
- **Retry limits**: Max attempts enforced (typically 3)
- **Non-retryable errors**: 404s don't trigger retries
- **Telemetry**: Log retry attempts for monitoring

---

### Exemplo 3: Registro de Telemetria com Contexto (Integração de Entrada)

**Context**: Capture erros com contexto completo para depuração de produção sem expor segredos.

**Implementation**:

```typescript
// tests/e2e/telemetry-logging.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Telemetry Logging Pattern
 * - Log errors with request context
 * - Redact sensitive data (tokens, passwords, PII)
 * - Integrate with monitoring (Sentry, Datadog)
 * - Validate error logging without exposing secrets
 */

type ErrorLog = {
  level: 'error' | 'warn' | 'info';
  message: string;
  context?: {
    endpoint?: string;
    method?: string;
    statusCode?: number;
    userId?: string;
    sessionId?: string;
  };
  timestamp: string;
};

test.describe('Error Telemetry', () => {
  test('should log API errors with context', async ({ page }) => {
    const errorLogs: ErrorLog[] = [];

    // Capture console errors
    page.on('console', (msg) => {
      if (msg.type() === 'error') {
        try {
          const log = JSON.parse(msg.text());
          errorLogs.push(log);
        } catch {
          // Not a structured log, ignore
        }
      }
    });

    // Mock failing API
    await page.route('**/api/orders', (route) =>
      route.fulfill({
        status: 500,
        body: JSON.stringify({ error: 'Payment processor unavailable' }),
      }),
    );

    // Act: Trigger error
    await page.goto('/checkout');
    await page.getByTestId('place-order').click();

    // Wait for error UI
    await expect(page.getByTestId('error-message')).toBeVisible();

    // Assert: Error logged with context
    expect(errorLogs).toContainEqual(
      expect.objectContaining({
        level: 'error',
        message: expect.stringContaining('API request failed'),
        context: expect.objectContaining({
          endpoint: '/api/orders',
          method: 'POST',
          statusCode: 500,
          userId: expect.any(String),
        }),
      }),
    );

    // Assert: Sensitive data NOT logged
    const logString = JSON.stringify(errorLogs);
    expect(logString).not.toContain('password');
    expect(logString).not.toContain('token');
    expect(logString).not.toContain('creditCard');
  });

  test('should send errors to Sentry with breadcrumbs', async ({ page }) => {
    const sentryEvents: any[] = [];

    // Mock Sentry SDK
    await page.addInitScript(() => {
      (window as any).Sentry = {
        captureException: (error: Error, context?: any) => {
          (window as any).__SENTRY_EVENTS__= (window as any).__SENTRY_EVENTS__ || [];
          (window as any).__SENTRY_EVENTS__.push({
            error: error.message,
            context,
            timestamp: Date.now(),
          });
        },
        addBreadcrumb: (breadcrumb: any) => {
          (window as any).__SENTRY_BREADCRUMBS__= (window as any).__SENTRY_BREADCRUMBS__ || [];
          (window as any).__SENTRY_BREADCRUMBS__.push(breadcrumb);
        },
      };
    });

    // Mock failing API
    await page.route('**/api/users', (route) => route.fulfill({ status: 403, body: { error: 'Forbidden' } }));

    // Act
    await page.goto('/users');

    // Assert: Sentry captured error
    const events = await page.evaluate(() => (window as any).__SENTRY_EVENTS__);
    expect(events).toHaveLength(1);
    expect(events[0]).toMatchObject({
      error: expect.stringContaining('403'),
      context: expect.objectContaining({
        endpoint: '/api/users',
        statusCode: 403,
      }),
    });

    // Assert: Breadcrumbs include user actions
    const breadcrumbs = await page.evaluate(() => (window as any).__SENTRY_BREADCRUMBS__);
    expect(breadcrumbs).toContainEqual(
      expect.objectContaining({
        category: 'navigation',
        message: '/users',
      }),
    );
  });
});

```

**CypressER com Sentry**:

```javascript
// cypress/e2e/telemetry-logging.cy.ts
describe('Error Telemetry', () => {
  it('should log API errors with redacted sensitive data', () => {
    const errorLogs = [];

    // Capture console errors
    cy.on('window:before:load', (win) => {
      cy.stub(win.console, 'error').callsFake((msg) => {
        errorLogs.push(msg);
      });
    });

    // Mock failing API
    cy.intercept('POST', '**/api/orders', {
      statusCode: 500,
      body: { error: 'Payment failed' },
    });

    // Act
    cy.visit('/checkout');
    cy.get('[data-cy="place-order"]').click();

    // Assert: Error logged
    cy.wrap(errorLogs).should('have.length.greaterThan', 0);

    // Assert: Context included
    cy.wrap(errorLogs[0]).should('include', '/api/orders');

    // Assert: Secrets redacted
    cy.wrap(JSON.stringify(errorLogs)).should('not.contain', 'password');
    cy.wrap(JSON.stringify(errorLogs)).should('not.contain', 'creditCard');
  });
});

```

**Error utilitário logger com redaction**:

```typescript
// src/utils/error-logger.ts
type ErrorContext = {
  endpoint?: string;
  method?: string;
  statusCode?: number;
  userId?: string;
  sessionId?: string;
  requestPayload?: any;
};

const SENSITIVE_KEYS = ['password', 'token', 'creditCard', 'ssn', 'apiKey'];

/**
 * Redact sensitive data from objects
 */
function redactSensitiveData(obj: any): any {
  if (typeof obj !== 'object' || obj === null) return obj;

  const redacted = { ...obj };

  for (const key of Object.keys(redacted)) {
    if (SENSITIVE_KEYS.some((sensitive) => key.toLowerCase().includes(sensitive))) {
      redacted[key] = '[REDACTED]';
    } else if (typeof redacted[key] === 'object') {
      redacted[key] = redactSensitiveData(redacted[key]);
    }
  }

  return redacted;
}

/**
 * Log error with context (Sentry integration)
 */
export function logError(error: Error, context?: ErrorContext) {
  const safeContext = context ? redactSensitiveData(context) : {};

  const errorLog = {
    level: 'error' as const,
    message: error.message,
    stack: error.stack,
    context: safeContext,
    timestamp: new Date().toISOString(),
  };

  // Console (development)
  console.error(JSON.stringify(errorLog));

  // Sentry (production)
  if (typeof window !== 'undefined' && (window as any).Sentry) {
    (window as any).Sentry.captureException(error, {
      contexts: { custom: safeContext },
    });
  }
}

```

**Key Pontos**:

- **Context-rich loging**: Ponto final, método, estado, ID do utilizador
- **Secret redaction**: Senhas, fichas, PII removidas antes do registo
- integração *Sentry**: Monitoramento da produção com migalhas de pão
- **Structured logs**: formato JSON para fácil análise
- **Test validação**: Registros de reservas contêm contexto, mas não segredos

---

### Example 4: Graceful Degradation Tests (Fallback Behavior)

**Context**: Validate application continues functioning when services are unavailable.

**Implementation**:

```typescript
// tests/e2e/graceful-degradation.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Graceful Degradation Pattern
 * - Simulate service unavailability
 * - Validate fallback behavior
 * - Ensure user experience degrades gracefully
 * - Verify telemetry captures degradation events
 */

test.describe('Service Unavailability', () => {
  test('should display cached data when API is down', async ({ page }) => {
    // Arrange: Seed localStorage with cached data
    await page.addInitScript(() => {
      localStorage.setItem(
        'products_cache',
        JSON.stringify({
          data: [
            { id: 1, name: 'Cached Product 1' },
            { id: 2, name: 'Cached Product 2' },
          ],
          timestamp: Date.now(),
        }),
      );
    });

    // Mock API unavailable
    await page.route(
      '**/api/products',
      (route) => route.abort('connectionrefused'), // Simulate server down
    );

    // Act
    await page.goto('/products');

    // Assert: Cached data displayed
    await expect(page.getByTestId('product-list')).toBeVisible();
    await expect(page.getByText('Cached Product 1')).toBeVisible();

    // Assert: Stale data warning shown
    await expect(page.getByTestId('cache-warning')).toBeVisible();
    await expect(page.getByTestId('cache-warning')).toContainText(/showing.*cached|offline.*mode/i);

    // Assert: Retry button available
    await expect(page.getByTestId('refresh-button')).toBeVisible();
  });

  test('should show fallback UI when analytics service fails', async ({ page }) => {
    // Mock analytics service down (non-critical)
    await page.route('**/analytics/track', (route) => route.fulfill({ status: 503, body: 'Service unavailable' }));

    // Act: Navigate normally
    await page.goto('/dashboard');

    // Assert: Page loads successfully (analytics failure doesn't block)
    await expect(page.getByTestId('dashboard-content')).toBeVisible();

    // Assert: Analytics error logged but not shown to user
    const consoleErrors = [];
    page.on('console', (msg) => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });

    // Trigger analytics event
    await page.getByTestId('track-action-button').click();

    // Analytics error logged
    expect(consoleErrors).toContainEqual(expect.stringContaining('Analytics service unavailable'));

    // But user doesn't see error
    await expect(page.getByTestId('error-message')).not.toBeVisible();
  });

  test('should fallback to local validation when API is slow', async ({ page }) => {
    // Mock slow API (> 5 seconds)
    await page.route('**/api/validate-email', async (route) => {
      await new Promise((resolve) => setTimeout(resolve, 6000)); // 6 second delay
      route.fulfill({
        status: 200,
        body: JSON.stringify({ valid: true }),
      });
    });

    // Act: Fill form
    await page.goto('/signup');
    await page.getByTestId('email-input').fill('test@example.com');
    await page.getByTestId('email-input').blur();

    // Assert: Client-side validation triggers immediately (doesn't wait for API)
    await expect(page.getByTestId('email-valid-icon')).toBeVisible({ timeout: 1000 });

    // Assert: Eventually API validates too (but doesn't block UX)
    await expect(page.getByTestId('email-validated-badge')).toBeVisible({ timeout: 7000 });
  });

  test('should maintain functionality with third-party script failure', async ({ page }) => {
    // Block third-party scripts (Google Analytics, Intercom, etc.)
    await page.route('**/*.google-analytics.com/**', (route) => route.abort());
    await page.route('**/*.intercom.io/**', (route) => route.abort());

    // Act
    await page.goto('/');

    // Assert: App works without third-party scripts
    await expect(page.getByTestId('main-content')).toBeVisible();
    await expect(page.getByTestId('nav-menu')).toBeVisible();

    // Assert: Core functionality intact
    await page.getByTestId('nav-products').click();
    await expect(page).toHaveURL(/.*\/products/);
  });
});

```

**Key Points**:

- **Cached fallbacks**: Display stale data when API unavailable
- **Non-critical degradation**: Analytics failures don't block app
- **Client-side fallbacks**: Local validation when API slow
- **Third-party resilience**: App works without external scripts
- **User transparency**: Stale data warnings displayed

---

## Lista de Verificação de Controlo de Tratamento de Erros

Antes do código de manipulação de erros de envio, verifique:

- [ ] **Scoped exception handling**: Ignorar apenas erros documentados (error de rede, códigos específicos)
- [ ] **Rethrow inesperado**: Ensaios de falha de erros desconhecidos (regressões de capturas)
- [ ] **Error UI testada**: O usuário vê mensagens de erro para todos os estados de erro
- [ ] * lógica *Retry validada**: Falhas sequenciais testar backoff e tentativas máximas
- [ ] **Telemetry verificado**: Erros registrados com o contexto (endpoint, status, usuário)
- [ ] **Secret redação**: Os logs não contêm senhas, tokens, PII
- [ ] **Graceful degradação**: Serviços críticos para baixo, aplicativo mostra interface traseira
- [ ] **Non-critical falhas**: Falhas de análise/rastreamento não bloqueiam o aplicativo

## Pontos de Integração

- Usado em fluxos de trabalho: `*automate` (geração de testes de manipulação de erros), `*test-review` (detecção de padrões de erros)
- Fragmentos relacionados: `network-first.md`, `test-quality.md`, `contract-testing.md`
- Ferramentas de monitoramento: Sentry, Datadog, LogRocket

_Source: Murat padrões de manipulação de erros, orientação de resiliência do Pacto, manipulação de erros de produção SEON
