# Etapa 3: Avaliação do modelo inicial

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- ✅ Sempre trate isso como uma descoberta colaborativa entre pares arquitetônicos
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS na avaliação de opções de modelo de arranque com versões atuais
- 🌐 SEMPRE procure na web para verificar as versões atuais - NUNCA confie em versões codificadas
A velocidade de desenvolvimento da IA mudou fundamentalmente
- 📖 CRITICAL: SEMPRE leia o arquivo passo completo antes de tomar qualquer ação - compreensão parcial leva à arquitetura incompleta
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 🌐 Procurar na Web para verificar as versões e opções atuais
- ⚠' Apresentar menu A/P/C depois de gerar análise de modelo de arranque
- 💾 APENAS salve quando o usuário escolher C (Continuar)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Usar protocolos de descoberta para explorar opções de arranque não convencionais ou abordagens personalizadas
- **P (Modo de Partida)**: trazer múltiplas perspectivas para avaliar trocas de iniciadores para diferentes casos de uso
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/\_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/\_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre para exibir o menu A/P/C deste passo após o A ou P terem completado
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- O contexto do projeto da etapa 2 está disponível e completo
- O ficheiro de contexto do projecto a partir do passo-01 pode conter preferências técnicas
- Ainda não foram tomadas decisões arquitectónicas - avaliar fundações
- Foco na descoberta de preferências técnicas e avaliação inicial
- Considere os requisitos do projeto e as preferências existentes ao avaliar opções

A sua tarefa:

Descubra as preferências técnicas e avalie as opções de modelo de arranque, alavancando as preferências técnicas existentes e estabelecendo fundações arquitetônicas sólidas.

Sequência de avaliação inicial:

### 0. Verificar Preferências e Contexto Técnico

**Verifique o Contexto do Projeto para Preferências Técnicas existentes:**
"Antes de mergulharmos em modelos iniciais, let me verifique se você tem alguma preferência técnica já documentada.

{{if_project_context_exists}}
Encontrei algumas regras técnicas no seu ficheiro de contexto do projecto:
{{extracted_technical_preferences_from_project_context}}

**Project Context Technical Rules Found:**

- Línguas/Frameworks: {{languages_frameworks_from_context}}
- Ferramentas e Bibliotecas: {{tools_from_context}}
- Padrões de desenvolvimento: {{patterns_from_context}}
- Preferências da plataforma: {{platforms_from_context}}

{{else}}
Não foram encontradas preferências técnicas existentes no ficheiro de contexto do projecto. Vamos estabelecer as suas preferências técnicas agora.
{{/if_project_context}}"

**Descubra Preferências Técnicas do Usuário:**
"Com base no seu contexto de projeto, a let discute suas preferências técnicas:

{{primary_technology_category}} Preferências:

- **Idiomas**: Você tem preferências entre TypeScript/JavaScript, Python, Go, Rust, etc?
- **Frameworks**: Qualquer familiaridade ou preferências existentes (React, Vue, Angular, Next.js, etc.)?
- **Databases**: Quaisquer preferências ou infra-estruturas existentes (PostgreSQL, MongoDB, MySQL, etc.)?

**Experiência de desenvolvimento:**

- Qual é o nível de experiência da sua equipa com diferentes tecnologias?
- Há alguma tecnologia que queiras aprender contra aquilo com que te sintas confortável?

**Plataforma/Preferências de implantação:**

- Preferências de provedor de nuvem (AWS, Vercel, Railway, etc.)?
- Preferências de container (Docker, Serverless, Tradicional)?

**Integrações:**

- Quaisquer sistemas existentes ou APIs que precise integrar?
- Serviços de terceiros que você planeja usar (pagamento, autenticação, análise, etc.)?

Essas preferências me ajudarão a recomendar os modelos de arranque mais adequados e orientar nossas decisões arquitetônicas."

### 1. Identificar o domínio tecnológico primário

Com base na análise do contexto do projeto e nas preferências técnicas, identificar a pilha tecnológica primária:

- **Aplicação Web** → Procure Next.js, Vite, Remix, Iniciadores SvelteKit
- **App móvel** → Procure Reagir Nativo, Expo, Iniciadores Flutter
- **API/Backend** → Procure NestJS, Express, Fastify, Entradas Supabase
- **Ferramenta CLI** → Procure por iniciadores de framework CLI (oclif, comandante, etc.)
- **Full-stack** → Procure T3, RedwoodJS, Blitz, Next.js starters
- **Desktop** → Procure Electron, entradas Tauri

### 2. Consideração dos requisitos de UX

Se a especificação UX foi carregada, considere os requisitos UX ao selecionar o iniciador:

- **Animais ricos** → Início compatível com o Framer Motion
- **Complexo para