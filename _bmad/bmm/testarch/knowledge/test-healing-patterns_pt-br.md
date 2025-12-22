# Teste padrões de cura

## Princípio

Falhas comuns de teste seguem padrões previsíveis (selecionadores de estacas, condições de corrida, afirmações dinâmicas de dados, erros de rede, esperas difíceis). **Automated healing** identifica assinaturas de falha e aplica correções baseadas em padrões. Cura manual captura esses padrões para automação futura.

## Racional

**The Problem**: Falhas de teste desperdiçam tempo de desenvolvimento em depuração repetitiva. As equipes consertam manualmente os mesmos problemas de selecionador, erros de tempo e dados que se confundem repetidamente em suítes de teste.

**The Solution**: Catalogue padrões de falha comuns com assinaturas diagnósticas e correções automatizadas. Quando um teste falhar, combine a mensagem de erro/rastreamento de stack com padrões conhecidos e aplique a correção correspondente. Isso transforma a manutenção do teste de depuração reativa em aplicação de padrão proativo.

**Why Esta questão**:

- Reduz o tempo de manutenção do teste em 60-80% (correcções baseadas em padrões vs depuração manual)
- Previne regressão de flakiness (mesmo erro corrigido uma vez, aplicado em toda parte)
- Construi conhecimento institucional (catálogo de falha cresce ao longo do tempo)
- Habilita suítes de teste de auto-cura (valida e cura automaticamente o fluxo de trabalho)

## Exemplos de padrões

### Exemplo 1: Padrão de falha comum - Seletores de impasse (elemento não encontrado)

**Context**: Falha no teste com os erros "Elemento não encontrado" ou "Localizador resolvido para 0 elementos"

**Diagnostic Assinatura**:

```typescript
// src/testing/healing/selector-healing.ts

export type SelectorFailure = {
  errorMessage: string;
  stackTrace: string;
  selector: string;
  testFile: string;
  lineNumber: number;
};

/**
 * Detect stale selector failures
 */
export function isSelectorFailure(error: Error): boolean {
  const patterns = [
    /locator.*resolved to 0 elements/i,
    /element not found/i,
    /waiting for locator.*to be visible/i,
    /selector.*did not match any elements/i,
    /unable to find element/i,
  ];

  return patterns.some((pattern) => pattern.test(error.message));
}

/**
 * Extract selector from error message
 */
export function extractSelector(errorMessage: string): string | null {
  // Playwright: "locator('button[type=\"submit\"]') resolved to 0 elements"
  const playwrightMatch = errorMessage.match(/locator\('([^']+)'\)/);
  if (playwrightMatch) return playwrightMatch[1];

  // Cypress: "Timed out retrying: Expected to find element: '.submit-button'"
  const cypressMatch = errorMessage.match(/Expected to find element: ['"]([^'"]+)['"]/i);
  if (cypressMatch) return cypressMatch[1];

  return null;
}

/**
 * Suggest better selector based on hierarchy
 */
export function suggestBetterSelector(badSelector: string): string {
  // If using CSS class → suggest data-testid
  if (badSelector.startsWith('.') || badSelector.includes('class=')) {
    const elementName = badSelector.match(/class=["']([^"']+)["']/)?.[1] || badSelector.slice(1);
    return `page.getByTestId('${elementName}') // Prefer data-testid over CSS class`;
  }

  // If using ID → suggest data-testid
  if (badSelector.startsWith('#')) {
    return `page.getByTestId('${badSelector.slice(1)}') // Prefer data-testid over ID`;
  }

  // If using nth() → suggest filter() or more specific selector
  if (badSelector.includes('.nth(')) {
    return `page.locator('${badSelector.split('.nth(')[0]}').filter({ hasText: 'specific text' }) // Avoid brittle nth(), use filter()`;
  }

  // If using complex CSS → suggest ARIA role
  if (badSelector.includes('>') || badSelector.includes('+')) {
    return `page.getByRole('button', { name: 'Submit' }) // Prefer ARIA roles over complex CSS`;
  }

  return `page.getByTestId('...') // Add data-testid attribute to element`;
}

```

* *Healing Implementation**:

```typescript
// tests/healing/selector-healing.spec.ts
import { test, expect } from '@playwright/test';
import { isSelectorFailure, extractSelector, suggestBetterSelector } from '../../src/testing/healing/selector-healing';

