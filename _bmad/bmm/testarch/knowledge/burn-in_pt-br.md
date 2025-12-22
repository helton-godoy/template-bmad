# Execução de Testes em Queimadura

## Princípio

Use a seleção de testes inteligente com análise git diff para executar apenas testes afetados. Filtrar alterações irrelevantes (configurações, tipos, documentos) e controlar o volume de teste com execução baseada em porcentagem. Reduza o IC desnecessário enquanto mantém a confiabilidade.

## Racional

`--only-changed` do dramaturgo dispara todos os testes afetados:

- Mudanças de arquivos de configuração desencadeiam centenas de testes
- Mudanças de definição de tipo causam corridas completas
- Sem controle de volume (tudo ou nada)
- Oleodutos CI lentos

O utilitário `burn-in` fornece:

- **Filtragem inteligente**: Ignorar padrões para arquivos irrelevantes (configurações, tipos, documentos)
- **Controlo de volume**: Percentagem de ensaios afectados após filtragem
- **Análise de dependência personalizada**: mais preciso do que o incorporado pela Playwright
- **Optimização CI**: gasodutos mais rápidos sem sacrificar a confiança
- **Processo de eliminação**: Comece com todos → filtro irrelevante → volume de controle

## Exemplos de padrões

### Exemplo 1: Configuração básica de gravação

**Contexto**: Executar o burn-in em arquivos alterados em comparação com o branch principal.

**Implementation**:

```typescript
// Step 1: Create burn-in script
// playwright/scripts/burn-in-changed.ts
import { runBurnIn } from '@seontechnologies/playwright-utils/burn-in'

async function main() {
  await runBurnIn({
    configPath: 'playwright/config/.burn-in.config.ts',
    baseBranch: 'main'
  })
}

main().catch(console.error)

// Step 2: Create config
// playwright/config/.burn-in.config.ts
import type { BurnInConfig } from '@seontechnologies/playwright-utils/burn-in'

const config: BurnInConfig = {
  // Files that never trigger tests (first filter)
  skipBurnInPatterns: [
    '**/config/**',
    '**/*constants*',
    '**/*types*',
    '**/*.md',
    '**/README*'
  ],

  // Run 30% of remaining tests after skip filter
  burnInTestPercentage: 0.3,

  // Burn-in repetition
  burnIn: {
    repeatEach: 3,  // Run each test 3 times
    retries: 1      // Allow 1 retry
  }
}

export default config

// Step 3: Add package.json script
{
  "scripts": {
    "test:pw:burn-in-changed": "tsx playwright/scripts/burn-in-changed.ts"
  }
}

```

**Pontos-chave**

- Filtragem em dois estágios: pular padrões, em seguida, controle de volume
- `skipBurnInPatterns` elimina arquivos irrelevantes
- `burnInTestPercentage` controla o volume do teste (0,3 = 30%)
- Análise de dependência personalizada encontra testes realmente afetados

### Exemplo 2: Integração CI

**Contexto**: Use o burn-in em ações do GitHub para executar CI eficiente.

**Implementation**:

```yaml

# .github/workflows/burn-in.yml
name: Burn-in Changed Tests

on:
  pull_request:
    branches: [main]

jobs:
  burn-in:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Need git history

      - name: Setup Node
        uses: actions/setup-node@v4

      - name: Install dependencies
        run: npm ci

      - name: Run burn-in on changed tests
        run: npm run test:pw:burn-in-changed -- --base-branch=origin/main

      - name: Upload artifacts
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: burn-in-failures
          path: test-results/

```

**Pontos-chave**

- `fetch-depth: 0` para o histórico git completo
- Passar `--base-branch=origin/main` para comparação PR
- Enviar os artefactos apenas em caso de falha
- Significativamente mais rápido do que a suite completa

### Exemplo 3: Como Funciona (Processo de Eliminação)

**Contexto**: Compreender o gasoduto de filtragem.

**Cenário:**

```
Git diff finds: 21 changed files
├─ Step 1: Skip patterns filter
│  Removed: 6 files (*.md, config/*, *types*)
│  Remaining: 15 files
│
├─ Step 2: Dependency analysis
│  Tests that import these 15 files: 45 tests
│
└─ Step 3: Volume control (30%)
   Final tests to run: 14 tests (30% of 45)

Result: Run 14 targeted tests instead of 147 with --only-changed!

```

**Pontos-chave**

- Oleoduto de três estágios: skip → analisar → controle
- Análise de dependência personalizada (não apenas importações)
- Percentagem aplicável após a filtragem
- Reduz dramaticamente o tempo de IC

### Exemplo 4: Configuração específica do ambiente

**Contexto**: Configurações diferentes para ambientes locais vs CI.

**Implementation**:

```typescript
import type { BurnInConfig } from '@seontechnologies/playwright-utils/burn-in';

const config: BurnInConfig = {
  skipBurnInPatterns: ['**/config/**', '**/*types*', '**/*.md'],

  // CI runs fewer iterations, local runs more
  burnInTestPercentage: process.env.CI ? 0.2 : 0.3,

  burnIn: {
    repeatEach: process.env.CI ? 2 : 3,
    retries: process.env.CI ? 0 : 1, // No retries in CI
  },
};

export default config;

```

**Pontos-chave**

- `process.env.CI` para detecção do ambiente
- Percentagem mais baixa na IC (20% vs 30%)
- Menos iterações na IC (2 vs 3)
- Nenhuma repetição na IC (falha rápida)

### Exemplo 5: Suporte de Revestimento

**Contexto**: Distribuir testes de burn-in em vários trabalhadores CI.

**Implementation**:

«``typescript
// burn-in-changed.ts com raspagem
import BMADPROTECT019End de '@seontechnologies/playwright-utils/burn-in';

async function main ()