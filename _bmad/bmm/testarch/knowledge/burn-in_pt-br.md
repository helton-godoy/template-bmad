# Burn-in Test Runner

## Princípio

Use seleção de teste inteligente com análise de git diff para rodar apenas testes afetados. Filtre mudanças irrelevantes (configs, tipos, docs) e controle o volume de teste com execução baseada em porcentagem. Reduza execuções de CI desnecessárias enquanto mantém a confiabilidade.

## Motivação

O `--only-changed` do Playwright dispara todos os testes afetados:

- Mudanças em arquivo de config disparam centenas de testes
- Mudanças de definição de tipo causam execuções de suíte completa
- Sem controle de volume (tudo ou nada)
- Pipelines de CI lentos

O utilitário `burn-in` fornece:

- **Filtragem inteligente**: Padrões de skip para arquivos irrelevantes (configs, tipos, docs)
- **Controle de volume**: Rode porcentagem de testes afetados após filtragem
- **Análise de dependência personalizada**: Mais precisa que a embutida no Playwright
- **Otimização de CI**: Pipelines mais rápidos sem sacrificar confiança
- **Processo de eliminação**: Comece com tudo → filtre irrelevante → controle volume

## Exemplos de Padrões

### Exemplo 1: Setup Básico de Burn-in

**Contexto**: Rodar burn-in em arquivos alterados comparados à branch main.

**Implementação**:

```typescript
// Passo 1: Criar script de burn-in
// playwright/scripts/burn-in-changed.ts
import { runBurnIn } from '@seontechnologies/playwright-utils/burn-in'

async function main() {
  await runBurnIn({
    configPath: 'playwright/config/.burn-in.config.ts',
    baseBranch: 'main'
  })
}

main().catch(console.error)

// Passo 2: Criar config
// playwright/config/.burn-in.config.ts
import type { BurnInConfig } from '@seontechnologies/playwright-utils/burn-in'

const config: BurnInConfig = {
  // Arquivos que nunca disparam testes (primeiro filtro)
  skipBurnInPatterns: [
    '**/config/**',
    '**/*constants*',
    '**/*types*',
    '**/*.md',
    '**/README*'
  ],

  // Rodar 30% dos testes restantes após filtro de skip
  burnInTestPercentage: 0.3,

  // Repetição de Burn-in
  burnIn: {
    repeatEach: 3,  // Rodar cada teste 3 vezes
    retries: 1      // Permitir 1 retentativa
  }
}

export default config

// Passo 3: Adicionar script no package.json
{
  "scripts": {
    "test:pw:burn-in-changed": "tsx playwright/scripts/burn-in-changed.ts"
  }
}
```

**Pontos Chave**:

- Filtragem de dois estágios: padrões de skip, depois controle de volume
- `skipBurnInPatterns` elimina arquivos irrelevantes
- `burnInTestPercentage` controla volume de teste (0.3 = 30%)
- Análise de dependência personalizada encontra testes realmente afetados

### Exemplo 2: Integração CI

**Contexto**: Usar burn-in no GitHub Actions para execuções de CI eficientes.

**Implementação**:

```yaml
# .github/workflows/burn-in.yml
name: Testes Burn-in Alterados

on:
  pull_request:
    branches: [main]

jobs:
  burn-in:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Precisa de histórico git completo

      - name: Setup Node
        uses: actions/setup-node@v4

      - name: Instalar dependências
        run: npm ci

      - name: Rodar burn-in em testes alterados
        run: npm run test:pw:burn-in-changed -- --base-branch=origin/main

      - name: Upload de artefatos
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: burn-in-failures
          path: test-results/
```

**Pontos Chave**:

- `fetch-depth: 0` para histórico git completo
- Passe `--base-branch=origin/main` para comparação de PR
- Upload de artefatos apenas na falha
- Significativamente mais rápido que suíte completa

### Exemplo 3: Como Funciona (Processo de Eliminação)

