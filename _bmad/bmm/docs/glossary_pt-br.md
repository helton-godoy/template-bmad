# Glossário BMM

Referência de terminologia abrangente para o Módulo Método BMad.

---

## Navegação

- [Conceitos Principais](#conceitos-principais)
- [Escala e Complexidade](#escala-e-complexidade)
- [Documentos de Planejamento](#documentos-de-planejamento)
- [Fluxo de Trabalho e Fases](#fluxo-de-trabalho-e-fases)
- [Agentes e Funções](#agentes-e-funções)
- [Status e Rastreamento](#status-e-rastreamento)
- [Tipos de Projeto](#tipos-de-projeto)
- [Termos de Implementação](#termos-de-implementação)

---

## Conceitos Principais

### BMM (Módulo Método BMad)

Sistema central de orquestração para desenvolvimento ágil orientado por IA, fornecendo gerenciamento de ciclo de vida abrangente através de agentes especializados e fluxos de trabalho.

### Método BMad

A metodologia completa para desenvolvimento de software assistido por IA, abrangendo planejamento, arquitetura, implementação e fluxos de trabalho de garantia de qualidade que se adaptam à complexidade do projeto.

### Sistema Adaptativo de Escala

Orquestração inteligente de fluxo de trabalho do Método BMad que ajusta automaticamente profundidade de planejamento, requisitos de documentação e processos de implementação baseados nas necessidades do projeto através de três faixas de planejamento distintas (Fluxo Rápido, Método BMad, Método Empresarial).

### Agente

Uma persona de IA especializada com expertise específica (PM, Arquiteto, SM, DEV, TEA) que guia usuários através de fluxos de trabalho e cria entregáveis. Agentes têm capacidades definidas, estilos de comunicação e acesso a fluxos de trabalho.

### Fluxo de Trabalho

Um processo guiado de múltiplas etapas que orquestra atividades de agentes de IA para produzir entregáveis específicos. Fluxos de trabalho são interativos e se adaptam ao contexto do usuário.

---

## Escala e Complexidade

### Trilha Fluxo Rápido

Trilha de implementação rápida usando apenas planejamento tech-spec. Melhor para correções de bugs, pequenos recursos e mudanças com escopo claro. Faixa típica: 1-15 estórias. Nenhuma fase de arquitetura necessária. Exemplos: correções de bugs, login OAuth, recursos de busca.

### Trilha Método BMad

Trilha de planejamento de produto completa usando PRD + Arquitetura + UX. Melhor para produtos, plataformas e recursos complexos exigindo design de sistema. Faixa típica: 10-50+ estórias. Exemplos: painéis administrativos, plataformas de e-commerce, produtos SaaS.

### Trilha Método Empresarial

Trilha de planejamento empresarial estendida adicionando Arquitetura de Segurança, Estratégia DevOps e Estratégia de Teste ao Método BMad. Melhor para requisitos empresariais, necessidades de conformidade e sistemas multi-tenant. Faixa típica: 30+ estórias. Exemplos: plataformas multi-tenant, sistemas orientados a conformidade, aplicações de missão crítica.

### Trilha de Planejamento

O caminho metodológico (Fluxo Rápido, Método BMad ou Método Empresarial) escolhido para um projeto baseado em necessidades de planejamento, complexidade e requisitos, em vez de contagem de estórias isoladamente.

**Nota:** Contagens de estórias são orientação, não definições. Trilhas são determinadas pelo planejamento que o projeto precisa, não matemática de estória.

---

## Documentos de Planejamento

### Tech-Spec (Especificação Técnica)

**Apenas trilha Fluxo Rápido.** Plano técnico abrangente criado antecipadamente que serve como documento de planejamento primário para pequenas mudanças ou recursos. Contém declaração do problema, abordagem de solução, mudanças em nível de arquivo, detecção de stack (brownfield), estratégia de teste e recursos para desenvolvedores.

### PRD (Documento de Requisitos de Produto)

**Trilhas Método BMad/Empresarial.** Documento de planejamento em nível de produto contendo visão, metas, Requisitos Funcionais (FRs), Requisitos Não-Funcionais (NFRs), critérios de sucesso e considerações de UX. Substitui tech-spec para projetos maiores que precisam de planejamento de produto. **Nota V6:** PRD foca no QUE construir (requisitos). Épico+Estórias são criados separadamente APÓS a arquitetura via fluxo de trabalho create-epics-and-stories.

### Documento de Arquitetura

**Trilhas Método BMad/Empresarial.** Documento de design de todo o sistema definindo estrutura, componentes, interações, modelos de dados, padrões de integração, segurança, desempenho e implantação.

**Adaptativo à Escala:** Complexidade da arquitetura escala com a trilha - Método BMad é leve a moderado, Método Empresarial é abrangente com estratégias de segurança/devops/teste.

### Épicos

Agrupamentos de recursos de alto nível que contêm múltiplas estórias relacionadas. Tipicamente abrangem 5-15 estórias cada e representam funcionalidade coesa (ex: "Épico de Autenticação de Usuário").

### Resumo do Produto (Product Brief)

Documento de planejamento estratégico opcional criado na Fase 1 (Análise) que captura visão do produto, contexto de mercado, necessidades do usuário e requisitos de alto nível antes do planejamento detalhado.

### GDD (Documento de Design de Jogo)

Equivalente de desenvolvimento de jogos do PRD, criado pelo agente Game Designer para projetos de jogos.

---

## Fluxo de Trabalho e Fases

### Fase 0: Documentação (Pré-requisito)

**Fase condicional para projetos brownfield.** Cria documentação abrangente da base de código antes do planejamento. Apenas obrigatória se documentação existente for insuficiente para agentes de IA.

### Fase 1: Análise (Opcional)

Fase de descoberta e pesquisa incluindo brainstorming, fluxos de trabalho de pesquisa e criação de resumo de produto. Opcional para Fluxo Rápido, recomendada para Método BMad, obrigatória para Método Empresarial.

### Fase 2: Planejamento (Obrigatório)

**Sempre obrigatório.** Cria requisitos formais e divisão de trabalho. Roteia para tech-spec (Fluxo Rápido) ou PRD (Método BMad/Empresarial) baseado na trilha selecionada.

### Fase 3: Solução (Dependente de Trilha)

Fase de design de arquitetura. Obrigatória para trilhas Método BMad e Método Empresarial. Inclui criação de arquitetura, validação e verificações de portão.

### Fase 4: Implementação (Obrigatório)

Desenvolvimento baseado em sprint através de iteração estória-por-estória. Usa fluxos de trabalho sprint-planning, create-story, dev-story, code-review e retrospective.

### Documentação (Pré-requisito para Brownfield)

**Pré-requisito condicional para projetos brownfield.** Cria documentação abrangente da base de código antes do planejamento. Apenas obrigatória se documentação existente for insuficiente para agentes de IA. Usa o fluxo de trabalho `document-project`.

### Fluxo de Especificação Rápida (Quick Spec Flow)

Sistema de fluxo de trabalho de via rápida para projetos de trilha Fluxo Rápido que vai direto da ideia para tech-spec para implementação, ignorando planejamento pesado. Projetado para correções de bugs, pequenos recursos e prototipagem rápida.

---

## Agentes e Funções

### PM (Gerente de Produto)

Agente responsável por criar PRDs, tech-specs e gerenciar requisitos de produto. Agente primário para planejamento da Fase 2.

### Analista (Analista de Negócios)

Agente que inicializa fluxos de trabalho, conduz pesquisa, cria resumos de produto e rastreia progresso. Frequentemente o ponto de entrada para novos projetos.

### Arquiteto

Agente que projeta arquitetura de sistema, cria documentos de arquitetura, realiza revisões técnicas e valida designs. Agente primário para solução da Fase 3.

### SM (Scrum Master)

Agente que gerencia sprints, cria estórias, gera contextos e coordena implementação. Orquestrador primário para implementação da Fase 4.

### DEV (Desenvolvedor)

Agente que implementa estórias, escreve código, roda testes e realiza revisões de código. Implementador primário na Fase 4.

### TEA (Arquiteto de Teste)

Agente responsável por estratégia de teste, portões de qualidade, avaliação de NFR e garantia de qualidade abrangente. Integra-se através de todas as fases.

### Escritor Técnico

Agente especializado em criar e manter documentação técnica de alta qualidade. Especialista em padrões de documentação, arquitetura de informação e escrita técnica profissional. O nome interno do agente é "paige" mas é apresentado como "Escritor Técnico" aos usuários.

### Designer UX

Agente que cria documentos de design UX, padrões de interação e especificações visuais para projetos pesados em UI.

### Game Designer

Agente especializado para projetos de desenvolvimento de jogos. Cria documentos de design de jogo (GDD) e fluxos de trabalho específicos de jogos.

### Mestre BMad

Agente orquestrador de meta-nível do BMad Core. Facilita o modo festa, lista tarefas e fluxos de trabalho disponíveis e fornece orientação de alto nível através de todos os módulos.

### Modo Festa

Recurso de colaboração multi-agente onde todos os agentes instalados (19+ do BMM, CIS, BMB, módulos customizados) discutem desafios juntos em tempo real. Mestre BMad orquestra, selecionando 2-3 agentes relevantes por mensagem para conversa cruzada e debate natural. Melhor para decisões estratégicas, brainstorming criativo, alinhamento cross-functional e resolução de problemas complexos. Veja [Guia do Modo Festa](./party-mode.md).

---

## Status e Rastreamento

### bmm-workflow-status.yaml

**Fases 1-3.** Arquivo de rastreamento que mostra fase atual, fluxos de trabalho completados, progresso e próximas ações recomendadas. Criado por workflow-init, atualizado automaticamente.

### sprint-status.yaml

**Fase 4 apenas.** Fonte única de verdade para rastreamento de implementação. Contém todos épicos, estórias e retrospectivas com status atual para cada. Criado por sprint-planning, atualizado por agentes.

### Progressão de Status de Estória

```
backlog → ready-for-dev → in-progress → review → done
```

- **backlog** - Estória existe no épico mas ainda não criada
- **ready-for-dev** - Arquivo de estória criado via create-story; validação é opcional (execute `validate-create-story` para verificação de qualidade antes do dev pegar)
- **in-progress** - DEV está implementando via dev-story
- **review** - Implementação completa, aguardando code-review
- **done** - Completado com DoD atendido

### Progressão de Status de Épico

```
backlog → in-progress → done
```

- **backlog** - Épico ainda não iniciado
- **in-progress** - Épico sendo trabalhado ativamente
- **done** - Todas estórias no épico completadas

### Retrospectiva

Fluxo de trabalho executado após completar cada épico para capturar aprendizados, identificar melhorias e alimentar insights no próximo planejamento de épico. Crítico para melhoria contínua.

---

## Tipos de Projeto

### Greenfield

Projeto novo começando do zero sem base de código existente. Liberdade para estabelecer padrões, escolher stack e projetar a partir de folha em branco.

### Brownfield

Projeto existente com base de código estabelecida, padrões e restrições. Requer compreensão da arquitetura existente, respeito às convenções estabelecidas e planejamento de integração com sistemas atuais.

**Crítico:** Projetos brownfield devem rodar fluxo de trabalho document-project ANTES do planejamento para garantir que agentes de IA tenham contexto adequado sobre código existente.

### Fluxo de Trabalho document-project

**Pré-requisito brownfield.** Analisa e documenta base de código existente, criando documentação abrangente incluindo visão geral do projeto, análise de arquitetura, árvore de fontes, contratos de API e modelos de dados. Três níveis de scan: rápido, profundo, exaustivo.

---

## Termos de Implementação

### Estória

Unidade única de trabalho implementável com critérios de aceitação claros, tipicamente 2-8 horas de esforço de desenvolvimento. Estórias são agrupadas em épicos e rastreadas no sprint-status.yaml.

### Arquivo de Estória

Arquivo Markdown contendo detalhes da estória: descrição, critérios de aceitação, notas técnicas, dependências, orientação de implementação e requisitos de teste.

### Contexto da Estória

Orientação de implementação embutida dentro de arquivos de estória durante o fluxo de trabalho create-story. Fornece contexto específico de implementação, referencia padrões existentes, sugere abordagens e ajuda a manter consistência com convenções de base de código estabelecidas.

### Planejamento de Sprint

Fluxo de trabalho que inicializa implementação da Fase 4 criando sprint-status.yaml, extraindo todos épicos/estórias de docs de planejamento e configurando infraestrutura de rastreamento.

### Verificação de Portão (Gate Check)

Fluxo de trabalho de validação (implementation-readiness) executado antes da Fase 4 para garantir que PRD + Arquitetura + Épicos + UX (opcional) estejam alinhados sem lacunas ou contradições. Obrigatório para trilhas Método BMad e Método Empresarial.

### DoD (Definição de Pronto)

Critérios que devem ser atendidos antes de marcar uma estória como pronta. Tipicamente inclui: implementação completa, testes escritos e passando, código revisado, documentação atualizada e critérios de aceitação validados.

### Fragmentação (Shard / Sharding)

**Apenas para otimização de runtime LLM (NÃO docs humanos).** Divisão de documentos de planejamento grandes (PRD, épicos, arquitetura) em arquivos menores baseados em seção para melhorar eficiência de fluxo de trabalho. Fluxos de trabalho Fase 1-3 carregam documentos fragmentados inteiros de forma transparente. Fluxos de trabalho Fase 4 carregam seletivamente apenas seções necessárias para economias massivas de tokens.

---

## Termos Adicionais

### Status do Fluxo de Trabalho

Fluxo de trabalho de ponto de entrada universal que verifica arquivo de status existente, exibe fase/progresso atual e recomenda próxima ação baseada no estado do projeto.

### Inicialização de Fluxo de Trabalho (Workflow Init)

Fluxo de trabalho de inicialização que cria bmm-workflow-status.yaml, detecta greenfield vs brownfield, determina trilha de planejamento e configura caminho de fluxo de trabalho apropriado.

### Seleção de Trilha

Análise automática por workflow-init que usa análise de palavras-chave, indicadores de complexidade e requisitos de projeto para sugerir trilha apropriada (Fluxo Rápido, Método BMad ou Método Empresarial). Usuário pode sobrescrever trilha sugerida.

### Corrigir Curso

Fluxo de trabalho executado durante Fase 4 quando mudanças significativas ou problemas surgem. Analisa impacto, propõe soluções e roteia para fluxos de trabalho de remediação apropriados.

### Estratégia de Migração

Plano para lidar com mudanças em dados existentes, esquemas, APIs ou padrões durante desenvolvimento brownfield. Crítico para garantir compatibilidade retroativa e lançamento suave.

### Feature Flags

Técnica de implementação para projetos brownfield que permite lançamento gradual de nova funcionalidade, rollback fácil e teste A/B. Recomendada para mudanças brownfield Método BMad e Empresarial.

### Pontos de Integração

Locais específicos onde novo código se conecta com sistemas existentes. Devem ser documentados explicitamente em tech-specs e arquiteturas brownfield.

### Detecção de Convenção

Recurso do Quick Spec Flow que detecta automaticamente estilo de código existente, convenções de nomenclatura, padrões e frameworks de bases de código brownfield, então pede ao usuário para confirmar antes de prosseguir.

---

## Documentação Relacionada

- [Guia de Início Rápido](./quick-start.md) - Aprenda o básico do BMM
- [Sistema Adaptativo de Escala](./scale-adaptive-system.md) - Mergulho profundo em trilhas e complexidade
- [Guia Brownfield](./brownfield-guide.md) - Trabalhando com bases de código existentes
- [Fluxo de Especificação Rápida](./quick-spec-flow.md) - Via rápida para trilha Fluxo Rápido
- [FAQ](./faq.md) - Perguntas comuns
