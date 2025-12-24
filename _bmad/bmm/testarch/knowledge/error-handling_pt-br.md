# Tratamento de Erro e Verificações de Resiliência

## Princípio

Trate falhas esperadas explicitamente: intercepte erros de rede, asserções de fallbacks de UI (mensagens de erro visíveis, retentativas disparadas) e use tratamento de exceção com escopo para ignorar erros conhecidos enquanto captura regressões. Teste a lógica de retentativa/backoff forçando falhas sequenciais (500 → timeout → sucesso) e valide o log de telemetria. Logue erros capturados com contexto (payload da requisição, usuário/sessão) mas oculte segredos para manter artefatos seguros para compartilhamento.

## Motivação

Testes falham por duas razões: bugs genuínos ou tratamento de erro ruim no próprio teste. Sem padrões de tratamento de erro explícitos, testes tornam-se ruidosos (exceções não capturadas causam falhas falsas) ou silenciosos (engolir todos os erros esconde bugs reais). Tratamento de exceção com escopo (Cypress.on('uncaught:exception'), page.on('pageerror')) permite que testes ignorem erros documentados e esperados enquanto expõem os inesperados. Testes de resiliência (lógica de retentativa, degradação graciosa) garantem que aplicações tratem falhas graciosamente em produção.

## Exemplos de Padrões

### Exemplo 1: Tratamento de Exceção com Escopo (Apenas Erros Esperados)

**Contexto**: Trate erros conhecidos (Falhas de rede, 500s esperados) sem mascarar bugs inesperados.

**Implementação**:

```typescript
// tests/e2e/error-handling.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Padrão de Tratamento de Erro com Escopo
 * - Apenas ignore erros específicos e documentados
 * - Relance tudo o mais para capturar regressões
 * - Valide UI de erro e experiência do usuário
 */

test.describe('Tratamento de Erro de API', () => {
  test('deve exibir mensagem de erro quando API retorna 500', async ({ page }) => {
    // Escopo de tratamento de erro APENAS para este teste
    const consoleErrors: string[] = [];
    page.on('pageerror', (error) => {
      // Apenas engula NetworkError documentado
      if (error.message.includes('NetworkError: Failed to fetch')) {
        consoleErrors.push(error.message);
        return; // Engula este erro específico
      }
      // Relance todos os outros erros (capture regressões!)
      throw error;
    });

    // Arrange: Mock resposta de erro 500
    await page.route('**/api/users', (route) =>
      route.fulfill({
        status: 500,
        contentType: 'application/json',
        body: JSON.stringify({
          error: 'Erro interno do servidor',
          code: 'INTERNAL_ERROR',
        }),
      }),
    );

    // Act: Navegar para página que busca usuários
    await page.goto('/dashboard');

    // Assert: UI de erro exibida
    await expect(page.getByTestId('error-message')).toBeVisible();
    await expect(page.getByTestId('error-message')).toContainText(/erro.*carregando|falha.*carregar/i);

    // Assert: Botão de tentar novamente visível
    await expect(page.getByTestId('retry-button')).toBeVisible();

    // Assert: NetworkError foi lançado e capturado
    expect(consoleErrors).toContainEqual(expect.stringContaining('NetworkError'));
  });

  test('NÃO deve engolir erros inesperados', async ({ page }) => {
    let unexpectedError: Error | null = null;

    page.on('pageerror', (error) => {
      // Capture mas não engula - teste deve falhar
      unexpectedError = error;
      throw error;
    });

    // Arrange: App tem erro JavaScript (bug)
    await page.addInitScript(() => {
      // Simular bug no código do app
      (window as any).buggyFunction = () => {
        throw new Error('BUG INESPERADO: undefined não é uma função');
      };
    });

    await page.goto('/dashboard');

    // Disparar função com bug
    await page.evaluate(() => (window as any).buggyFunction());

    // Assert: Teste falha porque erro inesperado NÃO foi engolido
    expect(unexpectedError).not.toBeNull();
    expect(unexpectedError?.message).toContain('BUG INESPERADO');
  });
});
```

