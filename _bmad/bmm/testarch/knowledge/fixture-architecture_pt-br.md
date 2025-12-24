# Playbook de Arquitetura de Fixture

## Princípio

Construa helpers de teste como funções puras primeiro, depois envolva-os em fixtures específicas do framework. Componha capacidades usando `mergeTests` (Playwright) ou comandos em camadas (Cypress) em vez de herança. Cada fixture deve resolver uma preocupação isolada (auth, API, logs, rede).

## Motivação

Page Object Models tradicionais criam acoplamento forte através de cadeias de herança (`BasePage → LoginPage → AdminPage`). Quando classes base mudam, todos os descendentes quebram. Funções puras com wrappers de fixture fornecem:

- **Testabilidade**: Funções puras rodam em testes unitários sem overhead de framework
- **Composabilidade**: Misture capacidades livremente via `mergeTests`, sem restrições de herança
- **Reutilização**: Exporte fixtures via subcaminhos de pacote para compartilhamento entre projetos
- **Manutenibilidade**: Uma preocupação por fixture = limites de responsabilidade claros

## Exemplos de Padrões

### Exemplo 1: Padrão Função Pura → Fixture

**Contexto**: Ao construir qualquer helper de teste, sempre comece com uma função pura que aceita todas as dependências explicitamente. Então envolva-a em uma fixture Playwright ou comando Cypress.

**Implementação**:

```typescript
// playwright/support/helpers/api-request.ts
// Passo 1: Função pura (SEMPRE PRIMEIRO!)
type ApiRequestParams = {
  request: APIRequestContext;
  method: 'GET' | 'POST' | 'PUT' | 'DELETE';
  url: string;
  data?: unknown;
  headers?: Record<string, string>;
};

export async function apiRequest({
  request,
  method,
  url,
  data,
  headers = {}
}: ApiRequestParams) {
  const response = await request.fetch(url, {
    method,
    data,
    headers: {
      'Content-Type': 'application/json',
      ...headers
    }
  });

  if (!response.ok()) {
    throw new Error(`API request failed: ${response.status()} ${await response.text()}`);
  }

  return response.json();
}

// Passo 2: Wrapper de Fixture
// playwright/support/fixtures/api-request-fixture.ts
import { test as base } from '@playwright/test';
import { apiRequest } from '../helpers/api-request';

export const test = base.extend<{ apiRequest: typeof apiRequest }>({
  apiRequest: async ({ request }, use) => {
    // Injetar dependência de framework, expor função pura
    await use((params) => apiRequest({ request, ...params }));
  }
});

// Passo 3: Exportações de pacote para reutilização
// package.json
{
  "exports": {
    "./api-request": "./playwright/support/helpers/api-request.ts",
    "./api-request/fixtures": "./playwright/support/fixtures/api-request-fixture.ts"
  }
}
```

**Pontos Chave**:

- Função pura é testável unitariamente sem rodar Playwright
- Dependência de framework (`request`) injetada na fronteira da fixture
- Fixture expõe a função pura para o contexto de teste
- Exportações de subcaminho de pacote permitem `import { apiRequest } from 'my-fixtures/api-request'`

### Exemplo 2: Sistema de Fixture Componível com mergeTests

**Contexto**: Ao construir capacidades de teste abrangentes, componha múltiplas fixtures focadas em vez de criar classes helper monolíticas. Cada fixture fornece uma capacidade.

**Implementação**:

```typescript
// playwright/support/fixtures/merged-fixtures.ts
import { test as base, mergeTests } from '@playwright/test';
import { test as apiRequestFixture } from './api-request-fixture';
import { test as networkFixture } from './network-fixture';
import { test as authFixture } from './auth-fixture';
import { test as logFixture } from './log-fixture';

// Compor todas as fixtures para capacidades abrangentes
export const test = mergeTests(base, apiRequestFixture, networkFixture, authFixture, logFixture);

export { expect } from '@playwright/test';

// Exemplo de uso em testes:
// import { test, expect } from './support/fixtures/merged-fixtures';
//
// test('usuário pode criar pedido', async ({ page, apiRequest, auth, network }) => {
//   await auth.loginAs('customer@example.com');
//   await network.interceptRoute('POST', '**/api/orders', { id: 123 });
//   await page.goto('/checkout');
//   await page.click('[data-testid="submit-order"]');
//   await expect(page.getByText('Order #123')).toBeVisible();
// });
```

