# Etapa 4: Decisões de Arquitectura Principais

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre pares arquitetônicos
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS em tomar decisões arquitetônicas críticas de forma colaborativa
- 🌐 Sempre procurar na web para verificar as versões atuais da tecnologia
A velocidade de desenvolvimento da IA mudou fundamentalmente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 🌐 Pesquise na web para verificar as versões e opções de tecnologia
- ⚠
- 💾 APENAS salve quando o usuário escolher C (Continuar)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e apresentar escolhas para cada categoria de decisão:

- **A (Elicitação Avançada)**: Utilizar protocolos de descoberta para explorar abordagens inovadoras para decisões específicas
- **P (Modo de Partida)**: trazer múltiplas perspectivas para avaliar trocas de decisões
- **C (Continua)**: Salve as decisões atuais e prossiga para a categoria de próxima decisão

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/\_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/\_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre para exibir o menu A/P/C deste passo após o A ou P terem completado
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Contexto do projeto a partir do passo 2 está disponível
- A escolha do modelo de arranque da etapa 3 está disponível
- O ficheiro de contexto do projecto pode conter preferências técnicas e regras
- Preferências técnicas descobertas na etapa 3 estão disponíveis
- Foco em decisões ainda não tomadas pelo modelo de arranque ou preferências existentes
- Tomada de decisão colaborativa, não recomendações

A sua tarefa:

Facilitar a tomada de decisões arquitetônicas colaborativas, alavancando as preferências técnicas existentes e as decisões de modelos de arranque, focando em escolhas ainda essenciais para o sucesso do projeto.

## DECISÃO QUE TOMA SEQUÊNCIA:

### 1. Carregar Quadro de Decisão e Verificar Preferências existentes

**Reveja as Preferências Técnicas da Etapa 3:**
"Com base na nossa discussão sobre preferências técnicas na etapa 3, a let baseia-se nessas bases:

**Suas Preferências Técnicas:**
{{user_technical_preferences_from_step_3}}

**Decisões do modelo de arranque:**
{{starter_template_decisions}}

**Project Context Technical Rules:**
{{project_context_technical_rules}}"

**Identificar as restantes decisões:**
Com base nas preferências técnicas, na escolha do modelo de arranque e no contexto do projecto, identificar as restantes decisões críticas:

**Já decidido (não re-decida):**

- {{starter_template_decisions}}
- {{user_technology_preferences}}
- {{project_context_technical_rules}}

**Decisões críticas:** Deve ser decidido antes de implementation poder prosseguir
**Decisões importantes:** Formar a arquitetura significativamente
**Bela para ter:** Pode ser adiada se necessário

### 2. Categorias de decisão por prioridade

#### Categoria 1: Arquitetura de dados

- Escolha do banco de dados (se não for determinado pelo arranque)
- Abordagem de modelagem de dados
- Estratégia de validação de dados
- Abordagem da migração
- Estratégia de cache

#### Categoria 2: Autenticação e segurança

- Método de autenticação
- Padrões de autorização
- middleware de segurança
- Encriptação de dados
- Estratégia de segurança da API

#### Categoria 3: API e Comunicação

- padrões de design de API (REST, GraphQL, etc.)
- Abordagem de documentação API
- Erro ao manusear padrões
- Estratégia de limitação de taxas
- Comunicação entre serviços

#### Categoria 4: Arquitetura Frontend (se aplicável)

- Abordagem da gestão estatal
- Arquitetura de componentes
- Estratégia de roteamento
- Otimização do desempenho
- Otimização de pacotes

#### Categoria 5: Infraestrutura e implantação

- Estratégia de acolhimento
- Aproximação do gasoduto CI/CD
- Configuração do ambiente
- Monitoramento e registro
- Estratégia de escala

### 3. Facilitar cada categoria de decisão

Para cada categoria, facilitar a tomada de decisão colaborativa:

**Apresentar a decisão:**
Baseado no nível de habilidade do usuário e contexto do projeto:

**Modo de especialista:**
{{Decision_Category}}: BMADPROTECT013End}

Options: {{concise_option_list_with_tradeoffs}}

Qual é a sua preferência por esta decisão?"

**Modo intermediário:**
"Próxima decisão: {{Human_Friendly_Category}}

Temos de escolher {{Specific_Decision}}.

Opções comuns:
{{option_list_with_brief_explanations}}

Para o teu projecto, eu inclinava-me para {{recommendation}} porque {{reason}}. Quais são os seus pensamentos?"

**Modo de início:**
Vamos falar sobre {{Human_Friendly_Category}}.

{{Educational_Context_About_Why_This_Matters}}

Pense em