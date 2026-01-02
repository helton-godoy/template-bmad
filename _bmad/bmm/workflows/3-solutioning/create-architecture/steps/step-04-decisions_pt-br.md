# Passo 4: Decisões Arquitetônicas

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- 📖 CRÍTICO: Leia o arquivo de passo completo antes de tomar qualquer ação
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido
- 📋 VOCÊ É UM FACILITADOR, não um gerador de conteúdo
- 🎯 FOQUE na tomada de decisões estruturadas para componentes chave

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠️ Apresente menu A/P/C após gerar decisões
- 💾 SALVE APENAS quando o usuário escolher C (Continuar)
- 📖 Atualize o frontmatter `stepsCompleted: [1, 2, 3, 4]` antes de carregar o próximo passo
- 🚫 PROIBIDO carregar o próximo passo até que C seja selecionado

## MENUS DE COLABORAÇÃO (A/P/C):

Este passo irá gerar conteúdo e apresentar opções:

- **A (Elicitação Avançada)**: Aprofundar nas compensações (trade-offs) das decisões
- **P (Modo Festa)**: Debater alternativas arquitetônicas
- **C (Continuar)**: Salvar e prosseguir

## LIMITES DE CONTEXTO:

- Stack inicial já definido no passo 3
- Foco em decisões de alto nível (banco de dados, autenticação, comunicação, hospedagem)
- Considere as restrições identificadas no passo 2

## SUA TAREFA:

Facilitar a tomada de decisões para os principais componentes arquitetônicos, garantindo que as escolhas sejam compatíveis com o stack inicial e os requisitos do projeto.

## SEQUÊNCIA DE DECISÕES:

### 1. Identificar Áreas de Decisão

Com base no tipo de projeto e stack inicial, identifique quais decisões precisam ser tomadas:

- **Persistência de Dados**: SQL vs NoSQL, qual banco específico?
- **Autenticação e Autorização**: Provedor (Auth0, Firebase) vs Customizado? JWT vs Sessão?
- **Comunicação de API**: REST vs GraphQL vs gRPC?
- **Gerenciamento de Estado**: Global vs Local? Qual biblioteca?
- **Hospedagem/Infraestrutura**: Serverless vs Containers vs PaaS?

### 2. Facilitar Decisões

Para cada área, apresente opções e guie o usuário:

"Com base no nosso stack ({tech_stack}), precisamos decidir sobre [Área]:

**Opção A: [Opção 1]**
- Prós: ...
- Contras: ...
- Melhor para: ...

**Opção B: [Opção 2]**
- Prós: ...
- Contras: ...
- Melhor para: ...

Qual abordagem se alinha melhor com nossos requisitos de {NFR_relevante}?"

### 3. Registrar Decisões (ADR Leve)

Para cada decisão tomada, registre o "porquê":

- **Contexto**: O problema que estamos resolvendo
- **Decisão**: A tecnologia ou padrão escolhido
- **Justificativa**: Por que escolhemos isso (vínculo com requisitos)
- **Consequências**: O que ganhamos e o que perdemos (trade-offs)

### 4. Gerar Conteúdo de Decisões

Prepare o conteúdo para anexar ao documento:

#### Estrutura do conteúdo:

```markdown
## Architectural Decisions

### Data Persistence
- **Decision:** [Selected Database Technology]
- **Rationale:** [Why this fits our data model and scale]

### Authentication & Security
- **Decision:** [Selected Auth Strategy]
- **Rationale:** [Security requirements alignment]

### API Strategy
- **Decision:** [Selected Protocol]
- **Rationale:** [Client consumption needs]

### State Management
- **Decision:** [Selected Pattern/Lib]
- **Rationale:** [Complexity management]

### Deployment Strategy
- **Decision:** [Selected Infrastructure]
- **Rationale:** [Ops complexity vs control]
```

### 5. Apresentar Conteúdo e Menu

Mostre o conteúdo e o menu A/P/C.

### 6. Lidar com Seleção de Menu

- A: Refinar trade-offs
- P: Debater alternativas
- C: Salvar e ir para Padrões (Passo 5)

## MÉTRICAS DE SUCESSO:

✅ Decisões principais tomadas para todos os componentes críticos
✅ Justificativas claras registradas para cada decisão
✅ Alinhamento com o stack inicial e NFRs
✅ Usuário participou ativamente das escolhas

## PRÓXIMO PASSO:

Após o usuário selecionar [C], carregue `./step-05-patterns_pt-br.md` para definir os padrões de design e implementação.
