---
name: 'step-05-scope'
description: 'Define MVP scope with clear boundaries and outline future vision while managing scope creep'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/1-analysis/product-brief'

# File References
thisStepFile: '{workflow_path}/steps/step-05-scope.md'
nextStepFile: '{workflow_path}/steps/step-06-complete.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/analysis/product-brief-{{project_name}}-{{date}}.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Etapa 5: Definição do âmbito de aplicação do MVP

## PASSO:

Definir escopo MVP com fronteiras claras e delinear visão futura através de negociação de escopo colaborativo que equilibra ambição com realismo.

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

- 🎯 Concentre-se apenas na definição do âmbito mínimo viável e na visão futura
- 🚫 PROIBIDO a criar escopo MVP que é muito grande ou inclui características não essenciais
- 💬 Abordagem: Negociação de âmbito sistemático com definição clara de limites
- 📋 Definição de âmbito COLABORATIVO que previne a fluência de âmbito

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Gerar escopo MVP colaborativamente com o usuário
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4, 5]` antes de carregar o próximo passo
- 🚫 PROIBIDO proceder sem confirmação do utilizador através do menu

## CONTEXTO MONTANTES:

- Contexto disponível: Documento atual e matéria frontal das etapas anteriores, visão de produto, usuários e métricas de sucesso já definidas
- Focus: Definir o que é essencial para MVP vs. melhorias futuras
- Limits: Equilibrar as necessidades do usuário com a viabilidade implementation
- Dependencies: Visão do produto, personas do usuário e métricas de sucesso de etapas anteriores devem estar completas

## Sequência de Instruções (Não desvie, salte ou optimize)

### 1. Iniciar definição de escopo

**Exploração de Abertura:**
"Agora que entendemos o que {{project_name}} faz, quem serve, e como vamos medir o sucesso, let define o que precisamos construir primeiro.

**Scope Discovery:**

Qual é o mínimo que precisamos para resolver o problema principal?
- Quais recursos fariam os usuários dizer "isso resolve o meu problema"?
Como equilibrar a ambição com algo valioso para os usuários rapidamente?

Vamos começar com a mentalidade MVP: qual é a menor versão que cria valor real?"

### 2. MVP Principais Características Definição

**Perguntas de Característica do MVP:**
Definir características essenciais para o produto mínimo viável:

- "Qual é a funcionalidade principal que deve funcionar?"
- "Quais recursos abordam diretamente o problema principal que estamos resolvendo?"
- "O que os usuários considerariam 'incompleto' se faltasse?"
- "Que características criam o momento 'aha!' que discutimos mais cedo?"

**Critérios MVP:**

- **Resolve o Problema Principal:** Endereça o principal ponto de dor de forma eficaz
- **User Value:** Cria resultados significativos para os utilizadores-alvo
- **Fealsable:** Alcance com recursos disponíveis e timeline
- **Tensível:** Permite a aprendizagem e a iteração com base no feedback do utilizador

### 3. Fora de alcance Limites

**Exploração fora do âmbito de aplicação:**
Defina o que explicitamente não estará no MVP:

"Que características seria bom ter, mas não são essenciais?"
- "Que funcionalidade poderia esperar pela versão 2.0?"
- "Para que dizemos "não" intencionalmente?"
- "Como comunicamos estes limites às partes interessadas?"

**Configuração de limite:**

- Comunicação clara sobre o que não está incluído
- Razão para adiar certas características
- Considerações sobre prazos para futuras adições
- Explicações comerciais para as partes interessadas

### 4. Critérios de sucesso do MVP

**Validação de sucesso:**
Defina o que torna o MVP bem sucedido:

- "Como saberemos que o MVP é bem sucedido?"
- "Que métricas indicarão que devemos ir além do MVP?"
- "Que sinais de feedback do usuário validam nossa abordagem?"
"Qual é o ponto de decisão para escalar além do MVP?"

**Portas de sucesso:**

- Métricas de adoção do usuário
- Provas de validação de problemas
- Confirmação de viabilidade técnica
- Validação do modelo de negócio

### 5. Exploração de Visão Futuro

**Perguntas da visão:**
Define a visão do produto a longo prazo:

- "Se isto for muito bem sucedido, o que será daqui a 2-3 anos?"
- "Que capacidades