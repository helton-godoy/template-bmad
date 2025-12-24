# Pipeline CI e Estratégia de Burn-In

## Princípio

Pipelines de CI devem executar testes de forma confiável, rápida e fornecer feedback claro. Testes de burn-in (rodar testes alterados múltiplas vezes) eliminam a instabilidade antes do merge. Estagie jobs estrategicamente: instale/cacheie uma vez, execute specs alterados primeiro para feedback rápido, depois divida suítes completas em shards com fail-fast desativado para preservar evidências.

## Motivação

CI é o portão de qualidade para produção. Um pipeline mal configurado desperdiça tempo do desenvolvedor (feedback lento, falsos positivos) ou envia código quebrado (falsos negativos, cobertura insuficiente). Testes de burn-in garantem confiabilidade testando o código alterado sob estresse, enquanto execução paralela e seleção inteligente de teste otimizam velocidade sem sacrificar a abrangência.

## Exemplos de Padrões

### Exemplo 1: Workflow GitHub Actions com Execução Paralela

**Contexto**: Pipeline CI/CD pronto para produção para testes E2E com cache, paralelização e testes de burn-in.

**Implementação**:

```yaml
# .github/workflows/e2e-tests.yml
name: Testes E2E
on:
  pull_request:
  push:
    branches: [main, develop]

env:
  NODE_VERSION_FILE: '.nvmrc'
  CACHE_KEY: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}

jobs:
  install-dependencies:
    name: Instalar & Cachear Dependências
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - name: Checkout código
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version-file: ${{ env.NODE_VERSION_FILE }}
          cache: 'npm'

      - name: Cachear módulos node
        uses: actions/cache@v4
        id: npm-cache
        with:
          path: |
            ~/.npm
            node_modules
            ~/.cache/Cypress
            ~/.cache/ms-playwright
          key: ${{ env.CACHE_KEY }}
          restore-keys: |
            ${{ runner.os }}-node-

      - name: Instalar dependências
        if: steps.npm-cache.outputs.cache-hit != 'true'
        run: npm ci --prefer-offline --no-audit

      - name: Instalar browsers Playwright
        if: steps.npm-cache.outputs.cache-hit != 'true'
        run: npx playwright install --with-deps chromium

  test-changed-specs:
    name: Testar Specs Alterados Primeiro (Burn-In)
    needs: install-dependencies
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - name: Checkout código
        uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Histórico completo para diff preciso

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version-file: ${{ env.NODE_VERSION_FILE }}
          cache: 'npm'

      - name: Restaurar dependências
        uses: actions/cache@v4
        with:
          path: |
            ~/.npm
            node_modules
            ~/.cache/ms-playwright
          key: ${{ env.CACHE_KEY }}

      - name: Detectar arquivos de teste alterados
        id: changed-tests
        run: |
          CHANGED_SPECS=$(git diff --name-only origin/main...HEAD | grep -E '\.(spec|test)\.(ts|js|tsx|jsx)$' || echo "")
          echo "changed_specs=${CHANGED_SPECS}" >> $GITHUB_OUTPUT
          echo "Specs alterados: ${CHANGED_SPECS}"

      - name: Rodar burn-in em specs alterados (10 iterações)
        if: steps.changed-tests.outputs.changed_specs != ''
        run: |
          SPECS="${{ steps.changed-tests.outputs.changed_specs }}"
          echo "Rodando burn-in: 10 iterações em specs alterados"
          for i in {1..10}; do
            echo "Iteração burn-in $i/10"
            npm run test -- $SPECS || {
              echo "❌ Burn-in falhou na iteração $i"
              exit 1
            }
          done
          echo "✅ Burn-in passou - 10/10 execuções bem-sucedidas"

      - name: Upload de artefatos na falha
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: burn-in-failure-artifacts
          path: |
            test-results/
            playwright-report/
            screenshots/
          retention-days: 7

  test-e2e-sharded:
    name: Testes E2E (Shard ${{ matrix.shard }}/${{ strategy.job-total }})
    needs: [install-dependencies, test-changed-specs]
    runs-on: ubuntu-latest
    timeout-minutes: 30
    strategy:
      fail-fast: false # Rodar todos os shards mesmo se um falhar
      matrix:
        shard: [1, 2, 3, 4]
    steps:
      - name: Checkout código
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version-file: ${{ env.NODE_VERSION_FILE }}
          cache: 'npm'

      - name: Restaurar dependências
        uses: actions/cache@v4
        with:
          path: |
            ~/.npm
            node_modules
            ~/.cache/ms-playwright
          key: ${{ env.CACHE_KEY }}

      - name: Rodar testes E2E (shard ${{ matrix.shard }})
        run: npm run test:e2e -- --shard=${{ matrix.shard }}/4
        env:
          TEST_ENV: staging
          CI: true

      - name: Upload resultados de teste
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results-shard-${{ matrix.shard }}
          path: |
            test-results/
            playwright-report/
          retention-days: 30

      - name: Upload relatório JUnit
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: junit-results-shard-${{ matrix.shard }}
          path: test-results/junit.xml
          retention-days: 30

  merge-test-results:
    name: Fundir Resultados de Teste & Gerar Relatório
    needs: test-e2e-sharded
    runs-on: ubuntu-latest
    if: always()
    steps:
      - name: Baixar resultados de todos shards
        uses: actions/download-artifact@v4
        with:
          pattern: test-results-shard-*
          path: all-results/

      - name: Fundir relatórios HTML
        run: |
          npx playwright merge-reports --reporter=html all-results/
          echo "Relatório fundido disponível em playwright-report/"

      - name: Upload relatório fundido
        uses: actions/upload-artifact@v4
        with:
          name: merged-playwright-report
          path: playwright-report/
          retention-days: 30

      - name: Comentar PR com resultados
        if: github.event_name == 'pull_request'
        uses: daun/playwright-report-comment@v3
        with:
          report-path: playwright-report/
```

