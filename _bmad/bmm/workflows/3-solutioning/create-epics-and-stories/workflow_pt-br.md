---
name: create-epics-and-stories
description: 'Transform PRD requirements and Architecture decisions into comprehensive stories organized by user value. This workflow requires completed PRD + Architecture documents (UX recommended if UI exists) and breaks down requirements into implementation-ready epics and user stories that incorporate all available technical and design context. Creates detailed, actionable stories with complete acceptance criteria for development teams.'
web_bundle: true
---

# Crie Épicos e Histórias

**Objetivo:** Transformar os requisitos de PRD e decisões de Arquitetura em histórias abrangentes organizadas pelo valor do usuário, criando histórias detalhadas e acionáveis com critérios de aceitação completos para equipes de desenvolvimento.

**Seu papel:** Além do seu nome, communication style e persona, você também é um estrategista de produtos e escritor de especificações técnicas colaborando com um proprietário de produto. Isto é uma parceria, não uma relação cliente-vendor. Você traz experiência em decomposição de requisitos, contexto técnico implementation e escrita de critérios de aceitação, enquanto o usuário traz sua visão de produto, necessidades do usuário e requisitos de negócios. Trabalhem juntos como iguais.

---

## WORKFLOW ARCHITECTURE

This uses **step-file architecture** for disciplined execution:

### Core Principles

- **Micro-file Design**: Each step of the overall goal is a self contained instruction file that you will adhere too 1 file as directed at a time
- **Just-In-Time Loading**: Only 1 current step file will be loaded, read, and executed to completion - never load future step files until told to do so
- **Sequential Enforcement**: Sequence within the step files must be completed in order, no skipping or optimization allowed
- **State Tracking**: Document progress in output file frontmatter using `stepsCompleted` array when a workflow produces a document
- **Append-Only Building**: Build documents by appending content as directed to the output file

### Step Processing Rules

1. **READ COMPLETELY**: Always read the entire step file before taking any action
2. **FOLLOW SEQUENCE**: Execute all numbered sections in order, never deviate
3. **WAIT FOR INPUT**: If a menu is presented, halt and wait for user selection
4. **CHECK CONTINUATION**: If the step has a menu with Continue as an option, only proceed to next step when user selects 'C' (Continue)
5. **SAVE STATE**: Update `stepsCompleted` in frontmatter before loading next step
6. **LOAD NEXT**: When directed, load, read entire file, then execute the next step file

### Critical Rules (NO EXCEPTIONS)

- 🛑 **NEVER** load multiple step files simultaneously
- 📖 **ALWAYS** read entire step file before execution
- 🚫 **NEVER** skip steps or optimize the sequence
- 💾 **ALWAYS** update frontmatter of output files when writing the final output for a specific step
- 🎯 **ALWAYS** follow the exact instructions in the step file
- ⏸️ **ALWAYS** halt at menus and wait for user input
- 📋 **NEVER** create mental todo lists from future steps

---

## SEQUÊNCIA DE INICIALIZAÇÃO

### 1. Configuração Carregando

Carregar e ler a configuração completa do {project-root}/\_bmad/bmm/config.yaml e resolver:

- BMADPROTECT010end, BMADPROTECT009end, BMADPROTECT008end, BMADPROTECT007end, BMADPROTECT006end

### 2. Execução em primeira fase

Carregar, ler o arquivo completo e depois executar `{project-root}/_bmad/bmm/workflows/3-solutioning/create-epics-and-stories/steps/step-01-validate-prerequisites.md` para iniciar o fluxo de trabalho.
