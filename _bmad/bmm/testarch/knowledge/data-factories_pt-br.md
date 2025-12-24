# Data Factories e Setup API-First

## Princípio

Prefira funções de factory que aceitem overrides e retornem objetos completos (`createUser(overrides)`). Semeie o estado do teste através de APIs, tasks ou helpers diretos de DB antes de visitar a UI—nunca via interações de UI lentas. UI é para validação apenas, não para setup.

## Motivação

Fixtures estáticas (arquivos JSON, objetos hardcoded) criam testes frágeis que:

- Falham quando esquemas evoluem (faltam novos campos obrigatórios)
- Causam colisões em execução paralela (mesmos IDs de usuário)
- Escondem a intenção do teste (o que importa para _este_ teste?)

Factories dinâmicas com overrides fornecem:

- **Segurança paralela**: UUIDs e timestamps previnem colisões
- **Evolução de esquema**: Padrões se adaptam a mudanças de esquema automaticamente
- **Intenção explícita**: Overrides mostram o que importa para cada teste
- **Velocidade**: Setup via API é 10-50x mais rápido que UI

## Exemplos de Padrões

### Exemplo 1: Função Factory com Overrides

**Contexto**: Ao criar dados de teste, construa funções de factory com padrões sensatos e overrides explícitos. Use `faker` para valores dinâmicos que previnem colisões.

**Implementação**:

```typescript
// test-utils/factories/user-factory.ts
import { faker } from '@faker-js/faker';

type User = {
  id: string;
  email: string;
  name: string;
  role: 'user' | 'admin' | 'moderator';
  createdAt: Date;
  isActive: boolean;
};

export const createUser = (overrides: Partial<User> = {}): User => ({
  id: faker.string.uuid(),
  email: faker.internet.email(),
  name: faker.person.fullName(),
  role: 'user',
  createdAt: new Date(),
  isActive: true,
  ...overrides,
});

// test-utils/factories/product-factory.ts
type Product = {
  id: string;
  name: string;
  price: number;
  stock: number;
  category: string;
};

export const createProduct = (overrides: Partial<Product> = {}): Product => ({
  id: faker.string.uuid(),
  name: faker.commerce.productName(),
  price: parseFloat(faker.commerce.price()),
  stock: faker.number.int({ min: 0, max: 100 }),
  category: faker.commerce.department(),
  ...overrides,
});

// Uso em testes:
test('admin pode deletar usuários', async ({ page, apiRequest }) => {
  // Usuário padrão
  const user = createUser();

  // Usuário admin (override explícito mostra intenção)
  const admin = createUser({ role: 'admin' });

  // Semeia via API (rápido!)
  await apiRequest({ method: 'POST', url: '/api/users', data: user });
  await apiRequest({ method: 'POST', url: '/api/users', data: admin });

  // Agora testa comportamento da UI
  await page.goto('/admin/users');
  await page.click(`[data-testid="delete-user-${user.id}"]`);
  await expect(page.getByText(`User ${user.name} deleted`)).toBeVisible();
});
```

**Pontos Chave**:

- `Partial<User>` permite sobrescrever qualquer campo sem quebrar a segurança de tipos
- Faker gera valores únicos—sem colisões em testes paralelos
- Override mostra a intenção do teste: `createUser({ role: 'admin' })` é explícito
- Factory vive em `test-utils/factories/` para fácil reutilização

### Exemplo 2: Padrão de Factory Aninhada

**Contexto**: Ao testar relacionamentos (pedidos com usuários e produtos), aninhe factories para criar grafos de objetos completos. Controle dados de relacionamento explicitamente.

**Implementação**:

