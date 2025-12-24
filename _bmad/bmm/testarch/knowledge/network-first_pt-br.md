# Salvaguardas Network-First

## Princípio

Registre interceptações de rede **antes** de qualquer navegação ou ação do usuário. Armazene a promessa de interceptação e aguarde-a imediatamente após o passo de disparo. Substitua waits implícitos por sinais determinísticos baseados em respostas de rede, desaparecimento de spinner ou hooks de evento.

## Motivação

A fonte mais comum de testes E2E instáveis são **condições de corrida** entre navegação e interceptação de rede:

- Navegar depois interceptar = requisições perdidas (tarde demais)
- Sem espera explícita = asserção roda antes da resposta chegar
- Waits fixos (`waitForTimeout(3000)`) = lentos, não confiáveis, frágeis

Padrões Network-first fornecem:

- **Zero condições de corrida**: Interceptação está ativa antes da ação de disparo
- **Waits determinísticos**: Aguarde pela resposta real, não timeouts arbitrários
- **Falhas acionáveis**: Asserções no status/corpo da resposta, não "elemento não encontrado" genérico
- **Velocidade**: Sem preenchimento com tempo de espera extra

## Exemplos de Padrões

### Exemplo 1: Padrão Interceptar Antes de Navegar

**Contexto**: O padrão fundamental para todos os testes E2E. Sempre registre a interceptação de rota **antes** da ação que dispara a requisição (navegação, clique, envio de formulário).

**Implementação**:

```typescript
// ✅ CORRETO: Interceptar ANTES de navegar
test('usuário pode ver dados do dashboard', async ({ page }) => {
  // Passo 1: Registrar interceptação PRIMEIRO
  const usersPromise = page.waitForResponse((resp) => resp.url().includes('/api/users') && resp.status() === 200);

  // Passo 2: ENTÃO disparar a requisição
  await page.goto('/dashboard');

  // Passo 3: ENTÃO aguardar a resposta
  const usersResponse = await usersPromise;
  const users = await usersResponse.json();

  // Passo 4: Asserção em dados estruturados
  expect(users).toHaveLength(10);
  await expect(page.getByText(users[0].name)).toBeVisible();
});

// Equivalente Cypress
describe('Dashboard', () => {
  it('deve exibir usuários', () => {
    // Passo 1: Registrar interceptação PRIMEIRO
    cy.intercept('GET', '**/api/users').as('getUsers');

    // Passo 2: ENTÃO disparar
    cy.visit('/dashboard');

    // Passo 3: ENTÃO aguardar
    cy.wait('@getUsers').then((interception) => {
      // Passo 4: Asserção em dados estruturados
      expect(interception.response.statusCode).to.equal(200);
      expect(interception.response.body).to.have.length(10);
      cy.contains(interception.response.body[0].name).should('be.visible');
    });
  });
});

// ❌ ERRADO: Navegar ANTES de interceptar (condição de corrida!)
test('exemplo de teste instável', async ({ page }) => {
  await page.goto('/dashboard'); // Requisição dispara imediatamente

  const usersPromise = page.waitForResponse('/api/users'); // TARDE DEMAIS - pode perder
  const response = await usersPromise; // Pode dar timeout aleatoriamente
});
```

**Pontos Chave**:

- Playwright: Use `page.waitForResponse()` com padrão de URL ou predicado **antes** de `page.goto()` ou `page.click()`
- Cypress: Use `cy.intercept().as()` **antes** de `cy.visit()` ou `cy.click()`
- Armazene promessa/alias, dispare ação, **então** aguarde resposta
- Isso previne 95% da instabilidade de condição de corrida em testes E2E

### Exemplo 2: Captura HAR para Debugging

**Contexto**: Ao debugar testes instáveis ou construir mocks determinísticos, capture tráfego de rede real com arquivos HAR. Reproduza-os em testes para execuções consistentes e offline.

**Implementação**:

