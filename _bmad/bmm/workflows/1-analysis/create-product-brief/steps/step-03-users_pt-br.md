---
name: 'step-03-users'
description: 'Definir usuários-alvo com personas ricas e mapear suas interações-chave com o produto'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/1-analysis/create-product-brief'

# File References
thisStepFile: '{workflow_path}/steps/step-03-users_pt-br.md'
nextStepFile: '{workflow_path}/steps/step-04-metrics_pt-br.md'
workflowFile: '{workflow_path}/workflow_pt-br.md'
outputFile: '{output_folder}/analysis/product-brief-{{project_name}}-{{date}}.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Passo 3: Descoberta de Usuários-Alvo

## OBJETIVO DO PASSO:

Definir usuários-alvo com personas ricas e mapear suas interações-chave com o produto através de pesquisa colaborativa de usuários e mapeamento de jornada.

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

### Regras Universais:

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- 📖 CRÍTICO: Leia o arquivo de passo completo antes de tomar qualquer ação
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido
- 📋 VOCÊ É UM FACILITADOR, não um gerador de conteúdo

### Reforço de Papel:

- ✅ Você é um facilitador Analista de Negócios focado no produto
- ✅ Se você já recebeu um nome, estilo de comunicação e persona, continue a usá-los enquanto desempenha este novo papel
- ✅ Engajamos em diálogo colaborativo, não comando-resposta
- ✅ Você traz pensamento estruturado e habilidades de facilitação, enquanto o usuário traz expertise de domínio e visão de produto
- ✅ Mantenha tom de descoberta colaborativa por todo o processo

### Regras Específicas do Passo:

- 🎯 Foque apenas em definir quem este produto serve e como eles interagem com ele
- 🚫 PROIBIDO criar perfis genéricos de usuários sem detalhes específicos
- 💬 Abordagem: Desenvolvimento sistemático de personas com mapeamento de jornada
- 📋 Desenvolvimento COLABORATIVO de personas, não criação de usuários baseada em suposições

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Gere personas de usuário e jornadas colaborativamente com o usuário
- 📖 Atualize o frontmatter `stepsCompleted: [1, 2, 3]` antes de carregar o próximo passo
- 🚫 PROIBIDO prosseguir sem confirmação do usuário através do menu

## LIMITES DE CONTEXTO:

- Contexto disponível: Documento atual e frontmatter de passos anteriores, visão do produto e problema já definidos
- Foco: Criar personas de usuário vívidas e acionáveis que se alinham com a visão do produto
- Limites: Foque em usuários que experimentam diretamente o problema ou se beneficiam da solução
- Dependências: Visão do produto e declaração do problema do passo-02 devem estar completas

## Sequência de Instruções (Não desvie, pule ou otimize)

### 1. Iniciar Descoberta de Usuários

**Exploração Inicial:**
"Agora que entendemos o que {{project_name}} faz, vamos definir para quem é.

**Descoberta de Usuários:**

- Quem experimenta o problema que estamos resolvendo?
- Existem diferentes tipos de usuários com necessidades diferentes?
- Quem obtém mais valor desta solução?
- Existem usuários primários e usuários secundários que devemos considerar?

Vamos começar identificando os principais grupos de usuários."

### 2. Desenvolvimento do Segmento de Usuário Primário

**Processo de Desenvolvimento de Persona:**
Para cada segmento de usuário primário, crie personas ricas:

**Nome & Contexto:**

- Dê a eles um nome realista e uma breve história de fundo
- Defina seu papel, ambiente e contexto
- O que os motiva? Quais são seus objetivos?

**Experiência do Problema:**

- Como eles vivenciam o problema atualmente?
- Quais soluções alternativas eles estão usando?
- Quais são os impactos emocionais e práticos?

**Visão de Sucesso:**

- Como seria o sucesso para eles?
- O que os faria dizer "isso é exatamente o que eu precisava"?

**Perguntas sobre Usuário Primário:**

- "Fale-me sobre uma pessoa típica que usaria {{project_name}}"
- "Como é o dia deles? Onde nosso produto se encaixa?"
- "O que eles estão tentando realizar que é difícil agora?"

### 3. Exploração do Segmento de Usuário Secundário

**Considerações sobre Usuário Secundário:**

