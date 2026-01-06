<!-- Alimentado por BMAD-CORE™ -->

# Configuração de Framework de Teste

**ID do Fluxo de Trabalho**: `_bmad/bmm/testarch/framework`
**Versão**: 4.0 (BMad v6)

---

## Visão Geral

Inicializar uma arquitetura de framework de teste pronta para produção (Playwright ou Cypress) com fixtures, auxiliares, configuração e melhores práticas. Este fluxo de trabalho constrói a infraestrutura de teste completa para aplicações web modernas.

---

## Requisitos de Pré-voo

**Crítico:** Verifique estes requisitos antes de prosseguir. Se algum falhar, PARE e notifique o usuário.

- ✅ `package.json` existe na raiz do projeto
- ✅ Nenhuma ferramenta de teste E2E moderna já está configurada (verifique se existem `playwright.config.*` ou `cypress.config.*`)
- ✅ Contexto arquitetural/pilha disponível (tipo de projeto, empacotador, dependências)

---

## Passo 1: Executar Verificações de Pré-voo

### Ações

1. **Validar package.json**
   - Ler `{project-root}/package.json`
   - Extrair tipo de projeto (React, Vue, Angular, Next.js, Node, etc.)
   - Identificar empacotador (Vite, Webpack, Rollup, esbuild)
   - Notar dependências de teste existentes

2. **Verificar por Framework Existente**
   - Pesquisar por `playwright.config.*`, `cypress.config.*`, `cypress.json`
   - Verificar `package.json` por dependências `@playwright/test` ou `cypress`
   - Se encontrado, PARE com mensagem: "Framework de teste existente detectado. Use o fluxo de trabalho `upgrade-framework` em vez disso."

3. **Reunir Contexto**
   - Procurar por documentos de arquitetura (`architecture.md`, `tech-spec*.md`)
   - Verificar documentação de API ou listas de endpoint
   - Identificar requisitos de autenticação

**Condição de Parada:** Se verificações de pré-voo falharem, pare imediatamente e reporte qual requisito falhou.

---

## Passo 2: Construir Framework

### Ações

1. **Seleção de Framework**

   **Lógica Padrão:**
   - **Playwright** (recomendado para):
     - Repositórios grandes (100+ arquivos)
     - Aplicações críticas de desempenho
     - Suporte multi-navegador necessário
     - Fluxos de usuário complexos exigindo depuração de vídeo/trace
     - Projetos exigindo paralelismo de worker

   - **Cypress** (recomendado para):
     - Pequenas equipes priorizando experiência do desenvolvedor
     - Foco em teste de componente
     - Recarregamento em tempo real durante desenvolvimento de teste
     - Requisitos de configuração mais simples

   **Estratégia de Detecção:**
   - Verificar `package.json` por preferência existente
   - Considerar variável `project_size` da configuração do fluxo de trabalho
   - Usar variável `framework_preference` se definida
   - Padrão para **Playwright** se incerto

