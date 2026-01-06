# Corrigir Curso - Instruções de Gestão de Mudança de Sprint

<critical>O mecanismo de execução do fluxo de trabalho é governado por: {project-root}/_bmad/core/tasks/workflow.xml</critical>
<critical>Você DEVE já ter carregado e processado: {project-root}/_bmad/bmm/workflows/4-implementation/correct-course/workflow.yaml</critical>
<critical>Comunique todas as respostas em {communication_language} e a linguagem DEVE ser adaptada para {user_skill_level}</critical>
<critical>Gere todos os documentos em {document_output_language}</critical>

<critical>SAÍDA DE DOCUMENTO: Épicos, histórias ou seções de PRD atualizados. Mudanças claras e acionáveis. O nível de habilidade do usuário ({user_skill_level}) afeta APENAS o estilo de conversa, não as atualizações de documentos.</critical>

<workflow>

<step n="1" goal="Inicializar Navegação de Mudança">
  <action>Confirmar o gatilho da mudança e coletar a descrição do usuário sobre o problema</action>
  <action>Perguntar: "Qual problema ou mudança específica foi identificada que requer navegação?"</action>
  <action>Verificar acesso aos documentos necessários do projeto:</action>
    - PRD (Documento de Requisitos do Produto)
    - Épicos e Histórias Atuais
    - Documentação de Arquitetura
    - Especificações de UI/UX
  <action>Perguntar ao usuário pela preferência de modo:</action>
    - **Incremental** (recomendado): Refinar cada edição colaborativamente
    - **Lote**: Apresentar todas as mudanças de uma vez para revisão
  <action>Armazenar a seleção de modo para uso durante todo o fluxo de trabalho</action>

<action if="change trigger is unclear">PARAR: "Não é possível navegar pela mudança sem um entendimento claro do problema desencadeador. Por favor, forneça detalhes específicos sobre o que precisa mudar e por quê."</action>

<action if="core documents are unavailable">PARAR: "Preciso de acesso aos documentos do projeto (PRD, Épicos, Arquitetura, UI/UX) para avaliar o impacto da mudança. Por favor, certifique-se de que estes documentos estejam acessíveis."</action>
</step>

<step n="0.5" goal="Descobrir e carregar documentos do projeto">
  <invoke-protocol name="discover_inputs" />
  <note>Após a descoberta, estas variáveis de conteúdo estão disponíveis: {prd_content}, {epics_content}, {architecture_content}, {ux_design_content}, {tech_spec_content}, {document_project_content}</note>
</step>

<step n="2" goal="Executar Checklist de Análise de Mudança">
  <action>Carregar e executar a análise sistemática de: {checklist}</action>
  <action>Trabalhar através de cada seção do checklist interativamente com o usuário</action>
  <action>Registrar status para cada item do checklist:</action>
    - [x] Feito - Item completado com sucesso
    - [N/A] Pular - Item não aplicável a esta mudança
    - [!] Ação-necessária - Item requer atenção ou acompanhamento
  <action>Manter notas contínuas de descobertas e impactos descobertos</action>
  <action>Apresentar progresso do checklist após cada seção principal</action>

<action if="checklist cannot be completed">Identificar problemas bloqueantes e trabalhar com o usuário para resolver antes de continuar</action>
</step>

<step n="3" goal="Rascunhar Propostas de Mudança Específicas">
<action>Com base nas descobertas do checklist, criar propostas de edição explícitas para cada artefato identificado</action>

<action>Para mudanças de História:</action>

- Mostrar formato de texto antigo → novo
- Incluir ID da história e seção sendo modificada
- Fornecer justificativa para cada mudança
- Exemplo de formato:

  ```
  História: [STORY-123] Autenticação de Usuário
  Seção: Critérios de Aceite

  ANTIGO:
  - Usuário pode fazer login com email/senha

  NOVO:
  - Usuário pode fazer login com email/senha
  - Usuário pode habilitar 2FA via aplicativo autenticador

  Justificativa: Requisito de segurança identificado durante implementação
  ```

<action>Para modificações de PRD:</action>

- Especificar seções exatas para atualizar
- Mostrar conteúdo atual e mudanças propostas
- Explicar impacto no escopo MVP e requisitos

<action>Para mudanças de Arquitetura:</action>

- Identificar componentes afetados, padrões ou escolhas de tecnologia
- Descrever atualizações de diagrama necessárias
- Notar quaisquer efeitos cascata em outros componentes

<action>Para atualizações de especificação UI/UX:</action>

- Referenciar telas ou componentes específicos
- Mostrar mudanças de wireframe ou fluxo necessárias
- Conectar mudanças ao impacto na experiência do usuário

<check if="mode is Incremental">
  <action>Apresentar cada proposta de edição individualmente</action>
  <ask>Revisar e refinar esta mudança? Opções: Aprovar [a], Editar [e], Pular [s]</ask>
  <action>Iterar em cada proposta com base no feedback do usuário</action>
</check>

<action if="mode is Batch">Coletar todas as propostas de edição e apresentar juntas no final do passo</action>

