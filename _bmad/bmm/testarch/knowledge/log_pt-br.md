# Utilitário Log

## Princípio

Use logging estruturado que se integra com relatórios de teste Playwright. Suporte a log de objetos, decoração de passos de teste e múltiplos níveis de log (info, step, success, warning, error, debug).

## Motivação

Console.log em testes Playwright tem limitações:

- Não visível em relatórios HTML
- Sem integração com passo de teste
- Sem saída estruturada
- Perdido no ruído do terminal durante CI

O utilitário `log` fornece:

- **Integração de relatório**: Logs aparecem nos relatórios HTML Playwright
- **Decoração de passo de teste**: `log.step()` cria passos colapsáveis na UI
- **Log de objeto**: Formata automaticamente objetos/arrays
- **Múltiplos níveis**: info, step, success, warning, error, debug
- **Console opcional**: Pode desativar saída de console mas manter logs de relatório

## Exemplos de Padrões

### Exemplo 1: Níveis de Logging Básicos

**Contexto**: Logar diferentes tipos de mensagens durante a execução do teste.

**Implementação**:

```typescript
import { log } from '@seontechnologies/playwright-utils';

test('demo de logging', async ({ page }) => {
  await log.step('Navegar para página de login');
  await page.goto('/login');

  await log.info('Inserindo credenciais');
  await page.fill('#username', 'testuser');

  await log.success('Login bem-sucedido');

  await log.warning('Limite de taxa aproximando');

  await log.debug({ userId: '123', sessionId: 'abc' });

  // Erros ainda são lançados, mas logados primeiro
  try {
    await page.click('#nonexistent');
  } catch (error) {
    await log.error('Clique falhou', false); // false = sem saída de console
    throw error;
  }
});
```

**Pontos Chave**:

- `step()` cria passos colapsáveis na UI Playwright
- `info()`, `success()`, `warning()` para diferentes tipos de mensagem
- `debug()` para dados detalhados (objetos/arrays)
- `error()` com supressão opcional de console
- Todos os logs aparecem em relatórios de teste

### Exemplo 2: Log de Objeto e Array

**Contexto**: Logar dados estruturados para debugging sem poluir console.

**Implementação**:

```typescript
test('log de objeto', async ({ apiRequest }) => {
  const { body } = await apiRequest({
    method: 'GET',
    path: '/api/users',
  });

  // Logar array de objetos
  await log.debug(body); // Formatado como JSON no relatório

  // Logar objeto específico
  await log.info({
    totalUsers: body.length,
    firstUser: body[0]?.name,
    timestamp: new Date().toISOString(),
  });

  // Estruturas aninhadas complexas
  await log.debug({
    request: {
      method: 'GET',
      path: '/api/users',
      timestamp: Date.now(),
    },
    response: {
      status: 200,
      body: body.slice(0, 3), // Primeiros 3 itens
    },
  });
});
```

**Pontos Chave**:

- Objetos auto-formatados como JSON bonito
- Arrays tratados graciosamente
- Estruturas aninhadas suportadas
- Todos visíveis em anexos de relatório Playwright

### Exemplo 3: Organização de Passo de Teste

**Contexto**: Organizar execução de teste em passos colapsáveis para melhor legibilidade em relatórios.

**Implementação**:

```typescript
test('organizado com passos', async ({ page, apiRequest }) => {
  await log.step('ARRANGE: Setup de dados de teste');
  const { body: user } = await apiRequest({
    method: 'POST',
    path: '/api/users',
    body: { name: 'Test User' },
  });

  await log.step('ACT: Realizar ação de usuário');
  await page.goto(`/users/${user.id}`);
  await page.click('#edit');
  await page.fill('#name', 'Updated Name');
  await page.click('#save');

  await log.step('ASSERT: Verificar mudanças');
  await expect(page.getByText('Updated Name')).toBeVisible();

  // Na UI Playwright, cada passo é colapsável
});
```

**Pontos Chave**:

- `log.step()` cria seções colapsáveis
- Organize por Arrange-Act-Assert
- Passos visíveis no visualizador de trace Playwright
- Melhor debugging quando testes falham

### Exemplo 4: Logging Condicional

**Contexto**: Logar mensagens diferentes baseado em ambiente ou condições de teste.

**Implementação**:

```typescript
test('logging condicional', async ({ page }) => {
  const isCI = process.env.CI === 'true';

  if (isCI) {
    await log.info('Rodando em ambiente CI');
  } else {
    await log.debug('Rodando localmente');
  }

  const isKafkaWorking = await checkKafkaHealth();

  if (!isKafkaWorking) {
    await log.warning('Kafka indisponível - pulando verificações de evento');
  } else {
    await log.step('Verificando eventos Kafka');
    // ... verificação de evento
  }
});
```

**Pontos Chave**:

- Log baseado em ambiente
- Pular logging com condicionais
- Usar níveis de log apropriados
- Informação de debug para local, mínimo para CI

### Exemplo 5: Integração com Auth e API

**Contexto**: Logar requisições de API autenticadas com tokens (com segurança).

**Implementação**:

```typescript
import { test } from '@seontechnologies/playwright-utils/fixtures';

// Helper para criar preview seguro de token
function createTokenPreview(token: string): string {
  if (!token || token.length < 10) return '[inválido]';
  return `${token.slice(0, 6)}...${token.slice(-4)}`;
}

test('deve logar fluxo de auth', async ({ authToken, apiRequest }) => {
  await log.info(`Usando token: ${createTokenPreview(authToken)}`);

  await log.step('Buscar recurso protegido');
  const { status, body } = await apiRequest({
    method: 'GET',
    path: '/api/protected',
    headers: { Authorization: `Bearer ${authToken}` },
  });

  await log.debug({
    status,
    bodyPreview: {
      id: body.id,
      recordCount: body.data?.length,
    },
  });

  await log.success('Recurso protegido acessado com sucesso');
});
```

**Pontos Chave**:

- Nunca logar tokens completos (risco de segurança)
- Usar funções de preview para dados sensíveis
- Combinar com utilitários de auth e API
- Logar no nível de detalhe apropriado

## Guia de Níveis de Log

| Nível     | Quando Usar                         | Mostra no Relatório  | Mostra no Console |
| --------- | ----------------------------------- | -------------------- | ----------------- |
| `step`    | Organização de teste, ações maiores | ✅ Passos colapsáveis| ✅ Sim            |
| `info`    | Informação geral, mudanças de estado| ✅ Sim               | ✅ Sim            |
| `success` | Operações bem-sucedidas             | ✅ Sim               | ✅ Sim            |
| `warning` | Problemas não críticos, checks pulados| ✅ Sim             | ✅ Sim            |
| `error`   | Falhas, exceções                    | ✅ Sim               | ✅ Configurável   |
| `debug`   | Dados detalhados, objetos           | ✅ Sim (anexado)     | ✅ Configurável   |

## Comparação com console.log

| console.log             | Utilitário log            |
| ----------------------- | ------------------------- |
| Não em relatórios       | Aparece em relatórios     |
| Sem passos de teste     | Cria passos colapsáveis   |
| JSON.stringify() manual | Auto-formata objetos      |
| Sem níveis de log       | 6 níveis de log           |
| Perdido na saída CI     | Preservado em artefatos   |

## Fragmentos Relacionados

- `overview.md` - Uso básico e importações
- `api-request.md` - Logar requisições API
- `auth-session.md` - Logar fluxo auth (com segurança)
- `recurse.md` - Logar progresso de polling

## Anti-Padrões

**❌ Logar objetos em passos:**

```typescript
await log.step({ user: 'test', action: 'create' }); // Mostra vazio na UI
```

**✅ Use strings para passos, objetos para debug:**

```typescript
await log.step('Criando usuário: test'); // Legível na UI
await log.debug({ user: 'test', action: 'create' }); // Dados detalhados
```

**❌ Logar dados sensíveis:**

```typescript
await log.info(`Password: ${password}`); // Risco de segurança!
await log.info(`Token: ${authToken}`); // Token completo exposto!
```

**✅ Use previews ou omita dados sensíveis:**

```typescript
await log.info('Usuário autenticado com sucesso'); // Sem dados sensíveis
await log.debug({ tokenPreview: token.slice(0, 6) + '...' });
```

**❌ Logging excessivo em loops:**

```typescript
for (const item of items) {
  await log.info(`Processando ${item.id}`); // 100 entradas de log!
}
```

**✅ Logar sumário ou usar nível debug:**

```typescript
await log.step(`Processando ${items.length} itens`);
await log.debug({ itemIds: items.map((i) => i.id) }); // Uma entrada de log
```