test('heal stale selector failures automatically', async ({ page }) => {
  await page.goto('/dashboard');

  try {
    // Original test with brittle CSS selector
    await page.locator('.btn-primary').click();
  } catch (error: any) {
    if (isSelectorFailure(error)) {
      const badSelector = extractSelector(error.message);
      const suggestion = badSelector ? suggestBetterSelector(badSelector) : null;

      console.log('HEALING SUGGESTION:', suggestion);

      // Apply healed selector
      await page.getByTestId('submit-button').click(); // Fixed!
    } else {
      throw error; // Not a selector issue, rethrow
    }
  }

  await expect(page.getByText('Success')).toBeVisible();
});

```

**Key Pontos**:

- Diagnosis: A mensagem de erro contém "localizador resolvido para 0 elementos" ou "elemento não encontrado"
- Fix: Substituir o selector quebradiço (classe CSS, ID, nth) por uma alternativa robusta (teste de dados, função ARIA)
- Prevention: Siga a hierarquia do seletor (dados-teste > ARIA > texto > CSS)
- Automation: Correspondência do padrão na mensagem de erro + traço da pilha

---

### Example 2: Common Failure Pattern - Race Conditions (Timing Errors)

**Context**: Test fails with "timeout waiting for element" or "element not visible" errors

**Diagnostic Signature**:

```typescript
// src/testing/healing/timing-healing.ts

export type TimingFailure = {
  errorMessage: string;
  testFile: string;
  lineNumber: number;
  actionType: 'click' | 'fill' | 'waitFor' | 'expect';
};

/**
 * Detect race condition failures
 */
export function isTimingFailure(error: Error): boolean {
  const patterns = [
    /timeout.*waiting for/i,
    /element is not visible/i,
    /element is not attached to the dom/i,
    /waiting for element to be visible.*exceeded/i,
    /timed out retrying/i,
    /waitForLoadState.*timeout/i,
  ];

  return patterns.some((pattern) => pattern.test(error.message));
}

/**
 * Detect hard wait anti-pattern
 */
