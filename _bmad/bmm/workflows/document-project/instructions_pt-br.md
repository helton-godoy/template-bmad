# Document Project Workflow Router

<critical>O motor de execução de fluxo de trabalho é regido por: {project-root}/\ bmad/core/tasks/workflow.xml</critical>
<critical>Você já deve ter carregado e processado: {project-root}/\ bmad/bmm/workflows/document-project/workflow.yaml</critical>
<critical> Comunicar todas as respostas no {communication_language}BADPROTECT123END

<workflow>

<critical>Este roteador determina o modo de fluxo de trabalho e delegados para subfluxos de trabalho especializados</critical>

<step n="1" goal="Validate workflow and get project info">

<invoke-workflow path="{project-root}/_bmad/bmm/workflows/workflow-status">
  <param>mode: data</param>
  <param>data_request: project_config</param>
</invoke-workflow>

<check if="status_exists == false">
BMADPROTECT111ndBMADPROTECT153end}BMADPROTECT110end
O fluxo de trabalho   <output>Note: Documentation pode ser executado independentemente. Continuando sem acompanhamento de progresso.</output>
<action>Set standalone mode = true</action>
<action>Status file found = false</action>
</check>

<check if="status_exists == true">
<action>Store {{status_file_path}} para atualizações posteriores</action>
<action>Set status file found = true</action>

<!-- Extract brownfield/greenfield from status data -->
<check if="field_type == 'greenfield'">
    <output>Note: This é um projeto de campo verde. O fluxo de trabalho de documentação é tipicamente para projetos de brownfield. </output>
<ask>Continue de qualquer maneira para documentar artefatos planning? (y/n)</ask>
<check if="n">
BMADPROTECT090EndFlow de saídaBMADPROTECT089End
</check>
</check>

<!-- Now validate sequencing -->
<invoke-workflow path="{project-root}/_bmad/bmm/workflows/workflow-status">
    <param>mode: validate</param>
    <param>calling_workflow: document-project</param>
</invoke-workflow>

<check if="warning != ''">
<output>BAMADPROTECT151End}BMADPROTECT077End
    <output>Note: This pode ser auto-invocado por prd para documentação de campo marrom. </output>
<ask>Continue com a documentação? (y/n)</ask>
<check if="n">
BMADPROTECT071endBMADPROTECT150end}BMADPROTECT070end
BMADPROTECT069EndExit workflowBMADPROTECT068End
</check>
</check>
</check>

</step>

<step n="2" goal="Check for resumability and determine workflow mode">
<critical>SMART ESTRATÉGIA DE LOGAÇÃO: Verifique primeiro o arquivo de estado antes de carregar quaisquer arquivos CSV</critical>

<action>Verifique o ficheiro de estado existente em: {output_folder}/project-scan-report.json</action>

<check if="project-scan-report.json exists">
<action>Leia o arquivo de estado e extração: timestamps, modo, scan level, current step, completed steps, project classification</action>
<action>Extract cached project type id(s) from state file if present</action>
<action>Calcule a idade do arquivo de estado (hora atual - última  atualização) </action>

<ask>I encontrou um estado de fluxo de trabalho em andamento do {{last_updated}}.

**Progresso atual:**

- Mode: {{mode}}
- Nível de varredura: {{scan_level}}
- Passos completados: {{completed_steps_count}}/{{total_steps}}
- Último passo: {{current_step}}
- Tipo(s) de projecto: {{cached_project_types}}

Gostaria de:

1. **Resumir de onde paramos** - Continuar do passo {{current_step}}
2. **Iniciar fresco** - Arquivar estado antigo e começar nova varredura
3. **Cancelar** - Sair sem alterações

A sua escolha [1/2/3]:
</ask>

<check if="user selects 1">
<action>Set resume mode = trueBMADPROTECT047End
<action>Set workflow mode = {{mode}}BMADPROTECT045End
<action>Resumidos dos resultados obtidos no ficheiro estatal</action>
<action>Load cached project type id(s) from state file</action>

<critical>CONDITIONAL CSV LOAding for RESUME:</critical>
<action> Para cada tipo de projeto em cache, carregue APENAS a linha correspondente de: {documentation_requirements_csv}</action>
<action>Skip loading project-types.csv and architecture registry.csv (não é necessário no currículo)</action>
<action>Store carregado requisitos de documentação para uso em etapas restantes</action>

<action>Display: "Retomando {{workflow_mode}} do {{current_step}} com tipo(s) de projeto em cache: {{cached_project_types}}"</action>

<check if="workflow_mode == deep_dive">
<action>Carregar e executar: {installed_path}/workflows/deep-dive-instructions.md com contexto de currículo</action>
</check>

<check if="workflow_mode == initial_scan OR workflow_mode == full_rescan">
<action>Carregar e executar: {installed_path}/workflows/full-scan-instructions.md com contexto de currículo</action>
</check>
</check>

<check if="user selects 2">
<action>Create archive directory: {output_folder}/.archive/</action>
<action>Mova o arquivo de estado antigo para: {output_folder}/.archive/project-scan-report-{{timestamp}}.json</action>
<action>Set resume mode = false</action>
<action>Continue até ao passo 0,5</action>
</check>

<check if="user selects 3">
<action>Display: "Sair do fluxo de trabalho sem alterações. " </action>
BMADPROTECT008EndExit workflowBMADPROTECT007End
</check>

</check>

<check if="state file age >= 24 horas">
<action>Display: "Encontrado arquivo de estado antigo (>24 horas). A iniciar um novo exame. " </action>
<action>Archive o arquivo de estado antigo para: {output  folder