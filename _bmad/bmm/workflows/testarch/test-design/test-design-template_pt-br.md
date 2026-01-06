# Design de Teste: Épico {epic_num} - {epic_title}

**Data:** {date}
**Autor:** {user_name}
**Status:** Rascunho / Aprovado

---

## Resumo Executivo

**Escopo:** {design_level} design de teste para Épico {epic_num}

**Resumo de Risco:**

- Total de riscos identificados: {total_risks}
- Riscos de alta prioridade (≥6): {high_priority_count}
- Categorias críticas: {top_categories}

**Resumo de Cobertura:**

- Cenários P0: {p0_count} ({p0_hours} horas)
- Cenários P1: {p1_count} ({p1_hours} horas)
- Cenários P2/P3: {p2p3_count} ({p2p3_hours} horas)
- **Esforço total**: {total_hours} horas (~{total_days} dias)

---

## Avaliação de Risco

### Riscos de Alta Prioridade (Pontuação ≥6)

| ID Risco | Categoria | Descrição     | Probabilidade | Impacto | Pontuação | Mitigação    | Dono    | Cronograma |
| -------- | --------- | ------------- | ------------- | ------- | --------- | ------------ | ------- | ---------- |
| R-001    | SEC       | {description} | 2             | 3       | 6         | {mitigation} | {owner} | {date}     |
| R-002    | PERF      | {description} | 3             | 2       | 6         | {mitigation} | {owner} | {date}     |

### Riscos de Média Prioridade (Pontuação 3-4)

| ID Risco | Categoria | Descrição     | Probabilidade | Impacto | Pontuação | Mitigação    | Dono    |
| -------- | --------- | ------------- | ------------- | ------- | --------- | ------------ | ------- |
| R-003    | TECH      | {description} | 2             | 2       | 4         | {mitigation} | {owner} |
| R-004    | DATA      | {description} | 1             | 3       | 3         | {mitigation} | {owner} |

### Riscos de Baixa Prioridade (Pontuação 1-2)

| ID Risco | Categoria | Descrição     | Probabilidade | Impacto | Pontuação | Ação      |
| -------- | --------- | ------------- | ------------- | ------- | --------- | --------- |
| R-005    | OPS       | {description} | 1             | 2       | 2         | Monitorar |
| R-006    | BUS       | {description} | 1             | 1       | 1         | Monitorar |

### Legenda de Categoria de Risco

- **TECH**: Técnico/Arquitetura (falhas, integração, escalabilidade)
- **SEC**: Segurança (controles de acesso, auth, exposição de dados)
- **PERF**: Desempenho (violações de SLA, degradação, limites de recursos)
- **DATA**: Integridade de Dados (perda, corrupção, inconsistência)
- **BUS**: Impacto no Negócio (dano UX, erros de lógica, receita)
- **OPS**: Operações (implantação, configuração, monitoramento)

---

## Plano de Cobertura de Teste

### P0 (Crítico) - Rodar em todo commit

**Critérios**: Bloqueia jornada central + Alto risco (≥6) + Sem solução alternativa

| Requisito     | Nível Teste | Link Risco | Contagem Teste | Dono | Notas   |
| ------------- | ----------- | ---------- | -------------- | ---- | ------- |
| {requirement} | E2E         | R-001      | 3              | QA   | {notes} |
| {requirement} | API         | R-002      | 5              | QA   | {notes} |

**Total P0**: {p0_count} testes, {p0_hours} horas

### P1 (Alto) - Rodar em PR para main

**Critérios**: Funcionalidades importantes + Risco médio (3-4) + Fluxos comuns

| Requisito     | Nível Teste | Link Risco | Contagem Teste | Dono | Notas   |
| ------------- | ----------- | ---------- | -------------- | ---- | ------- |
| {requirement} | API         | R-003      | 4              | QA   | {notes} |
| {requirement} | Componente  | -          | 6              | DEV  | {notes} |

**Total P1**: {p1_count} testes, {p1_hours} horas

### P2 (Médio) - Rodar noturnamente/semanalmente

**Critérios**: Funcionalidades secundárias + Baixo risco (1-2) + Casos de borda

| Requisito     | Nível Teste | Link Risco | Contagem Teste | Dono | Notas   |
| ------------- | ----------- | ---------- | -------------- | ---- | ------- |
| {requirement} | API         | R-004      | 8              | QA   | {notes} |
| {requirement} | Unidade     | -          | 15             | DEV  | {notes} |

**Total P2**: {p2_count} testes, {p2_hours} horas

### P3 (Baixo) - Rodar sob demanda

**Critérios**: Bom-ter + Exploratório + Benchmarks de desempenho

| Requisito     | Nível Teste | Contagem Teste | Dono | Notas   |
| ------------- | ----------- | -------------- | ---- | ------- |
| {requirement} | E2E         | 2              | QA   | {notes} |
| {requirement} | Unidade     | 8              | DEV  | {notes} |

