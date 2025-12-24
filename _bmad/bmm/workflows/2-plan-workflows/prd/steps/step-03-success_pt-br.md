---
name: 'step-03-success'
description: 'Define comprehensive success criteria covering user, business, and technical success'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-03-success.md'
nextStepFile: '{workflow_path}/steps/step-04-journeys.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/prd.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Etapa 3: Definição dos critérios de sucesso

**Progresso: Passo 3 de 11** - Próximo: Mapeamento de Viagem do Usuário

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre colegas de PM
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS na definição de como é ganhar para este produto
- 🎯 Descoberta COLABORATIVA, não definição de metas baseadas em suposições

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠ Apresentar o menu A/P/C após gerar o conteúdo dos critérios de sucesso
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights mais profundos sobre as métricas de sucesso
- **P (Modo de Festa)**: Traz múltiplas perspectivas para definir critérios de sucesso abrangentes
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal das etapas anteriores estão disponíveis
- Resumo Executivo e Classificação de Projetos já existem em documento
- Documentos de entrada a partir da etapa-01 estão disponíveis (sumários de produtos, pesquisa, brainstorming)
- Não são necessários ficheiros de dados adicionais para esta etapa
- Foco em critérios de sucesso mensuráveis e específicos
- LEVERAGE documentos de entrada existentes para informar os critérios de sucesso

A sua tarefa:

Defina critérios abrangentes de sucesso que cubram o sucesso do usuário, o sucesso empresarial e o sucesso técnico, usando documentos de entrada como base, permitindo o refinamento do usuário.

## DESCOBERÇÃO DE SUCESSO SEQUÊNCIA:

### 1. Comece a conversa de definição de sucesso

**Verifique documentos de entrada para indicadores de sucesso:**
Analise documentos breves, de pesquisa e de brainstorming de produtos para critérios de sucesso já mencionados.

**Se os documentos de entrada contêm critérios de sucesso:**
"Olhando para o seu resumo do produto e pesquisa, vejo alguns critérios iniciais de sucesso já definidos:

**De seu resumo:**
{{extracted_success_criteria_from_brief}}

**Da investigação:**
{{extracted_success_criteria_from_research}}

**De brainstorming:**
{{extracted_success_criteria_from_brainstorming}}

Isto dá-nos uma grande base. Vamos refinar e expandir esses pensamentos iniciais:

**Primeiro sucesso do usuário:**
Com base no que temos, como você refinaria esses indicadores de sucesso do usuário:

- {{refined_user_success_from_documents}}
- Há outras métricas de sucesso do usuário que devemos considerar?

**O que faria um usuário dizer 'isso valeu a pena'** além do que já foi capturado?

**Se nenhum critério de sucesso em documentos de entrada:**
Comece com o sucesso centrado no usuário:
"Agora que entendemos o que faz {{project_name}" especial, let define como é o sucesso.

**Primeiro sucesso do usuário:**

- O que faria um utilizador dizer que valeu a pena?
Qual é o momento em que percebem que isto resolveu o problema deles?
- Depois de utilizar {{project_name}}, com que resultado estão a afastar-se?

Vamos começar com a experiência de sucesso do usuário."

### 2. Explore as Métricas de Sucesso do Usuário

Ouça os resultados específicos do usuário e ajude a torná-los mensuráveis:

- Guia de vago para específico: NÃO "usuários são felizes" → "usuários completam [action chave] dentro [timeframe]"
- Pergunte sobre o sucesso emocional: "Quando eles se sentem encantados/ aliviados/empoderados?"
- Identificar momentos de sucesso: "Qual é o momento 'aha!'?"
- Defina cenários de conclusão: "O que o 'done' parece para o usuário?"

### 3. Definir o sucesso do negócio

Transição para métricas de negócios:
"Agora o olhar da let sobre o sucesso na perspectiva empresarial.

**Sucesso nos negócios:**

- Como é o sucesso em 3 meses? 12 meses?
Estamos a medir a receita, o crescimento do utilizador, o envolvimento, outra coisa?
- Que métrica faria