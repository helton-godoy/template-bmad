# Etapa 5: Implementation Regras de Consistência e Padrões

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre pares arquitetônicos
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS sobre padrões que impedem os conflitos entre o agente de IA implementation
- 🎯 EMFASSAM que agentes podem decidir de forma diferente, se não especificada
A velocidade de desenvolvimento da IA mudou fundamentalmente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 🎯 Foco na consistência, não implementation detalhes
- ⚠
- 💾 APENAS salve quando o usuário escolher C (Continuar)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4, 5]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver padrões de consistência abrangentes
- **P (Modo de Partida)**: trazer múltiplas perspectivas para identificar potenciais pontos de conflito
- **C (Continua)**: Salve os padrões e prossiga para a estrutura do projeto

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/\_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/\_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre para exibir o menu A/P/C deste passo após o A ou P terem completado
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- As principais decisões arquitetônicas do passo 4 estão completas
- A pilha de tecnologia é decidida e as versões são verificadas
- Foco em COMO os agentes devem implementar, não O QUE eles devem implementar
- Considere o que pode variar entre diferentes agentes de IA

A sua tarefa:

Defina padrões implementation e regras de consistência que garantam que vários agentes de IA escrevam código compatível e consistente que funcione em conjunto sem problemas.

## SEQUÊNCIA DE DEFINIÇÃO DOS PATTERNOS:

### 1. Identificar pontos de conflito potenciais

Com base na pilha de tecnologia escolhida e nas decisões, identificar onde agentes de IA poderiam fazer diferentes escolhas:

**Conflitos de Naming:**

- Convenção de nomenclatura de tabelas/colunas de banco de dados
- padrões de nomeação de parâmetros de API
- Nomeação de arquivos e diretórios
- Nomeação de componentes/function/variável
- Formatos de parâmetros de rota

**Conflitos estruturais:**

- Onde estão localizados os testes
- Como os componentes são organizados
- Onde vão os serviços públicos e os ajudantes
- Organização de arquivos de configuração
- Organização de ativos estáticos

**Format Conflitos:**

- Formatos de envoltório de resposta API
- Estruturas de resposta de erros
- Formatos de data/hora em APIs e UI
- Convenções de nomeação de campos JSON
- Utilização do código de estado da API

**Conflitos de comunicação:**

- Convenções de nomeação de eventos
- Estruturas de carga útil do evento
- Actualização do Estado
- Convenções de nomeação de ações
- Formatos e níveis de registro

**Conflictos de processo:**

- Carregando o estado de manipulação
- Padrões de recuperação de erros
- Tentar novamente as abordagens implementation
- Padrões de fluxo de autenticação
- Tempo de validação e métodos

### 2. Facilitar decisões de padrão

Para cada categoria de conflito, facilitar a definição de padrão colaborativo:

**Apresentar o ponto de conflito:**
Dado que estamos usando {{tech_stack}}, diferentes agentes de IA podem lidar com {{conflict_area}} de forma diferente.

Por exemplo, um agente pode nomear tabelas de banco de dados 'usuários' enquanto outro usa 'Utilizadores' - isso causaria conflitos.

Precisamos estabelecer padrões consistentes que todos os agentes seguem."

**Mostrar Opções e Trade-offs:**
"Abordagens comuns para {{pattern_category}}:

{{option_1}} - BMADPROTECT017End}
{{option_2}} - {{pros_and_cons}}
3. {{option_3}} - {{pros_and_cons}}

Qual abordagem faz mais sentido para o nosso projeto?"

**Conseguir decisão do usuário:**
"Qual é a sua preferência por este padrão? (ou discutir os trade-offs mais)"

### 3. Definir categorias de padrões

#### Padrões de Nomeação

**Database Naming:**

- Nomeação da tabela: usuários, usuários ou usuários?
- Nome da coluna: user id ou userId?
- Formato de chave estrangeira: user id ou fk user?
- Nomeação de índice: idx users email ou users email index?

**API Naming:**

- Nomeação do endpoint REST: /usuários ou /usuário? Plural ou singular?
- Formato do parâmetro de rota: :id ou {id}?
- Nome do parâmetro de consulta: user id ou userId?
- Convenções de nomeação de cabeçalho: X-Custom-Header ou Custom-Header?

**Nomeação de código:**

- Nome do componente: UserCard ou user-card?
- Nomeação de ficheiro: UserCard.tsx ou user-card.tsx?
- Nomeação da função: getUserData ou get user data?
- Nome da variável: userId ou user id?

#### Padrões de estrutura

**Organização do Projeto:**

- Onde vivem os testes? **testes**/ ou \*.test.ts co-localizados?
- Como são organizados os componentes? Por recurso ou por tipo?
- Para onde vão os serviços partilhados?
- Como são organizados serviços e repositórios?

**Arquivo Struc