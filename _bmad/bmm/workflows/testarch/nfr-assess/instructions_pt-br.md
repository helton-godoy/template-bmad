<!-- Powered by BMAD-CORE™ -->

# Avaliação de Requisitos Não Funcionais - Instruções v4.0

**Fluxo de Trabalho:** `testarch-nfr`
**Propósito:** Avaliar requisitos não funcionais (desempenho, segurança, confiabilidade, manutenibilidade) antes do lançamento com validação baseada em evidências
**Agente:** Arquiteto de Teste (TEA)
**Formato:** Markdown Puro v4.0 (sem blocos XML)

---

## Visão Geral

Este fluxo de trabalho realiza uma avaliação abrangente de requisitos não funcionais (RNFs) para validar se a implementação atende aos padrões de desempenho, segurança, confiabilidade e manutenibilidade antes do lançamento. Ele usa validação baseada em evidências com regras determinísticas de PASSOU/PREOCUPAÇÕES/FALHOU e fornece recomendações acionáveis para remediação.

**Capacidades Chave:**

- Avaliar múltiplas categorias de RNF (desempenho, segurança, confiabilidade, manutenibilidade, personalizado)
- Validar RNFs contra limites definidos de especificações técnicas, PRD ou padrões
- Classificar status deterministicamente (PASSOU/PREOCUPAÇÕES/FALHOU) com base em evidências
- Nunca adivinhar limites - marcar como PREOCUPAÇÕES se desconhecido
- Gerar trechos YAML prontos para integração com CI/CD
- Fornecer vitórias rápidas e ações recomendadas para remediação
- Criar checklists de evidências para lacunas

---

## Pré-requisitos

**Obrigatório:**

- Implementação implantada localmente ou acessível para avaliação
- Fontes de evidência disponíveis (resultados de teste, métricas, logs, resultados de CI)

**Recomendado:**

- Requisitos RNF definidos em tech-spec.md, PRD.md ou história
- Resultados de testes de desempenho, segurança, confiabilidade
- Métricas de aplicação (tempos de resposta, taxas de erro, taxa de transferência)
- Resultados de pipeline CI/CD para validação de burn-in

**Condições de Parada:**

- Se metas de RNF não estiverem definidas e não puderem ser obtidas, pare e solicite definição
- Se a implementação não estiver acessível para avaliação, pare e solicite implantação

---

## Passos do Fluxo de Trabalho

### Passo 1: Carregar Contexto e Base de Conhecimento

**Ações:**

1. Carregar fragmentos de conhecimento relevantes de `{project-root}/_bmad/bmm/testarch/tea-index.csv`:
   - `nfr-criteria.md` - Critérios e limites de requisitos não funcionais (segurança, desempenho, confiabilidade, manutenibilidade com exemplos de código, 658 linhas, 4 exemplos)
   - `ci-burn-in.md` - Padrões de burn-in de CI/CD para validação de confiabilidade (detecção de 10 iterações, sharding, execução seletiva, 678 linhas, 4 exemplos)
   - `test-quality.md` - Expectativas de qualidade de teste para manutenibilidade (determinístico, isolado, asserções explícitas, limites de comprimento/tempo, 658 linhas, 5 exemplos)
   - `playwright-config.md` - Padrões de configuração de desempenho: paralelização, padrões de timeout, saída de artefato (722 linhas, 5 exemplos)
   - `error-handling.md` - Padrões de validação de confiabilidade: exceções escopadas, validação de retentativa, log de telemetria, degradação graciosa (736 linhas, 4 exemplos)

2. Ler arquivo de história (se fornecido):
   - Extrair requisitos RNF
   - Identificar limites específicos ou SLAs
   - Notar quaisquer categorias RNF personalizadas

3. Ler artefatos BMad relacionados (se disponíveis):
   - `tech-spec.md` - Requisitos RNF técnicos e metas
   - `PRD.md` - Contexto RNF de nível de produto (expectativas do usuário)
   - `test-design.md` - Plano de teste RNF e prioridades

**Saída:** Entendimento completo das metas RNF, fontes de evidência e critérios de validação

---

