---
name: 'step-04-metrics'
description: 'Definir métricas de sucesso abrangentes que incluem sucesso do usuário, objetivos de negócios e indicadores-chave de desempenho'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/1-analysis/create-product-brief'

# File References
thisStepFile: '{workflow_path}/steps/step-04-metrics_pt-br.md'
nextStepFile: '{workflow_path}/steps/step-05-scope_pt-br.md'
workflowFile: '{workflow_path}/workflow_pt-br.md'
outputFile: '{output_folder}/analysis/product-brief-{{project_name}}-{{date}}.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Passo 4: Definição de Métricas de Sucesso

## OBJETIVO DO PASSO:

Definir métricas de sucesso abrangentes que incluem sucesso do usuário, objetivos de negócios e indicadores-chave de desempenho através de definição colaborativa de métricas alinhadas com a visão do produto e valor para o usuário.

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

- 🎯 Foque apenas em definir critérios de sucesso mensuráveis e objetivos de negócios
- 🚫 PROIBIDO criar métricas vagas que não podem ser medidas ou rastreadas
- 💬 Abordagem: Definição sistemática de métricas que conecta valor do usuário ao sucesso do negócio
- 📋 Definição COLABORATIVA de métricas que impulsiona decisões acionáveis

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Gere métricas de sucesso colaborativamente com o usuário
- 📖 Atualize o frontmatter `stepsCompleted: [1, 2, 3, 4]` antes de carregar o próximo passo
- 🚫 PROIBIDO prosseguir sem confirmação do usuário através do menu

## LIMITES DE CONTEXTO:

- Contexto disponível: Documento atual e frontmatter de passos anteriores, visão do produto e usuários-alvo já definidos
- Foco: Criar critérios de sucesso mensuráveis e acionáveis que se alinham com a estratégia do produto
- Limites: Foque em métricas que impulsionam decisões e demonstram criação de valor real
- Dependências: Visão do produto e personas de usuário de passos anteriores devem estar completas

## Sequência de Instruções (Não desvie, pule ou otimize)

### 1. Iniciar Descoberta de Métricas de Sucesso

**Exploração Inicial:**
"Agora que sabemos quem {{project_name}} serve e qual problema resolve, vamos definir como é o sucesso.

**Descoberta de Sucesso:**

- Como saberemos que estamos tendo sucesso para nossos usuários?
- O que faria os usuários dizerem 'isso valeu a pena'?
- Que métricas mostram que estamos criando valor real?

Vamos começar com a perspectiva do usuário."

### 2. Métricas de Sucesso do Usuário

**Perguntas sobre Sucesso do Usuário:**
Defina o sucesso da perspectiva do usuário:

- "Que resultado os usuários estão tentando alcançar?"
- "Como eles saberão que o produto está funcionando para eles?"
- "Qual é o momento em que eles percebem que isso está resolvendo o problema deles?"
- "Que comportamentos indicam que os usuários estão obtendo valor?"

**Exploração de Sucesso do Usuário:**
Guie de métricas vagas para específicas:

- "Usuários estão felizes" → "Usuários completam [ação chave] dentro de [prazo]"
- "Produto é útil" → "Usuários retornam [frequência] e usam [recurso principal]"
- Foque em resultados e comportamentos, não apenas em pontuações de satisfação

### 3. Objetivos de Negócios

**Perguntas sobre Sucesso do Negócio:**
Defina métricas de sucesso do negócio:

- "Como é o sucesso para o negócio em 3 meses? 12 meses?"
- "Estamos medindo receita, crescimento de usuários, engajamento ou outra coisa?"
- "Que métricas de negócios fariam você dizer 'isso está funcionando'?"
- "Como este produto contribui para objetivos mais amplos da empresa?"

**Categorias de Sucesso do Negócio:**

- **Métricas de Crescimento:** Aquisição de usuários, penetração de mercado
- **Métricas de Engajamento:** Padrões de uso, retenção, satisfação
- **Métricas Financeiras:** Receita, lucratividade, eficiência de custos
- **Métricas Estratégicas:** Posição de mercado, vantagem competitiva

### 4. Indicadores-Chave de Desempenho (KPIs)

**Processo de Desenvolvimento de KPI:**
Defina KPIs específicos e mensuráveis:

- Transforme objetivos em indicadores mensuráveis
- Garanta que cada KPI tenha um método de medição claro
- Defina metas e prazos onde apropriado
- Inclua indicadores antecedentes que preveem o sucesso

**Exemplos de KPI:**

- Aquisição de usuários: "X novos usuários por mês"
- Engajamento: "Y% dos usuários completam a jornada principal semanalmente"
- Impacto nos negócios: "$Z em economia de custos ou geração de receita"

### 5. Conectar Métricas à Estratégia

**Alinhamento Estratégico:**
Garanta que as métricas se alinhem com a visão do produto e as necessidades do usuário:

- Conecte cada métrica de volta à visão do produto
- Garanta que as métricas de sucesso do usuário impulsionem o sucesso do negócio
- Valide que as métricas medem o que realmente importa
- Evite métricas de vaidade que não impulsionam decisões

### 6. Gerar Conteúdo de Métricas de Sucesso

**Conteúdo para Anexar:**
Prepare a seguinte estrutura para anexar ao documento:

```markdown
## Success Metrics

[Success metrics content based on conversation]

### Business Objectives

[Business objectives content based on conversation, or N/A if not discussed]

### Key Performance Indicators

[Key performance indicators content based on conversation, or N/A if not discussed]
```

### 7. Apresentar OPÇÕES DE MENU

**Apresentação de Conteúdo:**
"Defini métricas de sucesso que nos ajudarão a rastrear se {{project_name}} está criando valor real para os usuários e alcançando objetivos de negócios.

**Aqui está o que vou adicionar ao documento:**
[Mostre o conteúdo markdown completo do passo 6]

**Selecione uma Opção:** [A] Elicitação Avançada [P] Modo Festa [C] Continuar"

#### Lógica de Tratamento de Menu:

- SE A: Execute {advancedElicitationTask} com o conteúdo de métricas atual para aprofundar nos insights de métricas de sucesso
- SE P: Execute {partyModeWorkflow} para trazer diferentes perspectivas para validar métricas abrangentes
- SE C: Salve o conteúdo em {outputFile}, atualize o frontmatter com stepsCompleted: [1, 2, 3, 4], então e apenas então carregue, leia o arquivo inteiro e execute {nextStepFile}
- SE Quaisquer outros comentários ou dúvidas: ajude o usuário a responder e então [Exiba Novamente as Opções de Menu](#7-apresentar-opcoes-de-menu)

#### REGRAS DE EXECUÇÃO:

- SEMPRE pare e aguarde a entrada do usuário após apresentar o menu
- APENAS prossiga para o próximo passo quando o usuário selecionar 'C'
- Após a execução de outros itens de menu, retorne a este menu com conteúdo atualizado
- O usuário pode conversar ou fazer perguntas - sempre responda e termine exibindo novamente as opções de menu

## NOTA CRÍTICA DE CONCLUSÃO DO PASSO

APENAS QUANDO [opção C continuar] for selecionada e [métricas de sucesso finalizadas e salvas no documento com frontmatter atualizado], você então carregará e lerá completamente `{nextStepFile}` para executar e iniciar a definição do escopo MVP.

---

## 🚨 MÉTRICAS DE SUCESSO/FALHA DO SISTEMA

### ✅ SUCESSO:

- Métricas de sucesso do usuário que focam em resultados e comportamentos
- Objetivos de negócios claros alinhados com a estratégia do produto
- KPIs específicos e mensuráveis com metas e prazos definidos
- Métricas que conectam valor do usuário ao sucesso do negócio
- Menu A/P/C apresentado e tratado corretamente com execução adequada da tarefa
- Conteúdo devidamente anexado ao documento quando C selecionado
- Frontmatter atualizado com stepsCompleted: [1, 2, 3, 4]

### ❌ FALHA DO SISTEMA:

- Métricas de sucesso vagas que não podem ser medidas ou rastreadas
- Objetivos de negócios desconectados do sucesso do usuário
- Muitas métricas ou falta de indicadores críticos de sucesso
- Métricas que não impulsionam decisões acionáveis
- Não apresentar o menu padrão A/P/C após a geração de conteúdo
- Anexar conteúdo sem o usuário selecionar 'C'
- Não atualizar o frontmatter corretamente

**Regra Mestra:** Pular passos, otimizar sequências ou não seguir instruções exatas é PROIBIDO e constitui FALHA DO SISTEMA.