**Equivalente Cypress**:

```javascript
// cypress/e2e/error-handling.cy.ts
describe('Tratamento de Erro de API', () => {
  it('deve exibir mensagem de erro quando API retorna 500', () => {
    // Escopo apenas para este teste
    cy.on('uncaught:exception', (err) => {
      // Apenas engula NetworkError documentado
      if (err.message.includes('NetworkError')) {
        return false; // Previne falha do teste
      }
      // Todos os outros erros falham o teste
      return true;
    });

    // Arrange: Mock erro 500
    cy.intercept('GET', '**/api/users', {
      statusCode: 500,
      body: {
        error: 'Erro interno do servidor',
        code: 'INTERNAL_ERROR',
      },
    }).as('getUsers');

    // Act
    cy.visit('/dashboard');
    cy.wait('@getUsers');

    // Assert: UI de Erro
    cy.get('[data-cy="error-message"]').should('be.visible');
    cy.get('[data-cy="error-message"]').should('contain', 'erro carregando');
    cy.get('[data-cy="retry-button"]').should('be.visible');
  });

  it('NÃO deve engolir erros inesperados', () => {
    // Sem manipulador de exceção - teste deve falhar em erros inesperados

    cy.visit('/dashboard');

    // Disparar erro inesperado
    cy.window().then((win) => {
      // Isso deve falhar o teste
      win.eval('throw new Error("BUG INESPERADO")');
    });

    // Teste falha (como esperado) - valida que detecção de erro funciona
  });
});
```

**Pontos Chave**:

- **Tratamento com escopo**: page.on() / cy.on() escopado para testes específicos
- **Allow-list explícita**: Apenas ignore erros documentados
- **Relançar inesperados**: Capture regressões falhando em erros desconhecidos
- **Validação de UI de erro**: Assegure que usuário vê mensagem de erro
- **Log**: Capture erros para debugging, não engula silenciosamente

---

### Exemplo 2: Padrão de Validação de Retentativa (Resiliência de Rede)

**Contexto**: Teste se lógica de retentativa/backoff funciona corretamente para falhas transitórias.

**Implementação**:

```typescript
// tests/e2e/retry-resilience.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Padrão de Validação de Retentativa
 * - Forçar falhas sequenciais (500 → 500 → 200)
 * - Validar tentativas de retentativa e tempo de backoff
 * - Assegurar que telemetria captura eventos de retentativa
 */

test.describe('Lógica de Retentativa de Rede', () => {
  test('deve tentar novamente em erro 500 e suceder', async ({ page }) => {
    let attemptCount = 0;
    const attemptTimestamps: number[] = [];

    // Mock API: Falha duas vezes, sucede na terceira tentativa
    await page.route('**/api/products', (route) => {
      attemptCount++;
      attemptTimestamps.push(Date.now());

      if (attemptCount <= 2) {
        // Primeiras 2 tentativas: erro 500
        route.fulfill({
          status: 500,
          body: JSON.stringify({ error: 'Erro de servidor' }),
        });
      } else {
        // 3ª tentativa: Sucesso
        route.fulfill({
          status: 200,
          contentType: 'application/json',
          body: JSON.stringify({ products: [{ id: 1, name: 'Produto 1' }] }),
        });
      }
    });

    // Act: Navegar (deve tentar novamente automaticamente)
    await page.goto('/products');

    // Assert: Dados eventualmente carregam após retentativas
    await expect(page.getByTestId('product-list')).toBeVisible();
    await expect(page.getByTestId('product-item')).toHaveCount(1);

    // Assert: Exatamente 3 tentativas feitas
    expect(attemptCount).toBe(3);

    // Assert: Tempo de backoff exponencial (1s → 2s entre tentativas)
    if (attemptTimestamps.length === 3) {
      const delay1 = attemptTimestamps[1] - attemptTimestamps[0];
      const delay2 = attemptTimestamps[2] - attemptTimestamps[1];

      expect(delay1).toBeGreaterThanOrEqual(900); // ~1 segundo
      expect(delay1).toBeLessThan(1200);
      expect(delay2).toBeGreaterThanOrEqual(1900); // ~2 segundos
      expect(delay2).toBeLessThan(2200);
    }

    // Assert: Telemetria logou eventos de retentativa
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

  test('deve desistir após max retentativas e mostrar erro', async ({ page }) => {
    let attemptCount = 0;

    // Mock API: Sempre falha (teste de limite de retentativa)
    await page.route('**/api/products', (route) => {
      attemptCount++;
      route.fulfill({
        status: 500,
        body: JSON.stringify({ error: 'Erro de servidor persistente' }),
      });
    });

    // Act
    await page.goto('/products');

    // Assert: Max retentativas atingido (3 tentativas típico)
    expect(attemptCount).toBe(3);

    // Assert: UI de erro exibida após exaurir retentativas
    await expect(page.getByTestId('error-message')).toBeVisible();
    await expect(page.getByTestId('error-message')).toContainText(/incapaz.*carregar|falha.*após.*tentativas/i);

    // Assert: Dados não exibidos
    await expect(page.getByTestId('product-list')).not.toBeVisible();
  });

  test('NÃO deve tentar novamente em 404 (erro não retentável)', async ({ page }) => {
    let attemptCount = 0;

    // Mock API: erro 404 (NÃO deve tentar novamente)
    await page.route('**/api/products/999', (route) => {
      attemptCount++;
      route.fulfill({
        status: 404,
        body: JSON.stringify({ error: 'Produto não encontrado' }),
      });
    });

    await page.goto('/products/999');

    // Assert: Apenas 1 tentativa (sem retentativas em 404)
    expect(attemptCount).toBe(1);

    // Assert: Erro 404 exibido imediatamente
    await expect(page.getByTestId('not-found-message')).toBeVisible();
  });
});
```

**Cypress com interceptação de retentativa**:

```javascript
// cypress/e2e/retry-resilience.cy.ts
describe('Lógica de Retentativa de Rede', () => {
  it('deve tentar novamente em 500 e suceder na 3ª tentativa', () => {
    let attemptCount = 0;

    cy.intercept('GET', '**/api/products', (req) => {
      attemptCount++;

      if (attemptCount <= 2) {
        req.reply({ statusCode: 500, body: { error: 'Erro de servidor' } });
      } else {
        req.reply({ statusCode: 200, body: { products: [{ id: 1, name: 'Produto 1' }] } });
      }
    }).as('getProducts');

    cy.visit('/products');

    // Aguardar requisição bem-sucedida final
    cy.wait('@getProducts').its('response.statusCode').should('eq', 200);

    // Assert: Dados carregados
    cy.get('[data-cy="product-list"]').should('be.visible');
    cy.get('[data-cy="product-item"]').should('have.length', 1);

    // Validar contagem de retentativa
    cy.wrap(attemptCount).should('eq', 3);
  });
});
```

**Pontos Chave**:

- **Falhas sequenciais**: Teste lógica de retentativa com 500 → 500 → 200
- **Tempo de backoff**: Valide atrasos de backoff exponencial
- **Limites de retentativa**: Max tentativas impostas (tipicamente 3)
- **Erros não retentáveis**: 404s não disparam retentativas
- **Telemetria**: Log tentativas de retentativa para monitoramento

---

### Exemplo 3: Log de Telemetria com Contexto (Integração Sentry)

**Contexto**: Capture erros com contexto completo para debugging de produção sem expor segredos.

**Implementação**:

