# Teste padrões de cura

## Princípio

Falhas comuns de teste seguem padrões previsíveis (selecionadores estacionários, condições de corrida, afirmações dinâmicas de dados, erros de rede, esperas difíceis). **A cura automatizada** identifica assinaturas de falhas e aplica correções baseadas em padrões. Cura manual captura esses padrões para automação futura.

## Racional

**The Problem**: Falhas de teste desperdiçam tempo de desenvolvimento em depuração repetitiva. As equipes consertam manualmente os mesmos problemas de seleção, erros de tempo e dados descompassos repetidamente entre as suítes de teste.

**A solução**: Catalogue padrões de falha comuns com assinaturas diagnósticas e correções automatizadas. Quando um teste falhar, coincida com a mensagem de erro/traço de stack contra padrões conhecidos e aplique a correção correspondente. Isso transforma a manutenção do teste de depuração reativa em aplicação de padrão proativo.

**Por que isso importa**:

- Reduz o tempo de manutenção do teste em 60-80% (correcções baseadas em padrões vs depuração manual)
- Evita a regressão de flakiness (mesmo erro corrigido uma vez, aplicado em toda parte)
- Constrói conhecimento institucional (catálogo de falha cresce ao longo do tempo)
- Habilita suítes de teste de auto-cura (valida e cura automaticamente o fluxo de trabalho)

## Exemplos de padrões

### Exemplo 1: Padrão de falha comum - Seletores de impasse (elemento não encontrado)

**Contexto**: O teste falha com erros de "Elemento não encontrado" ou "Localizador resolvido para 0 elementos"

**Assinatura diagnóstica**:

```typescript
// src/testing/healing/selector-healing.ts

export type SelectorFailure = {
  errorMessage: string;
  stackTrace: string;
  selector: string;
  testFile: string;
  lineNumber: number;
};

/**
 * Detect stale selector failures
 */
export function isSelectorFailure(error: Error): boolean {
  const patterns = [
    /locator.*resolved to 0 elements/i,
    /element not found/i,
    /waiting for locator.*to be visible/i,
    /selector.*did not match any elements/i,
    /unable to find element/i,
  ];

  return patterns.some((pattern) => pattern.test(error.message));
}

/**
 * Extract selector from error message
 */
export function extractSelector(errorMessage: string): string | null {
  // Playwright: "locator('button[type=\"submit\"]') resolved to 0 elements"
  const playwrightMatch = errorMessage.match(/locator\('([^']+)'\)/);
  if (playwrightMatch) return playwrightMatch[1];

  // Cypress: "Timed out retrying: Expected to find element: '.submit-button'"
  const cypressMatch = errorMessage.match(/Expected to find element: ['"]([^'"]+)['"]/i);
  if (cypressMatch) return cypressMatch[1];

  return null;
}

/**
 * Suggest better selector based on hierarchy
 */
export function suggestBetterSelector(badSelector: string): string {
  // If using CSS class → suggest data-testid
  if (badSelector.startsWith('.') || badSelector.includes('class=')) {
    const elementName = badSelector.match(/class=["']([^"']+)["']/)?.[1] || badSelector.slice(1);
    return `page.getByTestId('${elementName}') // Prefer data-testid over CSS class`;
  }

  // If using ID → suggest data-testid
  if (badSelector.startsWith('#')) {
    return `page.getByTestId('${badSelector.slice(1)}') // Prefer data-testid over ID`;
  }

  // If using nth() → suggest filter() or more specific selector
  if (badSelector.includes('.nth(')) {
    return `page.locator('${badSelector.split('.nth(')[0]}').filter({ hasText: 'specific text' }) // Avoid brittle nth(), use filter()`;
  }

  // If using complex CSS → suggest ARIA role
  if (badSelector.includes('>') || badSelector.includes('+')) {
    return `page.getByRole('button', { name: 'Submit' }) // Prefer ARIA roles over complex CSS`;
  }

  return `page.getByTestId('...') // Add data-testid attribute to element`;
}

```

**Cura Implementation**:

```typescript
// tests/healing/selector-healing.spec.ts
import { test, expect } from '@playwright/test';
import { isSelectorFailure, extractSelector, suggestBetterSelector } from '../../src/testing/healing/selector-healing';

test('heal stale selector failures automatically', async ({ page }) => {
  await page.goto('/dashboard');

  try {
    // Original test with brittle CSS selector
    await page.locator('.btn-primary').click();
  } catch (error: any) {
    if (isSelectorFailure(error)) {
      const badSelector = extractSelector(error.message);
      const suggestion = badSelector ? suggestBetterSelector(badSelector) : null;

      console.log('HEALING SUGGESTION:', suggestion);

      // Apply healed selector
      await page.getByTestId('submit-button').click(); // Fixed!
    } else {
      throw error; // Not a selector issue, rethrow
    }
  }

  await expect(page.getByText('Success')).toBeVisible();
});

```

**Pontos-chave**

- Diagnosis: A mensagem de erro contém "localizador resolvido para 0 elementos" ou "elemento não encontrado"
- Fix: Substituir o selector quebradiço (classe CSS, ID, nth) por uma alternativa robusta (função ARIA-dados)
- Prevention: Siga a hierarquia do seletor (dados-teste > ARIA > texto > CSS)
- Automation: Correspondência do padrão na mensagem de erro + rastreamento da pilha

---

### Exemplo 2: Padrão comum de falha - Race Co