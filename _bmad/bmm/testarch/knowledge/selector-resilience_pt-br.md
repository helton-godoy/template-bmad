# Resiliência do seletor

## Princípio

Seletores robustos seguem uma hierarquia rigorosa: **data-testid > papéis ARIA > conteúdo de texto > CSS/IDs** (último recurso). Seletores devem ser resilientes às mudanças de UI (estilhamento, layout, atualizações de conteúdo) e permanecer legíveis para manutenção.

## Racional

**The Problem**: Selectores Brittle (classes CSS, nth-child, XPath complexo) quebram quando mudanças de estilo UI, elementos são reordenados, ou atualizações de design ocorrem. Isso causa carga de manutenção de teste e BMADPROTECT011End negativos.

**The Solution**: Priorize selectores semânticos que reflitam a intenção do usuário (funções ARIA, nomes acessíveis, IDs de teste). Use filtragem dinâmica para listas em vez de índices nth(). Validar seletores durante revisão de código e refator proativamente.

**Por que isso importa**:

- Previne falhas de teste false (refactoring UI não quebra testes)
- Melhora a acessibilidade (papel ARIA beneficia tanto testes como leitores de tela)
- Melhora a legibilidade (selecionadores semânticos)
- Reduz a carga de manutenção (seletores de robustez sobrevivem às mudanças de design)

## Exemplos de padrões

### Exemplo 1: Hierarquia do Selector (Ordem Prioridade com Exemplos)

**Contexto**: Escolha o selector mais resistente para cada tipo de elemento

**Implementation**:

```typescript
// tests/selectors/hierarchy-examples.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Selector Hierarchy Best Practices', () => {
  test('Level 1: data-testid (BEST - most resilient)', async ({ page }) => {
    await page.goto('/login');

    // ✅ Best: Dedicated test attribute (survives all UI changes)
    await page.getByTestId('email-input').fill('user@example.com');
    await page.getByTestId('password-input').fill('password123');
    await page.getByTestId('login-button').click();

    await expect(page.getByTestId('welcome-message')).toBeVisible();

    // Why it's best:
    // - Survives CSS refactoring (class name changes)
    // - Survives layout changes (element reordering)
    // - Survives content changes (button text updates)
    // - Explicit test contract (developer knows it's for testing)
  });

  test('Level 2: ARIA roles and accessible names (GOOD - future-proof)', async ({ page }) => {
    await page.goto('/login');

    // ✅ Good: Semantic HTML roles (benefits accessibility + tests)
    await page.getByRole('textbox', { name: 'Email' }).fill('user@example.com');
    await page.getByRole('textbox', { name: 'Password' }).fill('password123');
    await page.getByRole('button', { name: 'Sign In' }).click();

    await expect(page.getByRole('heading', { name: 'Welcome' })).toBeVisible();

    // Why it's good:
    // - Survives CSS refactoring
    // - Survives layout changes
    // - Enforces accessibility (screen reader compatible)
    // - Self-documenting (role + name = clear intent)
  });

  test('Level 3: Text content (ACCEPTABLE - user-centric)', async ({ page }) => {
    await page.goto('/dashboard');

    // ✅ Acceptable: Text content (matches user perception)
    await page.getByText('Create New Order').click();
    await expect(page.getByText('Order Details')).toBeVisible();

    // Why it's acceptable:
    // - User-centric (what user sees)
    // - Survives CSS/layout changes
    // - Breaks when copy changes (forces test update with content)

    // ⚠️ Use with caution for dynamic/localized content:
    // - Avoid for content with variables: "User 123" (use regex instead)
    // - Avoid for i18n content (use data-testid or ARIA)
  });

  test('Level 4: CSS classes/IDs (LAST RESORT - brittle)', async ({ page }) => {
    await page.goto('/login');

    // ❌ Last resort: CSS class (breaks with styling updates)
    // await page.locator('.btn-primary').click()

    // ❌ Last resort: ID (breaks if ID changes)
    // await page.locator('#login-form').fill(...)

    // ✅ Better: Use data-testid or ARIA instead
    await page.getByTestId('login-button').click();

    // Why CSS/ID is last resort:
    // - Breaks with CSS refactoring (class name changes)
    // - Breaks with HTML restructuring (ID changes)
    // - Not semantic (unclear what element does)
    // - Tight coupling between tests and styling
  });
});

```

**Pontos-chave**
BMADPROTECT009End data-testid (melhor) > ARIA (bom) > texto (aceitável) > CSS/ID (último recurso)
- data-testid sobrevive a todas as alterações de UI (contrato de teste explícito)
- Funções da ARIA impõem acessibilidade (leitor de tela compatível)
- Conteúdo de texto é centrado no usuário (mas quebra com alterações de cópia)
- CSS/ID são quebradiços (quebra com refatorização de estilo)

---

### Exemplo 2: Padrões Selectores Dinâmicos (Listas, Filtros, Regex)

**Contexto**: Lidar com conteúdo dinâmico, listas e dados variáveis com seletores resilientes

**Implementation**:

«``typescript
// testes/seletores/seletores dinâmicos.spec.ts
import BMADPROTECT008End de '@ playwright/test';

test.describe('Padrões Selectores Dinámicos', () => {
  test('regex for variable content (user IDs, timestamps)', async ({ page }) => {
await page.goto('/usuários');

// ✅ Bom: Padrão Regex para IDs de usuário dinâmicos