# Composição de fixação com mesclagemTestes

## Princípio

Combine vários acessórios Playwright usando `mergeTests` para criar um objeto de teste unificado com todas as capacidades. Construir infraestrutura de teste composable fundindo jogos de playwright-utils com jogos de projeto personalizados.

## Racional

Usar dispositivos de várias fontes requer combiná-los:

- Importar de vários arquivos de fixação é verbose
- Conflitos de nomes entre jogos
- Definições de acessórios duplicados
- Nenhum objeto de teste simples claro

O `mergeTests` do dramaturgo fornece:

- **Single objecto de ensaio**: Todos os dispositivos num import
- * Resolução *Conflict**: Lida com colisões de nomes automaticamente
- **Composition padrão**: Mix utilitários, acessórios personalizados, acessórios de terceiros
- **Type safety**: Suporte completo do TipoScript para acessórios fundidos
- **Maintainability**: Um lugar para gerenciar todos os acessórios

## Exemplos de padrões

### Exemplo 1: Junção básica de fixação

**Context**: Combine vários acessórios de playwright-utils em um único objeto de teste.

**Implementation**:

```typescript
// playwright/support/merged-fixtures.ts
import { mergeTests } from '@playwright/test';
import { test as apiRequestFixture } from '@seontechnologies/playwright-utils/api-request/fixtures';
import { test as authFixture } from '@seontechnologies/playwright-utils/auth-session/fixtures';
import { test as recurseFixture } from '@seontechnologies/playwright-utils/recurse/fixtures';

// Merge all fixtures
export const test = mergeTests(apiRequestFixture, authFixture, recurseFixture);

export { expect } from '@playwright/test';

```

```typescript
// In your tests - import from merged fixtures
import { test, expect } from '../support/merged-fixtures';

test('all utilities available', async ({
  apiRequest, // From api-request fixture
  authToken, // From auth fixture
  recurse, // From recurse fixture
}) => {
  // All fixtures available in single test signature
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

**Key Pontos**:

- Criar um `merged-fixtures.ts` por projeto
- Importar objeto de teste de acessórios fundidos em todos os arquivos de teste
- Todos os utilitários disponíveis sem múltiplas importações
- Acesso seguro de tipo a todos os dispositivos

### Exemplo 2: Combinando com fixações personalizadas

**Context**: Adicione dispositivos específicos do projeto ao lado de dramaturgos-utils.

**Implementation**:

```typescript
// playwright/support/custom-fixtures.ts - Your project fixtures
import { test as base } from '@playwright/test';
import { createUser } from './factories/user-factory';
import { seedDatabase } from './helpers/db-seeder';

export const test = base.extend({
  // Custom fixture 1: Auto-seeded user
  testUser: async ({ request }, use) => {
    const user = await createUser({ role: 'admin' });
    await seedDatabase('users', [user]);
    await use(user);
    // Cleanup happens automatically
  },

  // Custom fixture 2: Database helpers
  db: async ({}, use) => {
    await use({
      seed: seedDatabase,
      clear: () => seedDatabase.truncate(),
    });
  },
});

// playwright/support/merged-fixtures.ts - Combine everything
import { mergeTests } from '@playwright/test';
import { test as apiRequestFixture } from '@seontechnologies/playwright-utils/api-request/fixtures';
import { test as authFixture } from '@seontechnologies/playwright-utils/auth-session/fixtures';
import { test as customFixtures } from './custom-fixtures';

export const test = mergeTests(
  apiRequestFixture,
  authFixture,
  customFixtures, // Your project fixtures
);

export { expect } from '@playwright/test';

```

```typescript
// In tests - all fixtures available
import { test, expect } from '../support/merged-fixtures';

test('using mixed fixtures', async ({
  apiRequest, // playwright-utils
  authToken, // playwright-utils
  testUser, // custom
  db, // custom
}) => {
  // Use playwright-utils
  const { body } = await apiRequest({
    method: 'GET',
    path: `/api/users/${testUser.id}`,
    headers: { Authorization: `Bearer ${authToken}` },
  });

  // Use custom fixture
  await db.clear();
});

```

**Key Pontos**:

- Os acessórios personalizados estendem o teste `base`
- Mesclar customizado com jogos de dramaturgo-utils
- Tudo disponível em uma assinatura de teste
- Separação sustentável de preocupações

### Exemplo 3: Integração completa do Suite de Utilitários

**Context**: Configuração de produção com todos os principais dramaturgos-utils e acessórios personalizados.

**Implementation**:

```typescript
// playwright/support/merged-fixtures.ts
import { mergeTests } from '@playwright/test';

// Playwright utils fixtures
import { test as apiRequestFixture } from '@seontechnologies/playwright-utils/api-request/fixtures';
import { test as authFixture } from '@seontechnologies/playwright-utils/auth-session/fixtures';
import { test as interceptFixture } from '@seontechnologies/playwright-utils/intercept-network-call/fixtures';
import { test as recurseFixture } from '@seontechnologies/playwright-utils/recurse/fixtures';
import { test as networkRecorderFixture } from '@seontechnologies/playwright-utils/network-recorder/fixtures';

// Custom project fixtures
import { test as customFixtures } from './custom-fixtures';

// Merge everything
export const test = mergeTests(apiRequestFixture, authFixture, interceptFixture, recurseFixture, networkRecorderFixture, customFixtures);

export { expect } from '@playwright/test';

```

```typescript
// In tests
import { test, expect } from '../support/merged-fixtures';