```typescript
// tests/e2e/telemetry-logging.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Padrão de Log de Telemetria
 * - Log erros com contexto de requisição
 * - Ocultar dados sensíveis (tokens, senhas, PII)
 * - Integrar com monitoramento (Sentry, Datadog)
 * - Validar log de erro sem expor segredos
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

test.describe('Telemetria de Erro', () => {
  test('deve logar erros de API com contexto', async ({ page }) => {
    const errorLogs: ErrorLog[] = [];

    // Capture erros de console
    page.on('console', (msg) => {
      if (msg.type() === 'error') {
        try {
          const log = JSON.parse(msg.text());
          errorLogs.push(log);
        } catch {
          // Não é um log estruturado, ignorar
        }
      }
    });

    // Mock API falhando
    await page.route('**/api/orders', (route) =>
      route.fulfill({
        status: 500,
        body: JSON.stringify({ error: 'Processador de pagamento indisponível' }),
      }),
    );

    // Act: Disparar erro
    await page.goto('/checkout');
    await page.getByTestId('place-order').click();

    // Aguardar UI de erro
    await expect(page.getByTestId('error-message')).toBeVisible();

    // Assert: Erro logado com contexto
    expect(errorLogs).toContainEqual(
      expect.objectContaining({
        level: 'error',
        message: expect.stringContaining('Requisição API falhou'),
        context: expect.objectContaining({
          endpoint: '/api/orders',
          method: 'POST',
          statusCode: 500,
          userId: expect.any(String),
        }),
      }),
    );

    // Assert: Dados sensíveis NÃO logados
    const logString = JSON.stringify(errorLogs);
    expect(logString).not.toContain('password');
    expect(logString).not.toContain('token');
    expect(logString).not.toContain('creditCard');
  });

  test('deve enviar erros para Sentry com breadcrumbs', async ({ page }) => {
    const sentryEvents: any[] = [];

    // Mock SDK Sentry
    await page.addInitScript(() => {
      (window as any).Sentry = {
        captureException: (error: Error, context?: any) => {
          (window as any).__SENTRY_EVENTS__ = (window as any).__SENTRY_EVENTS__ || [];
          (window as any).__SENTRY_EVENTS__.push({
            error: error.message,
            context,
            timestamp: Date.now(),
          });
        },
        addBreadcrumb: (breadcrumb: any) => {
          (window as any).__SENTRY_BREADCRUMBS__ = (window as any).__SENTRY_BREADCRUMBS__ || [];
          (window as any).__SENTRY_BREADCRUMBS__.push(breadcrumb);
        },
      };
    });

    // Mock API falhando
    await page.route('**/api/users', (route) => route.fulfill({ status: 403, body: { error: 'Proibido' } }));

    // Act
    await page.goto('/users');

    // Assert: Sentry capturou erro
    const events = await page.evaluate(() => (window as any).__SENTRY_EVENTS__);
    expect(events).toHaveLength(1);
    expect(events[0]).toMatchObject({
      error: expect.stringContaining('403'),
      context: expect.objectContaining({
        endpoint: '/api/users',
        statusCode: 403,
      }),
    });

    // Assert: Breadcrumbs incluem ações do usuário
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

**Cypress com Sentry**:

```javascript
// cypress/e2e/telemetry-logging.cy.ts
describe('Telemetria de Erro', () => {
  it('deve logar erros de API com dados sensíveis ocultados', () => {
    const errorLogs = [];

    // Capture erros de console
    cy.on('window:before:load', (win) => {
      cy.stub(win.console, 'error').callsFake((msg) => {
        errorLogs.push(msg);
      });
    });

    // Mock API falhando
    cy.intercept('POST', '**/api/orders', {
      statusCode: 500,
      body: { error: 'Pagamento falhou' },
    });

    // Act
    cy.visit('/checkout');
    cy.get('[data-cy="place-order"]').click();

    // Assert: Erro logado
    cy.wrap(errorLogs).should('have.length.greaterThan', 0);

    // Assert: Contexto incluído
    cy.wrap(errorLogs[0]).should('include', '/api/orders');

    // Assert: Segredos ocultados
    cy.wrap(JSON.stringify(errorLogs)).should('not.contain', 'password');
    cy.wrap(JSON.stringify(errorLogs)).should('not.contain', 'creditCard');
  });
});
```

**Utilitário de log de erro com ocultação**:

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
 * Ocultar dados sensíveis de objetos
 */
function redactSensitiveData(obj: any): any {
  if (typeof obj !== 'object' || obj === null) return obj;

  const redacted = { ...obj };

  for (const key of Object.keys(redacted)) {
    if (SENSITIVE_KEYS.some((sensitive) => key.toLowerCase().includes(sensitive))) {
      redacted[key] = '[OCULTADO]';
    } else if (typeof redacted[key] === 'object') {
      redacted[key] = redactSensitiveData(redacted[key]);
    }
  }

  return redacted;
}

/**
 * Logar erro com contexto (integração Sentry)
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

  // Console (desenvolvimento)
  console.error(JSON.stringify(errorLog));

  // Sentry (produção)
  if (typeof window !== 'undefined' && (window as any).Sentry) {
    (window as any).Sentry.captureException(error, {
      contexts: { custom: safeContext },
    });
  }
}
```

