# Governança de risco e manutenção de portas

## Princípio

A governança do risco transforma os debates subjetivos em decisões objetivas e orientadas por dados. Ao pontuar risco (probabilidade × impacto), classificando por categoria (TECH, SEC, PERF, etc.) e rastreando propriedade de mitigação, as equipes criam portões de qualidade transparentes que equilibram velocidade com segurança.

## Racional

**The Problem**: Sem governança formal de risco, os lançamentos se tornam políticos – vozes altas ganham, riscos silenciosos se escondem e equipes descobrem questões críticas na produção. "Achámos que estava tudo bem" não é uma estratégia de lançamento.

**The Solution**: Escala de risco (1-3 para probabilidade e impacto, total 1-9) cria linguagem compartilhada. Pontuações ≥6 demanda mitigação documentada. Pontuações = 9 falha na porta do mandato. Cada critério de aceitação mapeia para um teste, e lacunas exigem renúncias explícitas com proprietários e datas de validade.

**Por que isso importa**:

- Elimina ambiguidade das decisões de libertação (pontuações objetivas vs opiniões subjetivas)
- Cria trilha de auditoria para conformidade (FDA, SOC2, ISO exigem gerenciamento de risco documentado)
- Identifica true bloqueadores precoces (prevene incêndios de produção de última hora)
- Distribui responsabilidade (proprietários, planos de mitigação, prazos para cada risco >4)

## Exemplos de padrões

### Exemplo 1: Matriz de pontuação de risco com classificação automatizada (TypeScript)

**Contexto**: Calcular automaticamente as pontuações de risco a partir dos resultados dos testes e categorizar por tipo de risco

**Implementation**:

```typescript
// risk-scoring.ts - Risk classification and scoring system
export const RISK_CATEGORIES = {
  TECH: 'TECH', // Technical debt, architecture fragility
  SEC: 'SEC', // Security vulnerabilities
  PERF: 'PERF', // Performance degradation
  DATA: 'DATA', // Data integrity, corruption
  BUS: 'BUS', // Business logic errors
  OPS: 'OPS', // Operational issues (deployment, monitoring)
} as const;

export type RiskCategory = keyof typeof RISK_CATEGORIES;

export type RiskScore = {
  id: string;
  category: RiskCategory;
  title: string;
  description: string;
  probability: 1 | 2 | 3; // 1=Low, 2=Medium, 3=High
  impact: 1 | 2 | 3; // 1=Low, 2=Medium, 3=High
  score: number; // probability × impact (1-9)
  owner: string;
  mitigationPlan?: string;
  deadline?: Date;
  status: 'OPEN' | 'MITIGATED' | 'WAIVED' | 'ACCEPTED';
  waiverReason?: string;
  waiverApprover?: string;
  waiverExpiry?: Date;
};

// Risk scoring rules
export function calculateRiskScore(probability: 1 | 2 | 3, impact: 1 | 2 | 3): number {
  return probability * impact;
}

export function requiresMitigation(score: number): boolean {
  return score >= 6; // Scores 6-9 demand action
}

export function isCriticalBlocker(score: number): boolean {
  return score === 9; // Probability=3 AND Impact=3 → FAIL gate
}

export function classifyRiskLevel(score: number): 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL' {
  if (score === 9) return 'CRITICAL';
  if (score >= 6) return 'HIGH';
  if (score >= 4) return 'MEDIUM';
  return 'LOW';
}

// Example: Risk assessment from test failures
export function assessTestFailureRisk(failure: {
  test: string;
  category: RiskCategory;
  affectedUsers: number;
  revenueImpact: number;
  securityVulnerability: boolean;
}): RiskScore {
  // Probability based on test failure frequency (simplified)
  const probability: 1 | 2 | 3 = 3; // Test failed = High probability

  // Impact based on business context
  let impact: 1 | 2 | 3 = 1;
  if (failure.securityVulnerability) impact = 3;
  else if (failure.revenueImpact > 10000) impact = 3;
  else if (failure.affectedUsers > 1000) impact = 2;
  else impact = 1;

  const score = calculateRiskScore(probability, impact);

  return {
    id: `risk-${Date.now()}`,
    category: failure.category,
    title: `Test failure: ${failure.test}`,
    description: `Affects ${failure.affectedUsers} users, $${failure.revenueImpact} revenue`,
    probability,
    impact,
    score,
    owner: 'unassigned',
    status: score === 9 ? 'OPEN' : 'OPEN',
  };
}

```

**Pontos-chave**

- **pontuação do objectivo**: probabilidade (1-3) × impacto (1-3) = pontuação (1-9)
- **Limpos claros**: Pontuação ≥6 requer mitigação, pontuação = 9 blocos de liberação
- **Contexto empresarial**: Receita, usuários, cálculo de impacto da unidade de segurança
- **Status tracking**: ABERTO → MITIGADO → WAIVED → Ciclo de vida aceite

---

### Exemplo 2: Motor de decisão de porta com validação de rastreabilidade

**Contexto**: Decisão automática da porta baseada em pontuações de risco e cobertura de testes

**Implementation**:

«``typescript
// gate-decision-engine.ts
BMADPROTECT009End type GateDecision = 'PASS' □ 'CONCERNS'

export type CoverageGap = {
  acceptanceCriteria: string;
  testMissing: string;
  reason: string;
};

export tipo GateResult = {
  decision: GateDecision;
  timestamp: Date;
  criticalRisks: RiskScore[];
  highRisks: RiskScore[];
  coverageGaps: CoverageGap[];
  summary: string;
  recommendations: string[];
};

export function assessmentGate(params: { risks: RiskScore[]; coverageGaps: CoverageGap[]; waiverApprover?: string }): GateResult {
const {