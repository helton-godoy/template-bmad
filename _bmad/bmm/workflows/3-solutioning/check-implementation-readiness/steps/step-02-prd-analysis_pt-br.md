---
name: 'step-02-prd-analysis'
description: 'Read and analyze PRD to extract all FRs and NFRs for coverage validation'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/3-solutioning/implementation-readiness'

# File References
thisStepFile: '{workflow_path}/steps/step-02-prd-analysis.md'
nextStepFile: '{workflow_path}/steps/step-03-epic-coverage-validation.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/implementation-readiness-report-{{date}}.md'
epicsFile: '{output_folder}/*epic*.md' # Will be resolved to actual file
---

# Etapa 2: Análise PRD

## PASSO:

Ler e analisar totalmente o documento PRD (todo ou em pedaços) para extrair todos os Requisitos Funcionais (FR) e Requisitos Não Funcionais (NFR) para validação contra cobertura épica.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um gerente de produto especialista e mestre Scrum
- ✅ Sua experiência é em análise de requisitos e rastreabilidade
- ✅ Você pensa criticamente sobre a integralidade da exigência
- ✅ O sucesso é medido na extração completa dos requisitos

### Regras específicas dos passos:

- 🎯 Concentre-se apenas na leitura e extração de PRD
- 🚫 Não valide arquivos (done na etapa 1)
- 💬 Leia PRD completamente - arquivos inteiros ou todos os fragmentos
- 🚪 Extrair todos os FR e NFR com numeração

## PROTOCOLOS DE EXECUÇÃO:

- Carregar e ler completamente o PRD
- 💾 Extrair sistematicamente todos os requisitos
- 📖 Conclusões documentais do relatório
- 🚫 PROJECTO de ignorar ou resumir o conteúdo PRD

## PROCESSO DE ANÁLISE PRD:

### 1. Inicializar Análise PRD

"Começando **Análise PRD** para extrair todos os requisitos.

Eu vou.

1. Carregar o documento PRD (todo ou raspado)
2. Leia-o completa e completamente
3. Extrair TODOS os requisitos funcionais (FR)
4. Extrair TODOS os requisitos não funcionais (NFRs)
5. Conclusões documentais para validação de cobertura"

### 2. Carregar e ler PRD

A partir do inventário do documento na etapa 1:

- Se todo o arquivo PRD existe: Carregar e ler completamente
- Se existe um PRD: Carregar e ler TODOS os ficheiros na pasta PRD
- Garantir cobertura completa - nenhum arquivo ignorado

### 3. Requisitos funcionais de extracção (RF)

Procurar e extrair:

- FR numerados (FR1, FR2, FR3, etc.)
- Requisitos rotulados como "Requisito Funcional"
- Histórias de usuários ou casos de uso que representam necessidades funcionais
- Regras de negócio que devem ser implementadas

Formatar as conclusões como:

```

## Functional Requirements Extracted

FR1: [Complete requirement text]
FR2: [Complete requirement text]
FR3: [Complete requirement text]
...
Total FRs: [count]

```

### 4. Extrair requisitos não funcionais (NFR)

Procurar e extrair:

- Requisitos de desempenho (tempos de resposta, rendimento)
- Requisitos de segurança (autenticação, criptografia, etc.)
- Requisitos de usabilidade (acessibilidade, facilidade de uso)
- Requisitos de confiabilidade (tempo de espera, taxas de erro)
- Requisitos de escalabilidade (usuários concorrentes, crescimento de dados)
- Requisitos de conformidade (normas, regulamentos)

Formatar as conclusões como:

```

## Non-Functional Requirements Extracted

NFR1: [Performance requirement]
NFR2: [Security requirement]
NFR3: [Usability requirement]
...
Total NFRs: [count]

```

### 5. Requisitos adicionais do documento

Procurar por:

- Restrições ou suposições
- Requisitos técnicos não rotulados como FR/NFR
- Restrições comerciais
- Requisitos de integração

### 6. Adicionar ao relatório de avaliação

Adicionar ao {outputFile}:

```markdown

## PRD Analysis

### Functional Requirements

[Complete FR list from section 3]

### Non-Functional Requirements

[Complete NFR list from section 4]

### Additional Requirements

[Any other requirements or constraints found]

### PRD Completeness Assessment

[Initial assessment of PRD completeness and clarity]

```

### 7. Auto- Proceed to Next Step

Após a análise do PRD concluída, carregue imediatamente o próximo passo para validação de cobertura épica.

## PROCESSO DE VALIDAÇÃO DA COBERTURA EPICA

Análise PRD completa. Carregando o próximo passo para validar a cobertura épica.

---

## 🚨

### ✅ SUCESSO:

- PRD carregado e lido completamente
- Todos os FR extraídos com texto completo
- Todos os NFR identificados e documentados
- Resultados adicionados ao relatório de avaliação

### ❌

- Não ler PRD completo (especialmente versões em cacos)
- Requisitos em falta na extracção
- Resumindo em vez de extrair texto completo
- Não documentar conclusões no relatório

**Regra Mestre:** A extracção completa dos requisitos é essencial para a validação da rastreabilidade.
