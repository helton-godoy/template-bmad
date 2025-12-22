---
name: 'step-09-functional'
description: 'Synthesize all discovery into comprehensive functional requirements'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-09-functional.md'
nextStepFile: '{workflow_path}/steps/step-10-nonfunctional.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/prd.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Etapa 9: Síntese dos requisitos funcionais

**Progresso: Passo 9 de 11** - Próximo: Requisitos Não Funcionais

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre colegas de PM
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS na criação de inventário de capacidade abrangente para o produto
Este é o contrato de CAPABILIDADE para todos os trabalhos a jusante

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠ Apresentar menu A/P/C após gerar requisitos funcionais
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para garantir uma cobertura abrangente de requisitos
- **P (Modo de Festa)**: Traga várias perspectivas para validar o conjunto completo de requisitos
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/\_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/\_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal das etapas anteriores estão disponíveis
- TODOS os conteúdos anteriores (resumo executivo, critérios de sucesso, viagens, domínio, inovação, tipo de projecto) devem ser referenciados
- Não são necessários ficheiros de dados adicionais para esta etapa
- Foco nas capacidades, não implementation detalhes

## IMPORTÂNCIA CRÍTICA:

**Esta secção define o contrato de CAPABILIDADE para todo o produto:**

- Os designers de UX só irão projetar o que está listado aqui
- Arquitetos só irão apoiar o que está listado aqui
- A desagregação épica só irá implementar o que está listado aqui
- Se falta uma capacidade de FR, não existirá no produto final

## REQUISITOS FUNCIONAIS SÍNTESE SEQUÊNCIA:

### 1. Compreenda o propósito e uso da FR

Comece explicando o papel crítico dos requisitos funcionais:

**Proporção:**
FRs definem quais as capacidades que o produto deve ter. Eles são o inventário completo de recursos voltados para o usuário e do sistema que proporcionam a visão do produto.

**Propriedades críticas:**
✅ Cada FR é uma capacidade testável
✅ Cada FR é implementation-agnóstico (pode ser construído de muitas maneiras)
✅ Cada FR especifica Quem e O QUE, não COMO
✅ Sem detalhes de UI, sem números de desempenho, sem opções de tecnologia
✅ Cobertura abrangente das áreas de capacidade

**Como serão usados:**

1. UX Designer lê FRs → projeta interações para cada capacidade
2. Arquiteto lê FRs → projeta sistemas para suportar cada capacidade
3. PM lê FRs → cria épicos e histórias para implementar cada capacidade

### 2. Revisão do conteúdo existente para extração de capacidade

Revise sistematicamente todas as seções anteriores para extrair as capacidades:

**Extrair de:**

- Resumo Executivo → Principais capacidades de diferenciação de produtos
- Critérios de sucesso → Capacidades de sucesso
- Viagens de Usuário → Recursos revelados pela viagem
- Requisitos de Domínio → Compliance e capacidades regulatórias
- Padrões de Inovação → Recursos de recursos inovadores
- Requisitos do tipo de projeto → Necessidades de capacidade técnica

### 3. Organizar os requisitos por área de capacidade

Grupo FR por áreas de capacidade lógica (NOT por tecnologia ou camada):

**Bom exemplo de agrupamento:**

- ✅ "Gestão do Usuário" (não "Sistema de autenticação")
- ✅ "Content Discovery" (não "Procurar Algoritmo")
- ✅ "Colaboração de Equipa" (não "WebSocket Infrastructure")

**Alvo 5-8 Áreas de Capacidade** para projetos típicos.

### 4. Gerar Lista FR abrangente

Criar requisitos funcionais completos usando este formato:

**Formato:**

- FR#: [Actor] pode [capacidade] [contexto/restrição, se necessário]
- Número sequencialmente (FR1, FR2, FR3...)
- Objectivo de 20-50 FR para projectos típicos

**Verificação de altitude:**
Cada FR deve responder "WHAT capacidade existe?" "Como é que é implementado