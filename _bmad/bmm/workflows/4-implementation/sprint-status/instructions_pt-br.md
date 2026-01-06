# Status do Sprint - Serviço Multi-Modo

<critical>O mecanismo de execução do fluxo de trabalho é governado por: {project-root}/_bmad/core/tasks/workflow.xml</critical>
<critical>Você DEVE já ter carregado e processado: {project-root}/_bmad/bmm/workflows/4-implementation/sprint-status/workflow.yaml</critical>
<critical>Modos: interactive (padrão), validate, data</critical>
<critical>⚠️ ABSOLUTAMENTE NENHUMA ESTIMATIVA DE TEMPO. NÃO mencione horas, dias, semanas ou cronogramas.</critical>

<workflow>

<step n="0" goal="Determinar modo de execução">
  <action>Definir mode = {{mode}} se fornecido pelo chamador; caso contrário mode = "interactive"</action>

  <check if="mode == data">
    <action>Pular para Passo 20</action>
  </check>

  <check if="mode == validate">
    <action>Pular para Passo 30</action>
  </check>

  <check if="mode == interactive">
    <action>Continuar para Passo 1</action>
  </check>
</step>

<step n="1" goal="Localizar arquivo de status do sprint">
  <action>Tentar {sprint_status_file}</action>
  <check if="file not found">
    <output>❌ sprint-status.yaml não encontrado.
Execute `/bmad:bmm:workflows:sprint-planning` para gerá-lo, então reexecute sprint-status.</output>
    <action>Sair do fluxo de trabalho</action>
  </check>
  <action>Continuar para Passo 2</action>
</step>

<step n="2" goal="Ler e analisar sprint-status.yaml">
  <action>Ler o arquivo COMPLETO: {sprint_status_file}</action>
  <action>Analisar campos: generated, project, project_key, tracking_system, story_location</action>
  <action>Analisar mapa development_status. Classificar chaves:</action>
  - Épicos: chaves começando com "epic-" (e não terminando com "-retrospective")
  - Retrospectivas: chaves terminando com "-retrospective"
  - Histórias: todo o resto (e.g., 1-2-login-form)
  <action>Mapear status de história legado "drafted" → "ready-for-dev"</action>
  <action>Contar status de história: backlog, ready-for-dev, in-progress, review, done</action>
  <action>Mapear status de épico legado "contexted" → "in-progress"</action>
  <action>Contar status de épico: backlog, in-progress, done</action>
  <action>Contar status de retrospectiva: optional, done</action>

<action>Validar todos os status contra valores conhecidos:</action>

- Status de história válidos: backlog, ready-for-dev, in-progress, review, done, drafted (legado)
- Status de épico válidos: backlog, in-progress, done, contexted (legado)
- Status de retrospectiva válidos: optional, done

  <check if="any status is unrecognized">
    <output>
