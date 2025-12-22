---
name: 'step-02-design-epics'
description: 'Design and approve the epics_list that will organize all requirements into user-value-focused epics'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/3-solutioning/create-epics-and-stories'

# File References
thisStepFile: '{workflow_path}/steps/step-02-design-epics.md'
nextStepFile: '{workflow_path}/steps/step-03-create-stories.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/epics.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Template References
epicsTemplate: '{workflow_path}/templates/epics-template.md'
---

# Passo 2: Desenho da Lista Épica

## PASSO:

Para projetar e obter aprovação para a lista épica que organizará todos os requisitos em épicos focados no valor do usuário.

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
- ✅ Você traz estratégia de produto e experiência em design épico
- ✅ O usuário traz sua visão de produto e prioridades

### Regras específicas dos passos:

- 🎯 Foco apenas na criação da lista épica
- 🚫 PROJECTO de criar histórias individuais nesta etapa
- 💬 Organize épicos em torno do valor do usuário, não camadas técnicas
- 🚪 Obter aprovação explícita para a lista épica
- 🔗 **CRITICAL: Cada épico deve ser autónomo e permitir épicos futuros sem exigir épicos futuros para function**

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Design épicos com base colaborativamente em requisitos extraídos
- 💾 Actualização {{epics_list}} em {outputFile}
- 📖 Documentar o mapeamento de cobertura FR
- 🚫 FORBIDEN para carregar o próximo passo até que o usuário aprove épicos list

## PROCESSO DE DESENHO EPICO:

### 1. Requisitos extraídos de revisão

Carregar {outputFile} e revisão:

- **Requisitos funcionais:** Contagem e revisão FRs da Etapa 1
- **Requisitos não funcionais:** Reexame das NFR que devem ser abordadas
- **Requisitos complementares:** Reveja os requisitos técnicos e UX

### 2. Explique os princípios do projeto épico

**PRINCÍPIOS DE DESIGNAÇÃO ÉPICOS:**

1. **User-Value First**: Cada épico deve permitir que os usuários realizem algo significativo
2. **Agrupamento de requisitos**: FRs relacionados ao grupo que entregam resultados coesos do usuário
3. **Entrega Incremental**: Cada épico deve entregar valor independentemente
4. **Flow lógico**: Progressão natural da perspectiva do usuário
5. **🔗 Dependência-Livre Dentro Épico**: Histórias dentro de um épico NÃO devem depender de histórias futuras

**⚠□ PRINCÍPIO CRÍTICO:**
Organizar por VALOR UTILIZADOR, não camadas técnicas:

**✅ Exemplos Épicos Correctos (Standalone & Active futuros Épicos):**

- Épico 1: Autenticação e Perfis do Usuário (os usuários podem registrar, login, gerenciar perfis) - **Standalone: sistema de autenticação completo**
- Epic 2: Criação de Conteúdo (os usuários podem criar, editar, publicar conteúdo) - **Standalone: Usa aut; cria conteúdo**
- Épico 3: Interação social (os usuários podem seguir, comentar, como conteúdo) - **Standalone: Usa autth + content**
- Epic 4: Search & Discovery (usuários podem encontrar conteúdo e outros usuários) - **Standalone: Usa todos os anteriores**

**❌ Exemplos épicos errados (camadas técnicas ou dependências):**

- Epic 1: Configuração do Banco de Dados (cria todas as tabelas iniciais) - **Nenhum valor de utilizador**
- Epic 2: API Development (builds all endpoints) - **Nenhum valor de usuário**
- Epic 3: Frontend Components (cria componentes reutilizáveis) - **No user value**
- Épico 4: Pipeline de implantação (configuração CI/CD) - **Nenhum valor de usuário**

**🔗 REGRAS DE DEpendência:**

- Cada épico deve oferecer funcionalidade completa para o seu domínio
- Epic 2 não deve requerer Epic 3 para function
- Epic 3 pode construir sobre Epic 1 & 2 mas deve ficar sozinho

### 3. Design épico estrutura colaborativa

**Passo A: Identificar temas de valor do usuário**

- Procure grupos naturais nos FR
- Identificar viagens de usuário ou fluxos de trabalho
- Considere os tipos de usuários e seus objetivos

**Passo B: Propor estrutura épica**
Para cada épico proposto:

1. **Título Epic**: centrado no utilizador, focado no valor
2. **User Outcome**: O que os usuários podem realizar após este épico
3. **Cobertura FR**: Que números FR este endereço épico
4. **Implementation Notes**: Qualquer consideração técnica ou UX

**Passo C: Criar a lista épica**

Formatar a lista épica como:

```

## Epic List

### Epic 1: [Epic Title]
[Epic goal statement - what users can accomplish]
**FRs covered:** FR1, FR2, FR3, etc.

### Epic 2: [Epic Title]
[Epic goal statement - what users can accomplish]
**FRs covered:** FR4, FR5, FR6, etc.

[Continue for all epics]

```

### 4. Apresentar lista épica para revisão

Mostrar a lista completa de épicos para o utilizador