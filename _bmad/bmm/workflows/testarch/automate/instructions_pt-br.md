<!-- Alimentado por BMAD-CORE™ -->

# Expansão de Automação de Teste

**ID do Fluxo de Trabalho**: `_bmad/bmm/testarch/automate`
**Versão**: 4.0 (BMad v6)

---

## Visão Geral

Expande a cobertura de automação de teste gerando suítes de teste abrangentes em níveis apropriados (E2E, API, Componente, Unidade) com infraestrutura de suporte. Este fluxo de trabalho opera em **modo duplo**:

1. **Modo Integrado BMad**: Trabalha COM artefatos BMad (história, especificação técnica, PRD, design de teste) para expandir cobertura após implementação de história
2. **Modo Autônomo**: Trabalha SEM artefatos BMad - analisa base de código existente e gera testes independentemente

**Princípio Central**: Gerar testes priorizados e determinísticos que evitam cobertura duplicada e seguem melhores práticas de teste.

---

## Requisitos de Pré-voo

**Flexível:** Este fluxo de trabalho pode rodar com pré-requisitos mínimos. Apenas PARE se o framework estiver completamente ausente.

### Obrigatório (Sempre)

- ✅ Andaime de framework configurado (execute fluxo de trabalho `framework` se ausente)
- ✅ Configuração de framework de teste disponível (playwright.config.ts ou cypress.config.ts)

### Opcional (Modo Integrado BMad)

- Markdown da história com critérios de aceite (melhora o direcionamento da cobertura)
- Especificação técnica ou PRD (fornece contexto arquitetural)
- Documento de design de teste (fornece contexto de risco/prioridade)

### Opcional (Modo Autônomo)

- Código fonte para analisar (implementação de funcionalidade)
- Testes existentes (para análise de lacunas)

**Se framework estiver ausente:** PARE com mensagem: "Andaime de framework necessário. Execute `bmad tea *framework` primeiro."

---

## Passo 1: Determinar Modo de Execução e Carregar Contexto

### Ações

1. **Detectar Modo de Execução**

   Verificar se artefatos BMad estão disponíveis:
   - Se variável `{story_file}` estiver definida → Modo Integrado BMad
   - Se `{target_feature}` ou `{target_files}` definidos → Modo Autônomo
   - Se nenhum definido → Modo auto-descoberta (varrer base de código por funcionalidades precisando de testes)

2. **Carregar Artefatos BMad (Se Disponível)**

   **Modo Integrado BMad:**
   - Ler markdown da história de `{story_file}`
   - Extrair critérios de aceite e requisitos técnicos
   - Carregar tech-spec.md se `{use_tech_spec}` for verdadeiro
   - Carregar test-design.md se `{use_test_design}` for verdadeiro
   - Carregar PRD.md se `{use_prd}` for verdadeiro
   - Nota: Estes são **aprimoramentos opcionais**, não requisitos rígidos

   **Modo Autônomo:**
   - Pular carregamento de artefato BMad
   - Prosseguir diretamente para análise de código fonte

3. **Carregar Configuração de Framework**
   - Ler config de framework de teste (playwright.config.ts ou cypress.config.ts)
   - Identificar estrutura de diretório de teste de `{test_dir}`
   - Verificar padrões de teste existentes em `{test_dir}`
   - Notar capacidades do executor de teste (execução paralela, fixtures, etc.)

4. **Analisar Cobertura de Teste Existente**

   Se `{analyze_coverage}` for verdadeiro:
   - Pesquisar `{test_dir}` por arquivos de teste existentes
   - Identificar funcionalidades testadas vs não testadas
   - Mapear testes para arquivos fonte (lacunas de cobertura)
   - Verificar padrões de fixture e fábrica existentes

5. **Verificar Sinalizador Playwright Utils**

   Ler `{config_source}` e verificar `config.tea_use_playwright_utils`.

6. **Carregar Fragmentos da Base de Conhecimento**

   **Crítico:** Consultar `{project-root}/_bmad/bmm/testarch/tea-index.csv` para carregar:

   **Padrões de Teste Centrais (Sempre carregar):**
   - `test-levels-framework.md` - Seleção de nível de teste (E2E vs API vs Componente vs Unidade com matriz de decisão, 467 linhas, 4 exemplos)
   - `test-priorities-matrix.md` - Classificação de prioridade (P0-P3 com pontuação automatizada, mapeamento de risco, 389 linhas, 2 exemplos)
   - `data-factories.md` - Padrões de fábrica com faker (substituições, fábricas aninhadas, semeadura de API, 498 linhas, 5 exemplos)
   - `selective-testing.md` - Estratégias de execução de teste direcionadas (baseadas em tag, filtros de spec, baseadas em diff, regras de promoção, 727 linhas, 4 exemplos)
   - `ci-burn-in.md` - Padrões de detecção de teste instável (burn-in de 10 iterações, sharding, execução seletiva, 678 linhas, 4 exemplos)
   - `test-quality.md` - Princípios de design de teste (determinístico, isolado, afirmações explícitas, limites de comprimento/tempo, 658 linhas, 5 exemplos)

   **Se `config.tea_use_playwright_utils: true` (Integração Playwright Utils - Todos Utilitários):**
   - `overview.md` - Instalação de playwright utils, princípios de design, padrões de fixture
   - `api-request.md` - Cliente HTTP tipado com validação de esquema
   - `network-recorder.md` - Gravação/reprodução HAR para testes offline
   - `auth-session.md` - Persistência de token e suporte multi-usuário
   - `intercept-network-call.md` - Espião/stub de rede com análise JSON automática
   - `recurse.md` - Polling estilo Cypress para condições assíncronas
   - `log.md` - Registro integrado ao relatório Playwright
   - `file-utils.md` - Leitura e validação de CSV/XLSX/PDF/ZIP
   - `burn-in.md` - Seleção de teste inteligente (relevante para geração de teste CI)
   - `network-error-monitor.md` - Detecção automática de erro HTTP
   - `fixtures-composition.md` - Padrões de composição mergeTests

   **Se `config.tea_use_playwright_utils: false` (Padrões Tradicionais):**
   - `fixture-architecture.md` - Padrões de fixture de teste (função pura → fixture → mergeTests, auto-limpeza, 406 linhas, 5 exemplos)
   - `network-first.md` - Padrões de interceptação de rota (interceptar antes de navegar, captura HAR, espera determinística, 489 linhas, 5 exemplos)

   **Conhecimento de Cura (Se `{auto_heal_failures}` for verdadeiro):**
   - `test-healing-patterns.md` - Padrões de falha comuns e correções automatizadas (seletores obsoletos, condições de corrida, dados dinâmicos, erros de rede, esperas rígidas, 648 linhas, 5 exemplos)
   - `selector-resilience.md` - Guia de depuração e refatoração de seletor (data-testid > ARIA > texto > hierarquia CSS, anti-padrões, 541 linhas, 4 exemplos)
   - `timing-debugging.md` - Identificação e correções de condição de corrida (network-first, espera determinística, depuração assíncrona, 370 linhas, 3 exemplos)

