# Utilitário Recurse (Polling)

## Princípio

Utilize polling no estilo Cypress com `expect.poll` do Playwright para aguardar condições assíncronas. Fornece timeout configurável, intervalo, logs e callbacks pós-polling com categorização aprimorada de erros.

## Motivação

Testar operações assíncronas (jobs em segundo plano, consistência eventual, processamento de webhook) requer polling:

- `expect.poll` puro é verboso
- Sem logs nativos para debugging
- Erros de timeout genéricos
- Sem hooks pós-polling

O utilitário `recurse` oferece:

- **Sintaxe limpa**: Inspirado no cypress-recurse
- **Erros aprimorados**: Timeout vs falha no comando vs erros no predicado
- **Log integrado**: Rastreia o progresso do polling
- **Callbacks pós-poll**: Processa resultados após o sucesso
- **Type-safe**: Suporte completo a genéricos do TypeScript

## Exemplos de Padrões

### Exemplo 1: Polling Básico

**Contexto**: Aguardar a conclusão de uma operação assíncrona com timeout e intervalo personalizados.

**Implementação**:

```typescript
import { test } from '@seontechnologies/playwright-utils/recurse/fixtures';

test('deve aguardar a conclusão do job', async ({ recurse, apiRequest }) => {
  // Inicia o job
  const { body } = await apiRequest({
    method: 'POST',
    path: '/api/jobs',
    body: { type: 'export' },
  });

  // Poll até estar pronto
  const result = await recurse(
    () => apiRequest({ method: 'GET', path: `/api/jobs/${body.id}` }),
    (response) => response.body.status === 'completed',
    {
      timeout: 60000, // máx 60 segundos
      interval: 2000, // Verifica a cada 2 segundos
      log: 'Aguardando job de exportação completar',
    },
  );

  expect(result.body.downloadUrl).toBeDefined();
});
```

**Pontos Chave**:

- Primeiro arg: função de comando (o que executar)
- Segundo arg: função predicado (quando parar)
- Opções: timeout, intervalo, mensagem de log
- Retorna o valor quando o predicado retorna verdadeiro

### Exemplo 2: Polling com Asserções

**Contexto**: Utilizar asserções diretamente no predicado para testes mais expressivos.

**Implementação**:

```typescript
test('deve fazer polling com asserções', async ({ recurse, apiRequest }) => {
  await apiRequest({
    method: 'POST',
    path: '/api/events',
    body: { type: 'user-created', userId: '123' },
  });

  // Poll com asserções no predicado
  await recurse(
    async () => {
      const { body } = await apiRequest({ method: 'GET', path: '/api/events/123' });
      return body;
    },
    (event) => {
      // Use asserções em vez de retornos booleanos
      expect(event.processed).toBe(true);
      expect(event.timestamp).toBeDefined();
      // Se as asserções passarem, o predicado tem sucesso
    },
    { timeout: 30000 },
  );
});
```

**Pontos Chave**:

- O predicado pode usar asserções `expect()`
- Se as asserções lançarem erro, o polling continua
- Se as asserções passarem, o polling tem sucesso
- Mais expressivo que retornos booleanos

### Exemplo 3: Mensagens de Erro Personalizadas

**Contexto**: Fornecer mensagens de erro específicas do contexto para falhas de timeout.

**Implementação**:

```typescript
test('erro personalizado no timeout', async ({ recurse, apiRequest }) => {
  try {
    await recurse(
      () => apiRequest({ method: 'GET', path: '/api/status' }),
      (res) => res.body.ready === true,
      {
        timeout: 10000,
        error: 'Sistema falhou ao ficar pronto em 10 segundos - verifique workers em segundo plano',
      },
    );
  } catch (error) {
    // Mensagem de erro inclui contexto personalizado
    expect(error.message).toContain('verifique workers em segundo plano');
    throw error;
  }
});
```

**Pontos Chave**:

- A opção `error` fornece mensagem personalizada
- Substitui o padrão "Timed out after X ms"
- Inclui dicas de debugging na mensagem de erro
- Ajuda a diagnosticar falhas mais rapidamente

### Exemplo 4: Callback Pós-Polling

**Contexto**: Processar ou logar resultados após um polling bem-sucedido.

**Implementação**:

```typescript
test('processamento pós-poll', async ({ recurse, apiRequest }) => {
  const finalResult = await recurse(
    () => apiRequest({ method: 'GET', path: '/api/batch-job/123' }),
    (res) => res.body.status === 'completed',
    {
      timeout: 60000,
      post: (result) => {
        // Roda após polling bem-sucedido
        console.log(`Job completado em ${result.body.duration}ms`);
        console.log(`Processados ${result.body.itemsProcessed} itens`);
        return result.body;
      },
    },
  );

  expect(finalResult.itemsProcessed).toBeGreaterThan(0);
});
```

**Pontos Chave**:

- Callback `post` roda após o predicado ter sucesso
- Recebe o resultado final
- Pode transformar ou logar resultados
- O valor de retorno torna-se o resultado final do `recurse`

### Exemplo 5: Integração com API Request (Padrão Comum)

**Contexto**: Caso de uso mais comum - polling em endpoints de API para mudanças de estado.

**Implementação**:

```typescript
import { test } from '@seontechnologies/playwright-utils/fixtures';

test('polling end-to-end', async ({ apiRequest, recurse }) => {
  // Dispara operação assíncrona
  const { body: createResp } = await apiRequest({
    method: 'POST',
    path: '/api/data-import',
    body: { source: 's3://bucket/data.csv' },
  });

  // Poll até a importação completar
  const importResult = await recurse(
    () => apiRequest({ method: 'GET', path: `/api/data-import/${createResp.importId}` }),
    (response) => {
      const { status, rowsImported } = response.body;
      return status === 'completed' && rowsImported > 0;
    },
    {
      timeout: 120000, // 2 minutos para importações grandes
      interval: 5000, // Checa a cada 5 segundos
      log: `Polling da importação ${createResp.importId}`,
    },
  );

  expect(importResult.body.rowsImported).toBeGreaterThan(1000);
  expect(importResult.body.errors).toHaveLength(0);
});
```

**Pontos Chave**:

- Combina `apiRequest` + `recurse` para polling de API
- Ambos de `@seontechnologies/playwright-utils/fixtures`
- Predicados complexos com múltiplas condições
- Logging mostra o progresso do polling nos relatórios de teste

## Tipos de Erro Aprimorados

O utilitário categoriza erros para debugging mais fácil:

```typescript
// TimeoutError - Predicado nunca retornou verdadeiro
Error: Polling timed out after 30000ms: Job never completed

// CommandError - Função de comando lançou erro
Error: Command failed: Request failed with status 500

// PredicateError - Função predicado lançou erro (não de asserções)
Error: Predicate failed: Cannot read property 'status' of undefined
```

## Comparação com Playwright Puro

| Playwright Puro                                                   | Utilitário recurse                                                        |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `await expect.poll(() => { ... }, { timeout: 30000 }).toBe(true)` | `await recurse(() => { ... }, (val) => val === true, { timeout: 30000 })` |
| Sem logging                                                       | Opção de log integrada                                                    |
| Erros de timeout genéricos                                        | Erros categorizados (timeout/comando/predicado)                           |
| Sem hooks pós-poll                                                | Suporte a callback `post`                                                 |

## Quando Usar

**Use recurse para:**

- ✅ Conclusão de jobs em segundo plano
- ✅ Processamento de Webhook/eventos
- ✅ Consistência eventual de banco de dados
- ✅ Propagação de cache
- ✅ Transições de máquina de estado

**Fique com expect.poll puro para:**

- Visibilidade simples de elementos de UI (use `expect(locator).toBeVisible()`)
- Verificações de propriedade única
- Casos onde logging não é necessário

## Fragmentos Relacionados

- `api-request.md` - Combinar para polling de endpoints de API
- `overview.md` - Padrões de composição de fixtures
- `fixtures-composition.md` - Usando com mergeTests

## Anti-Padrões

**❌ Usar waits fixos em vez de polling:**

```typescript
await page.click('#export');
await page.waitForTimeout(5000); // Wait arbitrário
expect(await page.textContent('#status')).toBe('Ready');
```

**✅ Poll pela condição real:**

```typescript
await page.click('#export');
await recurse(
  () => page.textContent('#status'),
  (status) => status === 'Ready',
  { timeout: 10000 },
);
```

**❌ Polling muito frequente:**

```typescript
await recurse(
  () => apiRequest({ method: 'GET', path: '/status' }),
  (res) => res.body.ready,
  { interval: 100 }, // Martela a API a cada 100ms!
);
```

**✅ Intervalo razoável para chamadas de API:**

```typescript
await recurse(
  () => apiRequest({ method: 'GET', path: '/status' }),
  (res) => res.body.ready,
  { interval: 2000 }, // Checa a cada 2 segundos (razoável)
);
```
