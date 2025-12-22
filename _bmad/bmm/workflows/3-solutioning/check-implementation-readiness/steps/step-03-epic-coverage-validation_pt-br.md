---
name: 'step-03-epic-coverage-validation'
description: 'Validate that all PRD FRs are covered in epics and stories'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/3-solutioning/implementation-readiness'

# File References
thisStepFile: '{workflow_path}/steps/step-03-epic-coverage-validation.md'
nextStepFile: '{workflow_path}/steps/step-04-ux-alignment.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/implementation-readiness-report-{{date}}.md'
---

# Passo 3: Validação da Cobertura Épica

## PASSO:

Para validar que todos os Requisitos Funcionais do PRD são capturados no documento épico e histórias, identificando eventuais lacunas de cobertura.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um gerente de produto especialista e mestre Scrum
- ✅ Sua experiência é na rastreabilidade de requisitos
- ✅ Você garante que nenhum requisito cair através das rachaduras
- ✅ O sucesso é medido em cobertura FR completa

### Regras específicas dos passos:

- 🎯 Foco SOMENTE na validação de cobertura FR
- 🚫 Não analise a qualidade da história (isso é mais tarde)
- Compara o PRD. FRs contra lista de cobertura épica
- 🚪 Documentar todos os FR em falta

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Carregar o documento épico completamente
- 💾 Extrair cobertura FR de épicos
- 📖 Compare com a lista PRD FR
- 🚫 PROIBIDO proceder sem documentar lacunas

## PROCESSO DE VALIDAÇÃO DA CAPA EPICA:

### 1. Inicializar a Validação da Cobertura

"Início **Validação da Cobertura Épica**.

Eu vou.

1. Carregar o documento épico e histórias
2. Extrair informações de cobertura FR
3. Compare contra PRD FRs da etapa anterior
4. Identificar quaisquer FRs não cobertos em épicos"

### 2. Carregar documento épico

A partir do inventário do documento na etapa 1:

- Carregar os documentos épicos e histórias (todo ou desfiado)
- Leia-o completamente para encontrar informações de cobertura FR
- Procure seções como "Mapa de Cobertura FR" ou similares

### 3. Extrair cobertura épica FR

Do documento épico:

- Encontrar mapeamento de cobertura FR ou lista
- Extracto dos números FR que se pretende abranger
- Documento que abrange épicos que FR

Formato como:

```

## Epic FR Coverage Extracted

FR1: Covered in Epic X
FR2: Covered in Epic Y
FR3: Covered in Epic Z
...
Total FRs in epics: [count]

```

### 4. Comparar cobertura contra PRD

Usando a lista PRD FR do passo 2:

- Verifique cada PRD FR contra cobertura épica
- Identificar FRs NÃO abrangidos por épicos
- Note quaisquer FRs em épicos, mas não em PRD

Criar matriz de cobertura:

```

## FR Coverage Analysis

| FR Number | PRD Requirement | Epic Coverage  | Status    |
| --------- | --------------- | -------------- | --------- |
| FR1       | [PRD text]      | Epic X Story Y | ✓ Covered |
| FR2       | [PRD text]      | **NOT FOUND**  | ❌ MISSING |
| FR3       | [PRD text]      | Epic Z Story A | ✓ Covered |

```

### 5. Cobertura do documento em falta

Listar todos os FR não abrangidos:

```

## Missing FR Coverage

### Critical Missing FRs

FR#: [Full requirement text from PRD]
- Impact: [Why this is critical]
- Recommendation: [Which epic should include this]

### High Priority Missing FRs

[List any other uncovered FRs]

```

### 6. Adicionar ao relatório de avaliação

Anexar ao {outputFile}:

```markdown

## Epic Coverage Validation

### Coverage Matrix

[Complete coverage matrix from section 4]

### Missing Requirements

[List of uncovered FRs from section 5]

### Coverage Statistics

- Total PRD FRs: [count]
- FRs covered in epics: [count]
- Coverage percentage: [percentage]

```

### 7. Auto- Proceed to Next Step

Após a validação da cobertura completa, carregue imediatamente o próximo passo.

## PROCESSO DE ALIMENTAÇÃO DE UX

Validação de cobertura épica completa. Carregando o próximo passo para alinhamento UX.

---

## 🚨

### ✅ SUCESSO:

- Documento épico carregado completamente
- Cobertura FR extraída com precisão
- Todas as lacunas identificadas e documentadas
- Matriz de cobertura criada

### ❌

- Não ler documento épico completo
- Faltam FRs em comparação
- Não documentar requisitos descobertos
- Análise de cobertura incompleta

**Regra Mestre:** Cada FR deve ter um caminho implementation rastreável.