```typescript
// test-utils/factories/order-factory.ts
import { createUser } from './user-factory';
import { createProduct } from './product-factory';

type OrderItem = {
  product: Product;
  quantity: number;
  price: number;
};

type Order = {
  id: string;
  user: User;
  items: OrderItem[];
  total: number;
  status: 'pending' | 'paid' | 'shipped' | 'delivered';
  createdAt: Date;
  isActive: boolean;
};

export const createOrderItem = (overrides: Partial<OrderItem> = {}): OrderItem => {
  const product = overrides.product || createProduct();
  const quantity = overrides.quantity || faker.number.int({ min: 1, max: 5 });

  return {
    product,
    quantity,
    price: product.price * quantity,
    ...overrides,
  };
};

export const createOrder = (overrides: Partial<Order> = {}): Order => {
  const items = overrides.items || [createOrderItem(), createOrderItem()];
  const total = items.reduce((sum, item) => sum + item.price, 0);

  return {
    id: faker.string.uuid(),
    user: overrides.user || createUser(),
    items,
    total,
    status: 'pending',
    createdAt: new Date(),
    ...overrides,
  };
};

// Uso em testes:
test('usuário pode ver detalhes do pedido', async ({ page, apiRequest }) => {
  const user = createUser({ email: 'test@example.com' });
  const product1 = createProduct({ name: 'Widget A', price: 10.0 });
  const product2 = createProduct({ name: 'Widget B', price: 15.0 });

  // Relacionamentos explícitos
  const order = createOrder({
    user,
    items: [
      createOrderItem({ product: product1, quantity: 2 }), // $20
      createOrderItem({ product: product2, quantity: 1 }), // $15
    ],
  });

  // Semeia via API
  await apiRequest({ method: 'POST', url: '/api/users', data: user });
  await apiRequest({ method: 'POST', url: '/api/products', data: product1 });
  await apiRequest({ method: 'POST', url: '/api/products', data: product2 });
  await apiRequest({ method: 'POST', url: '/api/orders', data: order });

  // Testa UI
  await page.goto(`/orders/${order.id}`);
  await expect(page.getByText('Widget A x 2')).toBeVisible();
  await expect(page.getByText('Widget B x 1')).toBeVisible();
  await expect(page.getByText('Total: $35.00')).toBeVisible();
});
```

**Pontos Chave**:

- Factories aninhadas lidam com relacionamentos (pedido → usuário, pedido → produtos)
- Overrides cascateiam: forneça usuário/produtos personalizados ou use padrões
- Campos calculados (total) derivados automaticamente de dados aninhados
- Relacionamentos explícitos tornam os dados de teste claros e sustentáveis

### Exemplo 3: Factory com Seed de API

**Contexto**: Quando testes precisam de setup de dados, sempre use chamadas de API ou tasks de banco de dados—nunca navegação de UI. Envolva uso de factory com utilitários de seed para setup de teste limpo.

**Implementação**:

```typescript
// playwright/support/helpers/seed-helpers.ts
import { APIRequestContext } from '@playwright/test';
import { User, createUser } from '../../test-utils/factories/user-factory';
import { Product, createProduct } from '../../test-utils/factories/product-factory';

export async function seedUser(request: APIRequestContext, overrides: Partial<User> = {}): Promise<User> {
  const user = createUser(overrides);

  const response = await request.post('/api/users', {
    data: user,
  });

  if (!response.ok()) {
    throw new Error(`Failed to seed user: ${response.status()}`);
  }

  return user;
}

export async function seedProduct(request: APIRequestContext, overrides: Partial<Product> = {}): Promise<Product> {
  const product = createProduct(overrides);

  const response = await request.post('/api/products', {
    data: product,
  });

  if (!response.ok()) {
    throw new Error(`Failed to seed product: ${response.status()}`);
  }

  return product;
}

// GlobalSetup do Playwright para dados compartilhados
// playwright/support/global-setup.ts
import { chromium, FullConfig } from '@playwright/test';
import { seedUser } from './helpers/seed-helpers';

async function globalSetup(config: FullConfig) {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const context = page.context();

  // Semeia usuário admin para todos os testes
  const admin = await seedUser(context.request, {
    email: 'admin@example.com',
    role: 'admin',
  });

  // Salva estado de auth para reutilização
  await context.storageState({ path: 'playwright/.auth/admin.json' });

  await browser.close();
}

export default globalSetup;

// Equivalente Cypress com cy.task
// cypress/support/tasks.ts
export const seedDatabase = async (entity: string, data: unknown) => {
  // Insert direto no banco ou chamada de API
  if (entity === 'users') {
    await db.users.create(data);
  }
  return null;
};

// Uso em testes Cypress:
beforeEach(() => {
  const user = createUser({ email: 'test@example.com' });
  cy.task('db:seed', { entity: 'users', data: user });
});
```