**Pontos Chave**:

- **Instalar uma vez, reutilizar em todo lugar**: Dependências cacheadas em todos os jobs
- **Burn-in primeiro**: Specs alterados rodam 10x antes da suíte completa
- **Fail-fast desativado**: Todos shards rodam até completar para evidência total
- **Execução paralela**: 4 shards cortam tempo de execução em ~75%
- **Retenção de artefato**: 30 dias para relatórios, 7 dias para debugging de falha

---

### Exemplo 2: Padrão de Loop de Burn-In (Script Independente)

**Contexto**: Script bash reutilizável para testes de burn-in em specs alterados localmente ou em CI.

**Implementação**:

```bash
#!/bin/bash
# scripts/burn-in-changed.sh
# Uso: ./scripts/burn-in-changed.sh [iterações] [branch-base]

set -e  # Sair no erro

# Configuração
ITERATIONS=${1:-10}
BASE_BRANCH=${2:-main}
SPEC_PATTERN='\.(spec|test)\.(ts|js|tsx|jsx)$'

echo "🔥 Burn-In Test Runner"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Iterações: $ITERATIONS"
echo "Branch base: $BASE_BRANCH"
echo ""

# Detectar arquivos de teste alterados
echo "📋 Detectando arquivos de teste alterados..."
CHANGED_SPECS=$(git diff --name-only $BASE_BRANCH...HEAD | grep -E "$SPEC_PATTERN" || echo "")

if [ -z "$CHANGED_SPECS" ]; then
  echo "✅ Nenhum arquivo de teste alterado. Pulando burn-in."
  exit 0
fi

echo "Arquivos de teste alterados:"
echo "$CHANGED_SPECS" | sed 's/^/  - /'
echo ""

# Contar specs
SPEC_COUNT=$(echo "$CHANGED_SPECS" | wc -l | xargs)
echo "Rodando burn-in em $SPEC_COUNT arquivo(s) de teste..."
echo ""

# Loop de Burn-in
FAILURES=()
for i in $(seq 1 $ITERATIONS); do
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "🔄 Iteração $i/$ITERATIONS"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  # Rodar testes com lista de arquivos explícita
  if npm run test -- $CHANGED_SPECS 2>&1 | tee "burn-in-log-$i.txt"; then
    echo "✅ Iteração $i passou"
  else
    echo "❌ Iteração $i falhou"
    FAILURES+=($i)

    # Salvar artefatos de falha
    mkdir -p burn-in-failures/iteration-$i
    cp -r test-results/ burn-in-failures/iteration-$i/ 2>/dev/null || true
    cp -r screenshots/ burn-in-failures/iteration-$i/ 2>/dev/null || true

    echo ""
    echo "🛑 BURN-IN FALHOU na iteração $i"
    echo "Artefatos de falha salvos em: burn-in-failures/iteration-$i/"
    echo "Logs salvos em: burn-in-log-$i.txt"
    echo ""
    exit 1
  fi

  echo ""
done

# Sumário de sucesso
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 BURN-IN PASSOU"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Todas as $ITERATIONS iterações passaram para $SPEC_COUNT arquivo(s) de teste"
echo "Specs alterados estão estáveis e prontos para merge."
echo ""

# Limpar logs
rm -f burn-in-log-*.txt

exit 0
```

