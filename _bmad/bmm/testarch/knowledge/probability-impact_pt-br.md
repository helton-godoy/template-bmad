# Escala de probabilidade e impacto

## Princípio

A pontuação de risco utiliza uma matriz “probabilidade × impacto” (1-9 escala) para priorizar os esforços de teste. Escores mais elevados (6-9) exigem ação imediata; escores mais baixos (1-3) requerem apenas documentação. Esta abordagem sistemática garante que os recursos de teste se concentrem nos riscos de maior valor.

## Racional

**O Problema**: Sem avaliação de risco quantificável, as equipes testam cenários de baixo valor sem riscos críticos. A sensação de gut leva a uma priorização inconsistente e casos de borda perdidos.

**A Solução**: Normalizar a avaliação de risco com uma matriz 3×3 (probabilidade: 1-3, impacto: 1-3). Multiplique para obter pontuação de risco (1-9). Classificação automática (DOCUMENTO, MONITOR, MITIGATE, BLOCK) com base em limiares. Esta abordagem enfrenta riscos ocultos precocemente e justifica decisões de teste para as partes interessadas.

**Por que isso importa**:

- Linguagem de risco consistente entre produtos, engenharia e QA
- Priorização objetiva de cenários de teste (não de política)
- Decisões automáticas (escore=9 → FAIL até resolvido)
- pista de auditoria para conformidade e retrospectivas

## Exemplos de padrões

### Exemplo 1: Matriz de probabilidade-impacto Implementation (Classificação automatizada)

**Contexto**: Aplicar um sistema de pontuação de risco reutilizável com classificação automática de limiar

**Implementation**:

```typescript
// src/testing/risk-matrix.ts

/**
 * Probability levels:
 * 1 = Unlikely (standard implementation, low uncertainty)
 * 2 = Possible (edge cases or partial unknowns)
 * 3 = Likely (known issues, new integrations, high ambiguity)
 */
export type Probability = 1 | 2 | 3;

/**
 * Impact levels:
 * 1 = Minor (cosmetic issues or easy workarounds)
 * 2 = Degraded (partial feature loss or manual workaround)
 * 3 = Critical (blockers, data/security/regulatory exposure)
 */
export type Impact = 1 | 2 | 3;

/**
 * Risk score (probability × impact): 1-9
 */
export type RiskScore = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;

/**
 * Action categories based on risk score thresholds
 */
export type RiskAction = 'DOCUMENT' | 'MONITOR' | 'MITIGATE' | 'BLOCK';

export type RiskAssessment = {
  probability: Probability;
  impact: Impact;
  score: RiskScore;
  action: RiskAction;
  reasoning: string;
};

/**
 * Calculate risk score: probability × impact
 */
export function calculateRiskScore(probability: Probability, impact: Impact): RiskScore {
  return (probability * impact) as RiskScore;
}

/**
 * Classify risk action based on score thresholds:
 * - 1-3: DOCUMENT (awareness only)
 * - 4-5: MONITOR (watch closely, plan mitigations)
 * - 6-8: MITIGATE (CONCERNS at gate until mitigated)
 * - 9: BLOCK (automatic FAIL until resolved or waived)
 */
export function classifyRiskAction(score: RiskScore): RiskAction {
  if (score >= 9) return 'BLOCK';
  if (score >= 6) return 'MITIGATE';
  if (score >= 4) return 'MONITOR';
  return 'DOCUMENT';
}

/**
 * Full risk assessment with automatic classification
 */
export function assessRisk(params: { probability: Probability; impact: Impact; reasoning: string }): RiskAssessment {
  const { probability, impact, reasoning } = params;

  const score = calculateRiskScore(probability, impact);
  const action = classifyRiskAction(score);

  return { probability, impact, score, action, reasoning };
}

/**
 * Generate risk matrix visualization (3x3 grid)
 * Returns markdown table with color-coded scores
 */
export function generateRiskMatrix(): string {
  const matrix: string[][] = [];
  const header = ['Impact \\ Probability', 'Unlikely (1)', 'Possible (2)', 'Likely (3)'];
  matrix.push(header);

  const impactLabels = ['Critical (3)', 'Degraded (2)', 'Minor (1)'];
  for (let impact = 3; impact >= 1; impact--) {
    const row = [impactLabels[3 - impact]];
    for (let probability = 1; probability <= 3; probability++) {
      const score = calculateRiskScore(probability as Probability, impact as Impact);
      const action = classifyRiskAction(score);
      const emoji = action === 'BLOCK' ? '🔴' : action === 'MITIGATE' ? '🟠' : action === 'MONITOR' ? '🟡' : '🟢';
      row.push(`${emoji} ${score}`);
    }
    matrix.push(row);
  }

  return matrix.map((row) => `| ${row.join(' | ')} |`).join('\n');
}

```

**Pontos-chave**

- Probabilidade/impacto seguro de tipo (1-3 aplicado no momento da compilação)
- Classificação de ação automática (DOCUMENTO, MONITOR, MITIGATE, BLOCK)
- Geração de matriz visual para documentação
- Fórmula da pontuação de risco: `probability * impact` (máx = 9)
- Regras de decisão baseadas em limiares (6-8 = MITIGATE, 9 = BLOCK)

---

### Exemplo 2: Fluxo de trabalho de avaliação de risco (integração do teste Planning)

**Contexto**: Aplicar matriz de risco durante o projeto do teste para priorizar cenários

**Implementation**:

«``typescript
// tests/e2e/test-planning/risk-assessment.ts
import BMADPROTECT013End from '../../../../src/teste/matriz de risco «;

export tipo TestScenario = {
  id: string;
  title: string;
  feature: string;
  risk: RiskAssessment;
TestLevel: 'E2E' □ 'API' □ 'Unit';
Prioridade: 'P0'