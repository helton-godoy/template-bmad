# Avaliação dos requisitos não funcionais - Instruções v4.0

**Fluxo de trabalho:** `testarch-nfr`
**Põr:** Avaliar requisitos não funcionais (desempenho, segurança, confiabilidade, manutenção) antes da liberação com validação baseada em evidências
**Agente:** Arquiteto de ensaio (TEA)
**Formato:** Puro Markdown v4.0 (sem blocos XML)

---

## Overview

This workflow performs a comprehensive assessment of non-functional requirements (NFRs) to validate that the implementation meets performance, security, reliability, and maintainability standards before release. It uses evidence-based validation with deterministic PASS/CONCERNS/FAIL rules and provides actionable recommendations for remediation.

**Key Capabilities:**

- Assess multiple NFR categories (performance, security, reliability, maintainability, custom)
- Validate NFRs against defined thresholds from tech specs, PRD, or defaults
- Classify status deterministically (PASS/CONCERNS/FAIL) based on evidence
- Never guess thresholds - mark as CONCERNS if unknown
- Generate gate-ready YAML snippets for CI/CD integration
- Provide quick wins and recommended actions for remediation
- Create evidence checklists for gaps

---

## Pré-requisitos

**Obrigatório:**

- Implementation implantado localmente ou acessível para avaliação
- Fontes de evidência disponíveis (resultados de teste, métricas, logs, resultados de IC)

**Recomendado:**

- Requisitos NFR definidos em tech-spec.md, PRD.md, ou história
- Resultados de testes de desempenho, segurança, confiabilidade
- métricas de aplicação (tempos de resposta, taxas de erro, rendimento)
- Resultados do gasoduto CI/CD para validação de queimados

**Condições de sal:**

- Se os objectivos NFR não forem definidos e não puderem ser obtidos, pare e solicite a definição
- Se implementation não estiver acessível para avaliação, pare e solicite implantação

---

## Workflow Steps

### Step 1: Load Context and Knowledge Base

**Actions:**

1. Load relevant knowledge fragments from `{project-root}/_bmad/bmm/testarch/tea-index.csv`:
   - `nfr-criteria.md` - Non-functional requirements criteria and thresholds (security, performance, reliability, maintainability with code examples, 658 lines, 4 examples)
   - `ci-burn-in.md` - CI/CD burn-in patterns for reliability validation (10-iteration detection, sharding, selective execution, 678 lines, 4 examples)
   - `test-quality.md` - Test quality expectations for maintainability (deterministic, isolated, explicit assertions, length/time limits, 658 lines, 5 examples)
   - `playwright-config.md` - Performance configuration patterns: parallelization, timeout standards, artifact output (722 lines, 5 examples)
   - `error-handling.md` - Reliability validation patterns: scoped exceptions, retry validation, telemetry logging, graceful degradation (736 lines, 4 examples)

2. Read story file (if provided):
   - Extract NFR requirements
   - Identify specific thresholds or SLAs
   - Note any custom NFR categories

3. Read related BMad artifacts (if available):
   - `tech-spec.md` - Technical NFR requirements and targets
   - `PRD.md` - Product-level NFR context (user expectations)
   - `test-design.md` - NFR test plan and priorities

**Output:** Complete understanding of NFR targets, evidence sources, and validation criteria

---

### Etapa 2: Identificar as categorias e limiares NFR

**Acções:**

1. Determinar quais categorias NFR para avaliar (padrão: desempenho, segurança, confiabilidade, manutenção):
- **Performance**: Tempo de resposta, rendimento, utilização de recursos
- **Segurança**: autenticação, autorização, protecção de dados, verificação de vulnerabilidade
- **Fiabilidade**: Tratamento de erros, recuperação, disponibilidade, tolerância a falhas
- **Manutenção**: qualidade do código, cobertura do teste, documentação, dívida técnica

2. Adicione categorias NFR personalizadas se especificado (por exemplo, acessibilidade, internacionalização, conformidade)

3. Recolher limiares para cada NFR:
- Da tech-spec.md (fonte primária)
- De PRD.md (SLAs de nível de produto)
- Do arquivo de história (requisitos específicos de recursos)
- Variáveis de fluxo de trabalho (limiares padrão)
- Marcar limiares como UNKNOWN se não for definido

4. Nunca adivinhar limiares - se um limiar é desconhecido, marcar o NFR como CONCENTRAÇÃO

**Saída:** Lista completa de NFR para avaliar com limiares definidos (ou UNKNOWN)

---

### Passo 3: Recolher evidência

**Acções:**

1. Para cada categoria NFR, descubra fontes de evidência:

**Evidencia de desempenho:**
- Resultados do teste de carga (JMeter, k6, Farol)
- métricas de aplicação (tempos de resposta, rendimento, uso de recursos)
- Dados de monitoramento de desempenho (New Relic, Datadog, APM)
- Traços de desempenho do dramaturgo (se aplicável)

**Evidência de segurança:**
- Resultados da verificação de segurança (SAST, DAST, verificação de dependência)
- Resultados dos testes de autenticação/autorização
- Relatórios de testes de penetração
- Relatórios de avaliação da vulnerabilidade
- Resultados da auditoria de conformidade

**Evidencia de fiabilidade:**
- Registros de erros e taxas de erro
- Dados de monitorização do tempo de trabalho
- Resultados dos testes de engenharia do caos
- Resultados dos testes de falha/recuperação
- CI Burn-i