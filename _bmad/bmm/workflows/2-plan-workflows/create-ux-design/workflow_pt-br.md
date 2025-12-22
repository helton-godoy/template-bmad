---
name: create-ux-design
description: Work with a peer UX Design expert to plan your applications UX patterns, look and feel.
web_bundle: true
---

# Criar fluxo de trabalho de design UX

**Objetivo:** Crie especificações abrangentes de design de UX através de exploração visual colaborativa e tomada de decisão informada onde você atua como um facilitador de UX trabalhando com um stakeholder de produto.

---

## WORKFLOW ARCHITECTURE

This uses **micro-file architecture** for disciplined execution:

- Each step is a self-contained file with embedded rules
- Sequential progression with user control at each step
- Document state tracked in frontmatter
- Append-only document building through conversation

---

## INICIALIZAÇÃO

### Configuração Carregando

Carregar a configuração do `{project-root}/_bmad/bmm/config.yaml` e resolver:

- BMADPROTECT031end, BMADPROTECT030end, BMADPROTECT029end
- BMADPROTECT028End, BMADPROTECT027End, BMADPROTECT026End
- `date` como data atual gerada pelo sistema

### Caminhos

- `installed_path` = `{project-root}/_bmad/bmm/workflows/2-plan-workflows/create-ux-design`
- `template_path` = `{installed_path}/ux-design-template.md`
- `default_output_file` = `{output_folder}/ux-design-specification.md`

### Ficheiros de Saída

- Temas de cores: `{output_folder}/ux-color-themes.html`
- Direcção de projecto: `{output_folder}/ux-design-directions.html`

### Descoberta do documento de entrada

Descubra documentos de contexto para o contexto UX (Prioridade: pasta de análise primeiro, em seguida, pasta principal, em seguida, sharded):

- PRD: `{output_folder}/analysis/*prd*.md` ou `{output_folder}/*prd*.md` ou `{output_folder}/*prd*/**/*.md`
- Resumo do produto: `{output_folder}/analysis/*brief*.md` ou `{output_folder}/*brief*.md` ou `{output_folder}/*brief*/**/*.md`
- Epics: `{output_folder}/analysis/*epic*.md` ou `{output_folder}/*epic*.md` ou `{output_folder}/*epic*/**/*.md`
- Research: `{output_folder}/analysis/research/*research*.md` ou `{output_folder}/*research*.md` ou `{output_folder}/*research*/**/*.md`
- Brainstorming: `{output_folder}/analysis/brainstorming/*brainstorming*.md` ou `{output_folder}/*brainstorming*.md`

---

## EXECUÇÃO

Carregar e executar o `steps/step-01-init.md` para iniciar o fluxo de trabalho de design UX.
