# Avaliação NFR - {FEATURE_NAME}

**Data:** {DATE}
**História:** {STORY_ID} (se aplicável)
**Status Geral:** {OVERALL_STATUS} {STATUS_ICON}

---

## Resumo Executivo

**Avaliação:** {PASS_COUNT} PASSOU, {CONCERNS_COUNT} PREOCUPAÇÕES, {FAIL_COUNT} FALHOU

**Bloqueios:** {BLOCKER_COUNT} {BLOCKER_DESCRIPTION}

**Problemas de Alta Prioridade:** {HIGH_PRIORITY_COUNT} {HIGH_PRIORITY_DESCRIPTION}

**Recomendação:** {OVERALL_RECOMMENDATION}

---

## Avaliação de Desempenho

### Tempo de Resposta (p95)

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE}
- **Real:** {ACTUAL_VALUE}
- **Evidência:** {EVIDENCE_SOURCE}
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Vazão (Throughput)

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE}
- **Real:** {ACTUAL_VALUE}
- **Evidência:** {EVIDENCE_SOURCE}
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Uso de Recursos

- **Uso de CPU**
  - **Status:** {STATUS} {STATUS_ICON}
  - **Limiar:** {THRESHOLD_VALUE}
  - **Real:** {ACTUAL_VALUE}
  - **Evidência:** {EVIDENCE_SOURCE}

- **Uso de Memória**
  - **Status:** {STATUS} {STATUS_ICON}
  - **Limiar:** {THRESHOLD_VALUE}
  - **Real:** {ACTUAL_VALUE}
  - **Evidência:** {EVIDENCE_SOURCE}

### Escalabilidade

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_DESCRIPTION}
- **Real:** {ACTUAL_DESCRIPTION}
- **Evidência:** {EVIDENCE_SOURCE}
- **Descobertas:** {FINDINGS_DESCRIPTION}

---

## Avaliação de Segurança

### Força de Autenticação

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_DESCRIPTION}
- **Real:** {ACTUAL_DESCRIPTION}
- **Evidência:** {EVIDENCE_SOURCE}
- **Descobertas:** {FINDINGS_DESCRIPTION}
- **Recomendação:** {RECOMMENDATION} (se PREOCUPAÇÕES ou FALHOU)

### Controles de Autorização

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_DESCRIPTION}
- **Real:** {ACTUAL_DESCRIPTION}
- **Evidência:** {EVIDENCE_SOURCE}
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Proteção de Dados

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_DESCRIPTION}
- **Real:** {ACTUAL_DESCRIPTION}
- **Evidência:** {EVIDENCE_SOURCE}
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Gerenciamento de Vulnerabilidade

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_DESCRIPTION} (e.g., "0 críticas, <3 vulnerabilidades altas")
- **Real:** {ACTUAL_DESCRIPTION} (e.g., "0 críticas, 1 alta, 5 médias vulnerabilidades")
- **Evidência:** {EVIDENCE_SOURCE} (e.g., "Resultados varredura Snyk - scan-2025-10-14.json")
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Conformidade (se aplicável)

- **Status:** {STATUS} {STATUS_ICON}
- **Padrões:** {COMPLIANCE_STANDARDS} (e.g., "GDPR, HIPAA, PCI-DSS")
- **Real:** {ACTUAL_COMPLIANCE_STATUS}
- **Evidência:** {EVIDENCE_SOURCE}
- **Descobertas:** {FINDINGS_DESCRIPTION}

---

## Avaliação de Confiabilidade

### Disponibilidade (Uptime)

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE} (e.g., "99.9%")
- **Real:** {ACTUAL_VALUE} (e.g., "99.95%")
- **Evidência:** {EVIDENCE_SOURCE} (e.g., "Monitoramento uptime - uptime-report-2025-10-14.csv")
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Taxa de Erro

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE} (e.g., "<0.1%")
- **Real:** {ACTUAL_VALUE} (e.g., "0.05%")
- **Evidência:** {EVIDENCE_SOURCE} (e.g., "Logs de erro - logs/errors-2025-10.log")
- **Descobertas:** {FINDINGS_DESCRIPTION}

