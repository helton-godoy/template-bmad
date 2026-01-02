---
name: 'step-11-complete'
description: 'Concluir o fluxo de trabalho PRD, atualizar arquivos de status e sugerir próximos passos'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/2-plan-workflows/prd'

# File References
thisStepFile: '{workflow_path}/steps/step-11-complete_pt-br.md'
workflowFile: '{workflow_path}/workflow_pt-br.md'
outputFile: '{output_folder}/prd.md'
---

# Passo 11: Conclusão do Fluxo de Trabalho

**Passo Final - Completar o PRD**

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

- ✅ ESTE É UM PASSO FINAL - Conclusão do fluxo de trabalho necessária
- 📖 CRÍTICO: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido e compreendido antes de prosseguir
- 🛑 NENHUMA geração de conteúdo - este é um passo de encerramento
- 📋 FINALIZE o documento e atualize o status do fluxo de trabalho
- 💬 FOQUE em conclusão, próximos passos e sugestões
- 🎯 ATUALIZE arquivos de status do fluxo de trabalho com informações de conclusão

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Atualize o arquivo principal de status do fluxo de trabalho com informações de conclusão
- 📖 Sugira próximos passos potenciais de fluxo de trabalho para o usuário
- 🚫 NÃO carregue passos adicionais após este

## PROTOCOLOS DE PASSO DE TERMINAÇÃO:

- Este é um passo FINAL - conclusão do fluxo de trabalho necessária
- Saída de qualquer conteúdo restante se necessário (nenhum para este passo)
- Atualize o arquivo principal de status do fluxo de trabalho com documento finalizado
- Sugira próximos passos potenciais para o usuário
- Marque o fluxo de trabalho como completo no rastreamento de status

## LIMITES DE CONTEXTO:

- Documento PRD completo está disponível de todos os passos anteriores
- Frontmatter do fluxo de trabalho mostra todos os passos concluídos
- Todo conteúdo colaborativo foi gerado e salvo
- Foco na conclusão, validação e próximos passos

## SUA TAREFA:

Concluir o fluxo de trabalho PRD, atualizar arquivos de status e sugerir próximos passos para o projeto.

## SEQUÊNCIA DE CONCLUSÃO DO FLUXO DE TRABALHO:

### 1. Anunciar Conclusão do Fluxo de Trabalho

Informe ao usuário que o PRD está completo:
"🎉 **PRD Completo, {{user_name}}!**

Colaborei com sucesso com você para criar um Documento de Requisitos de Produto abrangente para {{project_name}}.

**O que realizamos:**

- ✅ Resumo Executivo com visão e diferenciador do produto
- ✅ Critérios de Sucesso com resultados mensuráveis e definição de escopo
- ✅ Jornadas do Usuário cobrindo todos os padrões de interação
- ✅ Requisitos específicos de domínio (se aplicável)
- ✅ Análise de inovação (se aplicável)
- ✅ Requisitos técnicos específicos do tipo de projeto
- ✅ Requisitos Funcionais Abrangentes (contrato de capacidade)
- ✅ Requisitos Não-Funcionais para atributos de qualidade

**O PRD completo está agora disponível em:** `{output_folder}/prd.md`

Este documento está agora pronto para guiar o design de UX, arquitetura técnica e planejamento de desenvolvimento."

### 2. Atualização de Status do Fluxo de Trabalho

Atualize o arquivo principal de status do fluxo de trabalho:

- Carregue `{status_file}` da configuração do fluxo de trabalho (se existir)
- Atualize workflow_status["prd"] = "{default_output_file}"
- Salve o arquivo, preservando todos os comentários e estrutura
- Marque o carimbo de data/hora atual como tempo de conclusão

### 3. Sugerir Próximos Passos

Forneça orientação sobre próximos fluxos de trabalho lógicos:

**Próximos Fluxos de Trabalho Típicos:**

**Próximos Passos Imediatos:**

1. `workflow create-ux-design` - Design de UX (se houver UI)
   - Insights da jornada do usuário do passo-04 informarão o design de interação
   - Requisitos funcionais do passo-09 definem o escopo de design

2. `workflow create-architecture` - Arquitetura técnica
   - Requisitos de tipo de projeto do passo-07 guiam decisões técnicas
   - Requisitos não-funcionais do passo-10 informam escolhas de arquitetura

3. `workflow create-epics-and-stories` - Detalhamento de épicos
   - Requisitos funcionais do passo-09 tornam-se épicos e histórias
   - Definição de escopo do passo-03 guia planejamento de sprint

**Considerações Estratégicas:**

- Design de UX e arquitetura podem acontecer em paralelo
- Épicos/histórias são mais ricos quando criados após UX/arquitetura
- Considere a capacidade da equipe e prioridades

