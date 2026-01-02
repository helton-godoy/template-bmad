---
name: 'step-01-init'
description: 'Inicializar o fluxo de trabalho PRD detectando estado de continuação e configurando o documento'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-01-init_pt-br.md'
nextStepFile: '{workflow_path}/steps/step-02-discovery_pt-br.md'
continueStepFile: '{workflow_path}/steps/step-01b-continue_pt-br.md'
workflowFile: '{workflow_path}/workflow_pt-br.md'
outputFile: '{output_folder}/prd.md'

# Template References
prdTemplate: '{workflow_path}/prd-template_pt-br.md'
---

# Passo 1: Inicialização do Fluxo de Trabalho

**Progresso: Passo 1 de 11** - Próximo: Descoberta do Projeto

## OBJETIVO DO PASSO:

Inicializar o fluxo de trabalho PRD detectando estado de continuação, descobrindo documentos de entrada e configurando a estrutura do documento para descoberta colaborativa de requisitos de produto.

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

### Regras Universais:

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- 📖 CRÍTICO: Leia o arquivo de passo completo antes de tomar qualquer ação
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido
- 📋 VOCÊ É UM FACILITADOR, não um gerador de conteúdo

### Reforço de Papel:

- ✅ Você é um facilitador PM focado no produto colaborando com um par especialista
- ✅ Se você já recebeu um nome, estilo de comunicação e persona, continue a usá-los enquanto desempenha este novo papel
- ✅ Engajamos em diálogo colaborativo, não comando-resposta
- ✅ Você traz pensamento estruturado e habilidades de facilitação, enquanto o usuário traz expertise de domínio e visão de produto

### Regras Específicas do Passo:

- 🎯 Foque apenas na inicialização e configuração - sem geração de conteúdo ainda
- 🚫 PROIBIDO olhar adiante para passos futuros ou assumir conhecimento deles
- 💬 Abordagem: Configuração sistemática com relatório claro para o usuário
- 🚪 Detecte o estado do fluxo de trabalho existente e lide com a continuação adequadamente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise do estado atual antes de tomar qualquer ação
- 💾 Inicialize a estrutura do documento e atualize o frontmatter apropriadamente
- 📖 Configure frontmatter `stepsCompleted: [1]` antes de carregar o próximo passo
- 🚫 PROIBIDO carregar o próximo passo até que o usuário selecione 'C' (Continuar)

## LIMITES DE CONTEXTO:

- Contexto disponível: Variáveis de workflow.md estão disponíveis na memória
- Foco: Inicialização do fluxo de trabalho e configuração do documento apenas
- Limites: Não assuma conhecimento de outros passos ou crie conteúdo ainda
- Dependências: Configuração carregada da inicialização do workflow.md

## Sequência de Instruções (Não desvie, pule ou otimize)

### 1. Verificar Estado do Fluxo de Trabalho Existente

Primeiro, verifique se o documento de saída já existe:

**Detecção de Estado do Fluxo de Trabalho:**

- Procure por arquivo em `{outputFile}`
- Se existir, leia o arquivo completo incluindo frontmatter
- Se não existir, este é um fluxo de trabalho novo

### 2. Lidar com Continuação (Se Documento Existir)

Se o documento existe e tem frontmatter com `stepsCompleted`:

**Protocolo de Continuação:**

- **PARE imediatamente** e carregue `{continueStepFile}`
- Não prossiga com nenhuma tarefa de inicialização
- Deixe o step-01b lidar com toda a lógica de continuação
- Esta é uma situação de auto-prosseguimento - nenhuma escolha do usuário necessária

### 3. Configuração de Fluxo de Trabalho Novo (Se Sem Documento)

Se nenhum documento existe ou sem `stepsCompleted` no frontmatter:

#### A. Descoberta de Documento de Entrada

Descubra e carregue documentos de contexto usando descoberta inteligente.

**IMPORTANTE: Rastreie contagens de documentos conforme você descobre arquivos.**

Inicialize contadores:

```
briefCount = 0
researchCount = 0
brainstormingCount = 0
projectDocsCount = 0
```

**Resumo do Produto (Prioridade: Análise → Principal → Fragmentado → Inteiro):**

1. Verifique pasta de análise: `{output_folder}/analysis/*brief*.md`
2. Se nenhum arquivo de análise: Tente pasta principal: `{output_folder}/*brief*.md`
3. Se nenhum arquivo principal: Verifique pasta de resumo fragmentado: `{output_folder}/*brief*/**/*.md`
4. Se pasta fragmentada existir: Carregue CADA arquivo nessa pasta completamente
5. Adicione arquivos descobertos ao frontmatter `inputDocuments`
6. **Atualize briefCount com número de arquivos encontrados**

**Documentos de Pesquisa (Prioridade: Análise → Principal → Fragmentado → Inteiro):**

1. Verifique pasta de análise: `{output_folder}/analysis/research/*research*.md`
2. Se nenhum arquivo de análise: Tente pasta principal: `{output_folder}/*research*.md`
3. Se nenhum arquivo principal: Verifique pasta de pesquisa fragmentada: `{output_folder}/*research*/**/*.md`
4. Carregue arquivos de pesquisa úteis completamente
5. Adicione arquivos descobertos ao frontmatter `inputDocuments`
6. **Atualize researchCount com número de arquivos encontrados**

**Documentos de Brainstorming (Prioridade: Análise → Principal):**

1. Verifique pasta de análise: `{output_folder}/analysis/brainstorming/*brainstorming*.md`
2. Se nenhum arquivo de análise: Tente pasta principal: `{output_folder}/*brainstorming*.md`
3. Adicione arquivos descobertos ao frontmatter `inputDocuments`
4. **Atualize brainstormingCount com número de arquivos encontrados**

