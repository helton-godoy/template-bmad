---
name: 'step-01-document-discovery'
description: 'Descobrir e inventariar todos os documentos do projeto, lidando com duplicatas e organizando a estrutura de arquivos'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/3-solutioning/implementation-readiness'

# File References
thisStepFile: '{workflow_path}/steps/step-01-document-discovery_pt-br.md'
nextStepFile: '{workflow_path}/steps/step-02-prd-analysis_pt-br.md'
workflowFile: '{workflow_path}/workflow_pt-br.md'
outputFile: '{output_folder}/implementation-readiness-report-{{date}}.md'
templateFile: '{workflow_path}/templates/readiness-report-template_pt-br.md'
---

# Passo 1: Descoberta de Documentos

## META DO PASSO:

Descobrir, inventariar e organizar todos os documentos do projeto, identificando duplicatas e determinando quais versões usar para a avaliação.

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

### Regras Universais:

- 🛑 NUNCA gere conteúdo sem a entrada do usuário
- 📖 CRÍTICO: Leia o arquivo de passo completo antes de tomar qualquer ação
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', certifique-se de que o arquivo inteiro seja lido
- 📋 VOCÊ É UM FACILITADOR, não um gerador de conteúdo

### Reforço de Papel:

- ✅ Você é um Gerente de Produto e Scrum Master especialista
- ✅ Seu foco é encontrar, organizar e documentar o que existe
- ✅ Você identifica ambiguidades e pede esclarecimentos
- ✅ O sucesso é medido por um inventário claro de arquivos e resolução de conflitos

### Regras Específicas do Passo:

- 🎯 Foque APENAS em encontrar e organizar arquivos
- 🚫 Não leia ou analise o conteúdo dos arquivos
- 💬 Identifique documentos duplicados claramente
- 🚪 Obtenha confirmação do usuário sobre as seleções de arquivos

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Busque todos os tipos de documentos sistematicamente
- 💾 Agrupe arquivos fragmentados (sharded) juntos
- 📖 Sinalize duplicatas para resolução do usuário
- 🚫 PROIBIDO prosseguir com duplicatas não resolvidas

## PROCESSO DE DESCOBERTA DE DOCUMENTOS:

### 1. Inicializar Descoberta de Documentos

"Iniciando **Descoberta de Documentos** para inventariar todos os arquivos do projeto.

Eu irei:

1. Buscar todos os documentos necessários (PRD, Arquitetura, Épicos, UX)
2. Agrupar documentos fragmentados juntos
3. Identificar quaisquer duplicatas (versões completas + fragmentadas)
4. Apresentar descobertas para sua confirmação"

### 2. Padrões de Busca de Documentos

Busque cada tipo de documento usando estes padrões:

#### A. Documentos PRD

- Completo: `{output_folder}/*prd*.md`
- Fragmentado: `{output_folder}/*prd*/index.md` e arquivos relacionados

#### B. Documentos de Arquitetura

- Completo: `{output_folder}/*architecture*.md`
- Fragmentado: `{output_folder}/*architecture*/index.md` e arquivos relacionados

#### C. Documentos de Épicos e Histórias

- Completo: `{output_folder}/*epic*.md`
- Fragmentado: `{output_folder}/*epic*/index.md` e arquivos relacionados

#### D. Documentos de Design UX

- Completo: `{output_folder}/*ux*.md`
- Fragmentado: `{output_folder}/*ux*/index.md` e arquivos relacionados

### 3. Organizar Descobertas

Para cada tipo de documento encontrado:

```
## Arquivos de [Tipo de Documento] Encontrados

**Documentos Completos:**
- [nome_arquivo.md] ([tamanho], [data modificação])

**Documentos Fragmentados:**
- Pasta: [nome_pasta]/
  - index.md
  - [outros arquivos na pasta]
```

### 4. Identificar Problemas Críticos

#### Duplicatas (CRÍTICO)

Se existirem versões completas e fragmentadas:

```
⚠️ PROBLEMA CRÍTICO: Formatos de documentos duplicados encontrados
- PRD existe como whole.md E pasta prd/
- VOCÊ DEVE escolher qual versão usar
- Remova ou renomeie a outra versão para evitar confusão
```

#### Documentos Ausentes (AVISO)

Se documentos necessários não forem encontrados:

```
⚠️ AVISO: Documento necessário não encontrado
- Documento de arquitetura não encontrado
- Impactará a completude da avaliação
```

### 5. Adicionar Seção Inicial do Relatório

Inicialize {outputFile} com {templateFile}.

### 6. Apresentar Descobertas e Obter Confirmação

Exiba as descobertas e pergunte:
"**Descoberta de Documentos Completa**

[Mostrar lista de arquivos organizada]

**Problemas Encontrados:**

- [Listar quaisquer duplicatas exigindo resolução]
- [Listar quaisquer documentos ausentes]

**Ações Necessárias:**

- Se duplicatas existirem: Por favor, remova/renomeie uma versão
- Confirme quais documentos usar para avaliação

**Pronto para prosseguir?** [C] Continuar após resolver problemas"

### 7. Apresentar OPÇÕES DE MENU

Exibir: **Selecione uma Opção:** [C] Continuar para Validação de Arquivos

#### REGRAS DE EXECUÇÃO:

- SEMPRE pare e aguarde a entrada do usuário após apresentar o menu
- APENAS prossiga com a seleção 'C'
- Se duplicatas identificadas, insista na resolução primeiro
- O usuário pode esclarecer localizações de arquivos ou solicitar buscas adicionais

#### Lógica de Tratamento do Menu:

- SE C: Salve o inventário de documentos em {outputFile}, atualize o frontmatter com o passo concluído e arquivos sendo incluídos, e somente então carregue, leia completamente e execute {nextStepFile}
- SE Quaisquer outros comentários ou dúvidas: ajude o usuário a responder e então exiba o menu novamente

## NOTA CRÍTICA DE CONCLUSÃO DO PASSO

SOMENTE QUANDO C for selecionado e o inventário de documentos for salvo você carregará {nextStepFile} para iniciar a validação de arquivos.

---

## 🚨 MÉTRICAS DE SUCESSO/FALHA DO SISTEMA

### ✅ SUCESSO:

- Todos os tipos de documentos buscados sistematicamente
- Arquivos organizados e inventariados claramente
- Duplicatas identificadas e sinalizadas para resolução
- Usuário confirmou seleções de arquivos

### ❌ FALHA DO SISTEMA:

- Não buscar todos os tipos de documentos
- Ignorar conflitos de documentos duplicados
- Prosseguir sem resolver problemas críticos
- Não salvar inventário de documentos

**Regra Mestra:** Identificação clara de arquivos é essencial para uma avaliação precisa.
