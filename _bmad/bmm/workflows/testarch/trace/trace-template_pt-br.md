# Matriz de Rastreabilidade & Decisão de Portão - História {STORY_ID}

**História:** {STORY_TITLE}
**Data:** {DATE}
**Avaliador:** {user_name or TEA Agent}

---

## FASE 1: RASTREABILIDADE DE REQUISITOS

### Resumo de Cobertura

| Prioridade | Total Critérios | Cobertura TOTAL | % Cobertura | Status       |
| ---------- | --------------- | --------------- | ----------- | ------------ |
| P0         | {P0_TOTAL}      | {P0_FULL}       | {P0_PCT}%   | {P0_STATUS}  |
| P1         | {P1_TOTAL}      | {P1_FULL}       | {P1_PCT}%   | {P1_STATUS}  |
| P2         | {P2_TOTAL}      | {P2_FULL}       | {P2_PCT}%   | {P2_STATUS}  |
| P3         | {P3_TOTAL}      | {P3_FULL}       | {P3_PCT}%   | {P3_STATUS}  |
| **Total**  | **{TOTAL}**     | **{FULL}**      | **{PCT}%**  | **{STATUS}** |

**Legenda:**

- ✅ PASSOU - Cobertura atende ao limiar do portão de qualidade
- ⚠️ AVISO - Cobertura abaixo do limiar mas não crítico
- ❌ FALHOU - Cobertura abaixo do limiar mínimo (bloqueio)

---

### Mapeamento Detalhado

#### {CRITERION_ID}: {CRITERION_DESCRIPTION} ({PRIORITY})

- **Cobertura:** {COVERAGE_STATUS} {STATUS_ICON}
- **Testes:**
  - `{TEST_ID}` - {TEST_FILE}:{LINE}
    - **Dado:** {GIVEN}
    - **Quando:** {WHEN}
    - **Então:** {THEN}
  - `{TEST_ID_2}` - {TEST_FILE_2}:{LINE}
    - **Dado:** {GIVEN_2}
    - **Quando:** {WHEN_2}
    - **Então:** {THEN_2}

- **Lacunas:** (se PARCIAL ou APENAS-UNIDADE ou APENAS-INTEGRAÇÃO)
  - Faltando: {MISSING_SCENARIO_1}
  - Faltando: {MISSING_SCENARIO_2}

- **Recomendação:** {RECOMMENDATION_TEXT}

---

#### Exemplo: AC-1: Usuário pode logar com email e senha (P0)

- **Cobertura:** TOTAL ✅
- **Testes:**
  - `1.3-E2E-001` - tests/e2e/auth.spec.ts:12
    - **Dado:** Usuário tem credenciais válidas
    - **Quando:** Usuário submete formulário de login
    - **Então:** Usuário é redirecionado para dashboard
  - `1.3-UNIT-001` - tests/unit/auth-service.spec.ts:8
    - **Dado:** Email válido e hash de senha
    - **Quando:** validateCredentials é chamado
    - **Então:** Retorna objeto de usuário

---

#### Exemplo: AC-3: Usuário pode redefinir senha via email (P1)

- **Cobertura:** PARCIAL ⚠️
- **Testes:**
  - `1.3-E2E-003` - tests/e2e/auth.spec.ts:44
    - **Dado:** Usuário solicita redefinição de senha
    - **Quando:** Usuário clica no link de redefinição no email
    - **Então:** Usuário pode definir nova senha

- **Lacunas:**
  - Faltando: Validação de entrega de email
  - Faltando: Tratamento de token expirado (caminho de erro)
  - Faltando: Tratamento de token inválido (teste de segurança)
  - Faltando: Teste de unidade para lógica de geração de token

- **Recomendação:** Adicionar `1.3-API-001` para teste de integração de serviço de email e `1.3-UNIT-003` para lógica de geração de token. Adicionar `1.3-E2E-004` para validação de caminho de erro (tokens expirados/inválidos).

---

### Análise de Lacunas

#### Lacunas Críticas (BLOQUEIO) ❌

{CRITICAL_GAP_COUNT} lacunas encontradas. **Não lançar até resolver.**

