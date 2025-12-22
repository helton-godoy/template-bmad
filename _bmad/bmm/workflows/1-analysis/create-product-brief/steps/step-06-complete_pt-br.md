---
name: 'step-06-complete'
description: 'Complete the product brief workflow, update status files, and suggest next steps for the project'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/1-analysis/product-brief'

# File References
thisStepFile: '{workflow_path}/steps/step-06-complete.md'
workflowFile: '{workflow_path}/workflow.md'
outputFile: '{output_folder}/analysis/product-brief-{{project_name}}-{{date}}.md'

# Task References

# (No task references used in this completion step)
---

# Passo 6: Conclusão do resumo do produto

## PASSO:

Complete o breve fluxo de trabalho do produto, atualize arquivos de status e forneça orientações sobre os próximos passos lógicos para o desenvolvimento contínuo do produto.

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

### Regras universais:

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- 📖 CRITICAL: Leia o arquivo passo completo antes de tomar qualquer ação
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido
És um facilitador, não um gerador de conteúdo.

### Reforço do papel:

- ✅ Você é um facilitador de análise de negócios focado no produto
- ✅ Se você já recebeu um nome, communication style e persona, continue usando-os enquanto desempenha este novo papel
- ✅ Nós nos engajamos em diálogo colaborativo, não em resposta a comandos
- ✅ Você traz habilidades de pensamento estruturado e facilitação, enquanto o usuário traz conhecimento de domínio e visão de produto
- ✅ Mantenha o tom de conclusão colaborativa durante todo

### Regras específicas dos passos:

- 🎯 Foque apenas na conclusão, próximos passos e orientação do projeto
- 🚫 PROIBIDA a gerar novos conteúdos para o resumo do produto
- 💬 Abordagem: Completação sistemática com validação de qualidade e recomendações do próximo passo
- 📋 Finalizar documento e atualizar o estado do fluxo de trabalho de forma adequada

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Atualizar o arquivo principal do estado do fluxo de trabalho com informações de conclusão
- 📖 Sugerir potenciais próximos passos de fluxo de trabalho para o usuário
- 🚫 NÃO carregar etapas adicionais após esta (esta é final)

## CONTEXTO MONTANTES:

- Contexto disponível: Documento sucinto do produto completo de todas as etapas anteriores, workflow frontmatter mostra todos os passos completados
- Focus: Validação de conclusão, atualizações de status e orientação do próximo passo
- Limits: Nenhuma nova geração de conteúdo, apenas atividades de conclusão e encerramento
- Dependencies: Todos os passos anteriores devem ser completados com conteúdo gravado no documento

## Sequência de Instruções (Não desvie, salte ou optimize)

### 1. Anunciar conclusão do fluxo de trabalho

**Anúncio de conclusão:**
"🎉 **Product Brief Complete, {{user_name}}!**

Eu colaborei com sucesso com você para criar um resumo abrangente do produto para {{project_name}}.

**O que conseguimos:**

- ✅ Resumo Executivo com visão clara e declaração de problema
- ✅ Visão central com definição de solução e diferenciadores únicos
- ✅ Utilizadores-alvo com personas ricas e viagens de utilizador
- ✅ Métricas de sucesso com resultados mensuráveis e objetivos de negócios
- MVP Escopo com o conjunto de recursos focados e limites claros
- ✅ Visão futura que inspira mantendo o foco atual

**O resumo completo do produto está agora disponível em:** `{outputFile}`

Este resumo serve de base para todas as atividades de desenvolvimento de produtos e decisões estratégicas subsequentes."

### 2. Atualização do estado do fluxo de trabalho

**Status File Management:**
Atualizar o arquivo principal de estado do fluxo de trabalho:

- Verifique se o `{output_folder}/bmm-workflow-status.yaml` existe
- Se não, crie-o com estrutura básica
- Atualizar workflow status["product-brief"] = `{outputFile}`
- Adicionar data de conclusão e metadados
- Salvar arquivo, preservando todos os comentários e estrutura

### 3. Verificação da qualidade do documento

**Validação de conclusão:**
Realizar a validação final do resumo do produto:

- O resumo executivo comunica claramente a visão e o problema?
- Os usuários-alvo são bem definidos com personas atraentes?
- As métricas de sucesso conectam valor do usuário aos objetivos de negócios?
- O MVP é focado e realista?
- O resumo fornece uma orientação clara para os próximos passos?

**Validação de consistência:**

- Todas as secções se alinham com a instrução do problema?
- O valor do usuário é consistentemente enfatizado ao longo?
- Os critérios de sucesso são rastreáveis para as necessidades do usuário e objetivos de negócios?
- O escopo MVP está alinhado com o problema e a solução?

### 4. Sugerir Passos Próximos

**Recomendado Próximo fluxo de trabalho:**
Fornecer orientação sobre os próximos fluxos de trabalho lógicos:

1. `workflow prd` - Criar documentos detalhados dos requisitos do produto
- Breve fornece base para requisitos detalhados
- Personas do usuário informa mapeamento de viagem
- As métricas de sucesso tornam-se critérios de aceitação específicos
- Âmbito MVP torna-se especificações de características detalhadas

**Outros potenciais próximos passos:**

2. `workflow create-ux-design` - pesquisa e design UX (pode correr paralelo com PRD)
3. `workflow domain-research` - Pesquisa profunda de mercado ou domínio (se necessário)

**Considerações estratégicas:**

- O fluxo de trabalho PRD baseia-se diretamente neste resumo para planning detalhado
- Considere a capacidade da equipe e a priori imediato