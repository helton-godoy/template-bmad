---
name: 'step-07-project-type'
description: 'Conduct project-type specific discovery using CSV-driven guidance'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-07-project-type.md'
nextStepFile: '{workflow_path}/steps/step-08-scoping.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/prd.md'

# Data Files
projectTypesCSV: '{workflow_path}/project-types.csv'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Passo 7: Mergulho profundo tipo projeto

**Progresso: Passo 7 de 11** - Próximo: Scoping

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre colegas de PM
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS sobre requisitos específicos do tipo de projecto e considerações técnicas
- 🎯 DATA-DRIVEN: Use a configuração CSV para guiar a descoberta

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠' Apresentar menu A/P/C após gerar conteúdo do tipo de projeto
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4, 5, 6, 7]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights mais profundos do tipo projeto
- **P (Modo de Festa)**: trazer perspectivas técnicas para explorar os requisitos específicos do projecto
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal das etapas anteriores estão disponíveis
- Tipo de projeto do passo-02 está disponível para carregamento de configuração
- Os dados CSV do tipo de projecto serão carregados nesta etapa
- Foco em requisitos técnicos e funcionais específicos deste tipo de projeto

A sua tarefa:

Realizar uma descoberta específica do tipo de projeto usando orientações orientadas para CSV para definir requisitos técnicos.

## DESCOBERÇÃO DO TÍTULO DE PROJECTOS:

### 1. Carregar dados de configuração do tipo de projeto

Carregar configuração específica do tipo de projeto:

- Carregar `{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd/project-types.csv` completamente
- Encontrar a linha onde o `project_type` corresponde ao tipo detectado a partir do passo- 02
- Extrair estas colunas:
- `key_questions` (lista separada por vírgulas das questões de descoberta)
- `required_sections` (lista separada por vírgulas de secções para documento)
- `skip_sections` (lista separada por vírgulas das secções a saltar)
- `innovation_signals` (já explorada na fase 6)

### 2. Realizar Discovery Guiado Usando Perguntas-chave

Processar `key_questions` da CSV e explorar cada:

#### Descoberta baseada em perguntas:

Para cada pergunta da `key_questions` da CSV:

- Pergunte ao usuário naturalmente em estilo conversacional
- Ouça a sua resposta e peça esclarecimentos de seguimento
- Conectar respostas à proposta de valor do produto

**Exemplo Fluxo:**
Se key questions = "Endpoints needed? ;Método de autenticação?;Formatos de dados?;Limites de taxa?;Versioning?;SDK necessários?"

Pergunte naturalmente:

- "Quais são os principais objetivos que sua API precisa expor?"
- "Como você vai lidar com autenticação e autorização?"
- "Quais formatos de dados você irá apoiar para pedidos e respostas?"

### 3. Requisitos específicos do tipo de projeto do documento

Com base nas respostas do usuário para key questions, sintetize requisitos abrangentes:

#### Categorias de requisitos:

Abrange as áreas indicadas pelo `required_sections` do CSV:

- Sintetizar o que foi descoberto para cada seção necessária
- Documentar requisitos específicos, restrições e decisões
- Conectar ao diferencial de produto quando relevante

#### Ignorar as secções irrelevantes:

Ignorar áreas indicadas pela `skip_sections` da CSV para evitar perder tempo em aspectos irrelevantes.

### 4. Gerar Seções de Conteúdo Dinâmico

Processar a lista `required_sections` da linha CSV correspondente. Para cada nome de seção, gerar conteúdo correspondente:

#### Mapeamentos comuns da secção CSV:

- "endpoint specs" ou "endpoint specification" → Documentação de endpoints da API
- "auth model" ou "autentication model" → Abordagem de autenticação
- "platform reqs" ou "platform requirements" → Necessidades de suporte à plataforma
- "device permissions" ou "disvice features" → Capacidades de dispositivos
- "tenant model" → M