# Fluxos de Trabalho de Análise BMM (Fase 1)

## Visão geral

Os fluxos de trabalho de fase 1 (Análise) são ferramentas de exploração e descoberta **opcional** que ajudam a validar ideias, compreender mercados e gerar contexto estratégico antes do início do planning.

**Princípio chave:** Os fluxos de trabalho de análise ajudam você a pensar estrategicamente antes de se comprometer com o implementation. Ignora-os se as tuas exigências já estão claras.

**Quando utilizar:** Iniciando novos projetos, explorando oportunidades, validando o ajuste do mercado, gerando ideias, entendendo espaços de problemas.

**Quando saltar:** Continuando projetos existentes com requisitos claros, recursos bem definidos com soluções conhecidas, restrições rigorosas onde a descoberta está completa.

---

## Phase 1 Analysis Workflow Overview

Phase 1 Analysis consists of three categories of optional workflows:

### Discovery & Ideation (Optional)

- **brainstorm-project** - Multi-track solution exploration for software projects
- **brainstorm-game** - Game concept generation (coming soon)

### Research & Validation (Optional)

- **research** - Market, technical, competitive, user, domain, and AI research
- **domain-research** - Industry-specific deep dive research

### Strategic Capture (Recommended for Greenfield)

- **product-brief** - Product vision and strategy definition

These workflows feed into Phase 2 (Planning) workflows, particularly the `prd` workflow.

---

## Referência rápida

| Workflow               | Agent   | Required    | Purpose                                                        | Output                       |
| ---------------------- | ------- | ----------- | -------------------------------------------------------------- | ---------------------------- |
| **brainstorm-project** | Analyst | No          | Explore solution approaches and architectures                  | Solution options + rationale |
| **research**           | Analyst | No          | Multi-type research (market/technical/competitive/user/domain) | Research reports             |
| **product-brief**      | Analyst | Recommended | Define product vision and strategy (interactive)               | Product Brief document       |

---

## Workflow Descriptions

### brainstorm-project

**Purpose:** Generate multiple solution approaches through parallel ideation tracks (architecture, UX, integration, value).

**Agent:** Analyst

**When to Use:**

- Unclear technical approach with business objectives
- Multiple solution paths need evaluation
- Hidden assumptions need discovery
- Innovation beyond obvious solutions

**Key Outputs:**

- Architecture proposals with trade-off analysis
- Value framework (prioritized features)
- Risk analysis (dependencies, challenges)
- Strategic recommendation with rationale

**Example:** "We need a customer dashboard" → Options: Monolith SSR (faster), Microservices SPA (scalable), Hybrid (balanced) with recommendation.

---

### investigação

**Proporção:** Sistema abrangente de pesquisa multi-tipo consolidando análise de mercado, técnica, competitiva, usuário e domínio.

**Agente:** Analista

**Tipos de investigação:**

| Type            | Purpose                                                | Use When                            |
| --------------- | ------------------------------------------------------ | ----------------------------------- |
| **market**      | TAM/SAM/SOM, competitive analysis                      | Need market viability validation    |
| **technical**   | Technology evaluation, ADRs                            | Choosing frameworks/platforms       |
| **competitive** | Deep competitor analysis                               | Understanding competitive landscape |
| **user**        | Customer insights, personas, JTBD                      | Need user understanding             |
| **domain**      | Industry deep dives, trends                            | Understanding domain/industry       |
| **deep_prompt** | Generate AI research prompts (ChatGPT, Claude, Gemini) | Need deeper AI-assisted research    |

**Características-chave:**

- Pesquisa web em tempo real
- Múltiplas estruturas analíticas (Cinco Forças de Porter, SWOT, ciclo de vida de adoção de tecnologia)
- Otimização específica da plataforma para o tipo de profundidade prompt
- Profundidade de pesquisa configurável (rápido/padrão/compreensivo)

**Exemplo (mercado):** "Ferramenta de gerenciamento de projetos SaaS" → TAM $50B, SAM $5B, SOM $50M, principais concorrentes (Asana, segunda-feira), recomendação de posicionamento.

---

### Brief-produto

**Purpose:** Breve criação interativa de produtos que orienta definição estratégica de visão de produtos.

**Agente:** Analista

**Quando usar:**

- Iniciando nova iniciativa produto/característica principal
- Alinhar as partes interessadas antes do planning detalhado
- Transição da exploração para a estratégia
- Precisa de documentação de produto de nível executivo

**Modes:**

- **Modo Interactivo** (recomendado): Desenvolvimento colaborativo passo a passo com questões de sondagem
- **YOLO Mode**: A IA gera rascunho completo do contexto, depois refinamento iterativo

**Saídas-chave:**

- Resumo executivo
- Declaração de problema com provas
- Proposta soluti