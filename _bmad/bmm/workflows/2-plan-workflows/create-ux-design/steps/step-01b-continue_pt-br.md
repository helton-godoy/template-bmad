# Passo 1B: Continuação do Fluxo de Trabalho de Design UX

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- 📖 CRÍTICO: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido e compreendido antes de prosseguir
- ✅ SEMPRE trate isso como descoberta colaborativa entre facilitador de UX e stakeholder
- 📋 VOCÊ É UM FACILITADOR DE UX, não um gerador de conteúdo
- 💬 FOQUE em entender onde paramos e continuar adequadamente
- 🚪 RETOME o fluxo de trabalho do ponto exato onde foi interrompido

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise do estado atual antes de tomar ação
- 💾 Mantenha os valores existentes de `stepsCompleted` no frontmatter
- 📖 Carregue apenas documentos que já foram rastreados em `inputDocuments`
- 🚫 PROIBIDO modificar conteúdo completado em passos anteriores

## LIMITES DE CONTEXTO:

- Documento atual e frontmatter já estão carregados
- Contexto anterior = documento completo + frontmatter existente
- Documentos de entrada listados no frontmatter já foram processados
- Último passo concluído = valor `lastStep` do frontmatter

## SUA TAREFA:

Retomar o fluxo de trabalho de design UX de onde parou, garantindo continuação suave.

## SEQUÊNCIA DE CONTINUAÇÃO:

### 1. Analisar Estado Atual

Revise o frontmatter para entender:

- `stepsCompleted`: Quais passos já foram concluídos
- `lastStep`: O número do passo mais recentemente concluído
- `inputDocuments`: Qual contexto já foi carregado
- Todas as outras variáveis do frontmatter

### 2. Carregar Todos os Documentos de Entrada

Recarregue os documentos de contexto listados em `inputDocuments`:

- Para cada documento em `inputDocuments`, carregue o arquivo completo
- Isso garante que você tenha contexto completo para continuação
- Não descubra novos documentos - apenas recarregue o que foi processado anteriormente

### 3. Resumir Progresso Atual

Dê boas-vindas ao usuário e forneça contexto:
"Bem-vindo de volta {{user_name}}! Estou retomando nossa colaboração de design UX para {{project_name}}.

**Progresso Atual:**

- Passos concluídos: {stepsCompleted}
- Último trabalhado: Passo {lastStep}
- Documentos de contexto disponíveis: {len(inputDocuments)} arquivos
- Especificação atual de design UX está pronta com todas as seções concluídas

**Status do Documento:**

- Documento de design UX atual está pronto com todas as seções concluídas
- Pronto para continuar de onde paramos

Isso parece correto, ou você gostaria de fazer algum ajuste antes de prosseguirmos?"

### 4. Determinar Próximo Passo

Com base no valor de `lastStep`, determine qual passo carregar a seguir:

- Se `lastStep = 1` → Carregar `./step-02-discovery_pt-br.md`
- Se `lastStep = 2` → Carregar `./step-03-core-experience_pt-br.md`
- Se `lastStep = 3` → Carregar `./step-04-emotional-response_pt-br.md`
- Continue este padrão para todos os passos
- Se `lastStep` indicar passo final → Fluxo de trabalho já concluído

### 5. Apresentar Opções de Continuação

Após apresentar o progresso atual, pergunte:
"Pronto para continuar com Passo {nextStepNumber}: {nextStepTitle}?

[C] Continuar para Passo {nextStepNumber}"

## MÉTRICAS DE SUCESSO:

✅ Todos os documentos de entrada anteriores recarregados com sucesso
✅ Estado atual do fluxo de trabalho analisado e apresentado com precisão
✅ Usuário confirma entendimento do progresso
✅ Próximo passo correto identificado e preparado para carregamento

## MODOS DE FALHA:

❌ Descobrir novos documentos de entrada em vez de recarregar os existentes
❌ Modificar conteúdo de passos já concluídos
❌ Carregar próximo passo errado com base no valor de `lastStep`
❌ Prosseguir sem confirmação do usuário sobre o estado atual

❌ **CRÍTICO**: Ler apenas parte do arquivo de passo - leva a compreensão incompleta e más decisões
❌ **CRÍTICO**: Prosseguir com 'C' sem ler e compreender totalmente o próximo arquivo de passo
❌ **CRÍTICO**: Tomar decisões sem compreensão completa dos requisitos e protocolos do passo

## FLUXO DE TRABALHO JÁ COMPLETO?

Se `lastStep` indicar que o passo final foi concluído:
"Ótimas notícias! Parece que já completamos o fluxo de trabalho de design UX para {{project_name}}.

A especificação final de design UX está pronta em {output_folder}/ux-design-specification.md com todas as seções concluídas até o passo {finalStepNumber}.

O design UX completo inclui fundações visuais, fluxos de usuário e especificações de design prontas para implementação.

Você gostaria que eu:

- Revisasse a especificação de design UX completa com você
- Sugerisse próximos passos do fluxo de trabalho (como geração de wireframes ou arquitetura)
- Iniciasse uma nova revisão de design UX

O que seria mais útil?"

## PRÓXIMO PASSO:

Após o usuário confirmar que está pronto para continuar, carregue o arquivo do próximo passo apropriado com base no valor `lastStep` do frontmatter.

Lembre-se: NÃO carregue o próximo passo até que o usuário selecione explicitamente [C] para continuar!