1. **{CRITERION_ID}: {CRITERION_DESCRIPTION}** (P0)
   - Cobertura Atual: {COVERAGE_STATUS}
   - Testes Faltando: {MISSING_TEST_DESCRIPTION}
   - Recomendado: {RECOMMENDED_TEST_ID} ({RECOMMENDED_TEST_LEVEL})
   - Impacto: {IMPACT_DESCRIPTION}

---

#### Lacunas de Alta Prioridade (BLOQUEIO PR) ⚠️

{HIGH_GAP_COUNT} lacunas encontradas. **Resolver antes de fundir PR.**

1. **{CRITERION_ID}: {CRITERION_DESCRIPTION}** (P1)
   - Cobertura Atual: {COVERAGE_STATUS}
   - Testes Faltando: {MISSING_TEST_DESCRIPTION}
   - Recomendado: {RECOMMENDED_TEST_ID} ({RECOMMENDED_TEST_LEVEL})
   - Impacto: {IMPACT_DESCRIPTION}

---

#### Lacunas de Média Prioridade (Noturno) ⚠️

{MEDIUM_GAP_COUNT} lacunas encontradas. **Resolver em melhorias de teste noturnas.**

1. **{CRITERION_ID}: {CRITERION_DESCRIPTION}** (P2)
   - Cobertura Atual: {COVERAGE_STATUS}
   - Recomendado: {RECOMMENDED_TEST_ID} ({RECOMMENDED_TEST_LEVEL})

---

#### Lacunas de Baixa Prioridade (Opcional) ℹ️

{LOW_GAP_COUNT} lacunas encontradas. **Opcional - adicionar se tempo permitir.**

1. **{CRITERION_ID}: {CRITERION_DESCRIPTION}** (P3)
   - Cobertura Atual: {COVERAGE_STATUS}

---

### Avaliação de Qualidade

#### Testes com Problemas

**Problemas de BLOQUEIO** ❌

- `{TEST_ID}` - {ISSUE_DESCRIPTION} - {REMEDIATION}

**Problemas de AVISO** ⚠️

- `{TEST_ID}` - {ISSUE_DESCRIPTION} - {REMEDIATION}

**Problemas de INFO** ℹ️

- `{TEST_ID}` - {ISSUE_DESCRIPTION} - {REMEDIATION}

---

#### Exemplo de Problemas de Qualidade

**Problemas de AVISO** ⚠️

- `1.3-E2E-001` - 145 segundos (excede meta de 90s) - Otimizar configuração de fixture para reduzir duração do teste
- `1.3-UNIT-005` - 320 linhas (excede limite de 300 linhas) - Dividir em múltiplos arquivos de teste focados

**Problemas de INFO** ℹ️

- `1.3-E2E-002` - Faltando estrutura Dado-Quando-Então - Refatorar bloco describe para usar formato BDD

---

#### Testes Passando nos Portões de Qualidade

**{PASSING_TEST_COUNT}/{TOTAL_TEST_COUNT} testes ({PASSING_PCT}%) atendem a todos os critérios de qualidade** ✅

---

### Análise de Cobertura Duplicada

#### Sobreposição Aceitável (Defesa em Profundidade)

- {CRITERION_ID}: Testado em unidade (lógica de negócio) e E2E (jornada do usuário) ✅

#### Duplicação Inaceitável ⚠️

- {CRITERION_ID}: Mesma validação em nível E2E e Componente
  - Recomendação: Remover {TEST_ID} ou consolidar com {OTHER_TEST_ID}

---

### Cobertura por Nível de Teste

| Nível Teste | Testes            | Critérios Cobertos   | % Cobertura      |
| ----------- | ----------------- | -------------------- | ---------------- |
| E2E         | {E2E_COUNT}       | {E2E_CRITERIA}       | {E2E_PCT}%       |
| API         | {API_COUNT}       | {API_CRITERIA}       | {API_PCT}%       |
| Componente  | {COMP_COUNT}      | {COMP_CRITERIA}      | {COMP_PCT}%      |
| Unidade     | {UNIT_COUNT}      | {UNIT_CRITERIA}      | {UNIT_PCT}%      |
| **Total**   | **{TOTAL_TESTS}** | **{TOTAL_CRITERIA}** | **{TOTAL_PCT}%** |

