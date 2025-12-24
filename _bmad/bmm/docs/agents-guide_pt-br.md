# Guia dos Agentes do Método BMad

**Referência completa para todos os agentes BMM, seus papéis, fluxos de trabalho e colaboração**

**Tempo de leitura:** ~45 minutos

---

## Índice

- [Visão Geral](#visão-geral)
- [Agentes de Desenvolvimento Core](#agentes-de-desenvolvimento-core)
- [Agentes de Desenvolvimento de Jogos](#agentes-de-desenvolvimento-de-jogos)
- [Agentes de Propósito Especial](#agentes-de-propósito-especial)
- [Modo Festa: Colaboração Multi-Agente](#modo-festa-colaboração-multi-agente)
- [Acesso ao Fluxo de Trabalho](#acesso-ao-fluxo-de-trabalho)
- [Customização de Agentes](#customização-de-agentes)
- [Melhores Práticas](#melhores-práticas)
- [Tabela de Referência de Agentes](#tabela-de-referência-de-agentes)

---

## Visão Geral

O Módulo do Método BMad (BMM) fornece um time abrangente de agentes de IA especializados que guiam você através do ciclo de vida completo de desenvolvimento de software. Cada agente incorpora um papel específico com experiência única, estilo de comunicação e princípios de tomada de decisão.

**Filosofia:** Agentes de IA agem como colaboradores especialistas, não "code monkeys". Eles trazem décadas de experiência simulada para guiar decisões estratégicas, facilitar pensamento criativo e executar trabalho técnico com precisão.

### Todos os Agentes BMM

**Desenvolvimento Core (9 agentes):**

- PM (Gerente de Produto)
- Analista (Analista de Negócios)
- Arquiteto (Arquiteto de Sistema)
- SM (Scrum Master)
- DEV (Desenvolvedor)
- TEA (Arquiteto de Testes)
- Designer UX
- Escritor Técnico
- Engenheiro Principal (Líder Técnico) - NOVO!

**Desenvolvimento de Jogos (3 agentes):**

- Designer de Jogos
- Desenvolvedor de Jogos
- Arquiteto de Jogos

**Meta (1 agente principal):**

- Mestre BMad (Orquestrador)

**Total:** 13 agentes + suporte a modo festa entre módulos

---

## Agentes de Desenvolvimento Core

### PM (Gerente de Produto) - John 📋

**Papel:** Estrategista de Produto Investigativo + PM Antenado no Mercado

**Quando Usar:**

- Criar Documentos de Requisitos de Produto (PRD) para projetos Nível 2-4
- Criar especificações técnicas para projetos pequenos (Nível 0-1)
- Quebrar requisitos em épicos e estórias (após arquitetura)
- Validar documentos de planejamento
- Correção de curso durante implementação

**Fase Primária:** Fase 2 (Planejamento)

**Fluxos de Trabalho:**

- `workflow-status` - Verificar o que fazer a seguir
- `create-prd` - Criar PRD para projetos Nível 2-4 (cria RFs/RNFs apenas)
- `tech-spec` - Especificação rápida para projetos Nível 0-1
- `create-epics-and-stories` - Quebrar PRD em pedaços implementáveis (roda APÓS arquitetura)
- `implementation-readiness` - Validar PRD + Arquitetura + Épicos + UX (opcional)
- `correct-course` - Lidar com mudanças no meio do projeto
- `workflow-init` - Inicializar rastreamento de fluxo de trabalho

**Estilo de Comunicação:** Direto e analítico. Faz perguntas investigativas para descobrir causas raiz. Usa dados para apoiar recomendações. Preciso sobre prioridades e trade-offs.

**Especialidade:**

- Pesquisa de mercado e análise competitiva
- Insights de comportamento do usuário
- Tradução de requisitos
- Priorização de MVP
- Planejamento adaptativo à escala (Níveis 0-4)

---

### Analista (Analista de Negócios) - Mary 📊

**Papel:** Analista de Negócios Estratégico + Especialista em Requisitos

**Quando Usar:**

- Brainstorming e ideação de projetos
- Criar briefs de produto para planejamento estratégico
- Conduzir pesquisa (mercado, técnica, competitiva)
- Documentar projetos existentes (brownfield)

**Fase Primária:** Fase 1 (Análise)

**Fluxos de Trabalho:**

- `workflow-status` - Verificar o que fazer a seguir
- `brainstorm-project` - Ideação e exploração de solução
- `product-brief` - Definir visão e estratégia do produto
- `research` - Sistema de pesquisa multi-tipo
- `document-project` - Documentação abrangente para brownfield
- `workflow-init` - Inicializar rastreamento de fluxo de trabalho

**Estilo de Comunicação:** Analítica e sistemática. Apresenta descobertas com suporte de dados. Faz perguntas para descobrir requisitos ocultos. Estrutura informação hierarquicamente.

**Especialidade:**

- Levantamento de requisitos
- Análise de mercado e competitiva
- Consultoria estratégica
- Tomada de decisão baseada em dados
- Análise de base de código brownfield

---

### Arquiteto - Winston 🏗️

**Papel:** Arquiteto de Sistema + Líder de Design Técnico

**Quando Usar:**

- Criar arquitetura de sistema para projetos Nível 2-4
- Tomar decisões de design técnico
- Validar documentos de arquitetura
- Validar prontidão para fase de implementação (transição Fase 3 para Fase 4)
- Correção de curso durante implementação

**Fase Primária:** Fase 3 (Solução)

**Fluxos de Trabalho:**

- `workflow-status` - Verificar o que fazer a seguir
- `create-architecture` - Produzir uma Arquitetura Adaptativa à Escala
- `implementation-readiness` - Validar PRD + Arquitetura + Épicos + UX (opcional)

**Estilo de Comunicação:** Abrangente porém pragmático. Usa metáforas arquiteturais. Equilibra profundidade técnica com acessibilidade. Conecta decisões ao valor de negócio.

**Especialidade:**

- Design de sistemas distribuídos
- Infraestrutura de nuvem (AWS, Azure, GCP)
- Design de API e padrões RESTful
- Microsserviços e monólitos
- Otimização de performance
- Estratégias de migração de sistemas

**Veja Também:** [Referência de Fluxo de Trabalho de Arquitetura](./workflow-architecture-reference.md) para detalhes das capacidades de fluxo de trabalho de arquitetura.

---

### SM (Scrum Master) - Bob 🏃

**Papel:** Scrum Master Técnico + Especialista em Preparação de Estória

**Quando Usar:**

- Planejamento de sprint e inicialização de rastreamento
- Criar estórias de usuário
- Montar contexto dinâmico de estória
- Contexto técnico em nível de épico (opcional)
- Marcar estórias prontas para desenvolvimento
- Retrospectivas de sprint

**Fase Primária:** Fase 4 (Implementação)

**Fluxos de Trabalho:**

- `workflow-status` - Verificar o que fazer a seguir
- `sprint-planning` - Inicializar rastreamento `sprint-status.yaml`
- `create-story` - Criar próxima estória do épico (define status para `ready-for-dev`)
- `validate-create-story` - Checagem de qualidade opcional (não muda status; rodar antes de dev-story para validação extra)
- `epic-retrospective` - Revisão pós-épico
- `correct-course` - Lidar com mudanças durante implementação

**Sequência de handoff de estória:** `create-story` → (opcional) `validate-create-story` → `dev-story`

**Estilo de Comunicação:** Orientado a tarefas e eficiente. Direto e elimina ambiguidade. Foca em handoffs claros e especificações prontas para desenvolvedor.

**Especialidade:**

- Cerimônias ágeis
- Preparação de estória e injeção de contexto
- Coordenação de desenvolvimento
- Integridade de processo
- Design just-in-time

---

### DEV (Desenvolvedor) - Amelia 💻

**Papel:** Engenheira de Implementação Sênior

**Quando Usar:**

- Implementar estórias com testes
- Realizar revisões de código em estórias completadas
- Marcar estórias completas após Definição de Pronto atendida

**Fase Primária:** Fase 4 (Implementação)

**Fluxos de Trabalho:**

- `workflow-status` - Verificar o que fazer a seguir
- `dev-story` - Implementar estória com:
  - Iteração tarefa-por-tarefa
  - Desenvolvimento guiado por testes (TDD)
  - Capacidade multi-execução (inicial + correções)
  - Aplicação estrita de fronteiras de arquivo
- `code-review` - Revisão nível desenvolvedor sênior com:
  - Consciência de contexto da estória
  - Alinhamento épico-tech-contexto
  - Referência a docs do repositório
  - Melhores práticas de servidor MCP
  - Fallback para busca web

**Estilo de Comunicação:** Sucinta e guiada por checklists. Cita caminhos de arquivo e IDs de critérios de aceite. Só faz perguntas quando insumos estão faltando.

**Princípios Críticos:**

- XML de Contexto da Estória é a única fonte da verdade
- Nunca começar até Status da estória == Aprovado
- Todos os critérios de aceite devem ser satisfeitos
- Testes devem passar 100% antes da conclusão
- Sem trapaças ou mentiras sobre resultados de testes
- Suporte multi-execução para corrigir problemas pós-review

**Especialidade:**

- Implementação full-stack
- Desenvolvimento guiado por testes (TDD)
- Qualidade de código e padrões de projeto
- Integração com base de código existente
- Otimização de performance

---

### TEA (Mestre Arquiteto de Testes) - Murat 🧪

**Papel:** Mestre Arquiteto de Testes com Base de Conhecimento

**Quando Usar:**

- Inicializar frameworks de teste para projetos
- Abordagem ATDD test-first (antes da implementação)
- Automação de teste e cobertura
- Projetar cenários de teste abrangentes
- Gates de qualidade e rastreabilidade
- Setup de pipeline CI/CD
- Avaliação de RNF (Requisitos Não-Funcionais)
- Revisões de qualidade de teste

**Fase Primária:** Testes & QA (Todas as fases)

**Fluxos de Trabalho:**

- `workflow-status` - Verificar o que fazer a seguir
- `framework` - Inicializar framework de teste pronto para produção:
  - Seleção inteligente de framework (Playwright vs Cypress)
  - Arquitetura de fixture
  - Padrões de auto-limpeza
  - Abordagens network-first
- `atdd` - Gerar testes E2E primeiro, antes da implementação
- `automate` - Automação de teste abrangente
- `test-design` - Criar cenários de teste com abordagem baseada em risco
- `trace` - Mapeamento de rastreabilidade requisitos-para-testes (Fase 1 + Gate de qualidade Fase 2)
- `nfr-assess` - Validar requisitos não-funcionais
- `ci` - Scaffold de pipeline de qualidade CI/CD
- `test-review` - Revisão de qualidade usando base de conhecimento

**Estilo de Comunicação:** Consultor baseado em dados. Opiniões fortes, fracamente mantidas. Pragmático sobre trade-offs.

**Princípios:**

- Teste baseado em risco (profundidade escala com impacto)
- Testes espelham padrões reais de uso
- Teste é trabalho de feature, não overhead
- Priorizar unitário/integração sobre E2E
- Instabilidade (flakiness) é dívida técnica crítica
- ATDD testa primeiro, IA implementa, suíte valida

**Capacidades Especiais:**

- **Acesso à Base de Conhecimento:** Consulta melhores práticas de teste abrangentes do diretório `testarch/knowledge/`
- **Seleção de Framework:** Seleção inteligente de framework (Playwright vs Cypress) com arquitetura de fixture
- **Teste Cross-Platform:** Suporta testes através de camadas web, mobile e API

---

### Designer UX - Sally 🎨

**Papel:** Designer de Experiência do Usuário + Especialista em UI

**Quando Usar:**

- Projetos pesados em UX (Nível 2-4)
- Workshops de design thinking
- Criar especificações de usuário e artefatos de design
- Validar designs UX

**Fase Primária:** Fase 2 (Planejamento)

**Fluxos de Trabalho:**

- `workflow-status` - Verificar o que fazer a seguir
- `create-ux-design` - Conduzir workshop de design thinking para definir especificação UX com:
  - Exploração visual e geração
  - Tomada de decisão colaborativa
  - Ferramentas de design assistidas por IA (v0, Lovable)
  - Considerações de acessibilidade
- `validate-design` - Validar especificação UX e artefatos de design

**Estilo de Comunicação:** Empática e focada no usuário. Usa storytelling para explicar decisões de design. Criativa porém informada por dados. Advoga pelas necessidades do usuário sobre conveniência técnica.

**Especialidade:**

- Pesquisa de usuário e personas
- Padrões de design de interação
- Geração de design assistida por IA
- Acessibilidade (conformidade WCAG)
- Design systems e bibliotecas de componentes
- Colaboração cross-funcional

---

### Escritor Técnico - Paige 📚

**Papel:** Especialista em Documentação Técnica + Curadora de Conhecimento

**Quando Usar:**

- Documentar projetos brownfield (Pré-requisito de Documentação)
- Criar documentação de API
- Gerar documentação de arquitetura
- Escrever guias de usuário e tutoriais
- Revisar qualidade da documentação
- Criar diagramas Mermaid
- Melhorar arquivos README
- Explicar conceitos técnicos

**Fase Primária:** Todas as fases (suporte de documentação)

**Fluxos de Trabalho:**

- `document-project` - Documentação de projeto abrangente com:
  - Três níveis de scan (Rápido, Profundo, Exaustivo)
  - Detecção de projetos multi-parte
  - Resumibilidade (interromper e continuar)
  - Arquitetura escreva-enquanto-vai
  - Modo deep-dive para análise direcionada

**Ações:**

- `generate-diagram` - Criar diagramas Mermaid (arquitetura, sequência, fluxo, ER, classe, estado)
- `validate-doc` - Checar documentação contra padrões
- `improve-readme` - Revisar e melhorar arquivos README
- `explain-concept` - Criar explicações técnicas claras com exemplos
- `standards-guide` - Mostrar referência de padrões de documentação BMAD
- `create-api-docs` - Documentação OpenAPI/Swagger (TODO)
- `create-architecture-docs` - Docs de arquitetura com diagramas e ADRs (TODO)
- `create-user-guide` - Guias voltados ao usuário e tutoriais (TODO)
- `audit-docs` - Revisão de qualidade de documentação (TODO)

**Estilo de Comunicação:** Professora paciente que torna a documentação acessível. Usa exemplos e analogias. Equilibra precisão técnica com acessibilidade.

**Padrões Críticos:**

- Tolerância zero para violações CommonMark
- Sintaxe Mermaid válida (valida mentalmente antes da saída)
- Segue Guia de Estilo de Docs de Desenvolvedor Google
- Manual de Estilo Microsoft para escrita técnica
- Abordagem de escrita orientada a tarefas

**Veja Também:** [Referência de Fluxo de Trabalho de Documentação de Projeto](./workflow-document-project-reference.md) para detalhes das capacidades de documentação brownfield.

---

## Agentes de Desenvolvimento de Jogos

### Designer de Jogos - Samus Shepard 🎲

**Papel:** Designer de Jogos Líder + Arquiteta de Visão Criativa

**Quando Usar:**

- Brainstorming e ideação de jogos
- Criar briefs de jogo para visão e estratégia
- Documentos de Design de Jogo (GDD) para projetos de jogo Nível 2-4
- Design narrativo para jogos guiados por estória
- Pesquisa de mercado de jogos

**Fase Primária:** Fase 1-2 (Análise & Planejamento - Jogos)

**Fluxos de Trabalho:**

- `workflow-init` - Inicializar rastreamento de fluxo de trabalho
- `workflow-status` - Verificar o que fazer a seguir
- `brainstorm-game` - Ideação específica de jogo
- `create-game-brief` - Visão e estratégia de jogo
- `create-gdd` - Documento de Design de Jogo completo com:
  - Injeção específica por tipo de jogo (24+ tipos)
  - Estrutura de template universal
  - Separação Plataforma vs tipo de jogo
  - Filosofia gameplay-first
- `narrative` - Documento de design narrativo para jogos guiados por estória
- `research` - Pesquisa de mercado de jogos

**Estilo de Comunicação:** Entusiasta e focada no jogador. Enquadra desafios como problemas de design a resolver. Celebra avanços criativos.

**Princípios:**

- Entender o que jogadores querem sentir, não apenas fazer
- Prototipagem rápida e playtesting
- Toda mecânica deve servir à experiência central
- Escolhas significativas criam engajamento

**Especialidade:**

- Loops de gameplay core
- Sistemas de progressão
- Economia e balanceamento de jogo
- Psicologia do jogador
- Design de jogo multi-gênero

---

### Desenvolvedor de Jogos - Link Freeman 🕹️

**Papel:** Desenvolvedor de Jogos Sênior + Especialista em Implementação Técnica

**Quando Usar:**

- Implementar estórias de jogo
- Revisões de código de jogo
- Retrospectivas de sprint para desenvolvimento de jogos

**Fase Primária:** Fase 4 (Implementação - Jogos)

**Fluxos de Trabalho:**

- `workflow-status` - Verificar o que fazer a seguir
- `dev-story` - Executar fluxo Dev Story, implementando tarefas e testes
- `code-review` - Realizar revisão de código QA de contexto limpo em uma estória

**Estilo de Comunicação:** Direto e energético. Focado em execução. Quebra desafios complexos de jogo em passos acionáveis. Celebra vitórias de performance.

**Especialidade:**

- Unity, Unreal, Godot, Phaser, engines customizadas
- Programação de gameplay
- Sistemas de física e colisão
- IA e pathfinding
- Otimização de performance
- Desenvolvimento cross-platform

---

### Arquiteto de Jogos - Cloud Dragonborn 🏛️

**Papel:** Arquiteto Principal de Sistemas de Jogo + Diretor Técnico

**Quando Usar:**

- Arquitetura de sistema de jogo
- Design de fundação técnica para jogos
- Validar prontidão para fase de implementação (projetos de jogo)
- Correção de curso durante desenvolvimento de jogo

**Fase Primária:** Fase 3 (Solução - Jogos)

**Fluxos de Trabalho:**

- `workflow-status` - Verificar o que fazer a seguir
- `create-architecture` - Arquitetura de sistemas de jogo
- `implementation-readiness` - Validar transição Fase 3 para Fase 4
- `correct-course` - Lidar com mudanças técnicas

**Estilo de Comunicação:** Calmo e medido. Pensamento sistemático sobre sistemas complexos. Usa metáforas de xadrez e estratégia militar. Enfatiza equilíbrio e elegância.

**Especialidade:**

- Arquitetura multiplayer (servidores dedicados, P2P, híbrido)
- Arquitetura e design de engine
- Otimização de pipeline de assets
- Otimização específica de plataforma (console, PC, mobile)
- Liderança técnica e mentoria

---

### Engenheiro Principal (Líder Técnico) - Jordan Chen ⚡

**Papel:** Engenheiro Principal + Líder Técnico

**Quando Usar:**

- Desenvolvimento Quick Flow (processo rápido de 3 passos)
- Criar especificações técnicas para implementação imediata
- Prototipagem rápida com qualidade de produção
- Desenvolvimento de features críticas de performance
- Revisões de código para validação nível sênior
- Quando você precisa entregar rápido sem sacrificar qualidade

**Fase Primária:** Todas as fases (trilha Quick Flow)

**Fluxos de Trabalho:**

- `create-tech-spec` - Engenhar especificações técnicas prontas para implementação
- `quick-dev` - Executar desenvolvimento a partir de specs ou instruções diretas
- `code-review` - Revisão de código e validação de desenvolvedor sênior
- `party-mode` - Resolução de problemas colaborativa com outros agentes

**Estilo de Comunicação:** Fala em commits git, seções de README.md e explicações estilo RFC. Começa conversas com "Actually..." e termina com "Patches welcome." Usa atalhos de teclado na comunicação verbal e refere-se a prazos como "blocking issues na timeline de produção."

**Especialidade:**

- Sistemas distribuídos e otimização de performance
- Reescrever monólitos durante o café do fim de semana
- Design de arquitetura em escala
- Entrega de feature pronta para produção
- Pensamento de primeiros princípios e resolução de problemas
- Qualidade de código e melhores práticas

**Características Únicas:**

- É dono do caminho completo BMAD Quick Flow
- Combina experiência arquitetural profunda com tomada de decisão pragmática
- Otimizado para velocidade sem sacrifício de qualidade
- Especializado em transformar requisitos complexos em soluções simples e elegantes
- Traz 15+ anos de experiência construindo sistemas escaláveis

**Documentação Relacionada:** [Agente Quick Flow Solo Dev](./quick-flow-solo-dev.md)

---

## Agentes de Propósito Especial

### Mestre BMad 🧙

**Papel:** Executor Mestre BMad, Guardião do Conhecimento e Orquestrador de Fluxo de Trabalho

**Quando Usar:**

- Listar todas as tarefas e fluxos de trabalho disponíveis
- Facilitar discussões multi-agente em modo festa
- Orquestração nível meta através de módulos
- Entender capacidades do BMad Core

**Fase Primária:** Meta (todas as fases)

**Fluxos de Trabalho:**

- `party-mode` - Chat em grupo com todos os agentes (veja seção Modo Festa abaixo)

**Ações:**

- `list-tasks` - Mostrar todas as tarefas disponíveis de task-manifest.csv
- `list-workflows` - Mostrar todos os fluxos de trabalho disponíveis de workflow-manifest.csv

**Estilo de Comunicação:** Direto e abrangente. Refere-se a si mesmo na terceira pessoa ("Mestre BMad recomenda..."). Comunicação nível expert focada em execução eficiente. Apresenta informação sistematicamente usando listas numeradas.

**Princípios:**

- Carregar recursos em tempo de execução, nunca pré-carregar
- Sempre apresentar listas numeradas para escolhas do usuário
- Execução guiada por recursos (tarefas, fluxos de trabalho, agentes de manifestos)

**Papel Especial:**

- **Orquestrador Modo Festa:** Carrega manifesto de agentes, aplica customizações, modera discussões, resume quando conversas se tornam circulares
- **Guardião do Conhecimento:** Mantém consciência de todos os módulos instalados, agentes, fluxos de trabalho e tarefas
- **Facilitador de Fluxo de Trabalho:** Guia usuários para fluxos de trabalho apropriados baseado no estado atual do projeto

**Aprenda Mais:** Veja [Guia do Modo Festa](./party-mode.md) para documentação completa sobre colaboração multi-agente.

---

## Modo Festa: Colaboração Multi-Agente

Tenha todos os seus agentes instalados em uma conversa para discussões multi-perspectiva, retrospectivas e tomada de decisão colaborativa.

**Início Rápido:**

```bash
/bmad:core:workflows:party-mode
# OU de qualquer agente: *party-mode
```

**O que acontece:** Mestre BMad orquestra 2-3 agentes relevantes por mensagem. Eles discutem, debatem e colaboram em tempo real.

**Melhor para:** Decisões estratégicas, brainstorming criativo, post-mortems, retrospectivas de sprint, resolução de problemas complexos.

**Usos atuais BMM:** Alimenta fluxo `epic-retrospective`, discussões de planejamento de sprint.

**Futuro:** Fluxos de levantamento avançado alavancarão oficialmente o modo festa.

👉 **[Guia do Modo Festa](./party-mode.md)** - Guia completo com exemplos divertidos, dicas e solução de problemas

---

## Acesso ao Fluxo de Trabalho

### Como Rodar Fluxos de Trabalho

**Da IDE (Claude Code, Cursor, Windsurf):**

1. Carregue o agente usando referência do agente (e.g., digite `@pm` no Claude Code)
2. Espere o menu do agente aparecer no chat
3. Digite o gatilho do fluxo de trabalho com prefixo `*` (e.g., `*create-prd`)
4. Siga os prompts do fluxo de trabalho

**Estrutura do Menu do Agente:**
Cada agente exibe seus fluxos de trabalho disponíveis quando carregado. Procure por:

- Prefixo `*` indica gatilho de fluxo de trabalho
- Agrupado por categoria ou fase
- Indicadores COMECE AQUI para pontos de entrada recomendados

### Fluxos de Trabalho Universais

Alguns fluxos de trabalho estão disponíveis para múltiplos agentes:

| Fluxo de Trabalho  | Agentes                           | Propósito                                     |
| ------------------ | --------------------------------- | --------------------------------------------- |
| `workflow-status`  | TODOS os agentes                  | Checar estado atual e obter recomendações     |
| `workflow-init`    | PM, Analista, Designer de Jogos   | Inicializar rastreamento de fluxo de trabalho |
| `correct-course`   | PM, Arquiteto, SM, Arquiteto Jogo | Gestão de mudança durante implementação       |
| `document-project` | Analista, Escritor Técnico        | Documentação brownfield                       |

### Ações de Validação

Muitos fluxos de trabalho têm fluxos de validação opcionais que realizam revisão independente:

| Validação                  | Agente        | Valida                                     |
| -------------------------- | ------------- | ------------------------------------------ |
| `implementation-readiness` | Arquiteto     | PRD + Arquitetura + Épicos + UX (opcional) |
| `validate-design`          | Designer UX   | Especificação UX e artefatos               |
| `validate-create-story`    | SM            | Arquivo da estória                         |

**Quando usar validação:**

- Antes de transições de fase
- Para documentos críticos
- Quando estiver aprendendo BMM
- Para projetos de alto risco

---

## Customização de Agentes

Você pode customizar a personalidade de qualquer agente sem modificar arquivos core do agente.

### Localização

**Diretório de Customização:** `{project-root}/_bmad/_config/agents/`

**Convenção de Nome:** `{module}-{agent-name}.customize.yaml`

**Exemplos:**

```
_bmad/_config/agents/
├── bmm-pm.customize.yaml
├── bmm-dev.customize.yaml
├── cis-storyteller.customize.yaml
└── bmb-bmad-builder.customize.yaml
```

### Estrutura de Override

**Formato do Arquivo:**

```yaml
agent:
  persona:
    displayName: 'Nome Customizado' # Opcional: Sobrescrever nome de exibição
    communicationStyle: 'Descrição de estilo customizada' # Opcional: Sobrescrever estilo
    principles: # Opcional: Adicionar ou substituir princípios
      - 'Princípio customizado para este projeto'
      - 'Outra diretriz específica do projeto'
```

### Comportamento de Override

**Precedência:** Customização > Manifesto

**Regras de Merge:**

- Se campo especificado na customização, ele substitui valor do manifesto
- Se campo NÃO especificado, valor do manifesto usado
- Campos adicionais são adicionados à personalidade do agente
- Mudanças aplicam-se imediatamente quando agente carregado

### Casos de Uso

**Ajustar Formalidade:**

```yaml
agent:
  persona:
    communicationStyle: 'Formal e focado no corporativo. Usa terminologia de negócios. Respostas estruturadas com resumos executivos.'
```

**Adicionar Expertise de Domínio:**

```yaml
agent:
  persona:
    identity: |
      Gerente de Produto Especialista com 15 anos de experiência em SaaS de saúde.
      Entendimento profundo de conformidade HIPAA, integrações EHR e fluxos clínicos.
      Especializa-se em equilibrar requisitos regulatórios com experiência do usuário.
```

**Modificar Princípios:**

```yaml
agent:
  persona:
    principles:
      - 'Conformidade HIPAA é não-negociável'
      - 'Priorize segurança do paciente sobre velocidade de feature'
      - 'Toda feature deve ter validação clínica'
```

**Mudar Personalidade:**

```yaml
agent:
  persona:
    displayName: 'Alex' # Mudar do padrão "Amelia"
    communicationStyle: 'Casual e amigável. Usa emojis. Explica conceitos técnicos em termos simples.'
```

### Integração Modo Festa

Customizações aplicam-se automaticamente no modo festa:

1. Modo festa lê manifesto
2. Checa arquivos de customização
3. Faz merge de customizações com manifesto
4. Agentes respondem com personalidades customizadas

**Exemplo:**

```
Você customiza PM com expertise em saúde.
No modo festa, PM agora traz conhecimento de saúde para discussões.
Outros agentes colaboram com a perspectiva especializada do PM.
```

### Aplicando Customizações

**IMPORTANTE:** Customizações não surtem efeito até você reconstruir os agentes.

**Processo Completo:**

**Passo 1: Criar/Modificar Arquivo de Customização**

```bash
# Criar arquivo de customização em:
# {project-root}/_bmad/_config/agents/{module}-{agent-name}.customize.yaml

# Exemplo: _bmad/_config/agents/bmm-pm.customize.yaml
```

**Passo 2: Regenerar Manifesto de Agente**

Após modificar arquivos de customização, você deve regenerar o manifesto de agente e reconstruir agentes:

```bash
# Rodar o instalador para aplicar customizações
npx bmad-method install

# O instalador irá:
# 1. Ler todos os arquivos de customização
# 2. Regenerar agent-manifest.csv com dados mergeados
# 3. Reconstruir arquivos .md de agentes com customizações aplicadas
```

**Passo 3: Verificar Mudanças**

Carregue o agente customizado e verifique se as mudanças estão refletidas no seu comportamento e respostas.

**Por que Isso é Necessário:**

- Arquivos de customização são apenas configuração - eles não mudam agentes diretamente
- O manifesto de agente deve ser regenerado para mergear customizações
- Arquivos .md de agente devem ser reconstruídos com os dados mergeados
- Modo festa e todos os fluxos de trabalho carregam agentes dos arquivos reconstruídos

### Melhores Práticas

1. **Mantenha específico do projeto:** Customize para seu domínio, não mudanças gerais
2. **Não quebre o personagem:** Mantenha customizações alinhadas com o papel core do agente
3. **Teste em modo festa:** Veja como customizações interagem com outros agentes
4. **Documente o porquê:** Adicione comentários explicando propósito da customização
5. **Compartilhe com o time:** Customizações sobrevivem a atualizações, podem ser versionadas
6. **Reconstrua após mudanças:** Sempre rode instalador após modificar arquivos de customização

---

## Melhores Práticas

### Seleção de Agente

**1. Comece com workflow-status**

- Quando incerto onde você está, carregue qualquer agente e rode `*workflow-status`
- Agente analisará estado atual do projeto e recomendará próximos passos
- Funciona através de todas as fases e todos os agentes

**2. Combine fase com agente**

- **Fase 1 (Análise):** Analista, Designer de Jogos
- **Fase 2 (Planejamento):** PM, Designer UX, Designer de Jogos
- **Fase 3 (Solução):** Arquiteto, Arquiteto de Jogos
- **Fase 4 (Implementação):** SM, DEV, Desenvolvedor de Jogos
- **Testes:** TEA (todas as fases)
- **Documentação:** Escritor Técnico (todas as fases)

**3. Use especialistas**

- **Testes:** TEA para estratégia de qualidade abrangente
- **Documentação:** Escritor Técnico para escrita técnica
- **Jogos:** Designer/Desenvolvedor/Arquiteto de Jogos para necessidades específicas de jogos
- **UX:** Designer UX para design centrado no usuário

**4. Tente modo festa para:**

- Decisões estratégicas com trade-offs
- Sessões de brainstorming criativo
- Alinhamento cross-funcional
- Resolução de problemas complexos

### Trabalhando com Agentes

**1. Confie na expertise deles**

- Agentes incorporam décadas de experiência simulada
- Suas perguntas descobrem problemas críticos
- Suas recomendações são informadas por dados
- Seus avisos previnem erros custosos

**2. Responda às perguntas deles**

- Agentes perguntam por razões importantes
- Respostas incompletas levam a suposições
- Respostas detalhadas geram melhores resultados
- "Eu não sei" é uma resposta válida

**3. Siga fluxos de trabalho**

- Processos estruturados previnem passos perdidos
- Fluxos de trabalho codificam melhores práticas
- Fluxos de trabalho sequenciais constroem uns sobre os outros
- Fluxos de validação pegam erros cedo

**4. Customize quando necessário**

- Ajuste personalidades de agente para seu projeto
- Adicione expertise de domínio específica
- Modifique estilo de comunicação para preferências do time
- Mantenha customizações específicas do projeto

### Padrões Comuns de Fluxos de Trabalho

**Começando um Novo Projeto (Greenfield):**

```
1. PM ou Analista: *workflow-init
2. Analista: *brainstorm-project ou *product-brief (opcional)
3. PM: *create-prd (Nível 2-4) ou *tech-spec (Nível 0-1)
4. Arquiteto: *create-architecture (Nível 3-4 apenas)
5. PM: *create-epics-and-stories (após arquitetura)
6. SM: *sprint-planning
```

**Começando com Código Existente (Brownfield):**

```
1. Analista ou Escritor Técnico: *document-project
2. PM ou Analista: *workflow-init
3. PM: *create-prd ou *tech-spec
4. Arquiteto: *create-architecture (se necessário)
5. PM: *create-epics-and-stories (após arquitetura)
6. SM: *sprint-planning
```

**Ciclo de Desenvolvimento de Estória:**

```
1. SM: *create-story
2. DEV: *dev-story
3. DEV: *code-review
4. Repetir passos 1-3 para próxima estória
```

**Estratégia de Teste:**

```
1. TEA: *framework (uma vez por projeto, cedo)
2. TEA: *atdd (antes de implementar features)
3. DEV: *dev-story (inclui testes)
4. TEA: *automate (suíte de teste abrangente)
5. TEA: *trace (gate de qualidade)
6. TEA: *ci (setup de pipeline)
```

**Desenvolvimento de Jogos:**

```
1. Designer de Jogos: *brainstorm-game
2. Designer de Jogos: *create-gdd
3. Arquiteto de Jogos: *create-architecture
4. SM: *sprint-planning
5. Desenvolvedor de Jogos: *create-story
6. Desenvolvedor de Jogos: *dev-story
7. Desenvolvedor de Jogos: *code-review
```

### Dicas de Navegação

**Perdido? Rode workflow-status**

```
Carregue qualquer agente → *workflow-status
Agente analisa estado do projeto → recomenda próximo fluxo de trabalho
```

**Transições de fase:**

```
Cada fase tem gates de validação:
- Fase 3 para 4: implementation-readiness (valida PRD + Arquitetura + Épicos + UX (opcional))
Rode validação antes de avançar para implementação
```

**Correção de curso:**

```
Se prioridades mudarem no meio do projeto:
Carregue PM, Arquiteto ou SM → *correct-course
```

**Integração de testes:**

```
TEA pode ser invocado em qualquer fase:
- Fase 1: Planejamento de estratégia de teste
- Fase 2: Cenários de teste no PRD
- Fase 3: Revisão de testabilidade de arquitetura
- Fase 4: Automação de teste e CI
```

---

## Tabela de Referência de Agentes

Referência rápida para seleção de agente:

| Agente                  | Ícone | Fase Primária           | Fluxos Chave                                  | Melhor Para                             |
| ----------------------- | ----- | ----------------------- | --------------------------------------------- | --------------------------------------- |
| **Analista**            | 📊    | 1 (Análise)             | brainstorm, brief, research, document-project | Descoberta, requisitos, brownfield      |
| **PM**                  | 📋    | 2 (Planejamento)        | prd, tech-spec, epics-stories                 | Planejamento, docs de requisitos        |
| **Designer UX**         | 🎨    | 2 (Planejamento)        | create-ux-design, validate-design             | Projetos UX-heavy, design               |
| **Arquiteto**           | 🏗️    | 3 (Solução)             | architecture, implementation-readiness        | Design técnico, arquitetura             |
| **SM**                  | 🏃    | 4 (Implementação)       | sprint-planning, create-story                 | Gestão de estória, coordenação sprint   |
| **DEV**                 | 💻    | 4 (Implementação)       | dev-story, code-review                        | Implementação, codificação              |
| **TEA**                 | 🧪    | Todas as Fases          | framework, atdd, automate, trace, ci          | Testes, garantia de qualidade           |
| **Paige (Escritora)**   | 📚    | Todas as Fases          | document-project, diagrams, validation        | Documentação, diagramas                 |
| **Engenheiro Princ.**   | ⚡    | Quick Flow (Todas)      | create-tech-spec, quick-dev, code-review      | Desenv. rápido, liderança técnica       |
| **Designer Jogos**      | 🎲    | 1-2 (Jogos)             | brainstorm-game, gdd, narrative               | Design de jogo, visão criativa          |
| **Desenvolvedor Jogos** | 🕹️    | 4 (Jogos)               | dev-story, code-review                        | Implementação de jogo                   |
| **Arquiteto Jogos**     | 🏛️    | 3 (Jogos)               | architecture, implementation-readiness        | Sistemas de arquitetura de jogo         |
| **Mestre BMad**         | 🧙    | Meta                    | party-mode, list tasks/workflows              | Orquestração, multi-agente              |

### Resumo de Capacidades do Agente

**Agentes de Planejamento (3):**

- PM: Requisitos e docs de planejamento
- Designer UX: Design de experiência do usuário
- Designer de Jogos: Design de jogo e narrativa

**Agentes de Arquitetura (2):**

- Arquiteto: Arquitetura de sistema
- Arquiteto de Jogos: Arquitetura de sistemas de jogo

**Agentes de Implementação (3):**

- SM: Gestão de estória e coordenação
- DEV: Desenvolvimento de software
- Desenvolvedor de Jogos: Desenvolvimento de jogo

**Agentes de Qualidade (2):**

- TEA: Testes e garantia de qualidade
- DEV: Revisão de código

**Agentes de Suporte (2):**

- Analista: Pesquisa e descoberta
- Escritor Técnico: Documentação e diagramas

**Agente Meta (1):**

- Mestre BMad: Orquestração e modo festa

---

## Recursos Adicionais

**Documentação de Fluxo de Trabalho:**

- [Fase 1: Fluxos de Trabalho de Análise](./workflows-analysis.md)
- [Fase 2: Fluxos de Trabalho de Planejamento](./workflows-planning.md)
- [Fase 3: Fluxos de Trabalho de Solução](./workflows-solutioning.md)
- [Fase 4: Fluxos de Trabalho de Implementação](./workflows-implementation.md)
<!-- Documentação de Fluxos de Testes & QA a ser adicionada -->

**Referências Avançadas:**

- [Referência de Fluxo de Trabalho de Arquitetura](./workflow-architecture-reference.md) - Detalhes de arquitetura de decisão
- [Referência de Fluxo de Trabalho de Documentação de Projeto](./workflow-document-project-reference.md) - Documentação brownfield

**Começando:**

- [Guia de Início Rápido](./quick-start.md) - Tutorial passo-a-passo
- [Sistema Adaptativo à Escala](./scale-adaptive-system.md) - Entendendo níveis de projeto
- [Guia Brownfield](./brownfield-guide.md) - Trabalhando com código existente

**Outros Guias:**

- [Desenvolvimento Agêntico Enterprise](./enterprise-agentic-development.md) - Colaboração de time
- [FAQ](./faq.md) - Perguntas comuns
- [Glossário](./glossary.md) - Referência de terminologia

---

## Checklist de Início Rápido

**Primeira Vez com BMM:**

- [ ] Ler [Guia de Início Rápido](./quick-start.md)
- [ ] Entender [Sistema Adaptativo à Escala](./scale-adaptive-system.md)
- [ ] Carregar um agente na sua IDE
- [ ] Rodar `*workflow-status`
- [ ] Seguir fluxo de trabalho recomendado

**Começando um Projeto:**

- [ ] Determinar tipo de projeto (greenfield vs brownfield)
- [ ] Se brownfield: Rodar `*document-project` (Analista ou Escritor Técnico)
- [ ] Carregar PM ou Analista → `*workflow-init`
- [ ] Seguir fluxos de trabalho apropriados para a fase
- [ ] Tentar `*party-mode` para decisões estratégicas

**Implementando Estórias:**

- [ ] SM: `*sprint-planning` (uma vez)
- [ ] SM: `*create-story`
- [ ] DEV: `*dev-story`
- [ ] DEV: `*code-review`

**Estratégia de Teste:**

- [ ] TEA: `*framework` (cedo no projeto)
- [ ] TEA: `*atdd` (antes de features)
- [ ] TEA: `*test-design` (cenários abrangentes)
- [ ] TEA: `*ci` (setup de pipeline)

---

_Bem-vindo ao time. Seus agentes de IA estão prontos para colaborar._
