<!-- Powered by BMAD-CORE™ -->

# Framework de Níveis de Teste

Guia abrangente para determinar níveis de teste apropriados (unitário, integração, E2E) para diferentes cenários.

## Matriz de Decisão de Nível de Teste

### Testes Unitários

**Quando usar:**

- Testar funções puras e lógica de negócio
- Correção de algoritmos
- Validação de entrada e transformação de dados
- Tratamento de erro em componentes isolados
- Cálculos complexos ou máquinas de estado

**Características:**

- Execução rápida (feedback imediato)
- Sem dependências externas (DB, API, sistema de arquivos)
- Altamente sustentável e estável
- Fácil de debugar falhas

**Cenários de exemplo:**

```yaml
unit_test:
  component: 'PriceCalculator'
  scenario: 'Calcular desconto com múltiplas regras'
  justification: 'Lógica de negócio complexa com múltiplos ramos'
  mock_requirements: 'Nenhum - função pura'
```

### Testes de Integração

**Quando usar:**

- Verificação de interação de componentes
- Operações de banco de dados e transações
- Contratos de endpoint de API
- Comunicação serviço-a-serviço
- Comportamento de middleware e interceptor

**Características:**

- Tempo de execução moderado
- Testa fronteiras de componentes
- Pode usar bancos de dados de teste ou containers
- Valida pontos de integração do sistema

**Cenários de exemplo:**

```yaml
integration_test:
  components: ['UserService', 'AuthRepository']
  scenario: 'Criar usuário com atribuição de role'
  justification: 'Fluxo de dados crítico entre serviço e persistência'
  test_environment: 'Banco de dados em memória'
```

### Testes End-to-End (E2E)

**Quando usar:**

- Jornadas de usuário críticas
- Fluxos de trabalho entre sistemas
- Teste de regressão visual
- Requisitos de conformidade e regulatórios
- Validação final antes do lançamento

**Características:**

- Execução mais lenta
- Testa fluxos de trabalho completos
- Requer setup de ambiente completo
- Mais realista, mas mais frágil

**Cenários de exemplo:**

```yaml
e2e_test:
  journey: 'Completar processo de checkout'
  scenario: 'Usuário compra com método de pagamento salvo'
  justification: 'Caminho crítico para receita requerendo validação completa'
  environment: 'Staging com gateway de pagamento de teste'
```

## Regras de Seleção de Nível de Teste

### Favoreça Testes Unitários Quando:

- Lógica pode ser isolada
- Sem efeitos colaterais envolvidos
- Feedback rápido necessário
- Alta complexidade ciclomática

### Favoreça Testes de Integração Quando:

- Testar camada de persistência
- Validar contratos de serviço
- Testar middleware/interceptores
- Fronteiras de componentes críticas

### Favoreça Testes E2E Quando:

- Caminhos críticos voltados ao usuário
- Interações multisistema
- Cenários de conformidade regulatória
- Regressão visual importante

## Anti-padrões a Evitar

- Teste E2E para validação de lógica de negócio
- Teste unitário de comportamento de framework
- Teste de integração de bibliotecas de terceiros
- Cobertura duplicada entre níveis

## Proteção Contra Cobertura Duplicada

**Antes de adicionar qualquer teste, verifique:**

1. Isso já foi testado em um nível inferior?
2. Um teste unitário pode cobrir isso em vez de integração?
3. Um teste de integração pode cobrir isso em vez de E2E?

**Sobreposição de cobertura é aceitável apenas quando:**

- Testando diferentes aspectos (unitário: lógica, integração: interação, e2e: experiência do usuário)
- Caminhos críticos exigindo defesa em profundidade
- Prevenção de regressão para funcionalidade quebrada anteriormente

## Convenções de Nomenclatura de Teste

- Unitário: `test_{componente}_{cenario}`
- Integração: `test_{fluxo}_{interacao}`
- E2E: `test_{jornada}_{resultado}`

## Formato de ID de Teste

`{EPICO}.{HISTORIA}-{NIVEL}-{SEQ}`