### Passo 2: Identificar Categorias RNF e Limites

**Ações:**

1. Determinar quais categorias RNF avaliar (padrão: desempenho, segurança, confiabilidade, manutenibilidade):
   - **Desempenho**: Tempo de resposta, taxa de transferência, uso de recurso
   - **Segurança**: Autenticação, autorização, proteção de dados, varredura de vulnerabilidade
   - **Confiabilidade**: Tratamento de erros, recuperação, disponibilidade, tolerância a falhas
   - **Manutenibilidade**: Qualidade de código, cobertura de teste, documentação, dívida técnica

2. Adicionar categorias RNF personalizadas se especificado (ex: acessibilidade, internacionalização, conformidade)

3. Reunir limites para cada RNF:
   - De tech-spec.md (fonte primária)
   - De PRD.md (SLAs de nível de produto)
   - De arquivo de história (requisitos específicos de feature)
   - De variáveis de fluxo de trabalho (limites padrão)
   - Marcar limites como DESCONHECIDO se não definidos

4. Nunca adivinhar limites - se um limite é desconhecido, marque o RNF como PREOCUPAÇÕES

**Saída:** Lista completa de RNFs para avaliar com limites definidos (ou DESCONHECIDOS)

---

### Passo 3: Reunir Evidência

**Ações:**

1. Para cada categoria RNF, descobrir fontes de evidência:

   **Evidência de Desempenho:**
   - Resultados de teste de carga (JMeter, k6, Lighthouse)
   - Métricas de aplicação (tempos de resposta, taxa de transferência, uso de recurso)
   - Dados de monitoramento de desempenho (New Relic, Datadog, APM)
   - Traces de desempenho Playwright (se aplicável)

   **Evidência de Segurança:**
   - Resultados de varredura de segurança (SAST, DAST, varredura de dependência)
   - Resultados de teste de autenticação/autorização
   - Relatórios de teste de penetração
   - Relatórios de avaliação de vulnerabilidade
   - Resultados de auditoria de conformidade

   **Evidência de Confiabilidade:**
   - Logs de erro e taxas de erro
   - Dados de monitoramento de tempo de atividade (uptime)
   - Resultados de teste de engenharia de caos
   - Resultados de teste de failover/recuperação
   - Resultados de burn-in de CI (estabilidade ao longo do tempo)

   **Evidência de Manutenibilidade:**
   - Relatórios de cobertura de código (Istanbul, NYC, c8)
   - Resultados de análise estática (ESLint, SonarQube)
   - Métricas de dívida técnica
   - Completude da documentação
   - Avaliação de qualidade de teste (do fluxo de trabalho test-review)

2. Ler arquivos relevantes de diretórios de evidência:
   - `{test_results_dir}` para resultados de execução de teste
   - `{metrics_dir}` para métricas de aplicação
   - `{logs_dir}` para logs de aplicação
   - Resultados de pipeline CI/CD (se `include_ci_results` for verdadeiro)

3. Marcar RNFs sem evidência como "SEM EVIDÊNCIA" - nunca inferir ou assumir

**Saída:** Inventário de evidência abrangente para cada RNF

---

### Passo 4: Avaliar RNFs com Regras Determinísticas

**Ações:**

1. Para cada RNF, aplicar regras determinísticas de PASSOU/PREOCUPAÇÕES/FALHOU:

   **Critérios de PASSOU:**
   - Evidência existe E atende ao limite definido
   - Nenhuma preocupação sinalizada na evidência
   - Exemplo: Tempo de resposta é 350ms (limite: 500ms) → PASSOU

   **Critérios de PREOCUPAÇÕES:**
   - Limite é DESCONHECIDO (não definido)
   - Evidência está FALTANDO ou INCOMPLETA
   - Evidência está próxima do limite (dentro de 10%)
   - Evidência mostra problemas intermitentes
   - Exemplo: Tempo de resposta é 480ms (limite: 500ms, 96% do limite) → PREOCUPAÇÕES

   **Critérios de FALHOU:**
   - Evidência existe MAS não atende ao limite
   - Evidência crítica está FALTANDO
   - Evidência mostra falhas consistentes
   - Exemplo: Tempo de resposta é 750ms (limite: 500ms) → FALHOU

