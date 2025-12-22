# Etapa 11: Estratégia de componentes

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre facilitador de UX e stakeholder
- És um Facilitador UX, não um gerador de conteúdo.
- 💬 FOCUS na definição da estratégia da biblioteca de componentes e componentes personalizados
- 🎯 componente COLABORATIVO planning, não de concepção baseada em pressupostos

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠ Apresentar menu A/P/C após gerar conteúdo de estratégia de componentes
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights de componentes mais profundos
- **P (Modo de Festa)**: Traz múltiplas perspectivas para definir a estratégia de componentes
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/\_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/\_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal das etapas anteriores estão disponíveis
- A escolha do sistema de design da etapa 6 determina os componentes disponíveis
- Viagens do usuário a partir da etapa 10 identificar necessidades de componentes
- Foco na definição de componentes personalizados e estratégia implementation

A sua tarefa:

Defina a estratégia de biblioteca de componentes e design de componentes personalizados não abrangidos pelo sistema de design.

## ESTRATÉGIA COMPONENTE SEQUÊNCIA:

### 1. Analisar a Cobertura do Sistema de Design

Reveja quais componentes estão disponíveis vs. necessários:
"Com base no nosso sistema de design escolhido [sistema de design do passo 6], let identifica quais componentes já estão disponíveis e o que precisamos para criar customizados.

**Disponível do sistema de design:**
[Lista de componentes disponíveis no sistema de projeto escolhido]

**Componentes necessários para {{project_name}}:**
Olhando para nossas jornadas de usuário e direção de design, precisamos:

- [Componente precisa 1 da análise da viagem]
- [Componente precisa 2 de requisitos de projeto]
- [Componente precisa 3 da experiência principal]

**Análise de Gap:**

- [Gap 1 - necessário, mas não disponível]
- [Gap 2 - necessário, mas não disponível]"

### 2. Design de componentes personalizados

Para cada componente personalizado necessário, design completamente:

**Para cada componente personalizado:**
**«[Nome do componente] Desenho:**

**Proporção:** O que esse componente faz para os usuários?
**Conteúdo:** Que informações ou dados exibe?
**Acções:** O que os usuários podem fazer com este componente?
**Estados:** Que estados diferentes tem? (padrão, hover, ativo, desativado, erro, etc.)
**Variantes:** São necessários diferentes tamanhos ou estilos?
**Acessibilidade:** Quais rótulos ARIA e suporte ao teclado necessários?

Vamos percorrer cada componente personalizado sistematicamente."

### 3. Especificações do componente do documento

Criar especificações detalhadas para cada componente:

**Modelo de especificação do componente:**

```markdown

### [Component Name]

**Purpose:** [Clear purpose statement]
**Usage:** [When and how to use]
**Anatomy:** [Visual breakdown of parts]
**States:** [All possible states with descriptions]
**Variants:** [Different sizes/styles if applicable]
**Accessibility:** [ARIA labels, keyboard navigation]
**Content Guidelines:** [What content works best]
**Interaction Behavior:** [How users interact]

```

### 4. Definir estratégia de componentes

Estabelecer uma abordagem global da biblioteca de componentes:
"**Estratégia Componente:**

**Componentes de fundação:** (do sistema de concepção)

- [Componente de fundação 1]
- [Componente de fundação 2]

**Componentes Personalizados:** (projetado nesta etapa)

- [Componente personalizado 1 com lógica]
- [Componente personalizado 2 com lógica]

**Implementation Aproximação:**

- Construir componentes personalizados usando tokens de sistema de design
- Assegurar a coerência com os padrões estabelecidos
- Siga as melhores práticas de acessibilidade
- Criar padrões reutilizáveis para casos de uso comum"

### 5. Plano Implementation Roteiro

Definir como e quando construir componentes:
**Implementation Roteiro:**

**Fase 1 - Componentes Principais:**

- [Componente 1] - Necessário para [fluxo crítico]
- [Componente 2] - Necessário para [fluxo crítico]

**Fase 2 - Componentes de Apoio:**

[Componente 3]
- [Componente 4] - suporta [padrão de design]

**Fase 3 - Componentes de Melhoria:**

- [Componente 5] - Optimiza [a viagem do utilizador]
[Componente 6] - adiciona [característica especial]

Este roteiro ajuda a priorizar o desenvolvimento baseado na criticidade da jornada do usuário."

### 6. Gerar estratégia de componentes