Exemplos:

- `1.3-UNIT-001`
- `1.3-INT-002`
- `1.3-E2E-001`

## Exemplos de Código Real

### Exemplo 1: Teste E2E (Jornada Completa do Usuário)

**Cenário**: Usuário loga, navega para o dashboard e faz um pedido.

```typescript
// tests/e2e/checkout-flow.spec.ts
import { test, expect } from '@playwright/test';
import { createUser, createProduct } from '../test-utils/factories';

test.describe('Fluxo de Checkout', () => {
  test('usuário pode completar compra com método de pagamento salvo', async ({ page, apiRequest }) => {
    // Setup: Semear dados via API (rápido!)
    const user = createUser({ email: 'buyer@example.com', hasSavedCard: true });
    const product = createProduct({ name: 'Widget', price: 29.99, stock: 10 });

    await apiRequest.post('/api/users', { data: user });
    await apiRequest.post('/api/products', { data: product });

    // Network-first: Interceptar ANTES da ação
    const loginPromise = page.waitForResponse('**/api/auth/login');
    const cartPromise = page.waitForResponse('**/api/cart');
    const orderPromise = page.waitForResponse('**/api/orders');

    // Passo 1: Login
    await page.goto('/login');
    await page.fill('[data-testid="email"]', user.email);
    await page.fill('[data-testid="password"]', 'password123');
    await page.click('[data-testid="login-button"]');
    await loginPromise;

    // Assert: Dashboard visível
    await expect(page).toHaveURL('/dashboard');
    await expect(page.getByText(`Welcome, ${user.name}`)).toBeVisible();

    // Passo 2: Adicionar produto ao carrinho
    await page.goto(`/products/${product.id}`);
    await page.click('[data-testid="add-to-cart"]');
    await cartPromise;
    await expect(page.getByText('Added to cart')).toBeVisible();

    // Passo 3: Checkout com pagamento salvo
    await page.goto('/checkout');
    await expect(page.getByText('Visa ending in 1234')).toBeVisible(); // Cartão salvo
    await page.click('[data-testid="use-saved-card"]');
    await page.click('[data-testid="place-order"]');
    await orderPromise;

    // Assert: Confirmação de pedido
    await expect(page.getByText('Order Confirmed')).toBeVisible();
    await expect(page.getByText(/Order #\d+/)).toBeVisible();
    await expect(page.getByText('$29.99')).toBeVisible();
  });
});
```

**Pontos Chave (E2E)**:

- Testa jornada completa do usuário através de múltiplas páginas
- Setup de API para dados (rápido), UI para asserções (centrado no usuário)
- Interceptação Network-first para prevenir instabilidade
- Valida caminho de receita crítico de ponta a ponta

### Exemplo 2: Teste de Integração (Camada API/Serviço)

**Cenário**: UserService cria usuário e atribui role via AuthRepository.

```typescript
// tests/integration/user-service.spec.ts
import { test, expect } from '@playwright/test';
import { createUser } from '../test-utils/factories';

test.describe('Integração UserService', () => {
  test('deve criar usuário com role admin via API', async ({ request }) => {
    const userData = createUser({ role: 'admin' });

    // Chamada direta de API (sem UI)
    const response = await request.post('/api/users', {
      data: userData,
    });

    expect(response.status()).toBe(201);

    const createdUser = await response.json();
    expect(createdUser.id).toBeTruthy();
    expect(createdUser.email).toBe(userData.email);
    expect(createdUser.role).toBe('admin');

    // Verificar estado do banco de dados
    const getResponse = await request.get(`/api/users/${createdUser.id}`);
    expect(getResponse.status()).toBe(200);

    const fetchedUser = await getResponse.json();
    expect(fetchedUser.role).toBe('admin');
    expect(fetchedUser.permissions).toContain('user:delete');
    expect(fetchedUser.permissions).toContain('user:update');

    // Limpeza
    await request.delete(`/api/users/${createdUser.id}`);
  });

  test('deve validar restrição de unicidade de email', async ({ request }) => {
    const userData = createUser({ email: 'duplicate@example.com' });

    // Criar primeiro usuário
    const response1 = await request.post('/api/users', { data: userData });
    expect(response1.status()).toBe(201);

    const user1 = await response1.json();

    // Tentar email duplicado
    const response2 = await request.post('/api/users', { data: userData });
    expect(response2.status()).toBe(409); // Conflito
    const error = await response2.json();
    expect(error.message).toContain('Email already exists');

    // Limpeza
    await request.delete(`/api/users/${user1.id}`);
  });
});
```

