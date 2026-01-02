# Passo 2: Compreensão do Projeto

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- 📖 CRÍTICO: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido e compreendido antes de prosseguir
- ✅ SEMPRE trate isso como descoberta colaborativa entre facilitador de UX e stakeholder
- 📋 VOCÊ É UM FACILITADOR DE UX, não um gerador de conteúdo
- 💬 FOQUE em entender o contexto do projeto e necessidades do usuário
- 🎯 Descoberta COLABORATIVA, não baseada em suposições

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠️ Apresente o menu A/P/C após gerar conteúdo de compreensão do projeto
- 💾 SALVE APENAS quando o usuário escolher C (Continuar)
- 📖 Atualize o frontmatter `stepsCompleted: [1, 2]` antes de carregar o próximo passo
- 🚫 PROIBIDO carregar o próximo passo até que C seja selecionado

## MENUS DE COLABORAÇÃO (A/P/C):

Este passo irá gerar conteúdo e apresentar opções:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights mais profundos do projeto
- **P (Modo Festa)**: Traga múltiplas perspectivas para entender o contexto do projeto
- **C (Continuar)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO DE PROTOCOLO:

- Quando 'A' selecionado: Execute {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' selecionado: Execute {project-root}/_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS sempre retornam ao menu A/P/C deste passo
- Usuário aceita/rejeita alterações de protocolo antes de prosseguir

## LIMITES DE CONTEXTO:

- Documento atual e frontmatter do passo 1 estão disponíveis
- Documentos de entrada (PRD, resumos, épicos) já carregados estão na memória
- Não são necessários arquivos de dados adicionais para este passo
- Foco na compreensão do projeto e do usuário

## SUA TAREFA:

Entender o contexto do projeto, usuários-alvo e o que torna este produto especial de uma perspectiva UX.

## SEQUÊNCIA DE DESCOBERTA DE PROJETO:

### 1. Revisar Contexto Carregado

Comece analisando o que sabemos dos documentos carregados:
"Com base na documentação do projeto que carregamos, deixe-me confirmar o que estou entendendo sobre {{project_name}}.

**Dos documentos:**
{resumo dos principais insights dos documentos PRD, resumos e outros contextos carregados}

**Usuários-alvo:**
{resumo das informações do usuário dos documentos carregados}

**Recursos Principais:**
{resumo dos principais recursos e objetivos dos documentos carregados}

Isso corresponde ao seu entendimento? Há algumas correções ou adições que você gostaria de fazer?"

### 2. Preencher Lacunas de Contexto (Se Sem Documentos ou Lacunas)

Se nenhum documento foi carregado ou falta informação chave:
"Como não temos documentação completa, vamos começar com o essencial:

**O que você está construindo?** (Descreva seu produto em 1-2 frases)

**Para quem é isso?** (Descreva seu usuário ideal ou público-alvo)

**O que torna isso especial ou diferente?** (Qual é a proposta de valor única?)

**Qual é a principal coisa que os usuários farão com isso?** (Ação ou objetivo central do usuário)"

### 3. Explorar Contexto de Usuário Mais Profundo

Mergulhe na compreensão do usuário:
"Deixe-me entender melhor seus usuários para informar o design UX:

**Perguntas de Contexto do Usuário:**

- Que problema os usuários estão tentando resolver?
- O que os frustra com soluções atuais?
- O que os faria dizer 'isso é exatamente o que eu precisava'?
- Qual é o nível de proficiência técnica dos usuários?
- Que dispositivos eles usarão mais?
- Quando/onde eles usarão este produto?"

### 4. Identificar Desafios de Design UX

Identifique os principais desafios de UX para enfrentar:
"Pelo que discutimos, estou vendo algumas considerações importantes sobre design de UX:

**Desafios de Design:**

- [Identifique 2-3 principais desafios UX com base no tipo de projeto e necessidades do usuário]
- [Note quaisquer considerações específicas da plataforma]
- [Destaque quaisquer fluxos ou interações de usuário complexos]

**Oportunidades de Design:**

- [Identifique 2-3 áreas onde um ótimo UX poderia criar vantagem competitiva]
- [Note quaisquer oportunidades para padrões inovadores de UX]

Isso captura as principais considerações de UX que precisamos abordar?"

### 5. Gerar Conteúdo de Compreensão do Projeto

Prepare o conteúdo para anexar ao documento:

#### Estrutura do Conteúdo:

Ao salvar no documento, anexe estas seções de Nível 2 e Nível 3:

```markdown
## Executive Summary

### Project Vision

[Project vision summary based on conversation]

### Target Users

[Target user descriptions based on conversation]

### Key Design Challenges

[Key UX challenges identified based on conversation]

### Design Opportunities

[Design opportunities identified based on conversation]
```

### 6. Apresentar Conteúdo e Menu

Mostre o conteúdo de compreensão do projeto gerado e apresente as opções:
"Documentei nossa compreensão de {{project_name}} de uma perspectiva UX. Isso guiará todas as nossas decisões de design daqui para frente.

**Aqui está o que vou adicionar ao documento:**

[Mostre o conteúdo markdown completo do passo 5]

**O que você gostaria de fazer?**
[A] Elicitação Avançada - Vamos mergulhar mais fundo na compreensão do projeto
[P] Modo Festa - Trazer diferentes perspectivas
[C] Continuar - Salvar e mover para Definir a Experiência Principal"

### 7. Lidar com Seleção de Menu

#### SE A (Elicitação Avançada):

- Execute {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Retorne com insights aprimorados

#### SE P (Modo Festa):

- Execute {project-root}/_bmad/core/workflows/party-mode/workflow.md
- Retorne com perspectivas colaborativas

#### SE C (Continuar):

- Anexe o conteúdo final ao documento
- Atualize frontmatter: `stepsCompleted: [1, 2]`
- Carregue `./step-03-core-experience_pt-br.md`

## MÉTRICAS DE SUCESSO:

✅ Visão do projeto claramente articulada de uma perspectiva UX
✅ Usuários-alvo definidos com necessidades e comportamentos
✅ Desafios de design chave identificados
✅ Oportunidades de design capturadas
✅ Menu A/P/C apresentado e tratado corretamente
✅ Conteúdo devidamente anexado ao documento quando C selecionado

## MODOS DE FALHA:

❌ Gerar conteúdo genérico sem entrada do usuário
❌ Falha em identificar desafios críticos de UX
❌ Não validar o entendimento com o usuário
❌ Prosseguir sem seleção explícita de 'C'

❌ **CRÍTICO**: Ler apenas parte do arquivo de passo - leva a compreensão incompleta e más decisões
❌ **CRÍTICO**: Prosseguir com 'C' sem ler e compreender totalmente o próximo arquivo de passo
❌ **CRÍTICO**: Tomar decisões sem compreensão completa dos requisitos e protocolos do passo

## PRÓXIMO PASSO:

Após o usuário selecionar [C], carregue `./step-03-core-experience_pt-br.md` para definir os objetivos emocionais e princípios de experiência.
