# Fluxos de Trabalho de Planejamento BMM (Fase 2)

## Visão Geral

Fluxos de trabalho da Fase 2 (Planejamento) são **obrigatórios** para todos os projetos. Eles transformam visão estratégica em requisitos acionáveis usando um **sistema adaptativo à escala** que seleciona automaticamente a profundidade de planejamento correta baseada na complexidade do projeto.

**Princípio chave:** Um ponto de entrada unificado (`workflow-init`) roteia inteligentemente para a metodologia de planejamento apropriada - de especificações técnicas rápidas a PRDs abrangentes.

**Quando usar:** Todos os projetos requerem planejamento. O sistema adapta a profundidade automaticamente baseada na complexidade.

---

## Visão Geral do Fluxo de Trabalho de Planejamento Fase 2

Planejamento Fase 2 usa um sistema adaptativo à escala com três trilhas:

### Quick Flow (Planejamento Simples)

- Entrada: `workflow-init` roteia baseado na complexidade do projeto
- Fluxo de trabalho: `tech-spec`
- Saída: Documento técnico com estrutura estória/épico
- Contagem de estória: 1-15 (típico)
- Próximo: Fase 4 (Implementação) - pula Fase 3

### Método BMad (Recomendado)

- Entrada: `workflow-init` roteia baseado na complexidade do projeto
- Fluxos de trabalho: `prd` → (opcional) `create-ux-design`
- Saída: PRD com RFs/RNFs
- Contagem de estória: 10-50+ (típico)
- Próximo: Fase 3 (Solução) → Fase 4

### Método Enterprise

- Planejamento: Mesmo que Método BMad (fluxo `prd`)
- Solução: Fluxos de trabalho Fase 3 estendidos (Arquitetura + Segurança + DevOps)
- Contagem de estória: 30+ (típico)
- Próximo: Fase 4

O fluxo de trabalho `correct-course` pode ser usado a qualquer momento para mudanças de requisitos significativas.

---

## Referência Rápida

| Fluxo de Trabalho    | Agente      | Trilha                  | Propósito                                       | Estórias Típicas |
| -------------------- | ----------- | ----------------------- | ----------------------------------------------- | ---------------- |
| **workflow-init**    | PM/Analista | Todas                   | Ponto de entrada: descoberta + roteamento       | N/A              |
| **tech-spec**        | PM          | Quick Flow              | Documento técnico → Estória ou Épico+Estórias   | 1-15             |
| **prd**              | PM          | Método BMad, Enterprise | PRD Estratégico com RFs/RNFs (sem quebra épico) | 10-50+           |
| **create-ux-design** | Designer UX | Método BMad, Enterprise | Especificação UX opcional (após PRD)            | N/A              |
| **correct-course**   | PM/SM       | Todas                   | Mudanças de requisitos no meio do fluxo         | N/A              |

**Nota:** Contagens de estória são orientação. Melhoria V6: Épicos+Estórias são criados APÓS arquitetura para melhor qualidade.

---

## Sistema de Planejamento Adaptativo à Escala

BMM usa três trilhas de planejamento distintas que se adaptam à complexidade do projeto:

### Trilha 1: Quick Flow

**Melhor Para:** Correções de bug, features simples, escopo claro, melhorias

**Planejamento:** Tech-spec apenas → Implementação

**Tempo:** Horas a 1 dia

**Contagem de Estória:** Tipicamente 1-15 (orientação)

**Documentos:** tech-spec.md + arquivos de estória

**Exemplo:** "Corrigir bug de autenticação", "Adicionar login social OAuth"

---

### Trilha 2: Método BMad (RECOMENDADO)

**Melhor Para:** Produtos, plataformas, features complexas, múltiplos épicos

**Planejamento:** PRD + Arquitetura → Implementação

**Tempo:** 1-3 dias

**Contagem de Estória:** Tipicamente 10-50+ (orientação)

**Documentos:** PRD.md (RFs/RNFs) + architecture.md + epics.md + arquivos de épico

**Greenfield:** Resumo de Produto (opcional) → PRD (RFs/RNFs) → UX (opcional) → Arquitetura → Épicos+Estórias → Implementação

**Brownfield:** document-project → PRD (RFs/RNFs) → Arquitetura (recomendado) → Épicos+Estórias → Implementação

**Exemplo:** "Dashboard de cliente", "Plataforma e-commerce", "Adicionar busca a app existente"