**Pontos Chave (Integração)**:

- Testa camada de serviço + interação com banco de dados
- Sem UI envolvida—validação pura de API
- Foco em lógica de negócio (atribuição de role, restrições)
- Mais rápido que E2E, mais realista que testes unitários

### Exemplo 3: Teste de Componente (Componente UI Isolado)

**Cenário**: Testar componente de botão isoladamente com props e interações de usuário.

```typescript
// src/components/Button.cy.tsx (Cypress Component Test)
import { Button } from './Button';

describe('Componente Button', () => {
  it('deve renderizar com rótulo correto', () => {
    cy.mount(<Button label="Click Me" />);
    cy.contains('Click Me').should('be.visible');
  });

  it('deve chamar handler onClick quando clicado', () => {
    const onClickSpy = cy.stub().as('onClick');
    cy.mount(<Button label="Submit" onClick={onClickSpy} />);

    cy.get('button').click();
    cy.get('@onClick').should('have.been.calledOnce');
  });

  it('deve estar desabilitado quando prop disabled for true', () => {
    cy.mount(<Button label="Disabled" disabled={true} />);
    cy.get('button').should('be.disabled');
    cy.get('button').should('have.attr', 'aria-disabled', 'true');
  });

  it('deve mostrar spinner de carregamento quando loading', () => {
    cy.mount(<Button label="Loading" loading={true} />);
    cy.get('[data-testid="spinner"]').should('be.visible');
    cy.get('button').should('be.disabled');
  });

  it('deve aplicar estilos de variante corretamente', () => {
    cy.mount(<Button label="Primary" variant="primary" />);
    cy.get('button').should('have.class', 'btn-primary');

    cy.mount(<Button label="Secondary" variant="secondary" />);
    cy.get('button').should('have.class', 'btn-secondary');
  });
});

// Equivalente Playwright Component Test
import { test, expect } from '@playwright/experimental-ct-react';
import { Button } from './Button';

test.describe('Componente Button', () => {
  test('deve chamar handler onClick quando clicado', async ({ mount }) => {
    let clicked = false;
    const component = await mount(
      <Button label="Submit" onClick={() => { clicked = true; }} />
    );

    await component.getByRole('button').click();
    expect(clicked).toBe(true);
  });

  test('deve estar desabilitado quando loading', async ({ mount }) => {
    const component = await mount(<Button label="Loading" loading={true} />);
    await expect(component.getByRole('button')).toBeDisabled();
    await expect(component.getByTestId('spinner')).toBeVisible();
  });
});
```

**Pontos Chave (Componente)**:

- Testa componente UI isoladamente (sem app completo)
- Props + interações de usuário + estados visuais
- Mais rápido que E2E, mais realista que testes unitários para UI
- Ótimo para componentes de design system

### Exemplo 4: Teste Unitário (Função Pura)

**Cenário**: Testar função de lógica de negócio pura sem dependências de framework.