2. Documentar descobertas para cada RNF:
   - Status (PASSOU/PREOCUPAÇÕES/FALHOU)
   - Fonte de evidência (caminho do arquivo, nome do teste, nome da métrica)
   - Valor real vs limite
   - Justificativa para classificação de status

3. Classificar severidade com base na categoria:
   - **CRÍTICO**: Falhas de segurança, falhas de confiabilidade (afetam usuários imediatamente)
   - **ALTA**: Falhas de desempenho, falhas de manutenibilidade (afetam usuários em breve)
   - **MÉDIA**: Preocupações sem falhas (podem afetar usuários eventualmente)
   - **BAIXA**: Evidência faltando para RNFs não críticos

**Saída:** Avaliação RNF completa com classificações de status determinísticas

---

### Passo 5: Identificar Vitórias Rápidas e Ações Recomendadas

**Ações:**

1. Para cada RNF com status PREOCUPAÇÕES ou FALHOU, identificar vitórias rápidas:
   - Melhorias de baixo esforço e alto impacto
   - Mudanças de configuração (nenhuma mudança de código necessária)
   - Oportunidades de otimização (cache, indexação, compressão)
   - Adições de monitoramento (detectar problemas antes que se tornem falhas)

2. Fornecer ações recomendadas para cada problema:
   - Passos específicos para remediar (não conselhos genéricos)
   - Prioridade (CRÍTICO, ALTA, MÉDIA, BAIXA)
   - Esforço estimado (horas, dias)
   - Dono sugerido (dev, ops, segurança)

3. Sugerir ganchos de monitoramento para lacunas:
   - Adicionar monitoramento de desempenho (APM, monitoramento sintético)
   - Adicionar rastreamento de erros (Sentry, Rollbar, logs de erro)
   - Adicionar monitoramento de segurança (detecção de intrusão, logs de auditoria)
   - Adicionar limites de alerta (notificar antes que limites sejam violados)

4. Sugerir mecanismos de falha rápida (fail-fast):
   - Adicionar circuit breakers para confiabilidade
   - Adicionar rate limiting para desempenho
   - Adicionar portões de validação para segurança
   - Adicionar smoke tests para manutenibilidade

**Saída:** Plano de remediação acionável com recomendações priorizadas

---

### Passo 6: Gerar Entregáveis

**Ações:**

1. Criar arquivo markdown de avaliação RNF:
   - Usar template de `nfr-report-template.md`
   - Incluir resumo executivo (status geral, problemas críticos)
   - Adicionar avaliação RNF-por-RNF (status, evidência, limites)
   - Adicionar resumo de descobertas (contagem PASSOU, contagem PREOCUPAÇÕES, contagem FALHOU)
   - Adicionar seção de vitórias rápidas
   - Adicionar seção de ações recomendadas
   - Adicionar checklist de lacunas de evidência
   - Salvar em `{output_folder}/nfr-assessment.md`

2. Gerar trecho YAML de portão (se habilitado):

   ```yaml
   nfr_assessment:
     date: '2025-10-14'
     categories:
       performance: 'PASS'
       security: 'CONCERNS'
       reliability: 'PASS'
       maintainability: 'PASS'
     overall_status: 'CONCERNS'
     critical_issues: 0
     high_priority_issues: 1
     concerns: 2
     blockers: false
   ```

3. Gerar checklist de evidência (se habilitado):
   - Listar todos os RNFs com evidência FALTANDO ou INCOMPLETA
   - Atribuir donos para coleta de evidência
   - Sugerir fontes de evidência (testes, métricas, logs)
   - Definir prazos para coleta de evidência

4. Atualizar arquivo de história (se habilitado e solicitado):
   - Adicionar seção "Avaliação RNF" ao markdown da história
   - Link para relatório de avaliação RNF
   - Incluir status geral e problemas críticos
   - Adicionar status de portão

**Saída:** Documentação de avaliação RNF completa pronta para revisão e integração CI/CD

---

## Abordagem Não Prescritiva

