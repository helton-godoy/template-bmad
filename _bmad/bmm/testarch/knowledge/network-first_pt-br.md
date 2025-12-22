# Primeiras salvaguardas da rede

## Princípio

Registre interceptações de rede **antes** de qualquer navegação ou ação do usuário. Armazene a promessa de interceptação e BMADPROTECT027 End-lo imediatamente após o passo de disparo. Substituir esperas implícitas por sinais determinísticos baseados em respostas de rede, desaparecimento do spinner ou ganchos de eventos.

## Racional

A fonte mais comum de testes Flaky E2E é **condições de corrida** entre navegação e intercepção de rede:

- Navegar e interceptar = pedidos perdidos (muito tarde)
- Nenhuma espera explícita = asserção é executada antes da resposta chegar
- Esperas difíceis (`waitForTimeout(3000)`) = lenta, não confiável, frágil

Os primeiros padrões da rede fornecem:

- **Condições de corrida Zero**: Intercepto é ativo antes de desencadear ação
- **Deterministic waits**: Espere por resposta real, não tempo limite arbitrário
- **Falhas acionáveis**: Assessoria sobre o estado/corpo de resposta, não genérico "elemento não encontrado"
- **Velocidade**: Sem estofamento com tempo de espera extra

## Exemplos de padrões

### Exemplo 1: Interceptar antes de navegar

**Contexto**: O padrão fundamental para todos os testes E2E. Registre sempre a intercepção da rota **antes** da ação que desencadeia o pedido (navegação, clique, envio do formulário).

**Implementation**:

```typescript
// ✅ CORRECT: Intercept BEFORE navigate
test('user can view dashboard data', async ({ page }) => {
  // Step 1: Register interception FIRST
  const usersPromise = page.waitForResponse((resp) => resp.url().includes('/api/users') && resp.status() === 200);

  // Step 2: THEN trigger the request
  await page.goto('/dashboard');

  // Step 3: THEN await the response
  const usersResponse = await usersPromise;
  const users = await usersResponse.json();

  // Step 4: Assert on structured data
  expect(users).toHaveLength(10);
  await expect(page.getByText(users[0].name)).toBeVisible();
});

// Cypress equivalent
describe('Dashboard', () => {
  it('should display users', () => {
    // Step 1: Register interception FIRST
    cy.intercept('GET', '**/api/users').as('getUsers');

    // Step 2: THEN trigger
    cy.visit('/dashboard');

    // Step 3: THEN await
    cy.wait('@getUsers').then((interception) => {
      // Step 4: Assert on structured data
      expect(interception.response.statusCode).to.equal(200);
      expect(interception.response.body).to.have.length(10);
      cy.contains(interception.response.body[0].name).should('be.visible');
    });
  });
});

// ❌ WRONG: Navigate BEFORE intercept (race condition!)
test('flaky test example', async ({ page }) => {
  await page.goto('/dashboard'); // Request fires immediately

  const usersPromise = page.waitForResponse('/api/users'); // TOO LATE - might miss it
  const response = await usersPromise; // May timeout randomly
});

```

**Pontos-chave**

- Playwright: Usar `page.waitForResponse()` com padrão de URL ou predicado **antes** `page.goto()` ou `page.click()`
- Cypress: Utilizar `cy.intercept().as()` **antes** `cy.visit()` ou `cy.click()`
- Armazenar promessa/alias, ação gatilho, **então** await resposta
- Isto previne 95% de flaquidez em condições raciais nos testes E2E

### Exemplo 2: Captura de HAR para depuração

**Context**: Ao depurar testes flácidos ou construir simulagens determinísticas, capture tráfego de rede real com arquivos HAR. Reproduza-os em testes para testes consistentes e com capacidade offline.

**Implementation**:

«``typescript
// dramaturgo.config.ts - Habilitar gravação HAR
export defineConfig ({
  use: {
    // Record HAR on first run
    recordHar: { path: './hars/', mode: 'minimal' },
// Ou repetir HAR em testes
// ServiçoTrabalhadores: **bloco**,
},
});

// Capturar HAR para teste específico
ensaio('rede de captura para fluxo de ordem', async ({ page, context }) => {
  // Start recording
  await context.routeFromHAR('./hars/order-flow.har', {
    url: '**/api/**',
    update: true, // Update HAR with new requests
  });

BMADPROTECT022End page.goto('/checkout');
BMADPROTECT021End page.fill('[data-testid="credit-card"]', '4111111111111111');
await page.click('[data-testid="submit-order"]');
await expect(page.getByText('Ordem Confirmada')).toBeVisible();

// HAR salvo em ./hars/order-flow.har
});

// Repetir HAR para testes determinísticos (sem API real necessária)
ensaio('replay order flow from HAR', async ({ page, context }) => {
  // Replay captured HAR
  await context.routeFromHAR('./hars/order-flow.har', {
    url: '**/api/**',
    update: false, // Read-only mode
  });

// Testes com respostas exatas gravadas - totalmente determinístico
await page.goto('/checkout');
BMADPROTECT015End page.fill('[data-testid="credit-card"]', '4111111111111111');
await page.click('[data-testid="submit-order"]');
await expect(page.getByText('Ordem Confirmada')).ToBeVisible();
});

// Mock personalizado baseado em insights HAR
teste('Resposta à ordem de molde baseado em HAR', async ({ page }) = > {
// Depois de analisar o HAR, crie uma simulação focada
BMADPROTECT011End page.route('**/api/orders', (route) =>
route.fulfill( {
      status: 200,
conteúdoTipo: **aplication/json**,
      body: JSON.stringify ({
orderId: **12345**,
status: 'confirmar