**Por que Arquitetura para Brownfield?** Destila contexto de base de código massiva em design de solução focado para seu projeto específico.

---

### Trilha 3: Método Enterprise

**Melhor Para:** Requisitos enterprise, multi-tenant, compliance, sensível à segurança

**Planejamento (Fase 2):** Usa planejamento Método BMad (PRD com RFs/RNFs)

**Solução (Fase 3):** Fluxos estendidos (Arquitetura + Segurança + DevOps + SecOps como adições opcionais) → Épicos+Estórias

**Tempo:** 3-7 dias total (1-3 dias planejamento + 2-4 dias solução estendida)

**Contagem de Estória:** Tipicamente 30+ (mas definido por necessidades enterprise)

**Documentos Fase 2:** PRD.md (RFs/RNFs)

**Documentos Fase 3:** architecture.md + epics.md + arquivos de épico + security-architecture.md (opcional) + devops-strategy.md (opcional) + secops-strategy.md (opcional)

**Exemplo:** "SaaS multi-tenant", "Portal compatível com HIPAA", "Adicionar log de auditoria SOC2"

---

## Como Funciona a Seleção de Trilha

`workflow-init` guia você através de escolha educacional:

1. **Análise de Descrição** - Analisa descrição do projeto para complexidade
2. **Apresentação Educacional** - Mostra todas as três trilhas com trade-offs
3. **Recomendação** - Sugere trilha baseada em palavras-chave e contexto
4. **Escolha do Usuário** - Você seleciona a trilha que encaixa

O sistema guia mas nunca força. Você pode sobrescrever recomendações.

---

## Descrições de Fluxo de Trabalho

### workflow-init (Ponto de Entrada)

**Propósito:** Ponto de entrada único unificado para todo planejamento. Descobre necessidades de projeto e roteia inteligentemente para trilha apropriada.

**Agente:** PM (orquestra outros conforme necessário)

**Sempre Use:** Este é seu ponto de partida de planejamento. Não chame prd/tech-spec diretamente a menos que pulando descoberta.

**Processo:**

1. Descoberta (entender contexto, avaliar complexidade, identificar preocupações)
2. Decisão de Roteamento (determinar trilha, explicar racional, confirmar)
3. Executar Fluxo Alvo (invocar fluxo de planejamento, passar contexto)
4. Handoff (documentar decisões, recomendar próxima fase)

---

### tech-spec (Quick Flow)

**Propósito:** Especificação técnica leve para mudanças simples (trilha Quick Flow). Produz documento técnico e estrutura estória ou épico+estórias.

**Agente:** PM

**Quando Usar:**

- Correções de bug
- Adições de endpoint de API único
- Mudanças de configuração
- Adições de componente UI pequenos
- Regras de validação isoladas

**Saídas Chave:**

- **tech-spec.md** - Documento técnico contendo:
  - Declaração de problema e solução
  - Mudanças na árvore de fonte
  - Detalhes de implementação
  - Estratégia de teste
  - Critérios de aceite
- **Arquivo(s) de estória** - Estória única OU estrutura épico+estórias (1-15 estórias tipicamente)

**Pular Para Fase:** 4 (Implementação) - sem necessidade de arquitetura Fase 3

**Exemplo:** "Corrigir ponteiro nulo quando usuário não tem imagem de perfil" → Mudança de arquivo único, checagem de nulo, teste unitário, sem migração de DB.

---

### prd (Documento de Requisitos de Produto)

**Propósito:** PRD Estratégico com Requisitos Funcionais (RFs) e Requisitos Não-Funcionais (RNFs) para produtos de software (trilha Método BMad).

**Agente:** PM (com suporte de Arquiteto e Analista)

**Quando Usar:**

- Conjuntos de features médios a grandes
- Experiências de usuário multi-tela
- Lógica de negócio complexa
- Múltiplas integrações de sistema
- Entrega faseada requerida

**Estrutura Adaptativa à Escala:**

- **Leve:** RFs/RNFs focados, análise simplificada (10-15 páginas)
- **Padrão:** RFs/RNFs abrangentes, análise completa (20-30 páginas)
- **Abrangente:** RFs/RNFs extensivos, multi-fase, análise de stakeholder (30-50+ páginas)

**Saídas Chave:**

- PRD.md (requisitos completos com RFs e RNFs)

**Nota:** Melhoria V6 - PRD foca no QUE construir (requisitos). Épicos+Estórias são criados APÓS arquitetura via fluxo `create-epics-and-stories` para melhor qualidade.

