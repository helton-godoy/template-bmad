---
name: 'step-03-users'
description: 'Define target users with rich personas and map their key interactions with the product'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/1-analysis/product-brief'

# File References
thisStepFile: '{workflow_path}/steps/step-03-users.md'
nextStepFile: '{workflow_path}/steps/step-04-metrics.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/analysis/product-brief-{{project_name}}-{{date}}.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Passo 3: Usuários alvo Discovery

## PASSO:

Defina usuários-alvo com personas ricos e mapeie suas interações-chave com o produto através de pesquisa colaborativa do usuário e mapeamento de jornada.

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

- 🎯 Concentre-se apenas em definir quem este produto serve e como eles interagem com ele
- 🚫 PROIBIDA para criar perfis genéricos de usuários sem detalhes específicos
- 💬 Abordagem: Desenvolvimento sistemático de persona com mapeamento de viagens
- 📋 Desenvolvimento de personalidades COLABORATIVAs, não criação de usuários baseados em pressupostos

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Gerar personas de usuário e viagens colaborativamente com o usuário
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3]` antes de carregar o próximo passo
- 🚫 PROIBIDO proceder sem confirmação do utilizador através do menu

## CONTEXTO MONTANTES:

- Contexto disponível: Documento atual e matéria frontal das etapas anteriores, visão do produto e problema já definido
- Focus: Criando personas de usuário vívidas e acionáveis que se alinham à visão do produto
- Limits: Concentre-se nos usuários que experimentam diretamente o problema ou se beneficiam da solução
- Dependencies: Visão do produto e indicação do problema do passo-02 deve ser completa

## Sequência de Instruções (Não desvie, salte ou optimize)

### 1. Comece a descoberta do usuário

**Exploração de Abertura:**
"Agora que entendemos o que {{project_name}} faz, let define para quem é.

**User Discovery:**

- Quem vive o problema que estamos a resolver?
- Existem diferentes tipos de usuários com necessidades diferentes?
- Quem ganha mais valor com esta solução?
- Há usuários primários e usuários secundários que devemos considerar?

Vamos começar identificando os principais grupos de usuários."

### 2. Desenvolvimento primário do segmento do usuário

**Processo de Desenvolvimento de Persona:**
Para cada segmento de usuário primário, crie personas ricas:

**Nome & Contexto:**

- Dar-lhes um nome realista e breve história
- Definir o seu papel, ambiente e contexto
- O que os motiva? Quais são seus objetivos?

**Experiência de Problemas:**

- Como é que eles vivem o problema?
- Que soluções estão a usar?
- Quais são os impactos emocionais e práticos?

**Visão de sucesso:**

- Como seria o sucesso para eles?
- O que os faria dizer "isso é exactamente o que eu precisava"?

**Perguntas Primárias do Usuário:**

- "Fale-me de uma pessoa típica que usaria {{project_name}}"
- Como é o dia deles? Onde nosso produto se encaixa?"
- "O que estão a tentar fazer agora é difícil?"

### 3. Exploração Segmentar do Usuário

**Considerações de usuário secundários:**

- "Quem mais se beneficia desta solução, mesmo que não seja o utilizador principal?"
- "Há funções de administrador, apoio ou supervisão que devemos considerar?"
- "Quem influencia a decisão de adotar ou comprar este produto?"
- "Existem usuários parceiros ou interessados que importam?"

### 4. Mapeamento de Viagem de Usuário

**Elementos de viagem:**
Mapear interações chave para cada segmento de usuário:

- **Discovery:** Como eles descobrem sobre a solução?
- **A bordo:** Como é a primeira experiência deles?
- **Uso da coroa:** Como eles usam o produto no dia-a-dia?
- **Momento de sucesso:** Quando é que eles percebem o valor?
- **A longo prazo:** Como isso se torna parte de sua rotina?

**Perguntas de viagem:**

- "Andar através de como [Nome Persona] iria descobrir e começar a usar {{project_name}}"
- "Qual é o momento 'aha!' deles?"
- "Como é que este produto muda como eles funcionam ou vivem?"

### 5. Gerar Conteúdo de Usuários-alvo

**Content to Append:**
Preparar a seguinte estrutura para o anexo do documento:

Marcação para baixo

## Utilizadores-alvo

### Utilizadores primários

[Segmento primário do utilizador