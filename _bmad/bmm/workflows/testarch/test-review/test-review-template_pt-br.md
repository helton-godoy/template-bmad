# Checklist de Revisão de Teste - {FEATURE_NAME}

**Data:** {DATE}
**Revisor:** {REVIEWER_NAME}
**Autor:** {AUTHOR_NAME}
**Status:** {STATUS} (Rascunho / Aprovado / Mudanças Solicitadas)

---

## Resumo Executivo

**Revisão:** {PASS_COUNT} PASSOU, {CONCERNS_COUNT} PREOCUPAÇÕES, {FAIL_COUNT} FALHOU

**Recomendação:** {OVERALL_RECOMMENDATION}

---

## Arquitetura de Teste

### Seleção de Nível

- **Status:** {STATUS} {STATUS_ICON}
- **Descobertas:** {FINDINGS_DESCRIPTION}
- **Orientação:** Garantir que os testes estejam no nível apropriado (E2E vs API vs Componente vs Unidade) com base em `test-levels-framework.md`.

### Isolamento & Independência

- **Status:** {STATUS} {STATUS_ICON}
- **Descobertas:** {FINDINGS_DESCRIPTION}
- **Orientação:** Testes não devem depender uns dos outros ou de estado mutável compartilhado. Use padrões de `fixture-architecture.md`.

### Determinismo

- **Status:** {STATUS} {STATUS_ICON}
- **Descobertas:** {FINDINGS_DESCRIPTION}
- **Orientação:** Eliminar padrões instáveis como esperas rígidas ou condições de corrida. Veja `test-quality.md`.

---

## Implementação de Teste

### Nomenclatura & Organização

- **Status:** {STATUS} {STATUS_ICON}
- **Descobertas:** {FINDINGS_DESCRIPTION}
- **Orientação:** Nomes claros e descritivos usando estrutura Dado-Quando-Então.

### Afirmações

- **Status:** {STATUS} {STATUS_ICON}
- **Descobertas:** {FINDINGS_DESCRIPTION}
- **Orientação:** Use afirmações explícitas. Evite "roleta de afirmações" (muitas afirmações por teste).

### Seletores (se UI)

- **Status:** {STATUS} {STATUS_ICON}
- **Descobertas:** {FINDINGS_DESCRIPTION}
- **Orientação:** Use seletores resilientes (e.g., `data-testid`). Veja `selector-resilience.md`.

### Gerenciamento de Dados

- **Status:** {STATUS} {STATUS_ICON}
- **Descobertas:** {FINDINGS_DESCRIPTION}
- **Orientação:** Use fábricas para dados de teste. Garanta limpeza. Veja `data-factories.md`.

---

## Qualidade de Código

### Legibilidade

- **Status:** {STATUS} {STATUS_ICON}
- **Descobertas:** {FINDINGS_DESCRIPTION}

### Manutenibilidade

- **Status:** {STATUS} {STATUS_ICON}
- **Descobertas:** {FINDINGS_DESCRIPTION}
- **Orientação:** Princípios DRY (dentro do razoável para testes), fixtures modulares.

### Desempenho

- **Status:** {STATUS} {STATUS_ICON}
- **Descobertas:** {FINDINGS_DESCRIPTION}
- **Orientação:** Testes devem rodar eficientemente. Evite esperas desnecessárias.

---

## Problemas Específicos

### {ISSUE_TITLE_1}

- **Categoria:** {CATEGORY} (e.g., Instabilidade, Manutenibilidade)
- **Gravidade:** {SEVERITY} (Crítica / Maior / Menor)
- **Descrição:** {ISSUE_DESCRIPTION}
- **Recomendação:** {RECOMMENDATION}

### {ISSUE_TITLE_2}

- **Categoria:** {CATEGORY}
- **Gravidade:** {SEVERITY}
- **Descrição:** {ISSUE_DESCRIPTION}
- **Recomendação:** {RECOMMENDATION}

---

## Perguntas & Esclarecimentos

1. {QUESTION_1}
2. {QUESTION_2}

---

## Itens de Ação

- [ ] {ACTION_ITEM_1}
- [ ] {ACTION_ITEM_2}
- [ ] {ACTION_ITEM_3}

---

## Aprovação

**Resultado da Revisão:**

- [ ] **Aprovado** - Bom para fundir
- [ ] **Aprovado com Comentários** - Abordar problemas menores, sem necessidade de re-revisão
- [ ] **Mudanças Solicitadas** - Abordar problemas e solicitar re-revisão

**Assinatura do Revisor:** {REVIEWER_NAME}
**Data:** {DATE}

---

**Gerado pelo Agente BMad TEA** - {DATE}