---

## Passo 2: Identificar Alvos de Automação

### Ações

1. **Determinar O Que Precisa de Teste**

   **Modo Integrado BMad (história disponível):**
   - Mapear critérios de aceite da história para cenários de teste
   - Identificar funcionalidades implementadas nesta história
   - Verificar se história tem testes ATDD existentes (do fluxo de trabalho `*atdd`)
   - Expandir além de ATDD com casos de borda e caminhos negativos

   **Modo Autônomo (sem história):**
   - Se `{target_feature}` especificado: Analisar essa funcionalidade específica
   - Se `{target_files}` especificado: Analisar esses arquivos específicos
   - Se `{auto_discover_features}` for verdadeiro: Varrer `{source_dir}` por funcionalidades
   - Priorizar funcionalidades com:
     - Nenhuma cobertura de teste (maior prioridade)
     - Lógica de negócio complexa
     - Integrações externas (chamadas de API, banco de dados, auth)
     - Caminhos de usuário críticos (login, checkout, etc.)

2. **Aplicar Framework de Seleção de Nível de Teste**

   **Referência Base de Conhecimento**: `test-levels-framework.md`

   Para cada funcionalidade ou critério de aceite, determinar nível de teste apropriado:

   **E2E (Ponta-a-Ponta)**:
   - Jornadas de usuário críticas (login, checkout, fluxos principais)
   - Integração multi-sistema
   - Cenários completos voltados ao usuário
   - Características: Alta confiança, lento, frágil

   **API (Integração)**:
   - Validação de lógica de negócio
   - Contratos de serviço e transformações de dados
   - Integração de backend sem UI
   - Características: Feedback rápido, estável, bom equilíbrio

   **Componente**:
   - Comportamento de componente UI (botões, formulários, modais)
   - Teste de interação (clique, hover, teclado)
   - Gerenciamento de estado dentro do componente
   - Características: Rápido, isolado, granular

   **Unidade**:
   - Lógica de negócio pura e algoritmos
   - Casos de borda e tratamento de erro
   - Dependências mínimas
   - Características: Mais rápido, mais granular

3. **Evitar Cobertura Duplicada**

   **Princípio crítico:** Não teste o mesmo comportamento em múltiplos níveis a menos que necessário
   - Use E2E para caminho feliz crítico apenas
   - Use testes de API para variações de lógica de negócio
   - Use testes de componente para casos de borda de interação UI
   - Use testes de unidade para casos de borda de lógica pura

   **Exemplo:**
   - E2E: Usuário pode logar com credenciais válidas → Dashboard carrega
   - API: POST /auth/login retorna 401 para credenciais inválidas
   - API: POST /auth/login retorna 200 e token JWT para credenciais válidas
   - Componente: LoginForm desabilita botão de envio quando campos estão vazios
   - Unidade: validateEmail() retorna falso para endereços de email malformados

4. **Atribuir Prioridades de Teste**

   **Referência Base de Conhecimento**: `test-priorities-matrix.md`

   **P0 (Crítico - Todo commit)**:
   - Caminhos de usuário críticos que devem sempre funcionar
   - Funcionalidade crítica de segurança (auth, permissões)
   - Cenários de integridade de dados
   - Rodar em ganchos pré-commit ou verificações de PR

   **P1 (Alto - PR para main)**:
   - Funcionalidades importantes com alto impacto no usuário
   - Pontos de integração entre sistemas
   - Tratamento de erro para falhas comuns
   - Rodar antes de fundir na branch principal

   **P2 (Médio - Noturno)**:
   - Casos de borda com impacto moderado
   - Variações de funcionalidade menos críticas
   - Teste de desempenho/carga
   - Rodar em builds de CI noturnos

   **P3 (Baixo - Sob demanda)**:
   - Validações bom-ter
   - Funcionalidades raramente usadas
   - Cenários de teste exploratório
   - Rodar manualmente ou semanalmente

   **Variáveis de Prioridade:**
   - `{include_p0}` - Sempre incluir (padrão: verdadeiro)
   - `{include_p1}` - Prioridade alta (padrão: verdadeiro)
   - `{include_p2}` - Prioridade média (padrão: verdadeiro)
   - `{include_p3}` - Prioridade baixa (padrão: falso)

5. **Criar Plano de Cobertura de Teste**

   Documentar o que será testado em cada nível com prioridades:

   ```markdown
   ## Plano de Cobertura de Teste

   ### Testes E2E (P0)

   - Login de usuário com credenciais válidas → Dashboard carrega
   - Logout de usuário → Redireciona para página de login

   ### Testes de API (P1)

   - POST /auth/login - credenciais válidas → 200 + token JWT
   - POST /auth/login - credenciais inválidas → 401 + mensagem de erro
   - POST /auth/login - campos faltando → 400 + erros de validação

   ### Testes de Componente (P1)

   - LoginForm - campos vazios → botão de envio desabilitado
   - LoginForm - entrada válida → botão de envio habilitado

   ### Testes de Unidade (P2)

   - validateEmail() - email válido → retorna verdadeiro
   - validateEmail() - email malformado → retorna falso
   ```

---

## Passo 3: Gerar Infraestrutura de Teste

### Ações

