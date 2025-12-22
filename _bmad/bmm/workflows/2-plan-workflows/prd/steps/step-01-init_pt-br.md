---
name: 'step-01-init'
description: 'Initialize the PRD workflow by detecting continuation state and setting up the document'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-01-init.md'
nextStepFile: '{workflow_path}/steps/step-02-discovery.md'
continueStepFile: '{workflow_path}/steps/step-01b-continue.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/prd.md'

# Template References
prdTemplate: '{workflow_path}/prd-template.md'
---

# Passo 1: Inicialização do fluxo de trabalho

**Progresso: Passo 1 de 11** - Próximo: Project Discovery

## PASSO:

Inicialize o fluxo de trabalho PRD detectando o estado de continuação, descobrindo documentos de entrada e configurando a estrutura do documento para a descoberta colaborativa de requisitos de produto.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um facilitador PM focado em produtos colaborando com um par especialista
- ✅ Se você já recebeu um nome, communication style e persona, continue usando-os enquanto desempenha este novo papel
- ✅ Nós nos engajamos em diálogo colaborativo, não em resposta a comandos
- ✅ Você traz habilidades de pensamento estruturado e facilitação, enquanto o usuário traz conhecimento de domínio e visão de produto

### Regras específicas dos passos:

- 🎯 Foco apenas na inicialização e configuração - sem geração de conteúdo ainda
- 🚫 PROJECTO de olhar adiante para os passos futuros ou assumir conhecimento deles
- 💬 Abordagem: Configuração sistemática com relatórios claros ao usuário
- 🚪 Detectar o estado de fluxo de trabalho existente e lidar com a continuação corretamente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostrar a sua análise do estado atual antes de tomar qualquer ação
- 💾 Inicializar a estrutura do documento e atualizar o frontmatter apropriadamente
- 📖 Configurar matéria frontal `stepsCompleted: [1]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o usuário selecione 'C' (Continuar)

## CONTEXTO MONTANTES:

- Contexto disponível: Variáveis da workflow.md estão disponíveis na memória
- Focus: Inicialização do fluxo de trabalho e configuração do documento apenas
- Limits: Não assuma conhecimento de outras etapas ou crie conteúdo ainda
- Dependencies: Configuração carregada da inicialização do workflow.md

## Sequência de Instruções (Não desvie, salte ou optimize)

### 1. Verificação do Estado de fluxo de trabalho existente

Primeiro, verifique se o documento de saída já existe:

**Detecção do Estado de fluxo de trabalho:**

- Procure o arquivo no `{outputFile}`
- Se existir, leia o arquivo completo, incluindo o frontmatter
- Se não existe, este é um novo fluxo de trabalho

### 2. Manusear a continuação (se o documento existir)

Se o documento existir e tiver matéria-prima com `stepsCompleted`:

**Protocolo de continuação:**

- **STOP imediatamente** e carregar `{continueStepFile}`
- Não prossiga com nenhuma tarefa de inicialização
- Deixe passo-01b lidar com toda a lógica de continuação
- Esta é uma situação auto-procedida - nenhuma escolha do usuário necessária

### 3. Fresh Workflow Setup (Se nenhum documento)

Se não existir nenhum documento ou se não existir `stepsCompleted` na matéria frontal:

#### A. Descoberta do documento de entrada

Descubra e carregue documentos de contexto usando a descoberta inteligente.

**IMPORTANTE: O documento de trilha conta enquanto você descobre arquivos.**

Inicializar contadores:

```
briefCount = 0
researchCount = 0
brainstormingCount = 0
projectDocsCount = 0

```

**Produto Breve (Prioridade: Análise → Main → Cortado → Inteiro):**

1. Verifique a pasta de análise: `{output_folder}/analysis/*brief*.md`
2. Se nenhum arquivo de análise: Tente pasta principal: `{output_folder}/*brief*.md`
3. Se nenhum arquivo principal: Verifique para pasta breve sharded: `{output_folder}/*brief*/**/*.md`
4. Se existe pasta desfiada: Carregar todos os arquivos nessa pasta completamente
5. Adicionar arquivos descobertos à matéria frontal `inputDocuments`
6. **Atualizar resumoContar com o número de arquivos encontrados**

**Documentos de pesquisa (Prioridade: Análise → Main → Sharded → Inteiro):**

1. Verifique pasta de análise: `{output_folder}/analysis/research/*research*.md`
2. Se nenhum arquivo de análise: Tente pasta principal: `{output_folder}/*research*.md`
3. Se nenhum arquivo principal: Verifique para pasta de pesquisa sharded: `{output_folder}/*research*/**/*.md`
4. Carregar arquivos de pesquisa úteis completamente
5. Adicionar arquivos descobertos à matéria frontal `inputDocuments`
6. **Atualizar pesquisaContar com o número de arquivos encontrados**

**Documentos Brainstorming (Prioridade: Análise → Principal):**

1. Verifique a pasta de análise: `{output_folder}/analysis/brainstorming/*brainstorming*.md`
2. Se nenhum arquivo de análise: Tente pasta principal: `{output_folder}/*brainstorming*.md`
3. Adicionar arquivos descobertos à matéria frontal `inputDocuments`
4. **Update brainstormingConta com o número de arquivos encontrados**

**Documentação do projecto (Projectos existentes - Brownfield):**

1. Procure o arquivo de índice: `{output_folder}/index.md`
2. CRITICAL: Carregar index.md para entender quais arquivos de projeto estão disponíveis
3. Leia arquivos disponíveis de i