**Uso**:

```bash
# Rodar localmente com configurações padrão (10 iterações, comparar com main)
./scripts/burn-in-changed.sh

# Iterações customizadas e branch base
./scripts/burn-in-changed.sh 20 develop

# Adicionar ao package.json
{
  "scripts": {
    "test:burn-in": "bash scripts/burn-in-changed.sh",
    "test:burn-in:strict": "bash scripts/burn-in-changed.sh 20"
  }
}
```

**Pontos Chave**:

- **Sair na primeira falha**: Testes instáveis capturados imediatamente
- **Artefatos de falha**: Salvos por iteração para debugging
- **Configuração flexível**: Iterações e branch base customizáveis
- **Paridade CI/local**: Mesmo script roda em ambos ambientes
- **Saída clara**: Feedback visual sobre progresso e resultados

---

### Exemplo 3: Orquestração de Shard com Agregação de Resultado

**Contexto**: Estratégia de sharding avançada para grandes suítes de teste com fusão de resultado inteligente.

**Implementação**:

```javascript
// scripts/run-sharded-tests.js
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

/**
 * Rodar testes através de múltiplos shards e agregar resultados
 * Uso: node scripts/run-sharded-tests.js --shards=4 --env=staging
 */

const SHARD_COUNT = parseInt(process.env.SHARD_COUNT || '4');
const TEST_ENV = process.env.TEST_ENV || 'local';
const RESULTS_DIR = path.join(__dirname, '../test-results');

console.log(`🚀 Rodando testes através de ${SHARD_COUNT} shards`);
console.log(`Ambiente: ${TEST_ENV}`);
console.log('━'.repeat(50));

// Garantir que diretório de resultados exista
if (!fs.existsSync(RESULTS_DIR)) {
  fs.mkdirSync(RESULTS_DIR, { recursive: true });
}

/**
 * Rodar um único shard
 */
function runShard(shardIndex) {
  return new Promise((resolve, reject) => {
    const shardId = `${shardIndex}/${SHARD_COUNT}`;
    console.log(`\n📦 Iniciando shard ${shardId}...`);

    const child = spawn('npx', ['playwright', 'test', `--shard=${shardId}`, '--reporter=json'], {
      env: { ...process.env, TEST_ENV, SHARD_INDEX: shardIndex },
      stdio: 'pipe',
    });

    let stdout = '';
    let stderr = '';

    child.stdout.on('data', (data) => {
      stdout += data.toString();
      process.stdout.write(data);
    });

    child.stderr.on('data', (data) => {
      stderr += data.toString();
      process.stderr.write(data);
    });

    child.on('close', (code) => {
      // Salvar resultados do shard
      const resultFile = path.join(RESULTS_DIR, `shard-${shardIndex}.json`);
      try {
        const result = JSON.parse(stdout);
        fs.writeFileSync(resultFile, JSON.stringify(result, null, 2));
        console.log(`✅ Shard ${shardId} completado (código de saída: ${code})`);
        resolve({ shardIndex, code, result });
      } catch (error) {
        console.error(`❌ Shard ${shardId} falhou ao parsear resultados:`, error.message);
        reject({ shardIndex, code, error });
      }
    });

    child.on('error', (error) => {
      console.error(`❌ Shard ${shardId} erro de processo:`, error.message);
      reject({ shardIndex, error });
    });
  });
}

/**
 * Agregar resultados de todos os shards
 */
function aggregateResults() {
  console.log('\n📊 Agregando resultados de todos os shards...');

  const shardResults = [];
  let totalTests = 0;
  let totalPassed = 0;
  let totalFailed = 0;
  let totalSkipped = 0;
  let totalFlaky = 0;

  for (let i = 1; i <= SHARD_COUNT; i++) {
    const resultFile = path.join(RESULTS_DIR, `shard-${i}.json`);
    if (fs.existsSync(resultFile)) {
      const result = JSON.parse(fs.readFileSync(resultFile, 'utf8'));
      shardResults.push(result);

      // Agregar estatísticas
      totalTests += result.stats?.expected || 0;
      totalPassed += result.stats?.expected || 0;
      totalFailed += result.stats?.unexpected || 0;
      totalSkipped += result.stats?.skipped || 0;
      totalFlaky += result.stats?.flaky || 0;
    }
  }

  const summary = {
    totalShards: SHARD_COUNT,
    environment: TEST_ENV,
    totalTests,
    passed: totalPassed,
    failed: totalFailed,
    skipped: totalSkipped,
    flaky: totalFlaky,
    duration: shardResults.reduce((acc, r) => acc + (r.duration || 0), 0),
    timestamp: new Date().toISOString(),
  };

  // Salvar sumário agregado
  fs.writeFileSync(path.join(RESULTS_DIR, 'summary.json'), JSON.stringify(summary, null, 2));

  console.log('\n━'.repeat(50));
  console.log('📈 Sumário de Resultados de Teste');
  console.log('━'.repeat(50));
  console.log(`Total testes:   ${totalTests}`);
  console.log(`✅ Passou:      ${totalPassed}`);
  console.log(`❌ Falhou:      ${totalFailed}`);
  console.log(`⏭️  Pulado:      ${totalSkipped}`);
  console.log(`⚠️  Instável:    ${totalFlaky}`);
  console.log(`⏱️  Duração:     ${(summary.duration / 1000).toFixed(2)}s`);
  console.log('━'.repeat(50));

  return summary;
}

/**
 * Execução principal
 */
async function main() {
  const startTime = Date.now();
  const shardPromises = [];

  // Rodar todos shards em paralelo
  for (let i = 1; i <= SHARD_COUNT; i++) {
    shardPromises.push(runShard(i));
  }

  try {
    await Promise.allSettled(shardPromises);
  } catch (error) {
    console.error('❌ Um ou mais shards falharam:', error);
  }

  // Agregar resultados
  const summary = aggregateResults();

  const totalTime = ((Date.now() - startTime) / 1000).toFixed(2);
  console.log(`\n⏱️  Tempo total de execução: ${totalTime}s`);

  // Sair com falha se quaisquer testes falharam
  if (summary.failed > 0) {
    console.error('\n❌ Suíte de teste falhou');
    process.exit(1);
  }

  console.log('\n✅ Todos testes passaram');
  process.exit(0);
}

main().catch((error) => {
  console.error('Erro fatal:', error);
  process.exit(1);
});
```

