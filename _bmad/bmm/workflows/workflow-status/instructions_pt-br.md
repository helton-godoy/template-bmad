# Verificação de Status do Fluxo de Trabalho - Serviço Multi-Modo

<critical>O mecanismo de execução do fluxo de trabalho é governado por: {project-root}/_bmad/core/tasks/workflow.xml</critical>
<critical>Você DEVE já ter carregado e processado: {project-root}/_bmad/bmm/workflows/workflow-status/workflow.yaml</critical>
<critical>Este fluxo de trabalho opera em múltiplos modos: interactive (padrão), validate, data, init-check, update</critical>
<critical>Outros fluxos de trabalho podem chamar isso como um serviço para evitar duplicar lógica de status</critical>
<critical>⚠️ ABSOLUTAMENTE NENHUMA ESTIMATIVA DE TEMPO - NUNCA mencione horas, dias, semanas, meses ou QUALQUER previsão baseada em tempo. A IA mudou fundamentalmente a velocidade de desenvolvimento - o que antes levava equipes semanas/meses agora pode ser feito por uma pessoa em horas. NÃO dê NENHUMA estimativa de tempo.</critical>

<workflow>

<step n="0" goal="Determinar modo de execução">
  <action>Verificar parâmetro {{mode}} passado pelo fluxo de trabalho chamador</action>
  <action>Modo padrão = "interactive" se não especificado</action>

  <check if="mode == interactive">
    <action>Continuar para Passo 1 para fluxo normal de verificação de status</action>
  </check>

  <check if="mode == validate">
    <action>Pular para Passo 10 para serviço de validação de fluxo de trabalho</action>
  </check>

  <check if="mode == data">
    <action>Pular para Passo 20 para serviço de extração de dados</action>
  </check>

  <check if="mode == init-check">
    <action>Pular para Passo 30 para verificação simples de init</action>
  </check>

  <check if="mode == update">
    <action>Pular para Passo 40 para serviço de atualização de status</action>
  </check>
</step>

<step n="1" goal="Verificar por arquivo de status">
<action>Pesquisar {output_folder}/ por arquivo: bmm-workflow-status.yaml</action>

<check if="no status file found">
  <output>Nenhum status de fluxo de trabalho encontrado.</output>
  <ask>Gostaria de executar Workflow Init agora? (s/n)</ask>

  <check if="response == s OR response == sim">
    <action>Lançando workflow-init para configurar seu rastreamento de projeto...</action>
    <invoke-workflow path="{project-root}/_bmad/bmm/workflows/workflow-status/init/workflow.yaml"></invoke-workflow>
    <action>Sair do fluxo de trabalho e deixar workflow-init assumir</action>
  </check>

  <check if="else">
    <output>Nenhum arquivo de status de fluxo de trabalho. Execute workflow-init quando estiver pronto para habilitar rastreamento de progresso.</output>
    <action>Sair do fluxo de trabalho</action>
  </check>
</check>

<check if="status file found">
  <action>Continuar para passo 2</action>
</check>
</step>

<step n="2" goal="Ler e analisar status">
<action>Ler bmm-workflow-status.yaml</action>
<action>Analisar arquivo YAML e extrair metadados de comentários e campos:</action>

Analisar estes campos de comentários e metadados YAML:

- project (do campo YAML)
- project_type (do campo YAML)
- project_level (do campo YAML)
- field_type (do campo YAML)
- workflow_path (do campo YAML)

<action>Analisar seção workflow_status:</action>

- Extrair todas as entradas de fluxo de trabalho com seus status
- Identificar fluxos de trabalho concluídos (status = caminho do arquivo)
- Identificar fluxos de trabalho pendentes (status = required/optional/recommended/conditional)
- Identificar fluxos de trabalho pulados (status = skipped)

<action>Determinar estado atual:</action>

- Encontrar primeiro fluxo de trabalho com status != caminho do arquivo e != skipped
- Este é o PRÓXIMO fluxo de trabalho a ser trabalhado
- Consultar agente e comando do arquivo de caminho do fluxo de trabalho
  </step>

<step n="3" goal="Exibir status atual e opções">
<action>Carregar arquivo de caminho de fluxo de trabalho baseado no campo workflow_path</action>
<action>Identificar fase atual a partir do próximo fluxo de trabalho a ser feito</action>
<action>Construir lista de fluxos de trabalho concluídos, pendentes e opcionais</action>
<action>Para cada fluxo de trabalho, consultar seu agente do arquivo de caminho</action>