### MTTR (Tempo Médio Para Recuperação)

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE} (e.g., "<15 minutos")
- **Real:** {ACTUAL_VALUE} (e.g., "12 minutos")
- **Evidência:** {EVIDENCE_SOURCE} (e.g., "Relatórios de incidente - incidents/")
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Tolerância a Falhas

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_DESCRIPTION}
- **Real:** {ACTUAL_DESCRIPTION}
- **Evidência:** {EVIDENCE_SOURCE}
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Burn-In CI (Estabilidade)

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE} (e.g., "100 execuções bem-sucedidas consecutivas")
- **Real:** {ACTUAL_VALUE} (e.g., "150 execuções bem-sucedidas consecutivas")
- **Evidência:** {EVIDENCE_SOURCE} (e.g., "Resultados burn-in CI - ci-burn-in-2025-10-14.log")
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Recuperação de Desastre (se aplicável)

- **RTO (Objetivo de Tempo de Recuperação)**
  - **Status:** {STATUS} {STATUS_ICON}
  - **Limiar:** {THRESHOLD_VALUE}
  - **Real:** {ACTUAL_VALUE}
  - **Evidência:** {EVIDENCE_SOURCE}

- **RPO (Objetivo de Ponto de Recuperação)**
  - **Status:** {STATUS} {STATUS_ICON}
  - **Limiar:** {THRESHOLD_VALUE}
  - **Real:** {ACTUAL_VALUE}
  - **Evidência:** {EVIDENCE_SOURCE}

---

## Avaliação de Manutenibilidade

### Cobertura de Teste

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE} (e.g., ">=80%")
- **Real:** {ACTUAL_VALUE} (e.g., "87%")
- **Evidência:** {EVIDENCE_SOURCE} (e.g., "Relatório de cobertura - coverage/lcov-report/index.html")
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Qualidade de Código

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE} (e.g., ">=85/100")
- **Real:** {ACTUAL_VALUE} (e.g., "92/100")
- **Evidência:** {EVIDENCE_SOURCE} (e.g., "Análise SonarQube - sonarqube-report-2025-10-14.pdf")
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Dívida Técnica

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE} (e.g., "<5% razão de dívida")
- **Real:** {ACTUAL_VALUE} (e.g., "3.2% razão de dívida")
- **Evidência:** {EVIDENCE_SOURCE} (e.g., "Análise CodeClimate - codeclimate-2025-10-14.json")
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Completude da Documentação

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE} (e.g., ">=90%")
- **Real:** {ACTUAL_VALUE} (e.g., "95%")
- **Evidência:** {EVIDENCE_SOURCE} (e.g., "Auditoria de documentação - docs-audit-2025-10-14.md")
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Qualidade de Teste (de test-review, se disponível)

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_DESCRIPTION}
- **Real:** {ACTUAL_DESCRIPTION}
- **Evidência:** {EVIDENCE_SOURCE} (e.g., "Relatório de revisão de teste - test-review-2025-10-14.md")
- **Descobertas:** {FINDINGS_DESCRIPTION}

---

## Avaliações NFR Personalizadas (se aplicável)

### {CUSTOM_NFR_NAME_1}

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_DESCRIPTION}
- **Real:** {ACTUAL_DESCRIPTION}
- **Evidência:** {EVIDENCE_SOURCE}
- **Descobertas:** {FINDINGS_DESCRIPTION}

### {CUSTOM_NFR_NAME_2}

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_DESCRIPTION}
- **Real:** {ACTUAL_DESCRIPTION}
- **Evidência:** {EVIDENCE_SOURCE}
- **Descobertas:** {FINDINGS_DESCRIPTION}

---

## Vitórias Rápidas

{QUICK_WIN_COUNT} vitórias rápidas identificadas para implementação imediata:

1. **{QUICK_WIN_TITLE_1}** ({NFR_CATEGORY}) - {PRIORITY} - {ESTIMATED_EFFORT}
   - {QUICK_WIN_DESCRIPTION}
   - Nenhuma mudança de código necessária / Mudanças mínimas de código

2. **{QUICK_WIN_TITLE_2}** ({NFR_CATEGORY}) - {PRIORITY} - {ESTIMATED_EFFORT}
   - {QUICK_WIN_DESCRIPTION}

---

