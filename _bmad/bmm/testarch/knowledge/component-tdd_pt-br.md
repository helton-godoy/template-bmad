# Circulação de desenvolvimento conduzida por ensaios de componentes

## Princípio

Inicie todas as alterações da interface com um teste de componente de falha (`cy.mount`, Playwright ou RTL `render`). Siga o ciclo Red-Green-Refactor: escreva um teste de falha (vermelho), faça-o passar com código mínimo (verde), em seguida, melhore o implementation (refactor). Nave apenas após o ciclo terminar. Mantenha os testes de componentes sob 100 linhas, isolados com novos fornecedores por teste e valide a acessibilidade ao lado da funcionalidade.

## Racional

O componente TDD fornece feedback imediato durante o desenvolvimento. Os testes de falha (vermelho) esclarecem os requisitos antes de escrever o código. Implementações mínimas (verdes) impedem a sobre-engenharia. Refatorar com testes de passagem garante que as alterações não quebram a funcionalidade. Testes isolados com novos fornecedores evitam hemorragias em paralelo. Asserções de acessibilidade pegam questões de usabilidade cedo. A depuração visual (Cypress runner, Storybook, Playwright trace visor) acelera o diagnóstico quando os testes falham.

## Exemplos de padrões

### Exemplo 1: Red-Green-Refactor Loop

**Context**: Ao construir um novo componente, comece com um teste de falha que descreve o comportamento desejado. Implementar apenas o suficiente para passar, em seguida, refator para a qualidade.

**Implementation**:

```typescript
// Step 1: RED - Write failing test
// Button.cy.tsx (Cypress Component Test)
import { Button } from './Button';

describe('Button Component', () => {
  it('should render with label', () => {
    cy.mount(<Button label="Click Me" />);
    cy.contains('Click Me').should('be.visible');
  });

  it('should call onClick when clicked', () => {
    const onClickSpy = cy.stub().as('onClick');
    cy.mount(<Button label="Submit" onClick={onClickSpy} />);

    cy.get('button').click();
    cy.get('@onClick').should('have.been.calledOnce');
  });
});

// Run test: FAILS - Button component doesn't exist yet
// Error: "Cannot find module './Button'"

// Step 2: GREEN - Minimal implementation
// Button.tsx
type ButtonProps = {
  label: string;
  onClick?: () => void;
};

export const Button = ({ label, onClick }: ButtonProps) => {
  return <button onClick={onClick}>{label}</button>;
};

// Run test: PASSES - Component renders and handles clicks

// Step 3: REFACTOR - Improve implementation
// Add disabled state, loading state, variants
type ButtonProps = {
  label: string;
  onClick?: () => void;
  disabled?: boolean;
  loading?: boolean;
  variant?: 'primary' | 'secondary' | 'danger';
};

export const Button = ({
  label,
  onClick,
  disabled = false,
  loading = false,
  variant = 'primary'
}: ButtonProps) => {
  return (
    <button
      onClick={onClick}
      disabled={disabled || loading}
      className={`btn btn-${variant}`}
      data-testid="button"
    >
      {loading ? <Spinner /> : label}
    </button>
  );
};

// Step 4: Expand tests for new features
describe('Button Component', () => {
  it('should render with label', () => {
    cy.mount(<Button label="Click Me" />);
    cy.contains('Click Me').should('be.visible');
  });

  it('should call onClick when clicked', () => {
    const onClickSpy = cy.stub().as('onClick');
    cy.mount(<Button label="Submit" onClick={onClickSpy} />);

    cy.get('button').click();
    cy.get('@onClick').should('have.been.calledOnce');
  });

  it('should be disabled when disabled prop is true', () => {
    cy.mount(<Button label="Submit" disabled={true} />);
    cy.get('button').should('be.disabled');
  });

  it('should show spinner when loading', () => {
    cy.mount(<Button label="Submit" loading={true} />);
    cy.get('[data-testid="spinner"]').should('be.visible');
    cy.get('button').should('be.disabled');
  });

  it('should apply variant styles', () => {
    cy.mount(<Button label="Delete" variant="danger" />);
    cy.get('button').should('have.class', 'btn-danger');
  });
});

// Run tests: ALL PASS - Refactored component still works

// Playwright Component Test equivalent
import { test, expect } from '@playwright/experimental-ct-react';
import { Button } from './Button';

test.describe('Button Component', () => {
  test('should call onClick when clicked', async ({ mount }) => {
    let clicked = false;
    const component = await mount(
      <Button label="Submit" onClick={() => { clicked = true; }} />
    );

    await component.getByRole('button').click();
    expect(clicked).toBe(true);
  });

  test('should be disabled when loading', async ({ mount }) => {
    const component = await mount(<Button label="Submit" loading={true} />);
    await expect(component.getByRole('button')).toBeDisabled();
    await expect(component.getByTestId('spinner')).toBeVisible();
  });
});

```

