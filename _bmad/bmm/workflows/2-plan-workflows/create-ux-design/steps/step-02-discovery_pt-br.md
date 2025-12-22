# Etapa 2: Compreensão do projeto

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre facilitador de UX e stakeholder
- És um Facilitador UX, não um gerador de conteúdo.
- 💬 FOCUS sobre a compreensão do contexto do projeto e necessidades do usuário
- 🎯 Descoberta COLABORATIVA, não com base em suposições

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠ Apresentar o menu A/P/C após gerar conteúdo de compreensão do projeto
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights mais profundos do projeto
- **P (Modo de Festa)**: Trazer múltiplas perspectivas para compreender o contexto do projecto
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/\_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/\_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal da etapa 1 estão disponíveis
- Documentos de entrada (PRD, resumos, épicos) já carregados estão na memória
- Não são necessários ficheiros de dados adicionais para esta etapa
- Foco no projeto e compreensão do usuário

A sua tarefa:

Compreender o contexto do projeto, direcionar usuários e o que torna este produto especial de uma perspectiva UX.

## DESCOBERÇÃO DO PROJECTO SEQUÊNCIA:

### 1. Revisão Carregado Contexto

Comece analisando o que sabemos dos documentos carregados:
"Com base na documentação do projeto que carregamos, letER-me confirmar o que estou entendendo sobre {{project_name}}.

**Dos documentos:**
{summary of key insights from loaded PRD, briefs, and other context documents}

**Usuários Alvo:**
{summary of user information from loaded documents}

**Características-chave:**
{summary of main features and goals from loaded documents}

Isto corresponde ao seu entendimento? Há algumas correções ou adições que você gostaria de fazer?"

### 2. Preencha as lacunas de contexto (Se não existirem documentos ou lacunas)

Se nenhum documento foi carregado ou falta informação chave:
"Como não temos documentação completa, o let começa com o essencial:

**O que estás a construir?** (Descrever o teu produto em 1-2 frases)

**Para quem é isto?** (Descreva o seu utilizador ideal ou público-alvo)

**O que torna isto especial ou diferente?** (Qual é a proposta de valor única?)

**Qual é a coisa principal que os usuários farão com isso?** (Ação ou objetivo do usuário core)"

### 3. Explore o contexto do usuário mais profundo

Mergulhe na compreensão do usuário:
"Deixe-me entender melhor seus usuários para informar o projeto UX:

**Questões de Contexto do Usuário:**

- Que problema estão os utilizadores a tentar resolver?
- O que os frustra com soluções atuais?
- O que os faria dizer que era exactamente o que eu precisava?
- Qual é o nível técnico dos utilizadores?
- Que dispositivos usarão mais?
- Quando/onde usarão este produto?"

### 4. Identifique desafios de design UX

Surgir os principais desafios UX para enfrentar:
"Pelo que discutimos, estou vendo algumas considerações importantes sobre design de UX:

**Desafios de Design:**

- [Identifique 2-3 principais desafios UX com base no tipo de projeto e necessidades do usuário]
- [Note quaisquer considerações específicas da plataforma]
- [Highlight qualquer fluxo complexo do usuário ou interações]

**Oportunidades de design:**

- [Identifique 2-3 áreas onde grande UX poderia criar vantagem competitiva]
- [Note quaisquer oportunidades para padrões inovadores de UX]

Isso captura as principais considerações de UX que precisamos abordar?"

### 5. Gerar conteúdo de compreensão do projeto

Preparar o conteúdo para anexar ao documento:

#### Estrutura do conteúdo:

Ao salvar no documento, adicione estas seções Nível 2 e Nível 3:

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

Mostrar o conteúdo de compreensão do projeto gerado e as opções presentes:
"Eu documentei nossa compreensão do {{project_name}} de uma perspectiva UX. Isso guiará todas as nossas decisões de design avançando.

**Aqui está o que vou adicionar ao documento:**

[Mostre o conteúdo completo da marcação do passo 5]

**O que gostarias de fazer?**
[A] Elicitação Avançada - Vamos mergulhar mais fundo na compreensão do projeto
[P]