**Integração package.json**:

```json
{
  "scripts": {
    "test:sharded": "node scripts/run-sharded-tests.js",
    "test:sharded:ci": "SHARD_COUNT=8 TEST_ENV=staging node scripts/run-sharded-tests.js"
  }
}
```

**Pontos Chave**:

- **Execução de shard paralela**: Todos shards rodam simultaneamente
- **Agregação de resultado**: Sumário unificado através dos shards
- **Detecção de falha**: Código de saída reflete status geral do teste
- **Preservação de artefato**: Resultados de shard individual salvos para debugging
- **Compatibilidade CI/local**: Mesmo script funciona em ambos ambientes

---

### Exemplo 4: Execução de Teste Seletiva (Arquivos Alterados + Tags)

**Contexto**: Otimizar CI rodando apenas testes relevantes baseado em mudanças de arquivo e tags.

**Implementação**:

```bash
#!/bin/bash
# scripts/selective-test-runner.sh
# Seleção de teste inteligente baseada em arquivos alterados e tags de teste

set -e

BASE_BRANCH=${BASE_BRANCH:-main}
TEST_ENV=${TEST_ENV:-local}

echo "🎯 Runner de Teste Seletivo"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Branch base: $BASE_BRANCH"
echo "Ambiente: $TEST_ENV"
echo ""

# Detectar arquivos alterados (todos tipos, não apenas testes)
CHANGED_FILES=$(git diff --name-only $BASE_BRANCH...HEAD)

if [ -z "$CHANGED_FILES" ]; then
  echo "✅ Nenhum arquivo alterado. Pulando testes."
  exit 0
fi

echo "Arquivos alterados:"
echo "$CHANGED_FILES" | sed 's/^/  - /'
echo ""

# Determinar estratégia de teste baseado em mudanças
run_smoke_only=false
run_all_tests=false
affected_specs=""

# Arquivos críticos = rodar todos testes
if echo "$CHANGED_FILES" | grep -qE '(package\.json|package-lock\.json|playwright\.config|cypress\.config|\.github/workflows)'; then
  echo "⚠️  Arquivos de configuração críticos alterados. Rodando TODOS os testes."
  run_all_tests=true

# Mudanças de auth/segurança = rodar todos testes de auth + smoke
elif echo "$CHANGED_FILES" | grep -qE '(auth|login|signup|security)'; then
  echo "🔒 Arquivos de auth/segurança alterados. Rodando testes auth + smoke."
  npm run test -- --grep "@auth|@smoke"
  exit $?

# Mudanças de API = rodar integração + smoke tests
elif echo "$CHANGED_FILES" | grep -qE '(api|service|controller)'; then
  echo "🔌 Arquivos de API alterados. Rodando testes integração + smoke."
  npm run test -- --grep "@integration|@smoke"
  exit $?

# Mudanças de componente UI = rodar testes de componente relacionados
elif echo "$CHANGED_FILES" | grep -qE '\.(tsx|jsx|vue)$'; then
  echo "🎨 Componentes UI alterados. Rodando testes componente + smoke."

  # Extrair nomes de componente e encontrar testes relacionados
  components=$(echo "$CHANGED_FILES" | grep -E '\.(tsx|jsx|vue)$' | xargs -I {} basename {} | sed 's/\.[^.]*$//')
  for component in $components; do
    # Encontrar testes correspondendo nome do componente
    affected_specs+=$(find tests -name "*${component}*" -type f) || true
  done

  if [ -n "$affected_specs" ]; then
    echo "Rodando testes para: $affected_specs"
    npm run test -- $affected_specs --grep "@smoke"
  else
    echo "Nenhum teste específico encontrado. Rodando apenas smoke tests."
    npm run test -- --grep "@smoke"
  fi
  exit $?

# Documentação/config apenas = rodar smoke tests
elif echo "$CHANGED_FILES" | grep -qE '\.(md|txt|json|yml|yaml)$'; then
  echo "📝 Arquivos de documentação/config alterados. Rodando apenas smoke tests."
  run_smoke_only=true
else
  echo "⚙️  Outros arquivos alterados. Rodando smoke tests."
  run_smoke_only=true
fi

# Executar estratégia selecionada
if [ "$run_all_tests" = true ]; then
  echo ""
  echo "Rodando suíte de teste completa..."
  npm run test
elif [ "$run_smoke_only" = true ]; then
  echo ""
  echo "Rodando smoke tests..."
  npm run test -- --grep "@smoke"
fi
```

