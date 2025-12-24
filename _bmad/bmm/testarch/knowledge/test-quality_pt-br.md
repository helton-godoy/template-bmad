# Definição de Conclusão de Qualidade de Teste

## Princípio

Testes devem ser determinísticos, isolados, explícitos, focados e rápidos. Cada teste deve executar em menos de 1,5 minutos, conter menos de 300 linhas, evitar esperas fixas e condicionais, manter asserções visíveis nos corpos dos testes e limpar-se após a execução para execução paralela.

## Motivação

Testes de qualidade fornecem sinal confiável sobre a saúde da aplicação. Testes instáveis erodem a confiança e desperdiçam tempo de engenharia. Testes que usam esperas fixas (`waitForTimeout(3000)`) são não-determinísticos e lentos. Testes com asserções ocultas ou lógica condicional tornam-se insustentáveis. Testes grandes (>300 linhas) são difíceis de entender e depurar. Testes lentos (>1,5 min) bloqueiam pipelines de CI. Testes autolimpantes previnem poluição de estado em execuções paralelas.

## Exemplos de Padrões

### Exemplo 1: Padrão de Teste Determinístico

**Contexto**: Ao escrever testes, elimine todas as fontes de não-determinismo: esperas fixas, condicionais controlando fluxo, try-catch para controle de fluxo e dados aleatórios sem sementes.

**Implementação**:

```typescript
// ❌ RUIM: Teste não-determinístico com condicionais e esperas fixas
test('usuário pode ver painel - INSTÁVEL', async ({ page }) => {
  await page.goto('/dashboard');
  await page.waitForTimeout(3000); // NUNCA - espera arbitrária

  // Controle de fluxo condicional - comportamento do teste varia
  if (await page.locator('[data-testid="welcome-banner"]').isVisible()) {
    await page.click('[data-testid="dismiss-banner"]');
    await page.waitForTimeout(500);
  }

  // Try-catch para controle de fluxo - esconde problemas reais
  try {
    await page.click('[data-testid="load-more"]');
  } catch (e) {
    // Continua silenciosamente - teste passa mesmo se botão faltar
  }

  // Dados aleatórios sem controle
  const randomEmail = `user${Math.random()}@example.com`;
  await expect(page.getByText(randomEmail)).toBeVisible(); // Falhará aleatoriamente
});

// ✅ BOM: Teste determinístico com esperas explícitas
test('usuário pode ver painel', async ({ page, apiRequest }) => {
  const user = createUser({ email: 'test@example.com', hasSeenWelcome: true });

  // Setup via API (rápido, controlado)
  await apiRequest.post('/api/users', { data: user });

  // Network-first: Interceptar ANTES de navegar
  const dashboardPromise = page.waitForResponse((resp) => resp.url().includes('/api/dashboard') && resp.status() === 200);

  await page.goto('/dashboard');

  // Esperar por resposta real, não tempo arbitrário
  const dashboardResponse = await dashboardPromise;
  const dashboard = await dashboardResponse.json();

  // Asserções explícitas com dados controlados
  await expect(page.getByText(`Bem-vindo, ${user.name}`)).toBeVisible();
  await expect(page.getByTestId('dashboard-items')).toHaveCount(dashboard.items.length);

  // Sem condicionais - teste sempre executa mesmo caminho
  // Sem try-catch - falhas sobem claramente
});

// Equivalente Cypress
describe('Painel', () => {
  it('deve exibir painel do usuário', () => {
    const user = createUser({ email: 'test@example.com', hasSeenWelcome: true });

    // Setup via task (rápido, controlado)
    cy.task('db:seed', { users: [user] });

    // Interceptação network-first
    cy.intercept('GET', '**/api/dashboard').as('getDashboard');

    cy.visit('/dashboard');

    // Espera determinística por resposta
    cy.wait('@getDashboard').then((interception) => {
      const dashboard = interception.response.body;

      // Asserções explícitas
      cy.contains(`Bem-vindo, ${user.name}`).should('be.visible');
      cy.get('[data-cy="dashboard-items"]').should('have.length', dashboard.items.length);
    });
  });
});
```

**Pontos Chave**:

- Substitua `waitForTimeout()` por `waitForResponse()` ou verificações de estado de elemento
- Nunca use if/else para controlar fluxo de teste - testes devem ser determinísticos
- Evite try-catch para controle de fluxo - deixe falhas subirem claramente
- Use funções factory com dados controlados, não `Math.random()`
- Padrão network-first previne condições de corrida