**Integração:** Alimenta Arquitetura (Fase 3)

**Exemplo:** Checkout E-commerce → PRD com 15 RFs (conta usuário, gestão carrinho, fluxo pagamento) e 8 RNFs (performance, segurança, escalabilidade).

---

### create-ux-design (Design UX)

**Propósito:** Especificação UX para projetos onde experiência do usuário é o diferenciador primário (trilha Método BMad).

**Agente:** Designer UX

**Quando Usar:**

- UX é vantagem competitiva primária
- Fluxos de usuário complexos precisando de design thinking
- Padrões de interação inovadores
- Criação de design system
- Experiências críticas de acessibilidade

**Abordagem Colaborativa:**

1. Exploração visual (gerar múltiplas opções)
2. Decisões informadas (avaliar com necessidades do usuário)
3. Design colaborativo (refinar iterativamente)
4. Documentação viva (evolui com projeto)

**Saídas Chave:**

- ux-spec.md (especificação UX completa)
- Jornadas de usuário
- Wireframes e mockups
- Especificações de interação
- Design system (componentes, padrões, tokens)
- Quebra de épico (estórias UX)

**Integração:** Alimenta PRD ou atualiza épicos, então Arquitetura (Fase 3)

**Exemplo:** Redesign de Dashboard → Layout baseado em cards com toggle split-pane, 5 componentes card, 12 tokens de cor, grid responsivo, 3 épicos (Layout, Visualização, Acessibilidade).

---

### correct-course

**Propósito:** Lidar com mudanças de requisito significativas durante implementação (todas as trilhas).

**Agente:** PM, Arquiteto, ou SM

**Quando Usar:**

- Prioridades mudam no meio do projeto
- Novos requisitos emergem
- Ajustes de escopo necessários
- Bloqueadores técnicos requerem re-planejamento

**Processo:**

1. Analisar impacto da mudança
2. Propor soluções (continuar, pivotar, pausar)
3. Atualizar documentos afetados (PRD, épicos, estórias)
4. Re-rotear para implementação

**Integração:** Atualiza artefatos de planejamento, pode acionar revisão de arquitetura

---

## Guia de Decisão

### Qual Fluxo de Planejamento?

**Use `workflow-init` (Recomendado):** Deixe o sistema descobrir necessidades e rotear apropriadamente.

**Seleção Direta (Avançado):**

- **Correção de bug ou mudança única** → `tech-spec` (Quick Flow)
- **Produto de software** → `prd` (Método BMad)
- **Projeto inovação UX** → `create-ux-design` + `prd` (Método BMad)
- **Enterprise com compliance** → Escolha trilha em `workflow-init` → Método Enterprise

---

## Integração com Fase 3 (Solução)

Saídas de planejamento alimentam Solução:

| Saída de Planejamento | Entrada de Solução                 | Decisão de Trilha            |
| --------------------- | ---------------------------------- | ---------------------------- |
| tech-spec.md          | Pular Fase 3 → Fase 4 diretamente  | Quick Flow (sem arquitetura) |
| PRD.md                | **architecture** (Nível 3-4)       | Método BMad (recomendado)    |
| ux-spec.md            | **architecture** (design frontend) | Método BMad                  |
| Docs Enterprise       | **architecture** + segurança/ops   | Método Enterprise (obrigat.) |

**Pontos de Decisão Chave:**

- **Quick Flow:** Pula Fase 3 inteiramente → Fase 4 (Implementação)
- **Método BMad:** Fase 3 Opcional (simples), Fase 3 Obrigatória (complexo)
- **Enterprise:** Fase 3 Obrigatória (arquitetura + planejamento estendido)

Veja: [workflows-solutioning.md](./workflows-solutioning.md)

---

## Melhores Práticas

### 1. Sempre Comece com workflow-init

Deixe o ponto de entrada te guiar. Previne sobre-planejamento de features simples ou sub-planejamento de iniciativas complexas.

### 2. Confie na Recomendação

Se `workflow-init` sugere Método BMad, provavelmente há complexidade que você não considerou. Revise cuidadosamente antes de sobrescrever.

### 3. Itere nos Requisitos

Documentos de planejamento são vivos. Refine PRDs conforme aprende durante Solução e Implementação.

### 4. Envolva Stakeholders Cedo

Revise PRDs com stakeholders antes da Solução. Pegue desalinhamento cedo.

### 5. Foque no "O Que" Não "Como"

