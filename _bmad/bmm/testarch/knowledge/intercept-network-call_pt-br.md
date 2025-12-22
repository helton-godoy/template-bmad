# Utilitário de Intercepção de Chamadas de Rede

## Princípio

Interceptar pedidos de rede com uma única chamada declarativa que retorna uma promessa. Analisar automaticamente respostas JSON, suportar ambos os padrões espião (observe) e stub (mock), e usar poderoso padrão glob correspondência para filtragem de URL.

## Racional

A intercepção de rede da Vanilla Playwright requer vários passos:

- `page.route()` para instalação, `page.waitForResponse()` para captura
- Análise manual do JSON
- sintaxe verbose para tratamento condicional
- Predicados filtrantes complexos

O utilitário `interceptNetworkCall` fornece:

- **Chamada declarativa única**: Configuração e espera numa declaração
- **Automatic JSON análise**: resposta pré-parsed, fortemente tipado
- **Padrões de URL flexíveis**: Combinação de glob com picomatch
- **Modos de spy ou stub**: Observar o tráfego real ou respostas simuladas
- **API concisa**: reduz a caldeira em 60-70%

## Exemplos de padrões

### Exemplo 1: Espionar na rede (Observar tráfego real)

**Contexto**: Capture e inspecione respostas reais da API para validação.

**Implementation**:

```typescript
import { test } from '@seontechnologies/playwright-utils/intercept-network-call/fixtures';

test('should spy on users API', async ({ page, interceptNetworkCall }) => {
  // Setup interception BEFORE navigation
  const usersCall = interceptNetworkCall({
    url: '**/api/users', // Glob pattern
  });

  await page.goto('/dashboard');

  // Wait for response and access parsed data
  const { responseJson, status } = await usersCall;

  expect(status).toBe(200);
  expect(responseJson).toHaveLength(10);
  expect(responseJson[0]).toHaveProperty('name');
});

```

**Pontos-chave**

- Intercepção antes da navegação (crítico para testes livres de corrida)
- Retorna Promessa com `{ responseJson, status, requestBody }`
- Glob patterns (`**` corresponde a qualquer segmento de caminho)
- JSON automaticamente analisado

### Exemplo 2: Rede de Stub (Resposta a Mock)

**Context**: Mock API respostas para testar o comportamento de UI sem backend.

**Implementation**:

```typescript
test('should stub users API', async ({ page, interceptNetworkCall }) => {
  const mockUsers = [
    { id: 1, name: 'Test User 1' },
    { id: 2, name: 'Test User 2' },
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

  // UI shows mocked data
  await expect(page.getByText('Test User 1')).toBeVisible();
  await expect(page.getByText('Test User 2')).toBeVisible();
});

```

**Pontos-chave**

- `fulfillResponse` zomba da API
- Nenhuma infra-estrutura necessária.
- Teste a lógica da IU isoladamente
- Código do estado e corpo totalmente controlável

### Exemplo 3: Tratamento de resposta condicional

**Contexto**: Respostas diferentes baseadas no método ou parâmetros de solicitação.

**Implementation**:

```typescript
test('conditional mocking', async ({ page, interceptNetworkCall }) => {
  await interceptNetworkCall({
    url: '**/api/data',
    handler: async (route, request) => {
      if (request.method() === 'POST') {
        // Mock POST success
        await route.fulfill({
          status: 201,
          body: JSON.stringify({ id: 'new-id', success: true }),
        });
      } else if (request.method() === 'GET') {
        // Mock GET with data
        await route.fulfill({
          status: 200,
          body: JSON.stringify([{ id: 1, name: 'Item' }]),
        });
      } else {
        // Let other methods through
        await route.continue();
      }
    },
  });

  await page.goto('/data-page');
});

```

**Pontos-chave**

- `handler` function para lógica complexa
- Acesse objetos `route` e `request`
- Pode zombar, continuar, ou abortar
- Flexível para cenários avançados

### Exemplo 4: Simulação de Erro

**Contexto**: Tratamento de erros de teste na UI quando a API falha.

**Implementation**:

```typescript
test('should handle API errors gracefully', async ({ page, interceptNetworkCall }) => {
  // Simulate 500 error
  const errorCall = interceptNetworkCall({
    url: '**/api/users',
    fulfillResponse: {
      status: 500,
      body: { error: 'Internal Server Error' },
    },
  });

  await page.goto('/dashboard');
  await errorCall;

  // Verify UI shows error state
  await expect(page.getByText('Failed to load users')).toBeVisible();
  await expect(page.getByTestId('retry-button')).toBeVisible();
});

// Simulate network timeout
test('should handle timeout', async ({ page, interceptNetworkCall }) => {
  await interceptNetworkCall({
    url: '**/api/slow',
    handler: async (route) => {
      // Never respond - simulates timeout
      await new Promise(() => {});
    },
  });

  await page.goto('/slow-page');

  // UI should show timeout error
  await expect(page.getByText('Request timed out')).toBeVisible({ timeout: 10000 });
});

```

**Pontos-chave**

- Status de erro do Mock (4xx, 5xx)
- Cenários de tempo limite de teste
- Validar estados de erro UI
- Não são necessárias falhas reais.

### Exemplo 5: Intercepções Múltiplas (Ordem de Matérias!)

**Contexto**: Interceptando diferentes objetivos no sam