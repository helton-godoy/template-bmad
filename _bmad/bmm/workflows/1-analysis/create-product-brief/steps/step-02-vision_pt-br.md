---
name: 'step-02-vision'
description: 'Discover and define the core product vision, problem statement, and unique value proposition'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/1-analysis/product-brief'

# File References
thisStepFile: '{workflow_path}/steps/step-02-vision.md'
nextStepFile: '{workflow_path}/steps/step-03-users.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/analysis/product-brief-{{project_name}}-{{date}}.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Passo 2: Visão do produto Discovery

## PASSO:

Conduzir uma descoberta abrangente da visão do produto para definir o problema principal, solução e proposta de valor única através de análise colaborativa.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um facilitador de análise de negócios focado no produto
- ✅ Se você já recebeu um nome, communication style e persona, continue usando-os enquanto desempenha este novo papel
- ✅ Nós nos engajamos em diálogo colaborativo, não em resposta a comandos
- ✅ Você traz habilidades de pensamento estruturado e facilitação, enquanto o usuário traz conhecimento de domínio e visão de produto
- ✅ Mantenha o tom de descoberta colaborativo ao longo

### Regras específicas dos passos:

- 🎯 Concentre-se apenas na visão do produto, problema e descoberta de soluções
- 🚫 PROIBIDA a gerar visão sem entrada e colaboração real do usuário
- 💬 Aproximação: Descoberta sistemática do problema à solução
- 📋 Descoberta COLABORATIVA, não criação de visão baseada em suposições

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Gerar conteúdo de visão colaborativamente com o usuário
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2]` antes de carregar o próximo passo
- 🚫 PROIBIDO proceder sem confirmação do utilizador através do menu

## CONTEXTO MONTANTES:

- Contexto disponível: Documento atual e matéria frontal da etapa 1, documentos de entrada já carregados na memória
- Focus: Esta será a primeira secção de conteúdo anexada ao documento
- Limits: Foque-se na visão clara e convincente do produto e na indicação do problema
- Dependencies: A inicialização do documento a partir do passo-01 deve estar completa

## Sequência de Instruções (Não desvie, salte ou optimize)

### 1. Iniciar a Descoberta da Visão

**Abrir conversa:**
"Como seu colega do PM, estou animado para ajudá-lo a moldar a visão para {{project_name}}. Vamos começar pela fundação.

**Me fale sobre o produto que você imagina:**

- Que problema está a tentar resolver?
- Quem experimenta este problema mais intensamente?
Qual seria o sucesso das pessoas que estás a ajudar?
- O que te excita mais nesta solução?

Vamos começar com o espaço do problema antes de entrar em soluções."

### 2. Compreensão profunda de problemas

**Descoberta de Problemas:**
Explore o problema de vários ângulos usando perguntas direcionadas:

- Como é que as pessoas resolvem este problema?
- O que é frustrante nas soluções atuais?
- O que acontece se este problema não for resolvido?
- Quem sente esta dor mais intensamente?

### 3. Análise de soluções atuais

**Paisagem competitiva:**

- Que soluções existem hoje?
- Onde é que eles ficam aquém?
- Que lacunas deixam abertas?
Porque é que as soluções existentes não resolveram isto completamente?

### 4. Visão da solução

**Colaborative Solution Crafting:**

Se pudéssemos resolver isto perfeitamente, como seria?
Qual é a maneira mais simples de fazermos uma diferença significativa?
O que torna a tua abordagem diferente do que há lá fora?
- O que faria os usuários dizerem "isso é exatamente o que eu precisava"?

### 5. Diferenciadores únicos

**Advantage competitivo:**

- Qual é a tua vantagem injusta?
- O que seria difícil para os concorrentes copiarem?
- Que visão ou abordagem é única?
- Porque é a altura certa para esta solução?

### 6. Gerar Conteúdo Sumário Executivo

**Content to Append:**
Preparar a seguinte estrutura para o anexo do documento:

```markdown

## Executive Summary

[Executive summary content based on conversation]

---

## Core Vision

### Problem Statement

[Problem statement content based on conversation]

### Problem Impact

[Problem impact content based on conversation]

### Why Existing Solutions Fall Short

[Analysis of existing solution gaps based on conversation]

### Proposed Solution

[Proposed solution description based on conversation]

### Key Differentiators

[Key differentiators based on conversation]

```

### 7.

**Content Presentation:**
"Eu redigi o resumo executivo e visão central com base em nossa conversa. Isto captura a essência do {{project_name}} e o que o torna especial.

Aqui está o que vou adicionar ao docum