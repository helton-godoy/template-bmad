# Perguntas Frequentes (FAQ) do BMM

Respostas rápidas para perguntas comuns sobre o Módulo de Método BMad.

---

## Índice

- [Começando](#começando)
- [Escolhendo o Nível Certo](#escolhendo-o-nível-certo)
- [Fluxos de Trabalho e Fases](#fluxos-de-trabalho-e-fases)
- [Documentos de Planejamento](#documentos-de-planejamento)
- [Implementação](#implementação)
- [Desenvolvimento Brownfield](#desenvolvimento-brownfield)
- [Ferramentas e Técnico](#ferramentas-e-técnico)

---

## Começando

### P: Eu sempre preciso rodar o workflow-init?

**R:** Não, uma vez que você aprenda o fluxo, pode ir diretamente para os fluxos de trabalho. No entanto, o `workflow-init` é útil porque:

- Determina o nível apropriado do seu projeto automaticamente
- Cria o arquivo de rastreamento de status
- Roteia você para o fluxo de trabalho inicial correto

Para usuários experientes: use a [Referência Rápida](./quick-start.md#referência-rápida-de-mapeamento-agente-documento) para ir diretamente ao agente/fluxo de trabalho correto.

### P: Por que eu preciso de novos chats para cada fluxo de trabalho?

**R:** Fluxos de trabalho intensivos em contexto (como brainstorming, criação de PRD, design de arquitetura) podem causar alucinações na IA se rodados em sequência no mesmo chat. Começar do zero garante que o agente tenha capacidade máxima de contexto para cada fluxo de trabalho. Isso é particularmente importante para:

- Fluxos de planejamento (PRD, arquitetura)
- Fluxos de análise (brainstorming, pesquisa)
- Implementação de estória complexa

Fluxos rápidos como verificações de status podem reutilizar chats com segurança.

### P: Posso pular o workflow-status e apenas começar a trabalhar?

**R:** Sim, se você já sabe o nível do seu projeto e qual fluxo de trabalho vem a seguir. O `workflow-status` é útil principalmente para:

- Novos projetos (guia a configuração inicial)
- Quando você não tem certeza do que fazer a seguir
- Após pausas no trabalho (lembra onde você parou)
- Verificar o progresso geral

### P: Qual o mínimo que preciso para começar?

**R:** Para o caminho mais rápido:

1. Instale o BMad Method: `npx bmad-method@alpha install`
2. Para pequenas mudanças: Carregue o agente PM → rode `tech-spec` → implemente
3. Para projetos maiores: Carregue o agente PM → rode `prd` → arquiteto → implemente

### P: Como sei se estou na Fase 1, 2, 3 ou 4?

**R:** Verifique seu arquivo `bmm-workflow-status.md` (criado pelo `workflow-init`). Ele mostra sua fase atual e progresso. Se você não tem este arquivo, também pode saber pelo que está trabalhando:

- **Fase 1** - Brainstorming, pesquisa, resumo do produto (opcional)
- **Fase 2** - Criando um PRD ou tech-spec (sempre obrigatório)
- **Fase 3** - Design de arquitetura (apenas Nível 2-4)
- **Fase 4** - Escrevendo código de fato, implementando estórias

---

## Escolhendo o Nível Certo

### P: Como sei qual é o nível do meu projeto?

**R:** Use o `workflow-init` para detecção automática, ou autoavalie usando estas palavras-chave:

- **Nível 0:** "fix", "bug", "erro de digitação", "pequena mudança", "patch" → 1 estória
- **Nível 1:** "simples", "básico", "funcionalidade pequena", "adicionar" → 2-10 estórias
- **Nível 2:** "dashboard", "várias funcionalidades", "painel administrativo" → 5-15 estórias
- **Nível 3:** "plataforma", "integração", "complexo", "sistema" → 12-40 estórias
- **Nível 4:** "enterprise", "multi-tenant", "múltiplos produtos" → 40+ estórias

Na dúvida, comece menor. Você sempre pode rodar `create-prd` mais tarde se necessário.

### P: Posso mudar de nível no meio do projeto?

**R:** Sim! Se você começou no Nível 1 mas percebeu que é Nível 2, pode rodar `create-prd` para adicionar documentos de planejamento apropriados. O sistema é flexível - sua escolha de nível inicial não é permanente.

### P: E se o workflow-init sugerir o nível errado?

**R:** Você pode sobrescrevê-lo! O `workflow-init` sugere um nível mas sempre pede confirmação. Se você discordar, apenas diga e escolha o nível que acha apropriado. Confie no seu julgamento.

### P: Eu sempre preciso de arquitetura para o Nível 2?

**R:** Não, arquitetura é **opcional** para o Nível 2. Apenas crie arquitetura se precisar de design em nível de sistema. Muitos projetos Nível 2 funcionam bem apenas com o PRD criado durante o planejamento.

### P: Qual a diferença entre Nível 1 e Nível 2?

**R:**

- **Nível 1:** 1-10 estórias, usa `tech-spec` (mais simples, mais rápido), sem arquitetura
- **Nível 2:** 5-15 estórias, usa `PRD` (focado no produto), arquitetura opcional

A sobreposição (5-10 estórias) é intencional. Escolha baseado em:

- Precisa de planejamento nível de produto? → Nível 2
- Só precisa de plano técnico? → Nível 1
- Múltiplos épicos? → Nível 2
- Épico único? → Nível 1

---

## Fluxos de Trabalho e Fases

### P: Qual a diferença entre workflow-status e workflow-init?

**R:**

- **workflow-status:** Verifica status existente e diz o que vem a seguir (use ao continuar trabalho)
- **workflow-init:** Cria novo arquivo de status e configura projeto (use ao iniciar novo projeto)

Se arquivo de status existe, use `workflow-status`. Se não, use `workflow-init`.

### P: Posso pular a Fase 1 (Análise)?

**R:** Sim! A Fase 1 é opcional para todos os níveis, embora recomendada para projetos complexos. Pule se:

- Requisitos estão claros
- Nenhuma pesquisa necessária
- Trabalho sensível ao tempo
- Mudanças pequenas (Nível 0-1)

### P: Quando a Fase 3 (Arquitetura) é obrigatória?

**R:**

- **Nível 0-1:** Nunca (pule inteiramente)
- **Nível 2:** Opcional (apenas se design de sistema necessário)
- **Nível 3-4:** Obrigatória (arquitetura abrangente mandatória)

### P: O que acontece se eu pular um fluxo de trabalho recomendado?

**R:** Nada quebra! Fluxos de trabalho são orientação, não imposição. No entanto, pular fluxos recomendados (como arquitetura para Nível 3) pode causar:

- Problemas de integração durante implementação
- Retrabalho devido a planejamento ruim
- Decisões de design conflitantes
- Tempo de desenvolvimento mais longo no geral

### P: Como sei quando a Fase 3 está completa e posso começar a Fase 4?

**R:** Para Nível 3-4, rode o fluxo de trabalho `implementation-readiness`. Ele valida se PRD + Arquitetura + Épicos + UX (opcional) estão alinhados antes da implementação. Passar na verificação do gate = pronto para Fase 4.

### P: Posso rodar fluxos de trabalho em paralelo ou eles têm que ser sequenciais?

**R:** A maioria dos fluxos deve ser sequencial dentro de uma fase:

- Fase 1: brainstorm → research → product-brief (ordem opcional)
- Fase 2: PRD deve completar antes de avançar
- Fase 3: architecture → epics+stories → implementation-readiness (sequencial)
- Fase 4: Estórias dentro de um épico devem geralmente ser sequenciais, mas estórias em diferentes épicos podem ser paralelas se você tiver capacidade

---

## Documentos de Planejamento

### P: Por que sem tech-spec no Nível 2+?

**R:** Projetos Nível 2+ precisam de planejamento nível de produto (PRD) e design nível de sistema (Arquitetura), que o `tech-spec` não fornece. `tech-spec` é muito estreito para coordenar múltiplas funcionalidades. Em vez disso, Nível 2-4 usa:

- PRD (visão do produto, requisitos funcionais, requisitos não-funcionais)
- Arquitetura (design de sistema)
- Épicos+Estórias (criados APÓS a arquitetura estar completa)

### P: Preciso de um PRD para uma correção de bug?

**R:** Não! Correções de bugs são tipicamente Nível 0 (mudança atômica única). Use o Fluxo Rápido de Especificação (Quick Spec Flow):

- Carregue o agente PM
- Rode o fluxo `tech-spec`
- Implemente imediatamente

PRDs são para projetos Nível 2-4 com múltiplas funcionalidades requerendo coordenação de nível de produto.

### P: Posso pular o resumo do produto (product brief)?

**R:** Sim, o resumo do produto é sempre opcional. É mais valioso para:

- Projetos Nível 3-4 precisando de direção estratégica
- Projetos com stakeholders requerendo alinhamento
- Produtos novos precisando de pesquisa de mercado
- Quando você quer explorar espaço de solução antes de comprometer

---

## Implementação

### P: O create-story inclui contexto de implementação?

**R:** Sim! O fluxo `create-story` gera arquivos de estória que incluem orientação específica de implementação, referencia padrões existentes da sua documentação e fornece contexto técnico. O fluxo carrega sua arquitetura, PRD e documentação de projeto existente para criar estórias abrangentes. Para projetos Quick Flow usando `tech-spec`, a própria especificação técnica já é abrangente, então estórias podem ser mais simples.

### P: Como marco uma estória como feita?

**R:** Após `dev-story` completar e `code-review` passar:

1. Abra `sprint-status.yaml` (criado por `sprint-planning`)
2. Mude o status da estória de `review` para `done`
3. Salve o arquivo

### P: Posso trabalhar em múltiplas estórias de uma vez?

**R:** Sim, se você tiver capacidade! Estórias dentro de diferentes épicos podem ser trabalhadas em paralelo. No entanto, estórias dentro do mesmo épico são usualmente sequenciais porque constroem uma sobre a outra.

### P: E se minha estória demorar mais que o estimado?

**R:** Isso é normal! Estórias são estimativas. Se a implementação revelar mais complexidade:

1. Continue trabalhando até o DoD ser atendido
2. Considere se a estória deveria ser dividida
3. Documente aprendizados na retrospectiva
4. Ajuste estimativas futuras baseadas nesse aprendizado

### P: Quando devo rodar a retrospectiva?

**R:** Após completar todas as estórias em um épico (quando o épico está pronto). Retrospectivas capturam:

- O que correu bem
- O que poderia melhorar
- Insights técnicos
- Aprendizados para futuros épicos

Não espere até o fim do projeto - rode após cada épico para melhoria contínua.

---

## Desenvolvimento Brownfield

### P: O que é brownfield vs greenfield?

**R:**

- **Greenfield:** Novo projeto, começando do zero, folha em branco
- **Brownfield:** Projeto existente, trabalhando com base de código e padrões estabelecidos

### P: Tenho que rodar document-project para brownfield?

**R:** Altamente recomendado, especialmente se:

- Nenhuma documentação existente
- Documentação está desatualizada
- Agentes de IA precisam de contexto sobre código existente
- Complexidade Nível 2-4

Você pode pular se tiver documentação abrangente e atualizada, incluindo `docs/index.md`.

### P: E se eu esquecer de rodar document-project no brownfield?

**R:** Fluxos de trabalho faltarão contexto sobre código existente. Você pode obter:

- Sugestões que não combinam com padrões existentes
- Abordagens de integração que perdem APIs existentes
- Arquitetura que conflita com estrutura atual

Rode `document-project` e reinicie o planejamento com contexto apropriado.

### P: Posso usar Quick Spec Flow para projetos brownfield?

**R:** Sim! O Quick Spec Flow funciona muito bem para brownfield. Ele irá:

- Auto-detectar sua stack existente
- Analisar padrões de código brownfield
- Detectar convenções e pedir confirmação
- Gerar tech-spec rico em contexto que respeita código existente

Perfeito para correções de bugs e pequenas funcionalidades em bases de código existentes.

### P: Como o workflow-init lida com brownfield com docs de planejamento antigos?

**R:** O `workflow-init` pergunta sobre SEU trabalho atual primeiro, então usa artefatos antigos como contexto:

1. Mostra o que encontrou (PRD antigo, épicos, etc.)
2. Pergunta: "Isso é trabalho em andamento, esforço anterior ou trabalho proposto?"
3. Se esforço anterior: Pede para você descrever seu NOVO trabalho
4. Determina nível baseado no SEU trabalho, não em artefatos antigos

Isso previne que PRDs antigos Nível 3 forcem fluxo Nível 3 para nova correção de bug Nível 0.

### P: E se meu código existente não segue melhores práticas?

**R:** O Quick Spec Flow detecta suas convenções e pergunta: "Devo seguir estas convenções existentes?" Você decide:

- **Sim** → Manter consistência com base de código atual
- **Não** → Estabelecer novos padrões (documente o porquê na tech-spec)

O BMM respeita sua escolha - ele não forçará modernização, mas a oferecerá.

---

## Ferramentas e Técnico

### P: Por que meus diagramas Mermaid não estão renderizando?

**R:** Problemas comuns:

1. Faltando tag de linguagem: Use ` ```mermaid` não apenas ` ``` `
2. Erros de sintaxe no diagrama (valide em mermaid.live)
3. Ferramenta não suporta Mermaid (verifique seu renderizador Markdown)

Todos os docs BMM usam sintaxe Mermaid válida que deve renderizar no GitHub, VS Code e maioria das IDEs.

### P: Posso usar BMM com GitHub Copilot / Cursor / outras ferramentas de IA?

**R:** Sim! O BMM é complementar. O BMM lida com:

- Planejamento e estrutura de projeto
- Orquestração de fluxo de trabalho
- Personas e expertise de Agentes
- Geração de documentação
- Gates de qualidade

Seu assistente de codificação IA lida com:

- Completar código linha-por-linha
- Refatoração rápida
- Geração de teste

Use-os juntos para melhores resultados.

### P: Quais IDEs/ferramentas suportam BMM?

**R:** O BMM requer ferramentas com **modo agente** e acesso a **modelos LLM de alta qualidade** que possam carregar e seguir fluxos de trabalho complexos, e então implementar mudanças de código adequadamente.

**Ferramentas Recomendadas:**

- **Claude Code** ⭐ **Melhor escolha**
  - Sonnet 4.5 (excelente seguimento de fluxo, codificação, raciocínio)
  - Opus (máximo contexto, planejamento complexo)
  - Modo agente nativo desenhado para fluxos BMM

- **Cursor**
  - Suporta modelos Anthropic (Claude) e OpenAI
  - Modo agente com composer
  - Bom para desenvolvedores que preferem a UX do Cursor

- **Windsurf**
  - Suporte multi-modelo
  - Capacidades de agente
  - Adequado para fluxos BMM

**O Que Importa:**

1. **Modo Agente** - Pode carregar longas instruções de fluxo e manter contexto
2. **LLM de Alta Qualidade** - Modelos ranqueados alto no SWE-bench (benchmarks de codificação)
3. **Seleção de Modelo** - Acesso a Claude Sonnet 4.5, Opus, ou modelos classe GPT-4o
4. **Capacidade de Contexto** - Pode lidar com grandes documentos de planejamento e bases de código

**Por que a qualidade do modelo importa:** Fluxos BMM requerem LLMs que possam seguir processos multi-passo, manter contexto através de fases e implementar código que adere a especificações. Ferramentas com modelos mais fracos terão dificuldade com aderência a fluxo e qualidade de código.

Veja [Guias de Setup de IDE](https://github.com/bmad-code-org/BMAD-METHOD/tree/main/docs/ide-info) para especificidades de configuração.

### P: Posso customizar agentes?

**R:** Sim! Agentes são instalados como arquivos markdown com conteúdo estilo XML (otimizado para LLMs, legível por qualquer modelo). Crie arquivos de customização em `_bmad/_config/agents/[agent-name].customize.yaml` para sobrescrever comportamentos padrão enquanto mantém funcionalidade core intacta. Veja documentação de agente para opções de customização.

**Nota:** Enquanto agentes fonte neste repo são YAML, eles instalam como arquivos `.md` com tags estilo XML - um formato que qualquer LLM pode ler e seguir.

### P: O que acontece com meus docs de planejamento após implementação?

**R:** Mantenha-os! Eles servem como:

- Registro histórico de decisões
- Material de onboarding para novos membros do time
- Referência para melhorias futuras
- Trilha de auditoria para conformidade

Para projetos enterprise (Nível 4), considere arquivar artefatos de planejamento completados para manter o workspace limpo.

### P: Posso usar BMM para projetos não-software?

**R:** O BMM é otimizado para desenvolvimento de software, mas os princípios da metodologia (planejamento adaptativo à escala, design just-in-time, injeção de contexto) podem aplicar a outros tipos de projeto complexos. Você precisaria adaptar fluxos de trabalho e agentes para seu domínio.

---

## Perguntas Avançadas

### P: E se meu projeto crescer de Nível 1 para Nível 3?

**R:** Totalmente ok! Quando você perceber que o escopo cresceu:

1. Rode `create-prd` para adicionar planejamento nível de produto
2. Rode `create-architecture` para design de sistema
3. Use `tech-spec` existente como insumo para PRD
4. Continue com nível atualizado

O sistema é flexível - crescimento é esperado.

### P: Posso misturar abordagens greenfield e brownfield?

**R:** Sim! Cenário comum: adicionar nova funcionalidade greenfield a base de código brownfield. Abordagem:

1. Rode `document-project` para contexto brownfield
2. Use fluxos greenfield para planejamento de nova funcionalidade
3. Documente explicitamente pontos de integração entre novo e existente
4. Teste integração extensivamente

### P: Como lido com hotfixes urgentes durante uma sprint?

**R:** Use fluxo `correct-course` ou apenas:

1. Salve seu estado de trabalho atual
2. Carregue agente PM → `tech-spec` rápido para hotfix
3. Implemente hotfix (fluxo Nível 0)
4. Faça deploy do hotfix
5. Retorne ao trabalho original da sprint

Nível 0 Quick Spec Flow é perfeito para correções urgentes.

### P: E se eu discordar das recomendações do fluxo de trabalho?

**R:** Fluxos de trabalho são orientação, não imposição. Se um fluxo recomenda algo que não faz sentido para seu contexto:

- Explique seu raciocínio para o agente
- Peça por abordagens alternativas
- Pule a recomendação se estiver confiante
- Documente por que você desviou (para referência futura)

Confie na sua expertise - O BMM apoia suas decisões.

### P: Múltiplos desenvolvedores podem trabalhar no mesmo projeto BMM?

**R:** Sim! Mas o paradigma é fundamentalmente diferente de times ágeis tradicionais.

**Diferença Chave:**

- **Tradicional:** Múltiplos devs trabalham em estórias dentro de um épico (meses)
- **Agêntico:** Cada dev é dono de épicos completos (dias)

**No ágil tradicional:** Um time de 5 devs pode gastar 2-3 meses em um único épico, com cada dev possuindo estórias diferentes.

**Com BMM + Agentes de IA:** Um único dev pode completar um épico inteiro em 1-3 dias. O que costumava levar meses agora leva dias.

**Distribuição de Trabalho do Time:**

- **Recomendado:** Divida trabalho por **épico** (não estória)
- Cada desenvolvedor possui épicos completos de ponta a ponta
- Trabalho paralelo acontece no nível de épico
- Coordenação mínima necessária

**Para apps full-stack:**

- Frontend e backend podem ser épicos separados (incomum no ágil tradicional)
- Dev Frontend possui todos os épicos frontend
- Dev Backend possui todos os épicos backend
- Funciona porque a entrega é tão rápida

**Considerações Enterprise:**

- Use **submódulos git** para instalação BMM (não .gitignore)
- Permite configurações pessoais sem poluir repo principal
- Times podem usar ferramentas de IA diferentes (Claude Code, Cursor, etc.)
- Desenvolvedores podem seguir métodos diferentes ou criar agentes/fluxos customizados

**Dicas Rápidas:**

- Compartilhe `sprint-status.yaml` (fonte única da verdade)
- Atribua épicos inteiros a desenvolvedores (não estórias individuais)
- Coordene em fronteiras de épico, não nível de estória
- Use submódulos git para BMM em configurações enterprise

**Para cobertura abrangente de colaboração de time enterprise, estratégias de distribuição de trabalho, setup de submódulo git e expectativas de velocidade, veja:**

👉 **[Guia de Desenvolvimento Agêntico Empresarial](./enterprise-agentic-development.md)**

### P: O que é o modo festa e quando devo usá-lo?

**R:** O modo festa é uma funcionalidade única de colaboração multi-agente onde TODOS os seus agentes instalados (19+ do BMM, CIS, BMB, módulos customizados) discutem seus desafios juntos em tempo real.

**Como funciona:**

1. Rode `/bmad:core:workflows:party-mode` (ou `*party-mode` de qualquer agente)
2. Introduza seu tópico
3. Mestre BMad seleciona 2-3 agentes mais relevantes por mensagem
4. Agentes conversam, debatem e constroem sobre as ideias uns dos outros

**Melhor para:**

- Decisões estratégicas com trade-offs (escolhas de arquitetura, stack tecnológica, escopo)
- Brainstorming criativo (design de jogo, inovação de produto, ideação UX)
- Alinhamento cross-funcional (kickoffs de épico, retrospectivas, transições de fase)
- Resolução de problemas complexos (desafios multi-facetados, avaliação de risco)

**Festas de exemplo:**

- **Estratégia de Produto:** PM + Estrategista de Inovação (CIS) + Analista
- **Design Técnico:** Arquiteto + Solucionador de Problemas Criativo (CIS) + Arquiteto de Jogos
- **Experiência do Usuário:** Designer UX + Coach de Design Thinking (CIS) + Storyteller (CIS)

**Por que é poderoso:**

- Perspectivas diversas (técnica, criativa, estratégica)
- Debate saudável revela pontos cegos
- Insights emergentes da interação de agentes
- Colaboração natural através de módulos

**Para documentação completa:**

👉 **[Guia do Modo Festa](./party-mode.md)** - Como funciona, quando usar, composições de exemplo, melhores práticas

---

## Obtendo Ajuda

### P: Onde obtenho ajuda se minha pergunta não for respondida aqui?

**R:**

1. Pesquise na [Documentação Completa](./README.md) por tópicos relacionados
2. Pergunte na [Comunidade Discord](https://discord.gg/gk8jAdXWmj) (#general-dev)
3. Abra uma [Issue no GitHub](https://github.com/bmad-code-org/BMAD-METHOD/issues)
4. Assista [Tutoriais no YouTube](https://www.youtube.com/@BMadCode)

### P: Como reporto um bug ou peço uma funcionalidade?

**R:** Abra uma issue no GitHub em: <https://github.com/bmad-code-org/BMAD-METHOD/issues>

Por favor inclua:

- Versão BMM (verifique sua versão instalada)
- Passos para reproduzir (para bugs)
- Comportamento esperado vs real
- Fluxo de trabalho ou agente relevante envolvido

---

## Documentação Relacionada

- [Guia de Início Rápido](./quick-start.md) - Comece com BMM
- [Glossário](./glossary.md) - Referência de terminologia
- [Sistema Adaptativo à Escala](./scale-adaptive-system.md) - Entendendo níveis
- [Guia Brownfield](./brownfield-guide.md) - Fluxos de base de código existente

---

**Tem uma pergunta não respondida aqui?** Por favor [abra uma issue](https://github.com/bmad-code-org/BMAD-METHOD/issues) ou pergunte no [Discord](https://discord.gg/gk8jAdXWmj) para que possamos adicioná-la!