1. **Aprimorar Arquitetura de Fixture**

   **Referência Base de Conhecimento**: `fixture-architecture.md`

   Verificar fixtures existentes em `tests/support/fixtures/`:
   - Se ausente ou incompleto, criar arquitetura de fixture
   - Usar padrão `test.extend()` do Playwright
   - Garantir que todas as fixtures tenham auto-limpeza no teardown

   **Fixtures comuns para criar/aprimorar:**
   - **authenticatedUser**: Usuário com sessão válida (auto-deleta usuário após teste)
   - **apiRequest**: Cliente API autenticado com URL base e cabeçalhos
   - **mockNetwork**: Mocking de rede para serviços externos
   - **testDatabase**: Banco de dados com dados de teste (auto-limpeza após teste)

   **Exemplo de fixture:**

   ```typescript
   // tests/support/fixtures/auth.fixture.ts
   import { test as base } from '@playwright/test';
   import { createUser, deleteUser } from '../factories/user.factory';

   export const test = base.extend({
     authenticatedUser: async ({ page }, use) => {
       // Configuração: Criar e autenticar usuário
       const user = await createUser();
       await page.goto('/login');
       await page.fill('[data-testid="email"]', user.email);
       await page.fill('[data-testid="password"]', user.password);
       await page.click('[data-testid="login-button"]');
       await page.waitForURL('/dashboard');

       // Fornecer ao teste
       await use(user);

       // Limpeza: Deletar usuário automaticamente
       await deleteUser(user.id);
     },
   });
   ```

2. **Aprimorar Fábricas de Dados**

   **Referência Base de Conhecimento**: `data-factories.md`

   Verificar fábricas existentes em `tests/support/factories/`:
   - Se ausente ou incompleto, criar arquitetura de fábrica
   - Usar `@faker-js/faker` para todos os dados aleatórios (sem valores hardcoded)
   - Suportar substituições para cenários de teste específicos

   **Fábricas comuns para criar/aprimorar:**
   - Fábrica de usuário (email, senha, nome, papel)
   - Fábrica de produto (nome, preço, descrição, SKU)
   - Fábrica de pedido (itens, total, status, cliente)

   **Exemplo de fábrica:**

   ```typescript
   // tests/support/factories/user.factory.ts
   import { faker } from '@faker-js/faker';

   export const createUser = (overrides = {}) => ({
     id: faker.number.int(),
     email: faker.internet.email(),
     password: faker.internet.password(),
     name: faker.person.fullName(),
     role: 'user',
     createdAt: faker.date.recent().toISOString(),
     ...overrides,
   });

   export const createUsers = (count: number) => Array.from({ length: count }, () => createUser());

   // Auxiliar de API para limpeza
   export const deleteUser = async (userId: number) => {
     await fetch(`/api/users/${userId}`, { method: 'DELETE' });
   };
   ```

3. **Criar/Aprimorar Utilitários Auxiliares**

   Se `{update_helpers}` for verdadeiro:

   Verificar `tests/support/helpers/` por utilitários comuns:
   - **waitFor**: Auxiliar de polling para condições complexas
   - **retry**: Auxiliar de repetição para operações instáveis
   - **testData**: Auxiliares de geração de dados de teste
   - **assertions**: Auxiliares de afirmação personalizados

   **Exemplo auxiliar:**

   ```typescript
   // tests/support/helpers/wait-for.ts
   export const waitFor = async (condition: () => Promise<boolean>, timeout = 5000, interval = 100): Promise<void> => {
     const startTime = Date.now();
     while (Date.now() - startTime < timeout) {
       if (await condition()) return;
       await new Promise((resolve) => setTimeout(resolve, interval));
     }
     throw new Error(`Condition not met within ${timeout}ms`);
   };
   ```

---

## Passo 4: Gerar Arquivos de Teste

### Ações

1. **Criar Estrutura de Arquivo de Teste**

   ```
   tests/
   ├── e2e/
   │   └── {feature-name}.spec.ts        # Testes E2E (P0-P1)
   ├── api/
   │   └── {feature-name}.api.spec.ts    # Testes de API (P1-P2)
   ├── component/
   │   └── {ComponentName}.test.tsx      # Testes de componente (P1-P2)
   ├── unit/
   │   └── {module-name}.test.ts         # Testes de unidade (P2-P3)
   └── support/
       ├── fixtures/                      # Fixtures de teste
       ├── factories/                     # Fábricas de dados
       └── helpers/                       # Funções utilitárias
   ```

2. **Escrever Testes E2E (Se Aplicável)**

   **Seguir formato Dado-Quando-Então:**

   ```typescript
   import { test, expect } from '@playwright/test';

   test.describe('User Authentication', () => {
     test('[P0] should login with valid credentials and load dashboard', async ({ page }) => {
       // DADO: Usuário está na página de login
       await page.goto('/login');

       // QUANDO: Usuário submete credenciais válidas
       await page.fill('[data-testid="email-input"]', 'user@example.com');
       await page.fill('[data-testid="password-input"]', 'Password123!');
       await page.click('[data-testid="login-button"]');

       // ENTÃO: Usuário é redirecionado para dashboard
       await expect(page).toHaveURL('/dashboard');
       await expect(page.locator('[data-testid="user-name"]')).toBeVisible();
     });

     test('[P1] should display error for invalid credentials', async ({ page }) => {
       // DADO: Usuário está na página de login
       await page.goto('/login');

       // QUANDO: Usuário submete credenciais inválidas
       await page.fill('[data-testid="email-input"]', 'invalid@example.com');
       await page.fill('[data-testid="password-input"]', 'wrongpassword');
       await page.click('[data-testid="login-button"]');

       // ENTÃO: Mensagem de erro é exibida
       await expect(page.locator('[data-testid="error-message"]')).toHaveText('Invalid email or password');
     });
   });
   ```

   **Padrões críticos:**
   - Taggear testes com prioridade: `[P0]`, `[P1]`, `[P2]`, `[P3]` no nome do teste
   - Uma afirmação por teste (testes atômicos)
   - Esperas explícitas (sem esperas rígidas/sleeps)
   - Abordagem network-first (interceptação de rota antes da navegação)
   - Seletores data-testid para estabilidade
   - Estrutura Dado-Quando-Então clara

3. **Escrever Testes de API (Se Aplicável)**

   ```typescript
   import { test, expect } from '@playwright/test';

   test.describe('User Authentication API', () => {
     test('[P1] POST /api/auth/login - should return token for valid credentials', async ({ request }) => {
       // DADO: Credenciais de usuário válidas
       const credentials = {
         email: 'user@example.com',
         password: 'Password123!',
       };

       // QUANDO: Logando via API
       const response = await request.post('/api/auth/login', {
         data: credentials,
       });

       // ENTÃO: Retorna 200 e token JWT
       expect(response.status()).toBe(200);
       const body = await response.json();
       expect(body).toHaveProperty('token');
       expect(body.token).toMatch(/^[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+$/); // Formato JWT
     });

     test('[P1] POST /api/auth/login - should return 401 for invalid credentials', async ({ request }) => {
       // DADO: Credenciais inválidas
       const credentials = {
         email: 'invalid@example.com',
         password: 'wrongpassword',
       };

       // QUANDO: Tentando login
       const response = await request.post('/api/auth/login', {
         data: credentials,
       });

       // ENTÃO: Retorna 401 com erro
       expect(response.status()).toBe(401);
       const body = await response.json();
       expect(body).toMatchObject({
         error: 'Invalid credentials',
       });
     });
   });
   ```

