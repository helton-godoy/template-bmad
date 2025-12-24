---
name: 'step-10-nonfunctional'
description: 'Define quality attributes that matter for this specific product'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-10-nonfunctional.md'
nextStepFile: '{workflow_path}/steps/step-11-complete.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/prd.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Etapa 10: Requisitos não funcionais

**Progresso: Passo 10 de 11** - Próximo: PRD completo

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre colegas de PM
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS sobre os atributos de qualidade que importam para este produto específico
- 🎯 SELECTIVA: Apenas documentos NFR que se aplicam ao produto

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠' Apresentar menu A/P/C após gerar conteúdo NFR
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para garantir atributos de qualidade abrangentes
- **P (Modo de Festa)**: Apresentar perspectivas técnicas para validar a completude NFR
- **C (Continua)**: Salve o conteúdo no documento e prossiga para a etapa final

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal das etapas anteriores estão disponíveis
- Os requisitos funcionais já definidos e informarão os QNF
- Contexto de domínio e tipo de projeto irá orientar quais NFRs importam
- Foco em critérios de qualidade específicos e mensuráveis

A sua tarefa:

Defina requisitos não funcionais que especifiquem atributos de qualidade para o produto, focando apenas no que importa para este produto específico.

## REQUISITOS NÃO FUNCIONAIS SEQUÊNCIA:

### 1. Explicar a finalidade e o âmbito de aplicação da NFR

Comece por esclarecer o que são NFRs e por que somos seletivos:

**Propósito NFR:**
Os NFRs definem COMO O sistema deve funcionar, não O QUE deve fazer. Eles especificam atributos de qualidade como desempenho, segurança, escalabilidade, etc.

**Abordagem selectiva:**
Nós só documentamos NFRs que importam para este produto. Se uma categoria não se aplica, nós pulamos completamente. Isso evita o inchaço da exigência e foca no que é realmente importante.

### 2. Avaliar o contexto do produto para a relevância NFR

Avaliar as categorias NFR que importam com base no contexto do produto:

**Questões de avaliação rápida:**

- **Performance**: Existe impacto de velocidade voltado para o utilizador?
- **Segurança**: Tratamos de dados ou pagamentos sensíveis?
- **Escalabilidade**: Esperamos um rápido crescimento do utilizador?
- **Acessibilidade**: Estamos a servir grandes audiências públicas?
- **Integração**: Precisamos de nos ligar a outros sistemas?
- **Fiabilidade**: o tempo de paragem causaria problemas significativos?

### 3. Explore as categorias NFR relevantes

Para cada categoria relevante, realizar a descoberta orientada:

#### NFR de desempenho (se relevante):

"Vamos falar sobre requisitos de desempenho para {{project_name}}.

**Performance Questions:**

- Que partes do sistema precisam ser rápidas para que os usuários tenham sucesso?
- Há expectativas específicas de tempo de resposta?
- O que acontece se o desempenho for mais lento do que o esperado?
- Há cenários de usuários simultâneos que precisamos apoiar?"

#### NFR de segurança (se relevante):

"A segurança é fundamental para produtos que lidam com informações sensíveis.

**Perguntas de segurança:**

- Que dados precisam de ser protegidos?
- Quem deve ter acesso a quê?
- Quais são os riscos de segurança?
- Existem requisitos de conformidade (GDPR, HIPAA, PCI-DSS)?"

#### NFR de escalabilidade (se relevante):

"A escalabilidade importa se esperamos crescimento ou se temos demanda variável.

**Questões de Escalabilidade:**

- Quantos usuários esperamos inicialmente? A longo prazo?
- Há picos de tráfego sazonais ou de eventos?
- O que acontece se excedermos a nossa capacidade?"
- Que cenários de crescimento devemos planear?"

#### NFR de acessibilidade (se relevante):

"A acessibilidade garante que o produto funcione para usuários com deficiência.

**Perguntas de acessibilidade:**

- Estamos servindo usuários com impai visual, auditivo ou motor