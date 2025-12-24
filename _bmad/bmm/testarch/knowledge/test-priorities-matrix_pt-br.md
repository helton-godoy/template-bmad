<!-- Powered by BMAD-CORE™ -->

# Matriz de Prioridades de Teste

Guia para priorizar cenários de teste baseado em risco, criticalidade e impacto no negócio.

## Níveis de Prioridade

### P0 - Crítico (Deve Testar)

**Critérios:**

- Funcionalidade com impacto em receita
- Caminhos críticos de segurança
- Operações de integridade de dados
- Requisitos de conformidade regulatória
- Funcionalidade quebrada anteriormente (prevenção de regressão)

**Exemplos:**

- Processamento de pagamento
- Autenticação/autorização
- Criação/deleção de dados de usuário
- Cálculos financeiros
- Conformidade GDPR/privacidade

**Requisitos de Teste:**

- Cobertura abrangente em todos os níveis
- Caminhos felizes e infelizes
- Casos de borda e cenários de erro
- Performance sob carga

### P1 - Alto (Deveria Testar)

**Critérios:**

- Jornadas de usuário principais
- Funcionalidades usadas frequentemente
- Funcionalidades com lógica complexa
- Pontos de integração entre sistemas
- Funcionalidades afetando experiência do usuário

**Exemplos:**

- Fluxo de registro de usuário
- Funcionalidade de busca
- Importação/exportação de dados
- Sistemas de notificação
- Exibições de dashboard

**Requisitos de Teste:**

- Caminhos felizes primários obrigatórios
- Cenários de erro chave
- Casos de borda críticos
- Validação de performance básica

### P2 - Médio (Bom Testar)

**Critérios:**

- Funcionalidades secundárias
- Funcionalidade de admin
- Funcionalidades de relatório
- Opções de configuração
- Polimento de UI e estética

**Exemplos:**

- Painéis de configurações de admin
- Geração de relatório
- Customização de tema
- Documentação de ajuda
- Rastreamento de analytics

**Requisitos de Teste:**

- Cobertura de caminho feliz
- Tratamento de erro básico
- Pode adiar casos de borda

### P3 - Baixo (Testar se Houver Tempo)

**Critérios:**

- Funcionalidades raramente usadas
- Funcionalidade "nice-to-have"
- Problemas cosméticos
- Otimizações não críticas

**Exemplos:**

- Preferências avançadas
- Suporte a funcionalidade legada
- Funcionalidades experimentais
- Utilitários de debug

**Requisitos de Teste:**

- Apenas smoke tests
- Pode confiar em teste manual
- Documentar limitações conhecidas

## Ajustes de Prioridade Baseados em Risco

### Aumentar Prioridade Quando:

- Alto impacto no usuário (afeta >50% dos usuários)
- Alto impacto financeiro (>$10K perda potencial)
- Potencial de vulnerabilidade de segurança
- Requisitos de conformidade/legais
- Problemas reportados por clientes
- Implementação complexa (>500 LOC)
- Múltiplas dependências de sistema

### Diminuir Prioridade Quando:

- Protegido por feature flag
- Rollout gradual planejado
- Monitoramento forte implementado
- Capacidade de rollback fácil
- Métricas de uso baixo
- Implementação simples
- Componente bem isolado

## Cobertura de Teste por Prioridade

| Prioridade | Cobertura Unitária | Cobertura de Integração | Cobertura E2E      |
| ---------- | ------------------ | ----------------------- | ------------------ |
| P0         | >90%               | >80%                    | Todos caminhos críticos |
| P1         | >80%               | >60%                    | Principais caminhos felizes |
| P2         | >60%               | >40%                    | Smoke tests        |
| P3         | Melhor esforço     | Melhor esforço          | Apenas manual      |

## Regras de Atribuição de Prioridade

1. **Comece com impacto no negócio** - O que acontece se isso falhar?
2. **Considere probabilidade** - Quão provável é a falha?
3. **Fatore detectabilidade** - Saberíamos se falhasse?
4. **Considere recuperabilidade** - Podemos consertar rapidamente?

## Árvore de Decisão de Prioridade

```
É crítico para receita?
├─ SIM → P0
└─ NÃO → Afeta jornada de usuário principal?
    ├─ SIM → É de alto risco?
    │   ├─ SIM → P0
    │   └─ NÃO → P1
    └─ NÃO → É usado frequentemente?
        ├─ SIM → P1
        └─ NÃO → É voltado para cliente?
            ├─ SIM → P2
            └─ NÃO → P3
```

