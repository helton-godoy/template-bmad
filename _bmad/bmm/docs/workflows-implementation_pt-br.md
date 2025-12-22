# BMM Implementation Fluxos de trabalho (Fase 4)

## Visão geral

Os fluxos de trabalho da Fase 4 (Implementation) gerenciam o ciclo de desenvolvimento iterativo baseado em sprint usando um fluxo de trabalho “centrado em história” onde cada história passa por um ciclo de vida definido desde a criação até a conclusão.

**Princípio chave:** Uma história de cada vez, movê-la através de todo o ciclo de vida antes de começar o próximo.

---

## Complete Workflow Context

Phase 4 is the final phase of the BMad Method workflow. To see how implementation fits into the complete methodology:

The BMad Method consists of four phases working in sequence:

1. **Phase 1 (Analysis)** - Optional exploration and discovery workflows
2. **Phase 2 (Planning)** - Required requirements definition using scale-adaptive system
3. **Phase 3 (Solutioning)** - Technical architecture and design decisions
4. **Phase 4 (Implementation)** - Iterative sprint-based development with story-centric workflow

Phase 4 focuses on the iterative epic and story cycles where stories are implemented, reviewed, and completed one at a time.

For a visual representation of the complete workflow, see: [workflow-method-greenfield.excalidraw](./images/workflow-method-greenfield.excalidraw)

---

## Referência rápida

| Workflow            | Agent | When                  | Purpose                               |
| ------------------- | ----- | --------------------- | ------------------------------------- |
| **sprint-planning** | SM    | Once at Phase 4 start | Initialize sprint tracking file       |
| **create-story**    | SM    | Per story             | Create next story from epic backlog   |
| **dev-story**       | DEV   | Per story             | Implement story with tests            |
| **code-review**     | DEV   | Per story             | Senior dev quality review             |
| **retrospective**   | SM    | After epic complete   | Review lessons and extract insights   |
| **correct-course**  | SM    | When issues arise     | Handle significant mid-sprint changes |

---

## Agent Roles

### SM (Scrum Master) - Primary Implementation Orchestrator

**Workflows:** sprint-planning, create-story, retrospective, correct-course

**Responsibilities:**

- Initialize and maintain sprint tracking
- Create stories from epic backlog
- Handle course corrections when issues arise
- Facilitate retrospectives after epic completion
- Orchestrate overall implementation flow

### DEV (Developer) - Implementation and Quality

**Workflows:** dev-story, code-review

**Responsibilities:**

- Implement stories with tests
- Perform senior developer code reviews
- Ensure quality and adherence to standards
- Complete story implementation lifecycle

---

## Estados do ciclo de vida da história

As histórias passam por estes estados no ficheiro de status sprint:

1. **TODO** - História identificada mas não iniciada
2. **IN PROGRESS** - História a ser implementada (criação-história → dev-história)
3. **REALIZAÇÃO PARA REVISÃO** - Implementation completa, aguardando revisão de código
4. **DEUS** - Aceito e completo

---

## Typical Sprint Flow

### Sprint 0 (Planning Phase)

- Complete Phases 1-3 (Analysis, Planning, Solutioning)
- PRD/GDD + Architecture complete
- **V6: Epics+Stories created via create-epics-and-stories workflow (runs AFTER architecture)**

### Sprint 1+ (Implementation Phase)

**Start of Phase 4:**

1. SM runs `sprint-planning` (once)

**Per Epic:**

- Epic context and stories are already prepared from Phase 3

**Per Story (repeat until epic complete):**

1. SM runs `create-story`
2. DEV runs `dev-story`
3. DEV runs `code-review`
4. If code review fails: DEV fixes issues in `dev-story`, then re-runs `code-review`

**After Epic Complete:**

- SM runs `retrospective`
- Move to next epic

**As Needed:**

- Run `sprint-status` anytime in Phase 4 to inspect sprint-status.yaml and get the next implementation command
- Run `workflow-status` for cross-phase routing and project-level paths
- Run `correct-course` if significant changes needed

---

## Princípios-chave

### Uma história de cada vez

Complete o ciclo de vida completo de cada história antes de começar o próximo. Isso evita a mudança de contexto e garante qualidade.

### Gates de qualidade

Cada história passa pelo `code-review` antes de ser marcada done. Sem excepções.

### Monitoramento contínuo

O arquivo `sprint-status.yaml` é a única fonte de verdade para todo o progresso implementation.

---

### (Método BMad / Empresa)

```
PRD (PM) → Architecture (Architect)
  → create-epics-and-stories (PM)  ← V6: After architecture!
  → implementation-readiness (Architect)
  → sprint-planning (SM, once)
  → [Per Epic]:
      → story loop (SM/DEV)
      → retrospective (SM)
  → [Next Epic]
Current Phase: 4 (Implementation)
Current Epic: Epic 1 (Authentication)
Current Sprint: Sprint 1

Next Story: Story 1.3 (Email Verification)
Status: TODO
Dependencies: Story 1.2 (DONE) ✅

**Recommendation:** Run `create-story` to generate Story 1.3

After create-story:
1. Run dev-story
2. Run code-review
3. Update sprint-status.yaml to mark story done

```

Ver: [instrução de estado de fluxo de trabalho