**Exemplos Mínimos:** Este fluxo de trabalho fornece princípios e padrões, não templates rígidos. Equipes devem adaptar categorias RNF, limites e critérios de avaliação às suas necessidades.

**Padrões Chave para Seguir:**

- Usar validação baseada em evidências (sem adivinhação ou inferência)
- Aplicar regras determinísticas (classificação consistente de PASSOU/PREOCUPAÇÕES/FALHOU)
- Nunca adivinhar limites (marcar como PREOCUPAÇÕES se desconhecido)
- Fornecer recomendações acionáveis (passos específicos, não conselhos genéricos)
- Gerar artefatos prontos para portão (trechos YAML para CI/CD)

**Estender Conforme Necessário:**

- Adicionar categorias RNF personalizadas (acessibilidade, internacionalização, conformidade)
- Integrar com ferramentas externas (New Relic, Datadog, SonarQube, JIRA)
- Adicionar limites e regras personalizados
- Link para sistemas de avaliação externos

---

## Categorias e Critérios RNF

### Desempenho

**Critérios:**

- Tempo de resposta (percentis p50, p95, p99)
- Taxa de transferência (requisições por segundo, transações por segundo)
- Uso de recurso (CPU, memória, disco, rede)
- Escalabilidade (horizontal, vertical)

**Limites (Padrão):**

- Tempo de resposta p95: 500ms
- Taxa de transferência: 100 RPS
- Uso de CPU: < 70% média
- Uso de memória: < 80% máx

**Fontes de Evidência:**

- Resultados de teste de carga (JMeter, k6, Gatling)
- Dados APM (New Relic, Datadog, Dynatrace)
- Relatórios Lighthouse (para web apps)
- Traces de desempenho Playwright

---

### Segurança

**Critérios:**

- Autenticação (segurança de login, gerenciamento de sessão)
- Autorização (controle de acesso, permissões)
- Proteção de dados (criptografia, tratamento de PII)
- Gerenciamento de vulnerabilidade (SAST, DAST, varredura de dependência)
- Conformidade (GDPR, HIPAA, PCI-DSS)

**Limites (Padrão):**

- Pontuação de segurança: >= 85/100
- Vulnerabilidades críticas: 0
- Vulnerabilidades altas: < 3
- Força de autenticação: MFA habilitado

**Fontes de Evidência:**

- Resultados SAST (SonarQube, Checkmarx, Veracode)
- Resultados DAST (OWASP ZAP, Burp Suite)
- Varredura de dependência (Snyk, Dependabot, npm audit)
- Relatórios de teste de penetração
- Logs de auditoria de segurança

---

### Confiabilidade

**Critérios:**

- Disponibilidade (porcentagem de tempo de atividade)
- Tratamento de erro (degradação graciosa, recuperação de erro)
- Tolerância a falhas (redundância, failover)
- Recuperação de desastres (backup, restauração, RTO/RPO)
- Estabilidade (burn-in de CI, engenharia de caos)

**Limites (Padrão):**

- Tempo de atividade: >= 99.9% (três noves)
- Taxa de erro: < 0.1% (1 em 1000 requisições)
- MTTR (Tempo Médio Para Recuperação): < 15 minutos
- Burn-in de CI: 100 execuções bem-sucedidas consecutivas

**Fontes de Evidência:**

- Monitoramento de tempo de atividade (Pingdom, UptimeRobot, StatusCake)
- Logs de erro e taxas de erro
- Resultados de burn-in de CI (veja `ci-burn-in.md`)
- Resultados de teste de engenharia de caos (Chaos Monkey, Gremlin)
- Relatórios de incidente e postmortems

---

### Manutenibilidade

**Critérios:**

- Qualidade de código (complexidade, duplicação, code smells)
- Cobertura de teste (unitário, integração, E2E)
- Documentação (comentários de código, README, docs de arquitetura)
- Dívida técnica (taxa de dívida, churn de código)
- Qualidade de teste (do fluxo de trabalho test-review)

**Limites (Padrão):**

- Cobertura de teste: >= 80%
- Pontuação de qualidade de código: >= 85/100
- Taxa de dívida técnica: < 5%
- Completude da documentação: >= 90%