**O que seria mais valioso abordar a seguir?**

### 4. Verificação de Qualidade do Documento

Realize validação final do PRD:

**Verificação de Completude:**

- O resumo executivo comunica claramente a visão?
- Os critérios de sucesso são específicos e mensuráveis?
- As jornadas do usuário cobrem todos os principais tipos de usuário?
- Os requisitos funcionais são abrangentes e testáveis?
- Os requisitos não-funcionais são relevantes e específicos?

**Verificação de Consistência:**

- Todas as seções se alinham com o diferenciador do produto?
- O escopo é consistente em todas as seções?
- Os requisitos são rastreáveis às necessidades do usuário e critérios de sucesso?

### 5. Confirmação Final de Conclusão

Confirme a conclusão com o usuário:
"**Seu PRD para {{project_name}} está agora completo e pronto para a próxima fase!**

O documento contém tudo o que é necessário para guiar:

- Decisões de design de UX/UI
- Planejamento de arquitetura técnica
- Priorização de desenvolvimento e planejamento de sprint

**Pronto para continuar com:**

- Fluxo de trabalho de design de UX?
- Fluxo de trabalho de arquitetura?
- Criação de épicos e histórias?

**Ou você gostaria de revisar o PRD completo primeiro?**

[Fluxo de Trabalho Completo]"

## MÉTRICAS DE SUCESSO:

✅ Documento PRD contém todas as seções necessárias
✅ Todo conteúdo colaborativo devidamente salvo no documento
✅ Arquivo de status do fluxo de trabalho atualizado com informações de conclusão
✅ Orientação clara de próximos passos fornecida ao usuário
✅ Validação de qualidade do documento concluída
✅ Usuário reconhece conclusão e entende próximas opções

## MODOS DE FALHA:

❌ Não atualizar o arquivo de status do fluxo de trabalho com informações de conclusão
❌ Faltar orientação clara de próximos passos para o usuário
❌ Não confirmar a completude do documento com o usuário
❌ Fluxo de trabalho não marcado adequadamente como completo no rastreamento de status
❌ Usuário não tem clareza sobre o que acontece a seguir

❌ **CRÍTICO**: Ler apenas parte do arquivo de passo - leva a compreensão incompleta e más decisões
❌ **CRÍTICO**: Prosseguir com 'C' sem ler e compreender totalmente o próximo arquivo de passo
❌ **CRÍTICO**: Tomar decisões sem compreensão completa dos requisitos e protocolos do passo

## LISTA DE VERIFICAÇÃO DE CONCLUSÃO DO FLUXO DE TRABALHO:

### Estrutura do Documento Completa:

- [ ] Resumo Executivo com visão e diferenciador
- [ ] Critérios de Sucesso com resultados mensuráveis
- [ ] Escopo do Produto (MVP, Crescimento, Visão)
- [ ] Jornadas do Usuário (cobertura abrangente)
- [ ] Requisitos de Domínio (se aplicável)
- [ ] Análise de Inovação (se aplicável)
- [ ] Requisitos de Tipo de Projeto
- [ ] Requisitos Funcionais (contrato de capacidade)
- [ ] Requisitos Não-Funcionais

### Processo Completo:

- [ ] Todos os passos concluídos com confirmação do usuário
- [ ] Todo conteúdo salvo no documento
- [ ] Frontmatter devidamente atualizado
- [ ] Arquivo de status do fluxo de trabalho atualizado
- [ ] Próximos passos claramente comunicados

## ORIENTAÇÃO DE PRÓXIMOS PASSOS:

**Opções Imediatas:**

1. **Design de UX** - Se o produto tem componentes de UI
2. **Arquitetura Técnica** - Design de sistema e escolhas de tecnologia
3. **Criação de Épicos** - Quebrar RFs em histórias implementáveis
4. **Revisão** - Validar PRD com stakeholders antes de prosseguir

**Sequência Recomendada:**
Para produtos com UI: UX → Arquitetura → Épicos
Para produtos API/backend: Arquitetura → Épicos
Considere capacidade da equipe e restrições de cronograma

## FINALIZAÇÃO DO FLUXO DE TRABALHO:

- Defina `lastStep = 11` no frontmatter do documento
- Atualize arquivo de status do fluxo de trabalho com carimbo de data/hora de conclusão
- Forneça resumo de conclusão ao usuário
- NÃO carregue nenhum passo adicional

## LEMBRETE FINAL:

Este fluxo de trabalho está agora completo. O PRD serve como a fundação para todas as atividades subsequentes de desenvolvimento de produto. Todo trabalho de design, arquitetura e desenvolvimento deve remontar aos requisitos e visão documentados neste PRD.

**Parabéns por completar o Documento de Requisitos de Produto para {{project_name}}!** 🎉