---

### Recomendações de Rastreabilidade

#### Ações Imediatas (Antes de Fundir PR)

1. **{ACTION_1}** - {DESCRIPTION}
2. **{ACTION_2}** - {DESCRIPTION}

#### Ações de Curto Prazo (Neste Sprint)

1. **{ACTION_1}** - {DESCRIPTION}
2. **{ACTION_2}** - {DESCRIPTION}

#### Ações de Longo Prazo (Backlog)

1. **{ACTION_1}** - {DESCRIPTION}

---

#### Recomendações de Exemplo

**Ações Imediatas (Antes de Fundir PR)**

1. **Adicionar Testes de Redefinição de Senha P1** - Implementar `1.3-API-001` para integração de serviço de email e `1.3-E2E-004` para validação de caminho de erro. Cobertura P1 atualmente em 80%, meta é 90%.
2. **Otimizar Teste E2E Lento** - Refatorar `1.3-E2E-001` para usar configuração de fixture mais rápida. Atualmente 145s, meta é <90s.

**Ações de Curto Prazo (Neste Sprint)**

1. **Melhorar Cobertura P2** - Adicionar validação E2E para tempo limite de sessão (`1.3-E2E-005`). Atualmente cobertura APENAS-UNIDADE.
2. **Dividir Arquivo de Teste Grande** - Quebrar `1.3-UNIT-005` (320 linhas) em múltiplos arquivos de teste focados (<300 linhas cada).

**Ações de Longo Prazo (Backlog)**

1. **Enriquecer Cobertura P3** - Adicionar testes para casos de borda em critérios P3 se tempo permitir.

---

## FASE 2: DECISÃO DO PORTÃO DE QUALIDADE

**Tipo de Portão:** {story | epic | release | hotfix}
**Modo de Decisão:** {deterministic | manual}

---

### Resumo de Evidência

#### Resultados de Execução de Teste

- **Total Testes**: {total_count}
- **Passou**: {passed_count} ({pass_percentage}%)
- **Falhou**: {failed_count} ({fail_percentage}%)
- **Pulou**: {skipped_count} ({skip_percentage}%)
- **Duração**: {total_duration}

**Divisão de Prioridade:**

- **Testes P0**: {p0_passed}/{p0_total} passou ({p0_pass_rate}%) {✅ | ❌}
- **Testes P1**: {p1_passed}/{p1_total} passou ({p1_pass_rate}%) {✅ | ⚠️ | ❌}
- **Testes P2**: {p2_passed}/{p2_total} passou ({p2_pass_rate}%) {informativo}
- **Testes P3**: {p3_passed}/{p3_total} passou ({p3_pass_rate}%) {informativo}

**Taxa Geral de Aprovação**: {overall_pass_rate}% {✅ | ⚠️ | ❌}

**Fonte de Resultados de Teste**: {CI_run_id | test_report_url | local_run}

---

#### Resumo de Cobertura (da Fase 1)

**Cobertura de Requisitos:**

- **Critérios de Aceite P0**: {p0_covered}/{p0_total} coberto ({p0_coverage}%) {✅ | ❌}
- **Critérios de Aceite P1**: {p1_covered}/{p1_total} coberto ({p1_coverage}%) {✅ | ⚠️ | ❌}
- **Critérios de Aceite P2**: {p2_covered}/{p2_total} coberto ({p2_coverage}%) {informativo}
- **Cobertura Geral**: {overall_coverage}%

**Cobertura de Código** (se disponível):

- **Cobertura de Linha**: {line_coverage}% {✅ | ⚠️ | ❌}
- **Cobertura de Ramo**: {branch_coverage}% {✅ | ⚠️ | ❌}
- **Cobertura de Função**: {function_coverage}% {✅ | ⚠️ | ❌}

**Fonte de Cobertura**: {coverage_report_url | coverage_file_path}

---

#### Requisitos Não Funcionais (NFRs)

**Segurança**: {PASSOU | PREOCUPAÇÕES | FALHOU | NAO_AVALIADO} {✅ | ⚠️ | ❌}

- Problemas de Segurança: {security_issue_count}
- {details_if_issues}

