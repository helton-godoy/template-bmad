# Modo de Partido: Colaboração Multi-Agente

**Coloque todos os agentes de IA em uma conversa**

---

## What is Party Mode?

Ever wanted to gather your entire AI team in one room and see what happens? That's party mode.

Type `/bmad:core:workflows:party-mode` (or `*party-mode` from any agent), and suddenly you've got **all your AI agents** in one conversation. PM, Architect, DEV, UX Designer, the CIS creative agents - everyone shows up.

**Why it's useful:**

- **After complex workflows** - Debrief with the whole team about what worked, what didn't
- **Big decisions with tradeoffs** - Get technical, creative, and strategic perspectives simultaneously
- **Brainstorming sessions** - Watch ideas evolve through cross-pollination
- **When things go wrong** - Call out failures, watch agents defend their decisions, let them debate whose fault it was (oddly therapeutic)
- **Sprint retrospectives** - Party mode powers the retrospective workflow
- **Sprint planning** - Multi-agent collaboration for planning sessions

**Future use:** Advanced elicitation workflows will leverage party mode for sophisticated requirement gathering.

---

## Como funciona

**O básico:**

1. O modo de partido lê `_bmad/_config/agent-manifest.csv`
2. Carrega todos os agentes instalados (já inclui suas personalizações da instalação)
3. BMad Master orquestras - escolhe 2-3 agentes relevantes por mensagem com base no tópico
4. Os agentes respondem no caráter, podem concordar/discordar/construir as idéias uns dos outros
5. A discussão continua até você digitar "saída" ou chegar à conclusão natural

**É isso.** Sem fusão complexa, sem magia de corrida. Apenas agentes a falar.

---

## Quick Start

```bash

# Trigger party mode
/bmad:core:workflows:party-mode

# OR from any agent context
*party-mode

# During party
Ask questions, respond to agents, direct the conversation

# Exit
Type: exit

```

---

## Exemplos divertidos

### Exemplo 1: Chamando a má arquitetura

**Você:** "Ok time, nosso último sprint foi um desastre. O serviço de autenticação caiu três vezes. Quem estragou tudo?"

**Arquiteto (Winston):** "O projeto foi som - autenticação distribuída com retrocessos adequados. Se implementation desviou da especificação..."

**DEV (Amélia):** "Eu segui o documento de arquitetura exatamente. A especificação não explicava as condições de invalidação da sessão concorrente."

**PM (John):** "Ambos vocês perderam o problema maior - não validamos os requisitos de gerenciamento de sessão no PRD. A culpa é minha por não o apanhar."

**TEA (Murat):** "E eu deveria ter pego isso em testes de integração. Os cenários de teste não cobriram a invalidação concorrente."

*(Assistam ao debate de quem foi realmente a culpa - é terapêutica)*

---

### Example 2: Creative Brainstorming

**You:** "How do we make onboarding feel magical instead of boring?"

**UX Designer (Sally):** "Start with progressive disclosure - reveal features as users need them, not all at once in a tutorial."

**Storyteller (CIS):** "What if onboarding was a story? Each step reveals a character's journey - the user IS the hero."

**Innovation Strategist (CIS):** "Take it further - gamify with unlockable achievements. But make them meaningful, not arbitrary badges."

**Game Designer:** "Building on that - what if the first 'quest' is actually solving a real user problem? They learn by doing something valuable."

_(Ideas cross-pollinate and evolve)_

---

### Exemplo 3: Decisão técnica

**Você:** "Monolith ou microservices para MVP?"

**Arquiteto:** "Iniciar monólito. Microservices adicionar complexidade que você não precisa em 1000 usuários."

**PM:** "Acordo. Tempo de mercado importa mais do que escalabilidade teórica."

**DEV:** "Monolith com limites de módulo claros. Podemos extrair serviços mais tarde, se necessário."

**Estrategista de inovação:** "Tomar contraste - se o seu diferenciador é escalabilidade, construir para ele agora. Caso contrário, o Arquiteto tem razão."

*(Multiplas perspectivas revelam a resposta certa)*

---

## When NOT to Use Party Mode

**Skip party mode for:**

- Simple implementation questions → Use DEV agent
- Document review → Use Technical Writer
- Workflow status checks → Use any agent + `*workflow-status`
- Single-domain questions → Use specialist agent

**Use party mode for:**

- Multi-perspective decisions
- Creative collaboration
- Post-mortems and retrospectives
- Sprint planning sessions
- Complex problem-solving

---

## Personalização do agente

Modo partido usa agentes de `_bmad/[module]/agents/*.md` - estes já incluem quaisquer personalizações que você aplicado durante a instalação.

**Para personalizar agentes para o modo partido:**

1. Criar arquivo de personalização: `_bmad/_config/agents/bmm-pm.customize.yaml`
2. Execute `npx bmad-method install` para reconstruir agentes
3. Personalizações agora ativos no modo partido

Personalização de exemplo:

```yaml
agent:
  persona:
    principles:
      - 'HIPAA compliance is non-negotiable'
      - 'Patient safety over feature velocity'

```

Ver [Agents Guide](./agents-guide.md#agent-customization) para mais detalhes.

---

## Fluxos de trabalho BMM que utilizam o modo de partido

**Atual:**

- `epic-retrospe