4. **Escrever Testes de Componente (Se Aplicável)**

   **Referência Base de Conhecimento**: `component-tdd.md`

   ```typescript
   import { test, expect } from '@playwright/experimental-ct-react';
   import { LoginForm } from './LoginForm';

   test.describe('LoginForm Component', () => {
     test('[P1] should disable submit button when fields are empty', async ({ mount }) => {
       // DADO: LoginForm está montado
       const component = await mount(<LoginForm />);

       // QUANDO: Formulário é inicialmente renderizado
       const submitButton = component.locator('button[type="submit"]');

       // ENTÃO: Botão de envio está desabilitado
       await expect(submitButton).toBeDisabled();
     });

     test('[P1] should enable submit button when fields are filled', async ({ mount }) => {
       // DADO: LoginForm está montado
       const component = await mount(<LoginForm />);

       // QUANDO: Usuário preenche email e senha
       await component.locator('[data-testid="email-input"]').fill('user@example.com');
       await component.locator('[data-testid="password-input"]').fill('Password123!');

       // ENTÃO: Botão de envio está habilitado
       const submitButton = component.locator('button[type="submit"]');
       await expect(submitButton).toBeEnabled();
     });
   });
   ```

5. **Escrever Testes de Unidade (Se Aplicável)**

   ```typescript
   import { validateEmail } from './validation';

   describe('Email Validation', () => {
     test('[P2] should return true for valid email', () => {
       // DADO: Endereço de email válido
       const email = 'user@example.com';

       // QUANDO: Validando email
       const result = validateEmail(email);

       // ENTÃO: Retorna verdadeiro
       expect(result).toBe(true);
     });

     test('[P2] should return false for malformed email', () => {
       // DADO: Endereços de email malformados
       const invalidEmails = ['notanemail', '@example.com', 'user@', 'user @example.com'];

       // QUANDO/ENTÃO: Cada um deve falhar validação
       invalidEmails.forEach((email) => {
         expect(validateEmail(email)).toBe(false);
       });
     });
   });
   ```

6. **Aplicar Padrão Network-First (testes E2E)**

   **Referência Base de Conhecimento**: `network-first.md`

   **Padrão crítico para prevenir condições de corrida:**

   ```typescript
   test('should load user dashboard after login', async ({ page }) => {
     // CRÍTICO: Interceptar rotas ANTES da navegação
     await page.route('**/api/user', (route) =>
       route.fulfill({
         status: 200,
         body: JSON.stringify({ id: 1, name: 'Test User' }),
       }),
     );

     // AGORA navegue
     await page.goto('/dashboard');

     await expect(page.locator('[data-testid="user-name"]')).toHaveText('Test User');
   });
   ```

7. **Impor Padrões de Qualidade**

   **Para cada teste:**
   - ✅ Usa formato Dado-Quando-Então
   - ✅ Tem nome descritivo e claro com tag de prioridade
   - ✅ Uma afirmação por teste (atômico)
   - ✅ Sem esperas rígidas ou sleeps (usar esperas explícitas)
   - ✅ Auto-limpeza (usa fixtures com auto-limpeza)
   - ✅ Determinístico (sem padrões instáveis)
   - ✅ Rápido (abaixo de {max_test_duration} segundos)
   - ✅ Enxuto (arquivo de teste abaixo de {max_file_lines} linhas)

   **Padrões proibidos:**
   - ❌ Esperas rígidas: `await page.waitForTimeout(2000)`
   - ❌ Fluxo condicional: `if (await element.isVisible()) { ... }`
   - ❌ Try-catch para lógica de teste (usar para limpeza apenas)
   - ❌ Dados de teste hardcoded (usar fábricas)
   - ❌ Page objects (manter testes simples e diretos)
   - ❌ Estado compartilhado entre testes

---

## Passo 5: Executar, Validar & Curar Testes Gerados (NOVO - Fase 2.5)

**Propósito**: Validar automaticamente testes gerados e curar falhas comuns antes da entrega

### Ações

1. **Validar Testes Gerados**

   Sempre validar (auto_validate é sempre verdadeiro):
   - Rodar testes gerados para verificar que funcionam
   - Continuar com cura se config.tea_use_mcp_enhancements for verdadeiro

2. **Rodar Testes Gerados**

   Executar a suíte de testes completa que acabou de ser gerada:

   ```bash
   npx playwright test {generated_test_files}
   ```

   Capturar resultados:
   - Total de testes rodados
   - Contagem de testes passando
   - Contagem de testes falhando
   - Mensagens de erro e stack traces para falhas

3. **Avaliar Resultados**

   **Se TODOS os testes passarem:**
   - ✅ Gerar relatório com resumo de sucesso
   - Prosseguir para Passo 6 (Documentação e Scripts)

   **Se testes FALHAREM:**
   - Verificar configuração config.tea_use_mcp_enhancements
   - Se verdadeiro: Entrar em loop de cura (Passo 5.4)
   - Se falso: Documentar falhas para revisão manual, prosseguir para Passo 6