**Fontes de Evidência:**

- Relatórios de cobertura (Istanbul, NYC, c8, JaCoCo)
- Análise estática (ESLint, SonarQube, CodeClimate)
- Auditoria de documentação (manual ou automatizada)
- Relatório de revisão de teste (do fluxo de trabalho test-review)
- Métricas Git (churn de código, frequência de commit)

---

## Regras de Avaliação Determinísticas

### Regras de PASSOU

- Evidência existe
- Evidência atende ou excede limite
- Nenhuma preocupação sinalizada
- Qualidade é aceitável

**Exemplo:**

```markdown
RNF: Tempo de Resposta p95
Limite: 500ms
Evidência: Resultado de teste de carga mostra 350ms p95
Status: PASSOU ✅
```

---

### Regras de PREOCUPAÇÕES

- Limite é DESCONHECIDO
- Evidência está FALTANDO ou INCOMPLETA
- Evidência está próxima do limite (dentro de 10%)
- Evidência mostra problemas intermitentes
- Qualidade é marginal

**Exemplo:**

```markdown
RNF: Tempo de Resposta p95
Limite: 500ms
Evidência: Resultado de teste de carga mostra 480ms p95 (96% do limite)
Status: PREOCUPAÇÕES ⚠️
Recomendação: Otimizar antes da produção - muito próximo do limite
```

---

### Regras de FALHOU

- Evidência existe MAS não atende ao limite
- Evidência crítica está FALTANDO
- Evidência mostra falhas consistentes
- Qualidade é inaceitável

**Exemplo:**

```markdown
RNF: Tempo de Resposta p95
Limite: 500ms
Evidência: Resultado de teste de carga mostra 750ms p95 (150% do limite)
Status: FALHOU ❌
Recomendação: BLOQUEADOR - otimizar desempenho antes do lançamento
```

---

## Integração com Artefatos BMad

### Com tech-spec.md

- Fonte primária para requisitos e limites RNF
- Carregar metas de desempenho, requisitos de segurança, SLAs de confiabilidade
- Usar decisões arquiteturais para entender trade-offs de RNF

### Com test-design.md

- Entender plano de teste RNF e prioridades
- Referenciar prioridades de teste (P0/P1/P2/P3) para classificação de severidade
- Alinhar avaliação com validação RNF planejada

### Com PRD.md

- Entender expectativas RNF de nível de produto
- Verificar se RNFs alinham com metas de experiência do usuário
- Checar por requisitos RNF não declarados (implícitos por metas de produto)

---

## Portões de Qualidade

### Bloqueador de Lançamento (FALHOU)

- RNF crítico tem status FALHOU (segurança, confiabilidade)
- Falha de desempenho afeta experiência do usuário severamente
- Não lançar até que FALHOU seja resolvido

### Bloqueador de PR (ALTAS PREOCUPAÇÕES)

- RNF de alta prioridade tem status FALHOU
- Múltiplas PREOCUPAÇÕES existem
- Bloquear fusão de PR até endereçado

### Aviso (PREOCUPAÇÕES)

- Qualquer RNF tem status PREOCUPAÇÕES
- Evidência está faltando ou incompleta
- Endereçar antes do próximo lançamento

### Passou (PASSOU)

- Todos os RNFs têm status PASSOU
- Sem bloqueadores ou preocupações
- Pronto para lançamento

---

## Exemplo de Avaliação RNF

````markdown
# Avaliação RNF - História 1.3

**Feature:** Autenticação de Usuário
**Data:** 2025-10-14
**Status Geral:** PREOCUPAÇÕES ⚠️ (1 problema ALTA)

## Resumo Executivo

**Avaliação:** 3 PASSOU, 1 PREOCUPAÇÕES, 0 FALHOU
**Bloqueadores:** Nenhum
**Problemas de Alta Prioridade:** 1 (Segurança - MFA não forçado)
**Recomendação:** Endereçar preocupação de segurança antes do lançamento

## Avaliação de Desempenho

### Tempo de Resposta (p95)

