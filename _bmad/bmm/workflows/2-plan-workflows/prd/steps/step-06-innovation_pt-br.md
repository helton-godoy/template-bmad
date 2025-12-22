---
name: 'step-06-innovation'
description: 'Detect and explore innovative aspects of the product (optional step)'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-06-innovation.md'
nextStepFile: '{workflow_path}/steps/step-07-project-type.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/prd.md'

# Data Files
projectTypesCSV: '{workflow_path}/project-types.csv'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Passo 6: Descoberta da Inovação

**Progresso: Passo 6 de 11** - Próximo: Análise do Tipo de Projeto

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre colegas de PM
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS na detecção e exploração de aspectos inovadores do produto
- 🎯 PASSO OPCIONAL: Só proceder se sinais de inovação são detectados

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠ Apresentar menu A/P/C após gerar conteúdo de inovação
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4, 5, 6]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights de inovação mais profundos
- **P (Modo de Festa)**: trazer perspectivas criativas para explorar oportunidades de inovação
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/\_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/\_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal das etapas anteriores estão disponíveis
- Tipo de projeto a partir do passo-02 está disponível para correspondência de sinal de inovação
- Os dados CSV do tipo de projecto serão carregados nesta etapa
- Foco na detecção de inovação genuína, não na criatividade forçada

## Passo opcional:

Antes de prosseguir com esta etapa, procure sinais de inovação:

- Ouvir linguagem como "nada como isto existe", "pensar como o X funciona"
- Verificar sinais de inovação tipo projeto de CSV
- Procure novas abordagens ou combinações únicas
- Se nenhuma inovação foi detectada, pule esta etapa

A sua tarefa:

Detectar e explorar padrões de inovação no produto, focando no que o torna verdadeiramente novo e como validar os aspectos inovadores.

## SEQUÊNCIA DE DESCUBRA DE INOVAÇÃO:

### 1. Carregar dados de inovação do tipo projeto

Carregar sinais de inovação específicos para este tipo de projeto:

- Carregar `{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd/project-types.csv` completamente
- Encontre a linha onde o `project_type` corresponde ao tipo detectado a partir do passo- 02
- Extrair `innovation_signals` (lista separada por vírgulas)
- Extrair `web_search_triggers` para potencial investigação em inovação

### 2. Ouvir Indicadores de Inovação

Monitore a conversação para sinais de inovação gerais e específicos para projetos:

#### Linguagem de Inovação Geral:

- "Nada como isto existe"
- "Estamos a repensar como funciona"
- "Combinando [A] com [B] pela primeira vez"
- "Abordagem nova ao problema"
- "Ninguém tem done [conceito] antes"

#### Sinais específicos do tipo de projecto (de CSV):

Coincidir descrições do usuário com sinais inovação para seu tipo projeto:

- **api backend**: "Composição API;Novo protocolo"
- **mobile app**: "Inovação de gestos; características AR/VR"
- **saas b2b**: "Automatização do fluxo de trabalho; agentes de IA"
- **developer tool**: **Novo paradigma; Criação de DSL**

### 3.

Faça perguntas direcionadas sobre a descoberta da inovação:
"Enquanto exploramos o {{project_name}}, estou ouvindo o que o torna inovador.

**Indicadores de inovação:**

Estás a desafiar as hipóteses existentes sobre como as coisas funcionam?
- Está a combinar tecnologias ou abordagens de novas formas?
Há alguma coisa nisto que não tenha sido done antes?

Que aspectos do {{project_name}} se sentem mais inovadores para você?"

### 4. Exploração profunda da inovação (se detectada)

Se forem encontrados sinais de inovação, explore profundamente:

#### Perguntas de Inovação Discovery:

- "O que o torna único em comparação com as soluções existentes?"
- "Que suposição estás a desafiar?"
- "Como validamos isso?"
- "Qual é o recuo se não o fizer?"
- "Alguém já tentou isto antes?"

#### Pesquisa de contexto de mercado:

Se