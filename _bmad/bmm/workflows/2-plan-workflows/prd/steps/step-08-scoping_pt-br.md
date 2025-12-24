---
name: 'step-08-scoping'
description: 'Define MVP boundaries and prioritize features across development phases'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-08-scoping.md'
nextStepFile: '{workflow_path}/steps/step-09-functional.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/prd.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Passo 8: Exercício de Scoping - MVP & Características futuras

**Progresso: Passo 8 de 11** - Próximo: Requisitos Funcionais

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre colegas de PM
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS sobre as decisões de âmbito estratégico que mantêm os projectos viáveis
- 🎯 EMFASSAM o pensamento de MVP magro enquanto preservam a visão a longo prazo

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 📚 Reveja o documento PRD completo construído até agora
- ⚠ Apresentar menu A/P/C após gerar decisões de escopo
- 💾 SOMENTE salvar quando o usuário escolher C (Continuar)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para explorar abordagens inovadoras de escopo
- **P (Modo de Partida)**: trazer múltiplas perspectivas para garantir decisões abrangentes de âmbito
- **C (Continua)**: Salve as decisões de escopo e proceda aos requisitos funcionais

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre para exibir o menu A/P/C deste passo após o A ou P terem completado
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento PRD completo construído até agora está disponível para revisão
- Viagens do usuário, critérios de sucesso e requisitos de domínio estão documentados
- Foco nas decisões de escopo estratégico, não em detalhes
- Equilíbrio entre valor do usuário e viabilidade implementation

A sua tarefa:

Realize um exercício de escopo abrangente para definir os limites do MVP e priorizar recursos em todas as fases de desenvolvimento.

## SCOPING SEQUÊNCIA:

### 1.

Analise tudo documentado até agora:
"Eu revi o seu PRD completo até agora. Eis o que estabelecemos:

**Visão e sucesso do produto:**
{{summary_of_vision_and_success_criteria}}

**User Journeys:** {{number_of_journeys}} mapeado com narrativas ricas

**Domain & Innovation Focus:**
{{summary_of_domain_requirements_and_innovation}}

**Implicações atuais do escopo:**
Baseado em tudo o que documentámos, parece que pode ser:

- MVP simples (pequena equipa, escopo magro)
- [ ] Âmbito médio (equipa moderada, características equilibradas)
- [ ] Projeto complexo (grande equipe, escopo abrangente)

Essa avaliação inicial parece correta, ou você vê isso de forma diferente?"

### 2. Definir estratégia MVP

Facilitar decisões estratégicas MVP:

"Vamos pensar estrategicamente sobre sua estratégia de lançamento:

**Opções de Filosofia MVP:**

1. **MVP solucionador de problemas**: Resolver o problema principal com recursos mínimos
2. **Experience MVP**: Oferecer a experiência chave do usuário com funcionalidade básica
3. **Plataforma MVP**: Construir a base para a expansão futura
4. **Revenue MVP**: Gerar receita antecipada com características essenciais

**Perguntas críticas:**

- Qual é o mínimo que faria os usuários dizer "isso é útil"?
- O que faria os investidores/parceiros dizerem "isto tem potencial"?
Qual é o caminho mais rápido para a aprendizagem validada?

**Que abordagem MVP parece certa para {{project_name}}?**

### 3. Quadro da Decisão de Scoping

Utilizar a tomada de decisão estruturada para o âmbito de aplicação:

**É preciso ter uma análise:**
"Vamos identificar necessidades absolutas de MVP. Para cada critério de viagem e sucesso, pergunte:

- **Sem isso, o produto falha?** (Y/N)
- **Pode ser manual inicialmente?** (Y/N)
- **Isto é uma quebra de negócio para os primeiros adotivos?** (Y/N)

**Revisão atual do documento:**
Olhando para suas jornadas de usuário, quais são as experiências centrais absolutas que devem funcionar?

{{analyze_journeys_for_mvp_essentials}}"

**Análise agradável de ter:**
"Vamos também identificar o que poderia ser adicionado mais tarde:

**Melhoramentos pós-MVP:**

- Características que melhoram, mas não são essenciais
- Tipos de usuário que podem ser adicionados mais tarde
- Funcionalidade avançada que se baseia no MVP

**Quais recursos poderíamos adicionar nas versões 2, 3, etc?**

##