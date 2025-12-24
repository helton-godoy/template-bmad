# Guardrails de Configuração do Playwright

## Princípio

Carregue configs de ambiente via um mapa central (`envConfigMap`), padronize timeouts (ação 15s, navegação 30s, expect 10s, teste 60s), emita reporters HTML + JUnit, e armazene artefatos sob `test-results/` para upload de CI. Mantenha `.env.example`, `.nvmrc` e dependências de navegador versionadas para que execuções locais e de CI permaneçam alinhadas.

## Motivação

Configuração específica de ambiente previne que URLs, timeouts e credenciais hardcoded vazem para testes. Um mapa de config central com validação fail-fast captura ambientes ausentes cedo. Timeouts padronizados reduzem instabilidade enquanto permanecem longos o suficiente para condições de rede do mundo real. Armazenamento consistente de artefatos (`test-results/`, `playwright-report/`) permite que pipelines de CI façam upload de evidências de falha automaticamente. Dependências versionadas (`.nvmrc`, versões de navegador `package.json`) eliminam problemas de "funciona na minha máquina" entre ambientes local e CI.

## Exemplos de Padrões

### Exemplo 1: Configuração Baseada em Ambiente

**Contexto**: Ao testar contra múltiplos ambientes (local, staging, produção), use um mapa de config central que carrega configurações específicas de ambiente e falha rápido se `TEST_ENV` for inválido.

**Implementação**:

```typescript
// playwright.config.ts - Carregador central de config
import { config as dotenvConfig } from 'dotenv';
import path from 'path';

// Carregar .env da raiz do projeto
dotenvConfig({
  path: path.resolve(__dirname, '../../.env'),
});

// Mapa central de config de ambiente
const envConfigMap = {
  local: require('./playwright/config/local.config').default,
  staging: require('./playwright/config/staging.config').default,
  production: require('./playwright/config/production.config').default,
};

const environment = process.env.TEST_ENV || 'local';

// Falhar rápido se ambiente não suportado
if (!Object.keys(envConfigMap).includes(environment)) {
  console.error(`❌ Nenhuma configuração encontrada para ambiente: ${environment}`);
  console.error(`   Ambientes disponíveis: ${Object.keys(envConfigMap).join(', ')}`);
  process.exit(1);
}

console.log(`✅ Rodando testes contra: ${environment.toUpperCase()}`);

export default envConfigMap[environment as keyof typeof envConfigMap];
```

```typescript
// playwright/config/base.config.ts - Configuração base compartilhada
import { defineConfig } from '@playwright/test';
import path from 'path';

export const baseConfig = defineConfig({
  testDir: path.resolve(__dirname, '../tests'),
  outputDir: path.resolve(__dirname, '../../test-results'),
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [
    ['html', { outputFolder: 'playwright-report', open: 'never' }],
    ['junit', { outputFile: 'test-results/results.xml' }],
    ['list'],
  ],
  use: {
    actionTimeout: 15000,
    navigationTimeout: 30000,
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  globalSetup: path.resolve(__dirname, '../support/global-setup.ts'),
  timeout: 60000,
  expect: { timeout: 10000 },
});
```

```typescript
// playwright/config/local.config.ts - Ambiente local
import { defineConfig } from '@playwright/test';
import { baseConfig } from './base.config';

export default defineConfig({
  ...baseConfig,
  use: {
    ...baseConfig.use,
    baseURL: 'http://localhost:3000',
    video: 'off', // Sem vídeo localmente para velocidade
  },
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
    timeout: 120000,
  },
});
```

```typescript
// playwright/config/staging.config.ts - Ambiente staging
import { defineConfig } from '@playwright/test';
import { baseConfig } from './base.config';

export default defineConfig({
  ...baseConfig,
  use: {
    ...baseConfig.use,
    baseURL: 'https://staging.example.com',
    ignoreHTTPSErrors: true, // Permitir certificados auto-assinados em staging
  },
});
```

```typescript
// playwright/config/production.config.ts - Ambiente produção
import { defineConfig } from '@playwright/test';
import { baseConfig } from './base.config';

export default defineConfig({
  ...baseConfig,
  retries: 3, // Mais retentativas em produção
  use: {
    ...baseConfig.use,
    baseURL: 'https://example.com',
    video: 'on', // Sempre gravar falhas de produção
  },
});
```