- "Quem mais se beneficia desta solução, mesmo que não seja o usuário principal?"
- "Existem papéis administrativos, de suporte ou supervisão que devemos considerar?"
- "Quem influencia a decisão de adotar ou comprar este produto?"
- "Existem usuários parceiros ou stakeholders que importam?"

### 4. Mapeamento da Jornada do Usuário

**Elementos da Jornada:**
Mapeie as interações-chave para cada segmento de usuário:

- **Descoberta:** Como eles descobrem a solução?
- **Onboarding:** Como é a primeira experiência deles?
- **Uso Principal:** Como eles usam o produto no dia a dia?
- **Momento de Sucesso:** Quando eles percebem o valor?
- **Longo Prazo:** Como isso se torna parte de sua rotina?

**Perguntas sobre a Jornada:**

- "Descreva como [Nome da Persona] descobriria e começaria a usar {{project_name}}"
- "Qual é o momento 'aha!' deles?"
- "Como este produto muda a maneira como eles trabalham ou vivem?"

### 5. Gerar Conteúdo de Usuários-Alvo

**Conteúdo para Anexar:**
Prepare a seguinte estrutura para anexar ao documento:

```markdown
## Target Users

### Primary Users

[Primary user segment content based on conversation]

### Secondary Users

[Secondary user segment content based on conversation, or N/A if not discussed]

### User Journey

[User journey content based on conversation, or N/A if not discussed]
```

### 6. Apresentar OPÇÕES DE MENU

**Apresentação de Conteúdo:**
"Mapeei quem {{project_name}} serve e como eles interagirão com ele. Isso nos ajuda a garantir que estamos construindo algo que pessoas reais amarão usar.

**Aqui está o que vou adicionar ao documento:**
[Mostre o conteúdo markdown completo do passo 5]

**Selecione uma Opção:** [A] Elicitação Avançada [P] Modo Festa [C] Continuar"

#### Lógica de Tratamento de Menu:

- SE A: Execute {advancedElicitationTask} com o conteúdo atual de usuário para aprofundar em personas e jornadas
- SE P: Execute {partyModeWorkflow} para trazer diferentes perspectivas para validar o entendimento do usuário
- SE C: Salve o conteúdo em {outputFile}, atualize o frontmatter com stepsCompleted: [1, 2, 3], então e apenas então carregue, leia o arquivo inteiro e execute {nextStepFile}
- SE Quaisquer outros comentários ou dúvidas: ajude o usuário a responder e então [Exiba Novamente as Opções de Menu](#6-apresentar-opcoes-de-menu)

#### REGRAS DE EXECUÇÃO:

- SEMPRE pare e aguarde a entrada do usuário após apresentar o menu
- APENAS prossiga para o próximo passo quando o usuário selecionar 'C'
- Após a execução de outros itens de menu, retorne a este menu com conteúdo atualizado
- O usuário pode conversar ou fazer perguntas - sempre responda e termine exibindo novamente as opções de menu

## NOTA CRÍTICA DE CONCLUSÃO DO PASSO

APENAS QUANDO [opção C continuar] for selecionada e [personas de usuário finalizadas e salvas no documento com frontmatter atualizado], você então carregará e lerá completamente `{nextStepFile}` para executar e iniciar a definição de métricas de sucesso.

---

## 🚨 MÉTRICAS DE SUCESSO/FALHA DO SISTEMA

### ✅ SUCESSO:

- Personas de usuário ricas e críveis com motivações claras
- Distinção clara entre usuários primários e secundários
- Jornadas de usuário que mostram pontos de interação-chave e criação de valor
- Segmentos de usuário que se alinham com a visão do produto e declaração do problema
- Menu A/P/C apresentado e tratado corretamente com execução adequada da tarefa
- Conteúdo devidamente anexado ao documento quando C selecionado
- Frontmatter atualizado com stepsCompleted: [1, 2, 3]

### ❌ FALHA DO SISTEMA:

- Criar perfis genéricos de usuários sem detalhes específicos
- Faltar segmentos de usuários-chave que são importantes para o sucesso
- Jornadas de usuário que não mostram como o produto cria valor
- Não conectar as necessidades do usuário de volta à declaração do problema
- Não apresentar o menu padrão A/P/C após a geração de conteúdo
- Anexar conteúdo sem o usuário selecionar 'C'
- Não atualizar o frontmatter corretamente

**Regra Mestra:** Pular passos, otimizar sequências ou não seguir instruções exatas é PROIBIDO e constitui FALHA DO SISTEMA.
