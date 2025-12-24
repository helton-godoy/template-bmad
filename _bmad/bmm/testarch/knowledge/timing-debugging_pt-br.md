# Debugging de Timing e Correções de Condição de Corrida

## Princípio

Condições de corrida surgem quando testes fazem suposições sobre temporização assíncrona (rede, animações, atualizações de estado). **Espera determinística** elimina instabilidade esperando explicitamente por eventos observáveis (respostas de rede, mudanças de estado de elemento) em vez de timeouts arbitrários.

## Motivação

**O Problema**: Testes passam localmente mas falham no CI (temporização diferente), ou passam/falham aleatoriamente (condições de corrida). Esperas fixas (`waitForTimeout`, `sleep`) mascaram problemas de temporização sem resolvê-los.

**A Solução**: Substitua todas as esperas fixas por esperas baseadas em eventos (`waitForResponse`, `waitFor({ state })`). Implemente o padrão network-first (interceptar antes de navegar). Use verificações de estado explícitas (spinner de carregamento desanexado, dados carregados). Isso torna os testes determinísticos independentemente da velocidade da rede ou carga do sistema.

**Por Que Isso Importa**:

- Elimina testes instáveis (0 tolerância para falhas baseadas em temporização)
- Funciona consistentemente através de ambientes (local, CI, similar a produção)
- Execução de teste mais rápida (sem esperas desnecessárias)
- Intenção de teste mais clara (explícito sobre o que estamos esperando)

## Exemplos de Padrões

### Exemplo 1: Identificação de Condição de Corrida (Padrão Network-First)

**Contexto**: Prevenir condições de corrida interceptando requisições de rede antes da navegação

**Implementação**:

```typescript
// tests/timing/race-condition-prevention.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Padrões de Prevenção de Condição de Corrida', () => {
  test('❌ Anti-Padrão: Navegar depois interceptar (condição de corrida)', async ({ page, context }) => {
    // RUIM: Navegação começa antes da interceptação estar pronta
    await page.goto('/products'); // ⚠️ Corrida! API pode carregar antes da rota ser definida

    await context.route('**/api/products', (route) => {
      route.fulfill({ status: 200, body: JSON.stringify({ products: [] }) });
    });

    // Teste pode ver resposta real da API ou mock (não determinístico)
  });

  test('✅ Padrão: Interceptar ANTES de navegar (determinístico)', async ({ page, context }) => {
    // BOM: Interceptação pronta antes da navegação
    await context.route('**/api/products', (route) => {
      route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          products: [
            { id: 1, name: 'Produto A', price: 29.99 },
            { id: 2, name: 'Produto B', price: 49.99 },
          ],
        }),
      });
    });

    const responsePromise = page.waitForResponse('**/api/products');

    await page.goto('/products'); // Navegação acontece APÓS rota estar pronta
    await responsePromise; // Espera explícita pela rede

    // Teste vê resposta mock confiável (determinístico)
    await expect(page.getByText('Produto A')).toBeVisible();
  });

  test('✅ Padrão: Aguardar mudança de estado de elemento (carregando → carregado)', async ({ page }) => {
    await page.goto('/dashboard');

    // Aguardar indicador de carregamento aparecer (confirma carregamento iniciado)
    await page.getByTestId('loading-spinner').waitFor({ state: 'visible' });

    // Aguardar indicador de carregamento desaparecer (confirma carregamento completo)
    await page.getByTestId('loading-spinner').waitFor({ state: 'detached' });

    // Conteúdo agora confiavelmente visível
    await expect(page.getByTestId('dashboard-data')).toBeVisible();
  });

  test('✅ Padrão: Verificação de visibilidade explícita (não apenas presença)', async ({ page }) => {
    await page.goto('/modal-demo');

    await page.getByRole('button', { name: 'Abrir Modal' }).click();

    // ❌ Ruim: Elemento existe mas pode não estar visível ainda
    // await expect(page.getByTestId('modal')).toBeAttached()

    // ✅ Bom: Aguardar visibilidade (considera animações)
    await expect(page.getByTestId('modal')).toBeVisible();
    await expect(page.getByRole('heading', { name: 'Título Modal' })).toBeVisible();
  });

  test('❌ Anti-Padrão: waitForLoadState("networkidle") em SPAs', async ({ page }) => {
    // ⚠️ Deprecado para SPAs (conexões WebSocket nunca ociosas)
    // await page.goto('/dashboard')
    // await page.waitForLoadState('networkidle') // Pode dar timeout em SPAs

    // ✅ Melhor: Aguardar resposta específica de API
    const responsePromise = page.waitForResponse('**/api/dashboard');
    await page.goto('/dashboard');
    await responsePromise;

    await expect(page.getByText('Dashboard carregado')).toBeVisible();
  });
});
```