**Documentação do Projeto (Projetos Existentes - Brownfield):**

1. Procure por arquivo de índice: `{output_folder}/index.md`
2. CRÍTICO: Carregue index.md para entender quais arquivos de projeto estão disponíveis
3. Leia arquivos disponíveis do índice para entender o contexto do projeto existente
4. Isso fornece contexto essencial para estender projeto existente com novo PRD
5. Adicione arquivos descobertos ao frontmatter `inputDocuments`
6. **Atualize projectDocsCount com número de arquivos encontrados (incluindo index.md)**

**Regras de Carregamento:**

- Carregue TODOS os arquivos descobertos completamente (sem limite/offset)
- Para pastas fragmentadas, carregue TODOS os arquivos para ter visão completa
- Para projetos existentes, use index.md como guia para o que é relevante
- Rastreie todos os arquivos carregados com sucesso no array `inputDocuments` do frontmatter

#### B. Criar Documento Inicial

**Configuração do Documento:**

- Copie o modelo de `{prdTemplate}` para `{outputFile}`
- Inicialize frontmatter com estrutura adequada incluindo contagens de documentos:

```yaml
---
stepsCompleted: []
inputDocuments: []
documentCounts:
  briefs: { { briefCount } }
  research: { { researchCount } }
  brainstorming: { { brainstormingCount } }
  projectDocs: { { projectDocsCount } }
workflowType: 'prd'
lastStep: 0
project_name: '{{project_name}}'
user_name: '{{user_name}}'
date: '{{date}}'
---
```

#### C. Apresentar Resultados da Inicialização

**Relatório de Configuração para o Usuário:**

"Bem-vindo {{user_name}}! Configurei seu espaço de trabalho de PRD para {{project_name}}.

**Configuração do Documento:**

- Criado: `{outputFile}` a partir do modelo
- Inicializado frontmatter com estado do fluxo de trabalho

**Documentos de Entrada Descobertos:**

- Resumos de produto: {{briefCount}} arquivos {if briefCount > 0}✓ carregados{else}(nenhum encontrado){/if}
- Pesquisa: {{researchCount}} arquivos {if researchCount > 0}✓ carregados{else}(nenhum encontrado){/if}
- Brainstorming: {{brainstormingCount}} arquivos {if brainstormingCount > 0}✓ carregados{else}(nenhum encontrado){/if}
- Docs de projeto: {{projectDocsCount}} arquivos {if projectDocsCount > 0}✓ carregados (projeto brownfield){else}(nenhum encontrado - projeto greenfield){/if}

**Arquivos carregados:** {lista de nomes de arquivos específicos ou "Nenhum documento adicional encontrado"}

{if projectDocsCount > 0}
📋 **Nota:** Este é um **projeto brownfield**. Sua documentação de projeto existente foi carregada. No próximo passo, perguntarei especificamente sobre quais novos recursos ou mudanças você deseja adicionar ao seu sistema existente.
{/if}

Você tem algum outro documento que gostaria que eu incluísse, ou devemos continuar para o próximo passo?"

### 4. Apresentar OPÇÕES DE MENU

Exibir menu após relatório de configuração:

"[C] Continuar - Salvar isso e mover para Descoberta do Projeto (Passo 2 de 11)"

#### Lógica de Tratamento de Menu:

- SE C: Atualize frontmatter com `stepsCompleted: [1]`, então carregue, leia arquivo inteiro e execute {nextStepFile}
- SE usuário fornecer arquivos adicionais: Carregue-os, atualize inputDocuments e documentCounts, exiba novamente o relatório
- SE usuário fizer perguntas: Responda e exiba novamente o menu

#### REGRAS DE EXECUÇÃO:

- SEMPRE pare e aguarde a entrada do usuário após apresentar o menu
- APENAS prossiga para o próximo passo quando o usuário selecionar 'C'

## NOTA CRÍTICA DE CONCLUSÃO DO PASSO

APENAS QUANDO [opção C continuar] for selecionada e [frontmatter devidamente atualizado com stepsCompleted: [1] e documentCounts], você então carregará e lerá completamente `{nextStepFile}` para executar e iniciar a descoberta do projeto.

---

## 🚨 MÉTRICAS DE SUCESSO/FALHA DO SISTEMA

### ✅ SUCESSO:

- Fluxo de trabalho existente detectado e devidamente entregue ao step-01b
- Novo fluxo de trabalho inicializado com modelo e frontmatter adequado
- Documentos de entrada descobertos e carregados usando lógica de fragmentado-primeiro
- Todos os arquivos descobertos rastreados no frontmatter `inputDocuments`
- **Contagens de documentos armazenadas no frontmatter `documentCounts`**
- Usuário claramente informado sobre status brownfield vs greenfield
- Menu apresentado e entrada do usuário tratada corretamente
- Frontmatter atualizado com `stepsCompleted: [1]` antes de prosseguir

### ❌ FALHA DO SISTEMA:

- Prosseguir com nova inicialização quando fluxo de trabalho existente existe
- Não atualizar frontmatter com documentos de entrada descobertos
- **Não armazenar contagens de documentos no frontmatter**
- Criar documento sem estrutura de modelo adequada
- Não verificar pastas fragmentadas primeiro antes de arquivos inteiros
- Não relatar documentos descobertos ao usuário claramente
- Prosseguir sem o usuário selecionar 'C' (Continuar)

**Regra Mestra:** Pular passos, otimizar sequências ou não seguir instruções exatas é PROIBIDO e constitui FALHA DO SISTEMA.
