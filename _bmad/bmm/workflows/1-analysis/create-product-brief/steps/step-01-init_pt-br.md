---
name: 'step-01-init'
description: 'Inicializar o fluxo de trabalho de resumo de produto detectando o estado de continuação e configurando o documento'

# Definições de Caminho
workflow_path: '{project-root}/_bmad/bmm/workflows/1-analysis/product-brief'

# Referências de Arquivo
thisStepFile: '{workflow_path}/steps/step-01-init.md'
nextStepFile: '{workflow_path}/steps/step-02-vision.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/analysis/product-brief-{{project_name}}-{{date}}.md'

# Referências de Modelo
productBriefTemplate: '{workflow_path}/product-brief.template.md'
---

# Passo 1: Inicialização do Resumo de Produto

## OBJETIVO DO PASSO:

Inicializar o fluxo de trabalho de resumo de produto detectando o estado de continuação e configurando a estrutura do documento para descoberta colaborativa de produto.

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

### Regras Universais:

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- 📖 CRÍTICO: Leia o arquivo de passo completo antes de tomar qualquer ação
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido
- 📋 VOCÊ É UM FACILITADOR, não um gerador de conteúdo

### Reforço de Papel:

- ✅ Você é um facilitador Analista de Negócios focado no produto
- ✅ Se você já recebeu um nome, estilo de comunicação e persona, continue a usá-los enquanto desempenha este novo papel
- ✅ Engajamos em diálogo colaborativo, não comando-resposta
- ✅ Você traz pensamento estruturado e habilidades de facilitação, enquanto o usuário traz expertise de domínio e visão de produto
- ✅ Mantenha tom de descoberta colaborativa por todo o processo

### Regras Específicas do Passo:

- 🎯 Foque apenas na inicialização e configuração - sem geração de conteúdo ainda
- 🚫 PROIBIDO olhar adiante para passos futuros ou assumir conhecimento deles
- 💬 Abordagem: Configuração sistemática com relatório claro para o usuário
- 📋 Detecte o estado do fluxo de trabalho existente e lide com a continuação adequadamente

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

- Procure por arquivo em `{output_folder}/analysis/*product-brief*.md`
- Se existir, leia o arquivo completo incluindo frontmatter
- Se não existir, este é um fluxo de trabalho novo

### 2. Lidar com Continuação (Se Documento Existir)

Se o documento existe e tem frontmatter com `stepsCompleted`:

**Protocolo de Continuação:**

- **PARE imediatamente** e carregue `{workflow_path}/steps/step-01b-continue.md`
- Não prossiga com nenhuma tarefa de inicialização
- Deixe o step-01b lidar com toda a lógica de continuação
- Esta é uma situação de auto-prosseguimento - nenhuma escolha do usuário necessária

### 3. Configuração de Fluxo de Trabalho Novo (Se Sem Documento)

Se nenhum documento existe ou sem `stepsCompleted` no frontmatter:

#### A. Descoberta de Documento de Entrada

Descubra e carregue documentos de contexto usando descoberta inteligente:

**Documentos de Pesquisa (Prioridade: Fragmentado → Inteiro):**

1. Verifique por pasta de pesquisa fragmentada: `{output_folder}/analysis/research/**/*.md`
2. Se a pasta existir: Carregue CADA arquivo nessa pasta completamente
3. Se nenhuma pasta existir: Tente arquivo inteiro: `{output_folder}/analysis/research/*research*.md`
4. Adicione arquivos descobertos ao frontmatter `inputDocuments`

**Documentos de Brainstorming (Prioridade: Fragmentado → Inteiro):**

1. Verifique por pasta de brainstorming fragmentada: `{output_folder}/analysis/*brainstorm*/**/*.md`
2. Se a pasta existir: Carregue arquivos de brainstorming úteis completamente
3. Se nenhuma pasta existir: Tente arquivo inteiro: `{output_folder}/analysis/*brainstorm*.md`
4. Adicione arquivos descobertos ao frontmatter `inputDocuments`

**Documentação do Projeto (Projetos Existentes):**

1. Procure por arquivo de índice: `{output_folder}/**/index.md`
2. Carregue index.md para entender quais arquivos de projeto estão disponíveis
3. Leia arquivos disponíveis do índice para entender o contexto do projeto existente
4. Adicione arquivos descobertos ao frontmatter `inputDocuments`

#### B. Criar Documento Inicial

**Configuração do Documento:**

- Copie o modelo de `{productBriefTemplate}` para `{outputFile}`
- Inicialize frontmatter com estrutura adequada:

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

#### C. Apresentar Resultados da Inicialização

**Relatório de Configuração para o Usuário:**
"Bem-vindo {{user_name}}! Configurei seu espaço de trabalho de resumo de produto para {{project_name}}.

**Configuração do Documento:**

- Criado: `{outputFile}` a partir do modelo
- Inicializado frontmatter com estado do fluxo de trabalho

**Documentos de Entrada Descobertos:**

- Pesquisa: {número de arquivos de pesquisa carregados ou "Nenhum encontrado"}
- Brainstorming: {número de arquivos de brainstorming carregados ou "Nenhum encontrado"}
- Docs de projeto: {número de arquivos de projeto carregados ou "Nenhum encontrado"}

**Arquivos carregados:** {lista de nomes de arquivos específicos ou "Nenhum documento adicional encontrado"}

Você tem algum outro documento que gostaria que eu incluísse, ou devemos continuar para o próximo passo?"

### 4. Apresentar OPÇÕES DE MENU

Exibir: "**Prosseguindo para descoberta de visão de produto...**"

#### Lógica de Tratamento de Menu:

- Após o relatório de configuração ser apresentado, carregue imediatamente, leia o arquivo inteiro e então execute {nextStepFile}

#### REGRAS DE EXECUÇÃO:

- Este é um passo de inicialização com auto-prosseguimento após conclusão da configuração
- Prossiga diretamente para o próximo passo após configuração do documento e relatório

## NOTA CRÍTICA DE CONCLUSÃO DO PASSO

APENAS QUANDO [conclusão da configuração for alcançada e frontmatter devidamente atualizado], você então carregará e lerá completamente `{nextStepFile}` para executar e iniciar a descoberta de visão de produto.

---

## 🚨 MÉTRICAS DE SUCESSO/FALHA DO SISTEMA

### ✅ SUCESSO:

- Fluxo de trabalho existente detectado e devidamente entregue ao step-01b
- Novo fluxo de trabalho inicializado com modelo e frontmatter adequado
- Documentos de entrada descobertos e carregados usando lógica de fragmentado-primeiro
- Todos os arquivos descobertos rastreados no frontmatter `inputDocuments`
- Menu apresentado e entrada do usuário tratada corretamente
- Frontmatter atualizado com `stepsCompleted: [1]` antes de prosseguir

### ❌ FALHA DO SISTEMA:

- Prosseguir com nova inicialização quando fluxo de trabalho existente existe
- Não atualizar frontmatter com documentos de entrada descobertos
- Criar documento sem estrutura de modelo adequada
- Não verificar pastas fragmentadas primeiro antes de arquivos inteiros
- Não relatar documentos descobertos ao usuário claramente
- Prosseguir sem o usuário selecionar 'C' (Continuar)

**Regra Mestra:** Pular passos, otimizar sequências ou não seguir instruções exatas é PROIBIDO e constitui FALHA DO SISTEMA.
