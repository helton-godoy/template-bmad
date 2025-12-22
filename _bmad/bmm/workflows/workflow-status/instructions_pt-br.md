# Verificação do estado do fluxo de trabalho - Serviço multimodal

<critical>O motor de execução do fluxo de trabalho é regido por: {project-root}/\ bmad/core/tasks/workflow.xml</critical>
<critical>Você já deve ter carregado e processado: {project-root}/\ bmad/bmm/workflows/workflow-status/workflow.yaml</critical>
<critical>Este fluxo de trabalho opera em vários modos: interativo (padrão), validar, dados, verificar init, atualizar</critical>
<critical>Outros fluxos de trabalho podem chamar isso de serviço para evitar duplicar a lógica de status</critical>
<critical>⚠ , ABSOLUTAMENTE NÃO TEMPO ESTIMATOS - NUNCA mencionar horas, dias, semanas, meses, ou quaisquer previsões baseadas no tempo. A IA mudou fundamentalmente a velocidade de desenvolvimento - o que uma vez levou as equipes semanas/meses agora pode ser done por uma pessoa em horas. NÃO dê estimativas de tempo. </critical>

<workflow>

<step n="0" goal="Determine execution mode">
<action>Check for {{mode}} parâmetro passado chamando fluxo de trabalho</action>
<action>Default mode = "interactivo" se não especificado</action>

<check if="mode == interactive">
<action>Continue até o Passo 1 para verificação do estado normal fluxo</action>
</check>

<check if="mode == validate">
<action>Jump to Step 10 for workflow validation service</action>
</check>

<check if="mode == data">
<action>Jump to Step 20 for data extraction service</action>
</check>

<check if="mode == init-check">
<action> Pule para Passo 30 para verificação simples de init</action>
</check>

<check if="mode == update">
<action>Jump to Step 40 for status update service</action>
</check>
</step>

<step n="1" goal="Check for status file">
<action>Search BMADPROTECT128End/ for file: bmm-workflow- status.yamlBMADPROTECT056End

<check if="no status file found">
<output>Nenhum estado de fluxo de trabalho encontrado. </output>
<ask> Você gostaria de executar o Workflow Init agora? (y/n)</ask>

<check if="response == y OR response == yes">
<action>Início de fluxo de trabalho inicial para configurar o rastreamento do projeto...</action>
BMADPROTECT047EndBMADPROTECT046End
BMADPROTECT045EndExit workflow e BMADPROTECT096End workflow-init assumir BMADPROTECT044End
</check>

<check if="else">
<output>No workflow status file. Execute o início do fluxo de trabalho quando estiver pronto para habilitar o rastreamento de progresso. </output>
BMADPROTECT039EndExit workflowBMADPROTECT038End
</check>
</check>

<check if="status file found">
<action>Continue com o passo 2</action>
</check>
</step>

<step n="2" goal="Read and parse status">
<action> Read bmm-workflow-status.yaml</action>
<action>Parse arquivo YAML e extrair metadados de comentários e campos:</action>

Processar estes campos a partir de comentários YAML e metadados:

- projecto (do campo YAML)
- tipo  projeto (do campo YAML)
- nível  projeto (do campo YAML)
- tipo  de campo (do campo YAML)
- workflow path (do campo YAML)

<action>Parse workflow status section:</action>

- Extrair todas as entradas de fluxo de trabalho com seus status
- Identificar fluxos de trabalho completos (status = caminho do arquivo)
- Identificar fluxos de trabalho pendentes (status = requerido/opcional/recomendado/condicional)
- Identificar fluxos de trabalho ignorados (status = puled)

<action>Determine o estado atual:</action>

- Encontrar primeiro fluxo de trabalho com status ! = caminho do arquivo e ! = pulou
- Este é o próximo fluxo de trabalho para trabalhar
- Procure o agente e o comando a partir do arquivo de caminho de fluxo de trabalho
</step>

<step n="3" goal="Display current status and options">
<action>Load workflow path file based on workflow path field</action>
<action>Identifique a fase atual do próximo fluxo de trabalho para ser doneBADPROTECT016END
<action>Build lista de fluxos de trabalho completos, pendentes e opcionais</action>
<action> Para cada fluxo de trabalho, procure seu agente a partir do arquivo de caminho</action>

<output>

## 📊 Estado atual

**Projecto:** {{project}} (Nível {{project_level}} {{project_type}})

**Caminho:** {{workflow_path}}

**Progresso:**

{{#each phases}}
{{phase_name}}:
{{#each workflows_in_phase}}

- {{workflow_name}} ({{agent}}): {{status_display}}
{{/each}}
{{/each}}

## 🎯 Passos seguintes

**Próximo fluxo de trabalho:** {{next_workflow_name}}

**Agente:** {{next_agent}}

**Command:** /bmad:bmm:workflows:{{next_workflow_id}}

{{#if optional_workflows_available}}
**Fluxos de trabalho opcionais disponíveis:**
{{#each optional_workflows}}

- {{workflow_name}} ({{agent}} {{status}}
{{/each}}
{{/if}}
</output>
</step>

<step n="4" goal="Offer actions">
<ask> O que gostarias de fazer?

1. **Iniciar o próximo fluxo de trabalho** - {{next_workflow_name}} ({{next_agent}})
{{#if optional_workflows_available}}
2. **Execute fluxo de trabalho opcional** - Escolha entre as opções disponíveis
{{/if}}
3. **Ver status completo YAML** - Ver arquivo de status completo
4. **Update workflow status** - Marque um workflow como concluído ou ignorado
5. **Saída** - Voltar ao agente

Sua escolha:</ask>

<action>Selecção de utilizadores com base nas opções disponíveis</action>

<check if="choice == 1">
<output> Pronto para executar {{next_workflow_name}}!

**Command:** /bmad:bmm:workflows:{{next_workflow_id}}

**Agente:** Carregar primeiro o agente {{next_agent}}

{{#if next_agent !== current_agent}}
Tip: Start um novo chat e carregar o agente {{next_agent}}