</step>

<step n="4" goal="Gerar Proposta de Mudança de Sprint">
<action>Compilar documento abrangente de Proposta de Mudança de Sprint com as seguintes seções:</action>

<action>Seção 1: Resumo do Problema</action>

- Declaração clara do problema descrevendo o que desencadeou a mudança
- Contexto sobre quando/como o problema foi descoberto
- Evidência ou exemplos demonstrando o problema

<action>Seção 2: Análise de Impacto</action>

- Impacto no Épico: Quais épicos são afetados e como
- Impacto na História: Histórias atuais e futuras exigindo mudanças
- Conflitos de Artefatos: Documentos de PRD, Arquitetura, UI/UX precisando de atualizações
- Impacto Técnico: Código, infraestrutura ou implicações de implantação

<action>Seção 3: Abordagem Recomendada</action>

- Apresentar caminho escolhido da avaliação do checklist:
  - Ajuste Direto: Modificar/adicionar histórias dentro do plano existente
  - Possível Reversão: Reverter trabalho concluído para simplificar resolução
  - Revisão de MVP: Reduzir escopo ou modificar metas
- Fornecer justificativa clara para recomendação
- Incluir estimativa de esforço, avaliação de risco e impacto no cronograma

<action>Seção 4: Propostas de Mudança Detalhadas</action>

- Incluir todas as propostas de edição refinadas do Passo 3
- Agrupar por tipo de artefato (Histórias, PRD, Arquitetura, UI/UX)
- Garantir que cada mudança inclua antes/depois e justificativa

<action>Seção 5: Entrega para Implementação</action>

- Categorizar escopo da mudança:
  - Menor: Implementação direta pela equipe dev
  - Moderada: Reorganização do backlog necessária (PO/SM)
  - Maior: Replanejamento fundamental necessário (PM/Arquiteto)
- Especificar destinatários da entrega e suas responsabilidades
- Definir critérios de sucesso para implementação

<action>Apresentar Proposta de Mudança de Sprint completa para o usuário</action>
<action>Escrever documento de Proposta de Mudança de Sprint para {default_output_file}</action>
<ask>Revisar proposta completa. Continuar [c] ou Editar [e]?</ask>
</step>

<step n="5" goal="Finalizar e Encaminhar para Implementação">
<action>Obter aprovação explícita do usuário para a proposta completa</action>
<ask>Você aprova esta Proposta de Mudança de Sprint para implementação? (sim/não/revisar)</ask>

<check if="no or revise">
  <action>Coletar feedback específico sobre o que precisa de ajuste</action>
  <action>Retornar ao passo apropriado para abordar preocupações</action>
  <goto step="3">Se mudanças necessárias para editar propostas</goto>
  <goto step="4">Se mudanças necessárias para estrutura geral da proposta</goto>

</check>

<check if="yes the proposal is approved by the user">
  <action>Finalizar documento de Proposta de Mudança de Sprint</action>
  <action>Determinar classificação de escopo de mudança:</action>

- **Menor**: Pode ser implementado diretamente pela equipe de desenvolvimento
- **Moderada**: Requer reorganização do backlog e coordenação PO/SM
- **Maior**: Precisa de replanejamento fundamental com envolvimento de PM/Arquiteto

<action>Fornecer entrega apropriada com base no escopo:</action>

</check>

<check if="Minor scope">
  <action>Encaminhar para: Equipe de desenvolvimento para implementação direta</action>
  <action>Entregáveis: Propostas de edição finalizadas e tarefas de implementação</action>
</check>

<check if="Moderate scope">
  <action>Encaminhar para: Agentes Product Owner / Scrum Master</action>
  <action>Entregáveis: Proposta de Mudança de Sprint + plano de reorganização do backlog</action>
</check>

<check if="Major scope">
  <action>Encaminhar para: Gerente de Produto / Arquiteto de Solução</action>
  <action>Entregáveis: Proposta de Mudança de Sprint Completa + aviso de escalonamento</action>

<action>Confirmar conclusão da entrega e próximos passos com o usuário</action>
<action>Documentar entrega no log de execução do fluxo de trabalho</action>
</check>

</step>

<step n="6" goal="Conclusão do Fluxo de Trabalho">
<action>Resumir execução do fluxo de trabalho:</action>
  - Problema abordado: {{change_trigger}}
  - Escopo da mudança: {{scope_classification}}
  - Artefatos modificados: {{list_of_artifacts}}
  - Encaminhado para: {{handoff_recipients}}

<action>Confirmar todos os entregáveis produzidos:</action>

- Documento de Proposta de Mudança de Sprint
- Propostas de edição específicas com antes/depois
- Plano de entrega de implementação

<action>Relatar conclusão do fluxo de trabalho ao usuário com mensagem personalizada: "✅ Fluxo de trabalho Corrigir Curso completo, {user_name}!"</action>
<action>Lembrar usuário dos critérios de sucesso e próximos passos para equipe de implementação</action>
</step>

</workflow>
