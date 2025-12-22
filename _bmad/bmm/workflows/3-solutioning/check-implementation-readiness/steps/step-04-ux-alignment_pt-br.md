---
name: 'step-04-ux-alignment'
description: 'Check for UX document and validate alignment with PRD and Architecture'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/3-solutioning/implementation-readiness'

# File References
thisStepFile: '{workflow_path}/steps/step-04-ux-alignment.md'
nextStepFile: '{workflow_path}/steps/step-05-epic-quality-review.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/implementation-readiness-report-{{date}}.md'
---

# Passo 4: Alinhamento de UX

## PASSO:

Para verificar se existe documentação de UX e validar que ela se alinha com os requisitos de PRD e decisões de arquitetura, garantindo contas de arquitetura tanto para PRD e UX necessidades.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um UX VALIDATOR garantindo que a experiência do usuário seja corretamente abordada
- ✅ Os requisitos de UX devem ser suportados pela arquitetura
- ✅ Faltar documentação UX é um aviso se UI está implícito
- ✅ As lacunas de alinhamento devem ser documentadas

### Regras específicas dos passos:

- 🎯 Verifique primeiro a existência de documentos UX
- 🚫 Não assuma que UX não é necessário
- 💬 Validar alinhamento entre UX, PRD e Arquitetura
- 🚪 Adicionar conclusões ao relatório de saída

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Procure por documentação UX
- 💾 Se for encontrado, valide o alinhamento
- 📖 Se não for encontrado, avaliar se UX está implícito
- 🚫 PROIBIDA a proceder sem completar a avaliação

## PROCESSO DE ALIMENTAÇÃO UX:

### 1. Inicializar a Validação de UX

"Início da validação **UX Alinhamento**.

Eu vou.

1. Verifique se existe documentação UX
2. Se UX existe: validar alinhamento com PRD e Arquitetura
3. Se nenhum UX: determinar se UX está implícito e documento de aviso"

### 2. Procure por Documentação UX

Padrões de pesquisa:

- `{output_folder}/*ux*.md` (documento completo)
- `{output_folder}/*ux*/index.md` (esfarrapado)
- Procure termos relacionados à IU em outros documentos

### 3. Se o documento UX existir

#### A. UX ↔ PRD Alinhamento

- Verificar os requisitos de UX refletidos no PRD
- Verifique as jornadas do usuário em casos de uso de PRD
- Identificar os requisitos de UX não em PRD

#### B. UX ↔ Architecture Alinhamento

- Verificar arquitetura suporta requisitos de UX
- Verificar as necessidades de desempenho (responsividade, tempos de carga)
- Identificar componentes de UI não suportados pela arquitetura

### 4. Se não existir documento UX

Avaliar se UX/UI está implícito:

- O PRD menciona interface de utilizador?
- Existem componentes web/móvel implícitos?
- Isto é uma aplicação virada para o utilizador?

Se UX implicado, mas em falta: Adicionar o aviso ao relatório

### 5. Adicionar conclusões ao relatório

Adicionar ao {outputFile}:

```markdown

## UX Alignment Assessment

### UX Document Status

[Found/Not Found]

### Alignment Issues

[List any misalignments between UX, PRD, and Architecture]

### Warnings

[Any warnings about missing UX or architectural gaps]

```

### 6. Auto-Proceder para o passo seguinte

Após a avaliação de UX completa, imediatamente carregar o próximo passo.

## PROCESSO DE REEXAME DE QUALIDADE EPICA

Avaliação de alinhamento de UX completa. Carregando o próximo passo para revisão de qualidade épica.

---

## 🚨

### ✅ SUCESSO:

- Verificação da existência do documento UX
- Alinhamento validado se existir UX
- Aviso emitido se UX implicado, mas em falta
- Resultados adicionados ao relatório

### ❌

- Não verificando o documento UX
- Ignorando questões de alinhamento
- Não documentar avisos
