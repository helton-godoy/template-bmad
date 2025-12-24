# Utilitário Intercept Network Call

## Princípio

Intercepte requisições de rede com uma única chamada declarativa que retorna uma Promessa. Parseie automaticamente respostas JSON, suporte tanto padrões de espião (observar) quanto stub (mock), e use correspondência de padrão glob poderosa para filtragem de URL.

## Motivação

A interceptação de rede do Playwright puro requer múltiplos passos:

- `page.route()` para configurar, `page.waitForResponse()` para capturar
- Parsing manual de JSON
- Sintaxe verbosa para tratamento condicional
- Predicados de filtro complexos

O utilitário `interceptNetworkCall` fornece:

- **Chamada declarativa única**: Setup e espera em uma declaração
- **Parsing automático de JSON**: Resposta pré-parseada, fortemente tipada
- **Padrões de URL flexíveis**: Correspondência glob com picomatch
- **Modos de espião ou stub**: Observe tráfego real ou mock respostas
- **API concisa**: Reduz boilerplate em 60-70%

## Exemplos de Padrões

### Exemplo 1: Espionar na Rede (Observar Tráfego Real)

**Contexto**: Capturar e inspecionar respostas de API reais para validação.

**Implementação**:

```typescript
import { test } from '@seontechnologies/playwright-utils/intercept-network-call/fixtures';

test('deve espionar API de usuários', async ({ page, interceptNetworkCall }) => {
  // Setup de interceptação ANTES da navegação
  const usersCall = interceptNetworkCall({
    url: '**/api/users', // Padrão glob
  });

  await page.goto('/dashboard');

  // Aguardar resposta e acessar dados parseados
  const { responseJson, status } = await usersCall;

  expect(status).toBe(200);
  expect(responseJson).toHaveLength(10);
  expect(responseJson[0]).toHaveProperty('name');
});
```

**Pontos Chave**:

- Intercepte antes da navegação (crítico para testes livres de condição de corrida)
- Retorna Promessa com `{ responseJson, status, requestBody }`
- Padrões glob (`**` corresponde a qualquer segmento de caminho)
- JSON automaticamente parseado

### Exemplo 2: Stub de Rede (Mock de Resposta)

**Contexto**: Mock de respostas de API para testar comportamento de UI sem backend.

**Implementação**:

```typescript
test('deve fazer stub da API de usuários', async ({ page, interceptNetworkCall }) => {
  const mockUsers = [
    { id: 1, name: 'Usuário Teste 1' },
    { id: 2, name: 'Usuário Teste 2' },
  ];

  const usersCall = interceptNetworkCall({
    url: '**/api/users',
    fulfillResponse: {
      status: 200,
      body: mockUsers,
    },
  });

  await page.goto('/dashboard');
  await usersCall;

  // UI mostra dados mockados
  await expect(page.getByText('Usuário Teste 1')).toBeVisible();
  await expect(page.getByText('Usuário Teste 2')).toBeVisible();
});
```

**Pontos Chave**:

- `fulfillResponse` mocka a API
- Sem backend necessário
- Teste lógica de UI isoladamente
- Código de status e corpo totalmente controláveis

### Exemplo 3: Tratamento de Resposta Condicional

**Contexto**: Respostas diferentes baseadas em método de requisição ou parâmetros.

**Implementação**:

```typescript
test('mock condicional', async ({ page, interceptNetworkCall }) => {
  await interceptNetworkCall({
    url: '**/api/data',
    handler: async (route, request) => {
      if (request.method() === 'POST') {
        // Mock sucesso de POST
        await route.fulfill({
          status: 201,
          body: JSON.stringify({ id: 'new-id', success: true }),
        });
      } else if (request.method() === 'GET') {
        // Mock GET com dados
        await route.fulfill({
          status: 200,
          body: JSON.stringify([{ id: 1, name: 'Item' }]),
        });
      } else {
        // Deixar outros métodos passarem
        await route.continue();
      }
    },
  });

  await page.goto('/data-page');
});
```

**Pontos Chave**:

- Função `handler` para lógica complexa
- Acesso a objetos `route` e `request` completos
- Pode mockar, continuar ou abortar
- Flexível para cenários avançados

### Exemplo 4: Simulação de Erro

**Contexto**: Testar tratamento de erro na UI quando API falha.

**Implementação**:

```typescript
test('deve tratar erros de API graciosamente', async ({ page, interceptNetworkCall }) => {
  // Simular erro 500
  const errorCall = interceptNetworkCall({
    url: '**/api/users',
    fulfillResponse: {
      status: 500,
      body: { error: 'Erro Interno do Servidor' },
    },
  });

  await page.goto('/dashboard');
  await errorCall;

  // Verificar UI mostra estado de erro
  await expect(page.getByText('Falha ao carregar usuários')).toBeVisible();
  await expect(page.getByTestId('retry-button')).toBeVisible();
});

// Simular timeout de rede
test('deve tratar timeout', async ({ page, interceptNetworkCall }) => {
  await interceptNetworkCall({
    url: '**/api/slow',
    handler: async (route) => {
      // Nunca responder - simula timeout
      await new Promise(() => {});
    },
  });

  await page.goto('/slow-page');

  // UI deve mostrar erro de timeout
  await expect(page.getByText('Requisição excedeu tempo limite')).toBeVisible({ timeout: 10000 });
});
```

**Pontos Chave**:

- Mock de status de erro (4xx, 5xx)
- Testar cenários de timeout
- Validar estados de UI de erro
- Sem falhas reais necessárias

### Exemplo 5: Múltiplas Interceptações (Ordem Importa!)

**Contexto**: Interceptar diferentes endpoints no mesmo teste - ordem de setup é crítica.

**Implementação**:

```typescript
test('múltiplas interceptações', async ({ page, interceptNetworkCall }) => {
  // ✅ CORRETO: Configurar todas interceptações ANTES da navegação
  const usersCall = interceptNetworkCall({ url: '**/api/users' });
  const productsCall = interceptNetworkCall({ url: '**/api/products' });
  const ordersCall = interceptNetworkCall({ url: '**/api/orders' });

  // ENTÃO navegar
  await page.goto('/dashboard');

  // Aguardar por todos (ou específicos)
  const [users, products] = await Promise.all([usersCall, productsCall]);

  expect(users.responseJson).toHaveLength(10);
  expect(products.responseJson).toHaveLength(50);
});
```

**Pontos Chave**:

- Configure todas interceptações antes de disparar ações
- Use `Promise.all()` para aguardar múltiplas chamadas
- Ordem: interceptar → navegar → aguardar
- Previne condições de corrida

## Correspondência de Padrão URL

**Padrões glob suportados:**

```typescript
'**/api/users'; // Qualquer caminho terminando com /api/users
'/api/users'; // Correspondência exata
'**/users/*'; // Qualquer sub-caminho de users
'**/api/{users,products}'; // Ou users ou products
'**/api/users?id=*'; // Com query params
```

**Usa biblioteca picomatch** - mesma sintaxe de padrão do `page.route()` do Playwright mas com API mais limpa.

## Comparação com Playwright Puro

| Playwright Puro                                             | intercept-network-call                                       |
| ----------------------------------------------------------- | ------------------------------------------------------------ |
| `await page.route('/api/users', route => route.continue())` | `const call = interceptNetworkCall({ url: '**/api/users' })` |
| `const resp = await page.waitForResponse('/api/users')`     | (Combinado em declaração única)                              |
| `const json = await resp.json()`                            | `const { responseJson } = await call`                        |
| `const status = resp.status()`                              | `const { status } = await call`                              |
| Predicados de filtro complexos                              | Padrões glob simples                                         |

**Redução:** ~5-7 linhas → ~2-3 linhas por interceptação

## Fragmentos Relacionados

- `network-first.md` - Padrão core: interceptar antes de navegar
- `network-recorder.md` - Teste offline baseado em HAR
- `overview.md` - Básico de composição de fixture

## Anti-Padrões

**❌ Interceptar depois da navegação:**

```typescript
await page.goto('/dashboard'); // Navegação começa
const usersCall = interceptNetworkCall({ url: '**/api/users' }); // Tarde demais!
```

**✅ Interceptar antes de navegar:**

```typescript
const usersCall = interceptNetworkCall({ url: '**/api/users' }); // Primeiro
await page.goto('/dashboard'); // Então navegar
const { responseJson } = await usersCall; // Então aguardar
```

**❌ Ignorar a Promessa retornada:**

```typescript
interceptNetworkCall({ url: '**/api/users' }); // Não aguardado!
await page.goto('/dashboard');
// Sem espera determinística - condição de corrida
```

**✅ Sempre aguarde a interceptação:**

```typescript
const usersCall = interceptNetworkCall({ url: '**/api/users' });
await page.goto('/dashboard');
await usersCall; // Espera determinística
```