```typescript
// playwright.config.ts - Habilitar gravação HAR
export default defineConfig({
  use: {
    // Gravar HAR na primeira execução
    recordHar: { path: './hars/', mode: 'minimal' },
    // Ou reproduzir HAR em testes
    // serviceWorkers: 'block',
  },
});

// Capturar HAR para teste específico
test('capturar rede para fluxo de pedido', async ({ page, context }) => {
  // Iniciar gravação
  await context.routeFromHAR('./hars/order-flow.har', {
    url: '**/api/**',
    update: true, // Atualizar HAR com novas requisições
  });

  await page.goto('/checkout');
  await page.fill('[data-testid="credit-card"]', '4111111111111111');
  await page.click('[data-testid="submit-order"]');
  await expect(page.getByText('Order Confirmed')).toBeVisible();

  // HAR salvo em ./hars/order-flow.har
});

// Reproduzir HAR para testes determinísticos (sem API real necessária)
test('reproduzir fluxo de pedido do HAR', async ({ page, context }) => {
  // Reproduzir HAR capturado
  await context.routeFromHAR('./hars/order-flow.har', {
    url: '**/api/**',
    update: false, // Modo somente leitura
  });

  // Teste roda com respostas gravadas exatas - totalmente determinístico
  await page.goto('/checkout');
  await page.fill('[data-testid="credit-card"]', '4111111111111111');
  await page.click('[data-testid="submit-order"]');
  await expect(page.getByText('Order Confirmed')).toBeVisible();
});

// Mock personalizado baseado em insights HAR
test('mockar resposta de pedido baseado no HAR', async ({ page }) => {
  // Após analisar HAR, criar mock focado
  await page.route('**/api/orders', (route) =>
    route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({
        orderId: '12345',
        status: 'confirmed',
        total: 99.99,
      }),
    }),
  );

  await page.goto('/checkout');
  await page.click('[data-testid="submit-order"]');
  await expect(page.getByText('Order #12345')).toBeVisible();
});
```

**Pontos Chave**:

- Arquivos HAR capturam pares reais de requisição/resposta para análise
- `update: true` grava novo tráfego; `update: false` reproduz existente
- Modo de reprodução torna testes totalmente determinísticos (sem API upstream necessária)
- Use HAR para entender contratos de API, depois crie mocks focados

### Exemplo 3: Network Stub com Casos de Borda

**Contexto**: Ao testar tratamento de erro, timeouts e casos de borda, faça stub de respostas de rede para simular falhas. Teste tanto caminho feliz quanto cenários de erro.

**Implementação**:

```typescript
// Teste caminho feliz
test('pedido tem sucesso com dados válidos', async ({ page }) => {
  await page.route('**/api/orders', (route) =>
    route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({ orderId: '123', status: 'confirmed' }),
    }),
  );

  await page.goto('/checkout');
  await page.click('[data-testid="submit-order"]');
  await expect(page.getByText('Order Confirmed')).toBeVisible();
});

// Teste erro 500
test('pedido falha com erro de servidor', async ({ page }) => {
  // Ouvir erros de console (app deve logar graciosamente)
  const consoleErrors: string[] = [];
  page.on('console', (msg) => {
    if (msg.type() === 'error') consoleErrors.push(msg.text());
  });

  // Stub erro 500
  await page.route('**/api/orders', (route) =>
    route.fulfill({
      status: 500,
      contentType: 'application/json',
      body: JSON.stringify({ error: 'Internal Server Error' }),
    }),
  );

  await page.goto('/checkout');
  await page.click('[data-testid="submit-order"]');

  // Asserção que UI mostra erro graciosamente
  await expect(page.getByText('Something went wrong')).toBeVisible();
  await expect(page.getByText('Please try again')).toBeVisible();

  // Verificar erro logado (não lançado)
  expect(consoleErrors.some((e) => e.includes('Order failed'))).toBeTruthy();
});

// Teste timeout de rede
test('pedido dá timeout após 10 segundos', async ({ page }) => {
  // Stub resposta atrasada (nunca resolve dentro do timeout)
  await page.route(
    '**/api/orders',
    (route) => new Promise(() => {}), // Nunca resolve - simula timeout
  );

  await page.goto('/checkout');
  await page.click('[data-testid="submit-order"]');

  // App deve mostrar mensagem de timeout após timeout configurado
  await expect(page.getByText('Request timed out')).toBeVisible({ timeout: 15000 });
});

// Teste resposta de dados parciais
test('pedido lida com campos opcionais faltando', async ({ page }) => {
  await page.route('**/api/orders', (route) =>
    route.fulfill({
      status: 200,
      contentType: 'application/json',
      // Faltando campos opcionais como 'trackingNumber', 'estimatedDelivery'
      body: JSON.stringify({ orderId: '123', status: 'confirmed' }),
    }),
  );

  await page.goto('/checkout');
  await page.click('[data-testid="submit-order"]');

  // App deve lidar graciosamente - sem crash, mostra o que está disponível
  await expect(page.getByText('Order Confirmed')).toBeVisible();
  await expect(page.getByText('Tracking information pending')).toBeVisible();
});

// Equivalentes Cypress
describe('Casos de Borda de Pedido', () => {
  it('deve lidar com erro 500', () => {
    cy.intercept('POST', '**/api/orders', {
      statusCode: 500,
      body: { error: 'Internal Server Error' },
    }).as('orderFailed');

    cy.visit('/checkout');
    cy.get('[data-testid="submit-order"]').click();
    cy.wait('@orderFailed');
    cy.contains('Something went wrong').should('be.visible');
  });

  it('deve lidar com timeout', () => {
    cy.intercept('POST', '**/api/orders', (req) => {
      req.reply({ delay: 20000 }); // Atraso além do timeout do app
    }).as('orderTimeout');

    cy.visit('/checkout');
    cy.get('[data-testid="submit-order"]').click();
    cy.contains('Request timed out', { timeout: 15000 }).should('be.visible');
  });
});
```