```bash
# .env.example - Modelo para desenvolvedores
TEST_ENV=local
API_KEY=sua_chave_api_aqui
DATABASE_URL=postgresql://localhost:5432/test_db
```

**Pontos Chave**:

- `envConfigMap` central previne má configuração de ambiente
- Validação fail-fast com mensagem de erro clara (envs disponíveis listados)
- Config base define configurações compartilhadas, configs de ambiente sobrescrevem
- `.env.example` fornece modelo para segredos necessários
- `TEST_ENV=local` como padrão para desenvolvimento local
- Config de produção aumenta retentativas e habilita gravação de vídeo

### Exemplo 2: Padrões de Timeout

**Contexto**: Quando testes falham devido a configurações de timeout inconsistentes, padronize timeouts em todos os testes: ação 15s, navegação 30s, expect 10s, teste 60s. Exponha overrides através de fixtures em vez de literais inline.

**Implementação**:

```typescript
// playwright/config/base.config.ts - Timeouts padronizados
import { defineConfig } from '@playwright/test';

export default defineConfig({
  // Timeout global de teste: 60 segundos
  timeout: 60000,

  use: {
    // Timeout de ação: 15 segundos (click, fill, etc.)
    actionTimeout: 15000,

    // Timeout de navegação: 30 segundos (page.goto, page.reload)
    navigationTimeout: 30000,
  },

  // Timeout de expect: 10 segundos (todas asserções)
  expect: {
    timeout: 10000,
  },
});
```

```typescript
// playwright/support/fixtures/timeout-fixture.ts - Fixture de override de timeout
import { test as base } from '@playwright/test';

type TimeoutOptions = {
  extendedTimeout: (timeoutMs: number) => Promise<void>;
};

export const test = base.extend<TimeoutOptions>({
  extendedTimeout: async ({}, use, testInfo) => {
    const originalTimeout = testInfo.timeout;

    await use(async (timeoutMs: number) => {
      testInfo.setTimeout(timeoutMs);
    });

    // Restaurar timeout original após teste
    testInfo.setTimeout(originalTimeout);
  },
});

export { expect } from '@playwright/test';
```

```typescript
// Uso em testes - Timeouts padrão (implícito)
import { test, expect } from '@playwright/test';

test('usuário pode logar', async ({ page }) => {
  await page.goto('/login'); // Usa timeout de navegação 30s
  await page.fill('[data-testid="email"]', 'test@example.com'); // Usa timeout de ação 15s
  await page.click('[data-testid="login-button"]'); // Usa timeout de ação 15s

  await expect(page.getByText('Bem-vindo')).toBeVisible(); // Usa timeout de expect 10s
});
```

```typescript
// Uso em testes - Override de timeout por teste
import { test, expect } from '../support/fixtures/timeout-fixture';

test('operação de processamento de dados lenta', async ({ page, extendedTimeout }) => {
  // Sobrescrever timeout padrão de 60s para este teste lento
  await extendedTimeout(180000); // 3 minutos

  await page.goto('/data-processing');
  await page.click('[data-testid="process-large-file"]');

  // Aguardar operação de longa duração
  await expect(page.getByText('Processamento completo')).toBeVisible({
    timeout: 120000, // 2 minutos para asserção
  });
});
```

```typescript
// Override de timeout por asserção (inline)
test('API retorna rapidamente', async ({ page }) => {
  await page.goto('/dashboard');

  // Sobrescrever timeout de expect para API rápida (reduzir detecção de instabilidade)
  await expect(page.getByTestId('user-name')).toBeVisible({ timeout: 5000 }); // 5s em vez de 10s

  // Sobrescrever timeout de expect para API externa lenta
  await expect(page.getByTestId('weather-widget')).toBeVisible({ timeout: 20000 }); // 20s em vez de 10s
});
```

**Pontos Chave**:

- **Timeouts padronizados**: ação 15s, navegação 30s, expect 10s, teste 60s (padrões globais)
- Override baseado em fixture (`extendedTimeout`) para testes lentos (preferido sobre inline)
- Override de timeout por asserção via opção `{ timeout: X }` (use com moderação)
- Evite esperas fixas (`page.waitForTimeout(3000)`) - use esperas baseadas em evento
- Ambientes CI podem precisar de timeouts mais longos (trate em config específica de ambiente)

