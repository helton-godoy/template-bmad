# BMM Perguntas Frequentes

Respostas rápidas a perguntas comuns sobre o Módulo Método BMad.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Choosing the Right Level](#choosing-the-right-level)
- [Workflows and Phases](#workflows-and-phases)
- [Planning Documents](#planning-documents)
- [Implementation](#implementation)
- [Brownfield Development](#brownfield-development)
- [Tools and Technical](#tools-and-technical)

---

## Começando

### Q: Eu sempre preciso executar o início do fluxo de trabalho?

**A:** Não, uma vez que você aprende o fluxo você pode ir diretamente para fluxos de trabalho. No entanto, o início do fluxo de trabalho é útil porque:

- Determina automaticamente o nível adequado do seu projecto
- Cria o arquivo de status de rastreamento
- Leva- o ao fluxo de trabalho inicial correcto

Para usuários experientes: use o [Quick Reference](./quick-start.md#quick-reference-agent-document-mapping) para ir diretamente para o agente certo / fluxo de trabalho.

### P: Por que preciso de bate-papos novos para cada fluxo de trabalho?

**A:** Fluxos de trabalho intensivos em contexto (como brainstorming, criação de PRD, design de arquitetura) podem causar alucinações de IA se forem executados em sequência dentro do mesmo chat. Começar de novo garante que o agente tem capacidade de contexto máxima para cada fluxo de trabalho. Isto é particularmente importante para:

- Fluxos de trabalho Planning (PRD, arquitetura)
- Análise de fluxos de trabalho (brainstorming, pesquisa)
- História complexa implementation

Fluxos de trabalho rápidos como verificações de status podem reutilizar chats com segurança.

### Q: Posso pular o status do fluxo de trabalho e começar a trabalhar?

**A:** Sim, se você já conhece o seu nível de projeto e que fluxo de trabalho vem em seguida. O estado do fluxo de trabalho é principalmente útil para:

- Novos projetos (orienta a configuração inicial)
- Quando não sabes o que fazer a seguir.
- Depois de pausas no trabalho (lembra onde você parou)
- Verificação dos progressos globais

### P: Qual é o mínimo que preciso para começar?

**A:** Para o caminho mais rápido:

1. Método de instalação BMad: `npx bmad-method@alpha install`
2. Para pequenas mudanças: Carregar agente PM → executar tech-spec → implementar
3. Para projetos maiores: Carregar agente PM → executar prd → arquiteto → implementar

### P: Como sei se estou na Fase 1, 2, 3 ou 4?

**A:** Verifique o seu arquivo `bmm-workflow-status.md` (criado pelo workflow-init). Mostra a fase atual e o progresso. Se você não tem este arquivo, você também pode dizer pelo que você está trabalhando:

- **Fase 1** - Brainstorming, pesquisa, resumo do produto (opcional)
- **Fase 2** - Criação de um PRD ou de um tech-spec (sempre necessário)
- **Fase 3** - Design de arquitectura (apenas nível 2-4)
- **Fase 4** - Na verdade, escrever código, implementar histórias

---

## Choosing the Right Level

### Q: How do I know which level my project is?

**A:** Use workflow-init for automatic detection, or self-assess using these keywords:

- **Level 0:** "fix", "bug", "typo", "small change", "patch" → 1 story
- **Level 1:** "simple", "basic", "small feature", "add" → 2-10 stories
- **Level 2:** "dashboard", "several features", "admin panel" → 5-15 stories
- **Level 3:** "platform", "integration", "complex", "system" → 12-40 stories
- **Level 4:** "enterprise", "multi-tenant", "multiple products" → 40+ stories

When in doubt, start smaller. You can always run create-prd later if needed.

### Q: Can I change levels mid-project?

**A:** Yes! If you started at Level 1 but realize it's Level 2, you can run create-prd to add proper planning docs. The system is flexible - your initial level choice isn't permanent.

### Q: What if workflow-init suggests the wrong level?

**A:** You can override it! workflow-init suggests a level but always asks for confirmation. If you disagree, just say so and choose the level you think is appropriate. Trust your judgment.

### Q: Do I always need architecture for Level 2?

**A:**No, architecture is**optional** for Level 2. Only create architecture if you need system-level design. Many Level 2 projects work fine with just PRD created during planning.

### Q: What's the difference between Level 1 and Level 2?

**A:**

- **Level 1:** 1-10 stories, uses tech-spec (simpler, faster), no architecture
- **Level 2:** 5-15 stories, uses PRD (product-focused), optional architecture

The overlap (5-10 stories) is intentional. Choose based on:

- Need product-level planning? → Level 2
- Just need technical plan? → Level 1
- Multiple epics? → Level 2
- Single epic? → Level 1

---

## Fluxos de trabalho e fases

### Q: Qual é a diferença entre workflow-status e workflow-init?

**A:**

- **Estatuto do fluxo de trabalho:** Verifica o estado existente e diz-lhe o que se segue (usar ao continuar o trabalho)
- **Início de fluxo de trabalho:** Cria um novo ficheiro de estado e configura o projecto (utilizar ao iniciar o novo projecto)

Se o ficheiro de estado existir, use o estado do fluxo de trabalho. Caso contrário, use o início do fluxo de trabalho.

### P: Posso pular a Fase 1 (Análise)?

**A:** Sim! A fase 1 é opcional para todos os níveis, embora recomendada para projetos complexos. Ignorar se:

- Os requisitos são claros.
- Não há necessidade de pesquisa.
- Trabalho sensível ao tempo
- Pequenas alterações (Nível 0-1)

### P: Quando é necessária a Fase 3 (Arquitectura)?

**A:**

- **Nível 0-1:** Nunca (ski)