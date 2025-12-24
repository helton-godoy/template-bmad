# Resiliência de Seletores

## Princípio

Seletores robustos seguem uma hierarquia estrita: **data-testid > ARIA roles > conteúdo de texto > CSS/IDs** (último recurso). Seletores devem ser resilientes a mudanças de UI (estilo, layout, atualizações de conteúdo) e permanecer legíveis para manutenção.

## Motivação

**O Problema**: Seletores frágeis (classes CSS, nth-child, XPath complexo) quebram quando o estilo da UI muda, elementos são reordenados ou atualizações de design ocorrem. Isso causa sobrecarga de manutenção de testes e falsos negativos.

**A Solução**: Priorize seletores semânticos que refletem a intenção do usuário (ARIA roles, nomes acessíveis, IDs de teste). Use filtragem dinâmica para listas em vez de índices nth(). Valide seletores durante a revisão de código e refatore proativamente.

**Por Que Isso Importa**:

- Previne falhas falsas de teste (refatoração de UI não quebra testes)
- Melhora acessibilidade (ARIA roles beneficiam tanto testes quanto leitores de tela)
- Melhora legibilidade (seletores semânticos documentam intenção do usuário)
- Reduz sobrecarga de manutenção (seletores robustos sobrevivem a mudanças de design)

## Exemplos de Padrões

### Exemplo 1: Hierarquia de Seletores (Ordem de Prioridade com Exemplos)

**Contexto**: Escolha o seletor mais resiliente para cada tipo de elemento

**Implementação**:

```typescript
// tests/selectors/hierarchy-examples.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Melhores Práticas de Hierarquia de Seletores', () => {
  test('Nível 1: data-testid (MELHOR - mais resiliente)', async ({ page }) => {
    await page.goto('/login');

    // ✅ Melhor: Atributo de teste dedicado (sobrevive a todas as mudanças de UI)
    await page.getByTestId('email-input').fill('user@example.com');
    await page.getByTestId('password-input').fill('password123');
    await page.getByTestId('login-button').click();

    await expect(page.getByTestId('welcome-message')).toBeVisible();

    // Por que é o melhor:
    // - Sobrevive a refatoração de CSS (mudanças de nome de classe)
    // - Sobrevive a mudanças de layout (reordenação de elementos)
    // - Sobrevive a mudanças de conteúdo (atualizações de texto de botão)
    // - Contrato de teste explícito (desenvolvedor sabe que é para teste)
  });

  test('Nível 2: ARIA roles e nomes acessíveis (BOM - à prova de futuro)', async ({ page }) => {
    await page.goto('/login');

    // ✅ Bom: Roles HTML semânticas (beneficia acessibilidade + testes)
    await page.getByRole('textbox', { name: 'Email' }).fill('user@example.com');
    await page.getByRole('textbox', { name: 'Password' }).fill('password123');
    await page.getByRole('button', { name: 'Sign In' }).click();

    await expect(page.getByRole('heading', { name: 'Welcome' })).toBeVisible();

    // Por que é bom:
    // - Sobrevive a refatoração de CSS
    // - Sobrevive a mudanças de layout
    // - Impõe acessibilidade (compatível com leitor de tela)
    // - Auto-documentável (role + nome = intenção clara)
  });

  test('Nível 3: Conteúdo de texto (ACEITÁVEL - centrado no usuário)', async ({ page }) => {
    await page.goto('/dashboard');

    // ✅ Aceitável: Conteúdo de texto (corresponde à percepção do usuário)
    await page.getByText('Create New Order').click();
    await expect(page.getByText('Order Details')).toBeVisible();

    // Por que é aceitável:
    // - Centrado no usuário (o que o usuário vê)
    // - Sobrevive a mudanças de CSS/layout
    // - Quebra quando o texto muda (força atualização de teste com conteúdo)

    // ⚠️ Use com cautela para conteúdo dinâmico/localizado:
    // - Evite para conteúdo com variáveis: "User 123" (use regex em vez disso)
    // - Evite para conteúdo i18n (use data-testid ou ARIA)
  });

  test('Nível 4: Classes CSS/IDs (ÚLTIMO RECURSO - frágil)', async ({ page }) => {
    await page.goto('/login');

    // ❌ Último recurso: Classe CSS (quebra com atualizações de estilo)
    // await page.locator('.btn-primary').click()

    // ❌ Último recurso: ID (quebra se ID mudar)
    // await page.locator('#login-form').fill(...)

    // ✅ Melhor: Use data-testid ou ARIA em vez disso
    await page.getByTestId('login-button').click();

    // Por que CSS/ID é último recurso:
    // - Quebra com refatoração de CSS (mudanças de nome de classe)
    // - Quebra com reestruturação HTML (mudanças de ID)
    // - Não semântico (não claro o que o elemento faz)
    // - Acoplamento forte entre testes e estilização
  });
});
```