**Pontos Chave**:

- **Log rico em contexto**: Endpoint, método, status, ID de usuário
- **Ocultação de segredo**: Senhas, tokens, PII removidos antes de logar
- **Integração Sentry**: Monitoramento de produção com breadcrumbs
- **Logs estruturados**: Formato JSON para parsing fácil
- **Validação de teste**: Assegure que logs contêm contexto mas não segredos

---

### Exemplo 4: Testes de Degradação Graciosa (Comportamento de Fallback)

**Contexto**: Valide que aplicação continua funcionando quando serviços estão indisponíveis.

**Implementação**:

```typescript
// tests/e2e/graceful-degradation.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Padrão de Degradação Graciosa
 * - Simular indisponibilidade de serviço
 * - Validar comportamento de fallback
 * - Garantir que experiência do usuário degrade graciosamente
 * - Verificar que telemetria captura eventos de degradação
 */

test.describe('Indisponibilidade de Serviço', () => {
  test('deve exibir dados em cache quando API está fora', async ({ page }) => {
    // Arrange: Semear localStorage com dados em cache
    await page.addInitScript(() => {
      localStorage.setItem(
        'products_cache',
        JSON.stringify({
          data: [
            { id: 1, name: 'Produto Cacheado 1' },
            { id: 2, name: 'Produto Cacheado 2' },
          ],
          timestamp: Date.now(),
        }),
      );
    });

    // Mock API indisponível
    await page.route(
      '**/api/products',
      (route) => route.abort('connectionrefused'), // Simular servidor fora
    );

    // Act
    await page.goto('/products');

    // Assert: Dados em cache exibidos
    await expect(page.getByTestId('product-list')).toBeVisible();
    await expect(page.getByText('Produto Cacheado 1')).toBeVisible();

    // Assert: Aviso de dados obsoletos mostrado
    await expect(page.getByTestId('cache-warning')).toBeVisible();
    await expect(page.getByTestId('cache-warning')).toContainText(/exibindo.*cacheado|modo.*offline/i);

    // Assert: Botão de tentar novamente disponível
    await expect(page.getByTestId('refresh-button')).toBeVisible();
  });

  test('deve mostrar UI de fallback quando serviço de analytics falha', async ({ page }) => {
    // Mock serviço de analytics fora (não crítico)
    await page.route('**/analytics/track', (route) => route.fulfill({ status: 503, body: 'Serviço indisponível' }));

    // Act: Navegar normalmente
    await page.goto('/dashboard');

    // Assert: Página carrega com sucesso (falha de analytics não bloqueia)
    await expect(page.getByTestId('dashboard-content')).toBeVisible();

    // Assert: Erro de analytics logado mas não mostrado ao usuário
    const consoleErrors = [];
    page.on('console', (msg) => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });

    // Disparar evento de analytics
    await page.getByTestId('track-action-button').click();

    // Erro de analytics logado
    expect(consoleErrors).toContainEqual(expect.stringContaining('Serviço de analytics indisponível'));

    // Mas usuário não vê erro
    await expect(page.getByTestId('error-message')).not.toBeVisible();
  });

  test('deve fazer fallback para validação local quando API está lenta', async ({ page }) => {
    // Mock API lenta (> 5 segundos)
    await page.route('**/api/validate-email', async (route) => {
      await new Promise((resolve) => setTimeout(resolve, 6000)); // atraso de 6 segundos
      route.fulfill({
        status: 200,
        body: JSON.stringify({ valid: true }),
      });
    });

    // Act: Preencher formulário
    await page.goto('/signup');
    await page.getByTestId('email-input').fill('test@example.com');
    await page.getByTestId('email-input').blur();

    // Assert: Validação client-side dispara imediatamente (não espera por API)
    await expect(page.getByTestId('email-valid-icon')).toBeVisible({ timeout: 1000 });

    // Assert: Eventualmente API valida também (mas não bloqueia UX)
    await expect(page.getByTestId('email-validated-badge')).toBeVisible({ timeout: 7000 });
  });

  test('deve manter funcionalidade com falha de script de terceiros', async ({ page }) => {
    // Bloquear scripts de terceiros (Google Analytics, Intercom, etc.)
    await page.route('**/*.google-analytics.com/**', (route) => route.abort());
    await page.route('**/*.intercom.io/**', (route) => route.abort());

    // Act
    await page.goto('/');

    // Assert: App funciona sem scripts externos
    await expect(page.getByTestId('main-content')).toBeVisible();
    await expect(page.getByTestId('nav-menu')).toBeVisible();

    // Assert: Funcionalidade principal intacta
    await page.getByTestId('nav-products').click();
    await expect(page).toHaveURL(/.*\/products/);
  });
});
```

