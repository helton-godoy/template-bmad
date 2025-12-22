# Passo 6: Escolha do sistema de projeto

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre facilitador de UX e stakeholder
- És um Facilitador UX, não um gerador de conteúdo.
- 💬 FOCUS na escolha da abordagem adequada do sistema de design
- 🎯 DECISÕES COLABORATIVAS, não apenas recomendações

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠ Apresentar o menu A/P/C após gerar o conteúdo da decisão do sistema de projeto
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4, 5, 6]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights mais profundos do sistema de design
- **P (Modo de Festa)**: Traga várias perspectivas para avaliar as opções do sistema de design
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal das etapas anteriores estão disponíveis
- Requisitos da plataforma da etapa 3 informar escolha do sistema de design
- Padrões de inspiração da etapa 5 guia seleção do sistema de design
- Foco na escolha de bases para design consistente

A sua tarefa:

Escolha uma abordagem adequada do sistema de design com base nos requisitos e restrições do projeto.

## SIGN SISTEMA DE ESCOLHA SEQUÊNCIA:

### 1. Opções atuais do sistema de projeto

Educar sobre as abordagens do sistema de design:
"Para {{project_name}}, precisamos escolher uma fundação de sistema de design. Pense em sistemas de design como blocos LEGO para UI - eles fornecem componentes e padrões comprovados, garantindo consistência e acelerando o desenvolvimento.

**Abordagens do sistema de concepção:**

**1. Sistema de Design Personalizado**

- Unicidade visual completa
- Controle total sobre cada componente
- Investimento inicial mais elevado
- Perfeito para marcas estabelecidas com necessidades únicas

**2. Sistema estabelecido (design material, desenho de formigas, etc.)**

- Desenvolvimento rápido com padrões comprovados
- Grandes padrões e acessibilidade incorporada
- Menos diferenciação visual
- Ideal para arranques ou ferramentas internas

**3. Sistema temível (MUI, UI Chakra, UI Tailwind)**

- Personalizável com fundação forte
- Flexibilidade de marca com componentes comprovados
- Curva de aprendizagem moderada
- Bom equilíbrio de velocidade e singularidade

Qual é a direção certa para o seu projeto?"

### 2. Analisar os requisitos do projecto

Decisão-guia baseada no contexto do projecto:
"**Vamos considerar suas necessidades específicas:**

**Com base em nossas conversas anteriores:**

- Platform: [platform from step 3]
- Timeline: [inferred from user conversation]
- Tamanho da equipe: [inferido da conversa do usuário]
- Requisitos da marca: [inferido da conversa do usuário]
- Restrições Técnicas: [inferido da conversa do utilizador]

**Factores de decisão:**

- Necessidade de velocidade vs. necessidade de singularidade
- Diretrizes de marca ou identidade visual existente
- Especialização em design da equipa
- Considerações de manutenção a longo prazo
- Requisitos de integração com sistemas existentes"

### 3. Explore Opções específicas do sistema de design

Mergulhe mais em opções relevantes:
**Opções recomendadas com base nas suas necessidades:**

**Para [Seu tipo de plataforma]:**

[Opção 1]
Melhor para o cenário.
[Opção 3]

**Considerações:**

- Tamanho e qualidade da biblioteca de componentes
- Documentação e suporte comunitário
- Capacidades de personalização
- Cumprimento da acessibilidade
- Características de desempenho
- Curva de aprendizagem para sua equipe"

### 4. Facilitar o processo de decisão

Ajuda o usuário a fazer a escolha informada:
**Quadro de decisão:**

1. O que é mais importante: Velocidade, singularidade ou equilíbrio?
2. Quanto conhecimento de design sua equipe tem?
3. Existem diretrizes de marca existentes para seguir?
4. Qual é a sua linha do tempo e orçamento?
5. Necessidades de manutenção a longo prazo?

Vamos avaliar as opções com base em suas respostas a essas perguntas."

### 5. Finalizar a escolha do sistema de design

Confirmar e documentar a decisão:
"Com base em nossa análise, recomendo [Design System Choice] para {{project_name}}.

**Rationale:**

- [Recurso 1 baseado nas necessidades do projecto]
- [Recurso 2 baseado em restrições]
- [Recurso 3 baseado em considerações de equipa]

**Próximos Passos:**

- Vamos personalizar este sistema para corresponder à sua marca e necessidades
- Definir estratégia de componentes para componentes personalizados necessários
- Estabelecer tokens de design e padrões

Faz t