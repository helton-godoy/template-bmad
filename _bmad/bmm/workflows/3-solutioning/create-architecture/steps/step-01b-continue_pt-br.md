# Passo 1B: Continuação do Fluxo de Trabalho de Arquitetura

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- 📖 CRÍTICO: Leia o arquivo de passo completo antes de tomar qualquer ação
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido
- 📋 VOCÊ É UM FACILITADOR, não um gerador de conteúdo

## OBJETIVO DO PASSO:

Retomar o fluxo de trabalho de arquitetura de onde parou, garantindo continuação suave com restauração completa do contexto.

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
- Todas as outras variáveis do frontmatter

### 2. Restaurar Documentos de Contexto

**Recarregamento de Contexto:**

- Para cada documento em `inputDocuments`, carregue o arquivo completo
- Isso garante que você tenha contexto completo para continuação
- Não descubra novos documentos - apenas recarregue o que foi processado anteriormente

### 3. Apresentar Progresso Atual

**Relatório de Progresso para o Usuário:**
"Bem-vindo de volta {{user_name}}! Estou retomando nossa colaboração de arquitetura para {{project_name}}.

**Progresso Atual:**

- Passos concluídos: {stepsCompleted}
- Último trabalhado: Passo {lastStep}
- Documentos de contexto disponíveis: {len(inputDocuments)} arquivos

**Status do Documento:**

- O documento de decisão de arquitetura atual está pronto com todas as seções concluídas
- Pronto para continuar de onde paramos

Isso parece correto, ou você gostaria de fazer algum ajuste antes de prosseguirmos?"

### 4. Determinar Caminho de Continuação

**Lógica do Próximo Passo:**
Com base no valor de `lastStep`, determine qual passo carregar a seguir:

- Se `lastStep = 1` → Carregar `./step-02-context_pt-br.md`
- Se `lastStep = 2` → Carregar `./step-03-starter_pt-br.md`
- Se `lastStep = 3` → Carregar `./step-04-decisions_pt-br.md`
- Se `lastStep = 4` → Carregar `./step-05-patterns_pt-br.md`
- Se `lastStep = 5` → Carregar `./step-06-structure_pt-br.md`
- Se `lastStep = 6` → Carregar `./step-07-validation_pt-br.md`
- Se `lastStep = 7` → Carregar `./step-08-complete_pt-br.md`
- Se `lastStep = 8` → Fluxo de trabalho já concluído

### 5. Lidar com Conclusão do Fluxo de Trabalho

**Se o fluxo de trabalho já estiver completo (`lastStep = 8`):**
"Ótimas notícias! Parece que já completamos o fluxo de trabalho de arquitetura para {{project_name}}.

O documento final está pronto em `{outputFile}` com todas as seções concluídas até o passo 8.

Você gostaria que eu:

- Revisasse a arquitetura completa com você
- Sugerisse próximos passos do fluxo de trabalho (como criação de épicos ou implementação)
- Iniciasse uma nova revisão de arquitetura

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