<output>
## 📊 Status Atual

**Projeto:** {{project}} (Nível {{project_level}} {{project_type}})

**Caminho:** {{workflow_path}}

**Progresso:**

{{#each phases}}
{{phase_name}}:
{{#each workflows_in_phase}}

- {{workflow_name}} ({{agent}}): {{status_display}}
  {{/each}}
  {{/each}}

## 🎯 Próximos Passos

**Próximo Fluxo de Trabalho:** {{next_workflow_name}}

**Agente:** {{next_agent}}

**Comando:** /bmad:bmm:workflows:{{next_workflow_id}}

{{#if optional_workflows_available}}
**Fluxos de Trabalho Opcionais Disponíveis:**
{{#each optional_workflows}}

- {{workflow_name}} ({{agent}}) - {{status}}
  {{/each}}
  {{/if}}
  </output>
  </step>

<step n="4" goal="Oferecer ações">
<ask>O que você gostaria de fazer?

1. **Começar próximo fluxo de trabalho** - {{next_workflow_name}} ({{next_agent}})
   {{#if optional_workflows_available}}
2. **Executar fluxo de trabalho opcional** - Escolher entre opções disponíveis
   {{/if}}
3. **Ver YAML de status completo** - Ver arquivo de status completo
4. **Atualizar status do fluxo de trabalho** - Marcar um fluxo de trabalho como concluído ou pulado
5. **Sair** - Retornar ao agente

Sua escolha:</ask>

<action>Lidar com seleção do usuário baseada nas opções disponíveis</action>

<check if="choice == 1">
  <output>Pronto para executar {{next_workflow_name}}!

**Comando:** /bmad:bmm:workflows:{{next_workflow_id}}

**Agente:** Carregar agente {{next_agent}} primeiro

{{#if next_agent !== current_agent}}
Dica: Comece um novo chat e carregue o agente {{next_agent}} antes de executar este fluxo de trabalho.
{{/if}}
</output>
</check>

<check if="choice == 2 AND optional_workflows_available">
  <ask>Qual fluxo de trabalho opcional?
{{#each optional_workflows numbered}}
{{number}}. {{workflow_name}} ({{agent}})
{{/each}}

Sua escolha:</ask>
<action>Exibir comando e agente do fluxo de trabalho selecionado</action>
</check>

<check if="choice == 3">
  <action>Exibir conteúdo completo do arquivo bmm-workflow-status.yaml</action>
</check>

<check if="choice == 4">
  <ask>O que você gostaria de atualizar?

1. Marcar um fluxo de trabalho como **concluído** (fornecer caminho do arquivo)
2. Marcar um fluxo de trabalho como **pulado**

Sua escolha:</ask>

  <check if="update_choice == 1">
    <ask>Qual fluxo de trabalho? (Insira ID do fluxo de trabalho como 'prd' ou 'create-architecture')</ask>
    <ask>Caminho do arquivo criado? (e.g., docs/prd.md)</ask>
    <critical>APENAS escreva o caminho do arquivo como o valor do status - nenhum outro texto, notas ou metadados</critical>
    <action>Atualizar workflow_status no arquivo YAML: {{workflow_id}}: {{file_path}}</action>
    <action>Salvar arquivo YAML atualizado preservando TODA a estrutura e comentários</action>
    <output>✅ Atualizado {{workflow_id}} para concluído: {{file_path}}</output>
  </check>

  <check if="update_choice == 2">
    <ask>Qual fluxo de trabalho pular? (Insira ID do fluxo de trabalho)</ask>
    <action>Atualizar workflow_status no arquivo YAML: {{workflow_id}}: skipped</action>
    <action>Salvar arquivo YAML atualizado</action>
    <output>✅ Marcado {{workflow_id}} como pulado</output>
  </check>
</check>
</step>

<!-- ============================================= -->
<!-- MODOS DE SERVIÇO - Chamados por outros fluxos -->
<!-- ============================================= -->

<step n="10" goal="Modo de validação - Verificar se fluxo chamador deve prosseguir">
<action>Ler {output_folder}/bmm-workflow-status.yaml se existir</action>

<check if="status file not found">
  <template-output>status_exists = false</template-output>
  <template-output>should_proceed = true</template-output>
  <template-output>warning = "Nenhum arquivo de status encontrado. Executando sem rastreamento de progresso."</template-output>
  <template-output>suggestion = "Considere executar workflow-init primeiro para rastreamento de progresso"</template-output>
  <action>Retornar ao fluxo de trabalho chamador</action>
</check>

<check if="status file found">
  <action>Analisar arquivo YAML para extrair metadados do projeto e workflow_status</action>
  <action>Carregar arquivo de caminho do fluxo de trabalho do campo workflow_path</action>
  <action>Encontrar primeiro fluxo de trabalho não concluído em workflow_status (próximo fluxo)</action>
  <action>Verificar se {{calling_workflow}} corresponde ao próximo fluxo ou está na lista de fluxos</action>

<template-output>status_exists = true</template-output>
<template-output>project_level = {{project_level}}</template-output>
<template-output>project_type = {{project_type}}</template-output>
<template-output>field_type = {{field_type}}</template-output>
<template-output>next_workflow = {{next_workflow_id}}</template-output>

  <check if="calling_workflow == next_workflow">
    <template-output>should_proceed = true</template-output>
    <template-output>warning = ""</template-output>
    <template-output>suggestion = "Prosseguindo com próximo passo planejado"</template-output>
  </check>

  <check if="calling_workflow in workflow_status list">
    <action>Verificar o status de calling_workflow no YAML</action>

    <check if="status is file path">
      <template-output>should_proceed = true</template-output>
      <template-output>warning = "⚠️ Fluxo de trabalho já concluído: {{calling_workflow}}"</template-output>
      <template-output>suggestion = "Este fluxo de trabalho já foi concluído. Reexecutar irá sobrescrever: {{status}}"</template-output>
    </check>

    <check if="status is optional/recommended">
      <template-output>should_proceed = true</template-output>
      <template-output>warning = "Executando fluxo de trabalho opcional {{calling_workflow}}"</template-output>
      <template-output>suggestion = "Isto é opcional. Esperado próximo: {{next_workflow}}"</template-output>
    </check>

    <check if="status is required but not next">
      <template-output>should_proceed = true</template-output>
      <template-output>warning = "⚠️ Fora de sequência: Esperado {{next_workflow}}, executando {{calling_workflow}}"</template-output>
      <template-output>suggestion = "Considere executar {{next_workflow}} em vez disso, ou continue se intencional"</template-output>
    </check>

  </check>

  <check if="calling_workflow NOT in workflow_status list">
    <template-output>should_proceed = true</template-output>
    <template-output>warning = "⚠️ Fluxo de trabalho desconhecido: {{calling_workflow}} não está no caminho do fluxo de trabalho"</template-output>
    <template-output>suggestion = "Este fluxo de trabalho não é parte do caminho definido para este projeto"</template-output>
  </check>

<template-output>status_file_path = {{path to bmm-workflow-status.yaml}}</template-output>
</check>

<action>Retornar controle ao fluxo de trabalho chamador com todas as saídas de modelo</action>
</step>

<step n="20" goal="Modo de dados - Extrair informações específicas">
<action>Ler {output_folder}/bmm-workflow-status.yaml se existir</action>

<check if="status file not found">
  <template-output>status_exists = false</template-output>
  <template-output>error = "Nenhum arquivo de status para extrair dados"</template-output>
  <action>Retornar ao fluxo de trabalho chamador</action>
</check>

<check if="status file found">
  <action>Analisar arquivo YAML completamente</action>
  <template-output>status_exists = true</template-output>

  <check if="data_request == project_config">
    <template-output>project_name = {{project}}</template-output>
    <template-output>project_type = {{project_type}}</template-output>
    <template-output>project_level = {{project_level}}</template-output>
    <template-output>field_type = {{field_type}}</template-output>
    <template-output>workflow_path = {{workflow_path}}</template-output>
  </check>

  <check if="data_request == workflow_status">
    <action>Analisar seção workflow_status e retornar todos os pares workflow: status</action>
    <template-output>workflow_status = {{workflow_status_object}}</template-output>
    <action>Calcular estatísticas de conclusão:</action>
    <template-output>total_workflows = {{count all workflows}}</template-output>
    <template-output>completed_workflows = {{count file path statuses}}</template-output>
    <template-output>pending_workflows = {{count required/optional/etc}}</template-output>
    <template-output>skipped_workflows = {{count skipped}}</template-output>
  </check>

  <check if="data_request == all">
    <action>Retornar todos os campos analisados como saídas de modelo</action>
    <template-output>project = {{project}}</template-output>
    <template-output>project_type = {{project_type}}</template-output>
    <template-output>project_level = {{project_level}}</template-output>
    <template-output>field_type = {{field_type}}</template-output>
    <template-output>workflow_path = {{workflow_path}}</template-output>
    <template-output>workflow_status = {{workflow_status_object}}</template-output>
    <template-output>generated = {{generated}}</template-output>
  </check>

<template-output>status_file_path = {{path to bmm-workflow-status.yaml}}</template-output>
</check>

<action>Retornar controle ao fluxo de trabalho chamador com dados solicitados</action>
</step>

<step n="30" goal="Modo Init-check - Verificação simples de existência">
<action>Verificar se {output_folder}/bmm-workflow-status.yaml existe</action>

<check if="exists">
  <template-output>status_exists = true</template-output>
  <template-output>suggestion = "Arquivo de status encontrado. Pronto para prosseguir."</template-output>
</check>

<check if="not exists">
  <template-output>status_exists = false</template-output>
  <template-output>suggestion = "Sem arquivo de status. Execute workflow-init para criar um (opcional para rastreamento de progresso)"</template-output>
</check>

<action>Retornar imediatamente ao fluxo de trabalho chamador</action>
</step>

<step n="40" goal="Modo de atualização - Atualizações centralizadas de arquivo de status">
<action>Ler {output_folder}/bmm-workflow-status.yaml</action>

<check if="status file not found">
  <template-output>success = false</template-output>
  <template-output>error = "Nenhum arquivo de status encontrado. Não é possível atualizar."</template-output>
  <action>Retornar ao fluxo de trabalho chamador</action>
</check>

<check if="status file found">
  <action>Analisar arquivo YAML completamente</action>
  <action>Carregar arquivo de caminho do fluxo de trabalho do campo workflow_path</action>
  <action>Verificar parâmetro {{action}} para determinar tipo de atualização</action>

  <!-- ============================================= -->
  <!-- AÇÃO: complete_workflow -->
  <!-- ============================================= -->
  <check if="action == complete_workflow">
    <action>Obter parâmetro {{workflow_id}} (obrigatório)</action>
    <action>Obter parâmetro {{output_file}} (obrigatório - caminho para arquivo criado)</action>

    <critical>APENAS escreva o caminho do arquivo como o valor do status - nenhum outro texto, notas ou metadados</critical>
    <action>Atualizar status do fluxo de trabalho no YAML:</action>
    - Na seção workflow_status, atualizar: {{workflow_id}}: {{output_file}}

    <action>Encontrar {{workflow_id}} no YAML de caminho carregado</action>
    <action>Determinar próximo fluxo de trabalho da sequência de caminho</action>
    <action>Encontrar primeiro fluxo de trabalho em workflow_status com status != caminho do arquivo e != skipped</action>

    <action>Salvar arquivo YAML atualizado preservando TODA a estrutura e comentários</action>

    <template-output>success = true</template-output>
    <template-output>next_workflow = {{determined next workflow}}</template-output>
    <template-output>next_agent = {{determined next agent from path file}}</template-output>
    <template-output>completed_workflow = {{workflow_id}}</template-output>
    <template-output>output_file = {{output_file}}</template-output>

  </check>

  <!-- ============================================= -->
  <!-- AÇÃO: skip_workflow -->
  <!-- ============================================= -->
  <check if="action == skip_workflow">
    <action>Obter parâmetro {{workflow_id}} (obrigatório)</action>

    <action>Atualizar status do fluxo de trabalho no YAML:</action>
    - Na seção workflow_status, atualizar: {{workflow_id}}: skipped

    <action>Salvar arquivo YAML atualizado</action>

    <template-output>success = true</template-output>
    <template-output>skipped_workflow = {{workflow_id}}</template-output>

  </check>

  <!-- ============================================= -->
  <!-- Ação desconhecida -->
  <!-- ============================================= -->
  <check if="action not recognized">
    <template-output>success = false</template-output>
    <template-output>error = "Ação desconhecida: {{action}}. Ações válidas: complete_workflow, skip_workflow"</template-output>
  </check>

</check>

<action>Retornar controle ao fluxo de trabalho chamador com saídas de modelo</action>
</step>

</workflow>
