# Desenho do ensaio: {epic_num} - {epic_title}

**Data:** {date}
**Autor:** {user_name}
**Status:** Projecto/Aprovado

---

## Executive Summary

**Scope:** {design_level} test design for Epic {epic_num}

**Risk Summary:**

- Total risks identified: {total_risks}
- High-priority risks (≥6): {high_priority_count}
- Critical categories: {top_categories}

**Coverage Summary:**

- P0 scenarios: {p0_count} ({p0_hours} hours)
- P1 scenarios: {p1_count} ({p1_hours} hours)
- P2/P3 scenarios: {p2p3_count} ({p2p3_hours} hours)
- **Total effort**: {total_hours} hours (~{total_days} days)

---

## Avaliação de risco

Riscos de alta prioridade (Score ≥6)

| Risk ID | Category | Description   | Probability | Impact | Score | Mitigation   | Owner   | Timeline |
| ------- | -------- | ------------- | ----------- | ------ | ----- | ------------ | ------- | -------- |
| R-001   | SEC      | {description} | 2           | 3      | 6     | {mitigation} | {owner} | {date}   |
| R-002   | PERF     | {description} | 3           | 2      | 6     | {mitigation} | {owner} | {date}   |

### Riscos de média prioridade (Score 3-4)

| Risk ID | Category | Description   | Probability | Impact | Score | Mitigation   | Owner   |
| ------- | -------- | ------------- | ----------- | ------ | ----- | ------------ | ------- |
| R-003   | TECH     | {description} | 2           | 2      | 4     | {mitigation} | {owner} |
| R-004   | DATA     | {description} | 1           | 3      | 3     | {mitigation} | {owner} |

Riscos de baixa prioridade (Score 1-2)

| Risk ID | Category | Description   | Probability | Impact | Score | Action  |
| ------- | -------- | ------------- | ----------- | ------ | ----- | ------- |
| R-005   | OPS      | {description} | 1           | 2      | 2     | Monitor |
| R-006   | BUS      | {description} | 1           | 1      | 1     | Monitor |

### Legenda da categoria de risco

- **TECH**: Técnica/Arquitectura (faltas, integração, escalabilidade)
- **SEC**: Segurança (controlos de acesso, autenticação, exposição aos dados)
- **PERF**: Desempenho (violências SLA, degradação, limites de recursos)
- **DATA**: Integridade dos dados (perda, corrupção, inconsistência)
- **BUS**: Impacto empresarial (ruim UX, erros lógicos, receita)
- **OPS**: Operações (implantação, configuração, monitorização)

---

## Test Coverage Plan

### P0 (Critical) - Run on every commit

**Criteria**: Blocks core journey + High risk (≥6) + No workaround

| Requirement   | Test Level | Risk Link | Test Count | Owner | Notes   |
| ------------- | ---------- | --------- | ---------- | ----- | ------- |
| {requirement} | E2E        | R-001     | 3          | QA    | {notes} |
| {requirement} | API        | R-002     | 5          | QA    | {notes} |

**Total P0**: {p0_count} tests, {p0_hours} hours

### P1 (High) - Run on PR to main

**Criteria**: Important features + Medium risk (3-4) + Common workflows

| Requirement   | Test Level | Risk Link | Test Count | Owner | Notes   |
| ------------- | ---------- | --------- | ---------- | ----- | ------- |
| {requirement} | API        | R-003     | 4          | QA    | {notes} |
| {requirement} | Component  | -         | 6          | DEV   | {notes} |

**Total P1**: {p1_count} tests, {p1_hours} hours

### P2 (Medium) - Run nightly/weekly

**Criteria**: Secondary features + Low risk (1-2) + Edge cases

| Requirement   | Test Level | Risk Link | Test Count | Owner | Notes   |
| ------------- | ---------- | --------- | ---------- | ----- | ------- |
| {requirement} | API        | R-004     | 8          | QA    | {notes} |
| {requirement} | Unit       | -         | 15         | DEV   | {notes} |

**Total P2**: {p2_count} tests, {p2_hours} hours

### P3 (Low) - Run on-demand

**Criteria**: Nice-to-have + Exploratory + Performance benchmarks

| Requirement   | Test Level | Test Count | Owner | Notes   |
| ------------- | ---------- | ---------- | ----- | ------- |
| {requirement} | E2E        | 2          | QA    | {notes} |
| {requirement} | Unit       | 8          | DEV   | {notes} |

**Total P3**: {p3_count} tests, {p3_hours} hours

---

## Ordem de Execução

### Testes de fumo (<5 min)

**Purpose**: feedback rápido, pegar problemas de construção-quebra

- [ ] {scenario} (30s)
- [ ] {scenario} (45s)
- [ ] {scenario} (1min)

**Total**: BMADPROTECT013End scenarios

### P0 Testes (< 10 min)

**Purpose**: Validação crítica do caminho

- [ ] {scenario} (E2E)
- {scenario} (API)
- [ ] {scenario} (API)

**Total**: BMADPROTECT009End scenarios

### Testes P1 (<30 min)

**Purpose**: Cobertura importante do recurso

- {scenario} (API)
- {scenario} (Componente)

**Total**: {p1_count} scenarios

### Ensaios P2/P3 (<60 min)

**Purpose**: Cobertura de regressão completa

- {scenario} (Unit)
- {scenario} (API)

**Total**: {p2p3_count} scenarios

---

## Estimativas de recursos

### Esforço de desenvolvimento de testes

| Priority  | Count             | Hours/Test | Total Hours       | Notes                   |
| --------- | ----------------- | ---------- | ----------------- | ----------------------- |
(em milhões de ecus)