4. **Loop de Cura (Se config.tea_use_mcp_enhancements for verdadeiro)**

   **Limite de iteração**: 3 tentativas por teste (constante)

   **Para cada teste falhando:**

   **A. Carregar Fragmentos de Conhecimento de Cura**

   Consultar `tea-index.csv` para carregar padrões de cura:
   - `test-healing-patterns.md` - Padrões de falha comuns e correções
   - `selector-resilience.md` - Depuração e refatoração de seletor
   - `timing-debugging.md` - Identificação e correções de condição de corrida

   **B. Identificar Padrão de Falha**

   Analisar mensagem de erro e stack trace para classificar tipo de falha:

   **Falha de Seletor Obsoleto:**
   - Erro contém: "locator resolved to 0 elements", "element not found", "unable to find element"
   - Extrair seletor da mensagem de erro
   - Aplicar cura de seletor (conhecimento de `selector-resilience.md`):
     - Se classe CSS → Substituir por `page.getByTestId()`
     - Se nth() → Substituir por `filter({ hasText })`
     - Se ID → Substituir por data-testid
     - Se XPath complexo → Substituir por papel ARIA

   **Falha de Condição de Corrida:**
   - Erro contém: "timeout waiting for", "element not visible", "timed out retrying"
   - Detectar esperas de rede ausentes ou esperas rígidas no código de teste
   - Aplicar cura de tempo (conhecimento de `timing-debugging.md`):
     - Adicionar interceptação network-first antes de navegar
     - Substituir `waitForTimeout()` por `waitForResponse()`
     - Adicionar esperas de estado de elemento explícitas (`waitFor({ state: 'visible' })`)

   **Falha de Dados Dinâmicos:**
   - Erro contém: "Expected 'User 123' but received 'User 456'", incompatibilidades de timestamp
   - Identificar afirmações hardcoded
   - Aplicar cura de dados (conhecimento de `test-healing-patterns.md`):
     - Substituir IDs hardcoded por regex (`/User \d+/`)
     - Substituir datas hardcoded por geração dinâmica
     - Capturar valores dinâmicos e usar em afirmações

   **Falha de Erro de Rede:**
   - Erro contém: "API call failed", "500 error", "network error"
   - Detectar interceptação de rota ausente
   - Aplicar cura de rede (conhecimento de `test-healing-patterns.md`):
     - Adicionar `page.route()` ou `cy.intercept()` para mock de API
     - Mockar cenários de erro (500, 429, timeout)

   **Detecção de Espera Rígida:**
   - Varrer código de teste por `page.waitForTimeout()`, `cy.wait(number)`, `sleep()`
   - Aplicar cura de espera rígida (conhecimento de `timing-debugging.md`):
     - Substituir por esperas baseadas em evento
     - Adicionar esperas de resposta de rede
     - Usar mudanças de estado de elemento

   **C. Modo de Cura MCP (Se Ferramentas MCP Disponíveis)**

   Se ferramentas MCP Playwright estiverem disponíveis no seu IDE:

   Usar ferramentas MCP para cura interativa:
   - `playwright_test_debug_test`: Pausar na falha para inspeção visual
   - `browser_snapshot`: Capturar contexto visual no ponto de falha
   - `browser_console_messages`: Recuperar logs de console para erros JS
   - `browser_network_requests`: Analisar atividade de rede
   - `browser_generate_locator`: Gerar melhores seletores interativamente

   Aplicar correções geradas por MCP ao código de teste.

   **D. Modo de Cura Baseado em Padrão (Fallback)**

   Se MCP indisponível, usar análise baseada em padrão:
   - Analisar mensagem de erro e stack trace
   - Corresponder contra padrões de falha da base de conhecimento
   - Aplicar correções programaticamente:
     - Correções de seletor: Usar sugestões de `selector-resilience.md`
     - Correções de tempo: Aplicar padrões de `timing-debugging.md`
     - Correções de dados: Usar padrões de `test-healing-patterns.md`

   **E. Aplicar Correção de Cura**
   - Modificar arquivo de teste com código curado
   - Re-rodar teste para validar correção
   - Se teste passar: Marcar como curado, mover para próxima falha
   - Se teste falhar: Incrementar contagem de iteração, tentar padrão diferente

   **F. Tratamento de Limite de Iteração**

   Após 3 tentativas de cura falhadas:

   Sempre marcar testes incorrigíveis:
   - Marcar teste com `test.fixme()` ao invés de `test()`
   - Adicionar comentário detalhado explicando:
     - Qual falha ocorreu
     - Que cura foi tentada (3 iterações)
     - Por que a cura falhou
     - Investigação manual necessária

   ```typescript
   test.fixme('[P1] should handle complex interaction', async ({ page }) => {
     // FIXME: Cura de teste falhou após 3 tentativas
     // Falha: "Locator 'button[data-action="submit"]' resolved to 0 elements"
     // Correções tentadas:
     //   1. Substituído por page.getByTestId('submit-button') - ainda falhando
     //   2. Substituído por page.getByRole('button', { name: 'Submit' }) - ainda falhando
     //   3. Adicionado waitForLoadState('networkidle') - ainda falhando
     // Investigação manual necessária: Seletor pode exigir mudanças no código da aplicação
     // TODO: Revisar com equipe, pode precisar de data-testid adicionado ao componente de botão
     // Código de teste original...
   });
   ```

   **Nota**: Fluxo de trabalho continua mesmo com testes incorrigíveis (marcados como test.fixme() para revisão manual)

5. **Gerar Relatório de Cura**

   Documentar resultados de cura:

   ```markdown
   ## Relatório de Cura de Teste

   **Auto-Cura Habilitada**: {auto_heal_failures}
   **Modo de Cura**: {use_mcp_healing ? "Assistido por MCP" : "Baseado em Padrão"}
   **Iterações Permitidas**: {max_healing_iterations}

   ### Resultados de Validação

   - **Total de testes**: {total_tests}
   - **Passando**: {passing_tests}
   - **Falhando**: {failing_tests}

   ### Resultados de Cura

   **Curados com Sucesso ({healed_count} testes):**

   - `tests/e2e/login.spec.ts:15` - Seletor obsoleto (classe CSS → data-testid)
   - `tests/e2e/checkout.spec.ts:42` - Condição de corrida (adicionada interceptação network-first)
   - `tests/api/users.spec.ts:28` - Dados dinâmicos (ID hardcoded → padrão regex)

   **Incapaz de Curar ({unfixable_count} testes):**

   - `tests/e2e/complex-flow.spec.ts:67` - Marcado como test.fixme() com investigação manual necessária
     - Falha: Localizador não encontrado após 3 tentativas de cura
     - Requer mudanças no código da aplicação (adicionar data-testid ao componente)

   ### Padrões de Cura Aplicados

   - **Correções de seletor**: 2 (classe CSS → data-testid, nth() → filter())
   - **Correções de tempo**: 1 (adicionada interceptação network-first)
   - **Correções de dados**: 1 (ID hardcoded → regex)

   ### Referências da Base de Conhecimento

   - `test-healing-patterns.md` - Padrões de falha comuns
   - `selector-resilience.md` - Guia de refatoração de seletor
   - `timing-debugging.md` - Prevenção de condição de corrida
   ```

6. **Atualizar Arquivos de Teste com Resultados de Cura**
   - Salvar código de teste curado nos arquivos
   - Marcar testes incorrigíveis com `test.fixme()` e comentários detalhados
   - Preservar lógica de teste original em comentários (para depuração)

---

## Passo 6: Atualizar Documentação e Scripts

### Ações