### Exemplo 2: Teste Isolado com Limpeza

**Contexto**: Quando testes criam dados, eles devem limpar a si mesmos para prevenir poluição de estado em execuções paralelas. Use autolimpeza de fixture ou teardown explícito.

**Implementação**:

```typescript
// ❌ RUIM: Teste deixa dados para trás, polui outros testes
test('admin pode criar usuário - POLUI ESTADO', async ({ page, apiRequest }) => {
  await page.goto('/admin/users');

  // Email hardcoded - colide em execuções paralelas
  await page.fill('[data-testid="email"]', 'newuser@example.com');
  await page.fill('[data-testid="name"]', 'Novo Usuário');
  await page.click('[data-testid="create-user"]');

  await expect(page.getByText('Usuário criado')).toBeVisible();

  // SEM LIMPEZA - usuário permanece no banco de dados
  // Próxima execução de teste falha: "Email já existe"
});

// ✅ BOM: Teste limpa com autolimpeza de fixture
// playwright/support/fixtures/database-fixture.ts
import { test as base } from '@playwright/test';
import { deleteRecord, seedDatabase } from '../helpers/db-helpers';

type DatabaseFixture = {
  seedUser: (userData: Partial<User>) => Promise<User>;
};

export const test = base.extend<DatabaseFixture>({
  seedUser: async ({}, use) => {
    const createdUsers: string[] = [];

    const seedUser = async (userData: Partial<User>) => {
      const user = await seedDatabase('users', userData);
      createdUsers.push(user.id); // Rastrear para limpeza
      return user;
    };

    await use(seedUser);

    // Autolimpeza: Deletar todos usuários criados durante teste
    for (const userId of createdUsers) {
      await deleteRecord('users', userId);
    }
    createdUsers.length = 0;
  },
});

// Usar a fixture
test('admin pode criar usuário', async ({ page, seedUser }) => {
  // Criar admin com dados únicos
  const admin = await seedUser({
    email: faker.internet.email(), // Único a cada execução
    role: 'admin',
  });

  await page.goto('/admin/users');

  const newUserEmail = faker.internet.email(); // Único
  await page.fill('[data-testid="email"]', newUserEmail);
  await page.fill('[data-testid="name"]', 'Novo Usuário');
  await page.click('[data-testid="create-user"]');

  await expect(page.getByText('Usuário criado')).toBeVisible();

  // Verificar no banco de dados
  const createdUser = await seedUser({ email: newUserEmail });
  expect(createdUser.email).toBe(newUserEmail);

  // Autolimpeza acontece via teardown de fixture
});

// Equivalente Cypress com limpeza explícita
describe('Gerenciamento de Usuário Admin', () => {
  const createdUserIds: string[] = [];

  afterEach(() => {
    // Limpeza: Deletar todos usuários criados durante teste
    createdUserIds.forEach((userId) => {
      cy.task('db:delete', { table: 'users', id: userId });
    });
    createdUserIds.length = 0;
  });

  it('deve criar usuário', () => {
    const admin = createUser({ role: 'admin' });
    const newUser = createUser(); // Dados únicos via faker

    cy.task('db:seed', { users: [admin] }).then((result: any) => {
      createdUserIds.push(result.users[0].id);
    });

    cy.visit('/admin/users');
    cy.get('[data-cy="email"]').type(newUser.email);
    cy.get('[data-cy="name"]').type(newUser.name);
    cy.get('[data-cy="create-user"]').click();

    cy.contains('Usuário criado').should('be.visible');

    // Rastrear para limpeza
    cy.task('db:findByEmail', newUser.email).then((user: any) => {
      createdUserIds.push(user.id);
    });
  });
});
```

**Pontos Chave**:

- Use fixtures com autolimpeza via teardown (após `use()`)
- Rastreie todos recursos criados em array durante execução do teste
- Use `faker` para dados únicos - previne colisões paralelas
- Cypress: Use `afterEach()` com limpeza explícita
- Nunca hardcode IDs ou emails - sempre gere valores únicos

### Exemplo 3: Asserções Explícitas em Testes

**Contexto**: Ao validar resultados de teste, mantenha asserções visíveis nos corpos dos testes. Nunca esconda asserções em funções helper - isso obscurece a intenção do teste e torna falhas mais difíceis de diagnosticar.

**Implementação**:

