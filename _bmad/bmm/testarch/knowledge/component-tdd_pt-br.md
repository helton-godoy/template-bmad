# Circulação de desenvolvimento conduzida por testes de componentes

## Princípio

Iniciar todas as alterações de UI com um teste de componente de falha (`cy.mount`, Playwright component test ou RTL `render`). Siga o ciclo Red-Green-Refactor: escreva um teste de falha (vermelho), faça-o passar com código mínimo (verde), em seguida, melhore o implementation (refactor). Nave só depois do ciclo terminar. Mantenha os testes de componentes sob 100 linhas, isolados com novos fornecedores por teste e valide a acessibilidade ao lado da funcionalidade.

## Racional

O componente TDD fornece feedback imediato durante o desenvolvimento. Os testes de falha (vermelho) esclarecem os requisitos antes de escrever o código. Implementações mínimas (verdes) impedem o excesso de engenharia. Refatorar com testes de passagem garante que as alterações não quebram a funcionalidade. Testes isolados com novos fornecedores evitam hemorragias de estado em paralelo. Asserções de acessibilidade capturam questões de usabilidade precocemente. A depuração visual (Cypress runner, Storybook, Playwright trace viewer) acelera o diagnóstico quando os testes falham.

## Exemplos de padrões

### Exemplo 1: Ciclo de Refactor Vermelho-Verde

**Contexto**: Ao construir um novo componente, comece com um teste que descreva o comportamento desejado. Implementar apenas o suficiente para passar, em seguida, refator para a qualidade.

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

**Pontos-chave**

- Red: Erro de escrita primeiro - esclarece os requisitos antes da codificação
- Green: Implementar o código mínimo para passar - previne o excesso de engenharia
- Refactor: Melhorar a qualidade do código mantendo os testes verdes
- Expand: Adicionar testes para novas funcionalidades após a refatoração
- Repetições do ciclo: Cada novo recurso começa com um teste de falha

### Exemplo 2: Fornecedor Iso