export function hasHardWait(testCode: string): boolean {
  const hardWaitPatterns = [/page\.waitForTimeout\(/, /cy\.wait\(\d+\)/, /await.*sleep\(/, /setTimeout\(/];

  return hardWaitPatterns.some((pattern) => pattern.test(testCode));
}

/**
 * Suggest deterministic wait replacement
 */
export function suggestDeterministicWait(testCode: string): string {
  if (testCode.includes('page.waitForTimeout')) {
    return `
// ❌ Bad: Hard wait (flaky)
// await page.waitForTimeout(3000)

// ✅ Good: Wait for network response
await page.waitForResponse(resp => resp.url().includes('/api/data') && resp.status() === 200)

// OR wait for element state
await page.getByTestId('loading-spinner').waitFor({ state: 'detached' })
    `.trim();
  }

  if (testCode.includes('cy.wait(') && /cy\.wait\(\d+\)/.test(testCode)) {
    return `
// ❌ Bad: Hard wait (flaky)
// cy.wait(3000)

// ✅ Good: Wait for aliased network request
cy.intercept('GET', '/api/data').as('getData')
cy.visit('/page')
cy.wait('@getData')
    `.trim();
  }

  return `
// Add network-first interception BEFORE navigation:
await page.route('**/api/**', route => route.continue())
const responsePromise = page.waitForResponse('**/api/data')
await page.goto('/page')
await responsePromise
  `.trim();
}

```

**Healing Implementation**:

```typescript
// tests/healing/timing-healing.spec.ts
import { test, expect } from '@playwright/test';
import { isTimingFailure, hasHardWait, suggestDeterministicWait } from '../../src/testing/healing/timing-healing';

test('heal race condition with network-first pattern', async ({ page, context }) => {
  // Setup interception BEFORE navigation (prevent race)
  await context.route('**/api/products', (route) => {
    route.fulfill({
      status: 200,
      body: JSON.stringify({ products: [{ id: 1, name: 'Product A' }] }),
    });
  });

  const responsePromise = page.waitForResponse('**/api/products');

  await page.goto('/products');
  await responsePromise; // Deterministic wait

  // Element now reliably visible (no race condition)
  await expect(page.getByText('Product A')).toBeVisible();
});

test('heal hard wait with event-based wait', async ({ page }) => {
  await page.goto('/dashboard');

  // ❌ Original (flaky): await page.waitForTimeout(3000)

  // ✅ Healed: Wait for spinner to disappear
  await page.getByTestId('loading-spinner').waitFor({ state: 'detached' });

  // Element now reliably visible
  await expect(page.getByText('Dashboard loaded')).toBeVisible();
});

```

**Key Points**:

- Diagnosis: Error contains "timeout" or "not visible", often after navigation
- Fix: Replace hard waits with network-first pattern or element state waits
- Prevention: ALWAYS intercept before navigate, use waitForResponse()
- Automation: Detect `page.waitForTimeout()` or `cy.wait(number)` in test code

---

### Exemplo 3: Padrão de falha comum - Asserções dinâmicas de dados (IDs não-determinativos)

**Context**: O teste falha com "Usuário esperado 123", mas recebeu "Usuário 456" ou erros de timestamp

* *Diagnostic Assinatura**:

```typescript
// src/testing/healing/data-healing.ts

export type DataFailure = {
  errorMessage: string;
  expectedValue: string;
  actualValue: string;
  testFile: string;
  lineNumber: number;
};

/**
 * Detect dynamic data assertion failures
 */
export function isDynamicDataFailure(error: Error): boolean {
  const patterns = [
    /expected.*\d+.*received.*\d+/i, // ID mismatches
    /expected.*\d{4}-\d{2}-\d{2}.*received/i, // Date mismatches
    /expected.*user.*\d+/i, // Dynamic user IDs
    /expected.*order.*\d+/i, // Dynamic order IDs
    /expected.*to.*contain.*\d+/i, // Numeric assertions
  ];

  return patterns.some((pattern) => pattern.test(error.message));
}

/**
 * Suggest flexible assertion pattern
 */
export function suggestFlexibleAssertion(errorMessage: string): string {
  if (/expected.*user.*\d+/i.test(errorMessage)) {
    return `
// ❌ Bad: Hardcoded ID
// await expect(page.getByText('User 123')).toBeVisible()

// ✅ Good: Regex pattern for any user ID
await expect(page.getByText(/User \\d+/)).toBeVisible()

// OR use partial match
await expect(page.locator('[data-testid="user-name"]')).toContainText('User')
    `.trim();
  }

  if (/expected.*\d{4}-\d{2}-\d{2}/i.test(errorMessage)) {
    return `
// ❌ Bad: Hardcoded date
// await expect(page.getByText('2024-01-15')).toBeVisible()

// ✅ Good: Dynamic date validation
const today = new Date().toISOString().split('T')[0]
await expect(page.getByTestId('created-date')).toHaveText(today)

// OR use date format regex
await expect(page.getByTestId('created-date')).toHaveText(/\\d{4}-\\d{2}-\\d{2}/)
    `.trim();
  }

  if (/expected.*order.*\d+/i.test(errorMessage)) {
    return `
// ❌ Bad: Hardcoded order ID
// const orderId = '12345'

// ✅ Good: Capture dynamic order ID
const orderText = await page.getByTestId('order-id').textContent()
const orderId = orderText?.match(/Order #(\\d+)/)?.[1]
expect(orderId).toBeTruthy()

// Use captured ID in later assertions
await expect(page.getByText(\`Order #\${orderId} confirmed\`)).toBeVisible()
    `.trim();
  }

  return `Use regex patterns, partial matching, or capture dynamic values instead of hardcoding`;
}

```

* *Healing Implementation**:

```typescript
// tests/healing/data-healing.spec.ts
import { test, expect } from '@playwright/test';

test('heal dynamic ID assertion with regex', async ({ page }) => {
  await page.goto('/users');

  // ❌ Original (fails with random IDs): await expect(page.getByText('User 123')).toBeVisible()

  // ✅ Healed: Regex pattern matches any user ID
  await expect(page.getByText(/User \d+/)).toBeVisible();
});

test('heal timestamp assertion with dynamic generation', async ({ page }) => {
  await page.goto('/dashboard');

  // ❌ Original (fails daily): await expect(page.getByText('2024-01-15')).toBeVisible()

  // ✅ Healed: Generate expected date dynamically
  const today = new Date().toISOString().split('T')[0];
  await expect(page.getByTestId('last-updated')).toContainText(today);
});

test('heal order ID assertion with capture', async ({ page, request }) => {
  // Create order via API (dynamic ID)
  const response = await request.post('/api/orders', {
    data: { productId: '123', quantity: 1 },
  });
  const { orderId } = await response.json();

  // ✅ Healed: Use captured dynamic ID
  await page.goto(`/orders/${orderId}`);
  await expect(page.getByText(`Order #${orderId}`)).toBeVisible();
});

```

**Key Pontos**:

- Diagnosis: A mensagem de erro mostra o valor esperado vs o valor real desfasamento com IDs/timestamps
- Fix: Usar padrões regex (`/User \d+/`), correspondência parcial, ou capturar valores dinâmicos
- Prevention: Nunca IDs de código rígido, datas ou dados aleatórios em asserções
- Automation: Processar a mensagem de erro para valores esperados/actuales, sugerir padrões de regex

---

### Example 4: Common Failure Pattern - Network Errors (Missing Route Interception)

**Context**: Test fails with "API call failed" or "500 error" during test execution

**Diagnostic Signature**:

```typescript
// src/testing/healing/network-healing.ts

export type NetworkFailure = {
  errorMessage: string;
  url: string;
  statusCode: number;
  method: string;
};

/**
 * Detect network failure
 */
export function isNetworkFailure(error: Error): boolean {
  const patterns = [
    /api.*call.*failed/i,
    /request.*failed/i,
    /network.*error/i,
    /500.*internal server error/i,
    /503.*service unavailable/i,
    /fetch.*failed/i,
  ];

  return patterns.some((pattern) => pattern.test(error.message));
}

/**
 * Suggest route interception
 */
export function suggestRouteInterception(url: string, method: string): string {
  return `
// ❌ Bad: Real API call (unreliable, slow, external dependency)

// ✅ Good: Mock API response with route interception
await page.route('${url}', route => {
  route.fulfill({
    status: 200,
    contentType: 'application/json',
    body: JSON.stringify({
      // Mock response data
      id: 1,
      name: 'Test User',
      email: 'test@example.com'
    })
  })
})

// Then perform action
await page.goto('/page')
  `.trim();
}

```

**Healing Implementation**:

```typescript
// tests/healing/network-healing.spec.ts
import { test, expect } from '@playwright/test';

test('heal network failure with route mocking', async ({ page, context }) => {
  // ✅ Healed: Mock API to prevent real network calls
  await context.route('**/api/products', (route) => {
    route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({
        products: [
          { id: 1, name: 'Product A', price: 29.99 },
          { id: 2, name: 'Product B', price: 49.99 },
        ],
      }),
    });
  });

  await page.goto('/products');

  // Test now reliable (no external API dependency)
  await expect(page.getByText('Product A')).toBeVisible();
  await expect(page.getByText('$29.99')).toBeVisible();
});

test('heal 500 error with error state mocking', async ({ page, context }) => {
  // Mock API failure scenario
  await context.route('**/api/products', (route) => {
    route.fulfill({ status: 500, body: JSON.stringify({ error: 'Internal Server Error' }) });
  });

  await page.goto('/products');

  // Verify error handling (not crash)
  await expect(page.getByText('Unable to load products')).toBeVisible();
  await expect(page.getByRole('button', { name: 'Retry' })).toBeVisible();
});

```

**Key Points**:

- Diagnosis: Error message contains "API call failed", "500 error", or network-related failures
- Fix: Add `page.route()` or `cy.intercept()` to mock API responses
- Prevention: Mock ALL external dependencies (APIs, third-party services)
- Automation: Extract URL from error message, generate route interception code

---

### Exemplo 5: Padrão comum de falha - esperas difíceis (horário não confiável)

**Context**: O ensaio falha de forma intermitente com "tempo de espera ultrapassado" ou passa/falha aleatoriamente

**Diagnostic Assinatura**:

```typescript
// src/testing/healing/hard-wait-healing.ts

/**
 * Detect hard wait anti-pattern in test code
 */
export function detectHardWaits(testCode: string): Array<{ line: number; code: string }> {
  const lines = testCode.split('\n');
  const violations: Array<{ line: number; code: string }> = [];

  lines.forEach((line, index) => {
    if (line.includes('page.waitForTimeout(') || /cy\.wait\(\d+\)/.test(line) || line.includes('sleep(') || line.includes('setTimeout(')) {
      violations.push({ line: index + 1, code: line.trim() });
    }
  });

  return violations;
}

/**
 * Suggest event-based wait replacement
 */
export function suggestEventBasedWait(hardWaitLine: string): string {
  if (hardWaitLine.includes('page.waitForTimeout')) {
    return `
// ❌ Bad: Hard wait (flaky)
${hardWaitLine}

// ✅ Good: Wait for network response
await page.waitForResponse(resp => resp.url().includes('/api/') && resp.ok())

// OR wait for element state change
await page.getByTestId('loading-spinner').waitFor({ state: 'detached' })
await page.getByTestId('content').waitFor({ state: 'visible' })
    `.trim();
  }

  if (/cy\.wait\(\d+\)/.test(hardWaitLine)) {
    return `
// ❌ Bad: Hard wait (flaky)
${hardWaitLine}

// ✅ Good: Wait for aliased request
cy.intercept('GET', '/api/data').as('getData')
cy.visit('/page')
cy.wait('@getData') // Deterministic
    `.trim();
  }

  return 'Replace hard waits with event-based waits (waitForResponse, waitFor state changes)';
}

```

* *Healing Implementation**:

```typescript
// tests/healing/hard-wait-healing.spec.ts
import { test, expect } from '@playwright/test';

test('heal hard wait with deterministic wait', async ({ page }) => {
  await page.goto('/dashboard');

  // ❌ Original (flaky): await page.waitForTimeout(3000)

  // ✅ Healed: Wait for loading spinner to disappear
  await page.getByTestId('loading-spinner').waitFor({ state: 'detached' });

  // OR wait for specific network response
  await page.waitForResponse((resp) => resp.url().includes('/api/dashboard') && resp.ok());

  await expect(page.getByText('Dashboard ready')).toBeVisible();
});

test('heal implicit wait with explicit network wait', async ({ page }) => {
  const responsePromise = page.waitForResponse('**/api/products');

  await page.goto('/products');

  // ❌ Original (race condition): await page.getByText('Product A').click()

  // ✅ Healed: Wait for network first
  await responsePromise;
  await page.getByText('Product A').click();

  await expect(page).toHaveURL(/\/products\/\d+/);
});

```

**Key Pontos**:

- Diagnosis: O código de ensaio contém `page.waitForTimeout()` ou `cy.wait(number)`
- Fix: Substituir por `waitForResponse()`, `waitFor({ state })`, ou interceptações aliasadas
- Prevention: NUNCA use esperas difíceis, sempre use esperas baseadas em eventos/resposta
- Automation: Varrer o código de teste para padrões de espera dura, sugerir substituições determinísticas

---

## Catálogo de Padrão de Cura

| Failure Type   | Diagnostic Signature                          | Healing Strategy                      | Prevention Pattern                        |
| -------------- | --------------------------------------------- | ------------------------------------- | ----------------------------------------- |
| Stale Selector | "locator resolved to 0 elements"              | Replace with data-testid or ARIA role | Selector hierarchy (testid > ARIA > text) |
| Race Condition | "timeout waiting for element"                 | Add network-first interception        | Intercept before navigate                 |
| Dynamic Data   | "Expected 'User 123' but got 'User 456'"      | Use regex or capture dynamic values   | Never hardcode IDs/timestamps             |
| Network Error  | "API call failed", "500 error"                | Add route mocking                     | Mock all external dependencies            |
| Hard Wait      | Test contains `waitForTimeout()` or `wait(n)` | Replace with event-based waits        | Always use deterministic waits            |

## Fluxo de trabalho de cura

1. **Run teste** → Falha de captura
2. **Identify padrão** → Corresponder erro contra assinaturas diagnósticas
3. **Apply correção** → Use a estratégia de cura baseada em padrões
4. **Re-run teste** → Validar correção (máximo 3 iterações)
5. **Mark infixável** → Use `test.fixme()` se a cicatrização falhar após 3 tentativas

## Lista de Verificação de Cura

Antes de ativar a cura automática em fluxos de trabalho:

- [ ] **Failure catálogo documentado**: Padrões comuns identificados (seletores, timing, dados, rede, espera)
- [ ] **Diagnostic assinaturas definidas**: Erro padrões de mensagem para cada tipo de falha
- [ ] **Healing estratégias documentadas**: Corrigir padrões para cada tipo de falha
- [ ] **Prevention padrões documentados**: Melhores práticas para evitar a recorrência
- [ ] **Healing iteração limite definido**: Max 3 tentativas antes de marcar test.fixme()
- [ ] **MCP integração opcional**: Degradação graciosa sem dramaturgo MCP
- [ ] * *Pattern-based back**: Usar padrões de base de conhecimento quando MCP não estiver disponível
- [ ] **Healing relatório gerado**: Documentar o que foi curado e como

## Pontos de Integração

- **Used em fluxos de trabalho**: `*automate` (auto-cura após a geração do teste), `*atdd` (cura opcional para testes de aceitação)
- Fragmentos *Related**: `selector-resilience.md` (depuração do selector), `timing-debugging.md` (reparação das condições de corrida), `network-first.md` (padrões de intercepção), `data-factories.md` (manipulação dinâmica dos dados)
- **Tools**: Processamento de mensagens de erro, análise AST para padrões de código, MCP Playwright (opcional), correspondência de padrões

_Source: Playwright testes-cura padrões, análise de falha de produção teste, anti-padrãos comuns de teste-recursos-para-ai