```typescript
// ❌ RUIM: Asserções escondidas em funções helper
// helpers/api-validators.ts
export async function validateUserCreation(response: Response, expectedEmail: string) {
  const user = await response.json();
  expect(response.status()).toBe(201);
  expect(user.email).toBe(expectedEmail);
  expect(user.id).toBeTruthy();
  expect(user.createdAt).toBeTruthy();
  // Asserções escondidas - não visíveis no teste
}

test('criar usuário via API - OPACO', async ({ request }) => {
  const userData = createUser({ email: 'test@example.com' });

  const response = await request.post('/api/users', { data: userData });

  // Quais asserções estão rodando? Tenho que verificar helper.
  await validateUserCreation(response, userData.email);
  // Quando isso falha, erro é: "validateUserCreation falhou" - NÃO útil
});

// ✅ BOM: Asserções explícitas no teste
test('criar usuário via API', async ({ request }) => {
  const userData = createUser({ email: 'test@example.com' });

  const response = await request.post('/api/users', { data: userData });

  // Todas asserções visíveis - intenção de teste clara
  expect(response.status()).toBe(201);

  const createdUser = await response.json();
  expect(createdUser.id).toBeTruthy();
  expect(createdUser.email).toBe(userData.email);
  expect(createdUser.name).toBe(userData.name);
  expect(createdUser.role).toBe('user');
  expect(createdUser.createdAt).toBeTruthy();
  expect(createdUser.isActive).toBe(true);

  // Quando isso falha, erro é: "Esperado role ser 'user', obteve 'admin'" - ÚTIL
});

// ✅ ACEITÁVEL: Helper para extração de dados, NÃO asserções
// helpers/api-extractors.ts
export async function extractUserFromResponse(response: Response): Promise<User> {
  const user = await response.json();
  return user; // Apenas extrai, sem asserções
}

test('criar usuário com helper de extração', async ({ request }) => {
  const userData = createUser({ email: 'test@example.com' });

  const response = await request.post('/api/users', { data: userData });

  // Extrair dados com helper (OK)
  const createdUser = await extractUserFromResponse(response);

  // Mas manter asserções no teste (OBRIGATÓRIO)
  expect(response.status()).toBe(201);
  expect(createdUser.email).toBe(userData.email);
  expect(createdUser.role).toBe('user');
});

// Equivalente Cypress
describe('API Usuário', () => {
  it('deve criar usuário com asserções explícitas', () => {
    const userData = createUser({ email: 'test@example.com' });

    cy.request('POST', '/api/users', userData).then((response) => {
      // Todas asserções visíveis no teste
      expect(response.status).to.equal(201);
      expect(response.body.id).to.exist;
      expect(response.body.email).to.equal(userData.email);
      expect(response.body.name).to.equal(userData.name);
      expect(response.body.role).to.equal('user');
      expect(response.body.createdAt).to.exist;
      expect(response.body.isActive).to.be.true;
    });
  });
});

// ✅ BOM: Testes parametrizados para asserções soft (validação em massa)
test.describe('Validação de criação de usuário', () => {
  const testCases = [
    { field: 'email', value: 'test@example.com', expected: 'test@example.com' },
    { field: 'name', value: 'Test User', expected: 'Test User' },
    { field: 'role', value: 'admin', expected: 'admin' },
    { field: 'isActive', value: true, expected: true },
  ];

  for (const { field, value, expected } of testCases) {
    test(`deve definir ${field} corretamente`, async ({ request }) => {
      const userData = createUser({ [field]: value });

      const response = await request.post('/api/users', { data: userData });
      const user = await response.json();

      // Asserção parametrizada - ainda explícita
      expect(user[field]).toBe(expected);
    });
  }
});
```

**Pontos Chave**:

- Nunca esconda chamadas `expect()` em funções helper
- Helpers podem extrair/transformar dados, mas asserções ficam nos testes
- Testes parametrizados são aceitáveis para validação em massa (ainda explícitos)
- Asserções explícitas tornam falhas acionáveis: "Esperado X, obteve Y"
- Asserções ocultas produzem falhas vagas: "Função helper falhou"

### Exemplo 4: Limites de Tamanho de Teste

**Contexto**: Quando testes crescem além de 300 linhas, eles se tornam difíceis de entender, depurar e manter. Refatore testes longos extraindo helpers de setup, dividindo cenários ou usando fixtures.

**Implementação**:

```typescript
// ❌ RUIM: Teste monolítico de 400 linhas (truncado para exemplo)
test('jornada completa de usuário - MUITO LONGO', async ({ page, request }) => {
  // 50 linhas de setup
  const admin = createUser({ role: 'admin' });
  await request.post('/api/users', { data: admin });
  await page.goto('/login');
  await page.fill('[data-testid="email"]', admin.email);
  await page.fill('[data-testid="password"]', 'password123');
  await page.click('[data-testid="login"]');
  await expect(page).toHaveURL('/dashboard');

  // 100 linhas de criação de usuário
  await page.goto('/admin/users');
  const newUser = createUser();
  await page.fill('[data-testid="email"]', newUser.email);
  // ... mais 95 linhas de preenchimento de formulário, validação, etc.

  // 100 linhas de atribuição de permissões
  await page.click('[data-testid="assign-permissions"]');
  // ... mais 95 linhas

  // 100 linhas de preferências de notificação
  await page.click('[data-testid="notification-settings"]');
  // ... mais 95 linhas

  // 50 linhas de limpeza
  await request.delete(`/api/users/${newUser.id}`);
  // ... mais 45 linhas

  // TOTAL: 400 linhas - impossível de entender ou depurar
});

// ✅ BOM: Dividir em testes focados com fixture compartilhada
// playwright/support/fixtures/admin-fixture.ts
export const test = base.extend({
  adminPage: async ({ page, request }, use) => {
    // Setup compartilhado: Login como admin
    const admin = createUser({ role: 'admin' });
    await request.post('/api/users', { data: admin });

    await page.goto('/login');
    await page.fill('[data-testid="email"]', admin.email);
    await page.fill('[data-testid="password"]', 'password123');
    await page.click('[data-testid="login"]');
    await expect(page).toHaveURL('/dashboard');

    await use(page); // Fornecer página logada

    // Limpeza tratada pela fixture
  },
});

// Teste 1: Criação de usuário (50 linhas)
test('admin pode criar usuário', async ({ adminPage, seedUser }) => {
  await adminPage.goto('/admin/users');

  const newUser = createUser();
  await adminPage.fill('[data-testid="email"]', newUser.email);
  await adminPage.fill('[data-testid="name"]', newUser.name);
  await adminPage.click('[data-testid="role-dropdown"]');
  await adminPage.click('[data-testid="role-user"]');
  await adminPage.click('[data-testid="create-user"]');

  await expect(adminPage.getByText('Usuário criado')).toBeVisible();
  await expect(adminPage.getByText(newUser.email)).toBeVisible();

  // Verificar no banco de dados
  const created = await seedUser({ email: newUser.email });
  expect(created.role).toBe('user');
});

// Teste 2: Atribuição de permissão (60 linhas)
test('admin pode atribuir permissões', async ({ adminPage, seedUser }) => {
  const user = await seedUser({ email: faker.internet.email() });

  await adminPage.goto(`/admin/users/${user.id}`);
  await adminPage.click('[data-testid="assign-permissions"]');
  await adminPage.check('[data-testid="permission-read"]');
  await adminPage.check('[data-testid="permission-write"]');
  await adminPage.click('[data-testid="save-permissions"]');

  await expect(adminPage.getByText('Permissões atualizadas')).toBeVisible();

  // Verificar permissões atribuídas
  const response = await adminPage.request.get(`/api/users/${user.id}`);
  const updated = await response.json();
  expect(updated.permissions).toContain('read');
  expect(updated.permissions).toContain('write');
});

// Teste 3: Preferências de notificação (70 linhas)
test('admin pode atualizar preferências de notificação', async ({ adminPage, seedUser }) => {
  const user = await seedUser({ email: faker.internet.email() });

  await adminPage.goto(`/admin/users/${user.id}/notifications`);
  await adminPage.check('[data-testid="email-notifications"]');
  await adminPage.uncheck('[data-testid="sms-notifications"]');
  await adminPage.selectOption('[data-testid="frequency"]', 'daily');
  await adminPage.click('[data-testid="save-preferences"]');

  await expect(adminPage.getByText('Preferências salvas')).toBeVisible();

  // Verificar preferências
  const response = await adminPage.request.get(`/api/users/${user.id}/preferences`);
  const prefs = await response.json();
  expect(prefs.emailEnabled).toBe(true);
  expect(prefs.smsEnabled).toBe(false);
  expect(prefs.frequency).toBe('daily');
});

// TOTAL: 3 testes × 60 linhas média = 180 linhas
// Cada teste é focado, depurável e abaixo de 300 linhas
```

**Pontos Chave**:

- Divida testes monolíticos em cenários focados (<300 linhas cada)
- Extraia setup comum em fixtures (auto-executa para cada teste)
- Cada teste valida uma preocupação (criação de usuário, permissões, preferências)
- Falhas são mais fáceis de diagnosticar: "Atribuição de permissão falhou" vs "Jornada completa falhou"
- Testes podem rodar em paralelo (preocupações isoladas)

### Exemplo 5: Otimização de Tempo de Execução

**Contexto**: Quando testes demoram mais de 1,5 minutos, eles lentificam pipelines de CI e ciclos de feedback. Otimize usando setup de API em vez de navegação de UI, paralelizando operações independentes e evitando esperas desnecessárias.

**Implementação**:

```typescript
// ❌ RUIM: Teste de 4 minutos (setup lento, operações sequenciais)
test('usuário completa pedido - LENTO (4 min)', async ({ page }) => {
  // Passo 1: Inscrição manual via UI (90 segundos)
  await page.goto('/signup');
  await page.fill('[data-testid="email"]', 'buyer@example.com');
  await page.fill('[data-testid="password"]', 'password123');
  await page.fill('[data-testid="confirm-password"]', 'password123');
  await page.fill('[data-testid="name"]', 'Buyer User');
  await page.click('[data-testid="signup"]');
  await page.waitForURL('/verify-email'); // Esperar por verificação de email
  // ... fluxo de verificação de email manual

  // Passo 2: Criação manual de produto via UI (60 segundos)
  await page.goto('/admin/products');
  await page.fill('[data-testid="product-name"]', 'Widget');
  // ... mais 20 campos
  await page.click('[data-testid="create-product"]');

  // Passo 3: Navegar para checkout (30 segundos)
  await page.goto('/products');
  await page.waitForTimeout(5000); // Espera fixa desnecessária
  await page.click('[data-testid="product-widget"]');
  await page.waitForTimeout(3000); // Desnecessário
  await page.click('[data-testid="add-to-cart"]');
  await page.waitForTimeout(2000); // Desnecessário

  // Passo 4: Completar checkout (40 segundos)
  await page.goto('/checkout');
  await page.waitForTimeout(5000); // Desnecessário
  await page.fill('[data-testid="credit-card"]', '4111111111111111');
  // ... mais preenchimento de formulário
  await page.click('[data-testid="submit-order"]');
  await page.waitForTimeout(10000); // Desnecessário

  await expect(page.getByText('Pedido Confirmado')).toBeVisible();

  // TOTAL: ~240 segundos (4 minutos)
});

// ✅ BOM: Teste de 45 segundos (setup API, ops paralelas, esperas determinísticas)
test('usuário completa pedido', async ({ page, apiRequest }) => {
  // Passo 1: Setup API (paralelo, 5 segundos total)
  const [user, product] = await Promise.all([
    // Criar usuário via API (rápido)
    apiRequest
      .post('/api/users', {
        data: createUser({
          email: 'buyer@example.com',
          emailVerified: true, // Pular verificação
        }),
      })
      .then((r) => r.json()),

    // Criar produto via API (rápido)
    apiRequest
      .post('/api/products', {
        data: createProduct({
          name: 'Widget',
          price: 29.99,
          stock: 10,
        }),
      })
      .then((r) => r.json()),
  ]);

  // Passo 2: Setup Auth via estado de armazenamento (instantâneo, 0 segundos)
  await page.context().addCookies([
    {
      name: 'auth_token',
      value: user.token,
      domain: 'localhost',
      path: '/',
    },
  ]);

  // Passo 3: Interceptação network-first ANTES da navegação (10 segundos)
  const cartPromise = page.waitForResponse('**/api/cart');
  const orderPromise = page.waitForResponse('**/api/orders');

  await page.goto(`/products/${product.id}`);
  await page.click('[data-testid="add-to-cart"]');
  await cartPromise; // Espera determinística (sem espera fixa)

  // Passo 4: Checkout com esperas de rede (30 segundos)
  await page.goto('/checkout');
  await page.fill('[data-testid="credit-card"]', '4111111111111111');
  await page.fill('[data-testid="cvv"]', '123');
  await page.fill('[data-testid="expiry"]', '12/25');
  await page.click('[data-testid="submit-order"]');
  await orderPromise; // Espera determinística (sem espera fixa)

  await expect(page.getByText('Pedido Confirmado')).toBeVisible();
  await expect(page.getByText(`Pedido #${product.id}`)).toBeVisible();

  // TOTAL: ~45 segundos (6x mais rápido)
});

