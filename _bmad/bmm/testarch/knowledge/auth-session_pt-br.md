# Utilitário de sessão de autenticação

## Princípio

Persistir tokens de autenticação para disco e reutilizar através de testes. Suporta múltiplos identificadores de usuário, autenticação efêmera e contas específicas do trabalhador para execução paralela. Busque fichas uma vez, use em qualquer lugar.

## Racional

A autenticação incorporada do dramaturgo funciona, mas tem limitações:

- Reautentica-se para cada ensaio (lento)
- Único usuário por configuração do projeto
- Sem manipulação de expiração token
- Gerenciamento manual de sessões
- Configuração complexa para cenários multi-usuários

O utilitário `auth-session` fornece:

- **Persistência do token**: Autenticar uma vez, reutilizar através de corridas
- **Suporte multi-utilizador**: Identificadores de utilizador diferentes no mesmo conjunto de testes
- **Autenticação efêmera**: autenticação de utilizador em tempo real sem persistência de disco
- **Contas específicas do trabalhador**: Execução paralela com contas de usuário isoladas
- **Gestão automática do token**: verifica a validade, renova se expirado
- **Flexible provider pattern**: Adaptar-se a qualquer sistema de autenticação (OAuth2, JWT, custom)

## Exemplos de padrões

### Exemplo 1: Configuração básica da sessão de autenticação

**Contexto**: Configure a autenticação global que persiste nos ensaios.

**Implementation**:

```typescript
// Step 1: Configure in global-setup.ts
import { authStorageInit, setAuthProvider, configureAuthSession, authGlobalInit } from '@seontechnologies/playwright-utils/auth-session';
import myCustomProvider from './auth/custom-auth-provider';

async function globalSetup() {
  // Ensure storage directories exist
  authStorageInit();

  // Configure storage path
  configureAuthSession({
    authStoragePath: process.cwd() + '/playwright/auth-sessions',
    debug: true,
  });

  // Set custom provider (HOW to authenticate)
  setAuthProvider(myCustomProvider);

  // Optional: pre-fetch token for default user
  await authGlobalInit();
}

export default globalSetup;

// Step 2: Create auth fixture
import { test as base } from '@playwright/test';
import { createAuthFixtures, setAuthProvider } from '@seontechnologies/playwright-utils/auth-session';
import myCustomProvider from './custom-auth-provider';

// Register provider early
setAuthProvider(myCustomProvider);

export const test = base.extend(createAuthFixtures());

// Step 3: Use in tests
test('authenticated request', async ({ authToken, request }) => {
  const response = await request.get('/api/protected', {
    headers: { Authorization: `Bearer ${authToken}` },
  });

  expect(response.ok()).toBeTruthy();
});

```

**Pontos-chave**

- A configuração global é executada uma vez antes de todos os testes
- Token obtido uma vez, reutilizado em todos os testes
- O provedor personalizado define seu mecanismo de autenticação
- Questões de ordem: configure, em seguida, setProvider, então init

### Exemplo 2: Autenticação multi-usuário

**Contexto**: Testando com diferentes funções de usuário (admin, usuário regular, convidado) no mesmo conjunto de testes.

**Implementation**:

```typescript
import { test } from '../support/auth/auth-fixture';

// Option 1: Per-test user override
test('admin actions', async ({ authToken, authOptions }) => {
  // Override default user
  authOptions.userIdentifier = 'admin';

  const { authToken: adminToken } = await test.step('Get admin token', async () => {
    return { authToken }; // Re-fetches with new identifier
  });

  // Use admin token
  const response = await request.get('/api/admin/users', {
    headers: { Authorization: `Bearer ${adminToken}` },
  });
});

// Option 2: Parallel execution with different users
test.describe.parallel('multi-user tests', () => {
  test('user 1 actions', async ({ authToken }) => {
    // Uses default user (e.g., 'user1')
  });

  test('user 2 actions', async ({ authToken, authOptions }) => {
    authOptions.userIdentifier = 'user2';
    // Uses different token for user2
  });
});

```

**Pontos-chave**

- Substituir `authOptions.userIdentifier` por teste
- Tokens em cache separadamente por identificador de usuário
- Testes paralelos isolados com diferentes usuários
- Contas específicas dos trabalhadores possíveis

### Exemplo 3: Autenticação do Usuário Efémero

**Contexto**: Crie usuários de teste temporários que não persistem no disco (por exemplo, testando o fluxo de criação do usuário).

**Implementation**:

```typescript
import { applyUserCookiesToBrowserContext } from '@seontechnologies/playwright-utils/auth-session';
import { createTestUser } from '../utils/user-factory';

test('ephemeral user test', async ({ context, page }) => {
  // Create temporary user (not persisted)
  const ephemeralUser = await createTestUser({
    role: 'admin',
    permissions: ['delete-users'],
  });

  // Apply auth directly to browser context
  await applyUserCookiesToBrowserContext(context, ephemeralUser);

  // Page now authenticated as ephemeral user
  await page.goto('/admin/users');

  await expect(page.getByTestId('delete-user-btn')).toBeVisible();

  // User and token cleaned up after test
});

```

**Pontos-chave**

- Sem persistência de disco (efémero)
- Aplicar cookies diretamente no contexto
- Útil para testar o ciclo de vida do usuário
- Limpar automático quando o teste termina

### Exemplo 4: Teste de múltiplos usuários em teste único

**Contexto**: Tes