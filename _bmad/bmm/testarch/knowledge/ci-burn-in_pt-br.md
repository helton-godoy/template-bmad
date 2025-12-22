# Pipeline CI e estratégia de queima

## Princípio

Os pipelines CI devem executar testes de forma confiável, rápida e fornecer feedback claro. Testes de gravação (executando testes alterados várias vezes) elimina flakiness antes de mesclar. Trabalhos de palco estrategicamente: instale/cache uma vez, execute especificações alteradas primeiro para feedback rápido, em seguida, hard suites completas com falha-rápido desabilitado para preservar evidências.

## Racional

CI é o portão de qualidade para a produção. Um pipeline mal configurado desperdiça tempo de desenvolvimento (reação lenta, false positivos) ou envia código quebrado (false negativos, cobertura insuficiente). Testes de gravação garantem confiabilidade através de testes de estresse de código alterado, enquanto execução paralela e seleção de testes inteligentes otimizam a velocidade sem sacrificar a meticulosidade.

## Exemplos de padrões

### Exemplo 1: Fluxo de trabalho de ações do GitHub com execução paralela

**Contexto**: oleoduto CI/CD pronto para produção para testes E2E com caching, paralelização e teste de queima.

**Implementation**:

«```yaml

# .github/workflows/e2e-tests.yml
name: E2E Tests
on:
  pull_request:
  push:
branches: [principal, desenvolver]

env:
NODE_VERSION_FILE: '.nvmrc'
CACHE_KEY: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}

jobs:
dependências de instalação:
    name: Install & Cache Dependencies
runs-on: ubuntu-latest
Tempo limite de minutos: 10
    steps:
      - name: Código de saída
        uses: actions/checkout@ v4

      - name: Configuração Node.js
        uses: actions/setup-node@ v4
        with:
ficheiro de versão do nó: ${{ env.NODE_VERSION_FILE }}
cache: 'npm'

      - name: Módulos de nó de cache
        uses: actions/cache@ v4
        id: npm-cache
        with:
caminho: .
~/.npm
nó  módulo
~/.cache/Chipre
~/.cache/ms-playwright
chave: ${{ env.CACHE_KEY }}
restaurate-keys:

# {{ runner.os } # #

      - name: Instalar dependências
        if: steps.npm-cache.outputs.cache-hit!= 'true'
        run: npm ci -- prefer- offline -- no- audit

      - name: Instalar navegadores Playwright
        if: steps.npm-cache.outputs.cache-hit!= 'true'
        run: npx dramaturgo instalar -- with- deps cromo

Especificações do ensaio:
    name: Test Changed Specs First (Burn-In)
    needs: install-dependencies
runs-on: ubuntu-latest
Tempo- limite: 15
    steps:
      - name: Código de saída
        uses: actions/checkout@ v4
        with:
obter- profundidade: 0 # Histórico completo para diferenças precisas

      - name: Configuração Node.js
        uses: actions/setup-node@ v4
        with:
ficheiro de versão do nó: ${{ env.NODE_VERSION_FILE }}
cache: 'npm'

      - name: Restaurar dependências
        uses: actions/cache@ v4
        with:
caminho: .
~/.npm
nó  módulo
~/.cache/ms-playwright
chave: ${{ env.CACHE_KEY }}

      - name: Detecta ficheiros de teste alterados
        id: changed-tests
executar: □
CHANGED_SPECS=$(git diff --name-only origin/main...HEAD "! grep -E '\.(spec"test)\.(tsljsltsx'jsx)$' "! echo "")
eco "alterado specs=${CHANGED_SPECS}" >> $GITHUB_OUTPUT
Echo "Changed Specs: ${CHANGED_SPECS}"

      - name: Executar o burn-in em especificações alteradas (10 iterações)
        if: steps.changed-tests.outputs.changed specs != ''
executar: □
ESPECÍFICO="${{ steps.changed-tests.outputs.changed_specs }}"
eco "Burning-in: 10 iterações em especificações alteradas"
em {1..10};
eco "Burn-in iteração $i/10"
npm run test -- $SPECS
done
eco "✅ Burn-in passou - 10/10 execuções bem sucedidas"

      - name: Enviar os artefactos em caso de falha
        if: failure ()
        uses: actions/upload-artifact@ v4
        with:
          name: burn-in-failure-artifacts
caminho: .
resultados de ensaio/
relatório de dramaturgo/
imagens/
dias de retenção: 7

ensaio-e2e-sharded:
    name: E2E Tests (Shard ${{ matrix.shard }}/${{ strategy.job-total }})
needs: [install-dependências, test-changed-specs]
runs-on: ubuntu-latest
Tempo- limite: 30
    strategy:
fail-fast: false Correr todos os fragmentos mesmo que um falhe
      matrix:
cacos: [1, 2, 3, 4]
    steps:
      - name: Código de saída
        uses: actions/checkout@ v4

      - name: Configuração Node.js
        uses: actions/setup-node@ v4
        with:
ficheiro de versão do nó: ${{ env.NODE_VERSION_FILE }}
cache: 'npm'

      - name: Restaurar dependências
        uses: actions/cache@ v4
        with:
caminho: .
~/.npm
nó  módulo
~/.cache/ms-playwright
chave: ${{ env.CACHE_KEY }}

      - name: Execute testes E2E (hard ${{ matrix.shard }})
        run: npm run test:e2e ---shard=${{ matrix.shard }}/4
        env:
          TEST_ENV: staging
          CI: true

      - name: Enviar os resultados dos testes
        if: always ()