**Total P3**: {p3_count} testes, {p3_hours} horas

---

## Ordem de Execução

### Testes de Fumaça (<5 min)

**Propósito**: Feedback rápido, pegar problemas que quebram build

- [ ] {scenario} (30s)
- [ ] {scenario} (45s)
- [ ] {scenario} (1min)

**Total**: {smoke_count} cenários

### Testes P0 (<10 min)

**Propósito**: Validação de caminho crítico

- [ ] {scenario} (E2E)
- [ ] {scenario} (API)
- [ ] {scenario} (API)

**Total**: {p0_count} cenários

### Testes P1 (<30 min)

**Propósito**: Cobertura de funcionalidade importante

- [ ] {scenario} (API)
- [ ] {scenario} (Componente)

**Total**: {p1_count} cenários

### Testes P2/P3 (<60 min)

**Propósito**: Cobertura de regressão completa

- [ ] {scenario} (Unidade)
- [ ] {scenario} (API)

**Total**: {p2p3_count} cenários

---

## Estimativas de Recursos

### Esforço de Desenvolvimento de Teste

| Prioridade | Contagem          | Horas/Teste | Total Horas       | Notas                   |
| ---------- | ----------------- | ----------- | ----------------- | ----------------------- |
| P0         | {p0_count}        | 2.0         | {p0_hours}        | Config complexa, segurança |
| P1         | {p1_count}        | 1.0         | {p1_hours}        | Cobertura padrão        |
| P2         | {p2_count}        | 0.5         | {p2_hours}        | Cenários simples        |
| P3         | {p3_count}        | 0.25        | {p3_hours}        | Exploratório            |
| **Total**  | **{total_count}** | **-**       | **{total_hours}** | **~{total_days} dias**  |

### Pré-requisitos

**Dados de Teste:**

- Fábrica {factory_name} (baseada em faker, auto-limpeza)
- Fixture {fixture_name} (setup/teardown)

**Ferramentas:**

- {tool} para {purpose}
- {tool} para {purpose}

**Ambiente:**

- {env_requirement}
- {env_requirement}

---

## Critérios de Portão de Qualidade

### Limiares de Aprovação/Falha

- **Taxa de aprovação P0**: 100% (sem exceções)
- **Taxa de aprovação P1**: ≥95% (dispensas necessárias para falhas)
- **Taxa de aprovação P2/P3**: ≥90% (informativo)
- **Mitigações de alto risco**: 100% completas ou dispensas aprovadas

### Metas de Cobertura

- **Caminhos críticos**: ≥80%
- **Cenários de segurança**: 100%
- **Lógica de negócio**: ≥70%
- **Casos de borda**: ≥50%

### Requisitos Não Negociáveis

- [ ] Todos os testes P0 passam
- [ ] Nenhum item de alto risco (≥6) não mitigado
- [ ] Testes de segurança (categoria SEC) passam 100%
- [ ] Metas de desempenho atingidas (categoria PERF)

---

## Planos de Mitigação

### R-001: {Risk Description} (Pontuação: 6)

**Estratégia de Mitigação:** {detailed_mitigation}
**Dono:** {owner}
**Cronograma:** {date}
**Status:** Planejado / Em Progresso / Completo
**Verificação:** {how_to_verify}

### R-002: {Risk Description} (Pontuação: 6)

**Estratégia de Mitigação:** {detailed_mitigation}
**Dono:** {owner}
**Cronograma:** {date}
**Status:** Planejado / Em Progresso / Completo
**Verificação:** {how_to_verify}

---

## Suposições e Dependências

### Suposições

1. {assumption}
2. {assumption}
3. {assumption}

### Dependências

1. {dependency} - Necessário até {date}
2. {dependency} - Necessário até {date}

### Riscos para o Plano

- **Risco**: {risk_to_plan}
  - **Impacto**: {impact}
  - **Contingência**: {contingency}

---

## Aprovação

**Design de Teste Aprovado Por:**

- [ ] Gerente de Produto: {name} Data: {date}
- [ ] Líder Técnico: {name} Data: {date}
- [ ] Líder QA: {name} Data: {date}

**Comentários:**

---

---

---

## Apêndice

### Referências da Base de Conhecimento

- `risk-governance.md` - Framework de classificação de risco
- `probability-impact.md` - Metodologia de pontuação de risco
- `test-levels-framework.md` - Seleção de nível de teste
- `test-priorities-matrix.md` - Priorização P0-P3

### Documentos Relacionados

- PRD: {prd_link}
- Épico: {epic_link}
- Arquitetura: {arch_link}
- Especificação Técnica: {tech_spec_link}

---

**Gerado por**: Agente BMad TEA - Módulo Arquiteto de Teste
**Fluxo de Trabalho**: `_bmad/bmm/testarch/test-design`
**Versão**: 4.0 (BMad v6)
