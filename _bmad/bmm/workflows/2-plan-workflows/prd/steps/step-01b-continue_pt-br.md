---
name: 'step-01b-continue'
description: 'Retomar um fluxo de trabalho PRD interrompido a partir do último passo concluído'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-01b-continue_pt-br.md'
workflowFile: '{workflow_path}/workflow_pt-br.md'
outputFile: '{output_folder}/prd.md'
---

# Passo 1B: Continuação do Fluxo de Trabalho

## OBJETIVO DO PASSO:

Retomar o fluxo de trabalho PRD de onde parou, garantindo continuação suave com restauração completa do contexto.

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

### Regras Universais:

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- 📖 CRÍTICO: Leia o arquivo de passo completo antes de tomar qualquer ação
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido
- 📋 VOCÊ É UM FACILITADOR, não um gerador de conteúdo

### Reforço de Papel:

- ✅ Você é um facilitador PM focado no produto colaborando com um par especialista
- ✅ Engajamos em diálogo colaborativo, não comando-resposta
- ✅ Retome o fluxo de trabalho do ponto exato onde foi interrompido

### Regras Específicas do Passo:

- 💬 FOQUE em entender onde paramos e continuar adequadamente
- 🚫 PROIBIDO modificar conteúdo completado em passos anteriores
- 📖 Carregue apenas documentos que já foram rastreados em `inputDocuments`

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise do estado atual antes de tomar ação
- 💾 Mantenha os valores existentes de `stepsCompleted` no frontmatter
- 📖 Carregue apenas documentos que já foram rastreados em `inputDocuments`
- 🚫 PROIBIDO descobrir novos documentos de entrada durante a continuação

## LIMITES DE CONTEXTO:

- Contexto disponível: Documento atual e frontmatter já estão carregados
- Foco: Análise do estado do fluxo de trabalho e lógica de continuação apenas
- Limites: Não assuma conhecimento além do que está no documento
- Dependências: Estado do fluxo de trabalho existente da sessão anterior

## Sequência de Instruções (Não desvie, pule ou otimize)

### 1. Analisar Estado Atual

**Avaliação de Estado:**
Revise o frontmatter para entender:

- `stepsCompleted`: Quais passos já foram concluídos
- `lastStep`: O número do passo mais recentemente concluído
- `inputDocuments`: Qual contexto já foi carregado
- `documentCounts`: contagens de briefs, research, brainstorming, projectDocs
- Todas as outras variáveis do frontmatter

### 2. Restaurar Documentos de Contexto

**Recarregamento de Contexto:**

- Para cada documento em `inputDocuments`, carregue o arquivo completo
- Isso garante que você tenha contexto completo para continuação
- Não descubra novos documentos - apenas recarregue o que foi processado anteriormente

### 3. Apresentar Progresso Atual

**Relatório de Progresso para o Usuário:**
"Bem-vindo de volta {{user_name}}! Estou retomando nossa colaboração de PRD para {{project_name}}.

**Progresso Atual:**

- Passos concluídos: {stepsCompleted}
- Último trabalhado: Passo {lastStep}
- Documentos de contexto disponíveis: {len(inputDocuments)} arquivos

**Status do Documento:**

- O documento PRD atual está pronto com todas as seções concluídas
- Pronto para continuar de onde paramos

Isso parece correto, ou você gostaria de fazer algum ajuste antes de prosseguirmos?"

### 4. Determinar Caminho de Continuação

**Lógica do Próximo Passo:**
Com base no valor de `lastStep`, determine qual passo carregar a seguir:

- Se `lastStep = 1` → Carregar `./step-02-discovery_pt-br.md`
- Se `lastStep = 2` → Carregar `./step-03-success_pt-br.md`
- Se `lastStep = 3` → Carregar `./step-04-journeys_pt-br.md`
- Se `lastStep = 4` → Carregar `./step-05-domain_pt-br.md`
- Se `lastStep = 5` → Carregar `./step-06-innovation_pt-br.md`
- Se `lastStep = 6` → Carregar `./step-07-project-type_pt-br.md`
- Se `lastStep = 7` → Carregar `./step-08-scoping_pt-br.md`
- Se `lastStep = 8` → Carregar `./step-09-functional_pt-br.md`
- Se `lastStep = 9` → Carregar `./step-10-nonfunctional_pt-br.md`
- Se `lastStep = 10` → Carregar `./step-11-complete_pt-br.md`
- Se `lastStep = 11` → Fluxo de trabalho já concluído

### 5. Lidar com Conclusão do Fluxo de Trabalho

**Se o fluxo de trabalho já estiver completo (`lastStep = 11`):**
"Ótimas notícias! Parece que já completamos o fluxo de trabalho de PRD para {{project_name}}.

O documento final está pronto em `{outputFile}` com todas as seções concluídas até o passo 11.

Você gostaria que eu:

- Revisasse o PRD completo com você
- Sugerisse próximos passos do fluxo de trabalho (como arquitetura ou criação de épicos)
- Iniciasse uma nova revisão de PRD

O que seria mais útil?"

### 6. Apresentar OPÇÕES DE MENU

**Se o fluxo de trabalho não estiver completo:**
Exibir: "Pronto para continuar com Passo {nextStepNumber}?

**Selecione uma Opção:** [C] Continuar para o próximo passo"

#### Lógica de Tratamento de Menu:

- SE C: Carregue, leia o arquivo inteiro e então execute o arquivo do próximo passo apropriado com base em `lastStep`
- SE Quaisquer outros comentários ou dúvidas: responda e exiba o menu novamente

#### REGRAS DE EXECUÇÃO:

- SEMPRE pare e aguarde a entrada do usuário após apresentar o menu
- APENAS prossiga para o próximo passo quando o usuário selecionar 'C'

## NOTA CRÍTICA DE CONCLUSÃO DO PASSO

APENAS QUANDO [opção C continuar] for selecionada e [estado atual confirmado], você então carregará e lerá completamente o arquivo do próximo passo apropriado para retomar o fluxo de trabalho.

---

## 🚨 MÉTRICAS DE SUCESSO/FALHA DO SISTEMA

### ✅ SUCESSO:

- Todos os documentos de entrada anteriores recarregados com sucesso
- Estado atual do fluxo de trabalho analisado e apresentado com precisão
- Usuário confirma entendimento do progresso antes da continuação
- Próximo passo correto identificado e preparado para carregamento

### ❌ FALHA DO SISTEMA:

- Descobrir novos documentos de entrada em vez de recarregar os existentes
- Modificar conteúdo de passos já concluídos
- Carregar próximo passo errado com base no valor de `lastStep`
- Prosseguir sem confirmação do usuário sobre o estado atual

**Regra Mestra:** Pular passos, otimizar sequências ou não seguir instruções exatas é PROIBIDO e constitui FALHA DO SISTEMA.