⚠️ **Status desconhecido detectado:**
{{#each invalid_entries}}

- `{{key}}`: "{{status}}" (não reconhecido)
  {{/each}}

**Status válidos:**

- Histórias: backlog, ready-for-dev, in-progress, review, done
- Épicos: backlog, in-progress, done
- Retrospectivas: optional, done
  </output>
  <ask>Como estes devem ser corrigidos?
  {{#each invalid_entries}}
  {{@index}}. {{key}}: "{{status}}" → [selecione status válido]
  {{/each}}

Insira correções (e.g., "1=in-progress, 2=backlog") ou "pular" para continuar sem corrigir:</ask>
<check if="user provided corrections">
<action>Atualizar sprint-status.yaml com valores corrigidos</action>
<action>Reanalisar o arquivo com status corrigidos</action>
</check>
</check>

<action>Detectar riscos:</action>

- SE qualquer história tiver status "review": sugerir `/bmad:bmm:workflows:code-review`
- SE qualquer história tiver status "in-progress" E nenhuma história tiver status "ready-for-dev": recomendar manter foco na história ativa
- SE todos os épicos tiverem status "backlog" E nenhuma história tiver status "ready-for-dev": solicitar `/bmad:bmm:workflows:create-story`
- SE timestamp `generated` tiver mais de 7 dias: avisar "sprint-status.yaml pode estar obsoleto"
- SE qualquer chave de história não corresponder a um padrão de épico (e.g., história "5-1-..." mas nenhum "epic-5"): avisar "história órfã detectada"
- SE qualquer épico tiver status in-progress mas não tiver histórias associadas: avisar "épico em progresso não tem histórias"
  </step>

<step n="3" goal="Selecionar próxima recomendação de ação">
  <action>Escolher o próximo fluxo de trabalho recomendado usando prioridade:</action>
  <note>Ao selecionar "primeira" história: ordenar por número de épico, então número de história (e.g., 1-1 antes de 1-2 antes de 2-1)</note>
  1. Se qualquer status de história == in-progress → recomendar `dev-story` para a primeira história em progresso
  2. Senão se qualquer status de história == review → recomendar `code-review` para a primeira história em revisão
  3. Senão se qualquer status de história == ready-for-dev → recomendar `dev-story`
  4. Senão se qualquer status de história == backlog → recomendar `create-story`
  5. Senão se qualquer status de retrospectiva == optional → recomendar `retrospective`
  6. Senão → Todos os itens de implementação concluídos; sugerir `workflow-status` para planejar próxima fase
  <action>Armazenar recomendação selecionada como: next_story_id, next_workflow_id, next_agent (SM/DEV conforme apropriado)</action>
</step>

<step n="4" goal="Exibir resumo">
  <output>
## 📊 Status do Sprint

- Projeto: {{project}} ({{project_key}})
- Rastreamento: {{tracking_system}}
- Arquivo de status: {sprint_status_file}

**Histórias:** backlog {{count_backlog}}, ready-for-dev {{count_ready}}, in-progress {{count_in_progress}}, review {{count_review}}, done {{count_done}}

**Épicos:** backlog {{epic_backlog}}, in-progress {{epic_in_progress}}, done {{epic_done}}

**Próxima Recomendação:** /bmad:bmm:workflows:{{next_workflow_id}} ({{next_story_id}})

{{#if risks}}
**Riscos:**
{{#each risks}}

- {{this}}
  {{/each}}
  {{/if}}

  </output>
  </step>

<step n="5" goal="Oferecer ações">
  <ask>Escolha uma opção:
1) Executar fluxo de trabalho recomendado agora
2) Mostrar todas as histórias agrupadas por status
3) Mostrar sprint-status.yaml bruto
4) Sair
Escolha:</ask>

  <check if="choice == 1">
    <output>Execute `/bmad:bmm:workflows:{{next_workflow_id}}`.
Se o comando visar uma história, defina `story_key={{next_story_id}}` quando solicitado.</output>
  </check>

  <check if="choice == 2">
    <output>
### Histórias por Status
- Em Progresso: {{stories_in_progress}}
- Revisão: {{stories_in_review}}
- Pronto para Dev: {{stories_ready_for_dev}}
- Backlog: {{stories_backlog}}
- Concluído: {{stories_done}}
    </output>
  </check>

  <check if="choice == 3">
    <action>Exibir o conteúdo completo de {sprint_status_file}</action>
  </check>

  <check if="choice == 4">
    <action>Sair do fluxo de trabalho</action>
  </check>
</step>

<!-- ========================= -->
<!-- Modo de dados para outros fluxos -->
<!-- ========================= -->

<step n="20" goal="Saída do modo de dados">
  <action>Carregar e analisar {sprint_status_file} igual ao Passo 2</action>
  <action>Computar recomendação igual ao Passo 3</action>
  <template-output>next_workflow_id = {{next_workflow_id}}</template-output>
  <template-output>next_story_id = {{next_story_id}}</template-output>
  <template-output>count_backlog = {{count_backlog}}</template-output>
  <template-output>count_ready = {{count_ready}}</template-output>
  <template-output>count_in_progress = {{count_in_progress}}</template-output>
  <template-output>count_review = {{count_review}}</template-output>
  <template-output>count_done = {{count_done}}</template-output>
  <template-output>epic_backlog = {{epic_backlog}}</template-output>
  <template-output>epic_in_progress = {{epic_in_progress}}</template-output>
  <template-output>epic_done = {{epic_done}}</template-output>
  <template-output>risks = {{risks}}</template-output>
  <action>Retornar ao chamador</action>
</step>

<!-- ========================= -->
<!-- Modo de validação -->
<!-- ========================= -->

<step n="30" goal="Validar arquivo de status de sprint">
  <action>Verificar que {sprint_status_file} existe</action>
  <check if="missing">
    <template-output>is_valid = false</template-output>
    <template-output>error = "sprint-status.yaml ausente"</template-output>
    <template-output>suggestion = "Execute sprint-planning para criá-lo"</template-output>
    <action>Retornar</action>
  </check>

<action>Ler e analisar {sprint_status_file}</action>

<action>Validar campos de metadados obrigatórios existem: generated, project, project_key, tracking_system, story_location</action>
<check if="any required field missing">
<template-output>is_valid = false</template-output>
<template-output>error = "Campo(s) obrigatório(s) ausente(s): {{missing_fields}}"</template-output>
<template-output>suggestion = "Reexecute sprint-planning ou adicione campos ausentes manualmente"</template-output>
<action>Retornar</action>
</check>

<action>Verificar seção development_status existe com pelo menos uma entrada</action>
<check if="development_status missing or empty">
<template-output>is_valid = false</template-output>
<template-output>error = "development_status ausente ou vazio"</template-output>
<template-output>suggestion = "Reexecute sprint-planning ou repare o arquivo manualmente"</template-output>
<action>Retornar</action>
</check>

<action>Validar todos os valores de status contra status válidos conhecidos:</action>

- Histórias: backlog, ready-for-dev, in-progress, review, done (legado: drafted)
- Épicos: backlog, in-progress, done (legado: contexted)
- Retrospectivas: optional, done
  <check if="any invalid status found">
  <template-output>is_valid = false</template-output>
  <template-output>error = "Valores de status inválidos: {{invalid_entries}}"</template-output>
  <template-output>suggestion = "Corrija status inválidos em sprint-status.yaml"</template-output>
  <action>Retornar</action>
  </check>

<template-output>is_valid = true</template-output>
<template-output>message = "sprint-status.yaml válido: metadados completos, todos os status reconhecidos"</template-output>
</step>

</workflow>