### Exemplo 3: Configuração de Saída de Artefato

**Contexto**: Ao debugar falhas em CI, configure artefatos (screenshots, vídeos, traces, relatórios HTML) para serem capturados na falha e armazenados em locais consistentes para upload.

**Implementação**:

```typescript
// playwright.config.ts - Configuração de artefato
import { defineConfig } from '@playwright/test';
import path from 'path';

export default defineConfig({
  // Diretório de saída para artefatos de teste
  outputDir: path.resolve(__dirname, './test-results'),

  use: {
    // Screenshot apenas na falha (economiza espaço)
    screenshot: 'only-on-failure',

    // Gravação de vídeo na falha + retentativa
    video: 'retain-on-failure',

    // Gravação de trace na primeira retentativa (melhor dado de debugging)
    trace: 'on-first-retry',
  },

  reporter: [
    // Relatório HTML (visual, interativo)
    [
      'html',
      {
        outputFolder: 'playwright-report',
        open: 'never', // Não auto-abrir em CI
      },
    ],

    // JUnit XML (integração CI)
    [
      'junit',
      {
        outputFile: 'test-results/results.xml',
      },
    ],

    // Reporter de lista (saída de console)
    ['list'],
  ],
});
```

```typescript
// playwright/support/fixtures/artifact-fixture.ts - Captura de artefato customizada
import { test as base } from '@playwright/test';
import fs from 'fs';
import path from 'path';

export const test = base.extend({
  // Auto-capturar logs de console na falha
  page: async ({ page }, use, testInfo) => {
    const logs: string[] = [];

    page.on('console', (msg) => {
      logs.push(`[${msg.type()}] ${msg.text()}`);
    });

    await use(page);

    // Salvar logs na falha
    if (testInfo.status !== testInfo.expectedStatus) {
      const logsPath = path.join(testInfo.outputDir, 'console-logs.txt');
      fs.writeFileSync(logsPath, logs.join('\n'));
      testInfo.attachments.push({
        name: 'console-logs',
        contentType: 'text/plain',
        path: logsPath,
      });
    }
  },
});
```

```yaml
# .github/workflows/e2e.yml - Upload de artefato CI
name: Testes E2E
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version-file: '.nvmrc'

      - name: Instalar dependências
        run: npm ci

      - name: Instalar browsers Playwright
        run: npx playwright install --with-deps

      - name: Rodar testes
        run: npm run test
        env:
          TEST_ENV: staging

      # Upload de artefatos de teste na falha
      - name: Upload de resultados de teste
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: test-results
          path: test-results/
          retention-days: 30

      - name: Upload de relatório Playwright
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 30
```

```typescript
// Exemplo: Screenshot customizado em condição específica
test('capturar screenshot em erro específico', async ({ page }) => {
  await page.goto('/checkout');

  try {
    await page.click('[data-testid="submit-payment"]');
    await expect(page.getByText('Pedido Confirmado')).toBeVisible();
  } catch (error) {
    // Capturar screenshot customizado com timestamp
    await page.screenshot({
      path: `test-results/payment-error-${Date.now()}.png`,
      fullPage: true,
    });
    throw error;
  }
});
```

**Pontos Chave**:

- `screenshot: 'only-on-failure'` economiza espaço (não todo teste)
- `video: 'retain-on-failure'` captura fluxo completo em falhas
- `trace: 'on-first-retry'` fornece dados profundos de debugging (rede, DOM, console)
- Relatório HTML em `playwright-report/` (debugging visual)
- XML JUnit em `test-results/results.xml` (integração CI)
- CI faz upload de artefatos na falha com retenção de 30 dias
- Fixture customizada pode capturar logs de console, logs de rede, etc.

### Exemplo 4: Configuração de Paralelização

**Contexto**: Quando testes rodam lentamente em CI, configure paralelização com contagem de worker, sharding e execução totalmente paralela para maximizar velocidade enquanto mantém estabilidade.

**Implementação**:

```typescript
// playwright.config.ts - Configurações de paralelização
import { defineConfig } from '@playwright/test';
import os from 'os';

export default defineConfig({
  // Rodar testes em paralelo dentro de único arquivo
  fullyParallel: true,

  // Configuração de worker
  workers: process.env.CI
    ? 1 // Serial em CI para estabilidade (ou 2 para CI mais rápido)
    : os.cpus().length - 1, // Paralelo localmente (deixar 1 CPU para OS)

  // Prevenir .only() acidentalmente commitado de bloquear CI
  forbidOnly: !!process.env.CI,

  // Tentar novamente testes falhos em CI
  retries: process.env.CI ? 2 : 0,

  // Configuração de shard (dividir testes através de múltiplas máquinas)
  shard:
    process.env.SHARD_INDEX && process.env.SHARD_TOTAL
      ? {
          current: parseInt(process.env.SHARD_INDEX, 10),
          total: parseInt(process.env.SHARD_TOTAL, 10),
        }
      : undefined,
});
```

```yaml
# .github/workflows/e2e-parallel.yml - Execução CI com sharding
name: Testes E2E (Paralelo)
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        shard: [1, 2, 3, 4] # Dividir testes através de 4 máquinas
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version-file: '.nvmrc'

      - name: Instalar dependências
        run: npm ci

      - name: Instalar browsers Playwright
        run: npx playwright install --with-deps

      - name: Rodar testes (shard ${{ matrix.shard }})
        run: npm run test
        env:
          SHARD_INDEX: ${{ matrix.shard }}
          SHARD_TOTAL: 4
          TEST_ENV: staging

      - name: Upload resultados de teste
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: test-results-shard-${{ matrix.shard }}
          path: test-results/
```

```typescript
// playwright/config/serial.config.ts - Execução serial para testes instáveis
import { defineConfig } from '@playwright/test';
import { baseConfig } from './base.config';

export default defineConfig({
  ...baseConfig,

  // Desativar execução paralela
  fullyParallel: false,
  workers: 1,

  // Usado para: fluxos de autenticação, testes dependentes de banco de dados, testes de feature flag
});
```

```typescript
// Uso: Forçar execução serial para testes específicos
import { test } from '@playwright/test';

// Execução serial para testes de auth (estado de sessão compartilhado)
test.describe.configure({ mode: 'serial' });

test.describe('Fluxo de Autenticação', () => {
  test('usuário pode logar', async ({ page }) => {
    // Primeiro teste em bloco serial
  });

  test('usuário pode acessar dashboard', async ({ page }) => {
    // Depende do teste anterior (serial)
  });
});
```

```typescript
// Uso: Execução paralela para testes independentes (padrão)
import { test } from '@playwright/test';

test.describe('Catálogo de Produto', () => {
  test('pode ver produto 1', async ({ page }) => {
    // Roda em paralelo com outros testes
  });

  test('pode ver produto 2', async ({ page }) => {
    // Roda em paralelo com outros testes
  });
});
```

**Pontos Chave**:

- `fullyParallel: true` habilita execução paralela dentro de único arquivo de teste
- Workers: 1 em CI (estabilidade), N-1 CPUs localmente (velocidade)
- Sharding divide testes através de múltiplas máquinas CI (4x mais rápido com 4 shards)
- `test.describe.configure({ mode: 'serial' })` para testes dependentes
- `forbidOnly: true` em CI previne `.only()` de bloquear pipeline
- Estratégia de matriz em CI roda shards concorrentemente

### Exemplo 5: Configuração de Projeto

**Contexto**: Ao testar através de múltiplos navegadores, dispositivos ou configurações, use projetos Playwright para rodar os mesmos testes contra diferentes ambientes (chromium, firefox, webkit, mobile).

**Implementação**:

```typescript
// playwright.config.ts - Múltiplos projetos de navegador
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  projects: [
    // Browsers Desktop
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },

    // Browsers Mobile
    {
      name: 'mobile-chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'mobile-safari',
      use: { ...devices['iPhone 13'] },
    },

    // Tablet
    {
      name: 'tablet',
      use: { ...devices['iPad Pro'] },
    },
  ],
});
```

