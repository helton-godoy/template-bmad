# Utilitário de recurso (Polling)

## Princípio

Use pesquisas em estilo Cypress com `expect.poll` da Playwright para esperar por condições assíncronas. Fornece tempo limite configurável, intervalo, registro e callbacks pós-polling com categorização de erro aprimorada.

## Racional

Teste de operações async (empregos de base, eventual consistência, processamento webhook) requer votação:

- Vanilla `expect.poll` é verbose
- Nenhum registro incorporado para depuração
- Erros genéricos de tempo- limite
- Não há ganchos pós-poluição.

O utilitário `recurse` fornece:

- **Syntaxe limpa**: Inspirado por cipreste-recurso
- **Erros melhorados**: Tempo limite vs falha de comando vs erros predicados
- **Madeireira construída**: Progresso das sondagens
- **Convocações pós-poluição**: Resultados do processo após o sucesso
- **Type-safe**: Suporte genérico Full TypeScript

## Exemplos de padrões

### Exemplo 1: Polação básica

**Contexto**: Aguarde a operação async para completar com tempo limite e intervalo personalizados.

**Implementation**:

```typescript
import { test } from '@seontechnologies/playwright-utils/recurse/fixtures';

test('should wait for job completion', async ({ recurse, apiRequest }) => {
  // Start job
  const { body } = await apiRequest({
    method: 'POST',
    path: '/api/jobs',
    body: { type: 'export' },
  });

  // Poll until ready
  const result = await recurse(
    () => apiRequest({ method: 'GET', path: `/api/jobs/${body.id}` }),
    (response) => response.body.status === 'completed',
    {
      timeout: 60000, // 60 seconds max
      interval: 2000, // Check every 2 seconds
      log: 'Waiting for export job to complete',
    },
  );

  expect(result.body.downloadUrl).toBeDefined();
});

```

**Pontos-chave**

- Primeiro arg: comando function (o que executar)
- Segundo arg: predicado function (quando parar)
- Options: timeout, intervalo, mensagem de registo
- Retorna o valor quando predicado retorna true

### Exemplo 2: Polling with Assertions

**Contexto**: Use asserções diretamente no predicado para testes mais expressivos.

**Implementation**:

```typescript
test('should poll with assertions', async ({ recurse, apiRequest }) => {
  await apiRequest({
    method: 'POST',
    path: '/api/events',
    body: { type: 'user-created', userId: '123' },
  });

  // Poll with assertions in predicate
  await recurse(
    async () => {
      const { body } = await apiRequest({ method: 'GET', path: '/api/events/123' });
      return body;
    },
    (event) => {
      // Use assertions instead of boolean returns
      expect(event.processed).toBe(true);
      expect(event.timestamp).toBeDefined();
      // If assertions pass, predicate succeeds
    },
    { timeout: 30000 },
  );
});

```

**Pontos-chave**

- Predicate pode usar afirmações `expect()`
- Se as afirmações lançarem, as sondagens continuam
- Se as afirmações passarem, a votação terá sucesso.
- Mais expressivo que os retornos booleanos

### Exemplo 3: Mensagens de erro personalizadas

**Contexto**: Forneça mensagens de erro específicas do contexto para falhas de timeout.

**Implementation**:

```typescript
test('custom error on timeout', async ({ recurse, apiRequest }) => {
  try {
    await recurse(
      () => apiRequest({ method: 'GET', path: '/api/status' }),
      (res) => res.body.ready === true,
      {
        timeout: 10000,
        error: 'System failed to become ready within 10 seconds - check background workers',
      },
    );
  } catch (error) {
    // Error message includes custom context
    expect(error.message).toContain('check background workers');
    throw error;
  }
});

```

**Pontos-chave**

- `error` opção fornece mensagem personalizada
- Substitui o padrão "Timed out after X ms"
- Incluir dicas de depuração na mensagem de erro
- Ajuda a diagnosticar falhas mais rápido

### Exemplo 4: Chamada pós-polling

**Contexto**: Processo ou log de resultados após votação bem sucedida.

**Implementation**:

```typescript
test('post-poll processing', async ({ recurse, apiRequest }) => {
  const finalResult = await recurse(
    () => apiRequest({ method: 'GET', path: '/api/batch-job/123' }),
    (res) => res.body.status === 'completed',
    {
      timeout: 60000,
      post: (result) => {
        // Runs after successful polling
        console.log(`Job completed in ${result.body.duration}ms`);
        console.log(`Processed ${result.body.itemsProcessed} items`);
        return result.body;
      },
    },
  );

  expect(finalResult.itemsProcessed).toBeGreaterThan(0);
});

```

**Pontos-chave**

- `post` callback é executado após o predicado ter sucesso
- Recebe o resultado final
- Pode transformar ou registrar resultados
- Valor de retorno torna-se resultado final `recurse`

### Exemplo 5: Integração com Pedido de API (Padrão Comum)

**Contexto**: Caso de uso mais comum - sondagem de parâmetros API para alterações de estado.

**Implementation**:

«``typescript
BMADPROTECT021end BMADPROTECT029end de '@seontechnologies/playwright-utils/fixtures';

teste('end-to-end polling', async ({ apiRequest, recurse }) => {
  // Trigger async operation
  const { body: createResp } = BMADPROTECT017End apiRequest({
    method: 'POST',
    path: '/api/data-import',
    body: { source: 's3://bucket/data.csv' },
});

