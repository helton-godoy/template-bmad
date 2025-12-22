# BMM Planning Fluxos de trabalho (Fase 2)

## Visão geral

Os fluxos de trabalho da fase 2 (Planning) são **necessários**para todos os projectos. Eles transformam a visão estratégica em requisitos acionáveis usando um**sistema adaptador em escala** que seleciona automaticamente a profundidade planning correta com base na complexidade do projeto.

**Princípio chave:** Um ponto de entrada unificado (`workflow-init`) inteligentemente rotas para a metodologia planning adequada - de especificações tecnológicas rápidas para PRDs abrangentes.

**Quando utilizar:** Todos os projetos exigem planning. O sistema adapta a profundidade automaticamente com base na complexidade.

---

## Phase 2 Planning Workflow Overview

Phase 2 Planning uses a scale-adaptive system with three tracks:

### Quick Flow (Simple Planning)

- Entry: `workflow-init` routes based on project complexity
- Workflow: `tech-spec`
- Output: Technical document with story/epic structure
- Story count: 1-15 (typical)
- Next: Phase 4 (Implementation) - skips Phase 3

### BMad Method (Recommended)

- Entry: `workflow-init` routes based on project complexity
- Workflows: `prd` → (optional) `create-ux-design`
- Output: PRD with FRs/NFRs
- Story count: 10-50+ (typical)
- Next: Phase 3 (Solutioning) → Phase 4

### Enterprise Method

- Planning: Same as BMad Method (`prd` workflow)
- Solutioning: Extended Phase 3 workflows (Architecture + Security + DevOps)
- Story count: 30+ (typical)
- Next: Phase 4

The `correct-course` workflow can be used anytime for significant requirement changes.

---

## Referência rápida

| Workflow             | Agent       | Track                   | Purpose                                         | Typical Stories |
| -------------------- | ----------- | ----------------------- | ----------------------------------------------- | --------------- |
| **workflow-init**    | PM/Analyst  | All                     | Entry point: discovery + routing                | N/A             |
| **tech-spec**        | PM          | Quick Flow              | Technical document → Story or Epic+Stories      | 1-15            |
| **prd**              | PM          | BMad Method, Enterprise | Strategic PRD with FRs/NFRs (no epic breakdown) | 10-50+          |
| **create-ux-design** | UX Designer | BMad Method, Enterprise | Optional UX specification (after PRD)           | N/A             |
| **correct-course**   | PM/SM       | All                     | Mid-stream requirement changes                  | N/A             |

**Nota:** Contagem de histórias são orientação. Melhoria V6: Epic + Histórias são criadas após arquitetura para melhor qualidade.

---

## Scale-Adaptive Planning System

BMM uses three distinct planning tracks that adapt to project complexity:

### Track 1: Quick Flow

**Best For:** Bug fixes, simple features, clear scope, enhancements

**Planning:** Tech-spec only → Implementation

**Time:** Hours to 1 day

**Story Count:** Typically 1-15 (guidance)

**Documents:** tech-spec.md + story files

**Example:** "Fix authentication bug", "Add OAuth social login"

---

### Faixa 2: Método BMad (RECOMENDADO)

**Melhor para:** Produtos, plataformas, características complexas, múltiplos épicos

**Planning:** PRD + Arquitetura → Implementation

**Tempo:** 1-3 dias

**Contagem da história:** Tipicamente 10-50+ (orientação)

**Documentos:** PRD.md (FRs/NFRs) + architecture.md + epics.md + ficheiros épicos

**Greenfield:** Resumo do produto (opcional) → PRD (FRs/NFRs) → UX (opcional) → Arquitetura → Epics+ Histórias → Implementation

**Brownfield:** documento-projeto → PRD (FR/NFRs) → Arquitetura (recomendada) → Epics+ Histórias → Implementation

**Exemplo:** "Painel de cliente", "Plataforma de comércio eletrônico", "Adicionar pesquisa ao aplicativo existente"

**Por que arquitetura para Brownfield?** Destila um contexto de base de código em design de solução focada para o seu projeto específico.

---

### Track 3: Enterprise Method

**Best For:** Enterprise requirements, multi-tenant, compliance, security-sensitive

**Planning (Phase 2):** Uses BMad Method planning (PRD with FRs/NFRs)

**Solutioning (Phase 3):** Extended workflows (Architecture + Security + DevOps + SecOps as optional additions) → Epics+Stories

**Time:** 3-7 days total (1-3 days planning + 2-4 days extended solutioning)

**Story Count:** Typically 30+ (but defined by enterprise needs)

**Documents Phase 2:** PRD.md (FRs/NFRs)

**Documents Phase 3:** architecture.md + epics.md + epic files + security-architecture.md (optional) + devops-strategy.md (optional) + secops-strategy.md (optional)

**Example:** "Multi-tenant SaaS", "HIPAA-compliant portal", "Add SOC2 audit logging"

---

## Como funciona a seleção de faixas

`workflow-init` guia você através da escolha educacional:

1. **Description Analysis** - Analisa a descrição do projecto para a complexidade
2. **Apresentação Educacional** - Mostra todas as três faixas com trade-offs
3. **Recomendação** - Sugere faixa baseada em palavras-chave e contexto
4. **Escolha do Usuário** - Você seleciona a faixa que se encaixa

O sistema guia, mas nunca força. Podes anular as recomendações.

---

## Descrições do fluxo de trabalho

### início do fluxo de trabalho (ponto de entrada)

**Composto:**