## Ações Recomendadas

### Imediato (Antes do Lançamento) - Prioridade CRÍTICA/ALTA

1. **{ACTION_TITLE_1}** - {PRIORITY} - {ESTIMATED_EFFORT} - {OWNER}
   - {ACTION_DESCRIPTION}
   - {SPECIFIC_STEPS}
   - {VALIDATION_CRITERIA}

2. **{ACTION_TITLE_2}** - {PRIORITY} - {ESTIMATED_EFFORT} - {OWNER}
   - {ACTION_DESCRIPTION}
   - {SPECIFIC_STEPS}
   - {VALIDATION_CRITERIA}

### Curto Prazo (Próximo Sprint) - Prioridade MÉDIA

1. **{ACTION_TITLE_3}** - {PRIORITY} - {ESTIMATED_EFFORT} - {OWNER}
   - {ACTION_DESCRIPTION}

2. **{ACTION_TITLE_4}** - {PRIORITY} - {ESTIMATED_EFFORT} - {OWNER}
   - {ACTION_DESCRIPTION}

### Longo Prazo (Backlog) - Prioridade BAIXA

1. **{ACTION_TITLE_5}** - {PRIORITY} - {ESTIMATED_EFFORT} - {OWNER}
   - {ACTION_DESCRIPTION}

---

## Ganchos de Monitoramento

{MONITORING_HOOK_COUNT} ganchos de monitoramento recomendados para detectar problemas antes de falhas:

### Monitoramento de Desempenho

- [ ] {MONITORING_TOOL_1} - {MONITORING_DESCRIPTION}
  - **Dono:** {OWNER}
  - **Prazo:** {DEADLINE}

- [ ] {MONITORING_TOOL_2} - {MONITORING_DESCRIPTION}
  - **Dono:** {OWNER}
  - **Prazo:** {DEADLINE}

### Monitoramento de Segurança

- [ ] {MONITORING_TOOL_3} - {MONITORING_DESCRIPTION}
  - **Dono:** {OWNER}
  - **Prazo:** {DEADLINE}

### Monitoramento de Confiabilidade

- [ ] {MONITORING_TOOL_4} - {MONITORING_DESCRIPTION}
  - **Dono:** {OWNER}
  - **Prazo:** {DEADLINE}

### Limiares de Alerta

- [ ] {ALERT_DESCRIPTION} - Notificar quando {THRESHOLD_CONDITION}
  - **Dono:** {OWNER}
  - **Prazo:** {DEADLINE}

---

## Mecanismos Fail-Fast

{FAIL_FAST_COUNT} mecanismos fail-fast recomendados para prevenir falhas:

### Circuit Breakers (Confiabilidade)

- [ ] {CIRCUIT_BREAKER_DESCRIPTION}
  - **Dono:** {OWNER}
  - **Esforço Estimado:** {EFFORT}

### Limitação de Taxa (Desempenho)

- [ ] {RATE_LIMITING_DESCRIPTION}
  - **Dono:** {OWNER}
  - **Esforço Estimado:** {EFFORT}

### Portões de Validação (Segurança)

- [ ] {VALIDATION_GATE_DESCRIPTION}
  - **Dono:** {OWNER}
  - **Esforço Estimado:** {EFFORT}

### Testes de Fumaça (Manutenibilidade)

- [ ] {SMOKE_TEST_DESCRIPTION}
  - **Dono:** {OWNER}
  - **Esforço Estimado:** {EFFORT}

---

## Lacunas de Evidência

{EVIDENCE_GAP_COUNT} lacunas de evidência identificadas - ação necessária:

- [ ] **{NFR_NAME_1}** ({NFR_CATEGORY})
  - **Dono:** {OWNER}
  - **Prazo:** {DEADLINE}
  - **Evidência Sugerida:** {SUGGESTED_EVIDENCE_SOURCE}
  - **Impacto:** {IMPACT_DESCRIPTION}

- [ ] **{NFR_NAME_2}** ({NFR_CATEGORY})
  - **Dono:** {OWNER}
  - **Prazo:** {DEADLINE}
  - **Evidência Sugerida:** {SUGGESTED_EVIDENCE_SOURCE}
  - **Impacto:** {IMPACT_DESCRIPTION}

