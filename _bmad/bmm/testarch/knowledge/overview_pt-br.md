# Visão Geral do Playwright Utils

## Princípio

Use utilitários baseados em fixtures e prontos para produção do `@seontechnologies/playwright-utils` para padrões comuns de teste Playwright. Construa helpers de teste como funções puras primeiro, depois envolva em fixtures específicas de framework para composabilidade e reuso.

## Motivação

Escrever utilitários Playwright do zero para cada projeto leva a:

- Código duplicado em suítes de teste
- Padrões e qualidade inconsistentes
- Carga de manutenção quando APIs Playwright mudam
- Funcionalidades avançadas faltando (validação de esquema, gravação HAR, persistência de auth)

`@seontechnologies/playwright-utils` fornece:

- **Utilitários testados em produção**: Usados na SEON Technologies em produção
- **Design funcional primeiro**: Lógica principal como funções puras, fixtures por conveniência
- **Fixtures componíveis**: Use `mergeTests` para combinar utilitários
- **Suporte TypeScript**: Segurança de tipo total com tipos genéricos
- **Cobertura abrangente**: Requisições de API, auth, rede, logging, manipulação de arquivo, burn-in

## Instalação

```bash
npm install -D @seontechnologies/playwright-utils
```

**Dependências de Pares:**

- `@playwright/test` >= 1.54.1 (necessário)
- `ajv` >= 8.0.0 (opcional - para validação de JSON Schema)
- `zod` >= 3.0.0 (opcional - para validação de esquema Zod)

## Utilitários Disponíveis

### Utilitários de Teste Core

| Utilitário                 | Propósito                                  | Contexto de Teste |
| -------------------------- | ------------------------------------------ | ----------------- |
| **api-request**            | Cliente HTTP tipado com validação de esquema | Testes de API     |
| **network-recorder**       | Gravação/reprodução HAR para teste offline | Testes de UI      |
| **auth-session**           | Persistência de token, auth multi-usuário  | UI & API          |
| **recurse**                | Polling estilo Cypress para condições async| UI & API          |
| **intercept-network-call** | Spy/stub de rede com parsing JSON auto     | Testes de UI      |
| **log**                    | Logging integrado ao relatório Playwright  | UI & API          |
| **file-utils**             | Leitura/validação de CSV/XLSX/PDF/ZIP      | UI & API          |
| **burn-in**                | Seleção de teste inteligente com git diff  | CI/CD             |
| **network-error-monitor**  | Detecção automática de HTTP 4xx/5xx        | Testes de UI      |

## Padrões de Design

### Padrão 1: Core Funcional, Shell de Fixture

**Contexto**: Todos os utilitários seguem o mesmo padrão arquitetural - função pura como core, fixture como wrapper.

**Implementação**:

```typescript
// Importação direta (passar contexto Playwright explicitamente)
import { apiRequest } from '@seontechnologies/playwright-utils';

test('uso direto', async ({ request }) => {
  const { status, body } = await apiRequest({
    request, // Deve passar contexto de request
    method: 'GET',
    path: '/api/users',
  });
});

// Importação de fixture (contexto injetado automaticamente)
import { test } from '@seontechnologies/playwright-utils/fixtures';

test('uso de fixture', async ({ apiRequest }) => {
  const { status, body } = await apiRequest({
    // Sem necessidade de passar contexto de request
    method: 'GET',
    path: '/api/users',
  });
});
```

**Pontos Chave**:

- Funções puras testáveis sem rodar Playwright
- Fixtures injetam dependências de framework automaticamente
- Escolha importação direta (mais controle) ou fixture (conveniência)

### Padrão 2: Importações de Subcaminho para Tree-Shaking

**Contexto**: Importe apenas o que você precisa para manter tamanhos de bundle pequenos.

**Implementação**:

```typescript
// Importar utilitário específico
import { apiRequest } from '@seontechnologies/playwright-utils/api-request';

// Importar fixture específica
import { test } from '@seontechnologies/playwright-utils/api-request/fixtures';

// Importar tudo (use com moderação)
import { apiRequest, recurse, log } from '@seontechnologies/playwright-utils';
```

**Pontos Chave**:

- Importações de subcaminho permitem tree-shaking
- Mantenha tamanhos de bundle mínimos
- Importe de caminhos específicos para builds de produção

### Padrão 3: Composição de Fixture com mergeTests

**Contexto**: Combine múltiplas fixtures playwright-utils com suas próprias fixtures customizadas.

**Implementação**:

```typescript
// playwright/support/merged-fixtures.ts
import { mergeTests } from '@playwright/test';
import { test as apiRequestFixture } from '@seontechnologies/playwright-utils/api-request/fixtures';
import { test as authFixture } from '@seontechnologies/playwright-utils/auth-session/fixtures';
import { test as recurseFixture } from '@seontechnologies/playwright-utils/recurse/fixtures';
import { test as logFixture } from '@seontechnologies/playwright-utils/log/fixtures';

// Fundir todas fixtures em um objeto de teste
export const test = mergeTests(apiRequestFixture, authFixture, recurseFixture, logFixture);

export { expect } from '@playwright/test';
```

```typescript
// Em seus testes
import { test, expect } from '../support/merged-fixtures';

test('todos utilitários disponíveis', async ({ apiRequest, authToken, recurse, log }) => {
  await log.step('Fazendo requisição API autenticada');

  const { body } = await apiRequest({
    method: 'GET',
    path: '/api/protected',
    headers: { Authorization: `Bearer ${authToken}` },
  });

  await recurse(
    () => apiRequest({ method: 'GET', path: `/status/${body.id}` }),
    (res) => res.body.ready === true,
  );
});
```

**Pontos Chave**:

- `mergeTests` combina múltiplas fixtures sem conflitos
- Crie um arquivo merged-fixtures.ts por projeto
- Importe objeto de teste de suas fixtures fundidas em todos os testes
- Todos utilitários disponíveis em assinatura de teste única

## Integração com Testes Existentes

### Estratégia de Adoção Gradual

**1. Comece com logging** (zero mudanças quebrando):

```typescript
import { log } from '@seontechnologies/playwright-utils';

test('teste existente', async ({ page }) => {
  await log.step('Navegar para página'); // Apenas adicione logging
  await page.goto('/dashboard');
  // Resto do teste inalterado
});
```

**2. Adicione utilitários API** (para testes de API):

```typescript
import { test } from '@seontechnologies/playwright-utils/api-request/fixtures';

test('teste API', async ({ apiRequest }) => {
  const { status, body } = await apiRequest({
    method: 'GET',
    path: '/api/users',
  });

  expect(status).toBe(200);
});
```

**3. Expanda para utilitários de rede** (para testes de UI):

```typescript
import { test } from '@seontechnologies/playwright-utils/fixtures';

test('UI com controle de rede', async ({ page, interceptNetworkCall }) => {
  const usersCall = interceptNetworkCall({
    url: '**/api/users',
  });

  await page.goto('/dashboard');
  const { responseJson } = await usersCall;

  expect(responseJson).toHaveLength(10);
});
```

**4. Integração completa** (fixtures fundidas):

Crie merged-fixtures.ts e use em todos os testes.

## Fragmentos Relacionados

- `api-request.md` - Cliente HTTP com validação de esquema
- `network-recorder.md` - Teste offline baseado em HAR
- `auth-session.md` - Gerenciamento de token
- `intercept-network-call.md` - Interceptação de rede
- `recurse.md` - Padrões de polling
- `log.md` - Utilitário de logging
- `file-utils.md` - Operações de arquivo
- `fixtures-composition.md` - Padrões avançados de mergeTests

## Anti-Padrões

**❌ Não misture importações diretas e de fixture no mesmo teste:**

```typescript
import { apiRequest } from '@seontechnologies/playwright-utils';
import { test } from '@seontechnologies/playwright-utils/auth-session/fixtures';

test('ruim', async ({ request, authToken }) => {
  // Confuso - misturando direto (precisa de request) e fixture (tem authToken)
  await apiRequest({ request, method: 'GET', path: '/api/users' });
});
```

**✅ Use estilo de importação consistente:**

```typescript
import { test } from '../support/merged-fixtures';

test('bom', async ({ apiRequest, authToken }) => {
  // Limpo - tudo de fixtures
  await apiRequest({ method: 'GET', path: '/api/users' });
});
```

**❌ Não importe tudo quando precisa de um utilitário:**

```typescript
import * as utils from '@seontechnologies/playwright-utils'; // Bundle grande
```

**✅ Use importações de subcaminho:**

```typescript
import { apiRequest } from '@seontechnologies/playwright-utils/api-request'; // Bundle pequeno
```

## Implementação de Referência

O repositório oficial `@seontechnologies/playwright-utils` fornece exemplos funcionais de todos os padrões descritos nestes fragmentos.

**Repositório:** <https://github.com/seontechnologies/playwright-utils>

**Recursos chave:**

- **Exemplos de teste:** `playwright/tests` - Todos os utilitários em ação
- **Setup de framework:** `playwright.config.ts`, `playwright/support/merged-fixtures.ts`
- **Padrões CI:** `.github/workflows/` - GitHub Actions com sharding, paralelização

**Início rápido:**

```bash
git clone https://github.com/seontechnologies/playwright-utils.git
cd playwright-utils
nvm use
npm install
npm run test:pw-ui  # Explorar testes com Playwright UI
npm run test:pw
```

Todos os padrões em fragmentos TEA são testados em produção neste repositório.
