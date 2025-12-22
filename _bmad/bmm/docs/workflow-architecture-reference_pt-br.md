# Decisão Architecture Workflow - Referência técnica

**Módulo:** BMM (módulo de método BMAD)
**Tipo:** Solução de fluxo de trabalho

---

## Overview

The Decision Architecture workflow is a complete reimagining of how architectural decisions are made in the BMAD Method. Instead of template-driven documentation, this workflow facilitates an intelligent conversation that produces a **decision-focused architecture document** optimized for preventing AI agent conflicts during implementation.

---

## Filosofia Principal

**O Problema**: Quando vários agentes de IA implementam diferentes partes de um sistema, tomam decisões técnicas conflitantes que levam a implementações incompatíveis.

**The Solution**: Um "contrato de coerência" que documenta todas as decisões técnicas críticas antecipadamente, garantindo que cada agente siga os mesmos padrões e use as mesmas tecnologias.

---

## Key Features

### 1. Starter Template Intelligence ⭐ NEW

- Discovers relevant starter templates (create-next-app, create-t3-app, etc.)
- Considers UX requirements when selecting templates (animations, accessibility, etc.)
- Searches for current CLI options and defaults
- Documents decisions made BY the starter template
- Makes remaining architectural decisions around the starter foundation
- First implementation story becomes "initialize with starter command"

### 2. Adaptive Facilitation

- Adjusts conversation style based on user skill level (beginner/intermediate/expert)
- Experts get rapid, technical discussions
- Beginners receive education and protection from complexity
- Everyone produces the same high-quality output

### 3. Dynamic Version Verification

- NEVER trusts hardcoded version numbers
- Uses WebSearch to find current stable versions
- Verifies versions during the conversation
- Documents only verified, current versions

### 4. Intelligent Discovery

- No rigid project type templates
- Analyzes PRD to identify which decisions matter for THIS project
- Uses knowledge base of decisions and patterns
- Scales to infinite project types

### 5. Collaborative Decision Making

- Facilitates discussion for each critical decision
- Presents options with trade-offs
- Integrates advanced elicitation for innovative approaches
- Ensures decisions are coherent and compatible

### 6. Consistent Output

- Structured decision collection during conversation
- Strict document generation from collected decisions
- Validated against hard requirements
- Optimized for AI agent consumption

---

## Estrutura do fluxo de trabalho

```
Step 0: Validate workflow and extract project configuration
Step 0.5: Validate workflow sequencing
Step 1: Load PRD (with FRs/NFRs) and understand project context
Step 2: Discover and evaluate starter templates ⭐ NEW
Step 3: Adapt facilitation style and identify remaining decisions
Step 4: Facilitate collaborative decision making (with version verification)
Step 5: Address cross-cutting concerns
Step 6: Define project structure and boundaries
Step 7: Design novel architectural patterns (when needed) ⭐ NEW
Step 8: Define implementation patterns to prevent agent conflicts
Step 9: Validate architectural coherence
Step 10: Generate decision architecture document (with initialization commands)
Step 11: Validate document completeness
Step 12: Final review and update workflow status

```

---

## Files in This Workflow

- **workflow.yaml** - Configuration and metadata
- **instructions.md** - The adaptive facilitation flow
- **decision-catalog.yaml** - Knowledge base of all architectural decisions
- **architecture-patterns.yaml** - Common patterns identified from requirements
- **pattern-categories.csv** - Pattern principles that teach LLM what needs defining
- **checklist.md** - Validation requirements for the output document
- **architecture-template.md** - Strict format for the final document

---

## Como é diferente da arquitetura antiga

| Aspect               | Old Workflow                                 | New Workflow                                    |
| -------------------- | -------------------------------------------- | ----------------------------------------------- |
| **Approach**         | Template-driven                              | Conversation-driven                             |
| **Project Types**    | 11 rigid types with 22+ files                | Infinite flexibility with intelligent discovery |
| **User Interaction** | Output sections with "Continue?"             | Collaborative decision facilitation             |
| **Skill Adaptation** | One-size-fits-all                            | Adapts to beginner/intermediate/expert          |
| **Decision Making**  | Late in process (Step 5)                     | Upfront and central focus                       |
| **Output**           | Multiple documents including faux tech-specs | Single decision-focused architecture            |
| **Time**             | Confusing and slow                           | 30-90 minutes depending on skill level          |
• **Elicitação**