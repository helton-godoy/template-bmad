---
name: 'step-04-journeys'
description: 'Map ALL user types that interact with the system with narrative story-based journeys'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-04-journeys.md'
nextStepFile: '{workflow_path}/steps/step-05-domain.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/prd.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Passo 4: Mapeamento de Viagem de Usuário

**Progresso: Passo 4 de 11** - Próximo: Requisitos de Domínio

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre colegas de PM
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS no mapeamento de TODOS os tipos de usuário que interagem com o sistema
- 🎯 CRÍTICA: Nenhuma viagem = nenhum requisito funcional = o produto não existe

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠ Apresentar menu A/P/C após gerar conteúdo de viagem
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights de viagem mais profundos
- **P (Modo de Festa)**: Traga várias perspectivas para mapear jornadas abrangentes do usuário
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal das etapas anteriores estão disponíveis
- Critérios de sucesso e âmbito de aplicação já definidos
- Documentos de entrada a partir da etapa-01 estão disponíveis (sumários do produto com personas do usuário)
- Cada interação humana com o sistema precisa de uma jornada

A sua tarefa:

Crie jornadas de usuário narrativa convincentes que aproveitam personas existentes a partir de resumos de produtos e identifique tipos de usuários adicionais necessários para uma cobertura abrangente.

REVISTA MANTER SEQUÊNCIA:

### 1. Aproveite os usuários existentes e identifique tipos adicionais

**Verifique documentos de entrada para Personas existentes:**
Analise os documentos breves, de pesquisa e de brainstorming do produto para personas do usuário já definidas.

**Se o usuário Personas existe em documentos de entrada:**
"Encontrei algumas personas fantásticas do usuário em seu resumo do produto! Deixe-me apresentá-los e ver se precisamos expandir nosso elenco de personagens.

**De seu resumo:**
{{extracted_personas_from_brief_with_details}}

Estes são ótimos pontos de partida! Suas histórias já nos dão uma visão do que eles precisam da {{project_name}}.

**Para além dos utilizadores identificados, quem mais toca neste sistema?**
Com base no seu tipo de produto e escopo, podemos precisar:

{{suggest_additional_user_types_based_on_project_context}}

Que tipos de usuários adicionais devemos considerar para este produto?"

**Se nenhuma pessoa em documentos de entrada:**
Comece com uma descoberta abrangente do tipo de usuário:
"Agora que sabemos como é o sucesso, o mapa da let todas as pessoas que irão interagir com a {{project_name}}.

**Além dos usuários primários, quem mais toca neste sistema?**
Consider:

- Usuários finais (o foco principal)
- Administradores - gerenciar usuários, configurações, conteúdo
- Moderadores - revisão de conteúdo sinalizado, aplicar regras
- Equipe de suporte - ajudar usuários, investigar problemas
- Consumidores de API - se ferramenta dev ou plataforma
- Operações internas - análise, monitoramento, faturamento

Que tipos de usuário devemos mapear para este produto?"

### 2. Crie viagens baseadas em histórias narrativas

Para cada tipo de usuário, crie jornadas narrativas convincentes que contam sua história:

#### Processo de Criação de Viagem Narrativa:

**Se usar Persona existente de documentos de entrada:**
Vamos contar a história do {{persona_name} com o {{project_name}}.

**Sua história até agora:**
{{persona_backstory_from_brief}}

**Como {{project_name}} Muda sua vida:**
{{how_product_helps_them}

Vamos criar sua narrativa de viagem - onde vamos encontrá-los em sua história, e como {{project_name}} ajudá-los a escrever seu próximo capítulo?"

**Se criar uma nova pessoa:**
"Vamos dar vida a esse tipo de usuário com uma história convincente.

**Criando seu caráter:**

- **Nome**: Dê-lhes um nome e personalidade realistas
- **Situação**: O que está acontecendo em sua vida/trabalho que cria a necessidade?
- “Objetivo”: O que eles desesperado