**Pontos Chave**:

- Stub diferentes códigos de status HTTP (200, 400, 500, 503)
- Simule timeouts com `delay` ou promessas que não resolvem
- Teste respostas de dados parciais/incompletos
- Verifique se o app lida com erros graciosamente (sem crashes, mensagens amigáveis)

### Exemplo 4: Espera Determinística

**Contexto**: Nunca use waits fixos (`waitForTimeout(3000)`). Sempre aguarde por sinais explícitos: respostas de rede, mudanças de estado de elemento ou eventos personalizados.

**Implementação**:

```typescript
// ✅ BOM: Aguardar resposta com predicado
test('aguardar resposta específica', async ({ page }) => {
  const responsePromise = page.waitForResponse((resp) => resp.url().includes('/api/users') && resp.status() === 200);

  await page.goto('/dashboard');
  const response = await responsePromise;

  expect(response.status()).toBe(200);
  await expect(page.getByText('Dashboard')).toBeVisible();
});

// ✅ BOM: Aguardar múltiplas respostas
test('aguardar todos os dados necessários', async ({ page }) => {
  const usersPromise = page.waitForResponse('**/api/users');
  const productsPromise = page.waitForResponse('**/api/products');
  const ordersPromise = page.waitForResponse('**/api/orders');

  await page.goto('/dashboard');

  // Aguardar todos em paralelo
  const [users, products, orders] = await Promise.all([usersPromise, productsPromise, ordersPromise]);

  expect(users.status()).toBe(200);
  expect(products.status()).toBe(200);
  expect(orders.status()).toBe(200);
});

// ✅ BOM: Aguardar spinner desaparecer
test('aguardar indicador de carregamento', async ({ page }) => {
  await page.goto('/dashboard');

  // Aguardar spinner desaparecer (sinaliza dados carregados)
  await expect(page.getByTestId('loading-spinner')).not.toBeVisible();
  await expect(page.getByText('Dashboard')).toBeVisible();
});

// ✅ BOM: Aguardar evento personalizado (avançado)
test('aguardar evento ready personalizado', async ({ page }) => {
  let appReady = false;
  page.on('console', (msg) => {
    if (msg.text() === 'App ready') appReady = true;
  });

  await page.goto('/dashboard');

  // Poll até condição personalizada ser atendida
  await page.waitForFunction(() => appReady, { timeout: 10000 });

  await expect(page.getByText('Dashboard')).toBeVisible();
});

// ❌ RUIM: Espera fixa (timeout arbitrário)
test('exemplo de espera fixa instável', async ({ page }) => {
  await page.goto('/dashboard');
  await page.waitForTimeout(3000); // POR QUE 3 segundos? E se for mais lento? E se for mais rápido?
  await expect(page.getByText('Dashboard')).toBeVisible(); // Pode falhar se >3s
});

// Equivalentes Cypress
describe('Espera Determinística', () => {
  it('deve aguardar resposta', () => {
    cy.intercept('GET', '**/api/users').as('getUsers');
    cy.visit('/dashboard');
    cy.wait('@getUsers').its('response.statusCode').should('eq', 200);
    cy.contains('Dashboard').should('be.visible');
  });

  it('deve aguardar spinner desaparecer', () => {
    cy.visit('/dashboard');
    cy.get('[data-testid="loading-spinner"]').should('not.exist');
    cy.contains('Dashboard').should('be.visible');
  });

  // ❌ RUIM: Espera fixa
  it('espera fixa instável', () => {
    cy.visit('/dashboard');
    cy.wait(3000); // NUNCA FAÇA ISSO
    cy.contains('Dashboard').should('be.visible');
  });
});
```

**Pontos Chave**:

- `waitForResponse()` com padrão de URL ou predicado = determinístico
- `waitForLoadState('networkidle')` = aguardar toda atividade de rede terminar
- Aguarde mudanças de estado de elemento (spinner desaparece, botão habilitado)
- **NUNCA** use `waitForTimeout()` ou `cy.wait(ms)` - sempre não-determinístico

### Exemplo 5: Anti-Padrão - Navegar Depois Mockar

**Problema**:

```typescript
// ❌ RUIM: Condição de corrida - mock registrado DEPOIS que navegação começa
test('teste instável - navegar depois mockar', async ({ page }) => {
  // Navegação começa imediatamente
  await page.goto('/dashboard'); // Requisição para /api/users dispara AGORA

  // Mock registrado tarde demais - requisição já enviada
  await page.route('**/api/users', (route) =>
    route.fulfill({
      status: 200,
      body: JSON.stringify([{ id: 1, name: 'Test User' }]),
    }),
  );

  // Teste passa/falha aleatoriamente dependendo do timing
  await expect(page.getByText('Test User')).toBeVisible(); // Instável!
});

// ❌ RUIM: Sem espera por resposta
test('teste instável - sem espera explícita', async ({ page }) => {
  await page.route('**/api/users', (route) => route.fulfill({ status: 200, body: JSON.stringify([]) }));

  await page.goto('/dashboard');

  // Asserção roda imediatamente - pode falhar se resposta for lenta
  await expect(page.getByText('No users found')).toBeVisible(); // Instável!
});

// ❌ RUIM: Timeout genérico
test('teste instável - espera fixa', async ({ page }) => {
  await page.goto('/dashboard');
  await page.waitForTimeout(2000); // Espera arbitrária - frágil

  await expect(page.getByText('Dashboard')).toBeVisible();
});
```

**Por Que Falha**:

- **Mock depois de navegar**: Requisição dispara durante navegação, mock não está ativo ainda (condição de corrida)
- **Sem espera explícita**: Asserção roda antes da resposta chegar (dependente de tempo)
- **Waits fixos**: Testes lentos, frágeis (falha se < timeout, desperdiça tempo se > timeout)
- **Não-determinístico**: Passa localmente, falha no CI (velocidades diferentes)

**Abordagem Melhor**: Sempre interceptar → disparar → aguardar

```typescript
// ✅ BOM: Interceptar ANTES de navegar
test('teste determinístico', async ({ page }) => {
  // Passo 1: Registrar mock PRIMEIRO
  await page.route('**/api/users', (route) =>
    route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify([{ id: 1, name: 'Test User' }]),
    }),
  );

  // Passo 2: Armazenar promessa de resposta ANTES de disparar
  const responsePromise = page.waitForResponse('**/api/users');

  // Passo 3: ENTÃO disparar
  await page.goto('/dashboard');

  // Passo 4: ENTÃO aguardar resposta
  await responsePromise;

  // Passo 5: ENTÃO asserção (dados garantidos carregados)
  await expect(page.getByText('Test User')).toBeVisible();
});
```

**Pontos Chave**:

- Ordem importa: Mock → Promessa → Disparar → Aguardar → Asserção
- Sem condições de corrida: Mock está ativo antes da requisição disparar
- Espera explícita: Promessa de resposta garante dados carregados
- Determinístico: Sempre passa se o app funcionar corretamente

## Pontos de Integração

- **Usado em workflows**: `*atdd` (geração de teste), `*automate` (expansão de teste), `*framework` (setup de rede)
- **Fragmentos relacionados**:
  - `fixture-architecture.md` - Padrões de fixture de rede
  - `data-factories.md` - Setup API-first com rede
  - `test-quality.md` - Princípios de teste determinístico

## Debugging de Problemas de Rede

Quando testes de rede falham, verifique:

1. **Timing**: Interceptação está registrada **antes** da ação?
2. **Padrão de URL**: O padrão corresponde à URL real da requisição?
3. **Formato da resposta**: A resposta mockada é JSON/formato válido?
4. **Código de status**: O app está verificando 200 vs 201 vs 204?
5. **Arquivo HAR**: Capture tráfego real para entender contrato de API real

```typescript
// Debugar problemas de rede com logging
test('debug rede', async ({ page }) => {
  // Logar todas as requisições
  page.on('request', (req) => console.log('→', req.method(), req.url()));

  // Logar todas as respostas
  page.on('response', (resp) => console.log('←', resp.status(), resp.url()));

  await page.goto('/dashboard');
});
```

_Fonte: Filosofia de Teste Murat (linhas 94-137), padrões de rede Playwright, melhores práticas de interceptação Cypress._
