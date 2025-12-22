# Monitor de Erros de Rede

## Princípio

Detecte automaticamente e falhe testes quando erros HTTP 4xx/5xx ocorrem durante a execução. Aja como Sentry para testes - capture falhas silenciosas da infra-estrutura mesmo quando a UI passa as afirmações.

## Racional

Testes tradicionais de dramaturgo focam na UI:

- Infraestrutura 500 erros ignorados se UI parece correto
- Falhas silenciosas passam
- Sem visibilidade na saúde API de fundo
- Os testes passam enquanto os recursos são quebrados

O `network-error-monitor` fornece:

- **Detecção automática**: Todas as respostas HTTP 4xx/5xx
- **Falhas de teste**: Falha nos testes com erros de infra-estrutura (mesmo que a UI passe)
- **Artefatos estruturados**: JSON relata com detalhes de erro
- **Smart opt-out**: Desactivação para testes de validação à espera de erros
- **Deduplication**: Grupo de erros repetidos por padrão
- **Prevenção do efeito dominó**: Falhas de teste limite por padrão de erro

## Exemplos de padrões

### Exemplo 1: Monitoramento Automático Básico

**Contexto**: Falha automaticamente nos testes quando ocorrem erros na infra-estrutura.

**Implementation**:

```typescript
import { test } from '@seontechnologies/playwright-utils/network-error-monitor/fixtures';

// Monitoring automatically enabled
test('should load dashboard', async ({ page }) => {
  await page.goto('/dashboard');
  await expect(page.locator('h1')).toContainText('Dashboard');

  // ✅ Passes if no HTTP errors
  // ❌ Fails if any 4xx/5xx errors detected with clear message:
  //    "Network errors detected: 2 request(s) failed"
  //    Failed requests:
  //      GET 500 https://api.example.com/users
  //      POST 503 https://api.example.com/metrics
});

```

**Pontos-chave**

- Configuração zero - habilitado automaticamente para todos os testes
- Falha em qualquer resposta de 4xx/5xx
- Mensagem de erro estruturada com URLs e códigos de status
- Artefacto JSON ligado ao relatório de teste

### Exemplo 2: Opt-Out for Validation Tests

**Contexto**: Alguns testes esperam erros (validação, manipulação de erros, casos de borda).

**Implementation**:

```typescript
import { test } from '@seontechnologies/playwright-utils/network-error-monitor/fixtures';

// Opt-out with annotation
test('should show error on invalid input', { annotation: [{ type: 'skipNetworkMonitoring' }] }, async ({ page }) => {
  await page.goto('/form');
  await page.click('#submit'); // Triggers 400 error

  // Monitoring disabled - test won't fail on 400
  await expect(page.getByText('Invalid input')).toBeVisible();
});

// Or opt-out entire describe block
test.describe('error handling', { annotation: [{ type: 'skipNetworkMonitoring' }] }, () => {
  test('handles 404', async ({ page }) => {
    // All tests in this block skip monitoring
  });

  test('handles 500', async ({ page }) => {
    // Monitoring disabled
  });
});

```

**Pontos-chave**

- Utilizar anotação `{ type: 'skipNetworkMonitoring' }`
- Pode opt-out único teste ou bloco de descrição inteiro
- Monitoramento ainda ativo para outros testes
- Perfeito para cenários de erro intencional

### Exemplo 3: Integração com acessórios fundidos

**Contexto**: Combine rede-erro-monitor com outros utilitários.

**Implementation**:

```typescript
// playwright/support/merged-fixtures.ts
import { mergeTests } from '@playwright/test';
import { test as authFixture } from '@seontechnologies/playwright-utils/auth-session/fixtures';
import { test as networkErrorMonitorFixture } from '@seontechnologies/playwright-utils/network-error-monitor/fixtures';

export const test = mergeTests(
  authFixture,
  networkErrorMonitorFixture,
  // Add other fixtures
);

// In tests
import { test, expect } from '../support/merged-fixtures';

test('authenticated with monitoring', async ({ page, authToken }) => {
  // Both auth and network monitoring active
  await page.goto('/protected');

  // Fails if backend returns errors during auth flow
});

```

**Pontos-chave**

- Combine com `mergeTests`
- Funciona ao lado de todos os outros utilitários
- Monitoramento ativo automaticamente
- Não há necessidade de instalação extra

### Exemplo 4: Prevenção de Efeito Domino

**Contexto**: Um endpoint falhante não deve falhar todos os testes.

**Implementation**:

```typescript
// Configuration (internal to utility)
const config = {
  maxTestsPerError: 3, // Max 3 tests fail per unique error pattern
};

// Scenario:
// Test 1: GET /api/broken → 500 error → Test fails ❌
// Test 2: GET /api/broken → 500 error → Test fails ❌
// Test 3: GET /api/broken → 500 error → Test fails ❌
// Test 4: GET /api/broken → 500 error → Test passes ⚠️ (limit reached, warning logged)
// Test 5: Different error pattern → Test fails ❌ (new pattern, counter resets)

```

**Pontos-chave**

- Limita falhas em cascata
- Grupos de erros por URL + padrão de código de estado
- Avisa quando o limite for atingido
- Evita que a infra- estrutura flácida falhe em toda a suite

### Exemplo 5: Estrutura do artefato

**Contexto**: Testes de depuração falhou com artefatos de erro de rede.

**Implementation**:

Quando o teste falha devido a erros de rede, o artefato anexado:

```json
// test-results/my-test/network-errors.json
{
"erros": [
{
"url": "https://api.example.com/users",
"método": "GET",
"Estatuto": 500,