**Pontos Chave**:

- Hierarquia: data-testid (melhor) > ARIA (bom) > texto (aceitável) > CSS/ID (último recurso)
- data-testid sobrevive a TODAS as mudanças de UI (contrato de teste explícito)
- ARIA roles impõem acessibilidade (compatível com leitor de tela)
- Conteúdo de texto é centrado no usuário (mas quebra com mudanças de texto)
- CSS/ID são frágeis (quebram com refatoração de estilo)

---

### Exemplo 2: Padrões de Seletores Dinâmicos (Listas, Filtros, Regex)

**Contexto**: Lidar com conteúdo dinâmico, listas e dados variáveis com seletores resilientes

**Implementação**:

```typescript
// tests/selectors/dynamic-selectors.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Padrões de Seletores Dinâmicos', () => {
  test('regex para conteúdo variável (IDs de usuário, timestamps)', async ({ page }) => {
    await page.goto('/users');

    // ✅ Bom: Padrão Regex para IDs de usuário dinâmicos
    await expect(page.getByText(/User \d+/)).toBeVisible();

    // ✅ Bom: Regex para timestamps
    await expect(page.getByText(/Last login: \d{4}-\d{2}-\d{2}/)).toBeVisible();

    // ✅ Bom: Regex para contagens dinâmicas
    await expect(page.getByText(/\d+ items in cart/)).toBeVisible();
  });

  test('correspondência parcial de texto (case-insensitive, substring)', async ({ page }) => {
    await page.goto('/products');

    // ✅ Bom: Correspondência parcial (sobrevive a pequenas mudanças de texto)
    await page.getByText('Product', { exact: false }).first().click();

    // ✅ Bom: Case-insensitive (sobrevive a mudanças de capitalização)
    await expect(page.getByText(/sign in/i)).toBeVisible();
  });

  test('locators de filtro para listas (evite nth frágil)', async ({ page }) => {
    await page.goto('/products');

    // ❌ Ruim: Baseado em índice (quebra quando a ordem muda)
    // await page.locator('.product-card').nth(2).click()

    // ✅ Bom: Filtro por conteúdo (resiliente a reordenação)
    await page.locator('[data-testid="product-card"]').filter({ hasText: 'Premium Plan' }).click();

    // ✅ Bom: Filtro por atributo
    await page
      .locator('[data-testid="product-card"]')
      .filter({ has: page.locator('[data-status="active"]') })
      .first()
      .click();
  });

  test('nth() apenas quando absolutamente necessário', async ({ page }) => {
    await page.goto('/dashboard');

    // ⚠️ Aceitável: nth(0) para primeiro item (padrão comum)
    const firstNotification = page.getByTestId('notification').nth(0);
    await expect(firstNotification).toContainText('Welcome');

    // ❌ Ruim: nth(5) para índice arbitrário (frágil)
    // await page.getByTestId('notification').nth(5).click()

    // ✅ Melhor: Use filter() com critério específico
    await page.getByTestId('notification').filter({ hasText: 'Critical Alert' }).click();
  });

  test('combine múltiplos locators para especificidade', async ({ page }) => {
    await page.goto('/checkout');

    // ✅ Bom: Escopo estreito com locators combinados
    const shippingSection = page.getByTestId('shipping-section');
    await shippingSection.getByLabel('Address Line 1').fill('123 Main St');
    await shippingSection.getByLabel('City').fill('New York');

    // Escopo previne ambiguidade (múltiplos campos "City" na página)
  });
});
```

**Pontos Chave**:

- Padrões Regex lidam com conteúdo variável (IDs, timestamps, contagens)
- Correspondência parcial sobrevive a pequenas mudanças de texto (`exact: false`)
- `filter()` é mais resiliente que `nth()` (baseado em conteúdo vs baseado em índice)
- `nth(0)` aceitável para "primeiro item", evite índices arbitrários
- Combine locators para estreitar escopo (prevenir ambiguidade)

