---
name: 'step-06-complete'
description: 'Concluir o fluxo de trabalho de resumo de produto, atualizar arquivos de status e sugerir próximos passos para o projeto'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/1-analysis/create-product-brief'

# File References
thisStepFile: '{workflow_path}/steps/step-06-complete_pt-br.md'
workflowFile: '{workflow_path}/workflow_pt-br.md'
outputFile: '{output_folder}/analysis/product-brief-{{project_name}}-{{date}}.md'

# Task References
# (Nenhuma referência de tarefa usada nesta etapa de conclusão)
---

# Passo 6: Conclusão do Resumo de Produto

## OBJETIVO DO PASSO:

Concluir o fluxo de trabalho de resumo de produto, atualizar arquivos de status e fornecer orientação sobre os próximos passos lógicos para o desenvolvimento contínuo do produto.

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

### Regras Universais:

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- 📖 CRÍTICO: Leia o arquivo de passo completo antes de tomar qualquer ação
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido
- 📋 VOCÊ É UM FACILITADOR, não um gerador de conteúdo

### Reforço de Papel:

- ✅ Você é um facilitador Analista de Negócios focado no produto
- ✅ Se você já recebeu um nome, estilo de comunicação e persona, continue a usá-los enquanto desempenha este novo papel
- ✅ Engajamos em diálogo colaborativo, não comando-resposta
- ✅ Você traz pensamento estruturado e habilidades de facilitação, enquanto o usuário traz expertise de domínio e visão de produto
- ✅ Mantenha tom de conclusão colaborativa por todo o processo

### Regras Específicas do Passo:

- 🎯 Foque apenas na conclusão, próximos passos e orientação do projeto
- 🚫 PROIBIDO gerar novo conteúdo para o resumo de produto
- 💬 Abordagem: Conclusão sistemática com validação de qualidade e recomendações de próximos passos
- 📋 FINALIZE o documento e atualize o status do fluxo de trabalho adequadamente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Atualize o arquivo principal de status do fluxo de trabalho com informações de conclusão
- 📖 Sugira próximos passos potenciais de fluxo de trabalho para o usuário
- 🚫 NÃO carregue passos adicionais após este (este é o final)

## LIMITES DE CONTEXTO:

- Contexto disponível: Documento de resumo de produto completo de todos os passos anteriores, frontmatter do fluxo de trabalho mostra todos os passos concluídos
- Foco: Validação de conclusão, atualizações de status e orientação de próximos passos
- Limites: Nenhuma geração de novo conteúdo, apenas atividades de conclusão e encerramento
- Dependências: Todos os passos anteriores devem ser concluídos com conteúdo salvo no documento

## Sequência de Instruções (Não desvie, pule ou otimize)

### 1. Anunciar Conclusão do Fluxo de Trabalho

**Anúncio de Conclusão:**
"🎉 **Resumo de Produto Concluído, {{user_name}}!**

Colaborei com sucesso com você para criar um Resumo de Produto abrangente para {{project_name}}.

**O que realizamos:**

- ✅ Resumo Executivo com visão clara e declaração do problema
- ✅ Visão Central com definição da solução e diferenciadores únicos
- ✅ Usuários-Alvo com personas ricas e jornadas de usuário
- ✅ Métricas de Sucesso com resultados mensuráveis e objetivos de negócios
- ✅ Escopo MVP com conjunto de recursos focado e limites claros
- ✅ Visão Futura que inspira enquanto mantém o foco atual

**O Resumo de Produto completo está agora disponível em:** `{outputFile}`

Este resumo serve como a fundação para todas as atividades subsequentes de desenvolvimento de produto e decisões estratégicas."

### 2. Atualização de Status do Fluxo de Trabalho

**Gerenciamento de Arquivo de Status:**
Atualize o arquivo principal de status do fluxo de trabalho:

- Verifique se `{output_folder}/bmm-workflow-status.yaml` existe
- Se não, crie-o com estrutura básica
- Atualize workflow_status["product-brief"] = `{outputFile}`
- Adicione carimbo de data/hora de conclusão e metadados
- Salve o arquivo, preservando todos os comentários e estrutura

### 3. Verificação de Qualidade do Documento

**Validação de Completude:**
Realize validação final do resumo de produto:

- O resumo executivo comunica claramente a visão e o problema?
- Os usuários-alvo estão bem definidos com personas convincentes?
- As métricas de sucesso conectam o valor do usuário aos objetivos de negócios?
- O escopo do MVP é focado e realista?
- O resumo fornece direção clara para os próximos passos?

**Validação de Consistência:**

