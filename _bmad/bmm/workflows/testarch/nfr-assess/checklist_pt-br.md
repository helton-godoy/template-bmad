# Avaliação dos requisitos não funcionais - Lista de verificação da validação

**Fluxo de trabalho:** `testarch-nfr`
**Põr:** Assegurar uma avaliação NFR abrangente e baseada em provas com recomendações acionáveis

---

## Prerequisites Validation

- [ ] Implementation is deployed and accessible for evaluation
- [ ] Evidence sources are available (test results, metrics, logs, CI results)
- [ ] NFR categories are determined (performance, security, reliability, maintainability, custom)
- [ ] Evidence directories exist and are accessible (`test_results_dir`, `metrics_dir`, `logs_dir`)
- [ ] Knowledge base is loaded (nfr-criteria, ci-burn-in, test-quality)

---

## Carregando Contexto

- [ ] Tech-spec.md carregado com sucesso (se disponível)
- [ ] PRD.md carregado (se disponível)
- [ ] Arquivo de história carregado (se aplicável)
- [ ] Fragmentos de conhecimento relevantes carregados de `tea-index.csv`:
- `nfr-criteria.md`
- `ci-burn-in.md`
- [ ] `test-quality.md`
- [ ] `playwright-config.md` (se utilizar o dramaturgo)

---

## NFR Categories and Thresholds

### Performance

- [ ] Response time threshold defined or marked as UNKNOWN
- [ ] Throughput threshold defined or marked as UNKNOWN
- [ ] Resource usage thresholds defined or marked as UNKNOWN
- [ ] Scalability requirements defined or marked as UNKNOWN

### Security

- [ ] Authentication requirements defined or marked as UNKNOWN
- [ ] Authorization requirements defined or marked as UNKNOWN
- [ ] Data protection requirements defined or marked as UNKNOWN
- [ ] Vulnerability management thresholds defined or marked as UNKNOWN
- [ ] Compliance requirements identified (GDPR, HIPAA, PCI-DSS, etc.)

### Reliability

- [ ] Availability (uptime) threshold defined or marked as UNKNOWN
- [ ] Error rate threshold defined or marked as UNKNOWN
- [ ] MTTR (Mean Time To Recovery) threshold defined or marked as UNKNOWN
- [ ] Fault tolerance requirements defined or marked as UNKNOWN
- [ ] Disaster recovery requirements defined (RTO, RPO) or marked as UNKNOWN

### Maintainability

- [ ] Test coverage threshold defined or marked as UNKNOWN
- [ ] Code quality threshold defined or marked as UNKNOWN
- [ ] Technical debt threshold defined or marked as UNKNOWN
- [ ] Documentation completeness threshold defined or marked as UNKNOWN

### Custom NFR Categories (if applicable)

- [ ] Custom NFR category 1: Thresholds defined or marked as UNKNOWN
- [ ] Custom NFR category 2: Thresholds defined or marked as UNKNOWN
- [ ] Custom NFR category 3: Thresholds defined or marked as UNKNOWN

---

## Recolha de provas

### Provas de desempenho

- [ ] Resultados dos ensaios de carga recolhidos (JMeter, k6, Gatling, etc.)
- [ ] métricas de aplicação coletadas (tempos de resposta, rendimento, uso de recursos)
- [ ] Dados APM recolhidos (New Relic, Datadog, Dynatrace, etc.)
- [ ] Relatórios do farol recolhidos (se aplicação web)
- [ ] Traços de desempenho do dramaturgo recolhidos (se aplicável)

### Provas de segurança

- [ ] Resultados SAST recolhidos (SonarQube, Checkmarx, Veracode, etc.)
- [ ] Resultados do DAST recolhidos (OWASP ZAP, Burp Suite, etc.)
- [ ] Resultados de digitalização de dependência coletados (Snyk, Dependabot, auditoria npm)
- [ ] Relatórios de ensaio de penetração recolhidos (se disponível)
- [ ] Registos de auditoria de segurança recolhidos
- [ ] Resultados da auditoria de conformidade recolhidos (se aplicável)

### Prova de fiabilidade

- [ ] Dados de monitorização do tempo de funcionamento recolhidos (Pingdom, UptimeRobot, StatusCake)
- [ ] Registos de erros recolhidos
- [ ] métricas de taxa de erro coletadas
- [ ] Resultados de queima de IC recolhidos (estabilidade ao longo do tempo)
- [ ] Resultados dos ensaios de engenharia do caos recolhidos (se disponíveis)
- [ ] Resultados dos testes de falha/recuperação recolhidos (se disponíveis)
- [ ] Relatórios de incidentes e autópsias recolhidas (se aplicável)

### Prova de manutenção

- [ ] Relatórios de cobertura de código recolhidos (Istanbul, NYC, c8, JaCoCo)
- [ ] Resultados de análise estática recolhidos (ESLint, SonarQube, CodeClima)
- [ ] métricas técnicas da dívida recolhidas
- [ ] Resultados da auditoria de documentação recolhidos
- [ ] Relatório de revisão de teste coletado (do fluxo de trabalho de revisão de teste, se disponível)
- [ ] métricas git coletadas (código churn, frequência de commit, etc.)

---

## Avaliação NFR com regras determinísticas

### Avaliação do desempenho

- [ ] Tempo de resposta avaliado em relação ao limiar
- [ ] Produção avaliada em função do limiar
- [ ] Utilização dos recursos avaliada em função do limiar
- [ ] Escalabilidade avaliada em função dos requisitos
- [ ] Estado classificado (PASS/CONCERS/FAIL) com justificação
- [ ] Fonte de provas documentada (localização do ficheiro, nome métrico)

### Avaliação da segurança

- [ ] Resistência à autenticação avaliada em função dos requisitos
- [ ] Controlos de autorização avaliados em função dos requisitos
- [ ] Protecção de dados avaliada em conformidade com os requisitos
- [ ] Gestão da vulnerabilidade avaliada em função dos limiares
- [ ] Conformidade avaliada em conformidade com os requisitos
- [ ] Estado classificado (PASS/CONCERS/FAIL) com justificação
- [ ] Fonte de evidência documentada (localização do ficheiro, resultado da verificação)

### Avaliação da fiabilidade

- [ ] Disponibilidade (tempo de funcionamento) avaliada em função do limiar
- [ ] Taxa de erro avaliada em relação ao limiar
- [ ]