```typescript
// src/utils/price-calculator.test.ts (Jest/Vitest)
import { calculateDiscount, applyTaxes, calculateTotal } from './price-calculator';

describe('PriceCalculator', () => {
  describe('calculateDiscount', () => {
    it('deve aplicar desconto percentual corretamente', () => {
      const result = calculateDiscount(100, { type: 'percentage', value: 20 });
      expect(result).toBe(80);
    });

    it('deve aplicar desconto de valor fixo corretamente', () => {
      const result = calculateDiscount(100, { type: 'fixed', value: 15 });
      expect(result).toBe(85);
    });

    it('não deve aplicar desconto abaixo de zero', () => {
      const result = calculateDiscount(10, { type: 'fixed', value: 20 });
      expect(result).toBe(0);
    });

    it('deve lidar com nenhum desconto', () => {
      const result = calculateDiscount(100, { type: 'none', value: 0 });
      expect(result).toBe(100);
    });
  });

  describe('applyTaxes', () => {
    it('deve calcular imposto corretamente para US', () => {
      const result = applyTaxes(100, { country: 'US', rate: 0.08 });
      expect(result).toBe(108);
    });

    it('deve calcular imposto corretamente para EU (VAT)', () => {
      const result = applyTaxes(100, { country: 'DE', rate: 0.19 });
      expect(result).toBe(119);
    });

    it('deve lidar com taxa de imposto zero', () => {
      const result = applyTaxes(100, { country: 'US', rate: 0 });
      expect(result).toBe(100);
    });
  });

  describe('calculateTotal', () => {
    it('deve calcular total com desconto e impostos', () => {
      const items = [
        { price: 50, quantity: 2 }, // 100
        { price: 30, quantity: 1 }, // 30
      ];
      const discount = { type: 'percentage', value: 10 }; // -13
      const tax = { country: 'US', rate: 0.08 }; // +9.36

      const result = calculateTotal(items, discount, tax);
      expect(result).toBeCloseTo(126.36, 2);
    });

    it('deve lidar com array de itens vazio', () => {
      const result = calculateTotal([], { type: 'none', value: 0 }, { country: 'US', rate: 0 });
      expect(result).toBe(0);
    });

    it('deve calcular corretamente sem desconto ou imposto', () => {
      const items = [{ price: 25, quantity: 4 }];
      const result = calculateTotal(items, { type: 'none', value: 0 }, { country: 'US', rate: 0 });
      expect(result).toBe(100);
    });
  });
});
```

**Pontos Chave (Unitário)**:

- Teste de função pura—sem dependências de framework
- Execução rápida (milissegundos)
- Cobertura de casos de borda (zero, negativo, inputs vazios)
- Alta complexidade ciclomática tratada no nível unitário

## Quando Usar Qual Nível

| Cenário                | Unitário      | Integração        | E2E           |
| ---------------------- | ------------- | ----------------- | ------------- |
| Lógica de negócio pura | ✅ Primário   | ❌ Exagero        | ❌ Exagero    |
| Operações de BD        | ❌ Não pode   | ✅ Primário       | ❌ Exagero    |
| Contratos de API       | ❌ Não pode   | ✅ Primário       | ⚠️ Suplemento |
| Jornadas de usuário    | ❌ Não pode   | ❌ Não pode       | ✅ Primário   |
| Props/eventos de comp. | ✅ Parcial    | ⚠️ Teste de comp. | ❌ Exagero    |
| Regressão visual       | ❌ Não pode   | ⚠️ Teste de comp. | ✅ Primário   |
| Tratamento de erro (lógica)| ✅ Primário | ⚠️ Integração   | ❌ Exagero    |
| Tratamento de erro (UI)| ❌ Parcial    | ⚠️ Teste de comp. | ✅ Primário   |

## Exemplos de Anti-Padrão

**❌ RUIM: Teste E2E para lógica de negócio**

```typescript
// NÃO FAÇA ISSO
test('calcular desconto via UI', async ({ page }) => {
  await page.goto('/calculator');
  await page.fill('[data-testid="price"]', '100');
  await page.fill('[data-testid="discount"]', '20');
  await page.click('[data-testid="calculate"]');
  await expect(page.getByText('$80')).toBeVisible();
});
// Problema: Lento, frágil, testa lógica que deveria ser testada unitariamente
```

**✅ BOM: Teste unitário para lógica de negócio**

```typescript
test('calcular desconto', () => {
  expect(calculateDiscount(100, 20)).toBe(80);
});
// Rápido, confiável, isolado
```

_Fonte: Filosofia de Teste Murat (pirâmide de teste), estrutura existente test-levels-framework.md._