- **Status:** PASSOU ✅
- **Limite:** 500ms
- **Real:** 320ms (64% do limite)
- **Evidência:** Resultados de teste de carga (test-results/load-2025-10-14.json)
- **Descobertas:** Tempo de resposta bem abaixo do limite em todos os percentis

### Taxa de Transferência

- **Status:** PASSOU ✅
- **Limite:** 100 RPS
- **Real:** 250 RPS (250% do limite)
- **Evidência:** Resultados de teste de carga (test-results/load-2025-10-14.json)
- **Descobertas:** Sistema lida com carga alvo de 2.5x sem degradação

## Avaliação de Segurança

### Força de Autenticação

- **Status:** PREOCUPAÇÕES ⚠️
- **Limite:** MFA habilitado para todos os usuários
- **Real:** MFA opcional (não forçado)
- **Evidência:** Auditoria de segurança (security-audit-2025-10-14.md)
- **Descobertas:** MFA é implementado mas não forçado por padrão
- **Recomendação:** ALTA - Forçar MFA para todas as novas contas, fornecer caminho de migração para usuários existentes

### Proteção de Dados

- **Status:** PASSOU ✅
- **Limite:** PII criptografado em repouso e em trânsito
- **Real:** AES-256 em repouso, TLS 1.3 em trânsito
- **Evidência:** Varredura de segurança (security-scan-2025-10-14.json)
- **Descobertas:** Todo PII propriamente criptografado

## Avaliação de Confiabilidade

### Tempo de Atividade (Uptime)

- **Status:** PASSOU ✅
- **Limite:** 99.9% (três noves)
- **Real:** 99.95% acima de 30 dias
- **Evidência:** Monitoramento de uptime (uptime-report-2025-10-14.csv)
- **Descobertas:** Excede meta com margem

### Taxa de Erro

- **Status:** PASSOU ✅
- **Limite:** < 0.1% (1 em 1000)
- **Real:** 0.05% (1 em 2000)
- **Evidência:** Logs de erro (logs/errors-2025-10.log)
- **Descobertas:** Taxa de erro bem abaixo do limite

## Avaliação de Manutenibilidade

### Cobertura de Teste

- **Status:** PASSOU ✅
- **Limite:** >= 80%
- **Real:** 87%
- **Evidência:** Relatório de cobertura (coverage/lcov-report/index.html)
- **Descobertas:** Cobertura excede limite com boa distribuição

### Qualidade de Código

- **Status:** PASSOU ✅
- **Limite:** >= 85/100
- **Real:** 92/100
- **Evidência:** Análise SonarQube (sonarqube-report-2025-10-14.pdf)
- **Descobertas:** Alta pontuação de qualidade de código com baixa dívida técnica

## Vitórias Rápidas

1. **Forçar MFA (Segurança)** - ALTA - 4 horas
   - Adicionar flag de configuração para forçar MFA para novas contas
   - Nenhuma mudança de código necessária, apenas ajuste de config

## Ações Recomendadas

### Imediato (Antes do Lançamento)

1. **Forçar MFA para todas as novas contas** - ALTA - 4 horas - Equipe de Segurança
   - Adicionar `ENFORCE_MFA=true` para config de produção
   - Atualizar fluxo de integração de usuário para requerer configuração de MFA
   - Testar aplicação de MFA em ambiente de staging

### Curto prazo (Próximo Sprint)

1. **Migrar usuários existentes para MFA** - MÉDIA - 3 dias - Produto + Engenharia
   - Projetar UX de migração (prompt, incentivos, prazo)
   - Implementar fluxo de migração com período de carência
   - Comunicar migração para usuários existentes

## Lacunas de Evidência

- [ ] Resultados de teste de engenharia de caos (confiabilidade)
  - Dono: Equipe DevOps
  - Prazo: 2025-10-21
  - Evidência sugerida: Rodar testes chaos monkey em staging

- [ ] Relatório de teste de penetração (segurança)
  - Dono: Equipe de Segurança
  - Prazo: 2025-10-28
  - Evidência sugerida: Agendar pentest de terceiro

## Trecho YAML de Portão