**Pontos Chave**:

- Seed via API é 10-50x mais rápido que setup baseado em UI
- `globalSetup` semeia dados compartilhados uma vez (ex: usuário admin)
- Seed por teste usa helpers `seedUser()` para isolamento
- `cy.task` do Cypress permite acesso direto ao banco de dados para velocidade

### Exemplo 4: Anti-Padrão - Dados de Teste Hardcoded

**Problema**:

```typescript
// ❌ RUIM: Dados de teste hardcoded
test('usuário pode logar', async ({ page }) => {
  await page.goto('/login');
  await page.fill('[data-testid="email"]', 'test@test.com'); // Hardcoded
  await page.fill('[data-testid="password"]', 'password123'); // Hardcoded
  await page.click('[data-testid="submit"]');

  // E se este usuário já existir? Teste falha em execuções paralelas.
  // E se o esquema adicionar campos obrigatórios? Teste quebra.
});

// ❌ RUIM: Fixtures JSON estáticas
// fixtures/users.json
{
  "users": [
    { "id": 1, "email": "user1@test.com", "name": "User 1" },
    { "id": 2, "email": "user2@test.com", "name": "User 2" }
  ]
}

test('admin pode deletar usuário', async ({ page }) => {
  const users = require('../fixtures/users.json');
  // Frágil: IDs colidem em paralelo, desvio de esquema quebra testes
});
```

**Por Que Falha**:

- **Colisões paralelas**: IDs hardcoded (`id: 1`, `email: 'test@test.com'`) causam falhas quando testes rodam concorrentemente
- **Desvio de esquema**: Adicionar campos obrigatórios (`phoneNumber`, `address`) quebra todos os testes usando fixtures
- **Intenção oculta**: Este teste precisa de `email: 'test@test.com'` especificamente, ou qualquer email?
- **Setup lento**: Criação de dados baseada em UI é 10-50x mais lenta que API

**Abordagem Melhor**: Use factories

```typescript
// ✅ BOM: Dados baseados em factory
test('usuário pode logar', async ({ page, apiRequest }) => {
  const user = createUser({ email: 'unique@example.com', password: 'secure123' });

  // Semeia via API (rápido, seguro em paralelo)
  await apiRequest({ method: 'POST', url: '/api/users', data: user });

  // Testa UI
  await page.goto('/login');
  await page.fill('[data-testid="email"]', user.email);
  await page.fill('[data-testid="password"]', user.password);
  await page.click('[data-testid="submit"]');

  await expect(page).toHaveURL('/dashboard');
});

// ✅ BOM: Factories se adaptam a mudanças de esquema automaticamente
// Quando `phoneNumber` se torna obrigatório, atualize a factory uma vez:
export const createUser = (overrides: Partial<User> = {}): User => ({
  id: faker.string.uuid(),
  email: faker.internet.email(),
  name: faker.person.fullName(),
  phoneNumber: faker.phone.number(), // NOVO campo, todos os testes recebem automaticamente
  role: 'user',
  ...overrides,
});
```

**Pontos Chave**:

- Factories geram dados únicos, seguros para paralelo
- Evolução de esquema tratada em um lugar (factory), não em cada teste
- Intenção do teste explícita via overrides
- Seed via API é rápido e confiável

### Exemplo 5: Composição de Factory

**Contexto**: Ao construir factories especializadas, componha factories mais simples em vez de duplicar lógica. Faça camadas de overrides para cenários de teste específicos.

**Implementação**:

```typescript
// test-utils/factories/user-factory.ts (base)
export const createUser = (overrides: Partial<User> = {}): User => ({
  id: faker.string.uuid(),
  email: faker.internet.email(),
  name: faker.person.fullName(),
  role: 'user',
  createdAt: new Date(),
  isActive: true,
  ...overrides,
});

// Compor factories especializadas
export const createAdminUser = (overrides: Partial<User> = {}): User => createUser({ role: 'admin', ...overrides });

export const createModeratorUser = (overrides: Partial<User> = {}): User => createUser({ role: 'moderator', ...overrides });

export const createInactiveUser = (overrides: Partial<User> = {}): User => createUser({ isActive: false, ...overrides });

// Factories de nível de conta com feature flags
type Account = {
  id: string;
  owner: User;
  plan: 'free' | 'pro' | 'enterprise';
  features: string[];
  maxUsers: number;
};

export const createAccount = (overrides: Partial<Account> = {}): Account => ({
  id: faker.string.uuid(),
  owner: overrides.owner || createUser(),
  plan: 'free',
  features: [],
  maxUsers: 1,
  ...overrides,
});

export const createProAccount = (overrides: Partial<Account> = {}): Account =>
  createAccount({
    plan: 'pro',
    features: ['advanced-analytics', 'priority-support'],
    maxUsers: 10,
    ...overrides,
  });

export const createEnterpriseAccount = (overrides: Partial<Account> = {}): Account =>
  createAccount({
    plan: 'enterprise',
    features: ['advanced-analytics', 'priority-support', 'sso', 'audit-logs'],
    maxUsers: 100,
    ...overrides,
  });

// Uso em testes:
test('contas pro podem acessar analytics', async ({ page, apiRequest }) => {
  const admin = createAdminUser({ email: 'admin@company.com' });
  const account = createProAccount({ owner: admin });

  await apiRequest({ method: 'POST', url: '/api/users', data: admin });
  await apiRequest({ method: 'POST', url: '/api/accounts', data: account });

  await page.goto('/analytics');
  await expect(page.getByText('Advanced Analytics')).toBeVisible();
});

test('contas free não podem acessar analytics', async ({ page, apiRequest }) => {
  const user = createUser({ email: 'user@company.com' });
  const account = createAccount({ owner: user }); // Padrão para plano free

  await apiRequest({ method: 'POST', url: '/api/users', data: user });
  await apiRequest({ method: 'POST', url: '/api/accounts', data: account });

  await page.goto('/analytics');
  await expect(page.getByText('Upgrade to Pro')).toBeVisible();
});
```

**Pontos Chave**:

- Componha factories especializadas a partir de factories base (`createAdminUser` → `createUser`)
- Padrões cascateiam: `createProAccount` define plano + features automaticamente
- Ainda permite overrides: `createProAccount({ maxUsers: 50 })` funciona
- Intenção do teste clara: `createProAccount()` vs `createAccount({ plan: 'pro', features: [...] })`

## Pontos de Integração

- **Usado em workflows**: `*atdd` (geração de teste), `*automate` (expansão de teste), `*framework` (setup de factory)
- **Fragmentos relacionados**:
  - `fixture-architecture.md` - Funções puras e fixtures para integração de factory
  - `network-first.md` - Padrões de setup API-first
  - `test-quality.md` - Design de teste determinístico e seguro para paralelo

## Estratégia de Limpeza

Garanta que factories funcionem com padrões de limpeza:

```typescript
// Rastreia IDs criados para limpeza
const createdUsers: string[] = [];

afterEach(async ({ apiRequest }) => {
  // Limpa todos os usuários criados durante o teste
  for (const userId of createdUsers) {
    await apiRequest({ method: 'DELETE', url: `/api/users/${userId}` });
  }
  createdUsers.length = 0;
});

test('fluxo de registro de usuário', async ({ page, apiRequest }) => {
  const user = createUser();
  createdUsers.push(user.id);

  await apiRequest({ method: 'POST', url: '/api/users', data: user });
  // ... lógica de teste
});
```

## Integração com Feature Flag

Ao trabalhar com feature flags, inclua-as nas factories:

```typescript
export const createUserWithFlags = (
  overrides: Partial<User> = {},
  flags: Record<string, boolean> = {},
): User & { flags: Record<string, boolean> } => ({
  ...createUser(overrides),
  flags: {
    'new-dashboard': false,
    'beta-features': false,
    ...flags,
  },
});

// Uso:
const user = createUserWithFlags(
  { email: 'test@example.com' },
  {
    'new-dashboard': true,
    'beta-features': true,
  },
);
```

_Fonte: Filosofia de Teste Murat (linhas 94-120), padrões de teste API-first, documentação faker.js._
