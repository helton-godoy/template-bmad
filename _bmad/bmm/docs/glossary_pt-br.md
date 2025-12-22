# Glossário BMM

Referência terminologia abrangente para o Módulo Método BMad.

---

## Navigation

- [Core Concepts](#core-concepts)
- [Scale and Complexity](#scale-and-complexity)
- [Planning Documents](#planning-documents)
- [Workflow and Phases](#workflow-and-phases)
- [Agents and Roles](#agents-and-roles)
- [Status and Tracking](#status-and-tracking)
- [Project Types](#project-types)
- [Implementation Terms](#implementation-terms)

---

## Conceitos Principais

### BMM (módulo de método BMad)

Sistema de orquestração principal para o desenvolvimento ágil orientado por IA, fornecendo gerenciamento abrangente do ciclo de vida através de agentes especializados e fluxos de trabalho.

### Método BMad

A metodologia completa para o desenvolvimento de software assistido por IA, abrangendo planning, arquitetura, implementation e fluxos de trabalho de garantia de qualidade que se adaptam à complexidade do projeto.

### Sistema adaptativo à escala

A orquestração inteligente do fluxo de trabalho do BMad Method que ajusta automaticamente a profundidade do planning, os requisitos de documentação e os processos implementation baseados nas necessidades do projeto através de três faixas planning distintas (Quick Flow, BMad Method, Enterprise Method).

### Agente

Uma personalidade de IA especializada com experiência específica (PM, Arquiteto, SM, DEV, TEA) que orienta os usuários através de fluxos de trabalho e cria entregables. Os agentes têm recursos definidos, estilos de comunicação e acesso ao fluxo de trabalho.

### Fluxo de trabalho

Um processo orientado em várias etapas que orquestra atividades de agentes de IA para produzir entregas específicas. Os fluxos de trabalho são interativos e se adaptam ao contexto do usuário.

---

## Scale and Complexity

### Quick Flow Track

Fast implementation track using tech-spec planning only. Best for bug fixes, small features, and changes with clear scope. Typical range: 1-15 stories. No architecture phase needed. Examples: bug fixes, OAuth login, search features.

### BMad Method Track

Full product planning track using PRD + Architecture + UX. Best for products, platforms, and complex features requiring system design. Typical range: 10-50+ stories. Examples: admin dashboards, e-commerce platforms, SaaS products.

### Enterprise Method Track

Extended enterprise planning track adding Security Architecture, DevOps Strategy, and Test Strategy to BMad Method. Best for enterprise requirements, compliance needs, and multi-tenant systems. Typical range: 30+ stories. Examples: multi-tenant platforms, compliance-driven systems, mission-critical applications.

### Planning Track

The methodology path (Quick Flow, BMad Method, or Enterprise Method) chosen for a project based on planning needs, complexity, and requirements rather than story count alone.

**Note:** Story counts are guidance, not definitions. Tracks are determined by what planning the project needs, not story math.

---

## Planning Documentos

### Tech-Spec (Especificação técnica)

**Apenas a faixa de fluxo rápido.** Plano técnico abrangente criado antecipadamente que serve como o principal documento planning para pequenas alterações ou funcionalidades. Contém instrução de problema, abordagem de solução, mudanças de nível de arquivo, detecção de pilha (brownfield), estratégia de teste e recursos do desenvolvedor.

### PRD (Documento dos requisitos do produto)

**Método BMad/Tracks da empresa.**Documento planning de nível de produto contendo visão, objetivos, Requisitos Funcionais (FRs), Requisitos Não Funcionais (NFRs), critérios de sucesso e considerações de UX. Substitui o tech-spec para projetos maiores que necessitam do produto planning.**V6 Nota:** PRD foca no que construir (requisitos). Épico+ Histórias são criadas separadamente depois da arquitetura através do fluxo de trabalho create-epics-and-stories.

### Documento de Arquitetura

**Método BMad/Tracks da empresa.** Documento de design de todo o sistema que define estrutura, componentes, interações, modelos de dados, padrões de integração, segurança, desempenho e implantação.

**Scale-Adaptive:** Escalas de complexidade de arquitetura com pista - BMad Method é leve a moderada, Enterprise Method é abrangente com estratégias de segurança/devops/teste.

### Épicos

Grupos de recursos de alto nível que contêm várias histórias relacionadas. Normalmente entre 5-15 histórias cada e representam uma funcionalidade coesa (por exemplo, "User Autentication Epic").

### Resumo do produto

Documento estratégico opcional planning criado na Fase 1 (Análise) que captura visão de produto, contexto de mercado, necessidades do usuário e requisitos de alto nível antes de detalhada planning.

### GDD (Documento de Desenho do Jogo)

Desenvolvimento de jogos equivalente ao PRD, criado pelo agente Game Designer para projetos de jogos.

---

## Fluxo de trabalho e fases

### Fase 0: Documentação (pré-requisito)

**Fase condicional para projetos de brownfield.** Cria documentação abrangente de base de código antes do planning. Só é exigido se a documentação existente for insuficiente para os agentes de IA.

### Fase 1: Análise (Opcional)

Fase de descoberta e pesquisa, incluindo brainstorming, fluxos de trabalho de pesquisa e criação breve de produtos. Opcional para Fluxo Rápido, recomendado para Método BMad, necessário para Método Enterprise.

### Fase 2: Planning (obrigatório)

**Sempre necessário.** Cria requir formal