<!-- Powered by BMAD-CORE™ -->

# Configuração do Quadro de Teste

**ID do fluxo de trabalho**: `_bmad/bmm/testarch/framework`
**Versão**: 4.0 (BMad v6)

---

## Overview

Initialize a production-ready test framework architecture (Playwright or Cypress) with fixtures, helpers, configuration, and best practices. This workflow scaffolds the complete testing infrastructure for modern web applications.

---

## Requisitos de pré-voo

**Crítico:** Verifique estes requisitos antes de prosseguir. Se algum falhar, HALT e notificar o usuário.

- ✅ `package.json` existe na raiz do projecto
- ✅ Nenhum arnês de teste E2E moderno já está configurado (consulte `playwright.config.*` ou `cypress.config.*` existentes)
- ✅ Context Architectural/stack disponível (tipo de projeto, empacotador, dependências)

---

## Step 1: Run Preflight Checks

### Actions

1. **Validate package.json**
   - Read `{project-root}/package.json`
   - Extract project type (React, Vue, Angular, Next.js, Node, etc.)
   - Identify bundler (Vite, Webpack, Rollup, esbuild)
   - Note existing test dependencies

2. **Check for Existing Framework**
   - Search for `playwright.config.*`, `cypress.config.*`, `cypress.json`
   - Check `package.json` for `@playwright/test` or `cypress` dependencies
   - If found, HALT with message: "Existing test framework detected. Use workflow `upgrade-framework` instead."

3. **Gather Context**
   - Look for architecture documents (`architecture.md`, `tech-spec*.md`)
   - Check for API documentation or endpoint lists
   - Identify authentication requirements

**Halt Condition:** If preflight checks fail, stop immediately and report which requirement failed.

---

## Etapa 2: Quadro de andaimes

### Acções

1. **Selecção de quadros**

**Lógica padrão:**
- **Playwright** (recomendado para):
- Repositórios grandes (100+ arquivos)
- Aplicações críticas ao desempenho
- Suporte multi-browser necessário
- Fluxos complexos de usuários que requerem depuração de vídeo/traço
- Projectos que exigem paralelismo dos trabalhadores

- **Cypress** (recomendado para):
- Pequenas equipes priorizando a experiência do desenvolvedor
- Foco de teste de componentes
- Recarregamento em tempo real durante o desenvolvimento do teste
- Requisitos de configuração mais simples

**Estratégia de definição:**
- Verificar `package.json` para preferência existente
- Considere a variável `project_size` da configuração do fluxo de trabalho
- Use a variável `framework_preference` se definida
- Padrão para **Playwright** se incerto

2. **Criar estrutura de diretório**

```
   {project-root}/
   ├── tests/                        # Root test directory
   │   ├── e2e/                      # Test files (users organize as needed)
   │   ├── support/                  # Framework infrastructure (key pattern)
   │   │   ├── fixtures/             # Test fixtures (data, mocks)
   │   │   ├── helpers/              # Utility functions
   │   │   └── page-objects/         # Page object models (optional)
   │   └── README.md                 # Test suite documentation
   ```

**Nota**: Os utilizadores organizam ficheiros de teste (e2e/, api/, integration/, component/) conforme necessário. A pasta **suporte/** é o padrão crítico para acessórios e ajudantes utilizados em testes.

3. **Gerar arquivo de configuração**

**Para os dramaturgos** (`playwright.config.ts` ou `playwright.config.js`):

```typescript
   import { defineConfig, devices } from '@playwright/test';

   export default defineConfig({
     testDir: './tests/e2e',
     fullyParallel: true,
     forbidOnly: !!process.env.CI,
     retries: process.env.CI ? 2 : 0,
     workers: process.env.CI ? 1 : undefined,

     timeout: 60 * 1000, // Test timeout: 60s
     expect: {
       timeout: 15 * 1000, // Assertion timeout: 15s
     },

     use: {
       baseURL: process.env.BASE_URL || 'http://localhost:3000',
       trace: 'retain-on-failure',
       screenshot: 'only-on-failure',
       video: 'retain-on-failure',
       actionTimeout: 15 * 1000, // Action timeout: 15s
       navigationTimeout: 30 * 1000, // Navigation timeout: 30s
     },

     reporter: [['html', { outputFolder: 'test-results/html' }], ['junit', { outputFile: 'test-results/junit.xml' }], ['list']],

     projects: [
       { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
       { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
       { name: 'webkit', use: { ...devices['Desktop Safari'] } },
     ],
   });
   ```

**Para cipreste** (`cypress.config.ts` ou `cypress.config.js`):

«``typescript
BMADPROTECT019end BMADPROTECT024end da **cipreste**;

export defineConfig({
     e2e: {
       baseUrl: process.env.BASE_URL || 'http://localhost:3000',
       specPattern: 'tests/e2e/**/*.cy.{js,jsx,ts,tsx}',
arquivo de suporte: 'tests/support/e2e.ts',
       video: false,
       screenshotOnRunFailure: true,

configuraçãoNodeEvents( on, config) {
         // implement node event listeners here
       },
},

     retries: {
       runMode: 2,
       openMode: 0,
     },

     defaultCommandTimeout: 15000,
     requestTimeout: 30000,
     responseTimeout: 3000