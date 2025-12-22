---
last-redoc-date: 2025-11-05
---

# Guia do agente do arquitecto de ensaio (TEA)

## Visão geral

- **Persona:** Murat, Master Test Architecte and Quality Advisor focado em testes baseados em risco, arquitetura de acessórios, ATDD e governança CI/CD.
- **Missão:** Forneça estratégias de qualidade acionáveis, cobertura de automação e decisões de porta que dimensionem com a complexidade do projeto e exigências de conformidade.
- **Use Quando:** Método BMad ou projetos de trilha empresarial, risco de integração é não trivial, risco de regressão de campo marrom existe, ou evidência conformidade / NFR é necessária. (Projetos de fluxo rápido normalmente não requerem TEA)

## Ciclo de vida do fluxo de trabalho do TEA

A TEA integra-se no ciclo de vida de desenvolvimento BMad durante a Solução (Fase 3) e Implementation (Fase 4):

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#fff','primaryTextColor':'#000','primaryBorderColor':'#000','lineColor':'#000','secondaryColor':'#fff','tertiaryColor':'#fff','fontSize':'16px','fontFamily':'arial'}}}%%
graph TB
    subgraph Phase2["<b>Phase 2: PLANNING</b>"]
        PM["<b>PM: *prd (creates PRD with FRs/NFRs)</b>"]
        PlanNote["<b>Business requirements phase</b>"]
        PM -.-> PlanNote
    end

    subgraph Phase3["<b>Phase 3: SOLUTIONING</b>"]
        Architecture["<b>Architect: *architecture</b>"]
        EpicsStories["<b>PM/Architect: *create-epics-and-stories</b>"]
        TestDesignSys["<b>TEA: *test-design (system-level)</b>"]
        Framework["<b>TEA: *framework</b>"]
        CI["<b>TEA: *ci</b>"]
        GateCheck["<b>Architect: *implementation-readiness</b>"]
        Architecture --> EpicsStories
        Architecture --> TestDesignSys
        TestDesignSys --> Framework
        EpicsStories --> Framework
        Framework --> CI
        CI --> GateCheck
        Phase3Note["<b>Epics created AFTER architecture,</b><br/><b>then system-level test design and test infrastructure setup</b>"]
        EpicsStories -.-> Phase3Note
    end

    subgraph Phase4["<b>Phase 4: IMPLEMENTATION - Per Epic Cycle</b>"]
        SprintPlan["<b>SM: *sprint-planning</b>"]
        TestDesign["<b>TEA: *test-design (per epic)</b>"]
        CreateStory["<b>SM: *create-story</b>"]
        ATDD["<b>TEA: *atdd (optional, before dev)</b>"]
        DevImpl["<b>DEV: implements story</b>"]
        Automate["<b>TEA: *automate</b>"]
        TestReview1["<b>TEA: *test-review (optional)</b>"]
        Trace1["<b>TEA: *trace (refresh coverage)</b>"]

        SprintPlan --> TestDesign
        TestDesign --> CreateStory
        CreateStory --> ATDD
        ATDD --> DevImpl
        DevImpl --> Automate
        Automate --> TestReview1
        TestReview1 --> Trace1
        Trace1 -.->|next story| CreateStory
        TestDesignNote["<b>Test design: 'How do I test THIS epic?'</b><br/>Creates test-design-epic-N.md per epic"]
        TestDesign -.-> TestDesignNote
    end

    subgraph Gate["<b>EPIC/RELEASE GATE</b>"]
        NFR["<b>TEA: *nfr-assess (if not done earlier)</b>"]
        TestReview2["<b>TEA: *test-review (final audit, optional)</b>"]
        TraceGate["<b>TEA: *trace - Phase 2: Gate</b>"]
        GateDecision{"<b>Gate Decision</b>"}

        NFR --> TestReview2
        TestReview2 --> TraceGate
        TraceGate --> GateDecision
        GateDecision -->|PASS| Pass["<b>PASS ✅</b>"]
        GateDecision -->|CONCERNS| Concerns["<b>CONCERNS ⚠️</b>"]
        GateDecision -->|FAIL| Fail["<b>FAIL ❌</b>"]
        GateDecision -->|WAIVED| Waived["<b>WAIVED ⏭️</b>"]
    end

    Phase2 --> Phase3
    Phase3 --> Phase4
    Phase4 --> Gate

    style Phase2 fill:#bbdefb,stroke:#0d47a1,stroke-width:3px,color:#000
    style Phase3 fill:#c8e6c9,stroke:#2e7d32,stroke-width:3px,color:#000
    style Phase4 fill:#e1bee7,stroke:#4a148c,stroke-width:3px,color:#000
    style Gate fill:#ffe082,stroke:#f57c00,stroke-width:3px,color:#000
    style Pass fill:#4caf50,stroke:#1b5e20,stroke-width:3px,color:#000
    style Concerns fill:#ffc107,stroke:#f57f17,stroke-width:3px,color:#000
    style Fail fill:#f44336,stroke:#b71c1c,stroke-width:3px,color:#000
    style Waived fill:#9c27b0,stroke:#4a148c,stroke-width:3px,color:#000

```

**Nota de numeração de fase:** BMad utiliza uma metodologia de 4 fases com fase 1 opcional e pré-requisito de documentação:

- **Documentação** (Opcional para brownfield): Pré-requisito usando `*document-project`
- **Fase 1** (Opcional): Descoberta/Análise (`*brainstorm`, `*research`, `*product-brief`)
- **Fase 2** (obrigatório): Planning (`*prd` cria PRD com FRs/NFRs)
- **Fase 3** (dependente da faixa): Solução (`*architecture` → `*test-design` (nível do sistema) → `*create-epics-and-stories` → EA: `*framework`, `*ci` → `*implementation-readiness`)
- **Fase 4** (necessária): Implementation (`*sprint-planning` → per-epic: `*test-design` → per-story: fluxos de trabalho dev)

**workflows TEA:**`*framework` e `*ci` funcionam uma vez na Fase 3 após a arquitetura. `*test-design` é**modo dual**:

- **Nível do sistema (Fase 3):** Executar imediatamente após a redacção da arquitectura/ADR para produzir `test-