2. **Criar Estrutura de Diretório**

   ```
   {project-root}/
   ├── tests/                        # Diretório raiz de teste
   │   ├── e2e/                      # Arquivos de teste (usuários organizam conforme necessário)
   │   ├── support/                  # Infraestrutura do framework (padrão chave)
   │   │   ├── fixtures/             # Fixtures de teste (dados, mocks)
   │   │   ├── helpers/              # Funções utilitárias
   │   │   └── page-objects/         # Modelos de objeto de página (opcional)
   │   └── README.md                 # Documentação da suíte de teste
   ```

   **Nota**: Usuários organizam arquivos de teste (e2e/, api/, integration/, component/) conforme necessário. A pasta **support/** é o padrão crítico para fixtures e auxiliares usados através dos testes.

3. **Gerar Arquivo de Configuração**

   **Para Playwright** (`playwright.config.ts` ou `playwright.config.js`):

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

   **Para Cypress** (`cypress.config.ts` ou `cypress.config.js`):

   ```typescript
   import { defineConfig } from 'cypress';

   export default defineConfig({
     e2e: {
       baseUrl: process.env.BASE_URL || 'http://localhost:3000',
       specPattern: 'tests/e2e/**/*.cy.{js,jsx,ts,tsx}',
       supportFile: 'tests/support/e2e.ts',
       video: false,
       screenshotOnRunFailure: true,

       setupNodeEvents(on, config) {
         // implement node event listeners here
       },
     },

     retries: {
       runMode: 2,
       openMode: 0,
     },

     defaultCommandTimeout: 15000,
     requestTimeout: 30000,
     responseTimeout: 30000,
     pageLoadTimeout: 60000,
   });
   ```

4. **Gerar Configuração de Ambiente**

   Criar `.env.example`:

   ```bash
   # Configuração de Ambiente de Teste
   TEST_ENV=local
   BASE_URL=http://localhost:3000
   API_URL=http://localhost:3001/api

   # Autenticação (se aplicável)
   TEST_USER_EMAIL=test@example.com
   TEST_USER_PASSWORD=

   # Sinalizadores de Recurso (se aplicável)
   FEATURE_FLAG_NEW_UI=true

   # Chaves de API (se aplicável)
   TEST_API_KEY=
   ```

5. **Gerar Arquivo de Versão Node**

   Criar `.nvmrc`:

   ```
   20.11.0
   ```

   (Usar versão Node do `.nvmrc` existente ou padrão para LTS atual)

6. **Implementar Arquitetura de Fixture**

   **Referência Base de Conhecimento**: `testarch/knowledge/fixture-architecture.md`

   Criar `tests/support/fixtures/index.ts`:

   ```typescript
   import { test as base } from '@playwright/test';
   import { UserFactory } from './factories/user-factory';

   type TestFixtures = {
     userFactory: UserFactory;
   };

   export const test = base.extend<TestFixtures>({
     userFactory: async ({}, use) => {
       const factory = new UserFactory();
       await use(factory);
       await factory.cleanup(); // Auto-limpeza
     },
   });

   export { expect } from '@playwright/test';
   ```

7. **Implementar Fábricas de Dados**

   **Referência Base de Conhecimento**: `testarch/knowledge/data-factories.md`

   Criar `tests/support/fixtures/factories/user-factory.ts`:

   ```typescript
   import { faker } from '@faker-js/faker';

   export class UserFactory {
     private createdUsers: string[] = [];

     async createUser(overrides = {}) {
       const user = {
         email: faker.internet.email(),
         name: faker.person.fullName(),
         password: faker.internet.password({ length: 12 }),
         ...overrides,
       };

       // Chamada de API para criar usuário
       const response = await fetch(`${process.env.API_URL}/users`, {
         method: 'POST',
         headers: { 'Content-Type': 'application/json' },
         body: JSON.stringify(user),
       });

       const created = await response.json();
       this.createdUsers.push(created.id);
       return created;
     }

     async cleanup() {
       // Deletar todos os usuários criados
       for (const userId of this.createdUsers) {
         await fetch(`${process.env.API_URL}/users/${userId}`, {
           method: 'DELETE',
         });
       }
       this.createdUsers = [];
     }
   }
   ```

8. **Gerar Testes de Exemplo**

   Criar `tests/e2e/example.spec.ts`:

   ```typescript
   import { test, expect } from '../support/fixtures';

   test.describe('Example Test Suite', () => {
     test('should load homepage', async ({ page }) => {
       await page.goto('/');
       await expect(page).toHaveTitle(/Home/i);
     });

     test('should create user and login', async ({ page, userFactory }) => {
       // Create test user
       const user = await userFactory.createUser();

       // Login
       await page.goto('/login');
       await page.fill('[data-testid="email-input"]', user.email);
       await page.fill('[data-testid="password-input"]', user.password);
       await page.click('[data-testid="login-button"]');

       // Assert login success
       await expect(page.locator('[data-testid="user-menu"]')).toBeVisible();
     });
   });
   ```

9. **Atualizar Scripts package.json**

   Adicionar script de teste mínimo ao `package.json`:

   ```json
   {
     "scripts": {
       "test:e2e": "playwright test"
     }
   }
   ```

   **Nota**: Usuários podem adicionar scripts adicionais conforme necessário (e.g., `--ui`, `--headed`, `--debug`, `show-report`).

10. **Gerar Documentação**

    Criar `tests/README.md` com instruções de configuração (ver entregáveis Passo 3).

---

## Passo 3: Entregáveis

### Artefatos Primários Criados

1. **Arquivo de Configuração**
   - `playwright.config.ts` ou `cypress.config.ts`
   - Timeouts: ação 15s, navegação 30s, teste 60s
   - Repórteres: HTML + JUnit XML

2. **Estrutura de Diretório**
   - `tests/` com subdiretórios `e2e/`, `api/`, `support/`
   - `support/fixtures/` para fixtures de teste
   - `support/helpers/` para funções utilitárias

3. **Configuração de Ambiente**
   - `.env.example` com `TEST_ENV`, `BASE_URL`, `API_URL`
   - `.nvmrc` com versão Node

4. **Infraestrutura de Teste**
   - Arquitetura de fixture (padrão `mergeTests`)
   - Fábricas de dados (baseadas em faker, com auto-limpeza)
   - Testes de exemplo demonstrando padrões

5. **Documentação**
   - `tests/README.md` com instruções de configuração
   - Comentários em arquivos de config explicando opções

### Conteúdo do README

O `tests/README.md` gerado deve incluir:

- **Instruções de Configuração**: Como instalar dependências, configurar ambiente
- **Rodando Testes**: Comandos para execução local, modo com cabeça, modo de depuração
- **Visão Geral da Arquitetura**: Padrão de fixture, fábricas de dados, objetos de página
- **Melhores Práticas**: Estratégia de seletor (data-testid), isolamento de teste, limpeza
- **Integração CI**: Como testes rodam no pipeline de CI/CD
- **Referências da Base de Conhecimento**: Links para fragmentos de conhecimento TEA relevantes

---

## Notas Importantes

### Integração com Base de Conhecimento

**Crítico:** Verifique a configuração e carregue os fragmentos apropriados.

Leia `{config_source}` e verifique `config.tea_use_playwright_utils`.

**Se `config.tea_use_playwright_utils: true` (Integração Playwright Utils):**

Consulte `{project-root}/_bmad/bmm/testarch/tea-index.csv` e carregue:

- `overview.md` - Instalação de playwright utils e princípios de design
- `fixtures-composition.md` - Composição mergeTests com playwright-utils
- `auth-session.md` - Configuração de persistência de token (se auth necessário)
- `api-request.md` - Utilitários de teste de API (se testes de API planejados)
- `burn-in.md` - Seleção de teste inteligente para CI (recomendar durante configuração de framework)
- `network-error-monitor.md` - Detecção automática de erro HTTP (recomendar em fixtures mescladas)
- `data-factories.md` - Padrões de fábrica com faker (498 linhas, 5 exemplos)

Recomendar instalação de playwright-utils:

```bash
npm install -D @seontechnologies/playwright-utils
```

Recomendar adicionar burn-in e network-error-monitor a fixtures mescladas para confiabilidade aprimorada.

**Se `config.tea_use_playwright_utils: false` (Padrões Tradicionais):**

Consulte `{project-root}/_bmad/bmm/testarch/tea-index.csv` e carregue:

- `fixture-architecture.md` - Função pura → fixture → composição `mergeTests` com auto-limpeza (406 linhas, 5 exemplos)
- `data-factories.md` - Fábricas baseadas em Faker com substituições, fábricas aninhadas, semeadura de API, auto-limpeza (498 linhas, 5 exemplos)
- `network-first.md` - Salvaguardas de teste network-first: interceptar antes de navegar, captura HAR, espera determinística (489 linhas, 5 exemplos)
- `playwright-config.md` - Configuração específica de Playwright: baseada em ambiente, padrões de timeout, saída de artefato, paralelização, config de projeto (722 linhas, 5 exemplos)
- `test-quality.md` - Princípios de design de teste: determinístico, isolado com limpeza, afirmações explícitas, limites de comprimento/tempo (658 linhas, 5 exemplos)

### Orientação Específica de Framework

**Vantagens do Playwright:**

- Paralelismo de worker (significativamente mais rápido para grandes suítes)
- Visualizador de trace (depuração poderosa com capturas de tela, rede, console)
- Suporte multi-linguagem (TypeScript, JavaScript, Python, C#, Java)
- Capacidades de teste de API integradas
- Melhor manuseio de múltiplos contextos de navegador

**Vantagens do Cypress:**

- Experiência do desenvolvedor superior (recarregamento em tempo real)
- Excelente para teste de componente (Cypress CT ou use Vitest)
- Configuração mais simples para equipes pequenas
- Melhor adequado para modo de observação durante desenvolvimento

**Evite Cypress quando:**

- Cadeias de API são pesadas e complexas
- Cenários de múltiplas abas/janelas são comuns
- Paralelismo de worker é crítico para desempenho de CI

### Estratégia de Seletor

**Sempre recomende**:

- Atributos `data-testid` para elementos de UI
- Atributos `data-cy` se Cypress for escolhido
- Evite seletores CSS frágeis ou XPath

### Teste de Contrato

Para arquiteturas de microserviços, **recomende Pact** para teste de contrato orientado ao consumidor junto com testes E2E.

### Artefatos de Falha

Configure captura **apenas em falha**:

- Screenshots: apenas em falha
- Vídeos: reter em falha (deletar em sucesso)
- Traces: reter em falha (Playwright)

Isso reduz a sobrecarga de armazenamento enquanto mantém a capacidade de depuração.

---

## Resumo de Saída

Após completar este fluxo de trabalho, forneça um resumo:

```markdown
## Andaime de Framework Completo

