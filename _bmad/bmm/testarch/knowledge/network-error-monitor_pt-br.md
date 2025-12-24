# Monitor de Erro de Rede

## Princípio

Automaticamente detecte e falhe testes quando erros HTTP 4xx/5xx ocorrerem durante a execução. Atue como um Sentry para testes - capture falhas silenciosas de backend mesmo quando a UI passa nas asserções.

## Motivação

Testes Playwright tradicionais focam na UI:

- Erros 500 de backend ignorados se a UI parecer correta
- Falhas silenciosas passam despercebidas
- Sem visibilidade da saúde da API de fundo
- Testes passam enquanto funcionalidades estão quebradas

O `network-error-monitor` fornece:

- **Detecção automática**: Todas as respostas HTTP 4xx/5xx rastreadas
- **Falhas de teste**: Falha testes com erros de backend (mesmo se UI passar)
- **Artefatos estruturados**: Relatórios JSON com detalhes de erro
- **Opt-out inteligente**: Desative para testes de validação esperando erros
- **Deduplicação**: Agrupe erros repetidos por padrão
- **Prevenção de efeito dominó**: Limite falhas de teste por padrão de erro

## Exemplos de Padrões

### Exemplo 1: Auto-Monitoramento Básico

**Contexto**: Automaticamente falhe testes quando erros de backend ocorrerem.

**Implementação**:

```typescript
import { test } from '@seontechnologies/playwright-utils/network-error-monitor/fixtures';

// Monitoramento automaticamente ativado
test('deve carregar dashboard', async ({ page }) => {
  await page.goto('/dashboard');
  await expect(page.locator('h1')).toContainText('Dashboard');

  // ✅ Passa se nenhum erro HTTP
  // ❌ Falha se quaisquer erros 4xx/5xx detectados com mensagem clara:
  //    "Network errors detected: 2 request(s) failed"
  //    Failed requests:
  //      GET 500 https://api.example.com/users
  //      POST 503 https://api.example.com/metrics
});
```

**Pontos Chave**:

- Zero setup - auto-ativado para todos os testes
- Falha em qualquer resposta 4xx/5xx
- Mensagem de erro estruturada com URLs e códigos de status
- Artefato JSON anexado ao relatório de teste

### Exemplo 2: Opt-Out para Testes de Validação

**Contexto**: Alguns testes esperam erros (validação, tratamento de erro, casos de borda).

**Implementação**:

```typescript
import { test } from '@seontechnologies/playwright-utils/network-error-monitor/fixtures';

// Opt-out com anotação
test('deve mostrar erro em entrada inválida', { annotation: [{ type: 'skipNetworkMonitoring' }] }, async ({ page }) => {
  await page.goto('/form');
  await page.click('#submit'); // Dispara erro 400

  // Monitoramento desativado - teste não falhará no 400
  await expect(page.getByText('Entrada inválida')).toBeVisible();
});

// Ou opt-out bloco describe inteiro
test.describe('tratamento de erro', { annotation: [{ type: 'skipNetworkMonitoring' }] }, () => {
  test('trata 404', async ({ page }) => {
    // Todos testes neste bloco pulam monitoramento
  });

  test('trata 500', async ({ page }) => {
    // Monitoramento desativado
  });
});
```

**Pontos Chave**:

- Use anotação `{ type: 'skipNetworkMonitoring' }`
- Pode fazer opt-out de teste único ou bloco describe inteiro
- Monitoramento ainda ativo para outros testes
- Perfeito para cenários de erro intencionais

### Exemplo 3: Integração com Fixtures Fundidas

**Contexto**: Combine network-error-monitor com outros utilitários.

**Implementação**:

```typescript
// playwright/support/merged-fixtures.ts
import { mergeTests } from '@playwright/test';
import { test as authFixture } from '@seontechnologies/playwright-utils/auth-session/fixtures';
import { test as networkErrorMonitorFixture } from '@seontechnologies/playwright-utils/network-error-monitor/fixtures';

export const test = mergeTests(
  authFixture,
  networkErrorMonitorFixture,
  // Adicione outras fixtures
);

// Em testes
import { test, expect } from '../support/merged-fixtures';

test('autenticado com monitoramento', async ({ page, authToken }) => {
  // Tanto auth quanto monitoramento de rede ativos
  await page.goto('/protected');

  // Falha se backend retornar erros durante fluxo auth
});
```

**Pontos Chave**:

- Combine com `mergeTests`
- Funciona junto com todos os outros utilitários
- Monitoramento ativo automaticamente
- Nenhum setup extra necessário

### Exemplo 4: Prevenção de Efeito Dominó

**Contexto**: Um endpoint falhando não deve falhar todos os testes.

**Implementação**:

```typescript
// Configuração (interna ao utilitário)
const config = {
  maxTestsPerError: 3, // Máx 3 testes falham por padrão de erro único
};

// Cenário:
// Teste 1: GET /api/broken → erro 500 → Teste falha ❌
// Teste 2: GET /api/broken → erro 500 → Teste falha ❌
// Teste 3: GET /api/broken → erro 500 → Teste falha ❌
// Teste 4: GET /api/broken → erro 500 → Teste passa ⚠️ (limite atingido, aviso logado)
// Teste 5: Padrão de erro diferente → Teste falha ❌ (novo padrão, contador reseta)
```

**Pontos Chave**:

- Limita falhas em cascata
- Agrupa erros por padrão URL + código de status
- Avisa quando limite atingido
- Previne backend instável de falhar suíte inteira

### Exemplo 5: Estrutura de Artefato

**Contexto**: Debugging de testes falhos com artefatos de erro de rede.

**Implementação**:

Quando teste falha devido a erros de rede, artefato anexado:

```json
// test-results/my-test/network-errors.json
{
  "errors": [
    {
      "url": "https://api.example.com/users",
      "method": "GET",
      "status": 500,
      "statusText": "Internal Server Error",
      "timestamp": "2024-08-13T10:30:45.123Z"
    },
    {
      "url": "https://api.example.com/metrics",
      "method": "POST",
      "status": 503,
      "statusText": "Service Unavailable",
      "timestamp": "2024-08-13T10:30:46.456Z"
    }
  ],
  "summary": {
    "totalErrors": 2,
    "uniquePatterns": 2
  }
}
```

**Pontos Chave**:

- Artefato JSON por teste falho
- Detalhes completos do erro (URL, método, status, timestamp)
- Estatísticas de sumário
- Debugging fácil com dados estruturados

## Comparação com Verificações de Erro Manuais

| Abordagem Manual                                       | network-error-monitor      |
| ------------------------------------------------------ | -------------------------- |
| `page.on('response', resp => { if (!resp.ok()) ... })` | Auto-ativado, zero setup   |
| Checar cada resposta manualmente                       | Automático para todas requisições |
| Lógica de rastreamento de erro customizada             | Deduplicação integrada     |
| Sem artefatos estruturados                             | Artefatos JSON anexados    |
| Fácil de esquecer                                      | Nunca perca um erro de backend |

## Quando Usar

**Auto-ativado para:**

- ✅ Todos testes E2E
- ✅ Testes de integração
- ✅ Qualquer teste acessando APIs reais

**Opt-out para:**

- ❌ Testes de validação (esperando 4xx)
- ❌ Testes de tratamento de erro (esperando 5xx)
- ❌ Testes offline (playback network-recorder)

## Integração com Setup de Framework

No workflow `*framework`, mencione network-error-monitor:

```typescript
// Adicionar ao merged-fixtures.ts
import { test as networkErrorMonitorFixture } from '@seontechnologies/playwright-utils/network-error-monitor/fixtures';

export const test = mergeTests(
  // ... outras fixtures
  networkErrorMonitorFixture,
);
```

## Fragmentos Relacionados

- `overview.md` - Instalação e fixtures
- `fixtures-composition.md` - Fusão com outros utilitários
- `error-handling.md` - Padrões tradicionais de tratamento de erro

## Anti-Padrões

**❌ Fazer opt-out de monitoramento globalmente:**

```typescript
// Todo teste pula monitoramento
test.use({ annotation: [{ type: 'skipNetworkMonitoring' }] });
```

**✅ Opt-out apenas para testes de erro específicos:**

```typescript
test.describe('cenários de erro', { annotation: [{ type: 'skipNetworkMonitoring' }] }, () => {
  // Apenas estes testes pulam monitoramento
});
```

**❌ Ignorar artefatos de erro de rede:**

```typescript
// Teste falha, artefato mostra erros 500
// Desenvolvedor: "Funciona na minha máquina" ¯\_(ツ)_/¯
```

**✅ Checar artefatos para causa raiz:**

```typescript
// Ler artefato network-errors.json
// Identificar endpoint falho: GET /api/users → 500
// Consertar problema de backend antes de mergear
```