## Ordem de Execução de Teste

1. Execute testes P0 primeiro (falhe rápido em problemas críticos)
2. Execute testes P1 segundo (funcionalidade principal)
3. Execute testes P2 se houver tempo
4. Testes P3 apenas em ciclos de regressão completa

## Ajuste Contínuo

Revise e ajuste prioridades baseado em:

- Padrões de incidentes de produção
- Feedback de usuários e reclamações
- Analytics de uso
- Histórico de falha de teste
- Mudanças de prioridade de negócio

---

## Classificação de Prioridade Automatizada

### Exemplo: Calculadora de Prioridade (Automação Baseada em Risco)

```typescript
// src/testing/priority-calculator.ts

export type Priority = 'P0' | 'P1' | 'P2' | 'P3';

export type PriorityFactors = {
  revenueImpact: 'critical' | 'high' | 'medium' | 'low' | 'none';
  userImpact: 'all' | 'majority' | 'some' | 'few' | 'minimal';
  securityRisk: boolean;
  complianceRequired: boolean;
  previousFailure: boolean;
  complexity: 'high' | 'medium' | 'low';
  usage: 'frequent' | 'regular' | 'occasional' | 'rare';
};

/**
 * Calcular prioridade de teste baseado em múltiplos fatores
 * Espelha a árvore de decisão de prioridade com critérios objetivos
 */
export function calculatePriority(factors: PriorityFactors): Priority {
  const { revenueImpact, userImpact, securityRisk, complianceRequired, previousFailure, complexity, usage } = factors;

  // P0: Crítico para receita, segurança ou conformidade
  if (revenueImpact === 'critical' || securityRisk || complianceRequired || (previousFailure && revenueImpact === 'high')) {
    return 'P0';
  }

  // P0: Alta receita + alta complexidade + uso frequente
  if (revenueImpact === 'high' && complexity === 'high' && usage === 'frequent') {
    return 'P0';
  }

  // P1: Jornada de usuário principal (maioria impactada + uso frequente)
  if (userImpact === 'all' || userImpact === 'majority') {
    if (usage === 'frequent' || complexity === 'high') {
      return 'P1';
    }
  }

  // P1: Alta receita OU alta complexidade com uso regular
  if ((revenueImpact === 'high' && usage === 'regular') || (complexity === 'high' && usage === 'frequent')) {
    return 'P1';
  }

  // P2: Funcionalidades secundárias (algum impacto, uso ocasional)
  if (userImpact === 'some' || usage === 'occasional') {
    return 'P2';
  }

  // P3: Raramente usado, baixo impacto
  return 'P3';
}

/**
 * Gerar justificativa de prioridade (para trilha de auditoria)
 */
export function justifyPriority(factors: PriorityFactors): string {
  const priority = calculatePriority(factors);
  const reasons: string[] = [];

  if (factors.revenueImpact === 'critical') reasons.push('impacto crítico em receita');
  if (factors.securityRisk) reasons.push('crítico para segurança');
  if (factors.complianceRequired) reasons.push('requisito de conformidade');
  if (factors.previousFailure) reasons.push('prevenção de regressão');
  if (factors.userImpact === 'all' || factors.userImpact === 'majority') {
    reasons.push(`impacta ${factors.userImpact} usuários`);
  }
  if (factors.complexity === 'high') reasons.push('alta complexidade');
  if (factors.usage === 'frequent') reasons.push('usado frequentemente');

  return `${priority}: ${reasons.join(', ')}`;
}

/**
 * Exemplo: Cálculo de prioridade de cenário de pagamento
 */
const paymentScenario: PriorityFactors = {
  revenueImpact: 'critical',
  userImpact: 'all',
  securityRisk: true,
  complianceRequired: true,
  previousFailure: false,
  complexity: 'high',
  usage: 'frequent',
};

console.log(calculatePriority(paymentScenario)); // 'P0'
console.log(justifyPriority(paymentScenario));
// 'P0: impacto crítico em receita, crítico para segurança, requisito de conformidade, impacta todos os usuários, alta complexidade, usado frequentemente'
```

### Exemplo: Estratégia de Tagging de Suite de Teste

