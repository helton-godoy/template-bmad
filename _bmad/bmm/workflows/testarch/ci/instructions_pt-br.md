<!-- Powered by BMAD-CORE™ -->

# Configuração da tubulação CI/CD

**ID do fluxo de trabalho**: `_bmad/bmm/testarch/ci`
**Versão**: 4.0 (BMad v6)

---

## Overview

Scaffolds a production-ready CI/CD quality pipeline with test execution, burn-in loops for flaky test detection, parallel sharding, artifact collection, and notification configuration. This workflow creates platform-specific CI configuration optimized for fast feedback and reliable test execution.

---

## Requisitos de pré-voo

**Crítico:** Verifique estes requisitos antes de prosseguir. Se algum falhar, HALT e notificar o usuário.

- ✅ O repositório Git está inicializado (o diretório `.git/` existe)
- ✅ Passes de teste locais (`npm run test:e2e` tem sucesso)
- ✅ O framework de teste está configurado (do fluxo de trabalho `framework`)
- ✅ A equipe concorda com a plataforma CI alvo (Ações GitHub, GitLab CI, Circle CI, etc.)
- ✅ Acesso às configurações/segredos da plataforma CI disponíveis (se atualizar o gasoduto existente)

---

## Step 1: Run Preflight Checks

### Actions

1. **Verify Git Repository**
   - Check for `.git/` directory
   - Confirm remote repository configured (`git remote -v`)
   - If not initialized, HALT with message: "Git repository required for CI/CD setup"

2. **Validate Test Framework**
   - Look for `playwright.config.*` or `cypress.config.*`
   - Read framework configuration to extract:
     - Test directory location
     - Test command
     - Reporter configuration
     - Timeout settings
   - If not found, HALT with message: "Run `framework` workflow first to set up test infrastructure"

3. **Run Local Tests**
   - Execute `npm run test:e2e` (or equivalent from package.json)
   - Ensure tests pass before CI setup
   - If tests fail, HALT with message: "Fix failing tests before setting up CI/CD"

4. **Detect CI Platform**
   - Check for existing CI configuration:
     - `.github/workflows/*.yml` (GitHub Actions)
     - `.gitlab-ci.yml` (GitLab CI)
     - `.circleci/config.yml` (Circle CI)
     - `Jenkinsfile` (Jenkins)
   - If found, ask user: "Update existing CI configuration or create new?"
   - If not found, detect platform from git remote:
     - `github.com` → GitHub Actions (default)
     - `gitlab.com` → GitLab CI
     - Ask user if unable to auto-detect

5. **Read Environment Configuration**
   - Use `.nvmrc` for Node version if present
   - If missing, default to a current LTS (Node 24) or newer instead of a fixed old version
   - Read `package.json` to identify dependencies (affects caching strategy)

**Halt Condition:** If preflight checks fail, stop immediately and report which requirement failed.

---

## Passo 2: Andaimes CI Pipeline

### Acções

1. **Select CI Platform Template**

Com base na detecção ou preferência do usuário, use o modelo apropriado:

**Ações do GitHub** (`.github/workflows/test.yml`):
- Plataforma mais comum
- Excelente cache e suporte matricial
- Livre para acordos públicos, generoso nível livre para privado

**GitLab CI** (`.gitlab-ci.yml`):
- Integrado com GitLab
- Registro embutido e corredores
- Recursos poderosos do gasoduto

**Círculo CI** (`.circleci/config.yml`):
- Execução rápida com paralelismo
- Primeira abordagem do Docker
- Características empresariais

**Jenkins** (`Jenkinsfile`):
- Opção auto-alojada
- Personalização máxima
- Requer gestão de infra-estruturas

2. **Generate Pipeline Configuration**

Usar modelos do diretório `{installed_path}/`:
- `github-actions-template.yml`
- `gitlab-ci-template.yml`

**Estágios chave do gasoduto:**

```yaml
   stages:
     - lint # Code quality checks
     - test # Test execution (parallel shards)
     - burn-in # Flaky test detection
     - report # Aggregate results and publish
   ```

3. **Configurar execução de teste**

**Parallel Sharding:**

```yaml
   strategy:
     fail-fast: false
     matrix:
       shard: [1, 2, 3, 4]

   steps:
     - name: Run tests
       run: npm run test:e2e -- --shard=${{ matrix.shard }}/${{ strategy.job-total }}
   ```

**Composto:** Divide testes em tarefas paralelas N para execução mais rápida (alvo: < 10 min por fragmento)

4. **Add Burn-In Loop**

**Padrão crítico dos sistemas de produção:**

```yaml
   burn-in:
     name: Flaky Test Detection
     runs-on: ubuntu-latest
     steps:
       - uses: actions/checkout@v4

       - name: Setup Node
         uses: actions/setup-node@v4
         with:
           node-version-file: '.nvmrc'

       - name: Install dependencies
         run: npm ci

       - name: Run burn-in loop (10 iterations)
         run: |
           for i in {1..10}; do
             echo "🔥 Burn-in iteration $i/10"
             npm run test:e2e || exit 1
           done

       - name: Upload failure artifacts
         if: failure()
         uses: actions/upload-artifact@v4
         with:
           name: burn-in-failures
           path: test-results/
           retention-days: 30
   ```

**Põr:** Executa testes várias vezes para capturar falhas não determinísticas antes de atingir o ramo principal.

**Quando correr:**
- Em Pu