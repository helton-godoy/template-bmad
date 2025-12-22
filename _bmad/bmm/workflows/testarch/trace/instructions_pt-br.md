# Fluxo de trabalho do arquiteto de teste: Requisitos Rastreabilidade e Decisão da porta de qualidade

**Fluxo de trabalho:** `testarch-trace`
**Composto:** Gerar matriz de rastreabilidade de requisitos-para-testes, analisar lacunas de cobertura e tomar decisões de porta de qualidade (PASS/CONCERNS/FAIL/WAIVED)
**Agente:** Arquiteto de ensaio (TEA)
**Formato:** Puro Markdown v4.0 (sem blocos XML)

---

## Overview

This workflow operates in two sequential phases to validate test coverage and deployment readiness:

**PHASE 1 - REQUIREMENTS TRACEABILITY:** Create comprehensive traceability matrix mapping acceptance criteria to implemented tests, identify coverage gaps, and provide actionable recommendations.

**PHASE 2 - QUALITY GATE DECISION:** Use traceability results combined with test execution evidence to make gate decisions (PASS/CONCERNS/FAIL/WAIVED) that determine deployment readiness.

**Key Capabilities:**

- Map acceptance criteria to specific test cases across all levels (E2E, API, Component, Unit)
- Classify coverage status (FULL, PARTIAL, NONE, UNIT-ONLY, INTEGRATION-ONLY)
- Prioritize gaps by risk level (P0/P1/P2/P3) using test-priorities framework
- Apply deterministic decision rules based on coverage and test execution results
- Generate gate decisions with evidence and rationale
- Support waivers for business-approved exceptions
- Update workflow status and notify stakeholders

---

## Pré-requisitos

**Requisito (Fase 1):**

- Critérios de aceitação (do arquivo de história OU fornecido em linha)
- Conjunto de testes implementado (ou reconhecer lacunas a serem resolvidas)

**Requerido (Fase 2 - se `enable_gate_decision: true`):**

- Resultados da execução do ensaio (relatórios de ensaios IC/CD, taxas de passagem/falta)
- Desenho de ensaio com prioridades de risco (P0/P1/P2/P3)

**Recomendado:**

- `test-design.md` (para avaliação dos riscos e contexto prioritário)
- `nfr-assessment.md` (para portões de nível de libertação)
- `tech-spec.md` (para o contexto técnico implementation)
- Configuração do framework de teste (playwright. config.ts, jest.config.js, etc.)

**Condições de sal:**

- Se a história não tiver quaisquer testes implementados E não forem reconhecidas lacunas, recomendo que execute primeiro o fluxo de trabalho `*atdd`
- Se os critérios de aceitação estiverem completamente ausentes, pare e solicite-os
- Se a Fase 2 estiver ativa, mas os resultados da execução do teste faltarem, avise e pule a decisão da porta

---

## PHASE 1: REQUIREMENTS TRACEABILITY

This phase focuses on mapping requirements to tests, analyzing coverage, and identifying gaps.

---

### Passo 1: Carregar Contexto e Base de Conhecimento

**Acções:**

1. Carregar fragmentos de conhecimento relevantes de `{project-root}/_bmad/bmm/testarch/tea-index.csv`:
- `test-priorities-matrix.md` - P0/P1/P2/P3 quadro de risco com cálculo de prioridade automatizado, mapeamento baseado no risco, estratégia de marcação (389 linhas, 2 exemplos)
- `risk-governance.md` - Método de teste baseado em risco: 6 categorias (TECH, SEC, PERF, DADOS, BUS, OPS), pontuação automatizada, motor de decisão de porta, rastreabilidade de cobertura (625 linhas, 4 exemplos)
- `probability-impact.md` - Metodologia de pontuação de risco: probabilidade × matriz de impacto, classificação automatizada, reavaliação dinâmica, integração de portas (604 linhas, 4 exemplos)
- `test-quality.md` - Definição de Feito para testes: determinístico, isolado com limpeza, afirmações explícitas, limites comprimento/tempo (658 linhas, 5 exemplos)
- `selective-testing.md` - Duplicar padrões de cobertura: tag-based, filtros de especificações, seleção baseada em diff, regras de promoção (727 linhas, 4 exemplos)

2. Leia o arquivo da história (se fornecido):
- Critérios de aceitação do extracto
- Identificar o historial (por exemplo, 1.3)
- Observe qualquer projeto de teste existente ou informação prioritária

3. Leia artefatos relacionados BMad (se disponível):
- `test-design.md` - Avaliação de riscos e prioridades de teste
- `tech-spec.md` - Detalhes técnicos implementation
- `PRD.md` - Contexto dos requisitos do produto

**Saída:** Compreensão completa dos requisitos, prioridades e contexto existente

---

### Step 2: Discover and Catalog Tests

**Actions:**

1. Auto-discover test files related to the story:
   - Search for test IDs (e.g., `1.3-E2E-001`, `1.3-UNIT-005`)
   - Search for describe blocks mentioning feature name
   - Search for file paths matching feature directory
   - Use `glob` to find test files in `{test_dir}`

2. Categorize tests by level:
   - **E2E Tests**: Full user journeys through UI
   - **API Tests**: HTTP contract and integration tests
   - **Component Tests**: UI component behavior in isolation
   - **Unit Tests**: Business logic and pure functions

3. Extract test metadata:
   - Test ID (if present)
   - Describe/context blocks
   - It blocks (individual test cases)
   - Given-When-Then structure (if BDD)
   - Assertions used
   - Priority markers (P0/P1/P2/P3)

**Output:** Complete catalog of all tests for this feature

---

### Etapa 3: Critérios do mapa para os testes

**Acções:**

1. Para cada critério de aceitação:
- Procurar referências explícitas ( IDs de teste, descrever blocos que mencionam critério)
- Mapa para arquivos de teste específicos e bloqueia
- Use a narrativa dada quando para verificar o alinhamento
- Nível de ensaio do documento (E2E,