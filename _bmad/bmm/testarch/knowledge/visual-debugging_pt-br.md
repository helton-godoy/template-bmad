# Depuração Visual e Desenvolvimento Ergonómico

## Princípio

Loops de feedback rápido e artefatos transparentes de depuração são fundamentais para manter a confiabilidade do teste e confiança do desenvolvedor. Ferramentas de depuração visual (observadores de rastreamento, capturas de tela, vídeos, arquivos HAR) transformam falhas de teste criptografadas em insights acionáveis, reduzindo o tempo de triagem de horas para minutos.

## Racional

**The Problem**: Falhas de CI muitas vezes fornecem contexto mínimo — um tempo limite, um erro de seleção ou um erro de rede — obrigando os desenvolvedores a reproduzir problemas localmente (se puderem). Isso desperdiça tempo e desencoraja a manutenção do teste.

**A Solução**: Capture artefatos de depuração ricos **somente em falhas** para equilibrar os custos de armazenamento com valor diagnóstico. Ferramentas modernas como Playwright Trace Viewer, Cypress Debug UI e gravações HAR fornecem depuração interativa de viagens no tempo que revela exatamente o que o teste viu em cada passo.

**Por que isso importa**:

- Reduz o tempo de triagem de falhas em 80-90% (contexto visual vs logs somente)
- Activa a depuração sem reprodução local
- Melhora a confiança de manutenção do teste (causa raiz de falha clara)
- Condições de tempo de captura/corrida difíceis de reproduzir localmente

## Exemplos de padrões

### Exemplo 1: Configuração do Visualizador de Trace (Padrão de Produção)

**Contexto**: Capturar traços apenas na primeira repetição (equilibra armazenamento e diagnósticos)

**Implementation**:

```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    // Visual debugging artifacts (space-efficient)
    trace: 'on-first-retry', // Only when test fails once
    screenshot: 'only-on-failure', // Not on success
    video: 'retain-on-failure', // Delete on pass

    // Context for debugging
    baseURL: process.env.BASE_URL || 'http://localhost:3000',

    // Timeout context
    actionTimeout: 15_000, // 15s for clicks/fills
    navigationTimeout: 30_000, // 30s for page loads
  },

  // CI-specific artifact retention
  reporter: [
    ['html', { outputFolder: 'playwright-report', open: 'never' }],
    ['junit', { outputFile: 'results.xml' }],
    ['list'], // Console output
  ],

  // Failure handling
  retries: process.env.CI ? 2 : 0, // Retry in CI to capture trace
  workers: process.env.CI ? 1 : undefined,
});

```

**Abrir e usar o Visualizador de Trace**:

```bash

# After test failure in CI, download trace artifact

# Then open locally:
npx playwright show-trace path/to/trace.zip

# Or serve trace viewer:
npx playwright show-report

```

**Características chave para usar no visualizador de rastreamento**:

1. **Timeline**: Veja cada ação (clique, navegue, asserção) com timing
2. **Snapshots**: Hover sobre linha do tempo para ver o estado DOM naquele momento
3. **Rede Tab**: Inspecionar todas as chamadas de API, cabeçalhos, cargas, timing
4. **Console Tab**: Ver consola.log/error messages
5. **Fonte Tab**: Ver código de teste com marcadores de execução
6. **Metadata**: Navegador, SO, duração do teste, capturas de tela

**Por que isso funciona**:

- `on-first-retry` evita a captura de vestígios de passagens flácidas (armazenamento de salvas)
- Capturas de tela + vídeo dar contexto visual sem deixar rastros
- A linha do tempo interativa torna óbvios problemas de tempo (condições de corrida, API lenta)

---

### Exemplo 2: Gravação de arquivos HAR para depuração de rede

**Context**: Capture toda a atividade de rede para depuração de API reprodutível

**Implementation**:

```typescript
// tests/e2e/checkout-with-har.spec.ts
import { test, expect } from '@playwright/test';
import path from 'path';

test.describe('Checkout Flow with HAR Recording', () => {
  test('should complete payment with full network capture', async ({ page, context }) => {
    // Start HAR recording BEFORE navigation
    await context.routeFromHAR(path.join(__dirname, '../fixtures/checkout.har'), {
      url: '**/api/**', // Only capture API calls
      update: true, // Update HAR if file exists
    });

    await page.goto('/checkout');

    // Interact with page
    await page.getByTestId('payment-method').selectOption('credit-card');
    await page.getByTestId('card-number').fill('4242424242424242');
    await page.getByTestId('submit-payment').click();

    // Wait for payment confirmation
    await expect(page.getByTestId('success-message')).toBeVisible();

    // HAR file saved to fixtures/checkout.har
    // Contains all network requests/responses for replay
  });
});

```

**Usando HAR para o Mocking determinístico**:

«``typescript
// testes/e2e/checkout-replay-har.spec.ts
import { test, expect } de '@ playwright/test';
BMADPROTECT013End caminho de 'caminho';

ensaio('deve repetir o fluxo de saída de HAR', async ({ page, context }) => {
  // Replay network from HAR (no real API calls)
  await context.routeFromHAR(path.join(__dirname, '../fixtures/checkout.har'), {
    url: '**/api/**',
    update: false, // Read-only mode
  });

await page.goto('/checkout');

// Mesmo teste, mas as respostas de rede vêm do arquivo HAR
await page.getByTestId('método de pagamento').selectOption('cartão de crédito');
BMADPROTECT008End page.getByTestId('número-cartão').fill('4242424242424242');
BMADPROTECT007End page.g