```typescript
// tests/e2e/checkout.spec.ts
import { test, expect } from '@playwright/test';

// Taggear testes com prioridade para execução seletiva
test.describe('Fluxo de Checkout', () => {
  test('pagamento válido completa com sucesso @p0 @smoke @revenue', async ({ page }) => {
    // P0: Caminho feliz crítico para receita
    await page.goto('/checkout');
    await page.getByTestId('payment-method').selectOption('credit-card');
    await page.getByTestId('card-number').fill('4242424242424242');
    await page.getByRole('button', { name: 'Place Order' }).click();

    await expect(page.getByText('Order confirmed')).toBeVisible();
  });

  test('cartão expirado mostra erro amigável @p1 @error-handling', async ({ page }) => {
    // P1: Cenário de erro principal (impacto frequente no usuário)
    await page.goto('/checkout');
    await page.getByTestId('payment-method').selectOption('credit-card');
    await page.getByTestId('card-number').fill('4000000000000069'); // Cartão de teste: expirado
    await page.getByRole('button', { name: 'Place Order' }).click();

    await expect(page.getByText('Card expired. Please use a different card.')).toBeVisible();
  });

  test('código de cupom aplica desconto corretamente @p2', async ({ page }) => {
    // P2: Funcionalidade secundária (bom ter)
    await page.goto('/checkout');
    await page.getByTestId('coupon-code').fill('SAVE10');
    await page.getByRole('button', { name: 'Apply' }).click();

    await expect(page.getByText('10% discount applied')).toBeVisible();
  });

  test('formatação de mensagem de presente preservada @p3', async ({ page }) => {
    // P3: Funcionalidade cosmética (raramente usada)
    await page.goto('/checkout');
    await page.getByTestId('gift-message').fill('Happy Birthday!\n\nWith love.');
    await page.getByRole('button', { name: 'Place Order' }).click();

    // Formatação de mensagem preservada (quebras de linha intactas)
    await expect(page.getByTestId('order-summary')).toContainText('Happy Birthday!');
  });
});
```

**Rodar testes por prioridade:**

```bash
# Apenas P0 (smoke tests, 2-5 min)
npx playwright test --grep @p0

# P0 + P1 (funcionalidade principal, 10-15 min)
npx playwright test --grep "@p0|@p1"

# Regressão completa (todas as prioridades, 30+ min)
npx playwright test
```

---

## Integração com Pontuação de Risco

A prioridade deve alinhar com a pontuação de risco de `probability-impact.md`:

| Pontuação de Risco | Prioridade Típica | Motivação                                  |
| ------------------ | ----------------- | ------------------------------------------ |
| 9                  | P0                | Bloqueador crítico (probabilidade=3, impacto=3) |
| 6-8                | P0 ou P1          | Alto risco (requer mitigação)              |
| 4-5                | P1 ou P2          | Risco médio (monitorar de perto)           |
| 1-3                | P2 ou P3          | Baixo risco (documentar e adiar)           |

**Exemplo**: Pontuação de risco 9 (falha de API de checkout) → Prioridade P0 → cobertura abrangente necessária.

## Checklist de Prioridade

Antes de finalizar prioridades de teste:

- [ ] **Impacto em receita avaliado**: Funcionalidades de pagamento, assinatura, faturamento → P0
- [ ] **Riscos de segurança identificados**: Auth, exposição de dados, ataques de injeção → P0
- [ ] **Requisitos de conformidade documentados**: GDPR, PCI-DSS, SOC2 → P0
- [ ] **Impacto no usuário quantificado**: >50% usuários → P0/P1, <10% → P2/P3
- [ ] **Falhas anteriores revisadas**: Prevenção de regressão → aumentar prioridade
- [ ] **Complexidade avaliada**: >500 LOC ou múltiplas dependências → aumentar prioridade
- [ ] **Métricas de uso consultadas**: Uso frequente → P0/P1, uso raro → P2/P3
- [ ] **Cobertura de monitoramento confirmada**: Monitoramento forte → pode diminuir prioridade
- [ ] **Capacidade de rollback verificada**: Rollback fácil → pode diminuir prioridade
- [ ] **Prioridades taggeadas em testes**: @p0, @p1, @p2, @p3 para execução seletiva

## Pontos de Integração

- **Usado em workflows**: `*automate` (geração de teste baseada em prioridade), `*test-design` (priorização de cenário), `*trace` (validação de cobertura por prioridade)
- **Fragmentos relacionados**: `risk-governance.md` (pontuação de risco), `probability-impact.md` (avaliação de impacto), `selective-testing.md` (execução baseada em tag)
- **Ferramentas**: Playwright/Cypress grep para filtragem de tag, scripts CI para execução baseada em prioridade

_Fonte: Práticas de teste baseadas em risco, estratégias de priorização de teste, análise de incidente de produção_