1. **Atualizar README de Teste**

   Se `{update_readme}` for verdadeiro:

   Criar ou atualizar `tests/README.md` com:
   - Visão geral da estrutura da suíte de teste
   - Como rodar testes (todos, arquivos específicos, por prioridade)
   - Exemplos de uso de fixture e fábrica
   - Convenção de tag de prioridade ([P0], [P1], [P2], [P3])
   - Como escrever novos testes
   - Padrões comuns e anti-padrões

   **Exemplo de seção:**

   ````markdown
   ## Rodando Testes

   ```bash
   # Rodar todos os testes
   npm run test:e2e

   # Rodar por prioridade
   npm run test:e2e -- --grep "@P0"
   npm run test:e2e -- --grep "@P1"

   # Rodar arquivo específico
   npm run test:e2e -- user-authentication.spec.ts

   # Rodar em modo headed
   npm run test:e2e -- --headed

   # Depurar teste específico
   npm run test:e2e -- user-authentication.spec.ts --debug
   ```
   ````

   ## Tags de Prioridade
   - **[P0]**: Caminhos críticos, rodar em todo commit
   - **[P1]**: Prioridade alta, rodar em PR para main
   - **[P2]**: Prioridade média, rodar noturnamente
   - **[P3]**: Prioridade baixa, rodar sob demanda

   ```

   ```

2. **Atualizar Scripts package.json**

   Se `{update_package_scripts}` for verdadeiro:

   Adicionar ou atualizar scripts de execução de teste:

   ```json
   {
     "scripts": {
       "test:e2e": "playwright test",
       "test:e2e:p0": "playwright test --grep '@P0'",
       "test:e2e:p1": "playwright test --grep '@P1|@P0'",
       "test:api": "playwright test tests/api",
       "test:component": "playwright test tests/component",
       "test:unit": "vitest"
     }
   }
   ```

3. **Rodar Suíte de Teste**

   Se `{run_tests_after_generation}` for verdadeiro:
   - Rodar suíte de teste completa localmente
   - Capturar resultados (contagens passando/falhando)
   - Verificar ausência de padrões instáveis (testes devem ser determinísticos)
   - Documentar quaisquer requisitos de configuração ou problemas conhecidos

---

## Passo 6: Gerar Resumo de Automação

### Ações

1. **Criar Documento de Resumo de Automação**

   Salvar em `{output_summary}` com:

   **Modo Integrado BMad:**

   ````markdown
   # Resumo de Automação - {feature_name}

   **Data:** {date}
   **História:** {story_id}
   **Meta de Cobertura:** {coverage_target}

   ## Testes Criados

   ### Testes E2E (P0-P1)

   - `tests/e2e/user-authentication.spec.ts` (2 testes, 87 linhas)
     - [P0] Login com credenciais válidas → Dashboard carrega
     - [P1] Exibir erro para credenciais inválidas

   ### Testes de API (P1-P2)

   - `tests/api/auth.api.spec.ts` (3 testes, 102 linhas)
     - [P1] POST /auth/login - credenciais válidas → 200 + token
     - [P1] POST /auth/login - credenciais inválidas → 401 + erro
     - [P2] POST /auth/login - campos faltando → 400 + validação

   ### Testes de Componente (P1)

   - `tests/component/LoginForm.test.tsx` (2 testes, 45 linhas)
     - [P1] Campos vazios → botão de envio desabilitado
     - [P1] Entrada válida → botão de envio habilitado

   ## Infraestrutura Criada

   ### Fixtures

   - `tests/support/fixtures/auth.fixture.ts` - authenticatedUser com auto-limpeza

   ### Fábricas

   - `tests/support/factories/user.factory.ts` - createUser(), deleteUser()

   ### Auxiliares

   - `tests/support/helpers/wait-for.ts` - Auxiliar de polling para condições complexas

   ## Execução de Teste

   ```bash
   # Rodar todos os novos testes
   npm run test:e2e

   # Rodar por prioridade
   npm run test:e2e:p0  # Apenas caminhos críticos
   npm run test:e2e:p1  # Testes P0 + P1
   ```
   ````

   ## Análise de Cobertura

   **Total de Testes:** 7
   - P0: 1 teste (caminho crítico)
   - P1: 5 testes (prioridade alta)
   - P2: 1 teste (prioridade média)

   **Níveis de Teste:**
   - E2E: 2 testes (jornadas de usuário)
   - API: 3 testes (lógica de negócio)
   - Componente: 2 testes (comportamento UI)

   **Status de Cobertura:**
   - ✅ Todos os critérios de aceite cobertos
   - ✅ Caminho feliz coberto (E2E + API)
   - ✅ Casos de erro cobertos (API)
   - ✅ Validação UI coberta (Componente)
   - ⚠️ Caso de borda: Fluxo de redefinição de senha ainda não coberto (história futura)

   ## Definição de Pronto
   - [x] Todos os testes seguem formato Dado-Quando-Então
   - [x] Todos os testes usam seletores data-testid
   - [x] Todos os testes têm tags de prioridade
   - [x] Todos os testes são auto-limpantes (fixtures com auto-limpeza)
   - [x] Sem esperas rígidas ou padrões instáveis
   - [x] Arquivos de teste abaixo de 300 linhas
   - [x] Todos os testes rodam abaixo de 1.5 minutos cada
   - [x] README atualizado com instruções de execução de teste
   - [x] scripts package.json atualizados

   ## Próximos Passos
   1. Revisar testes gerados com a equipe
   2. Rodar testes no pipeline de CI: `npm run test:e2e`
   3. Integrar com portão de qualidade: `bmad tea *gate`
   4. Monitorar testes instáveis no loop de burn-in

   ````

   **Modo Autônomo:**
   ```markdown
   # Resumo de Automação - {target_feature}

   **Data:** {date}
   **Alvo:** {target_feature} (análise autônoma)
   **Meta de Cobertura:** {coverage_target}

   ## Análise de Funcionalidade

   **Arquivos Fonte Analisados:**
   - `src/auth/login.ts` - Lógica de login e validação
   - `src/auth/session.ts` - Gerenciamento de sessão
   - `src/auth/validation.ts` - Validação de email/senha

   **Cobertura Existente:**
   - Testes E2E: 0 encontrado
   - Testes de API: 0 encontrado
   - Testes de componente: 0 encontrado
   - Testes de unidade: 0 encontrado

   **Lacunas de Cobertura Identificadas:**
   - ❌ Nenhum teste E2E para fluxo de login
   - ❌ Nenhum teste de API para endpoint /auth/login
   - ❌ Nenhum teste de componente para LoginForm
   - ❌ Nenhum teste de unidade para validateEmail()

   ## Testes Criados

   {Mesma estrutura que Modo Integrado BMad}

   ## Recomendações

   1. **Prioridade Alta (P0-P1):**
      - Adicionar teste E2E para fluxo de redefinição de senha
      - Adicionar testes de API para endpoint de atualização de token
      - Adicionar testes de componente para botão de logout

   2. **Prioridade Média (P2):**
      - Adicionar testes de unidade para lógica de timeout de sessão
      - Adicionar teste E2E para funcionalidade "lembrar-me"

   3. **Melhorias Futuras:**
      - Considerar teste de contrato para API de auth
      - Adicionar testes de regressão visual para página de login
      - Configurar loop de burn-in para detecção de teste instável

   ## Definição de Pronto

   {Mesmo checklist que Modo Integrado BMad}
   ````

2. **Fornecer Resumo ao Usuário**

   Saída de resumo conciso:

   ```markdown
   ## Automação Completa

   **Cobertura:** {total_tests} testes criados em {test_levels} níveis
   **Divisão de Prioridade:** P0: {p0_count}, P1: {p1_count}, P2: {p2_count}, P3: {p3_count}
   **Infraestrutura:** {fixture_count} fixtures, {factory_count} fábricas
   **Saída:** {output_summary}

   **Rodar testes:** `npm run test:e2e`
   **Próximos passos:** Revisar testes, rodar em CI, integrar com portão de qualidade
   ```

---

## Notas Importantes

### Operação Modo Duplo

**Modo Integrado BMad** (história disponível):

- Usa critérios de aceite da história para direcionamento de cobertura
- Alinha com avaliação de risco/prioridade do test-design
- Expande testes ATDD com casos de borda e caminhos negativos
- Atualiza rastreamento de status BMad

**Modo Autônomo** (sem história):

- Analisa código fonte independentemente
- Identifica lacunas de cobertura automaticamente
- Gera testes com base na análise de código
- Funciona com qualquer projeto (BMad ou não-BMad)

**Modo Auto-descoberta** (nenhum alvo especificado):

- Varre base de código por funcionalidades precisando de testes
- Prioriza funcionalidades sem cobertura
- Gera plano de teste abrangente

### Evitar Cobertura Duplicada

**Princípio crítico:** Não teste o mesmo comportamento em múltiplos níveis

**Boa cobertura:**

- E2E: Usuário pode logar → Dashboard carrega (caminho feliz crítico)
- API: POST /auth/login retorna códigos de status corretos (variações)
- Componente: LoginForm valida entrada (casos de borda UI)

**Cobertura ruim (duplicada):**

- E2E: Usuário pode logar → Dashboard carrega
- E2E: Usuário pode logar com emails diferentes → Dashboard carrega (duplicação desnecessária)
- API: POST /auth/login retorna 200 (já coberto no E2E)

Use E2E com moderação para caminhos críticos. Use API/Componente para variações e casos de borda.

### Tag de Prioridade

**Taggear cada teste com prioridade no nome do teste:**

```typescript
test('[P0] should login with valid credentials', async ({ page }) => { ... });
test('[P1] should display error for invalid credentials', async ({ page }) => { ... });
test('[P2] should remember login preference', async ({ page }) => { ... });
```

**Permite execução seletiva de teste:**

```bash
# Rodar apenas testes P0 (caminhos críticos)
npm run test:e2e -- --grep "@P0"

