# Verificação de Erros e Resiliência

## Princípio

Tratar as falhas esperadas explicitamente: interceptar erros de rede, asseverar fallbacks de UI (mensagens de erro visíveis, repetições acionadas), e usar o manuseio de exceção escopo para ignorar erros conhecidos durante a captura de regressões. Teste a lógica de retry/backoff forçando falhas sequenciais (500 → timeout → sucesso) e valide o registro de telemetria. Registre erros capturados com o contexto (pedir carga útil, usuário/sessão) mas redigir segredos para manter artefatos seguros para compartilhamento.

## Racional

Os testes falham por duas razões: erros genuínos ou mau manuseio de erros no teste em si. Sem padrões explícitos de manipulação de erros, testes tornam-se barulhentos (excepções não captadas causam falhas false) ou silenciosos (swallowing todos os erros esconde erros reais). Manuseamento de exceções escopos (Cypress.on('não pego: exceção'), page.on('pageerror')) permite que os testes ignorem erros documentados e esperados enquanto surgem inesperados. Testes de resiliência (lógica de repetição, degradação graciosa) garante aplicações lidar com falhas graciosamente na produção.

## Exemplos de padrões

### Exemplo 1: Tratamento de Excepções Alcançadas (apenas erros esperados)

**Contexto**: Lidar com erros conhecidos (falhas de rede, esperados 500s) sem mascarar bugs inesperados.

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

**Equipamento cipreste**:

«``'javascript
// Cypress/e2e/error-handling.cy.ts
Description('API Error Handling', () => {
  it('should display error message when API returns 500', () => {
    // Scoped to this test only
    cy.on('uncaught:exception', (err) => {
      // Only swallow documented NetworkError
      if (err.message.includes('NetworkError')) {
        return false; // Prevent test failure
      }
// Todos os outros erros falham no teste
true de retorno;
});

// Organizar: erro de Mock 500
cy.intercept('GET', '**/api/usuários', {
      statusCode: 500,
      body: {
        error: 'Internal server error',
        code: 'INTERNAL_ERROR',
      },
}). como('getUsers');

// Act
cy.visit('/dashboard');
cy.wait('@ getUsers');

// Asserta: UI de erro
cy.get('[data-cy="error-mensage"]'). should('be.visible');
cy.get('[data-cy="error-message"]'). should('conttain', 'error loading');
cy.get('[data-cy="botão de ensaio"]'). should('be.visible');
});

não deve engolir erros inesperados, () = > {
// Nenhum manipulador de exceção - teste deve falhar em erros inesperados

cy.visit('/dashboard');

// Ativar erro inesperado
cy.window().then((win) => {
// Isto deve falhar no teste
ganhar