---

## Resumo de Descobertas

| Categoria       | PASSOU           | PREOCUPAÇÕES         | FALHOU           | Status Geral                        |
| --------------- | ---------------- | -------------------- | ---------------- | ----------------------------------- |
| Desempenho      | {P_PASS_COUNT}   | {P_CONCERNS_COUNT}   | {P_FAIL_COUNT}   | {P_STATUS} {P_ICON}                 |
| Segurança       | {S_PASS_COUNT}   | {S_CONCERNS_COUNT}   | {S_FAIL_COUNT}   | {S_STATUS} {S_ICON}                 |
| Confiabilidade  | {R_PASS_COUNT}   | {R_CONCERNS_COUNT}   | {R_FAIL_COUNT}   | {R_STATUS} {R_ICON}                 |
| Manutenibilidade| {M_PASS_COUNT}   | {M_CONCERNS_COUNT}   | {M_FAIL_COUNT}   | {M_STATUS} {M_ICON}                 |
| **Total**       | **{TOTAL_PASS}** | **{TOTAL_CONCERNS}** | **{TOTAL_FAIL}** | **{OVERALL_STATUS} {OVERALL_ICON}** |

---

## Trecho YAML de Portão

```yaml
nfr_assessment:
  date: '{DATE}'
  story_id: '{STORY_ID}'
  feature_name: '{FEATURE_NAME}'
  categories:
    performance: '{PERFORMANCE_STATUS}'
    security: '{SECURITY_STATUS}'
    reliability: '{RELIABILITY_STATUS}'
    maintainability: '{MAINTAINABILITY_STATUS}'
  overall_status: '{OVERALL_STATUS}'
  critical_issues: { CRITICAL_COUNT }
  high_priority_issues: { HIGH_COUNT }
  medium_priority_issues: { MEDIUM_COUNT }
  concerns: { CONCERNS_COUNT }
  blockers: { BLOCKER_BOOLEAN } # true/false
  quick_wins: { QUICK_WIN_COUNT }
  evidence_gaps: { EVIDENCE_GAP_COUNT }
  recommendations:
    - '{RECOMMENDATION_1}'
    - '{RECOMMENDATION_2}'
    - '{RECOMMENDATION_3}'
```

---

## Artefatos Relacionados

- **Arquivo de História:** {STORY_FILE_PATH} (se aplicável)
- **Especificação Técnica:** {TECH_SPEC_PATH} (se disponível)
- **PRD:** {PRD_PATH} (se disponível)
- **Design de Teste:** {TEST_DESIGN_PATH} (se disponível)
- **Fontes de Evidência:**
  - Resultados de Teste: {TEST_RESULTS_DIR}
  - Métricas: {METRICS_DIR}
  - Logs: {LOGS_DIR}
  - Resultados CI: {CI_RESULTS_PATH}

---

## Resumo de Recomendações

**Bloqueador de Lançamento:** {RELEASE_BLOCKER_SUMMARY}

**Alta Prioridade:** {HIGH_PRIORITY_SUMMARY}

**Média Prioridade:** {MEDIUM_PRIORITY_SUMMARY}

**Próximos Passos:** {NEXT_STEPS_DESCRIPTION}

---

## Aprovação

**Avaliação NFR:**

- Status Geral: {OVERALL_STATUS} {OVERALL_ICON}
- Problemas Críticos: {CRITICAL_COUNT}
- Problemas de Alta Prioridade: {HIGH_COUNT}
- Preocupações: {CONCERNS_COUNT}
- Lacunas de Evidência: {EVIDENCE_GAP_COUNT}

**Status do Portão:** {GATE_STATUS} {GATE_ICON}

**Próximas Ações:**

- Se PASSOU ✅: Prosseguir para fluxo de trabalho `*gate` ou lançamento
- Se PREOCUPAÇÕES ⚠️: Abordar problemas ALTA/CRÍTICA, reexecutar `*nfr-assess`
- Se FALHOU ❌: Resolver NFRs com status FALHOU, reexecutar `*nfr-assess`

**Gerado:** {DATE}
**Fluxo de Trabalho:** testarch-nfr v4.0

---

<!-- Alimentado por BMAD-CORE™ -->