**Key Pontos**:

- Red: Erro de escrita primeiro - esclarece os requisitos antes da codificação
- Green: Implementar o código mínimo para passar - previne a sobre-engenharia
- Refactor: Melhore a qualidade do código enquanto mantém os testes verdes
- Expand: Adicionar testes para novas funcionalidades após a refatoração
- Repetições do ciclo: Cada novo recurso começa com um teste de falha

### Exemplo 2: Padrão de isolamento do fornecedor

**Context**: Ao testar componentes que dependem de provedores de contexto (React Query, Auth, Router), embrulhe-os com provedores necessários em cada teste para evitar sangramento estado entre testes.

**Implementation**:

```typescript
// test-utils/AllTheProviders.tsx
import { FC, ReactNode } from 'react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { BrowserRouter } from 'react-router-dom';
import { AuthProvider } from '../contexts/AuthContext';

type Props = {
  children: ReactNode;
  initialAuth?: { user: User | null; token: string | null };
};

export const AllTheProviders: FC<Props> = ({ children, initialAuth }) => {
  // Create NEW QueryClient per test (prevent state bleed)
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: { retry: false },
      mutations: { retry: false }
    }
  });

  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <AuthProvider initialAuth={initialAuth}>
          {children}
        </AuthProvider>
      </BrowserRouter>
    </QueryClientProvider>
  );
};

// Cypress custom mount command
// cypress/support/component.tsx
import { mount } from 'cypress/react18';
import { AllTheProviders } from '../../test-utils/AllTheProviders';

Cypress.Commands.add('wrappedMount', (component, options = {}) => {
  const { initialAuth, ...mountOptions } = options;

  return mount(
    <AllTheProviders initialAuth={initialAuth}>
      {component}
    </AllTheProviders>,
    mountOptions
  );
});

// Usage in tests
// UserProfile.cy.tsx
import { UserProfile } from './UserProfile';

describe('UserProfile Component', () => {
  it('should display user when authenticated', () => {
    const user = { id: 1, name: 'John Doe', email: 'john@example.com' };

    cy.wrappedMount(<UserProfile />, {
      initialAuth: { user, token: 'fake-token' }
    });

    cy.contains('John Doe').should('be.visible');
    cy.contains('john@example.com').should('be.visible');
  });

  it('should show login prompt when not authenticated', () => {
    cy.wrappedMount(<UserProfile />, {
      initialAuth: { user: null, token: null }
    });

    cy.contains('Please log in').should('be.visible');
  });
});

// Playwright Component Test with providers
import { test, expect } from '@playwright/experimental-ct-react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { UserProfile } from './UserProfile';
import { AuthProvider } from '../contexts/AuthContext';

test.describe('UserProfile Component', () => {
  test('should display user when authenticated', async ({ mount }) => {
    const user = { id: 1, name: 'John Doe', email: 'john@example.com' };
    const queryClient = new QueryClient();

    const component = await mount(
      <QueryClientProvider client={queryClient}>
        <AuthProvider initialAuth={{ user, token: 'fake-token' }}>
          <UserProfile />
        </AuthProvider>
      </QueryClientProvider>
    );

    await expect(component.getByText('John Doe')).toBeVisible();
    await expect(component.getByText('john@example.com')).toBeVisible();
  });
});

```

**Key Pontos**:

- Criar novos fornecedores por teste (QueryClient, Router, Auth)
- Evita a poluição estatal entre testes
- `initialAuth` prop permite testar diferentes estados de autenticação
- Comando de montagem personalizado (`wrappedMount`) reduz a placa de caldeira
- Providers wrap component, não todo o conjunto de testes

### Exemplo 3: Asserções de Acessibilidade

**Context**: Ao testar componentes, valide a acessibilidade ao lado da funcionalidade usando axe-core, papéis ARIA, rótulos e navegação de teclado.

**Implementation**:

```typescript
// Cypress with axe-core
// cypress/support/component.tsx
import 'cypress-axe';

// Form.cy.tsx
import { Form } from './Form';

describe('Form Component Accessibility', () => {
  beforeEach(() => {
    cy.wrappedMount(<Form />);
    cy.injectAxe(); // Inject axe-core
  });

  it('should have no accessibility violations', () => {
    cy.checkA11y(); // Run axe scan
  });

  it('should have proper ARIA labels', () => {
    cy.get('input[name="email"]').should('have.attr', 'aria-label', 'Email address');
    cy.get('input[name="password"]').should('have.attr', 'aria-label', 'Password');
    cy.get('button[type="submit"]').should('have.attr', 'aria-label', 'Submit form');
  });

  it('should support keyboard navigation', () => {
    // Tab through form fields
    cy.get('input[name="email"]').focus().type('test@example.com');
    cy.realPress('Tab'); // cypress-real-events plugin
    cy.focused().should('have.attr', 'name', 'password');

    cy.focused().type('password123');
    cy.realPress('Tab');
    cy.focused().should('have.attr', 'type', 'submit');

    cy.realPress('Enter'); // Submit via keyboard
    cy.contains('Form submitted').should('be.visible');
  });

  it('should announce errors to screen readers', () => {
    cy.get('button[type="submit"]').click(); // Submit without data

    // Error has role="alert" and aria-live="polite"
    cy.get('[role="alert"]')
      .should('be.visible')
      .and('have.attr', 'aria-live', 'polite')
      .and('contain', 'Email is required');
  });

  it('should have sufficient color contrast', () => {
    cy.checkA11y(null, {
      rules: {
        'color-contrast': { enabled: true }
      }
    });
  });
});

// Playwright with axe-playwright
import { test, expect } from '@playwright/experimental-ct-react';
import AxeBuilder from '@axe-core/playwright';
import { Form } from './Form';

test.describe('Form Component Accessibility', () => {
  test('should have no accessibility violations', async ({ mount, page }) => {
    await mount(<Form />);

    const accessibilityScanResults = await new AxeBuilder({ page })
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('should support keyboard navigation', async ({ mount, page }) => {
    const component = await mount(<Form />);

    await component.getByLabel('Email address').fill('test@example.com');
    await page.keyboard.press('Tab');

    await expect(component.getByLabel('Password')).toBeFocused();

    await component.getByLabel('Password').fill('password123');
    await page.keyboard.press('Tab');

    await expect(component.getByRole('button', { name: 'Submit form' })).toBeFocused();

    await page.keyboard.press('Enter');
    await expect(component.getByText('Form submitted')).toBeVisible();
  });
});

```

**Key Pontos**:

- Use `cy.checkA11y()` (Cypress) ou `AxeBuilder` (Playwright) para digitalização automatizada de acessibilidade
- Validar papéis, rótulos e regiões vivas da ARIA
- Testar navegação de teclado (Tab, Enter, Escape)
- Garantir erros são anunciados aos leitores de tela (`role="alert"`, `aria-live`)
- Verificar contraste de cor atende aos padrões WCAG

### Exemplo 4: Teste de Regressão Visual

**Context**: Ao testar componentes, capture capturas de tela para detectar alterações visuais não intencionadas. Usar comparação visual Playwright ou plugins de instantâneo Cypress.

**Implementation**:

```typescript
// Playwright visual regression
import { test, expect } from '@playwright/experimental-ct-react';
import { Button } from './Button';

test.describe('Button Visual Regression', () => {
  test('should match primary button snapshot', async ({ mount }) => {
    const component = await mount(<Button label="Primary" variant="primary" />);

    // Capture and compare screenshot
    await expect(component).toHaveScreenshot('button-primary.png');
  });

  test('should match secondary button snapshot', async ({ mount }) => {
    const component = await mount(<Button label="Secondary" variant="secondary" />);
    await expect(component).toHaveScreenshot('button-secondary.png');
  });

  test('should match disabled button snapshot', async ({ mount }) => {
    const component = await mount(<Button label="Disabled" disabled={true} />);
    await expect(component).toHaveScreenshot('button-disabled.png');
  });

  test('should match loading button snapshot', async ({ mount }) => {
    const component = await mount(<Button label="Loading" loading={true} />);
    await expect(component).toHaveScreenshot('button-loading.png');
  });
});

// Cypress visual regression with percy or snapshot plugins
import { Button } from './Button';

describe('Button Visual Regression', () => {
  it('should match primary button snapshot', () => {
    cy.wrappedMount(<Button label="Primary" variant="primary" />);

    // Option 1: Percy (cloud-based visual testing)
    cy.percySnapshot('Button - Primary');

    // Option 2: cypress-plugin-snapshots (local snapshots)
    cy.get('button').toMatchImageSnapshot({
      name: 'button-primary',
      threshold: 0.01 // 1% threshold for pixel differences
    });
  });

  it('should match hover state', () => {
    cy.wrappedMount(<Button label="Hover Me" />);
    cy.get('button').realHover(); // cypress-real-events
    cy.percySnapshot('Button - Hover State');
  });

  it('should match focus state', () => {
    cy.wrappedMount(<Button label="Focus Me" />);
    cy.get('button').focus();
    cy.percySnapshot('Button - Focus State');
  });
});

// Playwright configuration for visual regression
// playwright.config.ts
export default defineConfig({
  expect: {
    toHaveScreenshot: {
      maxDiffPixels: 100, // Allow 100 pixels difference
      threshold: 0.2 // 20% threshold
    }
  },
  use: {
    screenshot: 'only-on-failure'
  }
});

// Update snapshots when intentional changes are made
// npx playwright test --update-snapshots

```

**Key Pontos**:

- Playwright: Use `toHaveScreenshot()` para comparação visual integrada
- Cypress: Usar plug- ins Percy (nuvem) ou instantâneo (local) para testes visuais
- Capture estados diferentes: padrão, hover, foco, desativado, carregando
- Definir limite para diferenças aceitáveis de pixels (evitar false positivos)
- Atualizar instantâneos quando as alterações visuais são intencionais
- Testes visuais capturam regressões não intencionadas de CSS/layout

## Pontos de Integração

- **Used em fluxos de trabalho**: `*atdd` (geração de testes componentes), `*automate` (expansão de testes componentes), `*framework` (configuração de testes componentes)
- * Fragmentos *Related**:
- `test-quality.md` - Mantenha os testes de componentes < 100 linhas, isoladas, focadas
- `fixture-architecture.md` - Padrões de embrulho do fornecedor, comandos personalizados de montagem
- `data-factories.md` - Funções de fábrica para adereços de componentes
- `test-levels-framework.md` - Quando utilizar testes componentes vs E2E

## Resumo do fluxo de trabalho TDD

* *Red-Green-Refactor Cycle**:

1. **Red**: Erro ao escrever o teste descrevendo o comportamento desejado
2. **Green**: Implementar o código mínimo para fazer o teste passar
3. **Refactor**: Melhorar a qualidade do código, testes permanecer verde
4. **Repeat**: Cada novo recurso começa com o teste de falha

**Component Test Checklist**:

- [ ] Rendimentos de ensaio com suportes necessários
- [ ] Teste as interações do usuário (clique, digite, envie)
- [ ] Teste estados diferentes (carregando, erro, desabilitado)
- [ ] Testar acessibilidade (ARIA, navegação com teclado)
- [ ] Teste de regressão visual (snapshots)
- [ ] Isole com novos fornecedores (sem hemorragia do estado)
- [ ] Manter testes < 100 linhas (divididas por intenção)

_Source: CCTDD repositório, Murat componentes testing talks, Playwright/Cypress componente testing docs.
