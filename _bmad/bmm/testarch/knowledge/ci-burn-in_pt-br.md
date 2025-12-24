# Pipeline CI e estratégia de queima

## Princípio

Os pipelines CI devem executar testes de forma confiável, rápida e fornecer feedback claro. Testes de gravação (executando testes alterados várias vezes) elimina flakiness antes de mesclar. Trabalhos de palco estrategicamente: instale/cache uma vez, execute especificações alteradas primeiro para feedback rápido, em seguida, hard suites completas com fail-fast desabilitado para preservar evidências.

## Racional

A CI é a porta de qualidade para a produção. Um oleoduto mal configurado desperdiça tempo de desenvolvimento (reação lenta, false positivos) ou envia código quebrado (false negativos, cobertura insuficiente). Testes de gravação garantem confiabilidade através de testes de estresse código alterado, enquanto execução paralela e seleção de teste inteligente otimizar a velocidade sem sacrificar a meticulosidade.

## Exemplos de padrões

### Exemplo 1: Fluxo de trabalho de ações do GitHub com execução paralela

**Context**: Pipeline CI/CD pronto para produção para testes E2E com caching, paralelização e teste de queima.

**Implementation**:

```yaml

# .github/workflows/e2e-tests.yml
name: E2E Tests
on:
  pull_request:
  push:
    branches: [main, develop]

env:
  NODE_VERSION_FILE: '.nvmrc'
  CACHE_KEY: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}

jobs:
  install-dependencies:
    name: Install & Cache Dependencies
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version-file: ${{ env.NODE_VERSION_FILE }}
          cache: 'npm'

      - name: Cache node modules
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

      - name: Install dependencies
        if: steps.npm-cache.outputs.cache-hit != 'true'
        run: npm ci --prefer-offline --no-audit

      - name: Install Playwright browsers
        if: steps.npm-cache.outputs.cache-hit != 'true'
        run: npx playwright install --with-deps chromium

  test-changed-specs:
    name: Test Changed Specs First (Burn-In)
    needs: install-dependencies
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Full history for accurate diff

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version-file: ${{ env.NODE_VERSION_FILE }}
          cache: 'npm'

      - name: Restore dependencies
        uses: actions/cache@v4
        with:
          path: |
            ~/.npm
            node_modules
            ~/.cache/ms-playwright
          key: ${{ env.CACHE_KEY }}

      - name: Detect changed test files
        id: changed-tests
        run: |
          CHANGED_SPECS=$(git diff --name-only origin/main...HEAD | grep -E '\.(spec|test)\.(ts|js|tsx|jsx)$' || echo "")
          echo "changed_specs=${CHANGED_SPECS}" >> $GITHUB_OUTPUT
          echo "Changed specs: ${CHANGED_SPECS}"

      - name: Run burn-in on changed specs (10 iterations)
        if: steps.changed-tests.outputs.changed_specs != ''
        run: |
          SPECS="${{ steps.changed-tests.outputs.changed_specs }}"
          echo "Running burn-in: 10 iterations on changed specs"
          for i in {1..10}; do
            echo "Burn-in iteration $i/10"
            npm run test -- $SPECS || {
              echo "❌ Burn-in failed on iteration $i"
              exit 1
            }
          done
          echo "✅ Burn-in passed - 10/10 successful runs"

      - name: Upload artifacts on failure
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
    name: E2E Tests (Shard ${{ matrix.shard }}/${{ strategy.job-total }})
    needs: [install-dependencies, test-changed-specs]
    runs-on: ubuntu-latest
    timeout-minutes: 30
    strategy:
      fail-fast: false # Run all shards even if one fails
      matrix:
        shard: [1, 2, 3, 4]
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version-file: ${{ env.NODE_VERSION_FILE }}
          cache: 'npm'

      - name: Restore dependencies
        uses: actions/cache@v4
        with:
          path: |
            ~/.npm
            node_modules
            ~/.cache/ms-playwright
          key: ${{ env.CACHE_KEY }}

      - name: Run E2E tests (shard ${{ matrix.shard }})
        run: npm run test:e2e -- --shard=${{ matrix.shard }}/4
        env:
          TEST_ENV: staging
          CI: true

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results-shard-${{ matrix.shard }}
          path: |
            test-results/
            playwright-report/
          retention-days: 30

      - name: Upload JUnit report
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: junit-results-shard-${{ matrix.shard }}
          path: test-results/junit.xml
          retention-days: 30

  merge-test-results:
    name: Merge Test Results & Generate Report
    needs: test-e2e-sharded
    runs-on: ubuntu-latest
    if: always()
    steps:
      - name: Download all shard results
        uses: actions/download-artifact@v4
        with:
          pattern: test-results-shard-*
          path: all-results/

      - name: Merge HTML reports
        run: |
          npx playwright merge-reports --reporter=html all-results/
          echo "Merged report available in playwright-report/"

      - name: Upload merged report
        uses: actions/upload-artifact@v4
        with:
          name: merged-playwright-report
          path: playwright-report/
          retention-days: 30

      - name: Comment PR with results
        if: github.event_name == 'pull_request'
        uses: daun/playwright-report-comment@v3
        with:
          report-path: playwright-report/

```

