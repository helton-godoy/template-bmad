# Avaliação NFR - {FEATURE_NAME}

**Data:** {DATE}
**História:** {STORY_ID} (se aplicável)
**Estado geral:** {OVERALL_STATUS} {STATUS_ICON}

---

## Executive Summary

**Assessment:** {PASS_COUNT} PASS, {CONCERNS_COUNT} CONCERNS, {FAIL_COUNT} FAIL

**Blockers:** {BLOCKER_COUNT} {BLOCKER_DESCRIPTION}

**High Priority Issues:** {HIGH_PRIORITY_COUNT} {HIGH_PRIORITY_DESCRIPTION}

**Recommendation:** {OVERALL_RECOMMENDATION}

---

## Avaliação do desempenho

### Tempo de resposta (p95)

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE}
- **Atual:** {ACTUAL_VALUE}
- **Evidência:** {EVIDENCE_SOURCE}
- **Encontros:** {FINDINGS_DESCRIPTION}

### Produção

- **Status:** BMADPROTECT079End BMADPROTECT078End
- **Limiar:** {THRESHOLD_VALUE}
- **Atual:** {ACTUAL_VALUE}
- **Evidência:** {EVIDENCE_SOURCE}
- **Encontros:** {FINDINGS_DESCRIPTION}

### Utilização dos Recursos

- **Uso PCU**
- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE}
- **Atual:** {ACTUAL_VALUE}
- **Evidência:** {EVIDENCE_SOURCE}

- **Uso da memória**
- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE}
- **Atual:** {ACTUAL_VALUE}
- **Evidência:** {EVIDENCE_SOURCE}

### Escalabilidade

- **Status:** BMADPROTECT063end BMADPROTECT062end
- **Limiar:** {THRESHOLD_DESCRIPTION}
- **Atual:** {ACTUAL_DESCRIPTION}
- **Evidência:** {EVIDENCE_SOURCE}
- **Encontros:** {FINDINGS_DESCRIPTION}

---

## Security Assessment

### Authentication Strength

- **Status:** {STATUS} {STATUS_ICON}
- **Threshold:** {THRESHOLD_DESCRIPTION}
- **Actual:** {ACTUAL_DESCRIPTION}
- **Evidence:** {EVIDENCE_SOURCE}
- **Findings:** {FINDINGS_DESCRIPTION}
- **Recommendation:** {RECOMMENDATION} (if CONCERNS or FAIL)

### Authorization Controls

- **Status:** {STATUS} {STATUS_ICON}
- **Threshold:** {THRESHOLD_DESCRIPTION}
- **Actual:** {ACTUAL_DESCRIPTION}
- **Evidence:** {EVIDENCE_SOURCE}
- **Findings:** {FINDINGS_DESCRIPTION}

### Data Protection

- **Status:** {STATUS} {STATUS_ICON}
- **Threshold:** {THRESHOLD_DESCRIPTION}
- **Actual:** {ACTUAL_DESCRIPTION}
- **Evidence:** {EVIDENCE_SOURCE}
- **Findings:** {FINDINGS_DESCRIPTION}

### Vulnerability Management

- **Status:** {STATUS} {STATUS_ICON}
- **Threshold:** {THRESHOLD_DESCRIPTION} (e.g., "0 critical, <3 high vulnerabilities")
- **Actual:** {ACTUAL_DESCRIPTION} (e.g., "0 critical, 1 high, 5 medium vulnerabilities")
- **Evidence:** {EVIDENCE_SOURCE} (e.g., "Snyk scan results - scan-2025-10-14.json")
- **Findings:** {FINDINGS_DESCRIPTION}

### Compliance (if applicable)

- **Status:** {STATUS} {STATUS_ICON}
- **Standards:** {COMPLIANCE_STANDARDS} (e.g., "GDPR, HIPAA, PCI-DSS")
- **Actual:** {ACTUAL_COMPLIANCE_STATUS}
- **Evidence:** {EVIDENCE_SOURCE}
- **Findings:** {FINDINGS_DESCRIPTION}

---

## Avaliação da fiabilidade

### Disponibilidade (hora de espera)

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE} (por exemplo, "99,9%")
- **Atual:** {ACTUAL_VALUE} (por exemplo, "99,95%")
- **Evidência:** {EVIDENCE_SOURCE} (por exemplo, "Monitorização do tempo de trabalho - relatório-2025-10-14.csv")
- **Encontros:** {FINDINGS_DESCRIPTION}

### Taxa de Erro

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE} (por exemplo, "<0.1%")
- **Actual:** {ACTUAL_VALUE} (e.g., "0.05%")
- **Evidence:** {EVIDENCE_SOURCE} (e.g., "Error logs - logs/errors-2025-10.log")
- **Findings:** {FINDINGS_DESCRIPTION}

### MTTR (Mean Time To Recovery)

- **Status:** {STATUS} {STATUS_ICON}
- **Threshold:** {THRESHOLD_VALUE} (e.g., "<15 minutes")
- **Actual:** {ACTUAL_VALUE} (e.g., "12 minutes")
- **Evidence:** {EVIDENCE_SOURCE} (e.g., "Incident reports - incidents/")
- **Findings:** {FINDINGS_DESCRIPTION}

### Fault Tolerance

- **Status:** {STATUS} {STATUS_ICON}
- **Threshold:** {THRESHOLD_DESCRIPTION}
- **Actual:** {ACTUAL_DESCRIPTION}
- **Evidence:** {EVIDENCE_SOURCE}
- **Findings:** {FINDINGS_DESCRIPTION}

### CI Burn-In (Stability)

- **Status:** {STATUS} {STATUS_ICON}
- **Threshold:** {THRESHOLD_VALUE} (e.g., "100 consecutive successful runs")
- **Actual:** {ACTUAL_VALUE} (e.g., "150 consecutive successful runs")
- **Evidence:** {EVIDENCE_SOURCE} (e.g., "CI burn-in results - ci-burn-in-2025-10-14.log")
- **Findings:** {FINDINGS_DESCRIPTION}

### Disaster Recovery (if applicable)

- **RTO (Recovery Time Objective)**
  - **Status:** {STATUS} {STATUS_ICON}
  - **Threshold:** {THRESHOLD_VALUE}
  - **Actual:** {ACTUAL_VALUE}
  - **Evidence:** {EVIDENCE_SOURCE}

- **RPO (Recovery Point Objective)**
  - **Status:** {STATUS} {STATUS_ICON}
  - **Threshold:** {THRESHOLD_VALUE}
  - **Actual:** {ACTUAL_VALUE}
  - **Evidence:** {EVIDENCE_SOURCE}

---

## Maintainability Assessment

### Test Coverage

- **Status:** {STATUS} {STATUS_ICON}
- **Threshold:** {THRESHOLD_VALUE} (e.g., ">=80%")
- **Atual:** {ACTUAL_VALUE} (por exemplo, "87%")
- **Evidência:** {EVIDENCE_SOURCE} (por exemplo, "Relatório de cobertura - cobertura/lcov-report/index.html")
- **Encontros:** {FINDINGS_DESCRIPTION}

### Qualidade do código

- **Status:** {STATUS} {STATUS_ICON}
- **Limiar:** {THRESHOLD_VALUE} (