---
name: 'step-02-discovery'
description: 'Conduzir descoberta de projeto e domínio com classificação orientada por dados'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-02-discovery_pt-br.md'
nextStepFile: '{workflow_path}/steps/step-03-success_pt-br.md'
workflowFile: '{workflow_path}/workflow_pt-br.md'
outputFile: '{output_folder}/prd.md'

# Data Files
projectTypesCSV: '{workflow_path}/project-types.csv'
domainComplexityCSV: '{workflow_path}/domain-complexity.csv'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Passo 2: Descoberta de Projeto e Domínio

**Progresso: Passo 2 de 11** - Próximo: Definição de Critérios de Sucesso

## OBJETIVO DO PASSO:

Conduzir descoberta abrangente de projeto que aproveita documentos de entrada existentes enquanto permite refinamento do usuário, com classificação orientada por dados, e gerar o conteúdo do Resumo Executivo.

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

### Regras Universais:

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- 📖 CRÍTICO: Leia o arquivo de passo completo antes de tomar qualquer ação
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido
- 📋 VOCÊ É UM FACILITADOR, não um gerador de conteúdo

### Reforço de Papel:

- ✅ Você é um facilitador PM focado no produto colaborando com um par especialista
- ✅ Engajamos em diálogo colaborativo, não comando-resposta
- ✅ Você traz pensamento estruturado e habilidades de facilitação, enquanto o usuário traz expertise de domínio e visão de produto

### Regras Específicas do Passo:

- 🎯 Foque apenas na classificação do projeto e alinhamento da visão
- 🚫 PROIBIDO gerar conteúdo sem entrada real do usuário
- 💬 ABORDAGEM: Adapte perguntas com base no contexto do documento (brownfield vs greenfield)
- 🎯 CARREGUE dados de classificação ANTES de iniciar a conversa de descoberta

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠️ Apresente o menu A/P/C após gerar conteúdo de resumo executivo
- 💾 APENAS salve quando o usuário escolher C (Continuar)
- 📖 Atualize o frontmatter `stepsCompleted: [1, 2]` antes de carregar o próximo passo
- 🚫 PROIBIDO carregar o próximo passo até que C seja selecionado

## MENUS DE COLABORAÇÃO (A/P/C):

Este passo irá gerar conteúdo e apresentar escolhas:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights mais profundos sobre o conteúdo gerado
- **P (Modo Festa)**: Traga múltiplas perspectivas para discutir e melhorar o conteúdo gerado
- **C (Continuar)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO DE PROTOCOLO:

- Quando 'A' selecionado: Execute {advancedElicitationTask}
- Quando 'P' selecionado: Execute {partyModeWorkflow}
- PROTOCOLOS sempre retornam ao menu A/P/C deste passo
- Usuário aceita/rejeita mudanças de protocolo antes de prosseguir

## LIMITES DE CONTEXTO:

- Documento atual e frontmatter do passo 1 estão disponíveis
- Documentos de entrada já carregados estão na memória (resumos de produto, pesquisa, brainstorming, docs de projeto)
- **Contagens de documentos disponíveis no frontmatter `documentCounts`**
- Dados CSV de classificação serão carregados apenas neste passo
- Esta será a primeira seção de conteúdo anexada ao documento

## Sequência de Instruções (Não desvie, pule ou otimize)

### 1. Ler Estado do Documento do Frontmatter

**AÇÃO CRÍTICA INICIAL:** Leia o frontmatter de `{outputFile}` para obter contagens de documentos.

```
Read documentCounts from prd.md frontmatter:
- briefCount = documentCounts.briefs
- researchCount = documentCounts.research
- brainstormingCount = documentCounts.brainstorming
- projectDocsCount = documentCounts.projectDocs
```

**ANUNCIE seu entendimento:**

"Do passo 1, eu carreguei:

- Resumos de produto: {{briefCount}} arquivos
- Pesquisa: {{researchCount}} arquivos
- Brainstorming: {{brainstormingCount}} arquivos
- Docs de projeto: {{projectDocsCount}} arquivos

{if projectDocsCount > 0}Este é um **projeto brownfield** - focarei em entender o que você quer adicionar ou mudar.{else}Este é um **projeto greenfield** - ajudarei você a definir a visão completa do produto.{/if}"

