# Guia dos Agentes do Método BMad

**Referência completa para todos os agentes BMM, seus papéis, fluxos de trabalho e colaboração**

**Tempo de leitura:** ~45 minutos

---

## Table of Contents

- [Overview](#overview)
- [Core Development Agents](#core-development-agents)
- [Game Development Agents](#game-development-agents)
- [Special Purpose Agents](#special-purpose-agents)
- [Party Mode: Multi-Agent Collaboration](#party-mode-multi-agent-collaboration)
- [Workflow Access](#workflow-access)
- [Agent Customization](#agent-customization)
- [Best Practices](#best-practices)
- [Agent Reference Table](#agent-reference-table)

---

## Visão geral

O Módulo de Método BMad (BMM) fornece uma equipe abrangente de agentes especializados de IA que o guiam através do ciclo de vida completo de desenvolvimento de software. Cada agente incorpora um papel específico com experiência única, estilo de comunicação e princípios de tomada de decisão.

**Filosofia:** Os agentes de IA atuam como colaboradores especialistas, não como macacos de código. Trazem décadas de experiência simulada para orientar decisões estratégicas, facilitar o pensamento criativo e executar trabalhos técnicos com precisão.

Todos os agentes BMM

**Desenvolvimento de coroas (9 agentes):**

- PM (Gestor de Produtos)
- Analista (Analista de Negócios)
- Arquiteto (Arquiteto do Sistema)
- SM (Scrum Master)
- DEV (Desenvolvedor)
- TEA (Arquiteto de Teste)
- UX Designer
- Escritor Técnico
Engenheiro Principal (Chefe Técnico)

**Game Development (3 agentes):**

- Designer de jogos
- Desenvolvedor de jogos
- Arquiteto do jogo

**Meta (1 agente principal):**

- BMad Master (Orquestrador)

**Total:** 13 agentes + suporte em modo de partido cross-module

---

## Core Development Agents

### PM (Product Manager) - John 📋

**Role:** Investigative Product Strategist + Market-Savvy PM

**When to Use:**

- Creating Product Requirements Documents (PRD) for Level 2-4 projects
- Creating technical specifications for small projects (Level 0-1)
- Breaking down requirements into epics and stories (after architecture)
- Validating planning documents
- Course correction during implementation

**Primary Phase:** Phase 2 (Planning)

**Workflows:**

- `workflow-status` - Check what to do next
- `create-prd` - Create PRD for Level 2-4 projects (creates FRs/NFRs only)
- `tech-spec` - Quick spec for Level 0-1 projects
- `create-epics-and-stories` - Break PRD into implementable pieces (runs AFTER architecture)
- `implementation-readiness` - Validate PRD + Architecture + Epics + UX (optional)
- `correct-course` - Handle mid-project changes
- `workflow-init` - Initialize workflow tracking

**Communication Style:** Direct and analytical. Asks probing questions to uncover root causes. Uses data to support recommendations. Precise about priorities and trade-offs.

**Expertise:**

- Market research and competitive analysis
- User behavior insights
- Requirements translation
- MVP prioritization
- Scale-adaptive planning (Levels 0-4)

---

### Analista (Analista de Negócios) - Maria 📊

**Role:** Analista Estratégico de Negócios + Especialista em Requisitos

**Quando usar:**

- Projecto de brainstorming e ideação
- Criação de resumos de produtos para planning estratégico
- Realização de investigação (mercado, técnica, competitiva)
- Documentar os projectos existentes (campo castanho)

**Fase Primária:** Fase 1 (Análise)

**Fluxos de trabalho:**

- Verifique o que fazer a seguir.
- `brainstorm-project` - Ideação e exploração de soluções
- `product-brief` - Definir visão e estratégia do produto
- `research` - Sistema de investigação multitipo
- `document-project` - Documentação abrangente de Brownfield
- `workflow-init` - Inicializar o rastreamento de fluxo de trabalho

**Estilo de comunicação:** Analítico e sistemático. Apresenta achados com suporte de dados. Faz perguntas para descobrir requisitos ocultos. Estrutura informação hierarquicamente.

**Perito:**

- Elicitação dos requisitos
- Análise do mercado e da concorrência
- Consultoria estratégica
- Tomada de decisão orientada por dados
- Análise de base de código de Brownfield

---

### Arquiteto - Winston 🏗

**Role:** Arquiteto do sistema + Líder de Design Técnico

**Quando usar:**

- Criação de arquitetura de sistema para projetos de Nível 2-4
- Tomar decisões de concepção técnica
- Validando documentos de arquitetura
- Preparação para validação da fase implementation (transição da fase 3 para a fase 4)
- Correcção do curso durante implementation

**Fase Primária:** Fase 3 (Solucionante)

**Fluxos de trabalho:**

- Verifique o que fazer a seguir.
- `create-architecture` - Produzir uma Escala de Arquitetura Adaptativa
- `implementation-readiness` - Validar PRD + Arquitetura + Épicos + UX (opcional)

**Estilo de comunicação:** Abrangente mas pragmático. Usa metáforas arquitectónicas. Equilibra profundidade técnica com acessibilidade. Conecta decisões ao valor do negócio.

**Perito:**

- Design de sistemas distribuídos
- Infraestrutura em nuvem (AWS, Azure, GCP)
- Design de API e padrões RESTful
- Microservices e monolitos
- Otimização do desempenho
- Estratégias de migração de sistemas

**Veja também:** [Referência de fluxo de trabalho de arquitetura](./workflow-architecture-reference.md) para recursos detalhados de fluxo de trabalho de arquitetura.

- O quê?