# Correção da depuração e da condição da corrida

## Princípio

As condições de corrida surgem quando os testes fazem suposições sobre o tempo assíncrono (rede, animações, atualizações de estado). **Deterministic waiting** elimina flakiness, esperando explicitamente eventos observáveis (respostas de rede, mudanças de estado de elemento) em vez de timeouts arbitrários.

## Racional

**The Problem**: Os testes passam localmente, mas falham em IC (tempo diferente), ou passam/ falham aleatoriamente (condições de corrida). Difícil espera (`waitForTimeout`, `sleep`) problemas de tempo da máscara sem resolvê-los.

**The Solution**: Substitua todas as esperas difíceis por esperas baseadas em eventos (`waitForResponse`, `waitFor({ state })`). Implementar o primeiro padrão de rede (interceptar antes de navegar). Usar verificações explícitas de estado (carregando spinner desacoplado, dados carregados). Isso torna os testes determinísticos independentemente da velocidade da rede ou da carga do sistema.

**Por que isso importa**:

- Elimina testes flácidos (0 tolerância para falhas baseadas no tempo)
- Funciona consistentemente em ambientes (local, CI, tipo produção)
- Execução mais rápida do teste (sem esperas desnecessárias)
- Mais clara intenção de teste (explique sobre o que estamos esperando)

## Exemplos de padrões

### Exemplo 1: Identificação da condição da corrida (primeiro padrão da rede)

**Contexto**: Prevenir as condições raciais interceptando os pedidos de rede antes da navegação

**Implementation**:

```typescript
// tests/timing/race-condition-prevention.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Race Condition Prevention Patterns', () => {
  test('❌ Anti-Pattern: Navigate then intercept (race condition)', async ({ page, context }) => {
    // BAD: Navigation starts before interception ready
    await page.goto('/products'); // ⚠️ Race! API might load before route is set

    await context.route('**/api/products', (route) => {
      route.fulfill({ status: 200, body: JSON.stringify({ products: [] }) });
    });

    // Test may see real API response or mock (non-deterministic)
  });

  test('✅ Pattern: Intercept BEFORE navigate (deterministic)', async ({ page, context }) => {
    // GOOD: Interception ready before navigation
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

    const responsePromise = page.waitForResponse('**/api/products');

    await page.goto('/products'); // Navigation happens AFTER route is ready
    await responsePromise; // Explicit wait for network

    // Test sees mock response reliably (deterministic)
    await expect(page.getByText('Product A')).toBeVisible();
  });

  test('✅ Pattern: Wait for element state change (loading → loaded)', async ({ page }) => {
    await page.goto('/dashboard');

    // Wait for loading indicator to appear (confirms load started)
    await page.getByTestId('loading-spinner').waitFor({ state: 'visible' });

    // Wait for loading indicator to disappear (confirms load complete)
    await page.getByTestId('loading-spinner').waitFor({ state: 'detached' });

    // Content now reliably visible
    await expect(page.getByTestId('dashboard-data')).toBeVisible();
  });

  test('✅ Pattern: Explicit visibility check (not just presence)', async ({ page }) => {
    await page.goto('/modal-demo');

    await page.getByRole('button', { name: 'Open Modal' }).click();

    // ❌ Bad: Element exists but may not be visible yet
    // await expect(page.getByTestId('modal')).toBeAttached()

    // ✅ Good: Wait for visibility (accounts for animations)
    await expect(page.getByTestId('modal')).toBeVisible();
    await expect(page.getByRole('heading', { name: 'Modal Title' })).toBeVisible();
  });

  test('❌ Anti-Pattern: waitForLoadState("networkidle") in SPAs', async ({ page }) => {
    // ⚠️ Deprecated for SPAs (WebSocket connections never idle)
    // await page.goto('/dashboard')
    // await page.waitForLoadState('networkidle') // May timeout in SPAs

    // ✅ Better: Wait for specific API response
    const responsePromise = page.waitForResponse('**/api/dashboard');
    await page.goto('/dashboard');
    await responsePromise;

    await expect(page.getByText('Dashboard loaded')).toBeVisible();
  });
});

```

**Pontos-chave**

- Rede-primeiro: SEMPRE interceptar antes de navegar (preveni condições de corrida)
- Alterações de estado: Aguarde para carregar o spinner descolado (completar carga explícita)
- Visibilidade vs presença: `toBeVisible()` contas para animações, `toBeAttached()` não
- Evite networkidle: Não confiável em SPA (WebSocket, ligações de votação)
- Explícito espera: Documento exatamente o que estamos esperando

---

### Exemplo 2: Padrões de espera determinísticos (baseados em eventos, não baseados no tempo)

**Contexto**: Substitua todas as esperas difíceis por esperas de eventos observáveis

**Implementation**:

«``typescript
// testes/timing/deterministic-waits.spec.ts
import {teste, e