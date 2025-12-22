---
name: 'step-01-validate-prerequisites'
description: 'Validate required documents exist and extract all requirements for epic and story creation'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/3-solutioning/create-epics-and-stories'

# File References
thisStepFile: '{workflow_path}/steps/step-01-validate-prerequisites.md'
nextStepFile: '{workflow_path}/steps/step-02-design-epics.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/epics.md'
epicsTemplate: '{workflow_path}/templates/epics-template.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Template References
epicsTemplate: '{workflow_path}/templates/epics-template.md'
---

# Passo 1: Validar os Requisitos Pré-requisitos e Extrair

## PASSO:

Para validar que todos os documentos de entrada necessários existem e extrair todos os requisitos (FRs, NFRs, e requisitos adicionais de UX/Arquitetura) necessários para a criação épica e história.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um estrategista de produto e escritor de especificações técnicas
- ✅ Se você já recebeu comunicação ou padrões de persona, continue a usar aqueles enquanto desempenha este novo papel
- ✅ Nós nos engajamos em diálogo colaborativo, não em resposta a comandos
- ✅ Você traz conhecimentos de extração de requisitos
- ✅ O usuário traz sua visão de produto e contexto

### Regras específicas dos passos:

- 🎯 Concentre-se apenas em extrair e organizar requisitos
- 🚫 PROJECTO de começar a criar épicos ou histórias nesta etapa
- 💬 Extrair os requisitos de todos os documentos disponíveis
- 🚪 POPULAR as seções do modelo exatamente como necessário

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Extrair sistematicamente de todos os documentos
- 💾 Popular {outputFile} com requisitos extraídos
- 📖 Actualizar o material frontal com o progresso da extracção
- 🚫 PROIBIDA a carregar o próximo passo até que o usuário selecione 'C' e os requisitos sejam extraídos

## PROCESSO DE EXTRAÇÃO DOS REQUISITOS:

### 1. Boas-vindas e visão geral

Bem-vindo {user_name}ER à criação épica abrangente e história!

**VALIAÇÃO PRÉ-REQUISITA CRÍTICA:**

Verificar os documentos necessários existem e estão completos:

1. **PRD.md** - Contém requisitos (FR e NFRs) e âmbito de aplicação do produto
2. **Architecture.md** - Contém decisões técnicas, contratos de API, modelos de dados
3. **UX Design.md** (se existe UI) - Contém padrões de interação, modelos, fluxos de usuário

### 2. Descoberta de Documentos e Validação

Buscar documentos necessários usando estes padrões (sharded significa que um documento grande foi dividido em vários pequenos arquivos com um index.md em uma pasta) - se o documento inteiro é encontrado, use isso em vez da versão desfiada:

**Prioridade de pesquisa de documentos PRD:**

1. `{output_folder}/*prd*.md` (documento completo)
2. `{output_folder}/*prd*/index.md` (versão danificada)

**Prioridade de pesquisa de documentos de arquitetura:**

1. `{output_folder}/*architecture*.md` (documento completo)
2. `{output_folder}/*architecture*/index.md` (versão emocionada)

**UX Design Document Search (Opcional):**

1. `{output_folder}/*ux*.md` (documento completo)
2. `{output_folder}/*ux*/index.md` (versão emocionada)

Pergunte ao usuário se existem outros documentos, ou se o que você encontrou é tudo o que há [Sim/Não]. Aguarde confirmação do usuário. Uma vez confirmado, criar o {outputFile} a partir do {epicsTemplate} e na matéria dianteira listar os arquivos na matriz de `inputDocuments: []`.

### 3. Requisitos funcionais de extracção (RF)

A partir do documento PRD (completo ou em pedaços), extrair TODAS as exigências funcionais:

**Método de extração:**

- Procure itens numerados como "FR1:", "Requisito Funcional 1:", ou similar
- Identificar as declarações de exigência que descrevem o que o sistema deve fazer
- Incluir ações do usuário, comportamentos do sistema e regras de negócios

**Formatar a lista FR como:**

```
FR1: [Clear, testable requirement description]
FR2: [Clear, testable requirement description]
...

```

### 4. Extrair requisitos não funcionais (NFR)

Do documento PRD, extraia TODAS as exigências não funcionais:

**Método de extração:**

- Procure por desempenho, segurança, usabilidade, requisitos de confiabilidade
- Identificar restrições e atributos de qualidade
- Incluir normas técnicas e requisitos de conformidade

**Formato da lista NFR como:**

```
NFR1: [Performance/Security/Usability requirement]
NFR2: [Performance/Security/Usability requirement]
...

```

### 5. Extrair requisitos adicionais da arquitectura

Reveja o documento de arquitetura para requisitos técnicos que afetam a criação épica e de histórias:

**Procure:**

- **Template Starter**: A arquitectura especifica um template starter/greenfield? Em caso afirmativo, documentar isto para Epic 1 Story 1
- Infra-estruturas e