---
name: 'step-03-create-stories'
description: 'Generate all epics with their stories following the template structure'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/3-solutioning/create-epics-and-stories'

# File References
thisStepFile: '{workflow_path}/steps/step-03-create-stories.md'
nextStepFile: '{workflow_path}/steps/step-04-final-validation.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/epics.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Template References
epicsTemplate: '{workflow_path}/templates/epics-template.md'
---

# Passo 3: Gerar Épicos e Histórias

## PASSO:

Para gerar todos os épicos com suas histórias baseadas no épico aprovado list, seguindo a estrutura do modelo exatamente.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
Processo épico sequencialmente
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um estrategista de produto e escritor de especificações técnicas
- ✅ Se você já recebeu comunicação ou padrões de persona, continue a usar aqueles enquanto desempenha este novo papel
- ✅ Nós nos engajamos em diálogo colaborativo, não em resposta a comandos
- ✅ Você traz conhecimento sobre criação de histórias e critérios de aceitação
- ✅ O usuário traz suas prioridades e restrições implementation

### Regras específicas dos passos:

- 🎯 Gerar histórias para cada épico seguindo exatamente o modelo
- 🚫 PROIBIDA a se desviar da estrutura do modelo
- 💬 Cada história deve ter critérios de aceitação claros
- 🚪 ENTENDER que cada história é completável por um único agente
- 🔗 **Critical: Histórias NÃO DEVEM depender de histórias futuras dentro do mesmo épico**

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Gerar histórias colaborativamente com a entrada do usuário
- 💾 Adicionar épicos e histórias ao {outputFile} seguindo o modelo
- 📖 Processo épicos um de cada vez em sequência
- 🚫 PROCURADO para pular qualquer épico ou correr através de histórias

## PROCESSO DE GERAÇÃO:

### 1. Carregar a estrutura épica aprovada

Carregar {outputFile} e revisão:

- Lista épica aprovada do Passo 2
- Mapa de cobertura FR
- Todos os requisitos (FR, NFR, adicional)
- Estrutura do modelo no final do documento

### 2. Explique a abordagem de criação de história

**ORIENTAÇÕES DE CRIAÇÃO DE história:**

Para cada épico, crie histórias que:

- Siga a estrutura exata do modelo
- São dimensionados para a completação do agente de dev único
- Ter valor de utilizador claro
- Incluir critérios de aceitação específicos
- requisitos de referência cumpridos

**🚨 PRINCÍPIO DE CRIAÇÃO DA BASE DE DADOS/ENTIDADE:**
Crie tabelas/entidades APENAS quando necessário pela história:

Epic 1 Story 1 cria todas as 50 tabelas de banco de dados
Cada história cria/altera SOMENTE as tabelas de que precisa

**🔗 PRINCÍPIO DA DEPENDÊNCIA:**
As histórias devem ser completas independentemente em sequência:

A história 1.2 requer que a história 1.3 seja completada primeiro.
- ✅ Certo: Cada história pode ser concluída com base apenas em histórias anteriores
- ❌ ERRADO: "Esperar que a História 1.4 seja implementada antes que isto funcione"
- ✅ Certo: "Esta história funciona independentemente e permite histórias futuras"

**Formato de história (do modelo):**

```

### Story {N}.{M}: {story_title}

As a {user_type},
I want {capability},
So that {value_benefit}.

**Acceptance Criteria:**

**Given** {precondition}
**When** {action}
**Then** {expected_outcome}
**And** {additional_criteria}

```

**✅ BOAS HISTÓRIAS:**

*Epic 1: Autenticação do Usuário*

- História 1.1: Registro de Usuário com Email
- História 1.2: Login do Usuário com Senha
- História 1.3: Reiniciar senha via Email

*Epic 2: Criação de Conteúdo*

- História 2.1: Criar Novo Blog Post
- História 2.2: Editar Blog existente
- História 2.3: Publicar Blog Post

**EMJ27**

- Story: "Set up database" (sem valor de utilizador)
- Story: "Create all models" (muito grande, sem valor de usuário)
- Story: "Build authentication system" (muito grande)
- Story: "Login UI (depends on Story 1.3 API endpoint)" (dependência futura!)
- Story: "Edit post (requires Story 1.4 to be implemented first)" (ordem errada!)

### 3. Process Epics Sequencialmente

Para cada épico na lista aprovada:

#### A. Visão geral épica

Display:

- Número e título épicos
- Declaração do objetivo épico
- FRs cobertos por este épico
- Quaisquer NFR ou requisitos adicionais relevantes

#### B. Repartição da História

Trabalhe com o usuário para dividir o épico em histórias:

- Identificar capacidades de utilizador distintas
- Garantir o fluxo lógico dentro do épico
- Tamanho histórias apropriadamente

#### C. Gerar cada história

Para cada história no épico:

1. **Título da história**: claro, orientado para a acção
2. **User Story**: Complete o formato As a/I want/So that format
3. **Critérios de aceitação**: Escrever critérios específicos e testáveis

**AC Redação Diretrizes:**

- Usar o formato dado/quando/então
- Cada AC deve ser testado independentemente
- Incluir casos de borda e condições de erro
- Exigências específicas de referência