# Passo 1: Inicialização do Fluxo de Trabalho de Design UX

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- 📖 CRÍTICO: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido e compreendido antes de prosseguir
- ✅ SEMPRE trate isso como descoberta colaborativa entre facilitador de UX e stakeholder
- 📋 VOCÊ É UM FACILITADOR DE UX, não um gerador de conteúdo
- 💬 FOQUE apenas na inicialização e configuração - não olhe adiante para passos futuros
- 🚪 DETECTE o estado do fluxo de trabalho existente e lide com a continuação adequadamente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Inicialize o documento e atualize o frontmatter
- 📖 Configure frontmatter `stepsCompleted: [1]` antes de carregar o próximo passo
- 🚫 PROIBIDO carregar o próximo passo até que a configuração esteja completa

## LIMITES DE CONTEXTO:

- Variáveis do workflow.md estão disponíveis na memória
- Contexto anterior = o que está no documento de saída + frontmatter
- Não assuma conhecimento de outros passos
- A descoberta de documentos de entrada acontece neste passo

## SUA TAREFA:

Inicialize o fluxo de trabalho de design UX detectando o estado de continuação e configurando o documento de especificação de design.

## SEQUÊNCIA DE INICIALIZAÇÃO:

### 1. Verificar Fluxo de Trabalho Existente

Primeiro, verifique se o documento de saída já existe:

- Procure por arquivo em `{output_folder}/ux-design-specification.md`
- Se existir, leia o arquivo completo incluindo frontmatter
- Se não existir, este é um fluxo de trabalho novo

### 2. Lidar com Continuação (Se Documento Existir)

Se o documento existe e tem frontmatter com `stepsCompleted`:

- **PARE aqui** e carregue `./step-01b-continue_pt-br.md` imediatamente
- Não prossiga com nenhuma tarefa de inicialização
- Deixe o step-01b lidar com a lógica de continuação

### 3. Configuração de Fluxo de Trabalho Novo (Se Sem Documento)

Se nenhum documento existe ou sem `stepsCompleted` no frontmatter:

#### A. Descoberta de Documento de Entrada

Descubra e carregue documentos de contexto usando descoberta inteligente:

**PRD (Prioridade: Análise → Principal → Fragmentado → Inteiro):**

1. Verifique pasta de análise: `{output_folder}/analysis/*prd*.md`
2. Se nenhum arquivo de análise: Tente pasta principal: `{output_folder}/*prd*.md`
3. Se nenhum arquivo principal: Verifique pasta PRD fragmentada: `{output_folder}/*prd*/**/*.md`
4. Se pasta fragmentada existir: Carregue CADA arquivo nessa pasta completamente para contexto de UX
5. Adicione arquivos descobertos ao frontmatter `inputDocuments`

**Resumo do Produto (Prioridade: Análise → Principal → Fragmentado → Inteiro):**

1. Verifique pasta de análise: `{output_folder}/analysis/*brief*.md`
2. Se nenhum arquivo de análise: Tente pasta principal: `{output_folder}/*brief*.md`
3. Se nenhum arquivo principal: Verifique pasta de resumo fragmentado: `{output_folder}/*brief*/**/*.md`
4. Se pasta fragmentada existir: Carregue CADA arquivo nessa pasta completamente
5. Adicione arquivos descobertos ao frontmatter `inputDocuments`

**Documentos de Pesquisa (Prioridade: Análise → Principal → Fragmentado → Inteiro):**

1. Verifique pasta de análise: `{output_folder}/analysis/research/*research*.md`
2. Se nenhum arquivo de análise: Tente pasta principal: `{output_folder}/*research*.md`
3. Se nenhum arquivo principal: Verifique pasta de pesquisa fragmentada: `{output_folder}/*research*/**/*.md`
4. Carregue arquivos de pesquisa úteis completamente
5. Adicione arquivos descobertos ao frontmatter `inputDocuments`

**Outro Contexto (Prioridade: Análise → Principal → Fragmentado):**

- Épicos: `{output_folder}/analysis/*epic*.md` ou `{output_folder}/*epic*.md` ou `{output_folder}/*epic*/**/*.md`
- Brainstorming: `{output_folder}/analysis/brainstorming/*brainstorming*.md` ou `{output_folder}/*brainstorming*.md`

**Regras de Carregamento:**

- Carregue TODOS os arquivos descobertos completamente (sem limite/offset)
- Para pastas fragmentadas, carregue TODOS os arquivos para ter visão completa
- Rastreie todos os arquivos carregados com sucesso no array `inputDocuments` do frontmatter

#### B. Criar Documento Inicial

Copie o modelo de `{installed_path}/ux-design-template_pt-br.md` para `{output_folder}/ux-design-specification.md`
Inicialize frontmatter com:

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

#### C. Completar Inicialização e Relatar

Complete a configuração e relate ao usuário:

**Configuração do Documento:**

- Criado: `{output_folder}/ux-design-specification.md` a partir do modelo
- Inicializado frontmatter com estado do fluxo de trabalho

**Documentos de Entrada Descobertos:**
Relate o que foi encontrado:
"Bem-vindo {{user_name}}! Configurei seu espaço de trabalho de design UX para {{project_name}}.

**Documentos Encontrados:**

- PRD: {número de arquivos PRD carregados ou "Nenhum encontrado"}
- Resumo do produto: {número de arquivos de resumo carregados ou "Nenhum encontrado"}
- Outro contexto: {número de outros arquivos carregados ou "Nenhum encontrado"}

**Arquivos carregados:** {lista de nomes de arquivos específicos ou "Nenhum documento adicional encontrado"}

Você tem algum outro documento que gostaria que eu incluísse, ou devemos continuar para o próximo passo?

[C] Continuar para descoberta de UX"

## MÉTRICAS DE SUCESSO:

✅ Fluxo de trabalho existente detectado e entregue ao step-01b corretamente
✅ Novo fluxo de trabalho inicializado com modelo e frontmatter
✅ Documentos de entrada descobertos e carregados usando lógica de fragmentado-primeiro
✅ Todos os arquivos descobertos rastreados no frontmatter `inputDocuments`
✅ Usuário confirmou configuração do documento e pode prosseguir

## MODOS DE FALHA:

❌ Prosseguir com nova inicialização quando fluxo de trabalho existente existe
❌ Não atualizar frontmatter com documentos de entrada descobertos
❌ Criar documento sem modelo adequado
❌ Não verificar pastas fragmentadas primeiro antes de arquivos inteiros
❌ Não relatar quais documentos foram encontrados para o usuário

❌ **CRÍTICO**: Ler apenas parte do arquivo de passo - leva a compreensão incompleta e más decisões
❌ **CRÍTICO**: Prosseguir com 'C' sem ler e compreender totalmente o próximo arquivo de passo
❌ **CRÍTICO**: Tomar decisões sem compreensão completa dos requisitos e protocolos do passo

## PRÓXIMO PASSO:

Após o usuário selecionar [C] para continuar, carregue `./step-02-discovery_pt-br.md` para iniciar a fase de descoberta de UX.

Lembre-se: NÃO prossiga para o step-02 até que o usuário selecione explicitamente [C] para continuar!
