# Composição de fixação com mesclagemTestes

## Princípio

Combine vários acessórios Playwright usando `mergeTests` para criar um objeto de teste unificado com todas as capacidades. Construir infraestrutura de teste composable fundindo jogos de playwright-utils com acessórios de projeto personalizados.

## Racional

Usar dispositivos de várias fontes requer combiná-los:

- Importar de vários arquivos de fixação é verbose
- Conflitos de nomes entre jogos
- Definições de acessórios duplicados
- Nenhum objeto de teste único claro

O `mergeTests` do dramaturgo fornece:

- **Objecto de ensaio único**: Todos os dispositivos de um import
- **Resolução de conflitos**: Lida automaticamente com colisões de nomes
- **Padrão de composição**: Misture utilitários, acessórios personalizados, acessórios de terceiros
- **Segurança do tipo**: Suporte Full TypeScript para acessórios fundidos
- **Manutenção**: Um lugar para gerir todos os acessórios

## Exemplos de padrões

### Exemplo 1: Junção básica de fixação

**Contexto**: Combine vários acessórios de playwright-utils em um único objeto de teste.

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

**Pontos-chave**

- Criar um `merged-fixtures.ts` por projeto
- Importar objeto de teste de acessórios fundidos em todos os arquivos de teste
- Todos os utilitários disponíveis sem múltiplas importações
- Acesso seguro de tipo a todos os dispositivos

### Exemplo 2: Combinando com fixações personalizadas

**Contexto**: Adicione dispositivos específicos para projetos ao lado de dramaturgos-utils.

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

**Pontos-chave**

- Os acessórios personalizados estendem o teste `base`
- Mesclar personalizado com acessórios de dramaturgo-utils
- Tudo disponível em uma assinatura de teste
- Separação sustentável de preocupações

### Exemplo 3: Integração completa do Suite de Utilitários

**Contexto**: Configuração de produção com todos os principais dramaturgos-utils e acessórios personalizados.

**Implementation**:

«``typescript
// playwright/support/merged-fixtures.ts
BMADPROTECT015end BMADPROTECT020end de '@ playwright/test';

// Playwright usa acessórios
import { test as apiRequestFixture } de '@seontechnologies/playwright-utils/api-request/fixtures';
import { test as authFixture } de '@seontechnologies/playwright-utils/auth-session/fixtures';
import BMADPROTECT017End from '@ seontechnologies/playwright- utilis/intercept-network- call/fixtur