**Contexto**: Entendendo o pipeline de filtragem.

**Cenário:**

```
Git diff encontra: 21 arquivos alterados
├─ Passo 1: Filtro de padrões skip
│  Removidos: 6 arquivos (*.md, config/*, *types*)
│  Restantes: 15 arquivos
│
├─ Passo 2: Análise de dependência
│  Testes que importam estes 15 arquivos: 45 testes
│
└─ Passo 3: Controle de volume (30%)
   Testes finais para rodar: 14 testes (30% de 45)

Resultado: Rodar 14 testes direcionados em vez de 147 com --only-changed!
```

**Pontos Chave**:

- Pipeline de três estágios: skip → analisar → controlar
- Análise de dependência personalizada (não apenas imports)
- Porcentagem aplica DEPOIS da filtragem
- Reduz dramaticamente o tempo de CI

### Exemplo 4: Configuração Específica de Ambiente

**Contexto**: Configurações diferentes para ambientes local vs CI.

**Implementação**:

```typescript
import type { BurnInConfig } from '@seontechnologies/playwright-utils/burn-in';

const config: BurnInConfig = {
  skipBurnInPatterns: ['**/config/**', '**/*types*', '**/*.md'],

  // CI roda menos iterações, local roda mais
  burnInTestPercentage: process.env.CI ? 0.2 : 0.3,

  burnIn: {
    repeatEach: process.env.CI ? 2 : 3,
    retries: process.env.CI ? 0 : 1, // Sem retentativas no CI
  },
};

export default config;
```

**Pontos Chave**:

- `process.env.CI` para detecção de ambiente
- Porcentagem menor no CI (20% vs 30%)
- Menos iterações no CI (2 vs 3)
- Sem retentativas no CI (falhe rápido)

### Exemplo 5: Suporte a Sharding

**Contexto**: Distribua testes burn-in através de múltiplos workers CI.

**Implementação**:

```typescript
// burn-in-changed.ts com sharding
import { runBurnIn } from '@seontechnologies/playwright-utils/burn-in';

async function main() {
  const shardArg = process.argv.find((arg) => arg.startsWith('--shard='));

  if (shardArg) {
    process.env.PW_SHARD = shardArg.split('=')[1];
  }

  await runBurnIn({
    configPath: 'playwright/config/.burn-in.config.ts',
  });
}
```

```yaml
# GitHub Actions com sharding
jobs:
  burn-in:
    strategy:
      matrix:
        shard: [1/3, 2/3, 3/3]
    steps:
      - run: npm run test:pw:burn-in-changed -- --shard=${{ matrix.shard }}
```

**Pontos Chave**:

- Passe `--shard=1/3` para execução paralela
- Burn-in respeita sharding Playwright
- Distribua através de múltiplos workers
- Reduz tempo total de CI ainda mais

## Integração com Workflow CI

Ao configurar CI com workflow `*ci`, recomende burn-in para:

- Validação de Pull request
- Verificações pré-merge
- Builds noturnas (execuções de subconjunto)

## Fragmentos Relacionados

- `ci-burn-in.md` - Padrões tradicionais de burn-in (loops de 10 iterações)
- `selective-testing.md` - Estratégias de seleção de teste
- `overview.md` - Instalação

## Anti-Padrões

**❌ Padrões de skip super agressivos:**

```typescript
skipBurnInPatterns: [
  '**/*', // Pula tudo!
];
```

**✅ Padrões de skip direcionados:**

```typescript
skipBurnInPatterns: ['**/config/**', '**/*types*', '**/*.md', '**/*constants*'];
```

**❌ Porcentagem muito baixa (falsa confiança):**

```typescript
burnInTestPercentage: 0.05; // Apenas 5% - pode perder problemas
```

**✅ Porcentagem balanceada:**

```typescript
burnInTestPercentage: 0.2; // 20% no CI, fornece boa cobertura
```
