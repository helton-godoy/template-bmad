# Passo 1b: Manipulador de Continuação do Fluxo de Trabalho

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre pares arquitetônicos
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS sobre entender o estado atual e obter confirmação do usuário
- 🚪 workflow Handle retoma suave e transparente
A velocidade de desenvolvimento da IA mudou fundamentalmente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 📖 Leia o documento existente completamente para entender o estado atual
- 💾 Actualizar a matéria frontal para reflectir a continuação
- 🚫 PROJECTO de prosseguir para o próximo passo sem confirmação do utilizador

## CONTEXTO MONTANTES:

- Documento existente e material frontal estão disponíveis
- Documentos de entrada já carregados devem estar em matéria frontal `inputDocuments`
- Passos já concluídos estão no array `stepsCompleted`
- Concentra-te em entender de onde paramos

A sua tarefa:

Lidar com a continuação do fluxo de trabalho analisando o trabalho existente e orientando o usuário a retomar na etapa apropriada.

## SEQUÊNCIA DE CONTINUAÇÃO:

### 1. Analisar o estado atual do documento

Leia completamente o documento de arquitetura existente e analise:

**Análise de matéria:**

- `stepsCompleted`: Quais os passos foram done
- `inputDocuments`: Que documentos foram carregados
- `lastStep`: Último passo que foi executado
- BMADPROTECT010end, BMADPROTECT009end, BMADPROTECT008end: Contexto básico

**Análise de Conteúdo:**

- Que secções existem no documento
- Que decisões arquitectónicas foram tomadas
- O que parece incompleto ou em progresso
- Quaisquer TODOS ou lugares restantes

### 2. Resumo da continuação atual

Mostra ao utilizador o seu progresso actual:

"Bem-vindo de volta {{user_name}}! Encontrei o seu trabalho de Arquitetura para {{project_name}}.

**Progresso atual:**

- Passos completados: {{stepsCompleted list}}
- Última etapa trabalhada em: Passo {{lastStep}}
- Documentos de entrada carregados: arquivos {{number of inputDocuments}}

**Seções de documentação encontradas:**
{list all H2/H3 sections found in the document}

{if_incomplete_sections}
**Áreas incompletas:**

- {areas that appear incomplete or have placeholders}
{/if_incomplete_sections}

**O que gostarias de fazer?**
Retoma de onde paramos
[C] Continuar para o próximo passo lógico
[O] Visão geral de todos os passos restantes
[X] Iniciar de novo (substituirá o trabalho existente)
"

### 3. Lidar com a escolha do usuário

#### Se 'R' (Resuma de onde paramos):

- Identificar o próximo passo com base no `stepsCompleted`
- Carregar o arquivo passo apropriado para continuar
- Example: Se `stepsCompleted: [1, 2, 3]`, carregar `step-04-decisions.md`

#### Se 'C' (Continua com o próximo passo lógico):

- Analise o conteúdo do documento para determinar o próximo passo lógico
- Pode ser necessário rever a qualidade do conteúdo e completude
- Se o conteúdo parecer completo para o passo atual, avance para o próximo
- Se o conteúdo parecer incompleto, sugira ficar no passo atual

#### Se 'O' (Overview de todos os passos restantes):

- Fornecer uma breve descrição de todos os passos restantes
- Deixe o usuário escolher em que passo trabalhar
- Não assumas que a progressão sequencial é sempre melhor.

#### Se 'X' (Começar):

- Confirm: "This will delete all existing architectural decisions. Are you sure? (y/n)"
- Se confirmado: Excluir o documento existente e retornar ao step-01-init.md
- Se não confirmado: Voltar ao menu de continuação

### 4. Navegar para Passo Seleccionado

Após o usuário fazer a escolha:

**Carregue o arquivo de passo selecionado:**

- Atualizar matéria frontal `lastStep` para refletir navegação atual
- Execute o arquivo de passo selecionado
- Deixe esse passo lidar com a lógica de continuação detalhada

**Preservação do Estado:**

- Manter todo o conteúdo existente no documento
- Manter `stepsCompleted` preciso
- Acompanhe a retomada no estado do fluxo de trabalho

### 5. Casos especiais de continuação

#### Se o `stepsCompleted` estiver vazio, mas o documento tiver conteúdo:

- Isso sugere um fluxo de trabalho interrompido
- Pergunte ao usuário: "Eu vejo que o documento tem conteúdo, mas nenhum passo é marcado como completo. Devo analisar o que está aqui e definir o status de passo apropriado?"

#### Se o documento aparecer corrompido ou incompleto:

- Pergunte ao usuário: "O documento parece incompleto. Você gostaria que eu tentasse recuperar o que está aqui, ou você preferiria começar de novo?"

#### Se o documento estiver completo, mas o fluxo de trabalho não marcado como done:

- Pergunte ao usuário: "A arquitetura parece completa! Devo marcar este fluxo de trabalho como terminado, ou há mais em que você gostaria de trabalhar?"

## SUCESSO METRICOS:

✅ Estado do documento existente devidamente analisado e compreendido
✅ Usuário apresentou opções claras de continuação
✅ A escolha do utilizador é feita de forma adequada e transparente
✅ Estado de fluxo de trabalho preservado e atualizado corretamente
✅ Navegação para passo apropriado manuseado suavemente

## MODELOS DE FALHA:

❌ Não ler o documento completo existente antes de fazer sugestões
A perder o rasto do que