**Pontos Chave**:

- **Fallbacks em cache**: Exibir dados obsoletos quando API indisponível
- **Degradação não crítica**: Falhas de analytics não bloqueiam app
- **Fallbacks client-side**: Validação local quando API lenta
- **Resiliência de terceiros**: App funciona sem scripts externos
- **Transparência do usuário**: Avisos de dados obsoletos exibidos

---

## Checklist de Teste de Tratamento de Erro

Antes de enviar código de tratamento de erro, verifique:

- [ ] **Tratamento de exceção com escopo**: Apenas ignore erros documentados (NetworkError, códigos específicos)
- [ ] **Relançar inesperados**: Erros desconhecidos falham testes (capturar regressões)
- [ ] **UI de erro testada**: Usuário vê mensagens de erro para todos os estados de erro
- [ ] **Lógica de retentativa validada**: Falhas sequenciais testam backoff e max tentativas
- [ ] **Telemetria verificada**: Erros logados com contexto (endpoint, status, usuário)
- [ ] **Ocultação de segredo**: Logs não contêm senhas, tokens, PII
- [ ] **Degradação graciosa**: Serviços críticos fora, app mostra UI de fallback
- [ ] **Falhas não críticas**: Falhas de analytics/rastreamento não bloqueiam app

## Pontos de Integração

- Usado em workflows: `*automate` (geração de teste de tratamento de erro), `*test-review` (detecção de padrão de erro)
- Fragmentos relacionados: `network-first.md`, `test-quality.md`, `contract-testing.md`
- Ferramentas de monitoramento: Sentry, Datadog, LogRocket

_Fonte: Padrões de tratamento de erro Murat, guia de resiliência Pact, tratamento de erro de produção SEON_
