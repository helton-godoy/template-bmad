---
name: 'step-01-init'
description: 'Initialize the product brief workflow by detecting continuation state and setting up the document'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/1-analysis/product-brief'

# File References
thisStepFile: '{workflow_path}/steps/step-01-init.md'
nextStepFile: '{workflow_path}/steps/step-02-vision.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/analysis/product-brief-{{project_name}}-{{date}}.md'

# Template References
productBriefTemplate: '{workflow_path}/product-brief.template.md'
---

# Etapa 1: Inicialização do resumo do produto

## PASSO:

Inicialize o breve fluxo de trabalho do produto detectando o estado de continuação e configurando a estrutura do documento para a descoberta colaborativa do produto.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um facilitador de análise de negócios focado no produto
- ✅ Se você já recebeu um nome, communication style e persona, continue usando-os enquanto desempenha este novo papel
- ✅ Nós nos engajamos em diálogo colaborativo, não em resposta a comandos
- ✅ Você traz habilidades de pensamento estruturado e facilitação, enquanto o usuário traz conhecimento de domínio e visão de produto
- ✅ Mantenha o tom de descoberta colaborativo ao longo

### Regras específicas dos passos:

- 🎯 Foco apenas na inicialização e configuração - sem geração de conteúdo ainda
- 🚫 PROJECTO de olhar adiante para os passos futuros ou assumir conhecimento deles
- 💬 Abordagem: Configuração sistemática com relatórios claros ao utilizador
- 📋 Detectar o estado de fluxo de trabalho existente e lidar com a continuação corretamente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostrar a sua análise do estado atual antes de tomar qualquer ação
- 💾 Inicializar a estrutura do documento e atualizar o frontmatter apropriadamente
- 📖 Configurar matéria frontal `stepsCompleted: [1]` antes de carregar o próximo passo
- 🚫 FORBIDEN para carregar o próximo passo até que o usuário selecione 'C' (Continuar)

## CONTEXTO MONTANTES:

- Contexto disponível: Variáveis da workflow.md estão disponíveis na memória
- Focus: Inicialização do fluxo de trabalho e configuração do documento apenas
- Limits: Não assuma conhecimento de outras etapas ou crie conteúdo ainda
- Dependencies: Configuração carregada da inicialização do workflow.md

## Sequência de Instruções (Não desvie, salte ou optimize)

### 1. Verificação do Estado de fluxo de trabalho existente

Primeiro, verifique se o documento de saída já existe:

**Detecção do Estado de fluxo de trabalho:**

- Procure o arquivo no `{output_folder}/analysis/*product-brief*.md`
- Se existir, leia o arquivo completo, incluindo o frontmatter
- Se não existe, este é um novo fluxo de trabalho

### 2. Manusear a continuação (se o documento existir)

Se o documento existir e tiver matéria-prima com `stepsCompleted`:

**Protocolo de continuação:**

- **STOP imediatamente** e carregar `{workflow_path}/steps/step-01b-continue.md`
- Não prossiga com nenhuma tarefa de inicialização
- Deixe passo-01b lidar com toda a lógica de continuação
- Esta é uma situação auto-procedida - nenhuma escolha do usuário necessária

### 3. Fresh Workflow Setup (Se nenhum documento)

Se não existir nenhum documento ou se não existir `stepsCompleted` na matéria frontal:

#### A. Descoberta do documento de entrada

Descubra e carregue documentos de contexto usando a descoberta inteligente:

**Documentos de pesquisa (Prioridade: Sharded → Inteiro):**

1. Verifique para pasta de pesquisa sharded: `{output_folder}/analysis/research/**/*.md`
2. Se a pasta existe: Carregar TODOS os arquivos nessa pasta completamente
3. Se nenhuma pasta existe: Tente o arquivo inteiro: `{output_folder}/analysis/research/*research*.md`
4. Adicionar arquivos descobertos para `inputDocuments` frontmatter

**Documentos Brainstorming (Prioridade: Sharded → Inteiro):**

1. Verifique para pasta de brainstorming sharded: `{output_folder}/analysis/*brainstorm*/**/*.md`
2. Se a pasta existe: Carregar arquivos de brainstorming úteis completamente
3. Se nenhuma pasta existe: Tente o arquivo inteiro: `{output_folder}/analysis/*brainstorm*.md`
4. Adicionar arquivos descobertos à matéria frontal `inputDocuments`

**Documentação do Projeto (Projetos existentes):**

1. Procure o arquivo de índice: `{output_folder}/**/index.md`
2. Carregar index.md para entender quais arquivos de projeto estão disponíveis
3. Leia arquivos disponíveis do índice para entender o contexto do projeto existente
4. Adicionar arquivos descobertos à matéria frontal `inputDocuments`

#### B. Criar Documento Inicial

**Configuração do Documento:**

- Copiar o modelo de `{productBriefTemplate}` para `{outputFile}`
- Inicializar a matéria frontal com estrutura adequada:

```yaml
---
stepsCompleted: []
inputDocuments: []
workflowType: 'product-brief'
lastStep: 0
project_name: '{{project_name}}'
user_name: '{{user_name}}'
date: '{{date}}'
---

```

#### C. Apresentar Resultados de Inicialização

**Setup Report to User:**
Bem-vindo BMADPROTECT023end}! Eu configurei o seu breve espaço de trabalho para o {{project_name}}.

**Configuração do Documento:**

- Created: `{outputFile}` do modelo
- Frontmatter inicializado com estado de fluxo de trabalho

**Descoberto Documentos de Entrada:**

- Não.