// Equivalente Cypress
describe('Fluxo de Pedido', () => {
  it('deve completar compra rapidamente', () => {
    // Passo 1: Setup API (paralelo, rápido)
    const user = createUser({ emailVerified: true });
    const product = createProduct({ name: 'Widget', price: 29.99 });

    cy.task('db:seed', { users: [user], products: [product] });

    // Passo 2: Setup Auth via sessão (instantâneo)
    cy.setCookie('auth_token', user.token);

    // Passo 3: Interceptação network-first
    cy.intercept('POST', '**/api/cart').as('addToCart');
    cy.intercept('POST', '**/api/orders').as('createOrder');

    cy.visit(`/products/${product.id}`);
    cy.get('[data-cy="add-to-cart"]').click();
    cy.wait('@addToCart'); // Espera determinística

    // Passo 4: Checkout
    cy.visit('/checkout');
    cy.get('[data-cy="credit-card"]').type('4111111111111111');
    cy.get('[data-cy="cvv"]').type('123');
    cy.get('[data-cy="expiry"]').type('12/25');
    cy.get('[data-cy="submit-order"]').click();
    cy.wait('@createOrder'); // Espera determinística

    cy.contains('Pedido Confirmado').should('be.visible');
    cy.contains(`Pedido #${product.id}`).should('be.visible');
  });
});

// Otimização adicional: Estado de auth compartilhado (0 segundos por teste)
// playwright/support/global-setup.ts
export default async function globalSetup() {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Criar usuário admin uma vez para todos os testes
  const admin = createUser({ role: 'admin', emailVerified: true });
  await page.request.post('/api/users', { data: admin });

  // Logar uma vez, salvar sessão
  await page.goto('/login');
  await page.fill('[data-testid="email"]', admin.email);
  await page.fill('[data-testid="password"]', 'password123');
  await page.click('[data-testid="login"]');

  // Salvar estado de auth para reuso
  await page.context().storageState({ path: 'playwright/.auth/admin.json' });

  await browser.close();
}

// Usar auth compartilhado em testes (instantâneo)
test.use({ storageState: 'playwright/.auth/admin.json' });

test('ação de admin', async ({ page }) => {
  // Já logado - sem overhead de auth (0 segundos)
  await page.goto('/admin');
  // ... lógica de teste
});
```

**Pontos Chave**:

- Use API para setup de dados (10-50x mais rápido que UI)
- Rode operações independentes em paralelo (`Promise.all`)
- Substitua esperas fixas com esperas determinísticas (`waitForResponse`)
- Reutilize sessões de auth via `storageState` (Playwright) ou `setCookie` (Cypress)
- Pule fluxos desnecessários (verificação de email, inscrições multi-passo)

## Pontos de Integração

- **Usado em workflows**: `*atdd` (qualidade de geração de teste), `*automate` (qualidade de expansão de teste), `*test-review` (validação de qualidade)
- **Fragmentos relacionados**:
  - `network-first.md` - Estratégias de espera determinística
  - `data-factories.md` - Padrões de dados isolados, seguros para paralelo
  - `fixture-architecture.md` - Extração de setup e limpeza
  - `test-levels-framework.md` - Escolhendo granularidade de teste apropriada para velocidade

## Checklist de Qualidade Principal

Todo teste deve passar nestes critérios:

- [ ] **Sem Esperas Fixas** - Use `waitForResponse`, `waitForLoadState` ou estado de elemento (não `waitForTimeout`)
- [ ] **Sem Condicionais** - Testes executam o mesmo caminho toda vez (sem if/else, try/catch para controle de fluxo)
- [ ] **< 300 Linhas** - Mantenha testes focados; divida testes grandes ou extraia setup para fixtures
- [ ] **< 1,5 Minutos** - Otimize com setup de API, operações paralelas e auth compartilhado
- [ ] **Autolimpante** - Use fixtures com autolimpeza ou teardown explícito `afterEach()`
- [ ] **Asserções Explícitas** - Mantenha chamadas `expect()` em corpos de teste, não escondidas em helpers
- [ ] **Dados Únicos** - Use `faker` para dados dinâmicos; nunca hardcode IDs ou emails
- [ ] **Seguro para Paralelo** - Testes não compartilham estado; rodam com sucesso com `--workers=4`

_Fonte: Checklist de qualidade Murat, Requisitos de Definição de Conclusão (linhas 370-381, 406-422)._
