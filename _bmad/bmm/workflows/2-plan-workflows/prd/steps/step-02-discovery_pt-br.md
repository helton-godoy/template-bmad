---
name: 'step-02-discovery'
description: 'Conduct project and domain discovery with data-driven classification'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-02-discovery.md'
nextStepFile: '{workflow_path}/steps/step-03-success.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/prd.md'

# Data Files
projectTypesCSV: '{workflow_path}/project-types.csv'
domainComplexityCSV: '{workflow_path}/domain-complexity.csv'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Passo 2: Descoberta de Projetos e Domínios

**Progresso: Passo 2 de 11** - Próximo: Definição de Critérios de Sucesso

## PASSO:

Realizar uma descoberta abrangente do projeto que aproveita os documentos de entrada existentes, permitindo o refinamento do usuário, com classificação baseada em dados, e gerar o conteúdo do Resumo Executivo.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um facilitador PM focado em produtos colaborando com um par especialista
- ✅ Nós nos engajamos em diálogo colaborativo, não em resposta a comandos
- ✅ Você traz habilidades de pensamento estruturado e facilitação, enquanto o usuário traz conhecimento de domínio e visão de produto

### Regras específicas dos passos:

- 🎯 Foco apenas na classificação do projecto e alinhamento da visão
- 🚫 PROIBIDA para gerar conteúdo sem entrada de usuário real
- 💬 ABORDAGEM: Adaptar perguntas baseadas no contexto do documento (marromfield vs greenfield)
- 🎯 Dados de classificação antes de iniciar a conversa de descoberta

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠ Apresentar menu A/P/C após gerar conteúdo sumário
- 💾 APENAS salve quando o usuário escolher C (Continuar)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights mais profundos sobre o conteúdo gerado
- **P (Modo de Festa)**: trazer múltiplas perspectivas para discutir e melhorar o conteúdo gerado
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {advancedElicitationTask}
- Quando 'P' seleccionado: Executar {partyModeWorkflow}
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal da etapa 1 estão disponíveis
- Os documentos de entrada já carregados estão na memória (sumários do produto, pesquisa, brainstorming, documentos do projeto)
- **Contagens de documentos disponíveis em matéria de fronte `documentCounts`**
- Classificação Os dados CSV serão carregados apenas nesta etapa
- Esta será a primeira secção de conteúdo anexada ao documento

## Sequência de Instruções (Não desvie, salte ou optimize)

### 1. Read Document State from Frontmatter

**PRIMEIRA ACÇÃO CRÍTICA:** Leia a matéria frontal do `{outputFile}` para obter contagens de documentos.

```
Read documentCounts from prd.md frontmatter:
- briefCount = documentCounts.briefs
- researchCount = documentCounts.research
- brainstormingCount = documentCounts.brainstorming
- projectDocsCount = documentCounts.projectDocs

```

**Anunciai o vosso entendimento:**

"A partir do passo 1, carreguei:

- Fichas de produto: {{briefCount}}
Arquivos BMADPROTECT022end BMADPROTECT017end}
Arquivos BMADPROTECT021end BMADPROTECT016end}
- Documentos do projeto: arquivos {{projectDocsCount}}

{if projectDocsCount > 0}Este é um **projeto Brownfield**- Vou focar em entender o que você quer adicionar ou mudar. {else}Este é um**projeto de campo verde** - Vou ajudá-lo a definir a visão completa do produto. {/if}"

### 2. Dados de classificação de carga

Carregar e preparar dados CSV para classificação inteligente:

- Carregar `{projectTypesCSV}` completamente
- Carregar `{domainComplexityCSV}` completamente
- Analisar estruturas de coluna e armazenar na memória para este passo apenas

### 3. Comece a conversa de descoberta

**SELECT EXACTY ONE DISCOVERY PATH baseado no estado do documento:**

---

#### PATH A: Tem resumo do produto (conte > 0)

**Use este caminho quando:** `briefCount > 0`

"Como seu colega de PM, eu revi o seu resumo do produto e tenho um ótimo ponto de partida para nossa descoberta. Deixe-me compartilhar o que eu entendo e você pode refinar ou corrigir conforme necessário.

**Baseado no seu resumo do produto:**

**O que você está construindo:**
{{extracted_vision_from_brief}}

**Problemas que resolve:**
{{extracted_problem_from_brief}}

**Usuários alvo:**
{{extracted_users_from_brief}}

**O que o torna especial:**
{{extracted_differentiator_from_brief}}

{se projecto