**Exemplos de Fixture Individual**:

```typescript
// network-fixture.ts
export const test = base.extend({
  network: async ({ page }, use) => {
    const interceptedRoutes = new Map();

    const interceptRoute = async (method: string, url: string, response: unknown) => {
      await page.route(url, (route) => {
        if (route.request().method() === method) {
          route.fulfill({ body: JSON.stringify(response) });
        }
      });
      interceptedRoutes.set(`${method}:${url}`, response);
    };

    await use({ interceptRoute });

    // Limpeza
    interceptedRoutes.clear();
  },
});

// auth-fixture.ts
export const test = base.extend({
  auth: async ({ page, context }, use) => {
    const loginAs = async (email: string) => {
      // Usar API para configurar auth (rápido!)
      const token = await getAuthToken(email);
      await context.addCookies([
        {
          name: 'auth_token',
          value: token,
          domain: 'localhost',
          path: '/',
        },
      ]);
    };

    await use({ loginAs });
  },
});
```

**Pontos Chave**:

- `mergeTests` combina fixtures sem herança
- Cada fixture tem responsabilidade única (rede, auth, logs)
- Testes importam fixture fundida e acessam todas as capacidades
- Sem acoplamento entre fixtures—adicione/remova livremente

### Exemplo 3: Helper HTTP Agnóstico a Framework

**Contexto**: Ao construir helpers HTTP, mantenha-os agnósticos a framework. Aceite todos os params explicitamente para que funcionem em testes unitários, Playwright, Cypress ou qualquer contexto.

**Implementação**:

```typescript
// shared/helpers/http-helper.ts
// Função pura, agnóstica a framework
type HttpHelperParams = {
  baseUrl: string;
  endpoint: string;
  method: 'GET' | 'POST' | 'PUT' | 'DELETE';
  body?: unknown;
  headers?: Record<string, string>;
  token?: string;
};

export async function makeHttpRequest({ baseUrl, endpoint, method, body, headers = {}, token }: HttpHelperParams): Promise<unknown> {
  const url = `${baseUrl}${endpoint}`;
  const requestHeaders = {
    'Content-Type': 'application/json',
    ...(token && { Authorization: `Bearer ${token}` }),
    ...headers,
  };

  const response = await fetch(url, {
    method,
    headers: requestHeaders,
    body: body ? JSON.stringify(body) : undefined,
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`HTTP ${method} ${url} falhou: ${response.status} ${errorText}`);
  }

  return response.json();
}

// Wrapper de fixture Playwright
// playwright/support/fixtures/http-fixture.ts
import { test as base } from '@playwright/test';
import { makeHttpRequest } from '../../shared/helpers/http-helper';

export const test = base.extend({
  httpHelper: async ({}, use) => {
    const baseUrl = process.env.API_BASE_URL || 'http://localhost:3000';

    await use((params) => makeHttpRequest({ baseUrl, ...params }));
  },
});

// Wrapper de comando Cypress
// cypress/support/commands.ts
import { makeHttpRequest } from '../../shared/helpers/http-helper';

Cypress.Commands.add('apiRequest', (params) => {
  const baseUrl = Cypress.env('API_BASE_URL') || 'http://localhost:3000';
  return cy.wrap(makeHttpRequest({ baseUrl, ...params }));
});
```

**Pontos Chave**:

- Função pura usa apenas `fetch` padrão, sem dependências de framework
- Testes unitários chamam `makeHttpRequest` diretamente com todos os params
- Wrappers Playwright e Cypress injetam config específica do framework
- Mesma lógica roda em todo lugar—zero duplicação

### Exemplo 4: Padrão de Limpeza de Fixture

**Contexto**: Quando fixtures criam recursos (dados, arquivos, conexões), garanta limpeza automática no teardown da fixture. Testes não devem vazar estado.

**Implementação**:

```typescript
// playwright/support/fixtures/database-fixture.ts
import { test as base } from '@playwright/test';
import { seedDatabase, deleteRecord } from '../helpers/db-helpers';

type DatabaseFixture = {
  seedUser: (userData: Partial<User>) => Promise<User>;
  seedOrder: (orderData: Partial<Order>) => Promise<Order>;
};

export const test = base.extend<DatabaseFixture>({
  seedUser: async ({}, use) => {
    const createdUsers: string[] = [];

    const seedUser = async (userData: Partial<User>) => {
      const user = await seedDatabase('users', userData);
      createdUsers.push(user.id);
      return user;
    };

    await use(seedUser);

    // Auto-limpeza: Deletar todos usuários criados durante teste
    for (const userId of createdUsers) {
      await deleteRecord('users', userId);
    }
    createdUsers.length = 0;
  },

  seedOrder: async ({}, use) => {
    const createdOrders: string[] = [];

    const seedOrder = async (orderData: Partial<Order>) => {
      const order = await seedDatabase('orders', orderData);
      createdOrders.push(order.id);
      return order;
    };

    await use(seedOrder);

    // Auto-limpeza: Deletar todos pedidos
    for (const orderId of createdOrders) {
      await deleteRecord('orders', orderId);
    }
    createdOrders.length = 0;
  },
});

// Exemplo de uso:
// test('usuário pode fazer pedido', async ({ seedUser, seedOrder, page }) => {
//   const user = await seedUser({ email: 'test@example.com' });
//   const order = await seedOrder({ userId: user.id, total: 100 });
//
//   await page.goto(`/orders/${order.id}`);
//   await expect(page.getByText('Order Total: $100')).toBeVisible();
//
//   // Nenhuma limpeza manual necessária—fixture cuida disso automaticamente
// });
```

**Pontos Chave**:

- Rastrear todos recursos criados em array durante execução do teste
- Teardown (após `use()`) deleta todos recursos rastreados
- Testes não limpam manualmente—acontece automaticamente
- Previne poluição de teste e instabilidade de estado compartilhado

### Anti-Padrão: Page Objects Baseados em Herança

**Problema**:

```typescript
// ❌ RUIM: Page Object Model com herança
class BasePage {
  constructor(public page: Page) {}

  async navigate(url: string) {
    await this.page.goto(url);
  }

  async clickButton(selector: string) {
    await this.page.click(selector);
  }
}

class LoginPage extends BasePage {
  async login(email: string, password: string) {
    await this.navigate('/login');
    await this.page.fill('#email', email);
    await this.page.fill('#password', password);
    await this.clickButton('#submit');
  }
}

class AdminPage extends LoginPage {
  async accessAdminPanel() {
    await this.login('admin@example.com', 'admin123');
    await this.navigate('/admin');
  }
}
```

**Por Que Falha**:

- Mudanças em `BasePage` quebram todos os descendentes (`LoginPage`, `AdminPage`)
- `AdminPage` herda detalhes de `login` desnecessários—acoplamento forte
- Não pode compor capacidades (ex: admin + recursos de relatório requerem herança múltipla)
- Difícil testar métodos de `BasePage` isoladamente
- Estado oculto em instâncias de classe leva a comportamento imprevisível

**Abordagem Melhor**: Use funções puras + fixtures

```typescript
// ✅ BOM: Funções puras com composição de fixture
// helpers/navigation.ts
export async function navigate(page: Page, url: string) {
  await page.goto(url);
}

// helpers/auth.ts
export async function login(page: Page, email: string, password: string) {
  await page.fill('[data-testid="email"]', email);
  await page.fill('[data-testid="password"]', password);
  await page.click('[data-testid="submit"]');
}

// fixtures/admin-fixture.ts
export const test = base.extend({
  adminPage: async ({ page }, use) => {
    await login(page, 'admin@example.com', 'admin123');
    await navigate(page, '/admin');
    await use(page);
  },
});

// Testes importam exatamente o que precisam—sem herança
```

## Pontos de Integração

- **Usado em workflows**: `*atdd` (geração de teste), `*automate` (expansão de teste), `*framework` (setup inicial)
- **Fragmentos relacionados**:
  - `data-factories.md` - Funções factory para dados de teste
  - `network-first.md` - Padrões de interceptação de rede
  - `test-quality.md` - Princípios de design de teste determinístico

## Diretrizes de Reutilização de Função Helper

Ao decidir se deve criar uma fixture, siga estas regras:

- **3+ usos** → Crie fixture com exportação de subcaminho (compartilhado entre testes/projetos)
- **2-3 usos** → Crie módulo utilitário (compartilhado dentro do projeto)
- **1 uso** → Mantenha inline (evite abstração prematura)
- **Lógica complexa** → Padrão de função factory (geração de dados dinâmica)

_Fonte: Filosofia de Teste Murat (linhas 74-122), padrões de produção SEON, documentação de fixture Playwright._
