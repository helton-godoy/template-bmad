# Utilitário de registo

## Princípio

Use o registro estruturado que se integra com os relatórios de teste da Playwright. Suporte ao registro de objetos, decoração de passo de teste e vários níveis de log (info, passo, sucesso, aviso, erro, depuração).

## Racional

Console.log em testes Playwright tem limitações:

- Não visível em relatórios HTML
- Sem integração do passo de teste
- Sem saída estruturada
- Perda de ruído terminal durante a IC

O utilitário `log` fornece:

- **Report integration**: Os logs aparecem em relatórios HTML da Playwright
- **Decoração de passo teste**: `log.step()` cria etapas desdobráveis em UI
- **Object loging**: Formata automaticamente objectos/arrays
- **Níveis múltiplos**: informação, passo, sucesso, aviso, erro, depuração
- **Console opcional**: Pode desativar a saída do console, mas manter registros de relatórios

## Exemplos de padrões

### Exemplo 1: Níveis Básicos de Registo

**Contexto**: Registre diferentes tipos de mensagens durante a execução do teste.

**Implementation**:

```typescript
import { log } from '@seontechnologies/playwright-utils';

test('logging demo', async ({ page }) => {
  await log.step('Navigate to login page');
  await page.goto('/login');

  await log.info('Entering credentials');
  await page.fill('#username', 'testuser');

  await log.success('Login successful');

  await log.warning('Rate limit approaching');

  await log.debug({ userId: '123', sessionId: 'abc' });

  // Errors still throw but get logged first
  try {
    await page.click('#nonexistent');
  } catch (error) {
    await log.error('Click failed', false); // false = no console output
    throw error;
  }
});

```

**Pontos-chave**

- `step()` cria passos desdobráveis em Playwright UI
- `info()`, `success()`, `warning()` para diferentes tipos de mensagens
- `debug()` para dados detalhados (objectos/arranjos)
- `error()` com supressão opcional do console
- Todos os registos aparecem nos relatórios de testes

### Exemplo 2: Object and Array Logging

**Contexto**: Registre dados estruturados para depuração sem o console de confusão.

**Implementation**:

```typescript
test('object logging', async ({ apiRequest }) => {
  const { body } = await apiRequest({
    method: 'GET',
    path: '/api/users',
  });

  // Log array of objects
  await log.debug(body); // Formatted as JSON in report

  // Log specific object
  await log.info({
    totalUsers: body.length,
    firstUser: body[0]?.name,
    timestamp: new Date().toISOString(),
  });

  // Complex nested structures
  await log.debug({
    request: {
      method: 'GET',
      path: '/api/users',
      timestamp: Date.now(),
    },
    response: {
      status: 200,
      body: body.slice(0, 3), // First 3 items
    },
  });
});

```

**Pontos-chave**

- Objetos auto-formatados como JSON bonito
- Arrays manuseados graciosamente
- Estruturas aninhadas suportadas
- Tudo visível nos anexos de relatório do Playwright

### Exemplo 3: Organização de Passo de Teste

**Contexto**: Organize a execução de testes em etapas colapsáveis para melhor legibilidade em relatórios.

**Implementation**:

```typescript
test('organized with steps', async ({ page, apiRequest }) => {
  await log.step('ARRANGE: Setup test data');
  const { body: user } = await apiRequest({
    method: 'POST',
    path: '/api/users',
    body: { name: 'Test User' },
  });

  await log.step('ACT: Perform user action');
  await page.goto(`/users/${user.id}`);
  await page.click('#edit');
  await page.fill('#name', 'Updated Name');
  await page.click('#save');

  await log.step('ASSERT: Verify changes');
  await expect(page.getByText('Updated Name')).toBeVisible();

  // In Playwright UI, each step is collapsible
});

```

**Pontos-chave**

- `log.step()` cria seções colapsáveis
- Organizar por Organizar- Act- Assert
- Passos visíveis no visualizador de rastreamento do Playwright
- Melhor depuração quando os testes falham

### Exemplo 4: Registo condicional

**Contexto**: Registar mensagens diferentes com base em condições de ambiente ou teste.

**Implementation**:

```typescript
test('conditional logging', async ({ page }) => {
  const isCI = process.env.CI === 'true';

  if (isCI) {
    await log.info('Running in CI environment');
  } else {
    await log.debug('Running locally');
  }

  const isKafkaWorking = await checkKafkaHealth();

  if (!isKafkaWorking) {
    await log.warning('Kafka unavailable - skipping event checks');
  } else {
    await log.step('Verifying Kafka events');
    // ... event verification
  }
});

```

**Pontos-chave**

- Registo baseado no ambiente
- Saltar o registo com condicional
- Usar níveis de log adequados
- Informações de depuração para local, mínimo para CI

### Exemplo 5: Integração com Auth e API

**Contexto**: Registre pedidos de API autenticados com tokens (seguro).

**Implementation**:

«``typescript
import { test } de '@seontechnologies/playwright-utils/fixtures';

// Ajudador para criar visualização segura do token
function createTokenPreview( token: string): string {
if (!token "!
BMADPROTECT021End log.info(`Using token: ${createTokenPreview(authToken)}`);