**Pontos Chave**:

- Network-first: SEMPRE intercepte antes de navegar (previne condições de corrida)
- Mudanças de estado: Aguarde spinner de carregamento desanexado (conclusão de carregamento explícita)
- Visibilidade vs presença: `toBeVisible()` considera animações, `toBeAttached()` não
- Evite networkidle: Não confiável em SPAs (conexões WebSocket, polling)
- Esperas explícitas: Documente exatamente o que estamos esperando

---

### Exemplo 2: Padrões de Espera Determinística (Baseado em Evento, Não Tempo)

**Contexto**: Substitua todas as esperas fixas por esperas de evento observável

**Implementação**:

```typescript
// tests/timing/deterministic-waits.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Padrões de Espera Determinística', () => {
  test('waitForResponse() com padrão de URL', async ({ page }) => {
    const responsePromise = page.waitForResponse('**/api/products');

    await page.goto('/products');
    await responsePromise; // Determinístico (aguarda chamada exata de API)

    await expect(page.getByText('Produtos carregados')).toBeVisible();
  });

  test('waitForResponse() com função predicado', async ({ page }) => {
    const responsePromise = page.waitForResponse((resp) => resp.url().includes('/api/search') && resp.status() === 200);

    await page.goto('/search');
    await page.getByPlaceholder('Buscar').fill('laptop');
    await page.getByRole('button', { name: 'Buscar' }).click();

    await responsePromise; // Aguardar resposta de busca bem-sucedida

    await expect(page.getByTestId('search-results')).toBeVisible();
  });

  test('waitForFunction() para condições customizadas', async ({ page }) => {
    await page.goto('/dashboard');

    // Aguardar condição JavaScript customizada
    await page.waitForFunction(() => {
      const element = document.querySelector('[data-testid="user-count"]');
      return element && parseInt(element.textContent || '0') > 0;
    });

    // Contagem de usuário agora carregada
    await expect(page.getByTestId('user-count')).not.toHaveText('0');
  });

  test('waitFor() estado de elemento (anexado, visível, oculto, desanexado)', async ({ page }) => {
    await page.goto('/products');

    // Aguardar elemento ser anexado ao DOM
    await page.getByTestId('product-list').waitFor({ state: 'attached' });

    // Aguardar elemento ser visível (animações completas)
    await page.getByTestId('product-list').waitFor({ state: 'visible' });

    // Realizar ação
    await page.getByText('Produto A').click();

    // Aguardar modal estar oculta (animação de fechar completa)
    await page.getByTestId('modal').waitFor({ state: 'hidden' });
  });

  test('Cypress: cy.wait() com interceptações com alias', async () => {
    // Exemplo Cypress (não Playwright)
    /*
    cy.intercept('GET', '/api/products').as('getProducts')
    cy.visit('/products')
    cy.wait('@getProducts') // Espera determinística por requisição específica

    cy.get('[data-testid="product-list"]').should('be.visible')
    */
  });
});
```

**Pontos Chave**:

