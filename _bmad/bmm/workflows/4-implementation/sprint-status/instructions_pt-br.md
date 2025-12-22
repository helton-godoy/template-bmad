# Sprint Status - Multi-Mode Service

<critical>O motor de execução de fluxo de trabalho é regido por: {project-root}/\ bmad/core/tasks/workflow.xml</critical>
<critical>Você já deve ter carregado e processado: {project-root}/\ bmad/bmm/workflows/4-implementation/sprint-status/workflow.yaml</critical>
<critical>Modes: interactive (padrão), valida, data</critical>
<critical>⚠ . NÃO mencionar horas, dias, semanas ou linhas do tempo. </critical>

<workflow>

<step n="0" goal="Determine execution mode">
<action>Set mode = {{mode}} se fornecido pelo chamador; caso contrário, modo = "interativo"</action>

<check if="mode == data">
<action> Pule para Passo 20</action>
</check>

<check if="mode == validate">
<action> Pule para Passo 30</action>
</check>

<check if="mode == interactive">
BMADPROTECT084EndContinue até ao passo 1BMADPROTECT083End
</check>
</step>

<step n="1" goal="Locate sprint status file">
BMADPROTECT079EndTry BMADPROTECT128EndBMADPROTECT078End
<check if="file not found">
<output>❌ sprint-status.yaml não encontrado.
Execute o `/bmad:bmm:workflows:sprint-planning` para gerá-lo, em seguida, repetir sprint-status. </output>
BMADPROTECT074EndExit workflowBMADPROTECT073End
</check>
BMADPROTECT071EndContinue até ao passo 2</action>
</step>

<step n="2" goal="Read and parse sprint-status.yaml">
<action>Leia o arquivo completo: {sprint_status_file}BADPROTECT066END
<action>Campos de processamento: gerados, projeto, chave projeto, sistema tracking, story location</action>
<action>Parse development status map. Classificar chaves:</action>
Teclas   - Epics: começando com "epic-" (e não terminando com "-retrospectiva")
  - Retrospectives: chaves que terminam com "-retrospectivas"
  - Stories: tudo o resto (por exemplo, 1-2-login-form)
<action>Map status de história legado "projetado" → "pronto para-dev"</action>
<action>Conte status da história: backlog, pronto para dev, em andamento, revisão, doneBADPROTECT058END
<action>Map status épico legado "contexto" → "em progresso"</action>
<action>Contar os estados épicos: backlog, in-progress, doneBADPROTECT054 END
<action>Conte status retrospectivo: opcional, doneBADPROTECT052END

<action>Validate all statuss against known values:</action>

- Status válidos do story: backlog, ready-for-dev, in-progress, review, done, redigido (legacy)
- Status épicos válidos: backlog, in-progress, done, contextualizado (legacy)
- Status retrospectivos válidos: opcional, done

<check if="any status is unrecognized">
<output>
⚠□ **Estado desconhecido detectado:**
{{#each invalid_entries}}

- `{{key}}`: "{{status}}" (não reconhecido)
{{/each}}

**Estatutos válidos:**
BMADPROTECT137End backlog, pronto para dev, em andamento, revisão, done
BMADPROTECT136 End backlog, in-progress, done
- Retrospectives: opcional, done
</output>
<ask> Como estes devem ser corrigidos?
{{#each invalid_entries}}
BMADPROTECT122end}. {{key}}: "{{status}}" → [selecionar estado válido]
{{/each}}

Introduza correcções (por exemplo, "1=em progresso, 2=backlog") ou "skip" para continuar sem fixar: </ask>
<check if="user provided corrections">
<action>Update sprint-status.yaml com valores corrigidos</action>
<action>Reparse o arquivo com status corrigido</action>
</check>
</check>

<action>Detecte riscos: </action>

- Se qualquer história tem status "revisão": sugerir `/bmad:bmm:workflows:code-review`
- Se alguma história tem status "em andamento" E nenhuma história tem status "pronto para dev": recomendo manter-se focado em história ativa
- Se todos os épicos têm status de "backlog" E nenhuma história tem status de "pronto para-dev": prompt `/bmad:bmm:workflows:create-story`
- Se `generated` timestamp tiver mais de 7 dias de idade: avisar "sprint-status.yaml pode estar velho"
- Se alguma chave de história não corresponder a um padrão épico (por exemplo, história "5-1-..." mas não "epic-5"): alertar "história órfã detectada"
- SE algum épico tem status em andamento, mas não tem histórias associadas: alertar "épico em andamento não tem histórias"
</step>

<step n="3" goal="Select next action recommendation">
<action>Escolha o próximo fluxo de trabalho recomendado usando prioridade:</action>
<note>Ao selecionar "primeira" história: ordenar por número épico, em seguida, número de história (por exemplo, 1-1 antes de 1-2 antes de 2-1)</note>
1. Se qualquer status da história == em andamento → recomenda `dev-story` para a primeira história em andamento
2. Caso contrário, se algum status da história == revisão → recomendar `code-review` para a primeira história da revisão
3. Caso contrário, se algum status da história == pronto-para-dev → recomendar `dev-story`
4. Caso contrário, se algum status da história == backlog → recomendar `create-story`
5. Caso contrário, se algum status retrospectivo == opcional → recomendar `retrospective`
6. Else → Todos os itens implementation done; sugerir `workflow-status` para planejar a próxima fase
<action>Store selected recommendation as: next story id, next workflow id, next agent (SM/DEV, conforme apropriado)</action>
</step>

<step n="4" goal="Display summary">
<output>

## 📊 Sprint Status

- Project: {{project}} ({{project_key}})
BMADPROTECT133end BMADPROTECT116end}
- Arquivo de estado: {sprint_status_file}

**Histórias:** backlog {{count_backlog}}, pronto para dev {{count_ready}}, em progresso {{count_in_progress}}, revisão {{count_review}}, done {{count_done}}

**Epics:** backlog {{epic_backlog}}, em progresso