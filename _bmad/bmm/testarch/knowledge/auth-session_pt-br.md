# Utilitário Auth Session

## Princípio

Persista tokens de autenticação em disco e reutilize através de execuções de teste. Suporte a múltiplos identificadores de usuário, autenticação efêmera e contas específicas por worker para execução paralela. Busque tokens uma vez, use em todo lugar.

## Motivação

A autenticação embutida do Playwright funciona mas tem limitações:

- Reautentica para cada execução de teste (lento)
- Único usuário por setup de projeto
- Sem tratamento de expiração de token
- Gerenciamento de sessão manual
- Setup complexo para cenários multi-usuário

O utilitário `auth-session` fornece:

- **Persistência de token**: Autentique uma vez, reutilize através de execuções
- **Suporte multi-usuário**: Diferentes identificadores de usuário na mesma suíte de teste
- **Auth efêmera**: Autenticação de usuário on-the-fly sem persistência em disco
- **Contas específicas por worker**: Execução paralela com contas de usuário isoladas
- **Gerenciamento de token automático**: Verifica validade, renova se expirado
- **Padrão de provedor flexível**: Adapte a qualquer sistema de auth (OAuth2, JWT, customizado)

## Exemplos de Padrões

### Exemplo 1: Setup Básico de Auth Session

**Contexto**: Configurar autenticação global que persiste através de execuções de teste.

**Implementação**:

```typescript
// Passo 1: Configurar em global-setup.ts
import { authStorageInit, setAuthProvider, configureAuthSession, authGlobalInit } from '@seontechnologies/playwright-utils/auth-session';
import myCustomProvider from './auth/custom-auth-provider';

async function globalSetup() {
  // Garantir que diretórios de armazenamento existem
  authStorageInit();

  // Configurar caminho de armazenamento
  configureAuthSession({
    authStoragePath: process.cwd() + '/playwright/auth-sessions',
    debug: true,
  });

  // Definir provedor customizado (COMO autenticar)
  setAuthProvider(myCustomProvider);

  // Opcional: pré-buscar token para usuário padrão
  await authGlobalInit();
}

export default globalSetup;

// Passo 2: Criar fixture auth
import { test as base } from '@playwright/test';
import { createAuthFixtures, setAuthProvider } from '@seontechnologies/playwright-utils/auth-session';
import myCustomProvider from './custom-auth-provider';

// Registrar provedor cedo
setAuthProvider(myCustomProvider);

export const test = base.extend(createAuthFixtures());

// Passo 3: Usar em testes
test('requisição autenticada', async ({ authToken, request }) => {
  const response = await request.get('/api/protected', {
    headers: { Authorization: `Bearer ${authToken}` },
  });

  expect(response.ok()).toBeTruthy();
});
```

**Pontos Chave**:

- Setup global roda uma vez antes de todos os testes
- Token buscado uma vez, reutilizado através de todos os testes
- Provedor customizado define seu mecanismo de auth
- Ordem importa: configure, então setProvider, então init

### Exemplo 2: Autenticação Multi-Usuário

**Contexto**: Testar com diferentes roles de usuário (admin, usuário regular, convidado) na mesma suíte de teste.

**Implementação**:

```typescript
import { test } from '../support/auth/auth-fixture';

// Opção 1: Sobrescrita de usuário por teste
test('ações de admin', async ({ authToken, authOptions }) => {
  // Sobrescrever usuário padrão
  authOptions.userIdentifier = 'admin';

  const { authToken: adminToken } = await test.step('Obter token admin', async () => {
    return { authToken }; // Re-busca com novo identificador
  });

  // Usar token admin
  const response = await request.get('/api/admin/users', {
    headers: { Authorization: `Bearer ${adminToken}` },
  });
});

// Opção 2: Execução paralela com diferentes usuários
test.describe.parallel('testes multi-usuário', () => {
  test('ações usuário 1', async ({ authToken }) => {
    // Usa usuário padrão (ex: 'user1')
  });

  test('ações usuário 2', async ({ authToken, authOptions }) => {
    authOptions.userIdentifier = 'user2';
    // Usa token diferente para user2
  });
});
```

**Pontos Chave**:

- Sobrescreva `authOptions.userIdentifier` por teste
- Tokens cacheados separadamente por identificador de usuário
- Testes paralelos isolados com diferentes usuários
- Contas específicas por worker possíveis

### Exemplo 3: Autenticação de Usuário Efêmera

**Contexto**: Criar usuários de teste temporários que não persistem em disco (ex: testar fluxo de criação de usuário).

**Implementação**:

```typescript
import { applyUserCookiesToBrowserContext } from '@seontechnologies/playwright-utils/auth-session';
import { createTestUser } from '../utils/user-factory';

test('teste de usuário efêmero', async ({ context, page }) => {
  // Criar usuário temporário (não persistido)
  const ephemeralUser = await createTestUser({
    role: 'admin',
    permissions: ['delete-users'],
  });

  // Aplicar auth diretamente ao contexto do navegador
  await applyUserCookiesToBrowserContext(context, ephemeralUser);

  // Página agora autenticada como usuário efêmero
  await page.goto('/admin/users');

  await expect(page.getByTestId('delete-user-btn')).toBeVisible();

  // Usuário e token limpos após teste
});
```

**Pontos Chave**:

- Sem persistência em disco (efêmero)
- Aplicar cookies diretamente ao contexto
- Útil para testar ciclo de vida de usuário
- Limpeza automática quando teste termina

### Exemplo 4: Testando Múltiplos Usuários em Único Teste

**Contexto**: Testar interações entre usuários (mensagens, compartilhamento, funcionalidades de colaboração).

**Implementação**:

```typescript
test('interação de usuário', async ({ browser }) => {
  // Contexto Usuário 1
  const user1Context = await browser.newContext({
    storageState: './auth-sessions/local/user1/storage-state.json',
  });
  const user1Page = await user1Context.newPage();

  // Contexto Usuário 2
  const user2Context = await browser.newContext({
    storageState: './auth-sessions/local/user2/storage-state.json',
  });
  const user2Page = await user2Context.newPage();

  // Usuário 1 envia mensagem
  await user1Page.goto('/messages');
  await user1Page.fill('#message', 'Olá do usuário 1');
  await user1Page.click('#send');

  // Usuário 2 recebe mensagem
  await user2Page.goto('/messages');
  await expect(user2Page.getByText('Olá do usuário 1')).toBeVisible();

  // Limpeza
  await user1Context.close();
  await user2Context.close();
});
```

**Pontos Chave**:

- Cada usuário tem contexto de navegador separado
- Referencie arquivos de estado de armazenamento diretamente
- Teste interações em tempo real
- Limpe contextos após teste

### Exemplo 5: Contas Específicas por Worker (Teste Paralelo)

**Contexto**: Rodar testes em paralelo com contas de usuário isoladas por worker para evitar conflitos.

**Implementação**:

```typescript
// playwright.config.ts
export default defineConfig({
  workers: 4, // 4 workers paralelos
  use: {
    // Cada worker usa usuário diferente
    storageState: async ({}, use, testInfo) => {
      const workerIndex = testInfo.workerIndex;
      const userIdentifier = `worker-${workerIndex}`;

      await use(`./auth-sessions/local/${userIdentifier}/storage-state.json`);
    },
  },
});

// Testes rodam em paralelo, cada worker com seu próprio usuário
test('teste paralelo 1', async ({ page }) => {
  // Worker 0 usa conta worker-0
  await page.goto('/dashboard');
});

test('teste paralelo 2', async ({ page }) => {
  // Worker 1 usa conta worker-1
  await page.goto('/dashboard');
});
```

**Pontos Chave**:

- Cada worker tem conta de usuário isolada
- Sem conflitos em execução paralela
- Gerenciamento de token automático por worker
- Escala para qualquer número de workers

## Padrão de Provedor de Auth Customizado

**Contexto**: Adaptar auth-session ao seu sistema de autenticação (OAuth2, JWT, SAML, customizado).

**Estrutura de provedor mínima**:

```typescript
import { type AuthProvider } from '@seontechnologies/playwright-utils/auth-session';

const myCustomProvider: AuthProvider = {
  getEnvironment: (options) => options.environment || 'local',

  getUserIdentifier: (options) => options.userIdentifier || 'default-user',

  extractToken: (storageState) => {
    // Extrair token do seu formato de armazenamento
    return storageState.cookies.find((c) => c.name === 'auth_token')?.value;
  },

  extractCookies: (tokenData) => {
    // Converter token para cookies para contexto de navegador
    return [
      {
        name: 'auth_token',
        value: tokenData,
        domain: 'example.com',
        path: '/',
        httpOnly: true,
        secure: true,
      },
    ];
  },

  isTokenExpired: (storageState) => {
    // Verificar se token está expirado
    const expiresAt = storageState.cookies.find((c) => c.name === 'expires_at');
    return Date.now() > parseInt(expiresAt?.value || '0');
  },

  manageAuthToken: async (request, options) => {
    // Lógica principal de aquisição de token
    // Retornar estado de armazenamento com cookies/localStorage
  },
};

export default myCustomProvider;
```

## Integração com API Request

```typescript
import { test } from '@seontechnologies/playwright-utils/fixtures';

test('chamada de API autenticada', async ({ apiRequest, authToken }) => {
  const { status, body } = await apiRequest({
    method: 'GET',
    path: '/api/protected',
    headers: { Authorization: `Bearer ${authToken}` },
  });

  expect(status).toBe(200);
});
```

## Fragmentos Relacionados

- `overview.md` - Instalação e composição de fixture
- `api-request.md` - Requisições de API autenticadas
- `fixtures-composition.md` - Fundindo auth com outros utilitários

## Anti-Padrões

**❌ Chamar setAuthProvider após globalSetup:**

```typescript
async function globalSetup() {
  configureAuthSession(...)
  await authGlobalInit()  // Provedor não definido ainda!
  setAuthProvider(provider)  // Tarde demais
}
```

**✅ Registrar provedor antes do init:**

```typescript
async function globalSetup() {
  authStorageInit()
  configureAuthSession(...)
  setAuthProvider(provider)  // Primeiro
  await authGlobalInit()     // Então init
}
```

**❌ Hardcoding caminhos de armazenamento:**

```typescript
const storageState = './auth-sessions/local/user1/storage-state.json'; // Frágil
```

**✅ Use funções helper:**

```typescript
import { getTokenFilePath } from '@seontechnologies/playwright-utils/auth-session';

const tokenPath = getTokenFilePath({
  environment: 'local',
  userIdentifier: 'user1',
  tokenFileName: 'storage-state.json',
});
```
