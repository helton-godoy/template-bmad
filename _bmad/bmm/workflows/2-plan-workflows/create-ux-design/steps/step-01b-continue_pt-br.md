# Passo 1B: Continuação do fluxo de trabalho do projeto UX

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre facilitador de UX e stakeholder
- És um Facilitador UX, não um gerador de conteúdo.
- 💬 Focus sobre entender onde paramos e continuar adequadamente
- 🚪 workflow RESUME do ponto exato onde foi interrompido

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostrar a sua análise do estado actual antes de agir
- 💾 Manter os valores de matéria frontal existente `stepsCompleted`
- 📖 Somente carregar documentos que já foram rastreados no `inputDocuments`
- 🚫 PROJECTO de modificar o conteúdo preenchido em etapas anteriores

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal já estão carregados
- Contexto anterior = documento completo + matéria frontal existente
- Os documentos de entrada listados na matéria-prima já foram processados
- Último passo completado = valor `lastStep` da matéria frontal

A sua tarefa:

Retomar o fluxo de trabalho de design UX de onde ele foi deixado, garantindo uma continuação suave.

## SEQUÊNCIA DE CONTINUAÇÃO:

### 1. Analisar o Estado actual

Reveja a matéria principal para entender:

- `stepsCompleted`: Quais passos já são done
- `lastStep`: O número do passo mais recentemente concluído
- `inputDocuments`: Qual o contexto já foi carregado
- Todas as outras variáveis de matéria frontal

### 2. Carregar todos os documentos de entrada

Recarregar os documentos de contexto listados no `inputDocuments`:

- Para cada documento em `inputDocuments`, carregue o arquivo completo
- Isso garante que você tem contexto completo para a continuação
- Não descobrir novos documentos - apenas recarregar o que foi processado anteriormente

### 3. Resuma o progresso atual

Acolhe o usuário de volta e fornece contexto:
"Bem-vindo de volta BMADPROTECT032end}! Estou retomando nossa colaboração de design UX para {{project_name}}.

**Progresso atual:**

- Passos completados: {stepsCompleted}
- Último trabalho em: Passo {lastStep}
- Documentos de contexto disponíveis: arquivos {len(inputDocuments)}
- Especificação de projeto UX atual está pronto com todas as seções concluídas

**Estado do documento:**

- Documento de projeto UX atual está pronto com todas as seções concluídas
- Pronto para continuar de onde paramos

Isso parece certo, ou você quer fazer algum ajuste antes de prosseguirmos?"

### 4. Determinar o Passo Seguinte

Com base no valor `lastStep`, determinar qual passo para carregar a seguir:

- Se `lastStep = 1` → Carregar `./step-02-discovery.md`
- Se `lastStep = 2` → Carregar `./step-03-core-experience.md`
- Se `lastStep = 3` → Carregar `./step-04-emotional-response.md`
- Continuar este padrão para todos os passos
- Se `lastStep` indica passo final → Fluxo de trabalho já concluído

### 5. Opções de continuação atuais

Após apresentar os progressos actuais, pergunte:
"Pronto para continuar com Passo {nextStepNumber}: {nextStepTitle}?

[C] Continue a passo {nextStepNumber}"

## SUCESSO METRICOS:

✅ Todos os documentos de entrada anteriores foram recarregados com sucesso
✅ Estado de fluxo de trabalho atual analisado e apresentado com precisão
✅ Usuário confirma compreensão do progresso
✅ Próximo passo correto identificado e preparado para carregamento

## MODELOS DE FALHA:

❌ Descobrindo novos documentos de entrada em vez de recarregar os existentes
❌ Modificando conteúdo de etapas já concluídas
❌ Carregando o passo seguinte errado com base no valor `lastStep`
❌ Prosseguindo sem confirmação do usuário do estado atual

❌ **CRÍTICA**: Leitura de apenas um arquivo de passo parcial - leva a uma compreensão incompleta e a más decisões
❌ **CRITICAL**: Prosseguindo com **C** sem ler e compreender completamente o ficheiro do próximo passo
❌ **CRITICAL**: Tomar decisões sem compreensão completa dos requisitos e protocolos de etapas

O fluxo de trabalho já está completo?

Se `lastStep` indicar que o passo final está concluído:
"Óptimas notícias! Parece que já completamos o fluxo de trabalho de design UX para {{project_name}}.

A especificação final de projeto UX está pronta no {output_folder}/ux-design-specification.md com todas as seções concluídas através do passo {finalStepNumber}.

O design completo do UX inclui fundações visuais, fluxos de usuários e especificações de design prontas para implementation.

Gostaria que eu...

- Reveja a especificação de design UX completa com você
- Sugerir os próximos passos de fluxo de trabalho (como geração ou arquitetura de wireframe)
- Iniciar uma nova revisão de design UX

O que seria mais útil?"

## Próximo passo:

Depois que o usuário confirmar que eles estão prontos para continuar, carregue o arquivo seguinte apropriado com base no valor `lastStep` da matéria frontal.

Remember: Do NÃO carregue o próximo passo até que o usuário selecione explicitamente [C] para continuar!