- `waitForResponse()`: Aguarda chamadas de API específicas (padrão de URL ou predicado)
- `waitForFunction()`: Aguarda condições JavaScript customizadas
- `waitFor({ state })`: Aguarda mudanças de estado de elemento (anexado, visível, oculto, desanexado)
- Cypress `cy.wait('@alias')`: Espera determinística por interceptações com alias
- Todas as esperas são baseadas em evento (não baseadas em tempo)

---

### Exemplo 3: Anti-Padrões de Timing (O que NUNCA fazer)

**Contexto**: Erros comuns de timing que causam instabilidade

**Exemplos de Problemas**:

```typescript
// tests/timing/anti-patterns.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Anti-Padrões de Timing para Evitar', () => {
  test('❌ NUNCA: page.waitForTimeout() (atraso arbitrário)', async ({ page }) => {
    await page.goto('/dashboard');

    // ❌ Ruim: Espera arbitrária de 3 segundos (instável)
    // await page.waitForTimeout(3000)
    // Problema: Pode ser muito curto (CI mais lento) ou muito longo (desperdiça tempo)

    // ✅ Bom: Aguardar evento observável
    await page.waitForResponse('**/api/dashboard');
    await expect(page.getByText('Dashboard carregado')).toBeVisible();
  });

  test('❌ NUNCA: cy.wait(numero) sem alias (atraso arbitrário)', async () => {
    // Exemplo Cypress
    /*
    // ❌ Ruim: Atraso arbitrário
    cy.visit('/products')
    cy.wait(2000) // Instável!

    // ✅ Bom: Aguardar requisição específica
    cy.intercept('GET', '/api/products').as('getProducts')
    cy.visit('/products')
    cy.wait('@getProducts') // Determinístico
    */
  });

  test('❌ NUNCA: Múltiplas esperas fixas em sequência (atrasos compostos)', async ({ page }) => {
    await page.goto('/checkout');

    // ❌ Ruim: Esperas fixas empilhadas (6+ segundos desperdiçados)
    // await page.waitForTimeout(2000) // Aguardar formulário
    // await page.getByTestId('email').fill('test@example.com')
    // await page.waitForTimeout(1000) // Aguardar validação
    // await page.getByTestId('submit').click()
    // await page.waitForTimeout(3000) // Aguardar redirecionamento

    // ✅ Bom: Esperas baseadas em evento (sem tempo desperdiçado)
    await page.getByTestId('checkout-form').waitFor({ state: 'visible' });
    await page.getByTestId('email').fill('test@example.com');
    await page.waitForResponse('**/api/validate-email');
    await page.getByTestId('submit').click();
    await page.waitForURL('**/confirmation');
  });

  test('❌ NUNCA: waitForLoadState("networkidle") em SPAs', async ({ page }) => {
    // ❌ Ruim: Não confiável em SPAs (conexões WebSocket nunca ociosas)
    // await page.goto('/dashboard')
    // await page.waitForLoadState('networkidle') // Timeout em SPAs!

    // ✅ Bom: Aguardar respostas específicas de API
    await page.goto('/dashboard');
    await page.waitForResponse('**/api/dashboard');
    await page.waitForResponse('**/api/user');
    await expect(page.getByTestId('dashboard-content')).toBeVisible();
  });

  test('❌ NUNCA: Sleep/setTimeout em testes', async ({ page }) => {
    await page.goto('/products');

    // ❌ Ruim: sleep Node.js (bloqueia thread de teste)
    // await new Promise(resolve => setTimeout(resolve, 2000))

    // ✅ Bom: Playwright auto-aguarda elemento
    await expect(page.getByText('Produtos carregados')).toBeVisible();
  });
});
```

**Por Que Estes Falham**:

- **Esperas fixas**: Timeouts arbitrários (muito curto → instável, muito longo → lento)
- **Esperas empilhadas**: Atrasos compostos (desperdício, não confiável)
- **networkidle**: Quebrado em SPAs (WebSocket/polling nunca ocioso)
- **Sleep**: Bloqueia execução (desperdiça tempo, não resolve condições de corrida)

**Abordagem Melhor**: Use esperas baseadas em evento dos exemplos acima

---

## Técnicas de Debugging Assíncrono

### Técnica 1: Análise de Cadeia de Promessas

```typescript
test('debugar cascata async com logs de console', async ({ page }) => {
  console.log('1. Iniciando navegação...');
  await page.goto('/products');

  console.log('2. Aguardando resposta da API...');
  const response = await page.waitForResponse('**/api/products');
  console.log('3. API respondeu:', response.status());

  console.log('4. Aguardando atualização de UI...');
  await expect(page.getByText('Produtos carregados')).toBeVisible();
  console.log('5. Teste completo');

  // Saída do console mostra exatamente onde problema de timing ocorre
});
```

### Técnica 2: Inspeção de Cascata de Rede (DevTools)

```typescript
test('inspecionar timing de rede com visualizador de trace', async ({ page }) => {
  await page.goto('/dashboard');

  // Gerar trace para análise
  // npx playwright test --trace on
  // npx playwright show-trace trace.zip

  // No visualizador de trace:
  // 1. Verificar aba Network para timing de chamada API
  // 2. Identificar requisições lentas (>1s tempo de resposta)
  // 3. Encontrar condições de corrida (requisições sobrepostas)
  // 4. Verificar ordem de requisição (dependências)
});
```

### Técnica 3: Visualizador de Trace para Visualização de Timing

```typescript
test('usar visualizador de trace para debugar timing', async ({ page }) => {
  // Rodar com trace: npx playwright test --trace on

  await page.goto('/checkout');
  await page.getByTestId('submit').click();

  // No visualizador de trace, examine:
  // - Linha do tempo: Ver timing exato de cada ação
  // - Snapshots: Pairar para ver estado do DOM em cada momento
  // - Rede: Identificar requisições lentas/falhas
  // - Console: Verificar erros async

  await expect(page.getByText('Sucesso')).toBeVisible();
});
```

---

## Checklist de Condição de Corrida

Antes de implantar testes:

- [ ] **Padrão network-first**: Todas as rotas interceptadas ANTES da navegação (sem condições de corrida)
- [ ] **Esperas explícitas**: Toda navegação seguida por `waitForResponse()` ou verificação de estado
- [ ] **Sem esperas fixas**: Zero instâncias de `waitForTimeout()`, `cy.wait(numero)`, `sleep()`
- [ ] **Esperas de estado de elemento**: Spinners de carregamento usam `waitFor({ state: 'detached' })`
- [ ] **Verificações de visibilidade**: Use `toBeVisible()` (considera animações), não apenas `toBeAttached()`
- [ ] **Validação de resposta**: Aguardar respostas bem-sucedidas (`resp.ok()` ou `status === 200`)
- [ ] **Análise de visualizador de trace**: Gerar traces para identificar problemas de timing (cascata de rede, erros de console)
- [ ] **Paridade CI/local**: Testes passam confiavelmente em ambos ambientes (sem suposições de timing)

## Pontos de Integração

- **Usado em workflows**: `*automate` (curar falhas de timing), `*test-review` (detectar anti-padrões de espera fixa), `*framework` (configurar padrões de timeout)
- **Fragmentos relacionados**: `test-healing-patterns.md` (diagnóstico de condição de corrida), `network-first.md` (padrões de interceptação), `playwright-config.md` (configuração de timeout), `visual-debugging.md` (análise de visualizador de trace)
- **Ferramentas**: Playwright Inspector (`--debug`), Trace Viewer (`--trace on`), Aba de Rede DevTools

_Fonte: Melhores práticas de timing Playwright, padrão network-first de test-resources-for-ai, debugging de condição de corrida em produção_
