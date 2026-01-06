# Roteador de Fluxo de Trabalho de Documentação de Projeto

<critical>O mecanismo de execução do fluxo de trabalho é governado por: {project-root}/_bmad/core/tasks/workflow.xml</critical>
<critical>Você DEVE já ter carregado e processado: {project-root}/_bmad/bmm/workflows/document-project/workflow.yaml</critical>
<critical>Comunique todas as respostas em {communication_language}</critical>

<workflow>

<critical>Este roteador determina o modo de fluxo de trabalho e delega para sub-fluxos especializados</critical>

<step n="1" goal="Validar fluxo de trabalho e obter informações do projeto">

<invoke-workflow path="{project-root}/_bmad/bmm/workflows/workflow-status">
  <param>mode: data</param>
  <param>data_request: project_config</param>
</invoke-workflow>

<check if="status_exists == false">
  <output>{{suggestion}}</output>
  <output>Nota: Fluxo de trabalho de documentação pode rodar autônomo. Continuando sem rastreamento de progresso.</output>
  <action>Definir standalone_mode = true</action>
  <action>Definir status_file_found = false</action>
</check>

<check if="status_exists == true">
  <action>Armazenar {{status_file_path}} para atualizações posteriores</action>
  <action>Definir status_file_found = true</action>

  <!-- Extrair brownfield/greenfield de dados de status -->
  <check if="field_type == 'greenfield'">
    <output>Nota: Este é um projeto greenfield. Fluxo de trabalho de documentação é tipicamente para projetos brownfield.</output>
    <ask>Continuar de qualquer maneira para documentar artefatos de planejamento? (s/n)</ask>
    <check if="n">
      <action>Sair do fluxo de trabalho</action>
    </check>
  </check>

  <!-- Agora validar sequenciamento -->
  <invoke-workflow path="{project-root}/_bmad/bmm/workflows/workflow-status">
    <param>mode: validate</param>
    <param>calling_workflow: document-project</param>
  </invoke-workflow>

  <check if="warning != ''">
    <output>{{warning}}</output>
    <output>Nota: Isso pode ser auto-invocado por prd para documentação brownfield.</output>
    <ask>Continuar com documentação? (s/n)</ask>
    <check if="n">
      <output>{{suggestion}}</output>
      <action>Sair do fluxo de trabalho</action>
    </check>
  </check>
</check>

</step>

<step n="2" goal="Verificar por resumibilidade e determinar modo de fluxo de trabalho">
<critical>ESTRATÉGIA DE CARREGAMENTO INTELIGENTE: Verifique arquivo de estado PRIMEIRO antes de carregar quaisquer arquivos CSV</critical>

<action>Verificar por arquivo de estado existente em: {output_folder}/project-scan-report.json</action>

<check if="project-scan-report.json exists">
  <action>Ler arquivo de estado e extrair: timestamps, mode, scan_level, current_step, completed_steps, project_classification</action>
  <action>Extrair project_type_id(s) em cache do arquivo de estado se presente</action>
  <action>Calcular idade do arquivo de estado (tempo atual - last_updated)</action>

<ask>Encontrei um estado de fluxo de trabalho em progresso de {{last_updated}}.

**Progresso Atual:**

- Modo: {{mode}}
- Nível de Varredura: {{scan_level}}
- Passos Concluídos: {{completed_steps_count}}/{{total_steps}}
- Último Passo: {{current_step}}
- Tipo(s) de Projeto: {{cached_project_types}}

Você gostaria de:

1. **Retomar de onde paramos** - Continuar do passo {{current_step}}
2. **Começar do zero** - Arquivar estado antigo e começar nova varredura
3. **Cancelar** - Sair sem mudanças

