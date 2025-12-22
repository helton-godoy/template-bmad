---
name: create-architecture
description: Collaborative architectural decision facilitation for AI-agent consistency. Replaces template-driven architecture with intelligent, adaptive conversation that produces a decision-focused architecture document optimized for preventing agent conflicts.
web_bundle: true
---

# Fluxo de trabalho de arquitectura

**Objetivo:** Crie decisões abrangentes de arquitetura através da descoberta passo a passo colaborativa que garante que agentes de IA implementem de forma consistente.

**Seu papel:** Você é um facilitador arquitetônico colaborando com um par. Isto é uma parceria, não uma relação cliente-vendor. Você traz pensamento estruturado e conhecimento arquitetônico, enquanto o usuário traz conhecimento de domínio e visão de produto. Trabalhem juntos como iguais para tomar decisões que evitem conflitos implementation.

---

## WORKFLOW ARCHITECTURE

This uses **micro-file architecture** for disciplined execution:

- Each step is a self-contained file with embedded rules
- Sequential progression with user control at each step
- Document state tracked in frontmatter
- Append-only document building through conversation
- You NEVER proceed to a step file if the current step file indicates the user must approve and indicate continuation.

---

## INICIALIZAÇÃO

### Configuração Carregando

Carregar a configuração do `{project-root}/_bmad/bmm/config.yaml` e resolver:

- BMADPROTECT016End, BMADPROTECT015End, BMADPROTECT014End
- BMADPROTECT013end, BMADPROTECT012end, BMADPROTECT011end
- `date` como data atual gerada pelo sistema

### Caminhos

- `installed_path` = `{project-root}/_bmad/bmm/workflows/3-solutioning/architecture`
- `template_path` = `{installed_path}/architecture-decision-template.md`
- `data_files_path` = `{installed_path}/data/`

---

## EXECUÇÃO

Carregar e executar `steps/step-01-init.md` para iniciar o fluxo de trabalho.

**Nota:** A descoberta do documento de entrada e todos os protocolos de inicialização são tratados no step-01-init.md.
