<!-- Powered by BMAD-CORE™ -->

# Quadro de níveis de ensaio

Guia abrangente para determinar níveis de teste adequados (unidade, integração, E2E) para diferentes cenários.

## Matriz de decisão do nível de ensaio

### Testes unitários

**Quando utilizar:**

- Teste de funções puras e lógica empresarial
- Correcção do algoritmo
- Validação de entrada e transformação de dados
- Tratamento de erros em componentes isolados
- Cálculos complexos ou máquinas de estado

**Características:**

- Execução rápida (feedback imediato)
- Sem dependências externas (DB, API, sistema de arquivos)
- Altamente sustentável e estável
- Falhas fáceis de depurar

**Exemplo de cenários:**

```yaml
unit_test:
  component: 'PriceCalculator'
  scenario: 'Calculate discount with multiple rules'
  justification: 'Complex business logic with multiple branches'
  mock_requirements: 'None - pure function'

```

### Testes de Integração

**Quando utilizar:**

- Verificação da interacção dos componentes
- Operações e transações de banco de dados
- Contratos de Endpoint API
- Comunicação entre serviços
- Middleware e comportamento interceptor

**Características:**

- Tempo de execução moderado
- Testes de limites de componentes
- Pode utilizar bases de dados de testes ou contentores
- Valida pontos de integração do sistema

**Exemplo de cenários:**

```yaml
integration_test:
  components: ['UserService', 'AuthRepository']
  scenario: 'Create user with role assignment'
  justification: 'Critical data flow between service and persistence'
  test_environment: 'In-memory database'

```

### Testes de fim a fim

**Quando utilizar:**

- Viagens críticas do usuário
- Fluxos de trabalho entre sistemas
- Testes de regressão visual
- Conformidade e requisitos regulamentares
- Validação final antes da libertação

**Características:**

- Execução mais lenta
- Testa fluxos de trabalho completos
- Requer configuração completa do ambiente
- Muito realista, mas mais frágil.

**Exemplo de cenários:**

```yaml
e2e_test:
  journey: 'Complete checkout process'
  scenario: 'User purchases with saved payment method'
  justification: 'Revenue-critical path requiring full validation'
  environment: 'Staging with test payment gateway'

```

## Regras de seleção do nível de teste

### Testes de Unidade Favor Quando:

- Lógica pode ser isolada
- Sem efeitos secundários envolvidos
- Retorno rápido necessário
- Alta complexidade ciclomática

### Testes de Integração Favorecida Quando:

- Testando camada de persistência
- Validação de contratos de serviços
- Teste de middleware/interceptores
- Limites de componentes críticos

### Testes de favor E2E Quando:

- Caminhos críticos voltados para o usuário
- Interacções multi- sistema
- Cenários de conformidade regulamentar
- Regressão visual importante

## Anti-padrão para evitar

- Teste E2E para validação lógica de negócios
- Comportamento da estrutura de teste da unidade
- Integração testando bibliotecas de terceiros
- Duplicar a cobertura entre os níveis

## Guarda de Cobertura Duplicada

**Antes de adicionar qualquer teste, verifique:**

1. Isto já está testado em um nível mais baixo?
2. Pode um teste de unidade cobrir isso em vez de integração?
3. Um teste de integração pode cobrir isso em vez de E2E?

**A sobreposição da cobertura só é aceitável quando:**

- Testando diferentes aspectos (unidade: lógica, integração: interação, e2e: experiência do usuário)
- Caminhos críticos que exigem defesa em profundidade
- Prevenção de regressão para funcionalidade previamente quebrada

## Convenções de nomeação de testes
BMADPROTECT044end BMADPROTECT011end
BMADPROTECT043end BMADPROTECT010end
BMADPROTECT042end BMADPROTECT009end

## Formato do ID de ensaio

`{EPIC}.{STORY}-{LEVEL}-{SEQ}`

Examples:

- `1.3-UNIT-001`
- `1.3-INT-002`
- `1.3-E2E-001`

## Exemplos de códigos reais

### Exemplo 1: Teste E2E (Viagem completa do usuário)

**Cenário**: O usuário faz login, navega até o painel e faz uma ordem.

«``typescript
// testes/e2e/checkout-flow.spec.ts
BMADPROTECT034end BMADPROTECT041end de '@ playwright/test';
BMADPROTECT033end BMADPROTECT040end de '../utils-teste/fábricas';

teste.descreva ("Fundo de Verificação", () => {
  test('user can complete purchase with saved payment method', async ({ page, apiRequest }) => {
    // Setup: Seed data via API (fast!)
    const user = createUser({ email: 'buyer@example.com', hasSavedCard: true });
const produto = criarProduto({ name: 'Widget', price: 29.99, stock: 10 });

BMADPROTECT029end apiRequest.post('/api/usuários', { data: user });
BMADPROTECT028end apiRequest.post('/api/products', { data: product });

// Primeira rede: Interceptar ANTES da ação
const loginPromete = page.waitForResponse('**/api/auth/login');
const cartPromete = page.waitForResponse('**/api/cart');
const orderPromise = page.waitForResponse('**/api/orders');

Passo 1: Login
await page.goto('/login');
await page.fill('[data-testid="email"], user.email);
await page.fill('[data-testid="password"]', 'password123');
await page.click('[data-testid="login-botton"]');
await loginPromete;

// Asserta: Painel visível
await espera(página). para HaveURL('/dashboard');
await expect(page.getByText(`Welcome, ${user.name}`)).ToBeVisible();

Passo 2: Adicionar produto ao carrinho
BMADPROTECT017End page.goto(`/products/${product.id}`);
await page.click('[data-testid="add-to-cart"]');
await cartP