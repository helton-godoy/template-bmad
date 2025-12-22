# Fluxos de trabalho de solução BMM (Fase 3)

## Visão geral

Os fluxos de trabalho da fase 3 (Solutioning) traduzem **o que**para construir (do Planning) em**como** para o construir (design técnico). Esta fase evita conflitos de agentes em projetos multi-épicos documentando decisões arquitetônicas antes do início do implementation.

**Princípio chave:** Tornar as decisões técnicas explícitas e documentadas para que todos os agentes implementem de forma consistente. Evite um agente escolhendo REST enquanto outro escolhe GraphQL.

**Requerido para:** BMad Method (projectos complexos), Enterprise Method

**Opcional para:** Método BMad (projetos simples), Quick Flow (skip inteiramente)

---

## Phase 3 Solutioning Workflow Overview

Phase 3 Solutioning has different paths based on the planning track selected:

### Quick Flow Path

- From Planning: tech-spec complete
- Action: Skip Phase 3 entirely
- Next: Phase 4 (Implementation)

### BMad Method & Enterprise Path

- From Planning: PRD with FRs/NFRs complete
- Optional: create-ux-design (if UX is critical)
- Required: architecture - System design with ADRs
- Required: create-epics-and-stories - Break requirements into implementable stories
- Required: implementation-readiness - Gate check validation
- Enterprise additions: Optional security-architecture and devops-strategy (future workflows)

### Gate Check Results

- **PASS** - All criteria met, proceed to Phase 4
- **CONCERNS** - Minor gaps identified, proceed with caution
- **FAIL** - Critical issues, must resolve before Phase 4

---

## Referência rápida

| Workflow                     | Agent       | Track                    | Purpose                                      |
| ---------------------------- | ----------- | ------------------------ | -------------------------------------------- |
| **create-ux-design**         | UX Designer | BMad Method, Enterprise  | Optional UX design (after PRD, before arch)  |
| **architecture**             | Architect   | BMad Method, Enterprise  | Technical architecture and design decisions  |
| **create-epics-and-stories** | PM          | BMad Method, Enterprise  | Break FRs/NFRs into epics after architecture |
| **implementation-readiness** | Architect   | BMad Complex, Enterprise | Validate planning/solutioning completeness   |

**Quando Ir Solução:**

- **Quick Flow:** Mudanças simples não precisam de arquitetura → Pular para a Fase 4

**Quando a solução é necessária:**

- **Método BMad:** Os projectos multi-épicos precisam de arquitectura para evitar conflitos
- **Enterprise:** O mesmo que BMad Method, além de fluxos de trabalho estendidos opcionais (arquitectura de teste, arquitetura de segurança, estratégia devops) adicionado após arquitetura mas ANTES verificação de portão

---

## Why Solutioning Matters

### The Problem Without Solutioning

```
Agent 1 implements Epic 1 using REST API
Agent 2 implements Epic 2 using GraphQL
Result: Inconsistent API design, integration nightmare

```

### The Solution With Solutioning

```
architecture workflow decides: "Use GraphQL for all APIs"
All agents follow architecture decisions
Result: Consistent implementation, no conflicts

```

### Solutioning vs Planning

| Aspect   | Planning (Phase 2)      | Solutioning (Phase 3)             |
| -------- | ----------------------- | --------------------------------- |
| Question | What and Why?           | How? Then What units of work?     |
| Output   | FRs/NFRs (Requirements) | Architecture + Epics/Stories      |
| Agent    | PM                      | Architect → PM                    |
| Audience | Stakeholders            | Developers                        |
| Document | PRD (FRs/NFRs)          | Architecture + Epic Files         |
| Level    | Business logic          | Technical design + Work breakdown |

---

## Descrições do fluxo de trabalho

### arquitetura

**Proporção:** Tornar explícitas as decisões técnicas para prevenir conflitos de agentes. Produz um documento de arquitetura focado na decisão otimizado para consistência de IA.

**Agente:** Arquiteto

**Quando usar:**

- Projetos multi-épicos (BMad Complex, Enterprise)
- Questões técnicas transversais
- Vários agentes implementando diferentes partes
- A complexidade da integração existe
- As escolhas tecnológicas precisam de alinhamento

**Quando Ir:**

- Fluxo rápido (mudanças simples)
- Método BMad Simples com simples pilha de tecnologia
- Épico único com abordagem técnica clara

**Abordagem de Conversação Adaptiva:**

Isto NÃO é um preenchimento de modelo. O fluxo de trabalho da arquitetura:

1. **Descobre** necessidades técnicas através da conversação
2. **Propõe** opções arquitectónicas com trade-offs
3. Decisões **Documentos** que impedem conflitos de agentes
4. **Focos** sobre os pontos de decisão, não documentação exaustiva

**Saídas-chave:**

**architecture.md** contendo:

1. **Visão geral da arquitetura** - Contexto do sistema, princípios, estilo
2. **System Architecture** - Diagrama de alto nível, interações de componentes, padrões de comunicação
3. **Arquitectura de dados** - Projeto de banco de dados, gestão do estado, cache, fluxo de dados
4. **API Architecture** - Estilo API (REST/GraphQL/gRPC), autenticação, versionamento, manipulação de erros
5. **Arquitectura da amizade** (se