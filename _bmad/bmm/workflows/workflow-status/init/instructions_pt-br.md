# Workflow Init - Instruções de configuração do projeto

<critical>O motor de execução do fluxo de trabalho é regido por: {project-root}/\ bmad/core/tasks/workflow.xml</critical>
<critical>Você já deve ter carregado e processado: workflow-init/workflow.yaml</critical>
<critical> Comunicar em {communication_language} com {user_name}BADPROTECT127END
<critical>Este fluxo de trabalho lida com ambos os novos projetos e projetos legados seguindo o método BMad</critical>

<workflow>

<step n="1" goal="Scan for existing work">
<output> Bem-vindo ao método BMad, {user_name}!</output>

<action>Performance varredura abrangente para o trabalho existente:

- Artefactos BMM: PRD, épicos, arquitetura, UX, breve, pesquisa, brainstorm
BMADPROTECT154End histórias, sprint-status, fluxo de trabalho-status
- Codebase: diretórios de código fonte, arquivos package, git repo
- Verifique os locais {output_folder} e {sprint_artifacts}
</action>

<action>Categorizar em um desses estados:

- CLEAN: Sem artefatos ou código (ou apenas andaime)
- PLANNING: Tem PRD/spec mas nenhum implementation
- ACTIVE: Tem histórias ou sprint status
- LEGACY: Tem código, mas nenhum artefato BMM
- UNCLEAR: Estado misto precisa de esclarecimentos
</action>

<ask> Como se chama o teu projecto? {{#if project_name}}(Exibições do CONFIG: {{project_name}}){{/if}}</ask>
<action>Store project  name</action>
<template-output>project  name</template-output>
</step>

<step n="2" goal="Choose setup path">
<check if="state == CLEAN">
BMADPROTECT107EndPerfeito! Recomeço detectado. </output>
<action>Continue até ao passo 3</action>
</check>

<check if="state == ACTIVE AND workflow_status exists">
<output>✅ Você já tem rastreamento de fluxo de trabalho em: {{workflow_status_path}}

Para verificar o progresso: Carregar qualquer agente BMM e executar /bmad:bmm:workflows:workflow-status

Feliz edifício! 🚀</output>
BMADPROTECT099EndExit workflow (já inicializado) </action>
</check>

<check if="state != CLEAN">
BMADPROTECT095EndEncontrado trabalho existente:
BMADPROTECT135End}BMADPROTECT094End

<ask>Como gostaria de proceder?

1. **Continuar** - Trabalhar com artefatos existentes
2. **Archive & Start Fresh** - Mover o trabalho antigo para o arquivo
3. **Express Setup** - Sei exatamente o que preciso
4. **Setup Guiado** - Explique-me as opções

Escolha [1-4]</ask>

<check if="choice == 1">
<action>Continuar existente = true</action>
<action>Store artefatos encontrados</action>
<action>Continue até o passo 7 (detectar faixa de artefatos)</action>
</check>

<check if="choice == 2">
<ask>Archive trabalho existente? (y/n)</ask>
<action if="y">Mova artefatos para {output_folder}/arquivo/</action>
<output>Pronto para começar de novo! </output>
<action>Continue até ao passo 3</action>
</check>

<check if="choice == 3">
<action>Salte para o passo 3 (caminho expresso)</action>
</check>

<check if="choice == 4">
<action>Continue até ao passo 4 (caminho guiado)</action>
</check>
</check>

<check if="state == CLEAN">
BMADPROTECT063EndSetup abordagem:

1. **Expresso** - Sei do que preciso
2. **Guiado** - Mostre-me as opções

Escolha [1 ou 2]:</ask>

<check if="choice == 1">
<action>Continue até ao passo 3 (expresso)</action>
</check>

<check if="choice == 2">
<action>Continue até ao passo 4 (guiado)</action>
</check>
</check>
</step>

<step n="3" goal="Express setup path">
<ask>E
1. **Novo projecto** (campo verde)
2. **Base de códigos existente** (campo marrom)

Escolha [1/2]:</ask>
<action>Set field type based on choice</action>

BMADPROTECT046EndBMADPROTECT003End abordagem:

1. **Método BMad** - planning completo para projectos complexos
2. **Metodo de empresa** - planning alargado com segurança/DevOps

Escolha [1/2]:</ask>
<action>Map to selected track: method/enterprise</action>

<output>🚀 **Para Fluxo Rápido (planning mínimo, directamente para o código):**
Em vez disso, carregue o agente **rápido-fluxo-solo-dev** - use o agente Quick Flow para um desenvolvimento mais rápido</output>

<template-output>field  typeBADPROTECT039END
BMADPROTECT038Endselected track</template-output>
<action>Salte para o passo 6 (opções de descoberta)</action>
</step>

<step n="4" goal="Guided setup - understand project">
BMADPROTECT032end Conte-me no que está a trabalhar. Qual é o objectivo? </ask>
<action>Store user description</action>

<action>Alyze para indicadores de tipo de campo:

- Brownfield: "existing", "atual", "melhor", "modificar"
- Greenfield: "new", "construir", "criar", "do zero"
- Se a base de códigos existir, por omissão para o campo marrom, a menos que o utilizador indique o andaime
</action>

<check if="field_type unclear AND codebase exists">
<ask>I ver código existente. Você é:
1. **Modificar** a base de código existente (campo marrom)
2. **Iniciando fresco** - código é apenas andaime (campo verde)

Escolha [1/2]:</ask>
<action>Set field type baseado na resposta</action>
</check>

<action if="field_type not set">Set based on codebase presence</action>

<action>Verifique palavras-chave de desenvolvimento de jogos</action>
<check if="game_detected">
<output>🎮 **DESENVOLVIMENTO DE GAME DETECTADO**

Para o desenvolvimento de jogos, instale o módulo BMGD:

```bash
bmad install bmgd

```

Continuar com os fluxos de trabalho de software? (y/n)</output>
<ask>Choice:</ask>
BMADPROTECT011EndExit workflowBMADPROTECT010End
</check>

<template-output>user  description</template- out