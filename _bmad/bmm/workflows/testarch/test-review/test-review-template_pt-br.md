# Revisão da qualidade do ensaio: {test_filename}

**Score de qualidade**: {score}/100 ({grade} - {assessment})
**Data de revisão**: {YYYY-MM-DD}
**ÂMBITO DE REVISÃO**: {single | directory | suite}
**Revisor**: {user_name or TEA Agent}

---

## Executive Summary

**Overall Assessment**: {Excellent | Good | Acceptable | Needs Improvement | Critical Issues}

**Recommendation**: {Approve | Approve with Comments | Request Changes | Block}

### Key Strengths

✅ {strength_1}
✅ {strength_2}
✅ {strength_3}

### Key Weaknesses

❌ {weakness_1}
❌ {weakness_2}
❌ {weakness_3}

### Summary

{1-2 paragraph summary of overall test quality, highlighting major findings and recommendation rationale}

---

## Avaliação dos critérios de qualidade

| Criterion                            | Status                          | Violations | Notes        |
| ------------------------------------ | ------------------------------- | ---------- | ------------ |
| BDD Format (Given-When-Then)         | {✅ PASS \| ⚠️ WARN \| ❌ FAIL} | {count}    | {brief_note} |
| Test IDs                             | {✅ PASS \| ⚠️ WARN \| ❌ FAIL} | {count}    | {brief_note} |
| Priority Markers (P0/P1/P2/P3)       | {✅ PASS \| ⚠️ WARN \| ❌ FAIL} | {count}    | {brief_note} |
| Hard Waits (sleep, waitForTimeout)   | {✅ PASS \| ⚠️ WARN \| ❌ FAIL} | {count}    | {brief_note} |
| Determinism (no conditionals)        | {✅ PASS \| ⚠️ WARN \| ❌ FAIL} | {count}    | {brief_note} |
| Isolation (cleanup, no shared state) | {✅ PASS \| ⚠️ WARN \| ❌ FAIL} | {count}    | {brief_note} |
| Fixture Patterns                     | {✅ PASS \| ⚠️ WARN \| ❌ FAIL} | {count}    | {brief_note} |
| Data Factories                       | {✅ PASS \| ⚠️ WARN \| ❌ FAIL} | {count}    | {brief_note} |
| Network-First Pattern                | {✅ PASS \| ⚠️ WARN \| ❌ FAIL} | {count}    | {brief_note} |
| Explicit Assertions                  | {✅ PASS \| ⚠️ WARN \| ❌ FAIL} | {count}    | {brief_note} |
| Test Length (≤300 lines)             | {✅ PASS \| ⚠️ WARN \| ❌ FAIL} | {lines}    | {brief_note} |
| Test Duration (≤1.5 min)             | {✅ PASS \| ⚠️ WARN \| ❌ FAIL} | {duration} | {brief_note} |
| Flakiness Patterns                   | {✅ PASS \| ⚠️ WARN \| ❌ FAIL} | {count}    | {brief_note} |

**Total Violations**: BMADPROTECT029End Critical, BMADPROTECT028End Alta, BMADPROTECT027End Médio, BMADPROTECT026End Baixo

---

## Quality Score Breakdown

```
Starting Score:          100
Critical Violations:     -{critical_count} × 10 = -{critical_deduction}
High Violations:         -{high_count} × 5 = -{high_deduction}
Medium Violations:       -{medium_count} × 2 = -{medium_deduction}
Low Violations:          -{low_count} × 1 = -{low_deduction}

Bonus Points:
  Excellent BDD:         +{0|5}
  Comprehensive Fixtures: +{0|5}
  Data Factories:        +{0|5}
  Network-First:         +{0|5}
  Perfect Isolation:     +{0|5}
  All Test IDs:          +{0|5}
                         --------
Total Bonus:             +{bonus_total}

Final Score:             {final_score}/100
Grade:                   {grade}

```

---

## Questões críticas (deve ser corrigido)

{If no critical issues: "No critical issues detected. ✅"}

{For each critical issue:}

### BMADPROTECT023end. {Issue Title}

**Severidade**: P0 (Crítico)
**Localização**: `{filename}:{line_number}`
**Critério**: {criterion_name}
**Base de Conhecimento**: [{fragment_name}BADPROTECT010END

**Descrição da emissão**:
{Detailed explanation of what the problem is and why it's critical}

**Código actual**:

```typescript
// ❌ Bad (current implementation)
{
  code_snippet_showing_problem;
}

```

**Recomendação de fixação**:

```typescript
// ✅ Good (recommended approach)
{
  code_snippet_showing_solution;
}

```

**Por que isso importa**:
{Explanation of impact - flakiness risk, maintainability, reliability}

**Violações relacionadas**:
{If similar issue appears elsewhere, note line numbers}

---

## Recommendations (Should Fix)

{If no recommendations: "No additional recommendations. Test quality is excellent. ✅"}

{For each recommendation:}

### {rec_number}. {Recommendation Title}

**Severity**: {P1 (High) | P2 (Medium) | P3 (Low)}
**Location**: `{filename}:{line_number}`
**Criterion**: {criterion_name}
**Knowledge Base**: [{fragment_name}]({fragment_path})

**Issue Description**:
{Detailed explanation of what could be improved and why}

**Current Code**:

```typescript
// ⚠️ Could be improved (current implementation)
{
  code_snippet_showing_current_approach;
}

```

**Recommended Improvement**:

```typescript
// ✅ Better approach (recommended)
{
  code_snippet_showing_improvement;
}

```

**Benefits**:
{Explanation of benefits - maintainability, readability, reusability}

**Priority**:
{Why this is P1/P2/P3 - urgency and impact}

---

## Melhores práticas encontradas

{If good patterns found, highlight them}

{For each best practice:}

### BMADPROTECT014End. {Best Practice Title}

**Localização**: `{filename}:{line_number}`
**Pattern**: {pattern_name}
**Base de Conhecimento**: [{fragment_name}BADPROTECT009END

**Por que isso é bom**:
{Explicação do motivo