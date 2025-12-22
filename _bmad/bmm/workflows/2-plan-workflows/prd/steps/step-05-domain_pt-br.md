---
name: 'step-05-domain'
description: 'Explore domain-specific requirements for complex domains (optional step)'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-05-domain.md'
nextStepFile: '{workflow_path}/steps/step-06-innovation.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/prd.md'

# Data Files
domainComplexityCSV: '{workflow_path}/domain-complexity.csv'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Etapa 5: Exploração Específica de Domínio

**Progresso: Passo 5 de 11** - Próximo: Inovação Foco

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre colegas de PM
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS sobre requisitos específicos de domínio e necessidades de conformidade
- 🎯 PASSO OPCIONAL: Só prosseguir se complexidade nível = "alto" a partir do passo- 02

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠ Apresentar menu A/P/C após gerar conteúdo de domínio
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4, 5]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights de domínio mais profundos
- **P (Modo de Festa)**: Traga perspectivas de especialização de domínio para explorar requisitos
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal das etapas anteriores estão disponíveis
- Complexidade de domínio do passo-02 deve ser "alta" para justificar esta etapa
- Dados CSV específicos do domínio serão carregados nesta etapa
- Foco em conformidade, regulamentos e restrições específicas de domínio

## Passo opcional:

Antes de prosseguir com esta etapa, verifique:

- O `complexity_level` do passo-02 é igual a "alto" e/ou o domínio tem necessidades específicas de regulação/conformidade?
- A exploração de domínio teria impacto significativo nos requisitos do produto?

Se não a essas perguntas, pule esta etapa e carregue `{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd/steps/step-06-innovation.md`.

A sua tarefa:

Explore requisitos específicos de domínio para domínios complexos que precisam de considerações especializadas de conformidade, regulatórias ou específicas do setor.

SEQUÊNCIA DE EXPLORAÇÃO DO DOMAIN:

### 1. Carregar dados de configuração de domínio

Carregar a configuração específica do domínio para domínios complexos:

- Carregar `{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd/domain-complexity.csv` completamente
- Encontre a linha onde o `domain` corresponde ao domínio detectado a partir do passo- 02
- Extrair estas colunas:
- `key_concerns` (lista separada por vírgulas)
- `required_knowledge` (exigência de competências de domínio)
- `web_searches` (consultas de investigação sugeridas)
- `special_sections` (secções específicas do domínio do documento)

### 2. Contexto atual de complexidade de domínio

Comece explicando por que este passo é necessário:
"Como {{project_name}} está no domínio {domain} com alta complexidade, precisamos explorar requisitos específicos de domínio.

**As principais preocupações para {domain}ER:**
[Lista das preocupações chave de CSV]

Este passo nos ajudará a entender os requisitos regulatórios, as necessidades de conformidade e as restrições específicas do setor que irão moldar nosso produto."

### 3. Explore requisitos específicos de domínio

Para cada preocupação no `key_concerns` do CSV:

#### Exploração de Domínio:

- Pergunte ao usuário sobre sua abordagem para esta preocupação
- Discutir implicações para o design do produto e requisitos
- Documentar requisitos específicos, restrições e necessidades de conformidade

**Exemplo para o domínio da saúde:**
Se key preocupações = "Aprovação FDA;Validação clínica;Compliance HIPAA;Segurança do paciente;Classificação do dispositivo médico;Responsabilidade"

Pergunte sobre cada um:

- "Será que este produto requer aprovação da FDA? Que classificação?"
- "Como você vai validar a precisão clínica e segurança?"
- "Que medidas de conformidade HIPAA são necessárias?"
- "Que protocolos de segurança devem estar em vigor?"
- "Que considerações de responsabilidade afetam o projeto?"

### 4. Requisitos de Domínio de Sintetização

Com base na conversa, sintetize requisitos de domínio que irão moldar tudo