```typescript
// playwright.config.ts - Projetos autenticados vs. não autenticados
import { defineConfig } from '@playwright/test';
import path from 'path';

export default defineConfig({
  projects: [
    // Projeto de setup (roda primeiro, cria estado de auth)
    {
      name: 'setup',
      testMatch: /global-setup\.ts/,
    },

    // Testes autenticados (reutilizam estado de auth)
    {
      name: 'authenticated',
      dependencies: ['setup'],
      use: {
        storageState: path.resolve(__dirname, './playwright/.auth/user.json'),
      },
      testMatch: /.*authenticated\.spec\.ts/,
    },

    // Testes não autenticados (páginas públicas)
    {
      name: 'unauthenticated',
      testMatch: /.*unauthenticated\.spec\.ts/,
    },
  ],
});
```

```typescript
// playwright/support/global-setup.ts - Projeto de setup para auth
import { chromium, FullConfig } from '@playwright/test';
import path from 'path';

async function globalSetup(config: FullConfig) {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Realizar autenticação
  await page.goto('http://localhost:3000/login');
  await page.fill('[data-testid="email"]', 'test@example.com');
  await page.fill('[data-testid="password"]', 'password123');
  await page.click('[data-testid="login-button"]');

  // Aguardar autenticação completar
  await page.waitForURL('**/dashboard');

  // Salvar estado de autenticação
  await page.context().storageState({
    path: path.resolve(__dirname, '../.auth/user.json'),
  });

  await browser.close();
}

export default globalSetup;
```

```bash
# Rodar projeto específico
npx playwright test --project=chromium
npx playwright test --project=mobile-chrome
npx playwright test --project=authenticated

# Rodar múltiplos projetos
npx playwright test --project=chromium --project=firefox

# Rodar todos projetos (padrão)
npx playwright test
```

```typescript
// Uso: Teste específico de projeto
import { test, expect } from '@playwright/test';

test('navegação mobile funciona', async ({ page, isMobile }) => {
  await page.goto('/');

  if (isMobile) {
    // Abrir menu mobile
    await page.click('[data-testid="hamburger-menu"]');
  }

  await page.click('[data-testid="products-link"]');
  await expect(page).toHaveURL(/.*products/);
});
```

```yaml
# .github/workflows/e2e-cross-browser.yml - Teste cross-browser CI
name: Testes E2E (Cross-Browser)
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        project: [chromium, firefox, webkit, mobile-chrome]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npx playwright install --with-deps

      - name: Rodar testes (${{ matrix.project }})
        run: npx playwright test --project=${{ matrix.project }}
```

**Pontos Chave**:

- Projetos permitem testar através de browsers, dispositivos e configurações
- `devices` do `@playwright/test` fornecem configurações pré-definidas (Pixel 5, iPhone 13, etc.)
- `dependencies` garante que projeto de setup rode primeiro (auth, semeadura de dados)
- `storageState` compartilha autenticação através de testes (0 segundos auth por teste)
- `testMatch` filtra quais testes rodam em qual projeto
- Estratégia de matriz CI roda projetos em paralelo (4x mais rápido com 4 projetos)
- Propriedade de contexto `isMobile` para lógica condicional em testes

## Pontos de Integração

- **Usado em workflows**: `*framework` (setup de config), `*ci` (paralelização, upload de artefato)
- **Fragmentos relacionados**:
  - `fixture-architecture.md` - Overrides de timeout baseados em fixture
  - `ci-burn-in.md` - Upload de artefato de pipeline CI
  - `test-quality.md` - Padrões de timeout (sem esperas fixas)
  - `data-factories.md` - Isolamento por teste (sem estado global compartilhado)

## Checklist de Configuração

**Antes de implantar testes, verifique**:

- [ ] Mapa de config de ambiente com validação fail-fast
- [ ] Timeouts padronizados (ação 15s, navegação 30s, expect 10s, teste 60s)
- [ ] Armazenamento de artefato em `test-results/` e `playwright-report/`
- [ ] Reporters HTML + JUnit configurados
- [ ] `.env.example`, `.nvmrc`, versões de browser commitadas
- [ ] Paralelização configurada (workers, sharding)
- [ ] Projetos definidos para teste cross-browser/dispositivo (se necessário)
- [ ] CI faz upload de artefatos na falha com retenção de 30 dias

_Fonte: Repo do livro Playwright, exemplo de configuração SEON, filosofia de teste Murat (linhas 216-271)._
