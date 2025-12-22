# Normas de documentação técnica para BMAD

**Para agente: escritor técnico**
**Composto: Referência concisa para criação e revisão de documentação**

---

## CRITICAL RULES

### Rule 1: CommonMark Strict Compliance

ALL documentation MUST follow CommonMark specification exactly. No exceptions.

### Rule 2: NO TIME ESTIMATES

NEVER document time estimates, durations, or completion times for any workflow, task, or activity. This includes:

- Workflow execution time (e.g., "30-60 min", "2-8 hours")
- Task duration estimates
- Reading time estimates
- Implementation time ranges
- Any temporal measurements

Time varies dramatically based on:

- Project complexity
- Team experience
- Tooling and environment
- Context switching
- Unforeseen blockers

**Instead:** Focus on workflow steps, dependencies, and outputs. Let users determine their own timelines.

### CommonMark Essentials

**Headers:**

- Use ATX-style ONLY: `#` `##` `###` (NOT Setext underlines)
- Single space after `#`: `# Title` (NOT `#Title`)
- No trailing `#`: `# Title` (NOT `# Title #`)
- Hierarchical order: Don't skip levels (h1→h2→h3, not h1→h3)

**Code Blocks:**

- Use fenced blocks with language identifier:
  ````markdown
  ```javascript
  const example = 'code';
  ```
  ````
- NOT indented code blocks (ambiguous)

**Lists:**

- Consistent markers within list: all `-` or all `*` or all `+` (don't mix)
- Proper indentation for nested items (2 or 4 spaces, stay consistent)
- Blank line before/after list for clarity

**Links:**

- Inline: `[text](url)`
- Reference: `[text][ref]` then `[ref]: url` at bottom
- NO bare URLs without `<>` brackets

**Emphasis:**

- Italic: `*text*` or `_text_`
- Bold: `**text**` or `__text__`
- Consistent style within document

**Line Breaks:**

- Two spaces at end of line + newline, OR
- Blank line between paragraphs
- NO single line breaks (they're ignored)

---

## Diagramas Sereias: Sintaxe Válida Requerida

**Regras críticas:**

1. Sempre especificar diagrama tipo primeira linha
2. Use a sintaxe válida da Sereia v10+
3. Teste sintaxe antes de saída (validação mental)
4. Mantenha o foco: 5-10 nós ideal, max 15

**Selecção do Tipo de Diagrama:**

- **Flowchart** - Fluxos de processo, árvores de decisão, fluxos de trabalho
- **sequenceDiagram** - Interações API, fluxos de mensagens, processos baseados no tempo
- **classDiagram** - Modelos de objectos, relações de classes, estrutura do sistema
- **erDiagram** - Esquemas de banco de dados, relações de entidade
- **StateDiagram-v2** - Máquinas estatais, ciclo de vida
- **gitGraph** - Estratégias de ramo, fluxos de controle de versão

**Formatação:**

BMADPROTECT004
fluxograma TD
Iniciar[Limpar etiqueta] --> Decisão{Question?}
Decisão -- > Sim! Ação 1 [Fazer isso]
Decisão -- > No2 Ação[Fazer isso]

```
```»

---

## Style Guide Principles (Distilled)

Apply in this hierarchy:

1. **Project-specific guide** (if exists) - always ask first
2. **BMAD conventions** (this document)
3. **Google Developer Docs style** (defaults below)
4. **CommonMark spec** (when in doubt)

### Core Writing Rules

**Task-Oriented Focus:**

- Write for user GOALS, not feature lists
- Start with WHY, then HOW
- Every doc answers: "What can I accomplish?"

**Clarity Principles:**

- Active voice: "Click the button" NOT "The button should be clicked"
- Present tense: "The function returns" NOT "The function will return"
- Direct language: "Use X for Y" NOT "X can be used for Y"
- Second person: "You configure" NOT "Users configure" or "One configures"

**Structure:**

- One idea per sentence
- One topic per paragraph
- Headings describe content accurately
- Examples follow explanations

**Accessibility:**

- Descriptive link text: "See the API reference" NOT "Click here"
- Alt text for diagrams: Describe what it shows
- Semantic heading hierarchy (don't skip levels)
- Tables have headers
- Emojis are acceptable if user preferences allow (modern accessibility tools support emojis well)

---

## Documentação OpenAPI/API

**Elementos Obrigatórios:**

- Endpoint caminho e método
- Requisitos de autenticação
- Parâmetros de solicitação (caminho, consulta, corpo) com tipos
- Pedido de exemplo (realista, trabalhando)
- Esquema de resposta com tipos
- Exemplos de resposta (sucesso + erros comuns)
- Códigos de erro e significados

**Padrões de qualidade:**

- Compliance de especificação OpenAPI 3.0+
- Esquemas completos (sem campos em falta)
- Exemplos que realmente funcionam
- Limpar mensagens de erro
- Sistemas de segurança documentados

---

## Tipos de documentação: Referência Rápida

**REDME:**

- O que (overview), Porquê (propósito), Como (início rápido)
- Instalação, Uso, Contribuir, Licença
- Sob 500 linhas (link para documentos detalhados)

**Referência API:**

- Cobertura final completa
- Exemplos de pedido/resposta
- Detalhes da autenticação
- Tratamento de erros
- Limites de taxa, se aplicável

**Guia do utilizador:**

- Seções baseadas em tarefas (Como ...)
- Instruções passo a passo
- Imagens/diagramas onde útil
- Secção de resolução de problemas

**Docs de arquitetura:**

- Diagrama de visão geral do sistema (Mermaid)
- Descrições de componentes
- Fluxo de dados
- Decisões tecnológicas (