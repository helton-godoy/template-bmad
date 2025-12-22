# Execução de teste seletiva e direcionada

## Princípio

Faça apenas os testes de que precisa, quando precisar. Use tags/grep para cortar suites por prioridade de risco (não por estrutura de diretórios), filtro por padrões de especificações ou git diff para focar em áreas impactadas, e combinar metadados de prioridade (P0-P3) com detecção de alterações para otimizar a execução pré-commit vs. CI. Documentar a estratégia de seleção claramente para que as equipes entendam quando a regressão completa é obrigatória.

## Racional

Executar todo o conjunto de testes em cada commit perde tempo e recursos. A seleção de teste inteligente fornece feedback rápido (testes de fumaça em minutos, regressão completa em horas) mantendo a confiança. A filosofia "32+ maneiras de testes seletivos" equilibra a velocidade com a cobertura: laços rápidos para desenvolvedores, validação abrangente antes da implantação. A seleção mal documentada leva a confusão sobre quando os testes são executados e por quê.

## Exemplos de padrões

### Exemplo 1: Execução baseada em etiquetas com níveis prioritários

**Contexto**: Organizar testes por prioridade de risco e fase de execução utilizando padrões grep/tag.

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

**Equipamento cipreste**:

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

**Usagem**:

«```bash

# dramaturgo
teste de execução npm: fumo # Execute todos os testes @ smoke
teste de execução npm: p0 # Execute todos os testes P0
npm execute test -- --grep "@ smoke.*@ p0" # Executar testes com ambas as etiquetas

# Cipreste (com @cypress/grep plugi