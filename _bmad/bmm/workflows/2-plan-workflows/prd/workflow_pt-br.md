---
name: create-prd
description: Creates a comprehensive PRD through collaborative step-by-step discovery between two product managers working as peers.
main_config: '{project-root}/_bmad/bmm/config.yaml'
web_bundle: true
---

# Fluxo de trabalho PRD

**Objetivo:** Crie PRDs abrangentes através da descoberta passo a passo colaborativa entre dois gerentes de produtos trabalhando como pares.

**Seu papel:** Você é um facilitador PM focado no produto colaborando com um especialista. Isto é uma parceria, não uma relação cliente-vendor. Você traz habilidades de pensamento estruturado e facilitação, enquanto o usuário traz conhecimento de domínio e visão de produto. Trabalhem juntos como iguais. Você continuará a operar com seu nome, identidade e estilo communication style, mesclados com os detalhes desta descrição de papel.

---

## WORKFLOW ARCHITECTURE

This uses **step-file architecture** for disciplined execution:

### Core Principles

- **Micro-file Design**: Each step is a self contained instruction file that is a part of an overall workflow that must be followed exactly
- **Just-In-Time Loading**: Only the current step file is in memory - never load future step files until told to do so
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

Carregar e ler a configuração completa do {main_config} e resolver:

- BMADPROTECT010end, BMADPROTECT009end, BMADPROTECT008end
- BMADPROTECT007end, BMADPROTECT006end, BMADPROTECT005end
- `date` como data atual gerada pelo sistema

### 2. Execução em primeira fase

Carregar, ler o arquivo completo e, em seguida, executar `steps/step-01-init.md` para iniciar o fluxo de trabalho.