**Desempenho**: {PASSOU | PREOCUPAÇÕES | FALHOU | NAO_AVALIADO} {✅ | ⚠️ | ❌}

- {performance_metrics_summary}

**Confiabilidade**: {PASSOU | PREOCUPAÇÕES | FALHOU | NAO_AVALIADO} {✅ | ⚠️ | ❌}

- {reliability_metrics_summary}

**Manutenibilidade**: {PASSOU | PREOCUPAÇÕES | FALHOU | NAO_AVALIADO} {✅ | ⚠️ | ❌}

- {maintainability_metrics_summary}

**Fonte NFR**: {nfr_assessment_file_path | not_assessed}

---

#### Validação de Instabilidade

**Resultados de Burn-in** (se disponível):

- **Iterações de Burn-in**: {iteration_count} (e.g., 10)
- **Testes Instáveis Detectados**: {flaky_test_count} {✅ se 0 | ❌ se >0}
- **Pontuação de Estabilidade**: {stability_percentage}%

**Lista de Testes Instáveis** (se houver):

- {flaky_test_1_name} - {failure_rate}
- {flaky_test_2_name} - {failure_rate}

**Fonte de Burn-in**: {CI_burn_in_run_id | not_available}

---

### Avaliação de Critérios de Decisão

#### Critérios P0 (Devem TODOS Passar)

| Critério              | Limiar    | Real                      | Status   |
| --------------------- | --------- | ------------------------- | -------- | -------- |
| Cobertura P0          | 100%      | {p0_coverage}%            | {✅ PASSOU | ❌ FALHOU} |
| Taxa Aprovação P0     | 100%      | {p0_pass_rate}%           | {✅ PASSOU | ❌ FALHOU} |
| Problemas Segurança   | 0         | {security_issue_count}    | {✅ PASSOU | ❌ FALHOU} |
| Falhas Críticas NFR   | 0         | {critical_nfr_fail_count} | {✅ PASSOU | ❌ FALHOU} |
| Testes Instáveis      | 0         | {flaky_test_count}        | {✅ PASSOU | ❌ FALHOU} |

**Avaliação P0**: {✅ TODOS PASSARAM | ❌ UM OU MAIS FALHARAM}

---

#### Critérios P1 (Necessário para PASSAR, Pode Aceitar para PREOCUPAÇÕES)

| Critério               | Limiar                    | Real                 | Status   | ----------- | -------- |
| ---------------------- | ------------------------- | -------------------- | -------- | ----------- | -------- |
| Cobertura P1           | ≥{min_p1_coverage}%       | {p1_coverage}%       | {✅ PASSOU | ⚠️ PREOCUPAÇÕES | ❌ FALHOU} |
| Taxa Aprovação P1      | ≥{min_p1_pass_rate}%      | {p1_pass_rate}%      | {✅ PASSOU | ⚠️ PREOCUPAÇÕES | ❌ FALHOU} |
| Taxa Aprovação Geral   | ≥{min_overall_pass_rate}% | {overall_pass_rate}% | {✅ PASSOU | ⚠️ PREOCUPAÇÕES | ❌ FALHOU} |
| Cobertura Geral        | ≥{min_coverage}%          | {overall_coverage}%  | {✅ PASSOU | ⚠️ PREOCUPAÇÕES | ❌ FALHOU} |

**Avaliação P1**: {✅ TODOS PASSARAM | ⚠️ ALGUMAS PREOCUPAÇÕES | ❌ FALHOU}

---

#### Critérios P2/P3 (Informativo, Não Bloqueia)

| Critério          | Real            | Notas                                                        |
| ----------------- | --------------- | ------------------------------------------------------------ |
| Taxa Aprovação P2 | {p2_pass_rate}% | {allow_p2_failures ? "Rastreado, não bloqueia" : "Avaliado"} |
| Taxa Aprovação P3 | {p3_pass_rate}% | {allow_p3_failures ? "Rastreado, não bloqueia" : "Avaliado"} |

---

### DECISÃO DO PORTÃO: {PASSOU | PREOCUPAÇÕES | FALHOU | DISPENSADO}

---

### Justificativa

{Explicar decisão baseada na avaliação de critérios}