**Uso no GitHub Actions**:

```yaml
# .github/workflows/selective-tests.yml
name: Testes Seletivos
on: pull_request

jobs:
  selective-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Rodar testes seletivos
        run: bash scripts/selective-test-runner.sh
        env:
          BASE_BRANCH: ${{ github.base_ref }}
          TEST_ENV: staging
```

**Pontos Chave**:

- **Roteamento inteligente**: Testes selecionados baseados em tipos de arquivo alterados
- **Filtragem baseada em Tag**: Use tags @smoke, @auth, @integration
- **Feedback rápido**: Apenas testes relevantes rodam na maioria dos PRs
- **Rede de segurança**: Mudanças críticas disparam suíte completa
- **Mapeamento de componente**: Mudanças de UI rodam testes de componente relacionados

---

## Checklist de Configuração CI

Antes de implantar seu pipeline CI, verifique:

- [ ] **Estratégia de cache**: node_modules, cache npm, binários de browser cacheados
- [ ] **Orçamentos de timeout**: Cada job tem timeout razoável (10-30 min)
- [ ] **Retenção de artefato**: 30 dias para relatórios, 7 dias para artefatos de falha
- [ ] **Paralelização**: Estratégia de matriz usa fail-fast: false
- [ ] **Burn-in ativado**: Specs alterados rodam 5-10x antes do merge
- [ ] **wait-on inicialização app**: CI espera pelo app (wait-on: '<http://localhost:3000>')
- [ ] **Segredos documentados**: README lista segredos necessários (chaves API, tokens)
- [ ] **Paridade local**: Scripts CI executáveis localmente (npm run test:ci)

## Pontos de Integração

- Usado em workflows: `*ci` (configuração de pipeline CI/CD)
- Fragmentos relacionados: `selective-testing.md`, `playwright-config.md`, `test-quality.md`
- Ferramentas CI: GitHub Actions, GitLab CI, CircleCI, Jenkins

_Fonte: Blog de estratégia CI/CD Murat, exemplos de workflow Playwright/Cypress, otimização de produção SEON_
