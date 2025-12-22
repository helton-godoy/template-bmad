# Manual de Arquitetura de Fixture

## Princípio

Crie ajudantes de teste como funções puras primeiro, em seguida, embrulhe-os em dispositivos específicos do framework. Compor capacidades usando `mergeTests` (Playwright) ou comandos em camadas (Cypress) em vez de herança. Cada dispositivo deve resolver uma preocupação isolada (auth, API, logs, rede).

## Racional

Modelos tradicionais de objetos de página criam acoplamento apertado através de cadeias de herança (`BasePage → LoginPage → AdminPage`). Quando as classes básicas mudam, todos os descendentes quebram. Funções puras com invólucros de fixação fornecem:

- **Testabilidade**: Funções puras executadas em testes unitários sem sobrecarga do quadro
- **Composability**: Misture as capacidades livremente via `mergeTests`, sem restrições de herança
- **Reusabilidade**: instalações de exportação via subcaminhos package para partilha de projectos cruzados
- **Manutenção**: uma preocupação por dispositivo = limites de responsabilidade claros

## Exemplos de padrões

### Exemplo 1: Função pura → Padrão de fixação

**Contexto**: Ao construir qualquer auxiliar de teste, comece sempre com um function puro que aceita todas as dependências explicitamente. Em seguida, embrulhe-o em um dispositivo Playwright ou comando Cypress.

**Implementation**:

```typescript
// playwright/support/helpers/api-request.ts
// Step 1: Pure function (ALWAYS FIRST!)
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

// Step 2: Fixture wrapper
// playwright/support/fixtures/api-request-fixture.ts
import { test as base } from '@playwright/test';
import { apiRequest } from '../helpers/api-request';

export const test = base.extend<{ apiRequest: typeof apiRequest }>({
  apiRequest: async ({ request }, use) => {
    // Inject framework dependency, expose pure function
    await use((params) => apiRequest({ request, ...params }));
  }
});

// Step 3: Package exports for reusability
// package.json
{
  "exports": {
    "./api-request": "./playwright/support/helpers/api-request.ts",
    "./api-request/fixtures": "./playwright/support/fixtures/api-request-fixture.ts"
  }
}

```

**Pontos-chave**

- Puro function é de teste unitário sem execução do dramaturgo
- Dependência do quadro (`request`) injectada no limite do dispositivo
- Fixture expõe o function puro ao contexto de teste
- Exportações do subcaminho do pacote permitem `import { apiRequest } from 'my-fixtures/api-request'`

### Exemplo 2: Sistema de fixação composível com testes de mesclagem

**Contexto**: Ao construir capacidades de teste abrangentes, componha vários dispositivos focados em vez de criar classes de ajuda monolíticas. Cada dispositivo fornece uma capacidade.

**Implementation**:

```typescript
// playwright/support/fixtures/merged-fixtures.ts
import { test as base, mergeTests } from '@playwright/test';
import { test as apiRequestFixture } from './api-request-fixture';
import { test as networkFixture } from './network-fixture';
import { test as authFixture } from './auth-fixture';
import { test as logFixture } from './log-fixture';

// Compose all fixtures for comprehensive capabilities
export const test = mergeTests(base, apiRequestFixture, networkFixture, authFixture, logFixture);

export { expect } from '@playwright/test';

// Example usage in tests:
// import { test, expect } from './support/fixtures/merged-fixtures';
//
// test('user can create order', async ({ page, apiRequest, auth, network }) => {
//   await auth.loginAs('customer@example.com');
//   await network.interceptRoute('POST', '**/api/orders', { id: 123 });
//   await page.goto('/checkout');
//   await page.click('[data-testid="submit-order"]');
//   await expect(page.getByText('Order #123')).toBeVisible();
// });

```

**Exemplos individuais de fixação**:

«``typescript
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
interceptedRutes.set(`${method}:${url}`, resposta);
};

BMADPROTECT020End use({ interceptRoute });

// Limpeza
InterceptadoRutes.clear();
},
});

// auth-fixture.ts
BMADPROTECT019end const test = base.extend({
  auth: async ({ page, context }, utilização) = > {
const loginAs = async (email: string) => {
// Use API para configurar a autenticação (rápido!)
BMADPROTECT014End token = BMADPROTECT013End getAuthToken( email);
BMADPROTECT012End context.addCookies([
{
          name: 'auth_token',
          value: token,
