# Matriz de Rastreabilidade e Decisão do Portal - História {STORY_ID}

**História:** {STORY_TITLE}
**Data:** {DATE}
**Avaliador:** {user_name or TEA Agent}

---

## PHASE 1: REQUIREMENTS TRACEABILITY

### Coverage Summary

| Priority  | Total Criteria | FULL Coverage | Coverage % | Status       |
| --------- | -------------- | ------------- | ---------- | ------------ |
| P0        | {P0_TOTAL}     | {P0_FULL}     | {P0_PCT}%  | {P0_STATUS}  |
| P1        | {P1_TOTAL}     | {P1_FULL}     | {P1_PCT}%  | {P1_STATUS}  |
| P2        | {P2_TOTAL}     | {P2_FULL}     | {P2_PCT}%  | {P2_STATUS}  |
| P3        | {P3_TOTAL}     | {P3_FULL}     | {P3_PCT}%  | {P3_STATUS}  |
| **Total** | **{TOTAL}**    | **{FULL}**    | **{PCT}%** | **{STATUS}** |

**Legend:**

- ✅ PASS - Coverage meets quality gate threshold
- ⚠️ WARN - Coverage below threshold but not critical
- ❌ FAIL - Coverage below minimum threshold (blocker)

---

### Mapeamento detalhado

#### BMADPROTECT079End: BMADPROTECT078End (BMADPROTECT077End)

- **Coverage:** {COVERAGE_STATUS} {STATUS_ICON}
- **Experimentos:**
- `{TEST_ID}` - BMADPROTECT074End: BMADPROTECT073End
- **Dados:** {GIVEN}
- **Quando:** {WHEN}
- **Então:** {THEN}
- `{TEST_ID_2}` - {TEST_FILE_2}: {LINE}
- **Dados:** {GIVEN_2}
- **Quando:** {WHEN_2}
- **Então:** {THEN_2}

- **Gaps:** (se PARCIAL ou UNIT-ONly ou INTEGRAÇÃO-ONly)
BMADPROTECT094end BMADPROTECT064end
BMADPROTECT093end BMADPROTECT063end

- **Recomendação:** {RECOMMENDATION_TEXT}

---

#### Example: AC-1: User can login with email and password (P0)

- **Coverage:** FULL ✅
- **Tests:**
  - `1.3-E2E-001` - tests/e2e/auth.spec.ts:12
    - **Given:** User has valid credentials
    - **When:** User submits login form
    - **Then:** User is redirected to dashboard
  - `1.3-UNIT-001` - tests/unit/auth-service.spec.ts:8
    - **Given:** Valid email and password hash
    - **When:** validateCredentials is called
    - **Then:** Returns user object

---

#### Exemplo: AC-3: O usuário pode redefinir senha via e-mail (P1)

- **Cobertura:** PARCIAL ⚠
- **Experimentos:**
- `1.3-E2E-003` - testes/e2e/auth.spec.ts:44
- **Dado:** Repor a senha do utilizador
- **Quando:** O utilizador clica em redefinir o link no e-mail
- **Então:** O usuário pode definir nova senha

- **Gaps:**
  - Missing: Validação da entrega por e- mail
  - Missing: Tratamento de token expirado (caminho de erro)
  - Missing: Tratamento inválido de fichas (teste de segurança)
  - Missing: Teste unitário para lógica de geração de fichas

- **Recomendação:** Adicione `1.3-API-001` para testes de integração de serviços de e-mail e `1.3-UNIT-003` para lógica de geração de fichas. Adicionar `1.3-E2E-004` para validação do caminho de erro (tokens expirados/inválidos).

---

### Gap Analysis

#### Critical Gaps (BLOCKER) ❌

{CRITICAL_GAP_COUNT} gaps found. **Do not release until resolved.**

1. **{CRITERION_ID}: {CRITERION_DESCRIPTION}** (P0)
   - Current Coverage: {COVERAGE_STATUS}
   - Missing Tests: {MISSING_TEST_DESCRIPTION}
   - Recommend: {RECOMMENDED_TEST_ID} ({RECOMMENDED_TEST_LEVEL})
   - Impact: {IMPACT_DESCRIPTION}

---

#### Aberturas de alta prioridade (PR BLOCKER) ⚠

BMADPROTECT061End gaps encontrados. **Endereço antes da fusão PR.**

1. **{CRITERION_ID}: {CRITERION_DESCRIPTION}** (P1)
- Cobertura atual: {COVERAGE_STATUS}
- Testes em falta: {MISSING_TEST_DESCRIPTION}
BMADPROTECT088end BMADPROTECT056end (BMADPROTECT055end)
   - Impact: {IMPACT_DESCRIPTION}

---

#### Medium Priority Gaps (Nightly) ⚠️

{MEDIUM_GAP_COUNT} gaps found. **Address in nightly test improvements.**

1. **{CRITERION_ID}: {CRITERION_DESCRIPTION}** (P2)
   - Current Coverage: {COVERAGE_STATUS}
   - Recommend: {RECOMMENDED_TEST_ID} ({RECOMMENDED_TEST_LEVEL})

---

#### Intervalos de baixa prioridade (Opcional)

BMADPROTECT053End gaps encontrados. **Opcional - adicionar se o tempo permitir.**

1. **{CRITERION_ID}: {CRITERION_DESCRIPTION}** (P3)
- Cobertura atual: {COVERAGE_STATUS}

---

### Quality Assessment

#### Tests with Issues

**BLOCKER Issues** ❌

- `{TEST_ID}` - {ISSUE_DESCRIPTION} - {REMEDIATION}

**WARNING Issues** ⚠️

- `{TEST_ID}` - {ISSUE_DESCRIPTION} - {REMEDIATION}

**INFO Issues** ℹ️

- `{TEST_ID}` - {ISSUE_DESCRIPTION} - {REMEDIATION}

---

#### Problemas de qualidade de exemplo

**Questões de alerta** ⚠

- `1.3-E2E-001` - 145 segundos (alvo superior aos 90s) - Otimize a configuração do dispositivo para reduzir a duração do teste
- `1.3-UNIT-005` - 320 linhas (limite de 300 linhas) - Dividir em vários arquivos de teste focados

**Questões de INFO**

- `1.3-E2E-002` - Estrutura em falta dada-quando-então - Refactor descrever bloco para usar o formato BDD

---

#### Tests Passing Quality Gates

**{PASSING_TEST_COUNT}/{TOTAL_TEST_COUNT} tests ({PASSING_PCT}%) meet all quality criteria** ✅

---

### Análise da Cobertura Duplicada

#### Sobreposição aceitável (Defesa em Profundidade)

- {CRITERION_ID}: Teste na unidade (lógica de negócio) e E2E (viagem ao utilizador) ✅

#### Duplicação Inaceitável ⚠

- {CRITERION_ID}: A mesma validação no nível E2E e Componente
  - Recommendation: Remover {TEST_ID} ou consolidar com {OTHER_TEST_ID}

---

### Cobertura por nível de ensaio

* Nível de teste * Testes * Critérios cobertos * Capa