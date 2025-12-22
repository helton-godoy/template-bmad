---
name: 'step-04-final-validation'
description: 'Validate complete coverage of all requirements and ensure implementation readiness'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/3-solutioning/create-epics-and-stories'

# File References
thisStepFile: '{workflow_path}/steps/step-04-final-validation.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/epics.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Template References
epicsTemplate: '{workflow_path}/templates/epics-template.md'
---

# Passo 4: Validação Final

## PASSO:

Para validar a cobertura completa de todos os requisitos e garantir que as histórias estejam prontas para o desenvolvimento.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 🔄 CRÍTICA: validação do processo sequencialmente sem pular
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um estrategista de produto e escritor de especificações técnicas
- ✅ Se você já recebeu comunicação ou padrões de persona, continue a usar aqueles enquanto desempenha este novo papel
- ✅ Nós nos engajamos em diálogo colaborativo, não em resposta a comandos
- ✅ Você traz experiência em validação e garantia de qualidade
- ✅ Usuário traz suas prioridades implementation e revisão final

### Regras específicas dos passos:

- 🎯 Concentre-se apenas na validação da cobertura completa dos requisitos
- 🚫 PROJECTO DE PUBLICAR as verificações de validação
- 💬 Validar cobertura FR, história completa e dependências
- 🚪 Garanta que todas as histórias estão prontas para o desenvolvimento

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Validar cada exigência tem cobertura de história
- Verifica as dependências da história e o fluxo.
- 📖 Verificar conformidade com a arquitetura
- 🚫 PROIBIDO Aprovar cobertura incompleta

## CONTEXTO MONTANTES:

- Contexto disponível: Repartição épica completa e história de etapas anteriores
- Focus: Validação final da cobertura dos requisitos e preparação para o relato
- Limits: Apenas validação, sem criação de novo conteúdo
- Dependencies: Geração completa de histórias a partir do Passo 3

## PROCESSO DE VALIDAÇÃO:

### 1. Validação da cobertura FR

Reveja o épico completo e história quebra para garantir que EVERY FR é coberto:

**CONTROLO CRÍTICO:**

- Passe por cada FR do Inventário de Requisitos
- Verifique se aparece em pelo menos uma história.
- Verificar se os critérios de aceitação correspondem plenamente ao RF
- Não devem ser descobertos FRs.

### 2. Arquitetura Implementation Validação

**Verifique a configuração do modelo inicial:**

- O documento de arquitectura especifica um modelo de arranque?
- Se SIM: Epic 1 Story 1 deve ser "Configurar projeto inicial do modelo inicial"
- Isto inclui clonagem, instalação de dependências, configuração inicial

**Database/Entity Creation Validation:**

- As tabelas/entidades de banco de dados são criadas APENAS quando necessário por histórias?
O Épico 1 cria todas as tabelas à frente.
- ✅ Direito: Mesas criadas como parte da primeira história que precisa
- Cada história deve criar/modificar apenas o que precisa

### 3. Validação da Qualidade da História

**Cada história deve:**

- Ser completo por um único agente de dev
- Ter critérios claros de aceitação
- FR específicos de referência implements
- Incluir os detalhes técnicos necessários
- **Não ter dependências para a frente** (só pode depender de histórias ANTERIORES)
- Ser implementável sem esperar por histórias futuras

### 4. Validação da Estrutura Épica

**Verifique isto:**

- Epics oferecem valor de usuário, não marcos técnicos
- As dependências fluem naturalmente
- Histórias da Fundação só configuram o que é necessário
- Nenhum trabalho técnico inicial.

### 5. Validação de dependência (CRITICAL)

**Epic Independence Check:**

- Cada épico oferece funcionalidade COMPLETE para seu domínio?
- Pode o Epic 2 function sem que o Epic 3 seja implementado?
- Pode Epic 3 function standalone usando saídas Epic 1 & 2?
- ❌ ERRADO: Epic 2 requer Epic 3 recursos para trabalhar
Cada épico é independentemente valioso.

**Checa de dependência de história dentro do Épico:**
Para cada épico, reveja histórias em ordem:

- A história N.1 pode ser completada sem histórias N.2, N.3, etc.?
- O Story N.2 pode ser concluído apenas com a saída Story N.1?
- A história N.3 pode ser concluída usando apenas as saídas N.1 e N.2?
Esta história depende de uma história futura.
- ❌ ERRADO: Referências de história características ainda não implementadas
- ✅ Certo: Cada história constrói-se apenas em histórias anteriores

### 6. Completar e salvar

Se todas as validações passarem:

- Actualizar os restantes placeholders no documento
- Assegurar a formatação adequada
- Salve o epics.md final

**Menu Final Apresentado:**
**Todas as validações completas!** [C] Fluxo de trabalho completo

Quando C é selecionado, o fluxo de trabalho está completo e o epics.md está pronto para o desenvolvimento.
