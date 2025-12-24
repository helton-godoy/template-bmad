# Passo 3: Definição da experiência principal

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre facilitador de UX e stakeholder
- És um Facilitador UX, não um gerador de conteúdo.
- 💬 FOCUS na definição da experiência e plataforma do utilizador principal
- 🎯 Descoberta COLABORATIVA, não com base em suposições

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠ Apresentar menu A/P/C após gerar conteúdo de experiência principal
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights de experiência mais profundos
- **P (Modo de Festa)**: Traga múltiplas perspectivas para definir a experiência ideal do usuário
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal das etapas anteriores estão disponíveis
- O entendimento do projeto da etapa 2 informa esta etapa
- Não são necessários ficheiros de dados adicionais para esta etapa
- Foco na experiência central e nas decisões de plataforma

A sua tarefa:

Defina a experiência do usuário principal, os requisitos da plataforma e o que torna a interação sem esforço.

## CORE EXPERIÊNCIA DESCOBERTA SEQUÊNCIA:

### 1. Definir a Acção do Utilizador Principal

Comece identificando a interação mais importante do usuário:
"Agora o let cava o coração da experiência do usuário para o {{project_name}}.

**Perguntas da experiência da core:**

- Qual é a coisa que os usuários farão mais frequentemente?
- Que acção do utilizador é absolutamente fundamental para acertar?
- O que deve ser completamente sem esforço para os usuários?
Se apanharmos uma interacção, tudo o resto segue. O que é?

Pense no loop central ou ação primária que define o valor do seu produto."

### 2. Explore os requisitos da plataforma

Determine onde e como os usuários irão interagir:
"Vamos definir o contexto da plataforma para {{project_name}}:

**Perguntas da Plataforma:**

- Web, aplicativo móvel, desktop ou várias plataformas?
- Isto será principalmente baseado em toque ou mouse / teclado?
- Quaisquer requisitos ou restrições específicos da plataforma?
- Temos de considerar a funcionalidade offline?
- Alguma capacidade específica do dispositivo que devamos aproveitar?"

### 3. Identificar Interações Sem Esforço

Superfície o que deve parecer mágico ou completamente sem costura:
**Desenho sem experiência:**

- Que ações do usuário devem se sentir completamente naturais e exigir pensamento zero?
- Onde os usuários atualmente lutam com produtos semelhantes?
- Que interação, se feita sem esforço, criaria prazer?
- O que deve acontecer automaticamente sem intervenção do usuário?
- Onde podemos eliminar os passos que os concorrentes exigem?"

### 4. Defina momentos críticos de sucesso

Identificar os momentos que determinam o sucesso ou o fracasso:
**Momentos críticos de sucesso:**

- Qual é o momento em que os usuários percebem "isso é melhor"?
- Quando é que o utilizador se sente bem sucedido ou realizado?
- Que interacção, se falhar, arruinaria a experiência?
- Quais são os fluxos do utilizador?
- Onde é que acontece o primeiro sucesso do utilizador?"

### 5. Princípios de experiência de síntese

Extrair princípios orientadores da conversação:
"Com base na nossa discussão, estou a ouvir estes princípios fundamentais de experiência para {{project_name}}:

**Princípios de experiência:**

- [Princípio 1 baseado no foco central de ação]
- [Princípio 2 baseado em interações sem esforço]
- [Princípio 3 baseado em considerações de plataforma]
- [Princípio 4 baseado em momentos críticos de sucesso]

Estes princípios guiarão todas as nossas decisões de UX. Eles capturam o que é mais importante?"

### 6. Gerar Conteúdo de Experiência Principal

Preparar o conteúdo para anexar ao documento:

#### Estrutura do conteúdo:

Ao salvar no documento, adicione estas seções Nível 2 e Nível 3:

```markdown

## Core User Experience

### Defining Experience

[Core experience definition based on conversation]

### Platform Strategy

[Platform requirements and decisions based on conversation]

### Effortless Interactions

[Effortless interaction areas identified based on conversation]

### Critical Success Moments

[Critical success moments defined based on conversation]

### Experience Principles

[Guiding principles for UX decisions based on conversation]

```

### 7. Apresentar Conteúdo e Menu

Mostrar o cont de experiência gerada no núcleo