Sua escolha [1/2/3]:
</ask>

    <check if="user selects 1">
      <action>Definir resume_mode = true</action>
      <action>Definir workflow_mode = {{mode}}</action>
      <action>Carregar resumos de descobertas do arquivo de estado</action>
      <action>Carregar project_type_id(s) em cache do arquivo de estado</action>

      <critical>CARREGAMENTO CSV CONDICIONAL PARA RETOMADA:</critical>
      <action>Para cada project_type_id em cache, carregar APENAS a linha correspondente de: {documentation_requirements_csv}</action>
      <action>Pular carregamento de project-types.csv e architecture_registry.csv (não necessário na retomada)</action>
      <action>Armazenar requisitos de doc carregados para uso nos passos restantes</action>

      <action>Exibir: "Retomando {{workflow_mode}} de {{current_step}} com tipo(s) de projeto em cache: {{cached_project_types}}"</action>

      <check if="workflow_mode == deep_dive">
        <action>Carregar e executar: {installed_path}/workflows/deep-dive-instructions.md com contexto de retomada</action>
      </check>

      <check if="workflow_mode == initial_scan OR workflow_mode == full_rescan">
        <action>Carregar e executar: {installed_path}/workflows/full-scan-instructions.md com contexto de retomada</action>
      </check>
    </check>

    <check if="user selects 2">
      <action>Criar diretório de arquivo: {output_folder}/.archive/</action>
      <action>Mover arquivo de estado antigo para: {output_folder}/.archive/project-scan-report-{{timestamp}}.json</action>
      <action>Definir resume_mode = false</action>
      <action>Continuar para Passo 0.5</action>
    </check>

    <check if="user selects 3">
      <action>Exibir: "Saindo do fluxo de trabalho sem mudanças."</action>
      <action>Sair do fluxo de trabalho</action>
    </check>

  </check>

  <check if="state file age >= 24 hours">
    <action>Exibir: "Encontrado arquivo de estado antigo (>24 horas). Começando varredura fresca."</action>
    <action>Arquivar arquivo de estado antigo para: {output_folder}/.archive/project-scan-report-{{timestamp}}.json</action>
    <action>Definir resume_mode = false</action>
    <action>Continuar para Passo 0.5</action>
  </check>

</step>

<step n="3" goal="Verificar por documentação existente e determinar modo de fluxo de trabalho" if="resume_mode == false">
<action>Verificar se {output_folder}/index.md existe</action>

<check if="index.md exists">
  <action>Ler index.md existente para extrair metadados (data, estrutura do projeto, contagem de partes)</action>
  <action>Armazenar como {{existing_doc_date}}, {{existing_structure}}</action>

<ask>Encontrei documentação existente gerada em {{existing_doc_date}}.

O que você gostaria de fazer?

1. **Re-escanear projeto inteiro** - Atualizar toda a documentação com as últimas mudanças
2. **Mergulho profundo em área específica** - Gerar documentação detalhada para um recurso/módulo/pasta particular
3. **Cancelar** - Manter documentação existente como está

Sua escolha [1/2/3]:
</ask>

  <check if="user selects 1">
    <action>Definir workflow_mode = "full_rescan"</action>
    <action>Exibir: "Iniciando re-escanemaneto completo do projeto..."</action>
    <action>Carregar e executar: {installed_path}/workflows/full-scan-instructions.md</action>
    <action>Após sub-fluxo completar, continuar para Passo 4</action>
  </check>

  <check if="user selects 2">
    <action>Definir workflow_mode = "deep_dive"</action>
    <action>Definir scan_level = "exhaustive"</action>
    <action>Exibir: "Iniciando modo de documentação de mergulho profundo..."</action>
    <action>Carregar e executar: {installed_path}/workflows/deep-dive-instructions.md</action>
    <action>Após sub-fluxo completar, continuar para Passo 4</action>
  </check>

  <check if="user selects 3">
    <action>Exibir mensagem: "Mantendo documentação existente. Saindo do fluxo de trabalho."</action>
    <action>Sair do fluxo de trabalho</action>
  </check>
</check>

<check if="index.md does not exist">
  <action>Definir workflow_mode = "initial_scan"</action>
  <action>Exibir: "Nenhuma documentação existente encontrada. Iniciando varredura inicial do projeto..."</action>
  <action>Carregar e executar: {installed_path}/workflows/full-scan-instructions.md</action>
  <action>Após sub-fluxo completar, continuar para Passo 4</action>
</check>

</step>

<step n="4" goal="Atualizar status e completar">

<check if="status_file_found == true">
  <invoke-workflow path="{project-root}/_bmad/bmm/workflows/workflow-status">
    <param>mode: update</param>
    <param>action: complete_workflow</param>
    <param>workflow_name: document-project</param>
  </invoke-workflow>

  <check if="success == true">
    <output>Status atualizado!</output>
  </check>
</check>

<output>**✅ Fluxo de Trabalho de Documentação de Projeto Completo, {user_name}!**

**Documentação Gerada:**

- Modo: {{workflow_mode}}
- Nível de Varredura: {{scan_level}}
- Saída: {output_folder}/index.md e arquivos relacionados

{{#if status_file_found}}
**Status Atualizado:**

- Rastreamento de progresso atualizado

**Próximos Passos:**

- **Próximo obrigatório:** {{next_workflow}} (agente {{next_agent}})

Verifique status a qualquer momento com: `workflow-status`
{{else}}
**Próximos Passos:**
Como nenhum fluxo de trabalho está em progresso:

- Consulte o guia de fluxo de trabalho BMM se não tiver certeza do que fazer a seguir
- Ou execute `workflow-init` para criar um caminho de fluxo de trabalho e obter próximos passos guiados
  {{/if}}
  </output>

</step>

</workflow>
