# Passo 1: Inicialização do fluxo de trabalho de projeto UX

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre facilitador de UX e stakeholder
- És um Facilitador UX, não um gerador de conteúdo.
- 💬 FOCUS na inicialização e configuração apenas - não olhe para a frente para passos futuros
- 🚪 DETECT estado de fluxo de trabalho existente e lidar com a continuação corretamente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Inicializar documento e atualizar frontmatter
- 📖 Configurar matéria frontal `stepsCompleted: [1]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que a configuração esteja completa

## CONTEXTO MONTANTES:

- Variáveis de workflow.md estão disponíveis em memória
- Contexto anterior = o que está no documento de saída + matéria frontal
- Não assumas o conhecimento de outras etapas.
- Descobrimento do documento de entrada acontece nesta etapa

A sua tarefa:

Inicialize o fluxo de trabalho de projeto UX detectando o estado de continuação e configurando o documento de especificação de projeto.

## SEQUÊNCIA DE INICIALIZAÇÃO:

### 1. Verificar o fluxo de trabalho existente

Primeiro, verifique se o documento de saída já existe:

- Procure o arquivo no `{output_folder}/ux-design-specification.md`
- Se existir, leia o arquivo completo, incluindo o frontmatter
- Se não existe, este é um novo fluxo de trabalho

### 2. Manusear a continuação (se o documento existir)

Se o documento existir e tiver matéria frontal com `stepsCompleted`:

- **STOP aqui** e carregar `./step-01b-continue.md` imediatamente
- Não prossiga com nenhuma tarefa de inicialização
- Deixe o passo-01b lidar com a lógica de continuação

### 3. Fresh Workflow Setup (Se nenhum documento)

Se não existir nenhum documento ou se não existir `stepsCompleted` no material da frente:

#### A. Descoberta do documento de entrada

Descubra e carregue documentos de contexto usando a descoberta inteligente:

**PRD (Prioridade: Análise → Main → Sharded → Inteiro):**

1. Verifique a pasta de análise: `{output_folder}/analysis/*prd*.md`
2. Se nenhum arquivo de análise: Tente pasta principal: `{output_folder}/*prd*.md`
3. Se nenhum arquivo principal: Verifique para pasta PRD sharded: `{output_folder}/*prd*/**/*.md`
4. Se existe pasta desfiada: Carregar cada arquivo nessa pasta completamente para o contexto UX
5. Adicionar arquivos descobertos para `inputDocuments` frontmatter

**Produto Breve (Prioridade: Análise → Main → Cortado → Inteiro):**

1. Verifique pasta de análise: `{output_folder}/analysis/*brief*.md`
2. Se nenhum arquivo de análise: Tente pasta principal: `{output_folder}/*brief*.md`
3. Se nenhum arquivo principal: Verifique para pasta breve sharded: `{output_folder}/*brief*/**/*.md`
4. Se existe pasta desfiada: Carregar todos os arquivos nessa pasta completamente
5. Adicionar arquivos descobertos à matéria frontal `inputDocuments`

**Documentos de pesquisa (Prioridade: Análise → Main → Sharded → Inteiro):**

1. Verifique a pasta de análise: `{output_folder}/analysis/research/*research*.md`
2. Se nenhum arquivo de análise: Tente pasta principal: `{output_folder}/*research*.md`
3. Se nenhum arquivo principal: Verifique para pasta de pesquisa sharded: `{output_folder}/*research*/**/*.md`
4. Carregar arquivos de pesquisa úteis completamente
5. Adicionar arquivos descobertos para `inputDocuments` frontmatter

**Outro contexto (Prioridade: Análise → Main → Sharded):**

- Epics: `{output_folder}/analysis/*epic*.md` ou `{output_folder}/*epic*.md` ou `{output_folder}/*epic*/**/*.md`
- Brainstorming: `{output_folder}/analysis/brainstorming/*brainstorming*.md` ou `{output_folder}/*brainstorming*.md`

**Regras de carga:**

- Carregar TODOS os arquivos descobertos completamente (sem deslocamento/limite)
- Para pastas em cacos, carregue TODOS os ficheiros para obter uma imagem completa
- Rastreie todos os arquivos carregados com sucesso no array `inputDocuments`

#### B. Criar Documento Inicial

Copiar o modelo de `{installed_path}/ux-design-template.md` para `{output_folder}/ux-design-specification.md`
Inicializar o material frontal com:

```yaml
---
stepsCompleted: []
inputDocuments: []
workflowType: 'ux-design'
lastStep: 0
project_name: '{{project_name}}'
user_name: '{{user_name}}'
date: '{{date}}'
---

```

#### C. Inicialização completa e relatório

Completar configuração e relatório ao usuário:

**Configuração do Documento:**

- Created: `{output_folder}/ux-design-specification.md` do modelo
- Frontmatter inicializado com estado de fluxo de trabalho

**Descoberto Documentos de Entrada:**
Relate o que foi encontrado:
Bem-vindo BMADPROTECT034end}! Eu configurei o seu espaço de trabalho de design UX para {{project_name}}.

**Documentos encontrados:**

- PRD: {number of PRD files loaded or "None found"}
- Resumo do produto: {number of brief files loaded or "None found"}
- Outro contexto: {number of other files loaded or "None found"}

**Arquivos carregados:** {list of specific file names or "No additional documents found"}

Tem outros documentos que queira que eu inclua, ou vamos continuar com o próximo passo?

[C] Continue à descoberta de UX"

## SUCESSO METRICOS:

✅ Fluxo de trabalho existente detectado e passado para o passo-01b corretamente
✅ Novo fluxo de trabalho