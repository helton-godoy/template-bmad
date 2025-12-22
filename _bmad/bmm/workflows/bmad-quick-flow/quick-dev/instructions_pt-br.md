# Quick-Dev - Fluxo de Trabalho de Desenvolvimento Flexível

<workflow>

<critical>Comunicar em {communication_language}, adaptado para {user_skill_level}BADPROTECT113END
BMADPROTECT112EndExecute continuamente até COMPLETE - não pare para marcos</critical>
<critical>Flexível - manuseia especificações técnicas ou instruções diretas</critical>
<critical>ALWAYS respeitam {project_context} se existir - define padrões de projeto</critical>

<checkpoint-handlers>
<on-select key="a">Carregar e executar {advanced_elicitation}, em seguida, retornar</on-select>
<on-select key="p">Carregar e executar {party_mode_workflow}, em seguida, retornar</on-select>
<on-select key="t">Carregar e executar {create_tech_spec_workflow}BADPROTECT100END
</checkpoint-handlers>

<step n="1" goal="Load project context and determine execution mode">

<action> Verifique se {project_context} existe. Se sim, carregá-lo - esta é sua referência fundamental para TODAS as decisões implementation (padrão, convenções, arquitetura). </action>

<action> Processar a entrada do usuário:

**Mode A: Tech-Spec** - por exemplo, `quick-dev tech-spec-auth.md`
→ Especificações de carga, extrair tarefas/contexto/AC, passo 3

**Modo B: Instruções Diretas** - por exemplo, `refactor src/foo.ts...`
→ Oferece planning escolha
</action>

<check if="Mode A">
<action>Load tech-spec, extrair tarefas/contexto/AC</action>
BMADPROTECT090Endstep 3BMADPROTECT089End
</check>

<check if="Mode B">

<!-- Escalation Threshold: Lightweight check - should we invoke scale-adaptive? -->

<action>EAvaliar o limiar de escalada contra a entrada do usuário (toques mínimos, sem carregamento de arquivos):

**Triggers escalation** (se 2+ sinais presentes):

- Vários componentes mencionados (por exemplo, painel + banco de dados api +)
- Linguagem de nível de sistema (por exemplo, plataforma, integração, arquitectura)
- Incerteza sobre a abordagem (por exemplo, "como devo", "melhor maneira de")
- Âmbito multicamadas (por exemplo, UI + infra-estrutura + dados em conjunto)
- Prazo alargado (por exemplo, "esta semana", "nos próximos dias")

**Reduz o sinal:**

- Marcadores de simplicidade (por exemplo, "just", "quickly", "fix", "bug", "typo", "simples", "basic", "menor")
- Foco em arquivo único/componente
- Pedido confiante, específico

Use julgamento holístico, não correspondência de palavras-chave mecânica. </action>

<!-- No Escalation: Simple request, offer existing choice -->
<check if="escalation threshold NOT triggered">
<ask>**[t] Plano primeiro** - Criar tech-spec e implementar
**[e] Execute diretamente** - Iniciar agora</ask>

<check if="t">
<action>Carregar e executar {create_tech_spec_workflow}BADPROTECT077END
<action>Continue até implementation após a especificação completa </action>
</check>

<check if="e">
<ask> Alguma orientação adicional antes de começar? (padrões, ficheiros, restrições) Ou "ir" para começar. </ask>
BMADPROTECT070Endstep 2BMADPROTECT069End
</check>

</check>

<!-- Escalation Triggered: Load scale-adaptive and evaluate level -->
<check if="escalation threshold triggered">
<action>Load {project_levels} e avaliar a entrada do usuário contra detection hints.keywordsBMAADPROTECT063END
<action>Determine o nível (0-4) utilizando definições adaptativas em escala</action>

<!-- Level 0: Scale-adaptive confirms simple, fall back to standard choice -->
<check if="level 0">
<ask>**[t] Plano primeiro** - Criar tech-spec e implementar

**[e] Execute diretamente** - Iniciar agora</ask>

<check if="t">
<action>Carregar e executar {create_tech_spec_workflow}BADPROTECT054END
<action>Continue até implementation após a especificação completa </action>
</check>

<check if="e">
<ask> Alguma orientação adicional antes de começar? (padrões, ficheiros, restrições) Ou "ir" para começar. </ask>
BMADPROTECT047Endstep 2BMADPROTECT046End
</check>
</check>

<check if="level 1 or 2 or couldn't determine level">
<ask> Isso parece um recurso focado com vários componentes.

**[t] Criar primeiro o tech-spec** (recomendado)
**[w] Parece maior que o dev-rápido** — veja o que recomenda o método BMad (workflow-init)
**[e] Execute diretamente**</ask>

<check if="t">
<action>Carregar e executar {create_tech_spec_workflow}BADPROTECT038END
<action>Continuar a implementation após a especificação completa </action>
</check>

<check if="w">
<action>Carregar e executar {workflow_init}BADPROTECT032END
<action>EXIT dev rápido - usuário foi encaminhado para BMad Method</action>
</check>

<check if="e">
<ask> Alguma orientação adicional antes de começar? (padrões, ficheiros, restrições) Ou "ir" para começar. </ask>
BMADPROTECT025Endstep 2</goto>
</check>
</check>

<!-- Level 3+: BMad Method territory, recommend workflow-init -->
<check if="level 3 or higher">
<ask> Isso soa como trabalho de plataforma/sistema.

**[w] Método BMad inicial** (recomendado) (início do fluxo de trabalho)
**[t] Criar tech-spec** (iluminador planning)
**[e] Execute diretamente** - sentindo-se com sorte</ask>

<check if="w">
<action>Carregar e executar {workflow_init}BADPROTECT015END
<action>EXIT dev rápido - usuário foi encaminhado para BMad Method</action>
</check>

<check if="t">
<action>Load and execute {create_tech_spec_workflow}BADPROTECT009END
<action>Continue até