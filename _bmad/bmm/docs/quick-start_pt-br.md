# Método BMad V6 Guia de Início Rápido

Comece com o BMad Method v6 para o seu novo projeto greenfield. Este guia orienta você através de software de construção do zero usando fluxos de trabalho alimentados por IA.

## TL;DR - O Caminho Rápido

1. **Instalar**: `npx bmad-method@alpha install`
2. **Inicializar**: Carregar agente analista → Executar "workflow-init"
3. **Plano**: Carregar agente PM → Executar "prd" (ou "tech-spec" para pequenos projetos)
4. **Arquiteto**: Carregar Arquiteto → Executar "criar-arquitetura" (10+ histórias somente)
5. **Construir**: Carregar agente SM → Executar fluxos de trabalho para cada história → Carregar agente DEV → Implementar
6. **Sempre use chats frescos** para cada fluxo de trabalho para evitar alucinações

---

## What is BMad Method?

BMad Method (BMM) helps you build software through guided workflows with specialized AI agents. The process follows four phases:

1. **Phase 1: Analysis** (Optional) - Brainstorming, Research, Product Brief
2. **Phase 2: Planning** (Required) - Create your requirements (tech-spec or PRD)
3. **Phase 3: Solutioning** (Track-dependent) - Design the architecture for BMad Method and Enterprise tracks
4. **Phase 4: Implementation** (Required) - Build your software Epic by Epic, Story by Story

### Complete Workflow Visualization

![BMad Method Workflow - Standard Greenfield](./images/workflow-method-greenfield.svg)

_Complete visual flowchart showing all phases, workflows, agents (color-coded), and decision points for the BMad Method standard greenfield track. Each box is color-coded by the agent responsible for that workflow._

## Installation

```bash

# Install v6 Alpha to your project
npx bmad-method@alpha install

```

The interactive installer will guide you through setup and create a `_bmad/` folder with all agents and workflows.

---

## Começando

### Passo 1: Inicializar seu fluxo de trabalho

1. **Carregue o agente analista** no seu IDE - Veja as instruções específicas do seu IDE em [docs/ide-info](https://github.com/bmad-code-org/BMAD-METHOD/tree/main/docs/ide-info) for how to activate agents:
   - [Claude Code](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/ide-info/claude-code.md)
   - [VS Code/Cursor/Windsurf](https://github.com/bmad-code-org/BMAD-METHOD/tree/main/docs/ide-info) - Check your IDE folder
   - Other IDEs also supported
2. **Wait for the agent's menu** to appear
3. **Tell the agent**: "Run workflow-init" or type "\*workflow-init" or select the menu item number

#### What happens during workflow-init?

Workflows are interactive processes in V6 that replaced tasks and templates from prior versions. There are many types of workflows, and you can even create your own with the BMad Builder module. For the BMad Method, you'll be interacting with expert-designed workflows crafted to work with you to get the best out of both you and the LLM.

During workflow-init, you'll describe:

- Your project and its goals
- Whether there's an existing codebase or this is a new project
- The general size and complexity (you can adjust this later)

#### Planning Faixas

Com base em sua descrição, o fluxo de trabalho irá sugerir uma faixa e let você escolher entre:

**Três faixas Planning:**

- **Quick Flow** - Fast implementation (apenas tecnologia específica) - correções de erros, características simples, escopo claro (tipicamente 1-15 histórias)
- **Método BMad** - planning (PRD + Arquitetura + UX) - produtos, plataformas, características complexas (normalmente 10-50+ histórias)
- **Método empresarial** - planning (Método BMad + Segurança/DevOps/Teste) - requisitos empresariais, conformidade, multi-atendimento (tipicamente mais de 30 andares)

**Nota**: Contagem de histórias são orientações, não definições. As faixas são escolhidas com base nas necessidades do planning, não na matemática da história.

#### O que é criado?

Uma vez que você confirme sua faixa, o arquivo `bmm-workflow-status.yaml` será criado na pasta de documentos do seu projeto (assumindo o local de instalação padrão). Este arquivo rastreia seu progresso em todas as fases.

**Notas importantes:**

- Cada faixa tem caminhos diferentes através das fases
- Contagem de histórias ainda pode mudar com base na complexidade global como você trabalha
- Para este guia, vamos assumir um projecto BMad Method
- Este fluxo de trabalho irá guiá-lo através da Fase 1 (opcional), Fase 2 (obrigatória) e Fase 3 (obrigatório para o método BMad e faixas Enterprise)

### Passo 2: Trabalhar através das Fases 1-3

Após o início do fluxo de trabalho terminar, você trabalhará nas fases planning. **Importante: Use chats frescos para cada fluxo de trabalho para evitar limitações de contexto.**

#### A verificar o seu estado

Se não sabe o que fazer a seguir:

1. Carregar qualquer agente em um novo chat
2. Peça "status de fluxo de trabalho"
3. O agente lhe dirá o próximo fluxo de trabalho recomendado ou necessário

**Exemplo de resposta:**

```
Phase 1 (Analysis) is entirely optional. All workflows are optional or recommended:
  - brainstorm-project - optional
  - research - optional
  - product-brief - RECOMMENDED (but not required)

The next TRULY REQUIRED step is:
  - PRD (Product Requirements Document) in Phase 2 - Planning
  - Agent: pm
  - Command: prd

```

#### Como executar fluxos de trabalho nas fases 1-3

Quando um agente lhe diz para correr