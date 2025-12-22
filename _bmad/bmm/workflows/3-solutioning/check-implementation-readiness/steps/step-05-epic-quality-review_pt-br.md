---
name: 'step-05-epic-quality-review'
description: 'Validate epics and stories against create-epics-and-stories best practices'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/3-solutioning/implementation-readiness'

# File References
thisStepFile: '{workflow_path}/steps/step-05-epic-quality-review.md'
nextStepFile: '{workflow_path}/steps/step-06-final-assessment.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/implementation-readiness-report-{{date}}.md'
epicsBestPractices: '{project-root}/_bmad/bmm/workflows/3-solutioning/create-epics-and-stories'
---

# Passo 5: Revisão da Qualidade Épica

## PASSO:

Para validar épicos e histórias contra as melhores práticas definidas no fluxo de trabalho create-epics-and-stories, com foco no valor do usuário, independência, dependências e prontidão implementation.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um ENFORCER DE QUALIDADE EPICO
- ✅ Sabes como são os bons épicos - desafiar qualquer coisa desviante
- ✅ Épicos técnicos estão errados - encontrá-los
- ✅ Dependências dianteiras são proibidas - capture-as
- As histórias devem ser independentes.

### Regras específicas dos passos:

- 🎯 Aplicar rigorosamente padrões de criação-epics-and-stories
- 🚫 Não aceite "menos técnicos" como épicos
- 💬 Desafie toda a dependência do trabalho futuro
- 🚪 Verifique o dimensionamento e estrutura da história

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Validação sistemática de cada épico e história
- 💾 Documentar todas as violações das melhores práticas
- 📖 Verificar cada relação de dependência
- 🚫 PROJECTO de aceitar problemas estruturais

## PROCESSO DE REVISÃO DA QUALIDADE EPICA:

### 1. Inicializar Validação de Melhores Práticas

"Início **Epic Quality Review** contra padrões de criação-epics-and-stories.

Vou validar rigorosamente:

- Epics entregam valor de usuário (não marcos técnicos)
- Independência épica (Epic 2 não precisa Epic 3)
- Dependências da história (sem referências)
- Dimensionamento adequado da história e completude

Qualquer desvio das melhores práticas será sinalizado como um defeito."

### 2. Validação da Estrutura Épica

#### A. Verificação de Foco do Valor do Usuário

Para cada épico:

- **Título épico:** É centrado no usuário (o que o usuário pode fazer)?
- **Epic Goal:** Descreve o resultado do utilizador?
- **Proposição de valor:** Os usuários podem se beneficiar deste épico sozinho?

**Pavilhões vermelhos (violações):**

- "Definir banco de dados" ou "Criar modelos" - nenhum valor de usuário
- "Desenvolvimento da API" - marco técnico
- "Configuração da infra-estrutura" - não voltado para o utilizador
- "Sistema de autenticação" - limítrofe (é valor do usuário?)

#### B. Validação da Independência Épica

Teste a independência épica:

- **Épico 1:** Deve permanecer completamente sozinho
- **Epic 2:** pode function usando apenas saída Epic 1
- **Épico 3:** pode function usando saídas Epic 1 & 2
- **Regra:** N épico não pode exigir N+1 para trabalhar

**Falhas do processo:**

- "Épico 2 requer características Epic 3 para function"
- Histórias em Epic 2 referenciando componentes Epic 3
- Dependências circulares entre épicos

### 3. Avaliação da Qualidade da História

#### A. Validação do dimensionamento da história

Verifique cada história:

- **Limpar valor do utilizador:** A história traz algo significativo?
- **Independente:** Pode ser concluída sem histórias futuras?

**As violações comuns:**

- "Configurar todos os modelos" - não uma história USER
- "Criar a UI de login (depende da história 1.3)" - dependência

#### B. Revisão dos critérios de aceitação

Para os AC de cada história:

- **Dado/Quando/Então Formato:** Estrutura BDD adequada?
- **Testável:** Cada AC pode ser verificada independentemente?
- **Complete:** Abrange todos os cenários, incluindo erros?
- **Específico:** Resultados esperados claros?

**Issues para encontrar:**

- Critérios vagos como "user can login"
- Faltam condições de erro
- Caminho feliz incompleto
- Resultados não mensuráveis

### 4. Análise de dependência

#### A. Dependências intra-épicas

Mapa de dependências da história dentro de cada épico:

- A história 1.1 deve ser completa sozinha
- História 1.2 pode usar saída Story 1.1
- História 1.3 pode usar saídas Story 1.1 & 1.2

**Violações críticas:**

- "Esta história depende da História 1.4"
- "Espera que a história do futuro funcione"
- Características de referência de histórias ainda não implementadas

#### B. Tempo de criação de banco de dados/entidade

Validar a abordagem de criação de bases de dados:

- **Errado:** Epic 1 Story 1 cria todas as tabelas à frente
- **Direito:** Cada história cria tabelas de que precisa
- **Verificar:** As tabelas são criadas apenas quando necessário?

### 5. Implementation especial Controlos

#### A. Requerimento do modelo inicial

Verifique se a Arquitetura especifica o modelo inicial:

- Se SIM: Epic 1 Story 1 deve ser "Configurar projeto inicial do modelo inicial"
- Verificar história inclui clonagem, dependências, configuração inicial

#### B. Greenfield vs Brownfield Indicadores

Os projectos Greenfield deveriam ter:

- História inicial de configuração do projeto
- Configuração do ambiente de desenvolvimento
- CI/CD pipeline setu