{Destacar evidência chave que conduziu a decisão}

{Notar quaisquer suposições ou ressalvas}

**Exemplo (PASSOU):**

> Todos os critérios P0 atendidos com 100% de cobertura e taxas de aprovação em testes críticos. Todos os critérios P1 excederam limiares com 98% de taxa de aprovação geral e 92% de cobertura. Nenhum problema de segurança detectado. Nenhum teste instável na validação. Funcionalidade pronta para implantação em produção com monitoramento padrão.

**Exemplo (PREOCUPAÇÕES):**

> Todos os critérios P0 atendidos, garantindo que jornadas de usuário críticas estejam protegidas. No entanto, cobertura P1 (88%) cai abaixo do limiar (90%) devido à falta de teste E2E para caso de borda AC-5. Taxa de aprovação geral (96%) é excelente. Problemas são não críticos e têm soluções alternativas aceitáveis. Risco é baixo o suficiente para implantar com monitoramento aprimorado.

**Exemplo (FALHOU):**

> BLOQUEIOS CRÍTICOS DETECTADOS:
>
> 1. Cobertura P0 incompleta (80%) - Validação de segurança AC-2 faltando
> 2. Falhas de teste P0 (75% taxa de aprovação) na funcionalidade central de pesquisa
> 3. Vulnerabilidade de injeção SQL não resolvida no filtro de pesquisa (CRÍTICO)
>
> Lançamento DEVE SER BLOQUEADO até que problemas P0 sejam resolvidos. Vulnerabilidade de segurança não pode ser dispensada.

**Exemplo (DISPENSADO):**

> Decisão original foi FALHOU devido a falha de teste P0 no módulo legado de exportação Excel 2007 (afeta <1% dos usuários). No entanto, lançamento contém recursos críticos de conformidade GDPR exigidos por prazo regulatório (15 Out). Negócio aprovou dispensa dado:
>
> - Prioridade regulatória sobrepõe risco de módulo legado
> - Solução alternativa disponível (usar Excel 2010+)
> - Problema será corrigido no hotfix v2.4.1 (previsto 20 Out)
> - Monitoramento aprimorado no local

---

### {Seção: Deletar se não aplicável}

#### Riscos Residuais (Para PREOCUPAÇÕES ou DISPENSADO)

Listar problemas P1/P2 não resolvidos que não bloqueiam lançamento mas devem ser rastreados:

1. **{Descrição do Risco}**
   - **Prioridade**: P1 | P2
   - **Probabilidade**: Baixa | Média | Alta
   - **Impacto**: Baixo | Médio | Alto
   - **Pontuação de Risco**: {probabilidade × impacto}
   - **Mitigação**: {solução alternativa ou plano de monitoramento}
   - **Remediação**: {correção no próximo sprint/lançamento}

**Risco Residual Geral**: {BAIXO | MÉDIO | ALTO}

---

#### Detalhes da Dispensa (Para DISPENSADO apenas)

**Decisão Original**: ❌ FALHOU

**Razão da Falha**:

- {list_of_blocking_issues}

**Informação da Dispensa**:

- **Razão da Dispensa**: {business_justification}
- **Aprovador da Dispensa**: {name}, {role} (e.g., Jane Doe, VP Engenharia)
- **Data de Aprovação**: {YYYY-MM-DD}
- **Expiração da Dispensa**: {YYYY-MM-DD} (**NOTA**: NÃO se aplica ao próximo lançamento)

**Plano de Monitoramento**:

- {enhanced_monitoring_1}
- {enhanced_monitoring_2}
- {escalation_criteria}

**Plano de Remediação**:

- **Alvo de Correção**: {next_release_version} (e.g., hotfix v2.4.1)
- **Data Limite**: {YYYY-MM-DD}
- **Dono**: {team_or_person}
- **Verificação**: {how_fix_will_be_verified}

**Justificativa de Negócio**:
{detailed_explanation_of_why_waiver_is_acceptable}

---

#### Problemas Críticos (Para FALHOU ou PREOCUPAÇÕES)

Principais bloqueios exigindo atenção imediata:

| Prioridade | Problema      | Descrição           | Dono         | Data Limite  | Status             |
| ---------- | ------------- | ------------------- | ------------ | ------------ | ------------------ |
| P0         | {issue_title} | {brief_description} | {owner_name} | {YYYY-MM-DD} | {OPEN/IN_PROGRESS} |
| P0         | {issue_title} | {brief_description} | {owner_name} | {YYYY-MM-DD} | {OPEN/IN_PROGRESS} |
| P1         | {issue_title} | {brief_description} | {owner_name} | {YYYY-MM-DD} | {OPEN/IN_PROGRESS} |

**Contagem de Problemas Bloqueantes**: {p0_blocker_count} bloqueios P0, {p1_blocker_count} problemas P1

---

### Recomendações de Portão

#### Para Decisão PASSOU ✅

1. **Prosseguir para implantação**
   - Implantar em ambiente de staging
   - Validar com testes de fumaça
   - Monitorar métricas chave por 24-48 horas
   - Implantar em produção com monitoramento padrão

2. **Monitoramento Pós-Implantação**
   - {metric_1_to_monitor}
   - {metric_2_to_monitor}
   - {alert_thresholds}

3. **Critérios de Sucesso**
   - {success_criterion_1}
   - {success_criterion_2}

---

#### Para Decisão PREOCUPAÇÕES ⚠️

1. **Implantar com Monitoramento Aprimorado**
   - Implantar em staging com período de validação estendido
   - Habilitar registro/monitoramento aprimorado para áreas de risco conhecidas:
     - {risk_area_1}
     - {risk_area_2}
   - Definir alertas agressivos para problemas potenciais
   - Implantar em produção com cautela

2. **Criar Backlog de Remediação**
   - Criar história: "{fix_title_1}" (Prioridade: {priority})
   - Criar história: "{fix_title_2}" (Prioridade: {priority})
   - Sprint alvo: {next_sprint}

3. **Ações Pós-Implantação**
   - Monitorar {specific_areas} de perto por {time_period}
   - Atualizações semanais de status sobre progresso de remediação
   - Reavaliar após correções implantadas

---

#### Para Decisão FALHOU ❌

1. **Bloquear Implantação Imediatamente**
   - NÃO implantar em nenhum ambiente
   - Notificar partes interessadas sobre problemas bloqueantes
   - Escalar para líder técnico e GP

2. **Corrigir Problemas Críticos**
   - Abordar bloqueios P0 listados na seção Problemas Críticos
   - Atribuições de dono confirmadas
   - Datas limite acordadas
   - Standup diário sobre resolução de bloqueio

3. **Reexecutar Portão Após Correções**
   - Reexecutar suíte de teste completa após correções
   - Reexecutar fluxo de trabalho `bmad tea *trace`
   - Verificar decisão PASSOU antes de implantar

---

#### Para Decisão DISPENSADO 🔓

1. **Implantar com Aprovação de Negócio**
   - Confirmar que aprovador da dispensa assinou
   - Documentar dispensa nas notas de lançamento
   - Notificar todas as partes interessadas sobre riscos dispensados

2. **Monitoramento Agressivo**
   - {enhanced_monitoring_plan}
   - {escalation_procedures}
   - Verificações diárias em áreas de risco dispensadas

3. **Remediação Obrigatória**
   - Correção DEVE ser completada até {due_date}
   - Problema NÃO PODE ser dispensado no próximo lançamento
   - Rastrear progresso de remediação semanalmente
   - Verificar correção no próximo portão

---

### Próximos Passos

**Ações Imediatas** (próximas 24-48 horas):

1. {action_1}
2. {action_2}
3. {action_3}

**Ações de Acompanhamento** (próximo sprint/lançamento):

1. {action_1}
2. {action_2}
3. {action_3}

**Comunicação com Partes Interessadas**:

- Notificar GP: {decision_summary}
- Notificar SM: {decision_summary}
- Notificar líder DEV: {decision_summary}

---

## Trecho YAML Integrado (CI/CD)