- Todas as seções se alinham com a declaração do problema central?
- O valor do usuário é consistentemente enfatizado por todo o documento?
- Os critérios de sucesso são rastreáveis às necessidades do usuário e objetivos de negócios?
- O escopo do MVP se alinha com o problema e a solução?

### 4. Sugerir Próximos Passos

**Próximo Fluxo de Trabalho Recomendado:**
Forneça orientação sobre próximos fluxos de trabalho lógicos:

1. `workflow prd` - Criar Documento de Requisitos de Produto detalhado
   - O resumo fornece fundação para requisitos detalhados
   - Personas de usuário informam mapeamento de jornada
   - Métricas de sucesso tornam-se critérios de aceitação específicos
   - Escopo do MVP torna-se especificações detalhadas de recursos

**Outros Próximos Passos Potenciais:**

2. `workflow create-ux-design` - Pesquisa e design de UX (pode rodar em paralelo com PRD)
3. `workflow domain-research` - Pesquisa profunda de mercado ou domínio (se necessário)

**Considerações Estratégicas:**

- O fluxo de trabalho de PRD baseia-se diretamente neste resumo para planejamento detalhado
- Considere a capacidade da equipe e prioridades imediatas
- Use o resumo para validar o conceito antes de se comprometer com trabalho detalhado
- O resumo pode guiar discussões iniciais de viabilidade técnica

### 5. Apresentar OPÇÕES DE MENU

**Confirmação de Conclusão:**
"**Seu Resumo de Produto para {{project_name}} está agora completo e pronto para a próxima fase!**

O resumo captura tudo o que é necessário para guiar o desenvolvimento subsequente do produto:

- Visão clara e definição do problema
- Compreensão profunda dos usuários-alvo
- Critérios de sucesso mensuráveis
- Escopo MVP focado com limites realistas
- Visão de longo prazo inspiradora

**Próximos Passos Sugeridos**

- Fluxo de trabalho de PRD para requisitos detalhados?
- Fluxo de trabalho de design de UX para planejamento de experiência do usuário?

**Resumo de Produto Concluído**"

#### Lógica de Tratamento de Menu:

- Visto que este é um passo de conclusão, não há continuação para outros passos do fluxo de trabalho
- O usuário pode fazer perguntas ou solicitar revisão do resumo concluído
- Forneça orientação sobre opções de próximo fluxo de trabalho quando solicitado
- Encerre a sessão do fluxo de trabalho graciosamente após confirmação de conclusão

#### REGRAS DE EXECUÇÃO:

- Este é um passo final com foco em conclusão
- Nenhum passo adicional de fluxo de trabalho para carregar após este
- O usuário pode solicitar revisão ou esclarecimento do resumo concluído
- Forneça orientação clara sobre opções de próximo fluxo de trabalho

## NOTA CRÍTICA DE CONCLUSÃO DO PASSO

APENAS QUANDO [confirmação de conclusão for fornecida e status do fluxo de trabalho atualizado], você então marcará o fluxo de trabalho como completo e encerrará a sessão graciosamente. Nenhum passo adicional é carregado após este passo final de conclusão.

---

## 🚨 MÉTRICAS DE SUCESSO/FALHA DO SISTEMA

### ✅ SUCESSO:

- Resumo de produto contém todas as seções essenciais com conteúdo colaborativo
- Todo o conteúdo colaborativo devidamente salvo no documento com frontmatter adequado
- Arquivo de status do fluxo de trabalho atualizado com informações de conclusão e carimbo de data/hora
- Orientação clara de próximos passos fornecida ao usuário com recomendações específicas de fluxo de trabalho
- Validação de qualidade do documento concluída com verificações de completude e consistência
- Usuário reconhece conclusão e entende as próximas opções disponíveis
- Fluxo de trabalho devidamente marcado como completo no rastreamento de status

### ❌ FALHA DO SISTEMA:

- Não atualizar o arquivo de status do fluxo de trabalho com informações de conclusão
- Faltar orientação clara de próximos passos para o usuário
- Não confirmar a completude do documento com o usuário
- Fluxo de trabalho não marcado adequadamente como completo no rastreamento de status
- Usuário não tem clareza sobre o que acontece a seguir ou opções disponíveis
- Problemas de qualidade do documento não identificados ou abordados

**Regra Mestra:** Pular passos, otimizar sequências ou não seguir instruções exatas é PROIBIDO e constitui FALHA DO SISTEMA.

## CONCLUSÃO FINAL DO FLUXO DE TRABALHO

Este resumo de produto está agora completo e serve como a fundação estratégica para todo o ciclo de vida do produto. Todo o trabalho subsequente de design, arquitetura e desenvolvimento deve remontar à visão, necessidades do usuário e critérios de sucesso documentados neste resumo.

**Parabéns por completar o Resumo de Produto para {{project_name}}!** 🎉
