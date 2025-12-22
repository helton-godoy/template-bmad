# Definição da qualidade do ensaio

## Princípio

Os testes devem ser determinísticos, isolados, explícitos, focados e rápidos. Cada teste deve ser executado em menos de 1,5 minutos, conter menos de 300 linhas, evitar esperas difíceis e condicionais, manter as afirmações visíveis em corpos de teste e limpar após si mesmo para execução paralela.

## Racional

Testes de qualidade fornecem sinal confiável sobre a saúde da aplicação. Testes flácidos corroem a confiança e desperdiçam tempo de engenharia. Os testes que utilizam esperas duras (`waitForTimeout(3000)`) são não determinísticos e lentos. Testes com asserções ocultas ou lógica condicional tornam-se inmanutáveis. Testes grandes (>300 linhas) são difíceis de entender e depurar. Testes lentos (>1,5 min) bloqueiam condutas de IC. Testes de autolimpeza evitam a poluição do estado em paralelo.

## Exemplos de padrões

### Exemplo 1: Padrão de teste determinístico

**Contexto**: Ao escrever testes, eliminar todas as fontes de não-determinismo: esperas difíceis, condicional controlando o fluxo, try-captch para controle de fluxo, e dados aleatórios sem sementes.

**Implementation**:

```typescript
// ❌ BAD: Non-deterministic test with conditionals and hard waits
test('user can view dashboard - FLAKY', async ({ page }) => {
  await page.goto('/dashboard');
  await page.waitForTimeout(3000); // NEVER - arbitrary wait

  // Conditional flow control - test behavior varies
  if (await page.locator('[data-testid="welcome-banner"]').isVisible()) {
    await page.click('[data-testid="dismiss-banner"]');
    await page.waitForTimeout(500);
  }

  // Try-catch for flow control - hides real issues
  try {
    await page.click('[data-testid="load-more"]');
  } catch (e) {
    // Silently continue - test passes even if button missing
  }

  // Random data without control
  const randomEmail = `user${Math.random()}@example.com`;
  await expect(page.getByText(randomEmail)).toBeVisible(); // Will fail randomly
});

// ✅ GOOD: Deterministic test with explicit waits
test('user can view dashboard', async ({ page, apiRequest }) => {
  const user = createUser({ email: 'test@example.com', hasSeenWelcome: true });

  // Setup via API (fast, controlled)
  await apiRequest.post('/api/users', { data: user });

  // Network-first: Intercept BEFORE navigate
  const dashboardPromise = page.waitForResponse((resp) => resp.url().includes('/api/dashboard') && resp.status() === 200);

  await page.goto('/dashboard');

  // Wait for actual response, not arbitrary time
  const dashboardResponse = await dashboardPromise;
  const dashboard = await dashboardResponse.json();

  // Explicit assertions with controlled data
  await expect(page.getByText(`Welcome, ${user.name}`)).toBeVisible();
  await expect(page.getByTestId('dashboard-items')).toHaveCount(dashboard.items.length);

  // No conditionals - test always executes same path
  // No try-catch - failures bubble up clearly
});

// Cypress equivalent
describe('Dashboard', () => {
  it('should display user dashboard', () => {
    const user = createUser({ email: 'test@example.com', hasSeenWelcome: true });

    // Setup via task (fast, controlled)
    cy.task('db:seed', { users: [user] });

    // Network-first interception
    cy.intercept('GET', '**/api/dashboard').as('getDashboard');

    cy.visit('/dashboard');

    // Deterministic wait for response
    cy.wait('@getDashboard').then((interception) => {
      const dashboard = interception.response.body;

      // Explicit assertions
      cy.contains(`Welcome, ${user.name}`).should('be.visible');
      cy.get('[data-cy="dashboard-items"]').should('have.length', dashboard.items.length);
    });
  });
});

```

**Pontos-chave**

- Substituir `waitForTimeout()` por `waitForResponse()` ou verificação do estado do elemento
- Nunca usar se/outro para controlar o fluxo de teste - testes devem ser determinísticos
- Evite tentar-captura para controle de fluxo - let falhas bolha para cima claramente
- Usar funções de fábrica com dados controlados, não `Math.random()`
- Primeiro padrão de rede previne condições de corrida

### Exemplo 2: Isolado Teste com limpeza

**Contexto**: Quando os testes criam dados, devem limpar-se para evitar a poluição do estado em corridas paralelas. Use a limpeza automática da instalação ou a remoção explícita.

**Implementation**:

«``typescript
// ❌ BAD: Teste deixa dados para trás, polui outros testes
bMADPROTECT016END ({ page, apiRequest }) => {
  await page.goto('/admin/users');

  // Hardcoded email - collides in parallel runs
  await page.fill('[data-testid="email"]', 'newuser@example.com');
  await page.fill('[data-testid="name"]', 'New User');
  await page.click('[data-testid="create-user"]');

  await expect(page.getByText('User created')).toBeVisible();

  // NO CLEANUP - user remains in database
  // Next test run fails: "Email already exists"
});

// ✅ BOM: Teste de limpeza com limpeza automática
// playwright/support/fixtures/database-fixture.ts
BMADPROTECT010end BMADPROTECT019end de '@ playwright/test';
BMADPROTECT009end BMADPROTECT018End from '../helpers/db-helpers'

tipo DatabaseFixture = {
seedUser: (userDat