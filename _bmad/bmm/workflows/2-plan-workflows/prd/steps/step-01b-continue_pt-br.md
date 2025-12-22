---
name: 'step-01b-continue'
description: 'Resume an interrupted PRD workflow from the last completed step'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-01b-continue.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/prd.md'
---

# Etapa 1B: Continuação do fluxo de trabalho

## PASSO:

Retomar o fluxo de trabalho PRD de onde ele foi parado, garantindo a continuação suave com restauração de contexto completo.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um facilitador PM focado em produtos colaborando com um par especialista
- ✅ Nós nos engajamos em diálogo colaborativo, não em resposta a comandos
- ✅ Retomar o fluxo de trabalho a partir do ponto exato onde foi interrompido

### Regras específicas dos passos:

- 💬 Focus em entender onde paramos e continuar adequadamente
- 🚫 PROJECTO de modificar o conteúdo preenchido em etapas anteriores
- 📖 Somente recarregar documentos que já foram rastreados no `inputDocuments`

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostrar a sua análise do estado actual antes de agir
- 💾 Manter valores de matéria frontal existente `stepsCompleted`
- 📖 Somente carregar documentos que já foram rastreados no `inputDocuments`
- 🚫 PROIBIDA a descobrir novos documentos de entrada durante a continuação

## CONTEXTO MONTANTES:

- Contexto disponível: Documento atual e material frontal já estão carregados
- Focus: Análise de estado de fluxo de trabalho e lógica de continuação apenas
- Limits: Não assuma o conhecimento além do que está no documento.
- Dependencies: Estado de fluxo de trabalho existente da sessão anterior

## Sequência de Instruções (Não desvie, salte ou optimize)

### 1. Analisar o Estado actual

**Avaliação do Estado:**
Reveja a matéria principal para entender:

- `stepsCompleted`: Quais passos já são done
- `lastStep`: O número do passo mais recentemente concluído
- `inputDocuments`: Qual o contexto já foi carregado
BMADPROTECT042End breves, pesquisa, brainstorming, projetoContagens de documentos
- Todas as outras variáveis de matéria frontal

### 2. Restaurar Documentos de Contexto

**Recarregamento de contexto:**

- Para cada documento em `inputDocuments`, carregue o arquivo completo
- Isso garante que você tem contexto completo para a continuação
- Não descobrir novos documentos - apenas recarregar o que foi processado anteriormente

### 3. Progresso atual

**Relatório de Progresso ao Usuário:**
"Bem-vindos de volta {{user_name}ER"! Estou a retomar a nossa colaboração PRD para {{project_name}}.

**Progresso atual:**

- Passos completados: {stepsCompleted}
- Último trabalho em: Passo {lastStep}
- Documentos de contexto disponíveis: arquivos {len(inputDocuments)}

**Estado do documento:**

- Documento PRD atual está pronto com todas as seções concluídas
- Pronto para continuar de onde paramos

Isso parece certo, ou você quer fazer algum ajuste antes de prosseguirmos?"

### 4. Determinar o Caminho de Continuação

**Próximo passo lógica:**
Com base no valor `lastStep`, determinar qual passo para carregar a seguir:

- Se `lastStep = 1` → Carregar `./step-02-discovery.md`
- Se `lastStep = 2` → Carregar `./step-03-success.md`
- Se `lastStep = 3` → Carregar `./step-04-journeys.md`
- Se `lastStep = 4` → Carregar `./step-05-domain.md`
- Se `lastStep = 5` → Carregar `./step-06-innovation.md`
- Se `lastStep = 6` → Carregar `./step-07-project-type.md`
- Se `lastStep = 7` → Carregar `./step-08-scoping.md`
- Se `lastStep = 8` → Carregar `./step-09-functional.md`
- Se `lastStep = 9` → Carregar `./step-10-nonfunctional.md`
- Se `lastStep = 10` → Carregar `./step-11-complete.md`
- Se `lastStep = 11` → Fluxo de trabalho já concluído

### 5. Completação do fluxo de trabalho

**Se o fluxo de trabalho já estiver completo (`lastStep = 11`):**
"Óptimas notícias! Parece que já completamos o fluxo de trabalho PRD para {{project_name}}.

O documento final está pronto no `{outputFile}` com todas as seções completadas até o passo 11.

Gostaria que eu...

- Reveja o PRD completo com você
- Sugerir os próximos passos de fluxo de trabalho (como arquitetura ou criação épica)
- Iniciar uma nova revisão PRD

O que seria mais útil?"

### 6.

**Se o fluxo de trabalho não estiver completo:**
Exibir: "Pronto para continuar com Passo {nextStepNumber}?

**Selecionar uma Opção:** [C] Continuar para o próximo passo"

#### Logic de manipulação do menu:

- IF C: Carregar, ler arquivo inteiro, em seguida, executar o arquivo próximo passo apropriado com base em `lastStep`
- SE Quaisquer outros comentários ou consultas: responder e refazer menu

#### REGRAS DE execução:

- SEMPRE parar e esperar pela entrada do usuário após apresentar o menu
- APENAS prossiga para o próximo passo quando o usuário selecionar 'C'

## NOTA DE ENSAIO CRÍTICO

SOMENTE QUANDO [C continuar opção] é selecionado e [estado atual confirmado], você então carregar e ler completamente o arquivo próximo passo apropriado para retomar o fluxo de trabalho.

---

## 🚨

### ✅ SUCESSO:

- Todos os documentos de entrada anteriores recarregados com sucesso
- Estado atual do fluxo de trabalho