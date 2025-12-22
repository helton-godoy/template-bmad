---
name: generate-project-context
description: Creates a concise project-context.md file with critical rules and patterns that AI agents must follow when implementing code. Optimized for LLM context efficiency.
---

# Gerar fluxo de trabalho de contexto do projeto

**Objetivo:** Crie um arquivo `project-context.md` conciso e otimizado contendo regras, padrões e diretrizes críticas que os agentes de IA devem seguir ao implementar o código. Este arquivo se concentra em detalhes não óbvios que LLMs precisam ser lembrados.

**Seu papel:** Você é um facilitador técnico trabalhando com um par para capturar as regras essenciais do implementation que garantirão uma geração de código consistente e de alta qualidade em todos os agentes de IA que trabalham no projeto.

---

## WORKFLOW ARCHITECTURE

This uses **micro-file architecture** for disciplined execution:

- Each step is a self-contained file with embedded rules
- Sequential progression with user control at each step
- Document state tracked in frontmatter
- Focus on lean, LLM-optimized content generation
- You NEVER proceed to a step file if the current step file indicates the user must approve and indicate continuation.

---

## INICIALIZAÇÃO

### Configuração Carregando

Carregar a configuração do `{project-root}/_bmad/bmm/config.yaml` e resolver:

- BMADPROTECT016End, BMADPROTECT015End, BMADPROTECT014End
- BMADPROTECT013end, BMADPROTECT012end, BMADPROTECT011end
- `date` como data atual gerada pelo sistema

### Caminhos

- `installed_path` = `{project-root}/_bmad/bmm/workflows/generate-project-context`
- `template_path` = `{installed_path}/project-context-template.md`
- `output_file` = `{output_folder}/project-context.md`

---

## EXECUÇÃO

Carregar e executar `steps/step-01-discover.md` para iniciar o fluxo de trabalho.

**Nota:** Os protocolos de descoberta e inicialização de documentos de entrada são tratados no step-01-discover.md.
