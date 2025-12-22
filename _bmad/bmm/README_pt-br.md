# BMM - Módulo Método BMad

Sistema de orquestração principal para o desenvolvimento ágil orientado por IA, fornecendo gerenciamento abrangente do ciclo de vida através de agentes especializados e fluxos de trabalho.

---

## 📚 Complete Documentation

👉 **[BMM Documentation Hub](./docs/README.md)** - Start here for complete guides, tutorials, and references

**Quick Links:**

- **[Quick Start Guide](./docs/quick-start.md)** - New to BMM? Start here (15 min)
- **[Agents Guide](./docs/agents-guide.md)** - Meet your 12 specialized AI agents (45 min)
- **[Scale Adaptive System](./docs/scale-adaptive-system.md)** - How BMM adapts to project size (42 min)
- **[FAQ](./docs/faq.md)** - Quick answers to common questions
- **[Glossary](./docs/glossary.md)** - Key terminology reference

---

## 🏗 Estrutura do Módulo

Este módulo contém:

```
bmm/
├── agents/          # 12 specialized AI agents (PM, Architect, SM, DEV, TEA, etc.)
├── workflows/       # 34 workflows across 4 phases + testing
├── teams/           # Pre-configured agent groups
├── tasks/           # Atomic work units
├── testarch/        # Comprehensive testing infrastructure
└── docs/            # Complete user documentation

```

### Agente Roster

**Core Development:** PM, Analista, Arquiteto, SM, DEV, TEA, UX Designer, Escritor Técnico
**Game Development:** Designer de jogos, desenvolvedor de jogos, arquiteto de jogos
**Orchestration:** BMad Master (do núcleo)

👉 **[Guia de Agentes Completos](./docs/agents-guide.md)** - Funções, fluxos de trabalho e quando usar cada agente

### Fases de fluxo de trabalho

**Fase 0:** Documentação (apenas campo marrom)
**Fase 1:** Análise (opcional) - 5 fluxos de trabalho
**Fase 2:** Planning (obrigatório) - 6 fluxos de trabalho
**Fase 3:** Solução (Nível 3-4) - 2 fluxos de trabalho
**Fase 4:** Implementation (iterativa) - 10 fluxos de trabalho
**Testing:** Garantia de qualidade (paralela) - 9 fluxos de trabalho

👉 **[Guias de fluxo de trabalho](./docs/README.md#-workflow-guides)** - Documentação detalhada para cada fase

---

## 🚀 Getting Started

**New Project:**

```bash

# Install BMM
npx bmad-method@alpha install

# Load Analyst agent in your IDE, then:
*workflow-init

```

**Existing Project (Brownfield):**

```bash

# Document your codebase first
*document-project

# Then initialize
*workflow-init

```

👉 **[Quick Start Guide](./docs/quick-start.md)** - Complete setup and first project walkthrough

---

## 🎯 Conceitos-chave

### Desenho Adaptativo à Escala

BMM se ajusta automaticamente à complexidade do projeto (Níveis 0-4):

- **Nível 0-1:** Fluxo de especificações rápidas para correções de erros e pequenas características
- **Nível 2:** PRD com arquitectura opcional
- **Nível 3-4:** PRD completo + arquitetura abrangente

👉 **[Scale Adaptive System](./docs/scale-adaptive-system.md)** - Discriminação completa do nível

### Story-Centric Implementation

Histórias passam por um ciclo de vida definido: `backlog → ready-for-dev → in-progress → review → done`

Just-in-time contexto épico e contexto de história fornecer experiência exata quando necessário.

👉 **[Implementation Workflows](./docs/workflows-implementation.md)** - Guia completo do ciclo de vida da história

### Colaboração Multi-Agente

Use o modo de festa para envolver todos os 19+ agentes (de BMM, CIS, BMB, módulos personalizados) em discussões de grupo para decisões estratégicas, brainstorming criativo e resolução de problemas complexos.

👉 **[Guia do modo de festa](./docs/party-mode.md)** - Como orquestrar a colaboração multiagente

---

## 📖 Additional Resources

- **[Brownfield Guide](./docs/brownfield-guide.md)** - Working with existing codebases
- **[Quick Spec Flow](./docs/quick-spec-flow.md)** - Fast-track for Level 0-1 projects
- **[Enterprise Agentic Development](./docs/enterprise-agentic-development.md)** - Team collaboration patterns
- **[Troubleshooting](./docs/troubleshooting.md)** - Common issues and solutions
- **[IDE Setup Guides](../../../docs/ide-info/)** - Configure Claude Code, Cursor, Windsurf, etc.

---

## 🤝 Comunidade

- **[Discord](https://discord.gg/gk8jAdXWmj)** - Get help, share feedback (#general-dev, #bugs-issues)
- **[Questões do GitHub](https://github.com/bmad-code-org/BMAD-METHOD/issues)** - Report bugs or request features
- **[YouTube](https://www.youtube.com/@BMadCode)** - Video tutorials and walkthroughs

---

**Ready to build?** → [Start with the Quick Start Guide](./docs/quick-start.md)