```yaml
traceability_and_gate:
  # Fase 1: Rastreabilidade
  traceability:
    story_id: "{STORY_ID}"
    date: "{DATE}"
    coverage:
      overall: {OVERALL_PCT}%
      p0: {P0_PCT}%
      p1: {P1_PCT}%
      p2: {P2_PCT}%
      p3: {P3_PCT}%
    gaps:
      critical: {CRITICAL_COUNT}
      high: {HIGH_COUNT}
      medium: {MEDIUM_COUNT}
      low: {LOW_COUNT}
    quality:
      passing_tests: {PASSING_COUNT}
      total_tests: {TOTAL_TESTS}
      blocker_issues: {BLOCKER_COUNT}
      warning_issues: {WARNING_COUNT}
    recommendations:
      - "{RECOMMENDATION_1}"
      - "{RECOMMENDATION_2}"

  # Fase 2: Decisão de Portão
  gate_decision:
    decision: "{PASSOU | PREOCUPAÇÕES | FALHOU | DISPENSADO}"
    gate_type: "{story | epic | release | hotfix}"
    decision_mode: "{deterministic | manual}"
    criteria:
      p0_coverage: {p0_coverage}%
      p0_pass_rate: {p0_pass_rate}%
      p1_coverage: {p1_coverage}%
      p1_pass_rate: {p1_pass_rate}%
      overall_pass_rate: {overall_pass_rate}%
      overall_coverage: {overall_coverage}%
      security_issues: {security_issue_count}
      critical_nfrs_fail: {critical_nfr_fail_count}
      flaky_tests: {flaky_test_count}
    thresholds:
      min_p0_coverage: 100
      min_p0_pass_rate: 100
      min_p1_coverage: {min_p1_coverage}
      min_p1_pass_rate: {min_p1_pass_rate}
      min_overall_pass_rate: {min_overall_pass_rate}
      min_coverage: {min_coverage}
    evidence:
      test_results: "{CI_run_id | test_report_url}"
      traceability: "{trace_file_path}"
      nfr_assessment: "{nfr_file_path}"
      code_coverage: "{coverage_report_url}"
    next_steps: "{brief_summary_of_recommendations}"
    waiver: # Apenas se DISPENSADO
      reason: "{business_justification}"
      approver: "{name}, {role}"
      expiry: "{YYYY-MM-DD}"
      remediation_due: "{YYYY-MM-DD}"
```

---

## Artefatos Relacionados

- **Arquivo de História:** {STORY_FILE_PATH}
- **Design de Teste:** {TEST_DESIGN_PATH} (se disponível)
- **Especificação Técnica:** {TECH_SPEC_PATH} (se disponível)
- **Resultados de Teste:** {TEST_RESULTS_PATH}
- **Avaliação NFR:** {NFR_FILE_PATH} (se disponível)
- **Arquivos de Teste:** {TEST_DIR_PATH}

---

## Aprovação

**Fase 1 - Avaliação de Rastreabilidade:**

- Cobertura Geral: {OVERALL_PCT}%
- Cobertura P0: {P0_PCT}% {P0_STATUS}
- Cobertura P1: {P1_PCT}% {P1_STATUS}
- Lacunas Críticas: {CRITICAL_COUNT}
- Lacunas de Alta Prioridade: {HIGH_COUNT}

**Fase 2 - Decisão de Portão:**

- **Decisão**: {PASSOU | PREOCUPAÇÕES | FALHOU | DISPENSADO} {STATUS_ICON}
- **Avaliação P0**: {✅ TODOS PASSARAM | ❌ UM OU MAIS FALHARAM}
- **Avaliação P1**: {✅ TODOS PASSARAM | ⚠️ ALGUMAS PREOCUPAÇÕES | ❌ FALHOU}

**Status Geral:** {STATUS} {STATUS_ICON}

**Próximos Passos:**

- Se PASSOU ✅: Prosseguir para implantação
- Se PREOCUPAÇÕES ⚠️: Implantar com monitoramento, criar backlog de remediação
- Se FALHOU ❌: Bloquear implantação, corrigir problemas críticos, reexecutar fluxo de trabalho
- Se DISPENSADO 🔓: Implantar com aprovação de negócio e monitoramento agressivo

**Gerado:** {DATE}
**Fluxo de Trabalho:** testarch-trace v4.0 (Aprimorado com Decisão de Portão)

---

<!-- Alimentado por BMAD-CORE™ -->
