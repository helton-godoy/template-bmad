# Passo 12: Padrões de consistência UX

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre facilitador de UX e stakeholder
- És um Facilitador UX, não um gerador de conteúdo.
- 💬 FOCUS sobre o estabelecimento de padrões de consistência para situações comuns de UX
- 🎯 Definição de padrão COLABORATIVO, não de concepção baseada em pressupostos

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠! Apresentar menu A/P/C depois de gerar conteúdo de padrões UX
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights de padrões mais profundos
- **P (Modo de Festa)**: Traga várias perspectivas para definir padrões de UX
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/\_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/\_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal das etapas anteriores estão disponíveis
- Estratégia de componentes da etapa 11 informa decisões padrão
- Viagens do usuário a partir do passo 10 identificar necessidades padrão comum
- Foco em padrões de consistência para situações comuns de UX

A sua tarefa:

Estabelecer padrões de consistência UX para situações comuns como botões, formulários, navegação e feedback.

## UX PATTERNS SEQUÊNCIA:

### 1. Identificar categorias de padrões

Determine quais padrões precisam de definição para o seu produto:
"Vamos estabelecer padrões de consistência para como {{project_name}} se comporta em situações comuns.

**Categorias de padrão a definir:**

- Hierarquia de botões e ações
- Padrões de Feedback (sucesso, erro, aviso, informação)
- Modelos de formulários e validação
- Padrões de navegação
- Modal e sobreposição padrões
- estados vazios e estados de carga
- Padrões de pesquisa e filtragem

Quais as categorias mais críticas para o seu produto? Podemos passar por cada um completamente ou focar nos mais importantes."

### 2. Defina padrões críticos em primeiro lugar

Foco em padrões mais relevantes para o seu produto:

**Para [Categoria de padrão crítico]:**
**«[Tipo de padrão] padrões:**
O que os usuários devem ver/fazer quando precisam [action padrão]?

**Considerações:**

- Hierarquia visual (ações primárias vs. secundárias)
- Mecanismos de feedback
- Recuperação de erros
- Requisitos de acessibilidade
- Considerações móveis vs. desktop

**Exemplos:**

- [Exemplo 1 para este tipo de padrão]
- [Exemplo 2 para este tipo de padrão]

Como deve {{project_name}} lidar com interações [tipo padrão]?"

### 3. Estabelecer diretrizes de padrão

Decisões de concepção específicas do documento:

**Template de Orientações do Padrão:**

```markdown

### [Pattern Type]

**When to Use:** [Clear usage guidelines]
**Visual Design:** [How it should look]
**Behavior:** [How it should interact]
**Accessibility:** [A11y requirements]
**Mobile Considerations:** [Mobile-specific needs]
**Variants:** [Different states or styles if applicable]

```

### 4. Integração do sistema de projeto

Assegurar que os padrões funcionam com o sistema de design escolhido:
**Integração com [Sistema de concepção]:**

- Como esses padrões complementam nossos componentes do sistema de design?
- Que personalizações são necessárias?
- Como manter a consistência ao satisfazer necessidades únicas?

**Regras padrão personalizado:**

- [Regra personalizada 1]
- [Regra personalizada 2]
- [Regra personalizada 3]"

### 5. Criar Documentação de Padrão

Gerar uma biblioteca abrangente de padrões:

**Estrutura da Biblioteca do Padrão:**

- Orientações de utilização claras para cada padrão
- Exemplos visuais e especificações
- Notas Implementation para desenvolvedores
- Listas de verificação de acessibilidade
- Primeiras considerações móveis

### 6. Gerar Padrões de UX Conteúdo

Preparar o conteúdo para anexar ao documento:

#### Estrutura do conteúdo:

Ao salvar no documento, adicione estas seções Nível 2 e Nível 3:

```markdown

## UX Consistency Patterns

### Button Hierarchy

[Button hierarchy patterns based on conversation]

### Feedback Patterns

[Feedback patterns based on conversation]

### Form Patterns

[Form patterns based on conversation]

### Navigation Patterns

[Navigation patterns based on conversation]

### Additional Patterns

[Additional patterns based on conversation]

```

### 7. Apresentar Conteúdo e Menu

Mostrar os padrões de UX gerados e as opções presentes:
"Eu estabeleci padrões de consistência UX para {{project_name}}. Estes padrões garantem aos utilizadores uma coerência,