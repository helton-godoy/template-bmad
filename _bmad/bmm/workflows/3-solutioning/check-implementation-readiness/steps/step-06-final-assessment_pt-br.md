---
name: 'step-06-final-assessment'
description: 'Compile final assessment and polish the readiness report'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/3-solutioning/implementation-readiness'

# File References
thisStepFile: '{workflow_path}/steps/step-06-final-assessment.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/implementation-readiness-report-{{date}}.md'
---

# Etapa 6: Avaliação final

## PASSO:

Fornecer um resumo completo de todas as conclusões e dar ao relatório um polimento final, garantindo recomendações claras e um estado de prontidão global.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 📖 Você está na etapa final - completar a avaliação
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você está entregando a AVALIAÇÃO FINAL
- ✅ Suas descobertas são objetivas e apoiadas por evidências
- ✅ Fornecer recomendações claras e acionáveis
- ✅ O sucesso é medido pelo valor dos achados

### Regras específicas dos passos:

- 🎯 Compilar e resumir todas as conclusões
- 🚫 Não amoleça a mensagem - seja direto
- 💬 Fornecer exemplos específicos para problemas
- 🚪 Adicionar a secção final ao relatório

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Reveja todas as conclusões das etapas anteriores
- 💾 Adicionar resumo e recomendações
- 📖 Determinar o estado geral de prontidão
- 🚫 Relatório final completo e presente

## PROCESSO DE AVALIAÇÃO FINAL:

### 1. Inicializar avaliação final

"Avaliação final".

Eu vou agora.

1. Reveja todas as conclusões de etapas anteriores
2. Forneça um resumo abrangente
3. Adicione recomendações específicas
4. Determinar o estado geral de prontidão"

### 2. Rever conclusões anteriores

Verifique o {outputFile} para seções adicionadas por etapas anteriores:

- Resultados de validação de arquivos e FR
- Questões de alinhamento por UX
- Violação da qualidade épica

### 3. Adicionar Secção de Avaliação Final

Anexar ao {outputFile}:

```markdown

## Summary and Recommendations

### Overall Readiness Status

[READY/NEEDS WORK/NOT READY]

### Critical Issues Requiring Immediate Action

[List most critical issues that must be addressed]

### Recommended Next Steps

1. [Specific action item 1]
2. [Specific action item 2]
3. [Specific action item 3]

### Final Note

This assessment identified [X] issues across [Y] categories. Address the critical issues before proceeding to implementation. These findings can be used to improve the artifacts or you may choose to proceed as-is.

```

### 4. Completar o relatório

- Assegurar que todas as conclusões sejam claramente documentadas
- Verificar recomendações são acionáveis
- Adicionar data e informação do avaliador
- Salve o relatório final

### 5. Conclusão atual

Display:
**Implementation Avaliação de prontidão completa**

Relatório gerado: {outputFile}

A avaliação encontrou [número] questões que requerem atenção. Reveja o relatório detalhado para conclusões e recomendações específicas."

## TRABALHAR COMPLETE

O fluxo de trabalho de prontidão implementation está agora completo. O relatório contém todas as conclusões e recomendações a considerar pelo utilizador.

---

## 🚨

### ✅ SUCESSO:

- Todos os resultados compilados e resumidos
- Recomendações claras apresentadas
- Determinação do estado de prontidão
- Relatório final salvo

### ❌

- Sem rever as conclusões anteriores
- Resumo incompleto
- Sem recomendações claras.
