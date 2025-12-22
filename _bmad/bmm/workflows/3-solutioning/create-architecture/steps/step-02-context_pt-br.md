# Etapa 2: Análise de Contexto do Projeto

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre pares arquitetônicos
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS sobre a compreensão do âmbito e dos requisitos do projecto para a arquitectura
- 🎯 ANALYZE documentos carregados, não assumir ou gerar requisitos
A velocidade de desenvolvimento da IA mudou fundamentalmente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠ Apresentar menu A/P/C após gerar análise de contexto do projeto
- 💾 SOMENTE salvar quando o usuário escolher C (Continuar)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights mais profundos sobre o contexto do projeto e implicações arquitetônicas
- **P (Modo de Festa)**: Traga várias perspectivas para analisar os requisitos do projeto de diferentes ângulos arquitetônicos
- **C (Continua)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre para exibir o menu A/P/C deste passo após o A ou P terem completado
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal da etapa 1 estão disponíveis
- Os documentos de entrada já carregados estão na memória (PRD, épicos, especificações UX, etc.)
- Foco nas implicações arquitectónicas das exigências
- Sem decisões tecnológicas ainda - fase de análise pura

A sua tarefa:

Leia e Analise completamente os documentos carregados do projeto para entender o escopo, os requisitos e as restrições arquitetônicas antes de iniciar a tomada de decisão.

## ANÁLISE DE CONTEXTO SEQUÊNCIA:

### 1. Rever os requisitos do projecto

**Da Análise PRD:**

- Extrair e analisar requisitos funcionais (RF)
- Identificar requisitos não funcionais (NFR) como desempenho, segurança, conformidade
- Observe quaisquer restrições técnicas ou dependências mencionadas
- Contar e categorizar requisitos para entender a escala do projeto

**De Épicos/Histórias (se disponíveis):**

- Mapa de estrutura épica e histórias de usuários para componentes arquitetônicos
- Extrair critérios de aceitação para implicações técnicas
- Identificar preocupações transversais que abrangem múltiplos épicos
- Estimativa da complexidade da história para planning

**De UX Design (se disponível):**

- Extrair implicações arquitetônicas dos requisitos de UX:
- Complexidade de componentes (formas simples vs interações ricas)
- Requisitos de animação/transição
- Necessidades de atualização em tempo real (dados ao vivo, recursos colaborativos)
- Requisitos de IU específicos da plataforma
- Normas de acessibilidade (nível de conformidade WCAG)
- Pontos de paragem de design responsivos
- Requisitos de capacidade desligados
- Expectativas de desempenho (tempos de carga, capacidade de interação)

### 2. Avaliação da Escala de Projetos

Calcular e apresentar a complexidade do projeto:

**Indicadores de complexidade:**

- Requisitos de recursos em tempo real
- Necessidades de multi-dotação
- Requisitos de conformidade regulamentar
- Complexidade de integração
- Complexidade de interação do usuário
- Complexidade e volume dos dados

### 3. Reflect Understanding

Apresente sua análise de volta ao usuário para validação:

"Estou revisando sua documentação de projeto para {{project_name}}.

{if_epics_loaded}I ver {{epic_count}} épicos com {{story_count}} histórias totais.
{if_no_epics}I encontrou requisitos funcionais {{fr_count}} organizados em {{fr_category_list}}.{/if_no_epics}
{if_ux_loaded}I também encontrou sua especificação UX que define os requisitos de experiência do usuário. {/if_ux_loaded}

**Aspectos arquitectónicos-chave noto:**

- [Summarize core functionality from FRs]
- [Note NFRs críticos que formarão arquitetura]
- {if_ux_loaded}[Nota complexidade UX e requisitos técnicos]{/if_ux_loaded}
- [Identifique desafios técnicos ou restrições únicas]
- [Highlight quaisquer requisitos regulamentares ou de conformidade]

**Indicadores de escala:**

- A complexidade do projecto parece ser: [baixa/média/alta/empresa]
- Domínio técnico primário: [web/mobile/api/backend/full-stack/etc]
- Questões transversais identificadas:

Essa análise me ajudará a guiá-lo através das decisões arquitetônicas necessárias para garantir que os agentes de IA implementem isso de forma consistente.

Isso corresponde à sua compreensão do escopo e dos requisitos do projeto?"

### 4. Gerar Conteúdo de Contexto do Projeto

Preparar o conteúdo para anexar ao documento:

#### Estrutura do conteúdo:

Marcação para baixo

## Analy Contexto do Projeto