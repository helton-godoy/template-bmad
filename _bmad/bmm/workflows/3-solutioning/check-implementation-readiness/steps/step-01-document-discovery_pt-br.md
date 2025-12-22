---
name: 'step-01-document-discovery'
description: 'Discover and inventory all project documents, handling duplicates and organizing file structure'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/3-solutioning/implementation-readiness'

# File References
thisStepFile: '{workflow_path}/steps/step-01-document-discovery.md'
nextStepFile: '{workflow_path}/steps/step-02-prd-analysis.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/implementation-readiness-report-{{date}}.md'
templateFile: '{workflow_path}/templates/readiness-report-template.md'
---

# Passo 1: Descoberta de documentos

## PASSO:

Descobrir, inventariar e organizar todos os documentos do projeto, identificar duplicatas e determinar quais versões usar para a avaliação.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um gerente de produto especialista e mestre Scrum
- ✅ Seu foco é encontrar organização e documentar o que existe
- ✅ Você identifica ambiguidades e pede esclarecimentos
- ✅ O sucesso é medido em inventário de arquivos claros e resolução de conflitos

### Regras específicas dos passos:

- 🎯 Foco apenas em encontrar e organizar arquivos
- 🚫 Não ler ou analisar o conteúdo do ficheiro
- 💬 Identificar claramente os documentos duplicados
- 🚪 Obter confirmação do usuário nas seleções de arquivos

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Procurar sistematicamente todos os tipos de documentos
- 💾
- 📖 Cópias da bandeira para resolução do usuário
- 🚫 PROJECTO de proceder com duplicados não resolvidos

## PROCESSO DE DESCOBERÇÃO DO DOCUMENTO:

### 1. Inicializar a Descoberta de Documentos

"Começando **Document Discovery** para inventariar todos os arquivos do projeto.

Eu vou.

1. Procure todos os documentos necessários (PRD, Arquitetura, Epics, UX)
2. Agrupar documentos em conjunto
3. Identifique quaisquer duplicatas (versão inteira + em fragmentos)
4. Apresentar conclusões para a sua confirmação"

### 2. Padrões de pesquisa de documentos

Procurar por cada tipo de documento usando estes padrões:

#### Documentos PRD
BMADPROTECT026end BMADPROTECT013end
- Sharded: `{output_folder}/*prd*/index.md` e arquivos relacionados

#### B. Documentos de arquitectura
BMADPROTECT024end BMADPROTECT011end
- Sharded: `{output_folder}/*architecture*/index.md` e arquivos relacionados

#### C. Documentos Épicos e Histórias
BMADPROTECT022end BMADPROTECT009end
- Sharded: `{output_folder}/*epic*/index.md` e arquivos relacionados

#### D. UX Design Documents
BMADPROTECT020end BMADPROTECT007end
- Sharded: `{output_folder}/*ux*/index.md` e arquivos relacionados

### 3. Organizar conclusões

Para cada tipo de documento encontrado:

```

## [Document Type] Files Found

**Whole Documents:**
- [filename.md] ([size], [modified date])

**Sharded Documents:**
- Folder: [foldername]/
  - index.md
  - [other files in folder]

```

### 4. Identificar questões críticas

#### Duplicados (críticos)

Se existirem versões inteiras e em pedaços:

```
⚠️ CRITICAL ISSUE: Duplicate document formats found
- PRD exists as both whole.md AND prd/ folder
- YOU MUST choose which version to use
- Remove or rename the other version to avoid confusion

```

#### Documentos em falta

Se os documentos exigidos não forem encontrados:

```
⚠️ WARNING: Required document not found
- Architecture document not found
- Will impact assessment completeness

```

### 5. Adicionar Secção do Relatório Inicial

Inicializar {outputFile} com {templateFile}.

### 6. Apresentar conclusões e obter confirmação

Mostrar as descobertas e perguntar:
**Document Discovery Complete**

[Mostrar lista de arquivos organizada]

**Issues Found:**

- [Lista de duplicatas que exigem resolução]
- [Lista de documentos em falta]

**Acções necessárias:**

- Se existirem duplicatas: Por favor, remova/ renomeie uma versão
- Confirmar que documentos devem ser utilizados para avaliação

**Prontos para prosseguir?** [C] Continuar depois de resolver problemas"

### 7.

Mostrar: **Selecionar uma Opção:** [C] Continuar a Validação de Ficheiros

#### REGRAS DE execução:

- SEMPRE parar e esperar pela entrada do usuário após apresentar o menu
- APENAS prossiga com a seleção "C"
- Se forem identificadas duplicatas, insista na resolução
- O usuário pode esclarecer locais de arquivo ou solicitar pesquisas adicionais

#### Logic de manipulação do menu:

- SE C: Salvar o inventário do documento para {outputFile}, atualizar a matéria frontal com etapa completa e arquivos sendo incluídos, e só então carregar ler completamente e executar {nextStepFile}
- SE Quaisquer outros comentários ou consultas: ajudar o usuário a responder ao menu replay

## NOTA DE ENSAIO CRÍTICO

APENAS QUANDO C é selecionado e o inventário do documento é salvo você carregará {nextStepFile} para iniciar a validação do arquivo.

---

## 🚨

### ✅ SUCESSO:

- Todos os tipos de documentos pesquisados sistematicamente
- Arquivos organizados e inventariados claramente
- Duplicados identificados e marcados para resolução
- Seleções de arquivos confirmadas pelo usuário

### ❌

- Não procurar.