test('full integration', async ({
  page,
  context,
  apiRequest,
  authToken,
  interceptNetworkCall,
  recurse,
  networkRecorder,
  testUser, // custom
}) => {
  // All utilities + custom fixtures available
  await networkRecorder.setup(context);

  const usersCall = interceptNetworkCall({ url: '**/api/users' });

  await page.goto('/users');
  const { responseJson } = await usersCall;

  expect(responseJson).toContainEqual(expect.objectContaining({ id: testUser.id }));
});

```

**Key Pontos**:

- Um merged-fixtures.ts para todo o projeto
- Combine todos os dramaturgos-utilizados que você usa
- Adicionar dispositivos de projeto personalizados
- import em todos os arquivos de teste

### Exemplo 4: Padrão de substituição de fixação

**Context**: Sobrescrever opções padrão para arquivos de teste específicos ou descreve.

**Implementation**:

```typescript
import { test, expect } from '../support/merged-fixtures';

// Override auth options for entire file
test.use({
  authOptions: {
    userIdentifier: 'admin',
    environment: 'staging',
  },
});

test('uses admin on staging', async ({ authToken }) => {
  // Token is for admin user on staging environment
});

// Override for specific describe block
test.describe('manager tests', () => {
  test.use({
    authOptions: {
      userIdentifier: 'manager',
    },
  });

  test('manager can access reports', async ({ page }) => {
    // Uses manager token
    await page.goto('/reports');
  });
});

```

**Key Pontos**:

- `test.use()` substitui opções de fixação
- Pode substituir no arquivo ou descrever nível
- Opções de mesclagem com padrões
- Substituições de tipo seguro

### Exemplo 5: Evitar conflitos de fixação

**Context**: Lidar com colisões de nomes ao fundir dispositivos com os mesmos nomes.

**Implementation**:

```typescript
// If two fixtures have same name, last one wins
import { test as fixture1 } from './fixture1'; // has 'user' fixture
import { test as fixture2 } from './fixture2'; // also has 'user' fixture

const test = mergeTests(fixture1, fixture2);
// fixture2's 'user' overrides fixture1's 'user'

// Better: Rename fixtures before merging
import { test as base } from '@playwright/test';
import { test as fixture1 } from './fixture1';

const fixture1Renamed = base.extend({
  user1: fixture1._extend.user, // Rename to avoid conflict
});

const test = mergeTests(fixture1Renamed, fixture2);
// Now both 'user1' and 'user' available

// Best: Design fixtures without conflicts
// - Prefix custom fixtures: 'myAppUser', 'myAppDb'
// - Playwright-utils uses descriptive names: 'apiRequest', 'authToken'

```

**Key Pontos**:

- Último jogo ganha em conflitos
- Renomear dispositivos para evitar colisões
- Conjuntos de design com nomes únicos
- Playwright-utils usa nomes descritivos (sem conflitos)

## Estrutura de projeto recomendada

```
playwright/
├── support/
│   ├── merged-fixtures.ts        # ⭐ Single test object for project
│   ├── custom-fixtures.ts        # Your project-specific fixtures
│   ├── auth/
│   │   ├── auth-fixture.ts       # Auth wrapper (if needed)
│   │   └── custom-auth-provider.ts
│   ├── fixtures/
│   │   ├── user-fixture.ts
│   │   ├── db-fixture.ts
│   │   └── api-fixture.ts
│   └── utils/
│       └── factories/
└── tests/
    ├── api/
    │   └── users.spec.ts          # import { test } from '../../support/merged-fixtures'
    ├── e2e/
    │   └── login.spec.ts          # import { test } from '../../support/merged-fixtures'
    └── component/
        └── button.spec.ts         # import { test } from '../../support/merged-fixtures'

```

## Benefícios da composição da fixação

*BMADPROTECT006 FINAL às importações directas:**

```typescript
// ❌ Without mergeTests (verbose)
import { test as base } from '@playwright/test';
import { apiRequest } from '@seontechnologies/playwright-utils/api-request';
import { getAuthToken } from './auth';
import { createUser } from './factories';

test('verbose', async ({ request }) => {
  const token = await getAuthToken();
  const user = await createUser();
  const response = await apiRequest({ request, method: 'GET', path: '/api/users' });
  // Manual wiring everywhere
});

// ✅ With mergeTests (clean)
import { test } from '../support/merged-fixtures';

test('clean', async ({ apiRequest, authToken, testUser }) => {
  const { body } = await apiRequest({ method: 'GET', path: '/api/users' });
  // All fixtures auto-wired
});

```

**Reduction:** ~10 linhas por teste → ~2 linhas

## Fragmentos relacionados

- `overview.md` - Princípios de instalação e design
- `api-request.md`, `auth-session.md`, `recurse.md` - Utilitários para fundir
- `network-recorder.md`, `intercept-network-call.md`, `log.md` - Utilitários adicionais

## Anti-Patterns

**❌ Importando teste de vários arquivos de fixação:**

```typescript
import { test } from '@seontechnologies/playwright-utils/api-request/fixtures';
// Also need auth...
import { test as authTest } from '@seontechnologies/playwright-utils/auth-session/fixtures';
// Name conflict! Which test to use?

```

**✅ Utilizar acessórios fundidos:**

```typescript
import { test } from '../support/merged-fixtures';
// All utilities available, no conflicts

```

**❌ Mesclando muitos acessórios (bacia de cozinha):**

```typescript
// Merging 20+ fixtures makes test signature huge
const test = mergeTests(...20 different fixtures)

test('my test', async ({ fixture1, fixture2, ..., fixture20 }) => {
  // Cognitive overload
})

```

**✅ Mesclar apenas o que você realmente usa:**

```typescript
// Merge the 4-6 fixtures your project actually needs
const test = mergeTests(apiRequestFixture, authFixture, recurseFixture, customFixtures);

```
