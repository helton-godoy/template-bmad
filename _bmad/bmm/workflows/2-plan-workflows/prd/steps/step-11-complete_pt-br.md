---
name: 'step-11-complete'
description: 'Complete the PRD workflow, update status files, and suggest next steps'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-11-complete.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/prd.md'
---

# Etapa 11: Completação do fluxo de trabalho

**Passo Final - Complete o PRD**

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

Este é um passo final.

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- 🛑 NÃO geração de conteúdo - esta é uma etapa de encerramento
- 📋 Finalizar documento e atualizar o estado do fluxo de trabalho
- 💬 FOCUS na conclusão, próximos passos, e sugestões
- 🎯 UPDATE arquivos de estado de fluxo de trabalho com informações de conclusão

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Atualizar o arquivo principal do estado do fluxo de trabalho com informações de conclusão
- 📖 Sugerir os próximos passos de fluxo de trabalho potenciais para o usuário
- 🚫 NÃO carregar etapas adicionais após esta

## PROTOCOLOS DE TERMINAÇÃO:

- Este é um passo final - a conclusão do fluxo de trabalho necessária
- Saída de qualquer conteúdo restante, se necessário (nenhum para esta etapa)
- Atualizar o arquivo principal do estado do fluxo de trabalho com documento finalizado
- Sugerir os próximos passos potenciais para o usuário
- Marcar o fluxo de trabalho como completo no rastreamento de status

## CONTEXTO MONTANTES:

- Documento PRD completo está disponível em todas as etapas anteriores
- O frontmatter do fluxo de trabalho mostra todos os passos completados
- Todo o conteúdo colaborativo foi gerado e salvo
- Foco na conclusão, validação e próximos passos

A sua tarefa:

Complete o fluxo de trabalho PRD, atualize arquivos de status e sugira os próximos passos para o projeto.

## SEQUÊNCIA DE COMPLEÇÃO DO FLUXO DE TRABALHO:

### 1. Anunciar conclusão do fluxo de trabalho

Informe o usuário que o PRD está completo:
"🎉 **PRD Complete, BMADPROTECT013end}!**

Eu colaborei com sucesso com você para criar um documento abrangente de requisitos de produto para {{project_name}}.

**O que conseguimos:**

- ✅ Resumo Executivo com visão e diferencial de produtos
- ✅ Critérios de sucesso com resultados mensuráveis e definição de âmbito
- ✅ Viagens de Usuário cobrindo todos os padrões de interação
- ✅ Requisitos específicos de domínio (se aplicável)
- ✅ Análise da inovação (se aplicável)
- ✅ Requisitos técnicos específicos do tipo de projecto
- ✅ Requisitos funcionais abrangentes (contrato de capacidade)
- ✅ Requisitos não funcionais para atributos de qualidade

**O PRD completo está agora disponível em:** `{output_folder}/prd.md`

Este documento está agora pronto para orientar o projeto, arquitetura técnica e desenvolvimento de UX planning."

### 2. Atualização do estado do fluxo de trabalho

Atualizar o arquivo principal de estado do fluxo de trabalho:

- Carregar `{status_file}` da configuração do fluxo de trabalho (se existir)
- Atualizar workflow status["prd"] = "{default_output_file}"
- Salvar arquivo, preservando todos os comentários e estrutura
- Marcar a hora atual como tempo de conclusão

### 3. Sugerir Passos Próximos

Fornecer orientação sobre os próximos fluxos de trabalho lógicos:

**Típico Próximo Fluxos de Trabalho:**

**Imediate Next Steps:**

1. `workflow create-ux-design` - UX Design (se a UI existir)
- Os insights da viagem do usuário da etapa-04 informarão o projeto da interação
- Requisitos funcionais da etapa-09 definir escopo de projeto

2. `workflow create-architecture` - Arquitetura técnica
- Requisitos de tipo de projeto de passo-07 guia decisões técnicas
- Requisitos não funcionais da etapa 10 informam as escolhas de arquitetura

3. `workflow create-epics-and-stories` - Discriminação épica
- Requisitos funcionais do passo-09 tornar-se épicos e histórias
- Definição de escopo do passo-03 guias sprint planning

**Considerações estratégicas:**

- Design e arquitetura UX pode acontecer em paralelo
- Épicos/história são mais ricos quando criados após UX/arquitetura
- Considere a capacidade e prioridades da sua equipe

**O que seria mais valioso para enfrentar em seguida?**

### 4. Verificação da qualidade do documento

Realizar a validação final do PRD:

**Verificação de conclusão:**

O resumo executivo comunica claramente a visão?
- Os critérios de sucesso são específicos e mensuráveis?
- As viagens de usuários cobrem todos os tipos de usuários principais?
- Os requisitos funcionais são abrangentes e testáveis?
- Os requisitos não funcionais são relevantes e específicos?

**Verificação de coerência:**

- Todas as seções se alinham com o diferenciador do produto?
- O alcance é consistente em todas as secções?
- Os requisitos são rastreáveis para as necessidades do usuário e critérios de sucesso?

### 5. Confirmação final da conclusão

Confirmar a conclusão com o utilizador:
"**Seu PRD para {{project_name}} está agora completo e pronto para a próxima fase!**

O documento contém tudo o que é necessário para orientar:

- Decisões de concepção UX/UI
- Arquitetura técnica planning
- Priorização do desenvolvimento e sprint planning

**Pronto para continuar com:**

- Fluxo de trabalho de design UX?
- Fluxo de trabalho de arquitectura?
- Criação épica e de histórias?

**Ou w