**Key Pontos**:

- **Install uma vez, reutilizar em toda a parte**: Dependências armazenadas em todos os trabalhos
- **Burn-in primeiro**: As especificações alteradas executam 10x antes da suite completa
- **Fail-fast desactivado**: Todos os fragmentos são executados até a conclusão para a evidência completa
- **Parallel execução**: 4 fragmentos cortar tempo de execução em ~75%
- **Artifact retenção**: 30 dias para relatórios, 7 dias para depuração de falhas

---

### Example 2: Burn-In Loop Pattern (Standalone Script)

**Context**: Reusable bash script for burn-in testing changed specs locally or in CI.

**Implementation**:

```bash
# !/bin/bash

# scripts/burn-in-changed.sh

# Usage: ./scripts/burn-in-changed.sh [iterations] [base-branch]

set -e  # Exit on error

# Configuration
ITERATIONS=${1:-10}
BASE_BRANCH=${2:-main}
SPEC_PATTERN='\.(spec|test)\.(ts|js|tsx|jsx)$'

echo "🔥 Burn-In Test Runner"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Iterations: $ITERATIONS"
echo "Base branch: $BASE_BRANCH"
echo ""

# Detect changed test files
echo "📋 Detecting changed test files..."
CHANGED_SPECS=$(git diff --name-only $BASE_BRANCH...HEAD | grep -E "$SPEC_PATTERN" || echo "")

if [-z "$CHANGED_SPECS"]; then
  echo "✅ No test files changed. Skipping burn-in."
  exit 0
fi

echo "Changed test files:"
echo "$CHANGED_SPECS" | sed 's/^/  - /'
echo ""

# Count specs
SPEC_COUNT=$(echo "$CHANGED_SPECS" | wc -l | xargs)
echo "Running burn-in on $SPEC_COUNT test file(s)..."
echo ""

# Burn-in loop
FAILURES=()
for i in $(seq 1 $ITERATIONS); do
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "🔄 Iteration $i/$ITERATIONS"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  # Run tests with explicit file list
  if npm run test -- $CHANGED_SPECS 2>&1 | tee "burn-in-log-$i.txt"; then
    echo "✅ Iteration $i passed"
  else
    echo "❌ Iteration $i failed"
    FAILURES+=($i)

    # Save failure artifacts
    mkdir -p burn-in-failures/iteration-$i
    cp -r test-results/ burn-in-failures/iteration-$i/ 2>/dev/null || true
    cp -r screenshots/ burn-in-failures/iteration-$i/ 2>/dev/null || true

    echo ""
    echo "🛑 BURN-IN FAILED on iteration $i"
    echo "Failure artifacts saved to: burn-in-failures/iteration-$i/"
    echo "Logs saved to: burn-in-log-$i.txt"
    echo ""
    exit 1
  fi

  echo ""
done

# Success summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 BURN-IN PASSED"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "All $ITERATIONS iterations passed for $SPEC_COUNT test file(s)"
echo "Changed specs are stable and ready to merge."
echo ""

# Cleanup logs
rm -f burn-in-log-*.txt

exit 0

```

**Usage**:

```bash

# Run locally with default settings (10 iterations, compare to main)
./scripts/burn-in-changed.sh

# Custom iterations and base branch
./scripts/burn-in-changed.sh 20 develop

# Add to package.json
{
  "scripts": {
    "test:burn-in": "bash scripts/burn-in-changed.sh",
    "test:burn-in:strict": "bash scripts/burn-in-changed.sh 20"
  }
}

```

**Key Points**:

- **Exit on first failure**: Flaky tests caught immediately
- **Failure artifacts**: Saved per-iteration for debugging
- **Flexible configuration**: Iterations and base branch customizable
- **CI/local parity**: Same script runs in both environments
- **Clear output**: Visual feedback on progress and results

---

### Exemplo 3: Orquestração de cordões com agregação de resultados

**Context**: Estratégia avançada para grandes suítes de teste com fusão inteligente de resultados.

**Implementation**:

```javascript
// scripts/run-sharded-tests.js
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

/**
 * Run tests across multiple shards and aggregate results
 * Usage: node scripts/run-sharded-tests.js --shards=4 --env=staging
 */

const SHARD_COUNT = parseInt(process.env.SHARD_COUNT || '4');
const TEST_ENV = process.env.TEST_ENV || 'local';
const RESULTS_DIR = path.join(__dirname, '../test-results');

console.log(`🚀 Running tests across ${SHARD_COUNT} shards`);
console.log(`Environment: ${TEST_ENV}`);
console.log('━'.repeat(50));

// Ensure results directory exists
if (!fs.existsSync(RESULTS_DIR)) {
  fs.mkdirSync(RESULTS_DIR, { recursive: true });
}

/**
 * Run a single shard
 */
function runShard(shardIndex) {
  return new Promise((resolve, reject) => {
    const shardId = `${shardIndex}/${SHARD_COUNT}`;
    console.log(`\n📦 Starting shard ${shardId}...`);

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
      // Save shard results
      const resultFile = path.join(RESULTS_DIR, `shard-${shardIndex}.json`);
      try {
        const result = JSON.parse(stdout);
        fs.writeFileSync(resultFile, JSON.stringify(result, null, 2));
        console.log(`✅ Shard ${shardId} completed (exit code: ${code})`);
        resolve({ shardIndex, code, result });
      } catch (error) {
        console.error(`❌ Shard ${shardId} failed to parse results:`, error.message);
        reject({ shardIndex, code, error });
      }
    });

    child.on('error', (error) => {
      console.error(`❌ Shard ${shardId} process error:`, error.message);
      reject({ shardIndex, error });
    });
  });
}

/**
 * Aggregate results from all shards
 */
function aggregateResults() {
  console.log('\n📊 Aggregating results from all shards...');

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

      // Aggregate stats
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

  // Save aggregated summary
  fs.writeFileSync(path.join(RESULTS_DIR, 'summary.json'), JSON.stringify(summary, null, 2));

  console.log('\n━'.repeat(50));
  console.log('📈 Test Results Summary');
  console.log('━'.repeat(50));
  console.log(`Total tests:    ${totalTests}`);
  console.log(`✅ Passed:      ${totalPassed}`);
  console.log(`❌ Failed:      ${totalFailed}`);
  console.log(`⏭️  Skipped:     ${totalSkipped}`);
  console.log(`⚠️  Flaky:       ${totalFlaky}`);
  console.log(`⏱️  Duration:    ${(summary.duration / 1000).toFixed(2)}s`);
  console.log('━'.repeat(50));

  return summary;
}

/**
 * Main execution
 */
async function main() {
  const startTime = Date.now();
  const shardPromises = [];

  // Run all shards in parallel
  for (let i = 1; i <= SHARD_COUNT; i++) {
    shardPromises.push(runShard(i));
  }

  try {
    await Promise.allSettled(shardPromises);
  } catch (error) {
    console.error('❌ One or more shards failed:', error);
  }

  // Aggregate results
  const summary = aggregateResults();

  const totalTime = ((Date.now() - startTime) / 1000).toFixed(2);
  console.log(`\n⏱️  Total execution time: ${totalTime}s`);

  // Exit with failure if any tests failed
  if (summary.failed > 0) {
    console.error('\n❌ Test suite failed');
    process.exit(1);
  }

  console.log('\n✅ All tests passed');
  process.exit(0);
}

main().catch((error) => {
  console.error('Fatal error:', error);
  process.exit(1);
});

```

**package.json integração**:

```json
{
  "scripts": {
    "test:sharded": "node scripts/run-sharded-tests.js",
    "test:sharded:ci": "SHARD_COUNT=8 TEST_ENV=staging node scripts/run-sharded-tests.js"
  }
}

```

**Key Pontos**:

-**Parallel execução de fragmentos**: Todos os fragmentos são executados simultaneamente
- **Result agregação**: Resumo unificado entre fragmentos
- * Detecção de *Failure**: O código de saída reflete o estado geral do teste
- **Artifact preservação**: Resultados de fragmentos individuais salvos para depuração
- **CI/compatibilidade local**: O mesmo programa funciona em ambos os ambientes

---

### Example 4: Selective Test Execution (Changed Files + Tags)

**Context**: Optimize CI by running only relevant tests based on file changes and tags.

**Implementation**:

```bash
# !/bin/bash

# scripts/selective-test-runner.sh

# Intelligent test selection based on changed files and test tags

set -e

BASE_BRANCH=${BASE_BRANCH:-main}
TEST_ENV=${TEST_ENV:-local}

echo "🎯 Selective Test Runner"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Base branch: $BASE_BRANCH"
echo "Environment: $TEST_ENV"
echo ""

# Detect changed files (all types, not just tests)
CHANGED_FILES=$(git diff --name-only $BASE_BRANCH...HEAD)

if [-z "$CHANGED_FILES"]; then
  echo "✅ No files changed. Skipping tests."
  exit 0
fi

echo "Changed files:"
echo "$CHANGED_FILES" | sed 's/^/  - /'
echo ""

# Determine test strategy based on changes
run_smoke_only=false
run_all_tests=false
affected_specs=""

# Critical files = run all tests
if echo "$CHANGED_FILES" | grep -qE '(package\.json|package-lock\.json|playwright\.config|cypress\.config|\.github/workflows)'; then
  echo "⚠️  Critical configuration files changed. Running ALL tests."
  run_all_tests=true

# Auth/security changes = run all auth + smoke tests
elif echo "$CHANGED_FILES" | grep -qE '(auth|login|signup|security)'; then
  echo "🔒 Auth/security files changed. Running auth + smoke tests."
  npm run test -- --grep "@auth|@smoke"
  exit $?

# API changes = run integration + smoke tests
elif echo "$CHANGED_FILES" | grep -qE '(api|service|controller)'; then
  echo "🔌 API files changed. Running integration + smoke tests."
  npm run test -- --grep "@integration|@smoke"
  exit $?

# UI component changes = run related component tests
elif echo "$CHANGED_FILES" | grep -qE '\.(tsx|jsx|vue)$'; then
  echo "🎨 UI components changed. Running component + smoke tests."

  # Extract component names and find related tests
  components=$(echo "$CHANGED_FILES" | grep -E '\.(tsx|jsx|vue)$' | xargs -I {} basename {} | sed 's/\.[^.]*$//')
  for component in $components; do
    # Find tests matching component name
    affected_specs+=$(find tests -name "*${component}*" -type f) || true
  done

  if [-n "$affected_specs"]; then
    echo "Running tests for: $affected_specs"
    npm run test -- $affected_specs --grep "@smoke"
  else
    echo "No specific tests found. Running smoke tests only."
    npm run test -- --grep "@smoke"
  fi
  exit $?

# Documentation/config only = run smoke tests
elif echo "$CHANGED_FILES" | grep -qE '\.(md|txt|json|yml|yaml)$'; then
  echo "📝 Documentation/config files changed. Running smoke tests only."
  run_smoke_only=true
else
  echo "⚙️  Other files changed. Running smoke tests."
  run_smoke_only=true
fi

# Execute selected strategy
if ["$run_all_tests" = true]; then
  echo ""
  echo "Running full test suite..."
  npm run test
elif ["$run_smoke_only" = true]; then
  echo ""
  echo "Running smoke tests..."
  npm run test -- --grep "@smoke"
fi

```

**Usage in GitHub Actions**:

```yaml

# .github/workflows/selective-tests.yml
name: Selective Tests
on: pull_request

jobs:
  selective-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run selective tests
        run: bash scripts/selective-test-runner.sh
        env:
          BASE_BRANCH: ${{ github.base_ref }}
          TEST_ENV: staging

```

**Key Points**:

- **Intelligent routing**: Tests selected based on changed file types
- **Tag-based filtering**: Use @smoke, @auth, @integration tags
- **Fast feedback**: Only relevant tests run on most PRs
- **Safety net**: Critical changes trigger full suite
- **Component mapping**: UI changes run related component tests

---

## Lista de Verificação de Configuração CI

Antes de implantar seu pipeline CI, verifique:

- [ ] **Caching strategy**: nó módulos, cache npm, binários do navegador em cache
- [ ] **Timeout orçamentos**: Cada trabalho tem tempo de espera razoável (10-30 min)
- [ ] **Artifact retension**: 30 dias para relatórios, 7 dias para artefatos de falha
- [ ] **Parallelization**: A estratégia Matrix utiliza falha rápida: false
- [ ] **Burn-in activado**: As especificações alteradas executam 5-10x antes da mesclagem
- [ ] **wait-on app startup**: CI espera pela app (espera: '<http://localhost:3000>')
- [ ] **Secrets documentado**: README lista segredos necessários (chaves API, fichas)
- [ ] **Local parity**: scripts CI executáveis localmente (npm run test:ci)

## Pontos de Integração

- Usado em fluxos de trabalho: `*ci` (configuração do gasoduto CI/CD)
- Fragmentos relacionados: `selective-testing.md`, `playwright-config.md`, `test-quality.md`
- Ferramentas CI: GitHub Actions, GitLab CI, CircleCI, Jenkins

_Source: Murat blog de estratégia CI/CD, exemplos de fluxo de trabalho Playwright/Cypress, pipelines de produção SEON