**Framework Selecionado**: Playwright (ou Cypress)

**Artefatos Criados**:

- ✅ Arquivo de configuração: `playwright.config.ts`
- ✅ Estrutura de diretório: `tests/e2e/`, `tests/support/`
- ✅ Config de ambiente: `.env.example`
- ✅ Versão Node: `.nvmrc`
- ✅ Arquitetura de fixture: `tests/support/fixtures/`
- ✅ Fábricas de dados: `tests/support/fixtures/factories/`
- ✅ Testes de exemplo: `tests/e2e/example.spec.ts`
- ✅ Documentação: `tests/README.md`

**Próximos Passos**:

1. Copie `.env.example` para `.env` e preencha variáveis de ambiente
2. Execute `npm install` para instalar dependências de teste
3. Execute `npm run test:e2e` para executar testes de exemplo
4. Revise `tests/README.md` para instruções de configuração detalhadas

**Referências da Base de Conhecimento Aplicadas**:

- Padrão de arquitetura de fixture (funções puras + mergeTests)
- Fábricas de dados com auto-limpeza (baseadas em faker)
- Salvaguardas de teste network-first
- Captura de artefato apenas em falha
```

---

## Validação

Após completar todos os passos, verifique:

- [ ] Arquivo de configuração criado e válido
- [ ] Estrutura de diretório existe
- [ ] Configuração de ambiente gerada
- [ ] Testes de exemplo rodam com sucesso
- [ ] Documentação completa e precisa
- [ ] Nenhum erro ou aviso durante o andaime

Consulte `checklist.md` para critérios de validação abrangentes.