---

### Exemplo 3: Anti-Padrões de Seletores (O que NÃO fazer)

**Contexto**: Erros comuns de seletores que causam testes frágeis

**Exemplos de Problemas**:

```typescript
// tests/selectors/anti-patterns.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Anti-Padrões de Seletores para Evitar', () => {
  test('❌ Anti-Padrão 1: Classes CSS (frágil)', async ({ page }) => {
    await page.goto('/login');

    // ❌ Ruim: Classe CSS (quebra com atualizações de sistema de design)
    // await page.locator('.btn-primary').click()
    // await page.locator('.form-input-lg').fill('test@example.com')

    // ✅ Bom: Use data-testid ou ARIA role
    await page.getByTestId('login-button').click();
    await page.getByRole('textbox', { name: 'Email' }).fill('test@example.com');
  });

  test('❌ Anti-Padrão 2: Baseado em índice nth() (frágil)', async ({ page }) => {
    await page.goto('/products');

    // ❌ Ruim: Baseado em índice (quebra quando a ordem dos produtos muda)
    // await page.locator('.product-card').nth(3).click()

    // ✅ Bom: Filtro baseado em conteúdo
    await page.locator('[data-testid="product-card"]').filter({ hasText: 'Laptop' }).click();
  });

  test('❌ Anti-Padrão 3: XPath Complexo (difícil de manter)', async ({ page }) => {
    await page.goto('/dashboard');

    // ❌ Ruim: XPath Complexo (ilegível, quebra com mudanças de estrutura)
    // await page.locator('xpath=//div[@class="container"]//section[2]//button[contains(@class, "primary")]').click()

    // ✅ Bom: Seletor semântico
    await page.getByRole('button', { name: 'Create Order' }).click();
  });

  test('❌ Anti-Padrão 4: Seletores de ID (acoplado à implementação)', async ({ page }) => {
    await page.goto('/settings');

    // ❌ Ruim: ID HTML (quebra se ID mudar para acessibilidade/SEO)
    // await page.locator('#user-settings-form').fill(...)

    // ✅ Bom: data-testid ou landmark ARIA
    await page.getByTestId('user-settings-form').getByLabel('Display Name').fill('John Doe');
  });

  test('✅ Refatoração: Seletor Ruim → Bom', async ({ page }) => {
    await page.goto('/checkout');

    // Antes (frágil):
    // await page.locator('.checkout-form > .payment-section > .btn-submit').click()

    // Depois (resiliente):
    await page.getByTestId('checkout-form').getByRole('button', { name: 'Complete Payment' }).click();

    await expect(page.getByText('Payment successful')).toBeVisible();
  });
});
```

**Por Que Estes Falham**:

- **Classes CSS**: Mudam frequentemente com atualizações de design (Tailwind, módulos CSS)
- **Índices nth()**: Frágeis a reordenação de elementos (novas features, testes A/B)
- **XPath Complexo**: Ilegível, quebra com mudanças de estrutura HTML
- **IDs HTML**: Não estáveis (melhorias de acessibilidade mudam IDs)

**Abordagem Melhor**: Use hierarquia de seletores (testid > ARIA > texto)

---

### Exemplo 4: Técnicas de Debugging de Seletores (Inspector, DevTools, MCP)

**Contexto**: Debugar falhas de seletores interativamente para encontrar melhores alternativas

**Implementação**:

```typescript
// tests/selectors/debugging-techniques.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Técnicas de Debugging de Seletores', () => {
  test('use Playwright Inspector para testar seletores', async ({ page }) => {
    await page.goto('/dashboard');

    // Pausa o teste para abrir o Inspector
    await page.pause();

    // No console do Inspector, teste seletores:
    // page.getByTestId('user-menu')              ✅ Funciona
    // page.getByRole('button', { name: 'Profile' }) ✅ Funciona
    // page.locator('.btn-primary')               ❌ Frágil

    // Use o recurso "Pick Locator" para gerar seletores
    // Use o modo "Record" para capturar interações do usuário

    await page.getByTestId('user-menu').click();
    await expect(page.getByRole('menu')).toBeVisible();
  });

  test('use locator.all() para debugar listas', async ({ page }) => {
    await page.goto('/products');

    // Debug: Quantos produtos estão visíveis?
    const products = await page.getByTestId('product-card').all();
    console.log(`Encontrados ${products.length} produtos`);

    // Debug: Que texto está em cada produto?
    for (const product of products) {
      const text = await product.textContent();
      console.log(`Texto do produto: ${text}`);
    }

    // Use descobertas para construir seletor melhor
    await page.getByTestId('product-card').filter({ hasText: 'Laptop' }).click();
  });

  test('use console DevTools para testar seletores', async ({ page }) => {
    await page.goto('/checkout');

    // Abra DevTools (manualmente ou via page.pause())
    // Teste seletores no console:
    // document.querySelectorAll('[data-testid="payment-method"]')
    // document.querySelector('#credit-card-input')

    // Encontre seletor robusto por tentativa e erro
    await page.getByTestId('payment-method').selectOption('credit-card');
  });

  test('MCP browser_generate_locator (se disponível)', async ({ page }) => {
    await page.goto('/products');

    // Se Playwright MCP disponível, use browser_generate_locator:
    // 1. Clique no elemento no navegador
    // 2. MCP gera seletor ideal
    // 3. Copie para o teste

    // Exemplo de saída do MCP:
    // page.getByRole('link', { name: 'Product A' })

    // Use seletor gerado
    await page.getByRole('link', { name: 'Product A' }).click();
    await expect(page).toHaveURL(/\/products\/\d+/);
  });
});
```

**Pontos Chave**:

- Playwright Inspector: Teste interativo de seletores com recurso "Pick Locator"
- `locator.all()`: Debuga listas para entender estrutura e conteúdo
- Console DevTools: Teste seletores CSS antes de adicionar aos testes
- MCP browser_generate_locator: Auto-gera seletores ideais (se MCP disponível)
- Sempre valide se seletores funcionam antes de commitar

---

### Exemplo 2: Guia de Refatoração de Seletores (Padrões Antes/Depois)

**Contexto**: Melhorar sistematicamente seletores frágeis para alternativas resilientes

**Implementação**:

```typescript
// tests/selectors/refactoring-guide.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Padrões de Refatoração de Seletores', () => {
  test('refatorar: Classe CSS → data-testid', async ({ page }) => {
    await page.goto('/products');

    // ❌ Antes: Classe CSS (quebra com atualizações Tailwind)
    // await page.locator('.bg-blue-500.px-4.py-2.rounded').click()

    // ✅ Depois: data-testid
    await page.getByTestId('add-to-cart-button').click();

    // Implementação: Adicione data-testid ao componente de botão
    // <button className="bg-blue-500 px-4 py-2 rounded" data-testid="add-to-cart-button">
  });

  test('refatorar: índice nth() → filter()', async ({ page }) => {
    await page.goto('/users');

    // ❌ Antes: Baseado em índice (quebra quando usuários reordenam)
    // await page.locator('.user-row').nth(2).click()

    // ✅ Depois: Filtro baseado em conteúdo
    await page.locator('[data-testid="user-row"]').filter({ hasText: 'john@example.com' }).click();
  });

  test('refatorar: XPath Complexo → ARIA role', async ({ page }) => {
    await page.goto('/checkout');

    // ❌ Antes: XPath Complexo (ilegível, frágil)
    // await page.locator('xpath=//div[@id="payment"]//form//button[contains(@class, "submit")]').click()

    // ✅ Depois: ARIA role
    await page.getByRole('button', { name: 'Complete Payment' }).click();
  });

  test('refatorar: Seletor ID → data-testid', async ({ page }) => {
    await page.goto('/settings');

    // ❌ Antes: ID HTML (muda com melhorias de acessibilidade)
    // await page.locator('#user-profile-section').getByLabel('Name').fill('John')

    // ✅ Depois: data-testid + label semântico
    await page.getByTestId('user-profile-section').getByLabel('Display Name').fill('John Doe');
  });

  test('refatorar: CSS profundamente aninhado → data-testid escopado', async ({ page }) => {
    await page.goto('/dashboard');

    // ❌ Antes: Aninhamento profundo (quebra com mudanças de estrutura)
    // await page.locator('.container .sidebar .menu .item:nth-child(3) a').click()

    // ✅ Depois: data-testid escopado
    const sidebar = page.getByTestId('sidebar');
    await sidebar.getByRole('link', { name: 'Settings' }).click();
  });
});
```

**Pontos Chave**:

- Classe CSS → data-testid (sobrevive a atualizações de sistema de design)
- nth() → filter() (baseado em conteúdo vs baseado em índice)
- XPath Complexo → ARIA role (legível, semântico)
- ID → data-testid (desacopla da estrutura HTML)
- Aninhamento profundo → locators escopados (modular, sustentável)

---

### Exemplo 3: Checklist de Melhores Práticas de Seletores

```typescript
// tests/selectors/validation-checklist.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Checklist de Validação de Seletor
 *
 * Antes de commitar teste, verifique se seletores atendem a estes critérios:
 */
test.describe('Validação de Melhores Práticas de Seletores', () => {
  test('✅ 1. Prefira data-testid para elementos interativos', async ({ page }) => {
    await page.goto('/login');

    // Elementos interativos (botões, inputs, links) devem usar data-testid
    await page.getByTestId('email-input').fill('test@example.com');
    await page.getByTestId('login-button').click();
  });

  test('✅ 2. Use ARIA roles para elementos semânticos', async ({ page }) => {
    await page.goto('/dashboard');

    // Elementos semânticos (headings, navegação, formulários) usam ARIA
    await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
    await page.getByRole('navigation').getByRole('link', { name: 'Settings' }).click();
  });

  test('✅ 3. Evite classes CSS (exceto ao testar estilos)', async ({ page }) => {
    await page.goto('/products');

    // ❌ Nunca para interação: page.locator('.btn-primary')
    // ✅ Apenas para regressão visual: await expect(page.locator('.error-banner')).toHaveCSS('color', 'rgb(255, 0, 0)')
  });

  test('✅ 4. Use filter() em vez de nth() para listas', async ({ page }) => {
    await page.goto('/orders');

    // Seleção de lista deve ser baseada em conteúdo
    await page.getByTestId('order-row').filter({ hasText: 'Order #12345' }).click();
  });

  test('✅ 5. Seletores são legíveis por humanos', async ({ page }) => {
    await page.goto('/checkout');

    // ✅ Bom: Intenção clara
    await page.getByTestId('shipping-address-form').getByLabel('Street Address').fill('123 Main St');

    // ❌ Ruim: Críptico
    // await page.locator('div > div:nth-child(2) > input[type="text"]').fill('123 Main St')
  });
});
```

**Regras de Validação**:

1. **Elementos interativos** (botões, inputs) → data-testid
2. **Elementos semânticos** (headings, nav, forms) → ARIA roles
3. **Classes CSS** → Evite (exceto testes de regressão visual)
4. **Listas** → filter() sobre nth() (seleção baseada em conteúdo)
5. **Legibilidade** → Seletores documentam intenção do usuário (claro, semântico)

---

## Checklist de Resiliência de Seletor

Antes de implantar seletores:

- [ ] **Hierarquia seguida**: data-testid (1ª escolha) > ARIA (2ª) > texto (3ª) > CSS/ID (último recurso)
- [ ] **Elementos interativos usam data-testid**: Botões, inputs, links têm atributos de teste dedicados
- [ ] **Elementos semânticos usam ARIA**: Headings, navegação, forms usam roles e nomes acessíveis
- [ ] **Sem padrões frágeis**: Sem classes CSS (exceto testes visuais), sem nth() arbitrário, sem XPath complexo
- [ ] **Conteúdo dinâmico tratado**: Regex para IDs/timestamps, filter() para listas, correspondência parcial para texto
- [ ] **Seletores são escopados**: Use locators de contêiner para estreitar escopo (prevenir ambiguidade)
- [ ] **Legível por humanos**: Seletores documentam intenção do usuário (claro, semântico, sustentável)
- [ ] **Validado no Inspector**: Teste seletores interativamente antes de commitar (page.pause())

## Pontos de Integração

- **Usado em workflows**: `*atdd` (gerar testes com seletores robustos), `*automate` (curar falhas de seletor), `*test-review` (validar qualidade de seletor)
- **Fragmentos relacionados**: `test-healing-patterns.md` (diagnóstico de falha de seletor), `fixture-architecture.md` (alternativas de page object), `test-quality.md` (padrões de manutenibilidade)
- **Ferramentas**: Playwright Inspector (Pick Locator), Console DevTools, Playwright MCP browser_generate_locator (opcional)

_Fonte: Melhores práticas de seletor Playwright, diretrizes de acessibilidade (ARIA), padrões de manutenção de teste em produção_