Planejamento define **o que** construir e **por que**. Deixe **como** (design técnico) para Fase 3 (Solução).

### 6. Document-Project Primeiro para Brownfield

Sempre rode `document-project` antes de planejar projetos brownfield. Agentes de IA precisam de contexto de base de código existente.

---

## Padrões Comuns

### Software Greenfield (Método BMad)

```
1. (Opcional) Análise: product-brief, research
2. workflow-init → roteia para prd
3. PM: fluxo prd
4. (Opcional) Designer UX: fluxo create-ux-design
5. → Fase 3: architecture
```

### Software Brownfield (Método BMad)

```
1. Escritor Técnico ou Analista: document-project
2. workflow-init → roteia para prd
3. PM: fluxo prd
4. → Fase 3: architecture (recomendado para design de solução focado)
```

### Correção de Bug (Quick Flow)

```
1. workflow-init → roteia para tech-spec
2. PM: fluxo tech-spec
3. → Fase 4: Implementação (pula Fase 3)
```

### Projeto Enterprise (Método Enterprise)

```
1. (Recomendado) Análise: research (compliance, segurança)
2. workflow-init → roteia para Método Enterprise
3. PM: fluxo prd
4. (Opcional) Designer UX: fluxo ux
5. PM: create-epics-and-stories
6. → Fase 3: architecture + segurança + devops + estratégia teste
```

---

## Anti-Padrões Comuns

### ❌ Pulando Planejamento

"Vamos só começar a codar e descobrir."
**Resultado:** Aumento de escopo, retrabalho, requisitos perdidos

### ❌ Sobre-Planejamento de Mudanças Simples

"Deixe-me escrever um PRD de 20 páginas para esta mudança de cor de botão."
**Resultado:** Tempo desperdiçado, paralisia de análise

### ❌ Planejamento Sem Descoberta

"Eu já sei o que quero, pule as perguntas."
**Resultado:** Resolvendo problema errado, perdendo oportunidades

### ❌ Tratando PRD como Imutável

"O PRD está travado, sem mudanças permitidas."
**Resultado:** Ignorando nova informação, planejamento rígido

### ✅ Abordagem Correta

- Use planejamento adaptativo à escala (profundidade certa para complexidade)
- Envolva stakeholders em revisão
- Itere conforme aprende
- Mantenha docs de planejamento vivos e atualizados
- Use `correct-course` para mudanças significativas

---

## Documentação Relacionada

- [Fase 1: Fluxos de Trabalho de Análise](./workflows-analysis.md) - Fase de descoberta opcional
- [Fase 3: Fluxos de Trabalho de Solução](./workflows-solutioning.md) - Próxima fase
- [Fase 4: Fluxos de Trabalho de Implementação](./workflows-implementation.md)
- [Sistema Adaptativo à Escala](./scale-adaptive-system.md) - Entendendo as três trilhas
- [Quick Spec Flow](./quick-spec-flow.md) - Detalhes da trilha Quick Flow
- [Guia de Agentes](./agents-guide.md) - Referência completa de agente

---

## Solução de Problemas

**P: Qual fluxo de trabalho devo rodar primeiro?**
R: Rode `workflow-init`. Ele analisa seu projeto e roteia para o fluxo de planejamento certo.

**P: Eu sempre preciso de um PRD?**
R: Não. Mudanças simples usam `tech-spec` (Quick Flow). Apenas trilhas Método BMad e Enterprise criam PRDs.

**P: Posso pular Fase 3 (Solução)?**
R: Sim para Quick Flow. Opcional para Método BMad (projetos simples). Obrigatório para Método BMad (projetos complexos) e Enterprise.

**P: Como sei qual trilha escolher?**
R: Use `workflow-init` - ele recomenda baseado na sua descrição. Contagens de estória são orientação, não definições.

**P: E se requisitos mudarem no meio do projeto?**
R: Rode fluxo `correct-course`. Ele analisa impacto e atualiza artefatos de planejamento.

**P: Projetos brownfield precisam de arquitetura?**
R: Recomendado! Arquitetura destila base de código massiva em design de solução focado para seu projeto específico.

**P: Quando rodo create-epics-and-stories?**
R: Na Fase 3 (Solução), após arquitetura estar completa.

**P: Devo usar product-brief antes do PRD?**
R: Opcional mas recomendado para greenfield. Ajuda pensamento estratégico. `workflow-init` oferece baseado no contexto.

---

_Planejamento Fase 2 - Requisitos adaptativos à escala para cada projeto._
