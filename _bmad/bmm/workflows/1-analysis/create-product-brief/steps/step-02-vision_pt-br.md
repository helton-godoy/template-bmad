---
name: 'step-02-vision'
description: 'Descobrir e definir a visão central do produto, declaração do problema e proposta de valor única'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/1-analysis/create-product-brief'

# File References
thisStepFile: '{workflow_path}/steps/step-02-vision_pt-br.md'
nextStepFile: '{workflow_path}/steps/step-03-users_pt-br.md'
workflowFile: '{workflow_path}/workflow_pt-br.md'
outputFile: '{output_folder}/analysis/product-brief-{{project_name}}-{{date}}.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Passo 2: Descoberta da Visão do Produto

## OBJETIVO DO PASSO:

Conduzir uma descoberta abrangente da visão do produto para definir o problema central, solução e proposta de valor única através de análise colaborativa.

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

- 🎯 Foque apenas na descoberta da visão do produto, problema e solução
- 🚫 PROIBIDO gerar visão sem entrada real e colaboração do usuário
- 💬 Abordagem: Descoberta sistemática do problema à solução
- 📋 Descoberta COLABORATIVA, não criação de visão baseada em suposições

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Gere conteúdo de visão colaborativamente com o usuário
- 📖 Atualize o frontmatter `stepsCompleted: [1, 2]` antes de carregar o próximo passo
- 🚫 PROIBIDO prosseguir sem confirmação do usuário através do menu

## LIMITES DE CONTEXTO:

- Contexto disponível: Documento atual e frontmatter do passo 1, documentos de entrada já carregados na memória
- Foco: Esta será a primeira seção de conteúdo anexada ao documento
- Limites: Foque-se em uma visão clara e convincente do produto e na declaração do problema
- Dependências: A inicialização do documento a partir do passo-01 deve estar completa

## Sequência de Instruções (Não desvie, pule ou otimize)

### 1. Iniciar a Descoberta da Visão

**Exploração Inicial:**
"Como seu parceiro de PM, estou animado para ajudá-lo a moldar a visão para {{project_name}}. Vamos começar pela fundação.

**Fale-me sobre o produto que você imagina:**

- Que problema você está tentando resolver?
- Quem experimenta este problema mais intensamente?
- Como seria o sucesso para as pessoas que você está ajudando?
- O que te empolga mais nesta solução?

Vamos começar com o espaço do problema antes de entrar em soluções."

### 2. Compreensão Profunda do Problema

**Descoberta do Problema:**
Explore o problema de vários ângulos usando perguntas direcionadas:

- Como as pessoas resolvem este problema atualmente?
- O que é frustrante nas soluções atuais?
- O que acontece se este problema não for resolvido?
- Quem sente essa dor mais intensamente?

### 3. Análise de Soluções Atuais

**Cenário Competitivo:**

- Que soluções existem hoje?
- Onde elas deixam a desejar?
- Que lacunas elas deixam abertas?
- Por que as soluções existentes não resolveram isso completamente?

### 4. Visão da Solução

**Criação Colaborativa da Solução:**

- Se pudéssemos resolver isso perfeitamente, como seria?
- Qual é a maneira mais simples de fazermos uma diferença significativa?
- O que torna sua abordagem diferente do que existe por aí?
- O que faria os usuários dizerem "isso é exatamente o que eu precisava"?

### 5. Diferenciadores Únicos

**Vantagem Competitiva:**

- Qual é a sua vantagem injusta?
- O que seria difícil para os concorrentes copiarem?
- Que insight ou abordagem é única?
- Por que agora é a hora certa para esta solução?

### 6. Gerar Conteúdo do Resumo Executivo

**Conteúdo para Anexar:**
Prepare a seguinte estrutura para anexar ao documento:

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

### 7. Apresentar OPÇÕES DE MENU

**Apresentação de Conteúdo:**
"Redigi o resumo executivo e a visão central com base em nossa conversa. Isso captura a essência de {{project_name}} e o que o torna especial.

**Aqui está o que vou adicionar ao documento:**
[Mostre o conteúdo markdown completo do passo 6]

**Selecione uma Opção:** [A] Elicitação Avançada [P] Modo Festa [C] Continuar"

#### Lógica de Tratamento de Menu:

- SE A: Execute {advancedElicitationTask} com o conteúdo de visão atual para refinar a declaração do problema e solução
- SE P: Execute {partyModeWorkflow} para trazer diferentes perspectivas para validar a visão do produto
- SE C: Salve o conteúdo em {outputFile}, atualize o frontmatter com stepsCompleted: [1, 2], então e apenas então carregue, leia o arquivo inteiro e execute {nextStepFile}
- SE Quaisquer outros comentários ou dúvidas: ajude o usuário a responder e então [Exiba Novamente as Opções de Menu](#7-apresentar-opcoes-de-menu)

#### REGRAS DE EXECUÇÃO:

- SEMPRE pare e aguarde a entrada do usuário após apresentar o menu
- APENAS prossiga para o próximo passo quando o usuário selecionar 'C'
- Após a execução de outros itens de menu, retorne a este menu com conteúdo atualizado
- O usuário pode conversar ou fazer perguntas - sempre responda e termine exibindo novamente as opções de menu

## NOTA CRÍTICA DE CONCLUSÃO DO PASSO

APENAS QUANDO [opção C continuar] for selecionada e [visão do produto finalizada e salva no documento com frontmatter atualizado], você então carregará e lerá completamente `{nextStepFile}` para executar e iniciar a descoberta de usuários alvo.

---

## 🚨 MÉTRICAS DE SUCESSO/FALHA DO SISTEMA

### ✅ SUCESSO:

- Declaração de problema clara e convincente que aborda uma dor real
- Solução proposta que se conecta diretamente ao problema
- Diferenciadores únicos identificados e articulados
- Resumo executivo que captura a essência do produto
- Menu A/P/C apresentado e tratado corretamente com execução adequada da tarefa
- Conteúdo devidamente anexado ao documento quando C selecionado
- Frontmatter atualizado com stepsCompleted: [1, 2]

### ❌ FALHA DO SISTEMA:

- Criar declarações de problema vagas sem impacto claro
- Propor soluções sem entender o problema primeiro
- Falhar em identificar por que as soluções atuais são inadequadas
- Gerar conteúdo de visão sem entrada do usuário
- Não apresentar o menu padrão A/P/C após a geração de conteúdo
- Anexar conteúdo sem o usuário selecionar 'C'
- Não atualizar o frontmatter corretamente

**Regra Mestra:** Pular passos, otimizar sequências ou não seguir instruções exatas é PROIBIDO e constitui FALHA DO SISTEMA.
