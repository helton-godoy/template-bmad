# Passo 2: Análise de Contexto do Projeto

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- 📖 CRÍTICO: Leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido e compreendido antes de prosseguir
- ✅ SEMPRE trate isso como uma descoberta colaborativa entre pares arquitetônicos
- 📋 VOCÊ É UM FACILITADOR, não um gerador de conteúdo
- 💬 FOQUE na compreensão do escopo e requisitos do projeto para a arquitetura
- 🎯 ANALISE documentos carregados, não assuma ou gere requisitos

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠️ Apresente menu A/P/C após gerar análise de contexto do projeto
- 💾 SALVE APENAS quando o usuário escolher C (Continuar)
- 📖 Atualize o frontmatter `stepsCompleted: [1, 2]` antes de carregar o próximo passo
- 🚫 PROIBIDO carregar o próximo passo até que C seja selecionado

## MENUS DE COLABORAÇÃO (A/P/C):

Este passo irá gerar conteúdo e apresentar opções:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights mais profundos sobre o contexto do projeto e implicações arquitetônicas
- **P (Modo Festa)**: Traga várias perspectivas para analisar os requisitos do projeto de diferentes ângulos arquitetônicos
- **C (Continuar)**: Salve o conteúdo no documento e prossiga para o próximo passo

## INTEGRAÇÃO DE PROTOCOLO:

- Quando 'A' selecionado: Execute {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' selecionado: Execute {project-root}/_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS sempre retornam para exibir o menu A/P/C deste passo após o A ou P terem completado
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## LIMITES DE CONTEXTO:

- Documento atual e frontmatter da passo 1 estão disponíveis
- Documentos de entrada já carregados estão na memória (PRD, épicos, especificações UX, etc.)
- Foco nas implicações arquitetônicas dos requisitos
- Sem decisões tecnológicas ainda - fase de análise pura

## SUA TAREFA:

Leia e analise completamente os documentos carregados do projeto para entender o escopo, os requisitos e as restrições arquitetônicas antes de iniciar a tomada de decisão.

## SEQUÊNCIA DE ANÁLISE DE CONTEXTO:

### 1. Revisar Requisitos do Projeto

**Da Análise PRD:**

- Extrair e analisar requisitos funcionais (RF)
- Identificar requisitos não funcionais (NFR) como desempenho, segurança, conformidade
- Observe quaisquer restrições técnicas ou dependências mencionadas
- Conte e categorize requisitos para entender a escala do projeto

**De Épicos/Histórias (se disponíveis):**

- Mapeie estrutura épica e histórias de usuários para componentes arquitetônicos
- Extraia critérios de aceitação para implicações técnicas
- Identifique preocupações transversais que abrangem múltiplos épicos
- Estime a complexidade da história para planejamento

**De UX Design (se disponível):**

- Extraia implicações arquitetônicas dos requisitos de UX:
- Complexidade de componentes (formas simples vs interações ricas)
- Requisitos de animação/transição
- Necessidades de atualização em tempo real (dados ao vivo, recursos colaborativos)
- Requisitos de UI específicos da plataforma
- Normas de acessibilidade (nível de conformidade WCAG)
- Pontos de interrupção de design responsivos
- Requisitos de capacidade offline
- Expectativas de desempenho (tempos de carga, capacidade de resposta)

### 2. Avaliação da Escala do Projeto

Calcule e apresente a complexidade do projeto:

**Indicadores de complexidade:**

- Requisitos de recursos em tempo real
- Necessidades de multi-tenancy
- Requisitos de conformidade regulamentar
- Complexidade de integração
- Complexidade de interação do usuário
- Complexidade e volume de dados

### 3. Refletir Entendimento

Apresente sua análise de volta ao usuário para validação:

"Estou revisando sua documentação de projeto para {{project_name}}.

{if_epics_loaded}Vejo {{epic_count}} épicos com {{story_count}} histórias totais.{/if_epics_loaded}
{if_no_epics}Encontrei {{fr_count}} requisitos funcionais organizados em {{fr_category_list}}.{/if_no_epics}
{if_ux_loaded}Também encontrei sua especificação UX que define os requisitos de experiência do usuário.{/if_ux_loaded}

**Aspectos arquitetônicos-chave que noto:**

- [Resuma a funcionalidade principal dos RFs]
- [Note NFRs críticos que formarão a arquitetura]
- {if_ux_loaded}[Note complexidade UX e requisitos técnicos]{/if_ux_loaded}
- [Identifique desafios técnicos ou restrições únicas]
- [Destaque quaisquer requisitos regulamentares ou de conformidade]

**Indicadores de escala:**

- A complexidade do projeto parece ser: [baixa/média/alta/empresa]
- Domínio técnico primário: [web/mobile/api/backend/full-stack/etc]
- Questões transversais identificadas:

Essa análise me ajudará a guiá-lo através das decisões arquitetônicas necessárias para garantir que os agentes de IA implementem isso de forma consistente.

Isso corresponde à sua compreensão do escopo e dos requisitos do projeto?"

### 4. Gerar Conteúdo de Contexto do Projeto

Prepare o conteúdo para anexar ao documento:

#### Estrutura do conteúdo:

```markdown
## Project Context Analysis

### Scope & Complexity
[Analysis of project scale and complexity]

### Key Functional Drivers
[Core functional requirements driving architecture]

### Critical Quality Attributes (NFRs)
[Performance, Security, Scalability requirements]

### Constraints & Compliance
[Technical, legal, or business constraints]
```

### 5. Apresentar Conteúdo e Menu

Mostre o conteúdo gerado e apresente o menu A/P/C:

"Documentei a análise de contexto do projeto.

**Aqui está o que vou adicionar ao documento:**
[Mostre o conteúdo markdown]

**O que você gostaria de fazer?**
[A] Elicitação Avançada - Aprofundar na análise de requisitos
[P] Modo Festa - Obter múltiplas perspectivas arquitetônicas
[C] Continuar - Salvar e ir para Decisões Iniciais (Passo 3)"

### 6. Lidar com Seleção de Menu

#### SE A (Elicitação Avançada):

- Execute {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Retorne com insights aprimorados

#### SE P (Modo Festa):

- Execute {project-root}/_bmad/core/workflows/party-mode/workflow.md
- Retorne com perspectivas colaborativas

#### SE C (Continuar):

- Anexe o conteúdo final ao documento
- Atualize frontmatter: `stepsCompleted: [1, 2]`
- Carregue `./step-03-starter_pt-br.md`

## MÉTRICAS DE SUCESSO:

✅ Análise completa dos requisitos funcionais e não funcionais
✅ Complexidade do projeto avaliada corretamente
✅ Implicações arquitetônicas de UX identificadas
✅ Usuário validou o entendimento do contexto
✅ Conteúdo salvo no documento com estrutura adequada

## MODOS DE FALHA:

❌ Ignorar documentos carregados e fazer perguntas genéricas
❌ Falha em identificar NFRs críticos
❌ Subestimar a complexidade do projeto
❌ Prosseguir sem validação do usuário

❌ **CRÍTICO**: Ler apenas parte do arquivo de passo
❌ **CRÍTICO**: Prosseguir com 'C' sem ler o próximo arquivo

## PRÓXIMO PASSO:

Após o usuário selecionar [C], carregue `./step-03-starter_pt-br.md` para tomar as decisões de tecnologia inicial.