```yaml
nfr_assessment:
  date: '2025-10-14'
  story_id: '1.3'
  categories:
    performance: 'PASS'
    security: 'CONCERNS'
    reliability: 'PASS'
    maintainability: 'PASS'
  overall_status: 'CONCERNS'
  critical_issues: 0
  high_priority_issues: 1
  medium_priority_issues: 0
  concerns: 1
  blockers: false
  recommendations:
    - 'Enforce MFA for all new accounts (HIGH - 4 hours)'
  evidence_gaps: 2
```
````

## Resumo de Recomendações

- **Bloqueador de Lançamento:** Nenhum ✅
- **Alta Prioridade:** 1 (Forçar MFA antes do lançamento)
- **Média Prioridade:** 1 (Migrar usuários existentes para MFA)
- **Próximos Passos:** Endereçar item de prioridade ALTA, então prosseguir para fluxo de trabalho de portão

```

---

## Checklist de Validação

Antes de completar este fluxo de trabalho, verifique:

- ✅ Todas as categorias RNF avaliadas (desempenho, segurança, confiabilidade, manutenibilidade, personalizado)
- ✅ Limites definidos ou marcados como DESCONHECIDO
- ✅ Evidência reunida para cada RNF (ou marcada como FALTANDO)
- ✅ Status classificado deterministicamente (PASSOU/PREOCUPAÇÕES/FALHOU)
- ✅ Nenhum limite foi adivinhado (marcado como PREOCUPAÇÕES se desconhecido)
- ✅ Vitórias rápidas identificadas para PREOCUPAÇÕES/FALHOU
- ✅ Ações recomendadas são específicas e acionáveis
- ✅ Lacunas de evidência documentadas com donos e prazos
- ✅ Relatório de avaliação RNF gerado e salvo
- ✅ Trecho YAML de portão gerado (se habilitado)
- ✅ Checklist de evidência gerada (se habilitada)

---

## Notas

- **Nunca Adivinhe Limites:** Se um limite é desconhecido, marque como PREOCUPAÇÕES e recomende defini-lo
- **Baseado em Evidência:** Toda avaliação deve ser respaldada por evidência (testes, métricas, logs, resultados de CI)
- **Regras Determinísticas:** Use classificação consistente de PASSOU/PREOCUPAÇÕES/FALHOU baseada em evidência
- **Recomendações Acionáveis:** Forneça passos específicos, não conselhos genéricos
- **Integração de Portão:** Gere trechos YAML que podem ser consumidos por pipelines de CI/CD

---

## Solução de Problemas

### "Limites RNF não definidos"
- Verifique tech-spec.md para requisitos RNF
- Verifique PRD.md para SLAs de nível de produto
- Verifique arquivo de história para requisitos específicos de feature
- Se limites verdadeiramente desconhecidos, marque como PREOCUPAÇÕES e recomende defini-los

### "Nenhuma evidência encontrada"
- Verifique diretórios de evidência (test-results, metrics, logs)
- Verifique pipeline CI/CD para resultados de teste
- Se evidência verdadeiramente faltando, marque RNF como "SEM EVIDÊNCIA" e recomende gerá-la

### "Status PREOCUPAÇÕES mas nenhum limite excedido"
- PREOCUPAÇÕES é correto quando limite é DESCONHECIDO ou evidência está FALTANDO/INCOMPLETA
- PREOCUPAÇÕES também é correto quando evidência está próxima do limite (dentro de 10%)
- Documente por que PREOCUPAÇÕES foi atribuído

### "Status FALHOU bloqueia lançamento"
- Isso é intencional - FALHOU significa RNF crítico não atendido
- Recomende ações de remediação com passos específicos
- Re-execute avaliação após remediação

---

## Fluxos de Trabalho Relacionados

- **testarch-test-design** - Definir requisitos RNF e plano de teste
- **testarch-framework** - Configurar frameworks de teste de desempenho/segurança
- **testarch-ci** - Configurar CI/CD para validação RNF
- **testarch-gate** - Usar avaliação RNF como entrada para decisões de portão de qualidade
- **testarch-test-review** - Revisar qualidade de teste (RNF de manutenibilidade)

---

<!-- Powered by BMAD-CORE™ -->
