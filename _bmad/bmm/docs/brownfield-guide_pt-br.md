# BMad Method Brownfield Development Guide

**Guia completo para trabalhar com bases de código existentes**

**Tempo de leitura:** ~35 minutos

---

## Quick Navigation

**Jump to:**

- [Quick Reference](#quick-reference) - Commands and files
- [Common Scenarios](#common-scenarios) - Real-world examples
- [Best Practices](#best-practices) - Success tips

---

O que é o Brownfield Development?

Os projectos Brownfield envolvem trabalhar nas bases de códigos existentes em vez de começar de novo:

- **Correcções de bugs** - Alterações de ficheiros individuais
- **Pequenos recursos** - Adicionar aos módulos existentes
- **Feature sets** - Vários recursos relacionados
- **Integrações principais** - Adições arquitectónicas complexas
- **Expansões de sistemas** - Melhorias em escala empresarial

**Diferença-chave de Greenfield:** Você deve entender e respeitar os padrões, arquitetura e restrições existentes.

**Core Principle:** Os agentes de IA precisam de documentação abrangente para entender o código existente antes que possam efetivamente planejar ou implementar mudanças.

---

## Getting Started

### Understanding Planning Tracks

For complete track details, see [Scale Adaptive System](./scale-adaptive-system.md).

**Brownfield tracks at a glance:**

| Track                 | Scope                      | Typical Stories | Key Difference                                  |
| --------------------- | -------------------------- | --------------- | ----------------------------------------------- |
| **Quick Flow**        | Bug fixes, small features  | 1-15            | Must understand affected code and patterns      |
| **BMad Method**       | Feature sets, integrations | 10-50+          | Integrate with existing architecture            |
| **Enterprise Method** | Enterprise expansions      | 30+             | Full system documentation + compliance required |

**Note:** Story counts are guidance, not definitions. Tracks are chosen based on planning needs.

### Track Selection for Brownfield

When you run `workflow-init`, it handles brownfield intelligently:

**Step 1: Shows what it found**

- Old planning docs (PRD, epics, stories)
- Existing codebase

**Step 2: Asks about YOUR work**

> "Are these works in progress, previous effort, or proposed work?"

- **(a) Works in progress** → Uses artifacts to determine level
- **(b) Previous effort** → Asks you to describe NEW work
- **(c) Proposed work** → Uses artifacts as guidance
- **(d) None of these** → You explain your work

**Step 3: Analyzes your description**

- Keywords: "fix", "bug" → Quick Flow, "dashboard", "platform" → BMad Method, "enterprise", "multi-tenant" → Enterprise Method
- Complexity assessment
- Confirms suggested track with you

**Key Principle:** System asks about YOUR current work first, uses old artifacts as context only.

**Example: Old Complex PRD, New Simple Work**

```
System: "Found PRD.md (BMad Method track, 30 stories, 6 months old)"
System: "Is this work in progress or previous effort?"
You: "Previous effort - I'm just fixing a bug now"
System: "Tell me about your current work"
You: "Update payment method enums"
System: "Quick Flow track (tech-spec approach). Correct?"
You: "Yes"
✅ Creates Quick Flow workflow

```

---

## Documentação: Primeiro passo crítico

🚨 **Para os projectos brownfield: Certifique-se sempre de documentação adequada de uso de IA antes de planning**

### Recomendação Predefinida: Executar o projeto-documento

**Melhor prática:**Execute o fluxo de trabalho `document-project` a menos que você tenha**documentação confirmada, confiável e otimizada por IA**.

### Por que o projeto de documento é quase sempre a escolha certa

Documentação existente muitas vezes tem problemas de qualidade que quebram fluxos de trabalho de IA:

**Problemas comuns:**

- **Muita Informação (TMI):** Ficheiros de marcação maciça com 10s ou 100s de secções de nível 2
- **Fora de Data:** A documentação não foi atualizada com alterações recentes de código
- **Formato errado:** Escrito para seres humanos, não agentes de IA (falta de estrutura, índice, padrões claros)
- **Cobertura incompleta:** Falta arquitetura crítica, padrões ou informações de configuração
- **Qualidade inconsistente:** Algumas áreas estão bem documentadas, outras não.

**Impacto em agentes de IA:**

- Agentes de IA atingiram limites de token lendo arquivos enormes
- Documentos ultrapassados causam alucinações (o agente pensa que os padrões antigos ainda se aplicam)
- Estrutura em falta significa que os agentes não conseguem encontrar informações relevantes
- Cobertura incompleta leva a suposições incorretas

### Árvore de decisão da documentação

**Passo 1: Avaliar a qualidade da documentação existente**

Pergunte a si mesmo:

- ✅ É **atual** (atualizado nos últimos 30 dias)?
- ✅ É **AI-optimizado** (estruturado com index.md, secções claras, <500 lines per file)?
- ✅ Is it **comprehensive** (architecture, patterns, setup all documented)?
- ✅ Do you **trust** it completely for AI agent consumption?

**If ANY answer is NO → Run `document-project`**

**Step 2: Check for Massive Documents**

If you have documentation but files are huge (>500 linhas, 10+ secções de nível 2):

1. **Primeiro:** Executar `shard-doc` ferramenta para dividir arquivos grandes:

«```bash

# Carregar BMad Master ou qualquer agente
_bmad/core/tools/shard-doc.xml