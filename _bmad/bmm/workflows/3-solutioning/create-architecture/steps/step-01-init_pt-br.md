# Etapa 1: Inicialização do fluxo de trabalho de arquitetura

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre pares arquitetônicos
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS na inicialização e configuração apenas - não olhe para a frente para passos futuros
- 🚪 DETECT estado de fluxo de trabalho existente e lidar com a continuação corretamente
A velocidade de desenvolvimento da IA mudou fundamentalmente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Inicializar documento e atualizar frontmatter
- 📖 Configurar matéria frontal `stepsCompleted: [1]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que a configuração esteja completa

## CONTEXTO MONTANTES:

- Variáveis do workflow.md estão disponíveis na memória
- Contexto anterior = o que está no documento de saída + matéria frontal
- Não assumas o conhecimento de outras etapas.
- Descobrimento do documento de entrada acontece nesta etapa

A sua tarefa:

Inicialize o fluxo de trabalho de arquitetura detectando o estado de continuação, descobrindo documentos de entrada e configurando o documento para a tomada de decisão arquitetural colaborativa.

## SEQUÊNCIA DE INICIALIZAÇÃO:

### 1. Verificar o fluxo de trabalho existente

Primeiro, verifique se o documento de saída já existe:

- Procura o ficheiro no `{output_folder}/architecture.md`
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

**Documento PRD (Prioridade: Análise → Main → Sharded → Inteiro):**

1. Verifique pasta de análise: `{output_folder}/*prd*.md`
2. Se nenhum arquivo principal: Verifique para pasta PRD sharded: `{output_folder}/*prd*/**/*.md`
3. Se existe pasta desfiada: Carregar cada arquivo nessa pasta completamente
4. Adicionar arquivos descobertos para `inputDocuments` frontmatter

**Epics/Storys Document (Prioridade: Análise → Main → Sharded → Whole):**

1. Verifique a pasta de análise: `{output_folder}/analysis/*epic*.md`
2. Se nenhum arquivo de análise: Tente pasta principal: `{output_folder}/*epic*.md`
3. Se nenhum arquivo principal: Verifique para pasta épica sharded: `{output_folder}/*epic*/**/*.md`
4. Se existe pasta desfiada: Carregar todos os arquivos nessa pasta completamente
5. Adicionar arquivos descobertos para `inputDocuments` frontmatter

**UX Design Specification (Prioridade: Análise → Main → Sharded → Whole):**

1. Verifique pasta: `{output_folder}/*ux*.md`
2. Se nenhum arquivo principal: Verifique para pasta UX sharded: `{output_folder}/*ux*/**/*.md`
3. Se existe pasta desfiada: Carregar cada arquivo nessa pasta completamente
4. Adicionar arquivos descobertos à matéria frontal `inputDocuments`

**Documentos de pesquisa (Prioridade: Análise → Principal):**

1. Verifique pasta: `{output_folder}/research/*research*.md`
2. Se nenhum arquivo: Tente pasta: `{output_folder}/*research*.md`
3. Adicionar arquivos descobertos à matéria frontal `inputDocuments`

**Documentação do Projeto (Projetos existentes):**

1. Procure o arquivo de índice: `{output_folder/index.md`
2. CRITICAL: Carregar index.md para entender quais arquivos de projeto estão disponíveis
3. Leia arquivos disponíveis do índice para entender o contexto do projeto existente
4. Isso fornece um contexto essencial para estender o projeto existente com nova arquitetura
5. Adicionar arquivos descobertos à matéria frontal `inputDocuments`

**Regras de Contexto do Projeto (Crítica para Agentes de IA):**

1. Verifique o arquivo de contexto do projeto: `**/project-context.md`
2. Se existir: Carregar o conteúdo do arquivo COMPLETE - isto contém regras críticas para agentes de IA
3. Adicionar ao frontmatter `hasProjectContext: true` e track caminho do arquivo
4. Relatório ao usuário: "Encontrado contexto de projeto existente com {number_of_rules} regras de agente"
5. Este arquivo contém padrões específicos de linguagem, regras de teste, e implementation diretrizes que devem ser seguidas

**Regras de carga:**

- Carregar TODOS os arquivos descobertos completamente (sem deslocamento/limite)
- Para pastas em cacos, carregue TODOS os ficheiros para obter uma imagem completa
- Para projetos existentes, use index.md como guia para o que é relevante
- Acompanhe todos os arquivos carregados com sucesso no array `inputDocuments`

#### B. Validar entradas necessárias

Antes de prosseguir, verifique se temos os insumos essenciais:

**Validação PRD:**

- Se nenhum PRD encontrado: "A arquitetura requer um PRD para trabalhar. Por favor, execute o fluxo de trabalho PRD primeiro ou forneça o caminho do arquivo PRD."
- Não proceder sem PRD

**Outras entradas:**

- Especificações UX: "Fornece requisitos de arquitectura UI/UX" (Opcional)

#### C. Criar Documento Inicial

Copiar o te