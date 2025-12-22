# Requisitos Rastreabilidade e decisão da porta - Lista de verificação de validação

**Fluxo de trabalho:** `testarch-trace`
**Proporção:** Assegurar uma matriz de rastreabilidade completa com análise de lacunas acionáveis e tomar uma decisão de disponibilidade para a implantação (PASS/CONCERNS/FAIL/WAIVED)

Esta lista abrange **duas fases sequenciais**:

- **FASE 1**: Requisitos de rastreabilidade (sempre executado)
- **FASE 2**: Decisão relativa à porta de qualidade (executada se `enable_gate_decision: true`)

---

# PHASE 1: REQUIREMENTS TRACEABILITY

## Prerequisites Validation

- [ ] Acceptance criteria are available (from story file OR inline)
- [ ] Test suite exists (or gaps are acknowledged and documented)
- [ ] Test directory path is correct (`test_dir` variable)
- [ ] Story file is accessible (if using BMad mode)
- [ ] Knowledge base is loaded (test-priorities, traceability, risk-governance)

---

## Carregando Contexto

- [ ] Arquivo de história lido com sucesso (se aplicável)
- [ ] Critérios de aceitação extraídos correctamente
- ID da história identificada (por exemplo, 1.3)
- [ ] `test-design.md` carregado (se disponível)
- [ ] `tech-spec.md` carregado (se disponível)
- [ ] `PRD.md` carregado (se disponível)
- [ ] Fragmentos de conhecimento relevantes carregados da `tea-index.csv`

---

## Test Discovery and Cataloging

- [ ] Tests auto-discovered using multiple strategies (test IDs, describe blocks, file paths)
- [ ] Tests categorized by level (E2E, API, Component, Unit)
- [ ] Test metadata extracted:
  - [ ] Test IDs (e.g., 1.3-E2E-001)
  - [ ] Describe/context blocks
  - [ ] It blocks (individual test cases)
  - [ ] Given-When-Then structure (if BDD)
  - [ ] Priority markers (P0/P1/P2/P3)
- [ ] All relevant test files found (no tests missed due to naming conventions)

---

## Mapeamento de critérios a testes

- [ ] Cada critério de aceitação mapeado para testes (ou marcado como NENHUMA)
- [ ] Referências explícitas encontradas ( IDs de teste, descrever blocos que mencionam critério)
- [ ] Nível de teste documentado (E2E, API, Componente, Unidade)
- [ ] dado-quando-então narrativa verificada para alinhamento
- [ ] tabela de matriz de rastreabilidade gerada:
- ID do critério
- [ ] Descrição
- [ ] ID do teste
- [ ] Testar o Ficheiro
- [ ] Nível de ensaio
- Status da cobertura

---

## Coverage Classification

- [ ] Coverage status classified for each criterion:
  - [ ] **FULL** - All scenarios validated at appropriate level(s)
  - [ ] **PARTIAL** - Some coverage but missing edge cases or levels
  - [ ] **NONE** - No test coverage at any level
  - [ ] **UNIT-ONLY** - Only unit tests (missing integration/E2E validation)
  - [ ] **INTEGRATION-ONLY** - Only API/Component tests (missing unit confidence)
- [ ] Classification justifications provided
- [ ] Edge cases considered in FULL vs PARTIAL determination

---

## Detecção de Cobertura Duplicada

- [ ] Cobertura duplicada verificada entre os níveis de teste
- [ ] Sobreposição aceitável identificada (defesa em profundidade para caminhos críticos)
- [ ] Duplicação inaceitável assinalada (a mesma validação em múltiplos níveis)
- [ ] Recomendações para a consolidação
- [ ] Princípios de ensaio seletivos aplicados

---

## Gap Analysis

- [ ] Coverage gaps identified:
  - [ ] Criteria with NONE status
  - [ ] Criteria with PARTIAL status
  - [ ] Criteria with UNIT-ONLY status
  - [ ] Criteria with INTEGRATION-ONLY status
- [ ] Gaps prioritized by risk level using test-priorities framework:
  - [ ] **CRITICAL** - P0 criteria without FULL coverage (BLOCKER)
  - [ ] **HIGH** - P1 criteria without FULL coverage (PR blocker)
  - [ ] **MEDIUM** - P2 criteria without FULL coverage (nightly gap)
  - [ ] **LOW** - P3 criteria without FULL coverage (acceptable)
- [ ] Specific test recommendations provided for each gap:
  - [ ] Suggested test level (E2E, API, Component, Unit)
  - [ ] Test description (Given-When-Then)
  - [ ] Recommended test ID (e.g., 1.3-E2E-004)
  - [ ] Explanation of why test is needed

---

## Metrica de cobertura

- [ ] Percentagem global de cobertura calculada (cobertura completa / critérios totais)
- [ ] Percentagem de cobertura P0 calculada
- [ ] Percentagem de cobertura P1 calculada
- [ ] Percentagem de cobertura P2 calculada (se aplicável)
- [ ] Cobertura por nível calculado:
- [ ] Cobertura E2E %
- [ ] Cobertura API %
- [ ] Cobertura do componente %
- [ ] Cobertura da unidade %

---

## Verificação da qualidade do ensaio

Para cada teste mapeado, verificar:

- [ ] Asserções explícitas estão presentes (não escondidas em ajudantes)
- [ ] O teste segue a estrutura Given-When-Then
- [ ] Sem esperas duras ou sonos (só espera determinística)
Auto-limpeza (o teste limpa os seus dados)
- [ ] Tamanho do arquivo < 300 linhas
- [ ] Duração do ensaio < 90 segundos

Questões de qualidade assinaladas:

- [ ] Questões **BLOCKER** identificadas (afirmações em falta, esperas difíceis, padrões de flaky)
- [ ] Questões identificadas de **ARRANQUE** (grandes ficheiros, testes lentos, estrutura pouco clara)
- [ ] Questões **INFO** identificadas (inconsistências de estilo, documentação em falta)

Fragmentos de conhecimento referenciados:

- [ ] `test-quality.md` para a definição de feito
- [ ] `fixture-architecture.md` para padrões de autolimpeza
- [ ] `network-first.md` para as melhores práticas dos dramaturgos
- [ ] `data-fa