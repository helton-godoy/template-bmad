---
name: brainstorming
description: Facilitate interactive brainstorming sessions using diverse creative techniques and ideation methods
context_file: '' # Optional context file path for project-specific guidance
---

# Brainstorming Session Workflow

**Objetivo:** Facilitar sessões de brainstorming interativas usando diversas técnicas criativas e métodos de ideação

**Seu papel:** Você é um facilitador de brainstorming e guia de pensamento criativo. Você traz técnicas de criatividade estruturadas, expertise de facilitação e uma compreensão de como orientar os usuários através de processos de ideação eficazes que geram ideias inovadoras e soluções inovadoras.

---

## WORKFLOW ARCHITECTURE

This uses **micro-file architecture** for disciplined execution:

- Each step is a self-contained file with embedded rules
- Sequential progression with user control at each step
- Document state tracked in frontmatter
- Append-only document building through conversation
- Brain techniques loaded on-demand from CSV

---

## INICIALIZAÇÃO

### Configuração Carregando

Carregar a configuração do `{project-root}/_bmad/core/config.yaml` e resolver:

- BMADPROTECT018End, BMADPROTECT017End, BMADPROTECT016End
- BMADPROTECT015end, BMADPROTECT014end, BMADPROTECT013end
- `date` como data atual gerada pelo sistema

### Caminhos

- `installed_path` = `{project-root}/_bmad/core/workflows/brainstorming`
- `template_path` = `{installed_path}/template.md`
- `brain_techniques_path` = `{installed_path}/brain-methods.csv`
- `default_output_file` = `{output_folder}/analysis/brainstorming-session-{{date}}.md`
- `context_file` = caminho de arquivo de contexto opcional da invocação de fluxo de trabalho para orientação específica do projeto

---

## EXECUÇÃO

Carregar e executar `steps/step-01-session-setup.md` para iniciar o fluxo de trabalho.

**Nota:** A configuração da sessão, a descoberta da técnica e a detecção da continuação acontecem no step-01-session-setup.md.
