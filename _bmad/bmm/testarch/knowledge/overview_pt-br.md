# Playwright utiliza visão geral

## Princípio

Use utilitários prontos para a produção e baseados em acessórios da `@seontechnologies/playwright-utils` para testes padrões comuns de Playwright. Crie ajudantes de teste como funções puras primeiro, em seguida, enrole em dispositivos específicos para compor e reutilizar.

## Racional

Escrever utilitários Playwright do zero para cada projeto leva a:

- Código duplicado em suites de teste
- Padrões inconsistentes e qualidade
- Carga de manutenção quando as APIs de Playwright mudam
- Recursos avançados em falta (validação de esquema, gravação HAR, persistência de autenticação)

`@seontechnologies/playwright-utils` fornece:

- **Utilidades de produção testadas**: Usado na SEON Technologies na produção
- **Design funcional-primeiro**: Lógica central como funções puras, dispositivos para conveniência
- **Composable fixtures**: Use `mergeTests` para combinar utilitários
- **TypeScript support**: Segurança completa do tipo com tipos genéricos
- **Cobertura compreensiva**: pedidos de API, autenticação, rede, registo, tratamento de ficheiros, gravação

## Instalação

```bash
npm install -D @seontechnologies/playwright-utils

```

**Dependências dos pares:**

- `@playwright/test` >= 1,54.1 (requerido)
- `ajv` >= 8.0.0 (opcional - para validação do esquema JSON)
- `zod` >= 3.0.0 (opcional - para validação do esquema Zod)

## Utilitários Disponíveis

### Utilitários de Teste Principais

| Utility                    | Purpose                                    | Test Context  |
| -------------------------- | ------------------------------------------ | ------------- |
| **api-request**            | Typed HTTP client with schema validation   | API tests     |
| **network-recorder**       | HAR record/playback for offline testing    | UI tests      |
| **auth-session**           | Token persistence, multi-user auth         | Both UI & API |
| **recurse**                | Cypress-style polling for async conditions | Both UI & API |
| **intercept-network-call** | Network spy/stub with auto JSON parsing    | UI tests      |
| **log**                    | Playwright report-integrated logging       | Both UI & API |
| **file-utils**             | CSV/XLSX/PDF/ZIP reading & validation      | Both UI & API |
| **burn-in**                | Smart test selection with git diff         | CI/CD         |
| **network-error-monitor**  | Automatic HTTP 4xx/5xx detection           | UI tests      |

## Padrões de desenho

### Padrão 1: Núcleo funcional, Concha de fixação

**Contexto**: Todos os utilitários seguem o mesmo padrão arquitetônico - function puro como núcleo, estrutura como invólucro.

**Implementation**:

```typescript
// Direct import (pass Playwright context explicitly)
import { apiRequest } from '@seontechnologies/playwright-utils';

test('direct usage', async ({ request }) => {
  const { status, body } = await apiRequest({
    request, // Must pass request context
    method: 'GET',
    path: '/api/users',
  });
});

// Fixture import (context injected automatically)
import { test } from '@seontechnologies/playwright-utils/fixtures';

test('fixture usage', async ({ apiRequest }) => {
  const { status, body } = await apiRequest({
    // No need to pass request context
    method: 'GET',
    path: '/api/users',
  });
});

```

**Pontos-chave**

- Funções puras testáveis sem execução do Playwright
- Fixtures injetar dependências framework automaticamente
- Escolha import direto (mais controle) ou instalação (conveniência)

### Padrão 2: Importações de Subcaminho para Tree-Shaking

**Contexto**: Importar apenas o que você precisa para manter tamanhos de pacotes pequenos.

**Implementation**:

```typescript
// Import specific utility
import { apiRequest } from '@seontechnologies/playwright-utils/api-request';

// Import specific fixture
import { test } from '@seontechnologies/playwright-utils/api-request/fixtures';

// Import everything (use sparingly)
import { apiRequest, recurse, log } from '@seontechnologies/playwright-utils';

```

**Pontos-chave**

- Importações de sub-caminho permitem agitar as árvores
- Mantenha tamanhos mínimos de pacotes
- Importação de caminhos específicos para construções de produção

### Padrão 3: Composição de fixação com mesclagemTestes

**Contexto**: Combine vários jogos de playwright-utils com seus próprios acessórios personalizados.

**Implementation**:

```typescript
// playwright/support/merged-fixtures.ts
import { mergeTests } from '@playwright/test';
import { test as apiRequestFixture } from '@seontechnologies/playwright-utils/api-request/fixtures';
import { test as authFixture } from '@seontechnologies/playwright-utils/auth-session/fixtures';
import { test as recurseFixture } from '@seontechnologies/playwright-utils/recurse/fixtures';
import { test as logFixture } from '@seontechnologies/playwright-utils/log/fixtures';

// Merge all fixtures into one test object
export const test = mergeTests(apiRequestFixture, authFixture, recurseFixture, logFixture);

export { expect } from '@playwright/test';

```

«``typescript
// Nos seus testes
BMADPROTECT015end BMADPROTECT020end de '../suporte/fixações incorporadas';

teste('todos os utilitários disponíveis', async ({ apiRequest, authToken, recurse, log }) => {
await log.step('Making au