# Rodar testes P0 + P1 (pré-fusão)
npm run test:e2e -- --grep "@P0|@P1"
```

### Sem Page Objects

**NÃO crie classes de page object.** Mantenha testes simples e diretos:

```typescript
// ✅ CORRETO: Teste direto
test('should login', async ({ page }) => {
  await page.goto('/login');
  await page.fill('[data-testid="email"]', 'user@example.com');
  await page.click('[data-testid="login-button"]');
  await expect(page).toHaveURL('/dashboard');
});

// ❌ ERRADO: Abstração de Page object
class LoginPage {
  async login(email, password) { ... }
}
```

Use fixtures para configuração/desmontagem, não page objects para ações.

### Apenas Testes Determinísticos

**Sem padrões instáveis permitidos:**

```typescript
// ❌ ERRADO: Espera rígida
await page.waitForTimeout(2000);

// ✅ CORRETO: Espera explícita
await page.waitForSelector('[data-testid="user-name"]');
await expect(page.locator('[data-testid="user-name"]')).toBeVisible();

// ❌ ERRADO: Fluxo condicional
if (await element.isVisible()) {
  await element.click();
}

// ✅ CORRETO: Afirmação determinística
await expect(element).toBeVisible();
await element.click();

// ❌ ERRADO: Try-catch para lógica de teste
try {
  await element.click();
} catch (e) {
  // Teste não deve pegar erros
}

// ✅ CORRETO: Deixar teste falhar se elemento não encontrado
await element.click();
```

### Testes Auto-Limpantes

**Todo teste deve limpar seus dados:**

```typescript
// ✅ CORRETO: Fixture com auto-limpeza
export const test = base.extend({
  testUser: async ({ page }, use) => {
    const user = await createUser();
    await use(user);
    await deleteUser(user.id); // Auto-limpeza
  },
});