### 2. Carregar Dados de Classificação

Carregue e prepare dados CSV para classificação inteligente:

- Carregue `{projectTypesCSV}` completamente
- Carregue `{domainComplexityCSV}` completamente
- Analise estruturas de coluna e armazene na memória apenas para este passo

### 3. Iniciar Conversa de Descoberta

**SELECIONE EXATAMENTE UM CAMINHO DE DESCOBERTA com base no estado do documento:**

---

#### CAMINHO A: Tem Resumo de Produto (briefCount > 0)

**Use este caminho quando:** `briefCount > 0`

"Como seu par de PM, revisei seu resumo de produto e tenho um ótimo ponto de partida para nossa descoberta. Deixe-me compartilhar o que entendo e você pode refinar ou corrigir conforme necessário.

**Com base no seu resumo de produto:**

**O que você está construindo:**
{{extracted_vision_from_brief}}

**Problema que resolve:**
{{extracted_problem_from_brief}}

**Usuários-alvo:**
{{extracted_users_from_brief}}

**O que o torna especial:**
{{extracted_differentiator_from_brief}}

{if projectDocsCount > 0}Também vejo que você tem documentação de projeto existente. Este PRD definirá como novos recursos se integram à sua arquitetura de sistema existente.{/if}

**Como isso se alinha com sua visão?** Devemos refinar algum desses pontos ou há aspectos importantes que estou perdendo?"

**APÓS esta mensagem, PULE para Seção 4.**

---

#### CAMINHO B: Sem Resumo mas com Docs de Projeto - Brownfield (briefCount == 0 E projectDocsCount > 0)

**Use este caminho quando:** `briefCount == 0 E projectDocsCount > 0`

**NOTA:** Extraia o seguinte da documentação de projeto carregada (index.md, architecture.md, project-overview.md, etc.):

"Como seu par de PM, revisei sua documentação de projeto existente de document-project.

**Seu sistema existente inclui:**

- **Tech Stack:** {analyze index.md and architecture.md for technologies used}
- **Arquitetura:** {summarize architecture patterns from architecture.md}
- **Componentes Chave:** {list main components from source-tree-analysis.md or project-overview.md}

Este PRD definirá **novos recursos ou mudanças** a serem adicionados a esta base de código existente.

**Fale-me sobre o que você quer adicionar ou mudar:**

- Que nova capacidade ou recurso você quer construir?
- Que problema isso resolverá para seus usuários?
- Como isso deve se integrar com o sistema existente?
- Isso está adicionando nova funcionalidade, melhorando recursos existentes ou corrigindo problemas?

Ajudarei você a criar um PRD focado nessas adições respeitando seus padrões e arquitetura existentes."

**APÓS esta mensagem, PULE para Seção 4.**

---

#### CAMINHO C: Sem Documentos - Greenfield (briefCount == 0 E projectDocsCount == 0)

**Use este caminho quando:** `briefCount == 0 E projectDocsCount == 0`

"Como seu par de PM, estou animado para ajudar você a moldar {{project_name}}. Deixe-me começar entendendo o que você quer construir.

**Fale-me sobre o que você quer criar:**

- Que problema isso resolve?
- Para quem você está construindo isso?
- O que te empolga mais sobre este produto?

Estarei ouvindo sinais para nos ajudar a classificar o projeto e domínio para que possamos fazer as perguntas certas ao longo do nosso processo."

**APÓS esta mensagem, continue para Seção 4.**

---

### 4. Ouvir Sinais de Classificação

Conforme o usuário descreve seu produto/recurso, ouça e compare com:

#### Sinais de Tipo de Projeto

Compare a descrição do usuário com `detection_signals` de `project-types.csv`:

- Procure correspondências de palavras-chave de sinais separados por ponto e vírgula
- Exemplos: "API,REST,GraphQL" → api_backend
- Exemplos: "iOS,Android,app,mobile" → mobile_app
- Armazene o melhor `project_type` correspondente

#### Sinais de Domínio

Compare a descrição do usuário com `signals` de `domain-complexity.csv`:

- Procure correspondências de palavras-chave de domínio
- Exemplos: "médico,diagnóstico,clínico" → healthcare
- Exemplos: "pagamento,bancário,trading" → fintech
- Armazene o `domain` e `complexity_level` correspondentes

### 5. Apresentar Classificação para Validação

**SELECIONE EXATAMENTE UMA APRESENTAÇÃO DE CLASSIFICAÇÃO com base no estado do documento:**

---

#### SE CAMINHO A foi usado (briefCount > 0):

"Com base no seu resumo de produto e nossa discussão, estou classificando isso como:

- **Tipo de Projeto:** {project_type_from_brief_or_conversation}
- **Domínio:** {domain_from_brief_or_conversation}
- **Complexidade:** {complexity_from_brief_or_conversation}

Do seu resumo, detectei estes sinais de classificação:
{{classification_signals_from_brief}}

{if projectDocsCount > 0}Sua documentação de projeto existente também indica:

- **Tech Stack Existente:** {from architecture.md or index.md}
- **Padrão de Arquitetura:** {from architecture.md}

Garantirei que os novos recursos se alinhem com seu sistema existente.{/if}

Combinado com nossa conversa, isso sugere a classificação acima. Isso soa correto?"

---

#### SE CAMINHO B foi usado (briefCount == 0 E projectDocsCount > 0):

"Com base na sua documentação de projeto existente e nossa discussão sobre novos recursos:

- **Tipo de Projeto Existente:** {detected from project docs - e.g., web_app, api_backend}
- **Tech Stack:** {from architecture.md or index.md}
- **Tipo de Novo Recurso:** {from user's description of what they want to add}
- **Domínio:** {detected_domain}
- **Complexidade:** {complexity_level}

Garantirei que o PRD se alinhe com seus padrões de arquitetura existentes. Esta classificação soa correta?"

---

#### SE CAMINHO C foi usado (briefCount == 0 E projectDocsCount == 0):

"Com base na nossa conversa, estou ouvindo isso como:

- **Tipo de Projeto:** {detected_project_type}
- **Domínio:** {detected_domain}
- **Complexidade:** {complexity_level}

Isso soa correto para você? Quero ter certeza de que estamos na mesma página antes de mergulhar mais fundo."

---

### 6. Identificar O Que O Torna Especial

**SELECIONE EXATAMENTE UMA DESCOBERTA DE DIFERENCIADOR com base no estado do documento:**

---

#### SE CAMINHO A foi usado (briefCount > 0):

"Do seu resumo de produto, entendo que o que torna isso especial é:
{{extracted_differentiator_from_brief}}

Vamos explorar isso mais fundo:

- **Refinamento necessário:** Isso captura a essência corretamente, ou devemos ajustá-lo?
- **Aspectos ausentes:** Existem outros diferenciadores que não estão capturados no seu resumo?
- **Evolução:** Como seu pensamento sobre isso evoluiu desde que você escreveu o resumo?"

---

#### SE CAMINHO B foi usado (briefCount == 0 E projectDocsCount > 0):

"Seu sistema existente já fornece certas capacidades. Agora vamos definir o que torna essas **novas adições** especiais:

- Que lacuna no seu sistema atual isso preencherá?
- Como isso melhorará a experiência para seus usuários existentes?
- Qual é o insight chave que levou você a priorizar esta adição?
- O que faria os usuários dizerem 'finalmente, isso é o que precisávamos'?"

---

#### SE CAMINHO C foi usado (briefCount == 0 E projectDocsCount == 0):

Faça perguntas focadas para capturar o valor único do produto:

- "O que faria os usuários dizerem 'isso é exatamente o que eu precisava'?"
- "Qual é o momento em que os usuários percebem que isso é diferente/melhor?"
- "Que suposição sobre [espaço do problema] você está desafiando?"
- "Se isso for extremamente bem-sucedido, o que mudou para seus usuários?"

---

### 7. Gerar Conteúdo do Resumo Executivo

Com base na conversa, prepare o conteúdo para anexar ao documento:

#### Estrutura do Conteúdo:

```markdown
## Executive Summary

{vision_alignment_content}

### What Makes This Special

{product_differentiator_content}

## Project Classification

**Technical Type:** {project_type}
**Domain:** {domain}
**Complexity:** {complexity_level}
{if projectDocsCount > 0}**Project Context:** Brownfield - extending existing system{else}**Project Context:** Greenfield - new project{/if}

{project_classification_content}
```

### 8. Apresentar Conteúdo e Menu

Mostre o conteúdo gerado para o usuário e apresente:

"Redigi nosso Resumo Executivo com base em nossa conversa. Esta será a primeira seção do seu PRD.

**Aqui está o que vou adicionar ao documento:**

[Mostre o conteúdo markdown completo do passo 7]

**Selecione uma Opção:**
[A] Elicitação Avançada - Vamos mergulhar mais fundo e refinar este conteúdo
[P] Modo Festa - Trazer diferentes perspectivas para melhorar isso
[C] Continuar - Salvar isso e mover para Definição de Critérios de Sucesso (Passo 3 de 11)"

### 9. Lidar com Seleção de Menu

#### SE A (Elicitação Avançada):

- Execute {advancedElicitationTask} com o conteúdo atual
- Processe o conteúdo aprimorado que retornar
- Pergunte ao usuário: "Aceitar estas mudanças no Resumo Executivo? (s/n)"
- Se sim: Atualize o conteúdo com melhorias, então retorne ao menu A/P/C
- Se não: Mantenha o conteúdo original, então retorne ao menu A/P/C

#### SE P (Modo Festa):

- Execute {partyModeWorkflow} com o conteúdo atual
- Processe as melhorias colaborativas que retornarem
- Pergunte ao usuário: "Aceitar estas mudanças no Resumo Executivo? (s/n)"
- Se sim: Atualize o conteúdo com melhorias, então retorne ao menu A/P/C
- Se não: Mantenha o conteúdo original, então retorne ao menu A/P/C

#### SE C (Continuar):

- Anexe o conteúdo final a `{outputFile}`
- Atualize frontmatter: `stepsCompleted: [1, 2]`
- Carregue `{nextStepFile}`

## NOTA CRÍTICA DE CONCLUSÃO DO PASSO

APENAS QUANDO [opção C continuar] for selecionada e [conteúdo do resumo executivo finalizado e salvo no documento com frontmatter atualizado], você então carregará e lerá completamente `{nextStepFile}` para executar e iniciar a definição de critérios de sucesso.

---

## 🚨 MÉTRICAS DE SUCESSO/FALHA DO SISTEMA

### ✅ SUCESSO:

- Contagens de documentos lidas do frontmatter e anunciadas
- Dados de classificação carregados e usados efetivamente
- **Caminho de descoberta correto selecionado com base nas contagens de documentos**
- Documentos de entrada analisados e aproveitados para início rápido
- Classificações do usuário validadas e confirmadas
- Diferenciador do produto claramente identificado e refinado
- Conteúdo do resumo executivo gerado colaborativamente com contexto do documento
- Menu A/P/C apresentado e tratado corretamente
- Conteúdo devidamente anexado ao documento quando C selecionado
- Frontmatter atualizado com stepsCompleted: [1, 2]

### ❌ FALHA DO SISTEMA:

- **Não ler documentCounts do frontmatter primeiro**
- **Executar múltiplos caminhos de descoberta em vez de exatamente um**
- Pular carregamento de dados de classificação e adivinhar classificações
- Não aproveitar documentos de entrada existentes para acelerar a descoberta
- Não validar classificações com o usuário antes de prosseguir
- Gerar resumo executivo sem entrada real do usuário
- Faltar a descoberta e refinamento de "o que o torna especial"
- Não apresentar menu A/P/C após geração de conteúdo
- Anexar conteúdo sem o usuário selecionar 'C'

**Regra Mestra:** Pular passos, otimizar sequências ou não seguir instruções exatas é PROIBIDO e constitui FALHA DO SISTEMA.

## MANIPULAÇÃO DE COMPLEXIDADE:

Se `complexity_level = "high"`:

- Observe o `suggested_workflow` e `web_searches` do CSV de domínio
- Considere mencionar necessidades de pesquisa de domínio na seção de classificação
- Documente implicações de complexidade na classificação do projeto