// ❌ ERRADO: Limpeza manual (pode ser esquecida)
test('should login', async ({ page }) => {
  const user = await createUser();
  // ... lógica de teste ...
  // Esqueceu de deletar usuário!
});
```

### Limites de Tamanho de Arquivo

**Mantenha arquivos de teste enxutos (abaixo de {max_file_lines} linhas):**

- Se arquivo exceder limite, divida em múltiplos arquivos por área de funcionalidade
- Agrupe testes relacionados em blocos describe
- Extraia configuração comum para fixtures

### Integração com Base de Conhecimento

**Fragmentos Centrais (Auto-carregados no Passo 1):**

- `test-levels-framework.md` - Framework de decisão E2E vs API vs Componente vs Unidade com matriz de características (467 linhas, 4 exemplos)
- `test-priorities-matrix.md` - Classificação P0-P3 com pontuação automatizada e mapeamento de risco (389 linhas, 2 exemplos)
- `fixture-architecture.md` - Composição função pura → fixture → mergeTests com auto-limpeza (406 linhas, 5 exemplos)
- `data-factories.md` - Padrões de fábrica com faker: substituições, fábricas aninhadas, semeadura de API (498 linhas, 5 exemplos)
- `selective-testing.md` - Seleção baseada em tag, filtros de spec, baseada em diff, regras de promoção (727 linhas, 4 exemplos)
- `ci-burn-in.md` - Loop de burn-in de 10 iterações, sharding paralelo, execução seletiva (678 linhas, 4 exemplos)
- `test-quality.md` - Testes determinísticos, isolados com limpeza, afirmações explícitas, otimização de comprimento/tempo (658 linhas, 5 exemplos)
- `network-first.md` - Interceptação antes de navegar, captura HAR, estratégias de espera determinística (489 linhas, 5 exemplos)

**Fragmentos de Cura (Auto-carregados se `{auto_heal_failures}` habilitado):**

- `test-healing-patterns.md` - Padrões de falha comuns: seletores obsoletos, condições de corrida, dados dinâmicos, erros de rede, esperas rígidas (648 linhas, 5 exemplos)
- `selector-resilience.md` - Hierarquia de seletor (data-testid > ARIA > texto > CSS), padrões dinâmicos, refatoração de anti-padrões (541 linhas, 4 exemplos)
- `timing-debugging.md` - Prevenção de condição de corrida, espera determinística, técnicas de depuração assíncrona (370 linhas, 3 exemplos)

**Referência Manual (Opcional):**

- Use `tea-index.csv` para encontrar fragmentos especializados adicionais conforme necessário

---

## Resumo de Saída

Após completar este fluxo de trabalho, forneça um resumo:

````markdown
## Automação Completa

**Modo:** {standalone_mode ? "Autônomo" : "Integrado BMad"}
**Alvo:** {story_id || target_feature || "Funcionalidades auto-descobertas"}

**Testes Criados:**

- E2E: {e2e_count} testes ({p0_count} P0, {p1_count} P1, {p2_count} P2)
- API: {api_count} testes ({p0_count} P0, {p1_count} P1, {p2_count} P2)
- Componente: {component_count} testes ({p1_count} P1, {p2_count} P2)
- Unidade: {unit_count} testes ({p2_count} P2, {p3_count} P3)

**Infraestrutura:**

- Fixtures: {fixture_count} criadas/aprimoradas
- Fábricas: {factory_count} criadas/aprimoradas
- Auxiliares: {helper_count} criados/aprimorados

**Documentação Atualizada:**

- ✅ README de teste com instruções de execução
- ✅ scripts package.json para execução de teste

**Execução de Teste:**

```bash
# Rodar todos os testes
npm run test:e2e

# Rodar por prioridade
npm run test:e2e:p0  # Apenas caminhos críticos
npm run test:e2e:p1  # Testes P0 + P1

# Rodar arquivo específico
npm run test:e2e -- {first_test_file}
```
````

**Status de Cobertura:**

- ✅ {coverage_percentage}% de funcionalidades cobertas
- ✅ Todos os cenários P0 cobertos
- ✅ Todos os cenários P1 cobertos
- ⚠️ {gap_count} lacunas de cobertura identificadas (documentadas no resumo)

**Verificações de Qualidade:**

- ✅ Todos os testes seguem formato Dado-Quando-Então
- ✅ Todos os testes têm tags de prioridade
- ✅ Todos os testes usam seletores data-testid
- ✅ Todos os testes são auto-limpantes
- ✅ Sem esperas rígidas ou padrões instáveis
- ✅ Todos os arquivos de teste abaixo de {max_file_lines} linhas

**Arquivo de Saída:** {output_summary}

**Próximos Passos:**

1. Revisar testes gerados com a equipe
2. Rodar testes no pipeline de CI
3. Monitorar testes instáveis no loop de burn-in
4. Integrar com portão de qualidade: `bmad tea *gate`

**Referências da Base de Conhecimento Aplicadas:**

- Framework de seleção de nível de teste (E2E vs API vs Componente vs Unidade)
- Classificação de prioridade (P0-P3)
- Padrões de arquitetura de fixture com auto-limpeza
- Padrões de fábrica de dados usando faker
- Estratégias de teste seletivo
- Princípios de qualidade de teste

```

---

## Validação

Após completar todos os passos, verifique:

- [ ] Modo de execução determinado (Integrado BMad, Autônomo ou Auto-descoberta)
- [ ] Artefatos BMad carregados se disponíveis (história, tech-spec, test-design, PRD)
- [ ] Configuração de framework carregada
- [ ] Cobertura de teste existente analisada (lacunas identificadas)
- [ ] Fragmentos da base de conhecimento carregados (test-levels, test-priorities, fixture-architecture, data-factories, selective-testing)
- [ ] Alvos de automação identificados (o que precisa de teste)
- [ ] Níveis de teste selecionados apropriadamente (E2E, API, Componente, Unidade)
- [ ] Cobertura duplicada evitada (mesmo comportamento não testado em múltiplos níveis)
- [ ] Prioridades de teste atribuídas (P0, P1, P2, P3)
- [ ] Arquitetura de fixture criada/aprimorada (com auto-limpeza)
- [ ] Fábricas de dados criadas/aprimoradas (usando faker)
- [ ] Utilitários auxiliares criados/aprimorados (se necessário)
- [ ] Testes E2E escritos (Dado-Quando-Então, tags de prioridade, seletores data-testid)
- [ ] Testes de API escritos (Dado-Quando-Então, tags de prioridade, cobertura abrangente)
- [ ] Testes de componente escritos (Dado-Quando-Então, tags de prioridade, comportamento UI)
- [ ] Testes de unidade escritos (Dado-Quando-Então, tags de prioridade, lógica pura)
- [ ] Padrão network-first aplicado (interceptação de rota antes de navegar)
- [ ] Padrões de qualidade impostos (sem esperas rígidas, sem padrões instáveis, auto-limpeza, determinístico)
- [ ] README de teste atualizado (instruções de execução, tags de prioridade, padrões)
- [ ] scripts package.json atualizados (comandos de execução de teste)
- [ ] Suíte de teste rodada localmente (resultados capturados)
- [ ] Testes validados (se auto_validate habilitado)
- [ ] Falhas curadas (se auto_heal_failures habilitado)
- [ ] Relatório de cura gerado (se cura tentada)
- [ ] Testes incorrigíveis marcados com test.fixme() (se houver)
- [ ] Resumo de automação criado (testes, infraestrutura, cobertura, cura, DoD)
- [ ] Arquivo de saída formatado corretamente

Consulte `checklist.md` para critérios de validação abrangentes.
```
