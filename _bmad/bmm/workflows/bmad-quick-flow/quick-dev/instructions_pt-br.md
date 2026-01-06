# Quick-Dev - Fluxo de Trabalho de Desenvolvimento Flexível

<workflow>

<critical>Comunique em {communication_language}, adaptado para {user_skill_level}</critical>
<critical>Execute continuamente até COMPLETO - não pare para marcos</critical>
<critical>Flexível - lida com tech-specs OU instruções diretas</critical>
<critical>SEMPRE respeite {project_context} se existir - ele define padrões do projeto</critical>

<checkpoint-handlers>
  <on-select key="a">Carregar e executar {advanced_elicitation}, depois retornar</on-select>
  <on-select key="p">Carregar e executar {party_mode_workflow}, depois retornar</on-select>
  <on-select key="t">Carregar e executar {create_tech_spec_workflow}</on-select>
</checkpoint-handlers>

<step n="1" goal="Carregar contexto do projeto e determinar modo de execução">

<action>Verificar se {project_context} existe. Se sim, carregue - esta é sua referência fundamental para TODAS as decisões de implementação (padrões, convenções, arquitetura).</action>

<action>Analisar entrada do usuário:

**Modo A: Tech-Spec** - e.g., `quick-dev tech-spec-auth.md`
→ Carregar especificação, extrair tarefas/contexto/CA, ir para passo 3

**Modo B: Instruções Diretas** - e.g., `refactor src/foo.ts...`
→ Oferecer escolha de planejamento
</action>

<check if="Mode A">
  <action>Carregar tech-spec, extrair tarefas/contexto/CA</action>
  <goto>step_3</goto>
</check>

<check if="Mode B">

  <!-- Limiar de Escalonamento: Verificação leve - devemos invocar adaptável à escala? -->

<action>Avaliar limiar de escalonamento contra entrada do usuário (mínimo de tokens, sem carregamento de arquivo):

**Gatilhos de escalonamento** (se 2+ sinais presentes):

- Múltiplos componentes mencionados (e.g., dashboard + api + banco de dados)
- Linguagem de nível de sistema (e.g., plataforma, integração, arquitetura)
- Incerteza sobre abordagem (e.g., "como devo", "melhor maneira de")
- Escopo multicamada (e.g., UI + backend + dados juntos)
- Prazo estendido (e.g., "esta semana", "nos próximos dias")

**Reduz sinal:**

- Marcadores de simplicidade (e.g., "apenas", "rapidamente", "consertar", "bug", "erro de digitação", "simples", "básico", "menor")
- Foco em arquivo/componente único
- Solicitação confiante e específica

Use julgamento holístico, não correspondência mecânica de palavras-chave.</action>

  <!-- Sem Escalonamento: Solicitação simples, oferecer escolha existente -->
  <check if="escalation threshold NOT triggered">
    <ask>**[t] Planejar primeiro** - Criar tech-spec então implementar
**[e] Executar diretamente** - Começar agora</ask>

    <check if="t">
      <action>Carregar e executar {create_tech_spec_workflow}</action>
      <action>Continuar para implementação após especificação completa</action>
    </check>

    <check if="e">
      <ask>Alguma orientação adicional antes de eu começar? (padrões, arquivos, restrições) Ou "ir" para iniciar.</ask>
      <goto>step_2</goto>
    </check>

  </check>

  <!-- Escalonamento Disparado: Carregar adaptável à escala e avaliar nível -->
  <check if="escalation threshold triggered">
    <action>Carregar {project_levels} e avaliar entrada do usuário contra detection_hints.keywords</action>
    <action>Determinar nível (0-4) usando definições adaptáveis à escala</action>

    <!-- Nível 0: Adaptável à escala confirma simples, recorrer à escolha padrão -->
    <check if="level 0">
      <ask>**[t] Planejar primeiro** - Criar tech-spec então implementar

**[e] Executar diretamente** - Começar agora</ask>

      <check if="t">
        <action>Carregar e executar {create_tech_spec_workflow}</action>
        <action>Continuar para implementação após especificação completa</action>
      </check>

      <check if="e">
        <ask>Alguma orientação adicional antes de eu começar? (padrões, arquivos, restrições) Ou "ir" para iniciar.</ask>
        <goto>step_2</goto>
      </check>
    </check>

    <check if="level 1 or 2 or couldn't determine level">
      <ask>Isso parece um recurso focado com múltiplos componentes.

**[t] Criar tech-spec primeiro** (recomendado)
**[w] Parece maior que quick-dev** — ver o que o Método BMad recomenda (workflow-init)
**[e] Executar diretamente**</ask>

      <check if="t">
        <action>Carregar e executar {create_tech_spec_workflow}</action>
        <action>Continuar para implementação após especificação completa</action>
      </check>

      <check if="w">
        <action>Carregar e executar {workflow_init}</action>
        <action>SAIR de quick-dev - usuário foi roteado para Método BMad</action>
      </check>

      <check if="e">
        <ask>Alguma orientação adicional antes de eu começar? (padrões, arquivos, restrições) Ou "ir" para iniciar.</ask>
        <goto>step_2</goto>
      </check>
    </check>

    <!-- Nível 3+: Território do Método BMad, recomendar workflow-init -->
    <check if="level 3 or higher">
      <ask>Isso soa como trabalho de plataforma/sistema.

**[w] Começar Método BMad** (recomendado) (workflow-init)
**[t] Criar tech-spec** (planejamento mais leve)
**[e] Executar diretamente** - sentindo sorte</ask>

      <check if="w">
        <action>Carregar e executar {workflow_init}</action>
        <action>SAIR de quick-dev - usuário foi roteado para Método BMad</action>
      </check>

      <check if="t">
        <action>Carregar e executar {create_tech_spec_workflow}</action>
        <action>Continuar para implementação após especificação completa</action>
      </check>

      <check if="e">
        <ask>Alguma orientação adicional antes de eu começar? (padrões, arquivos, restrições) Ou "ir" para iniciar.</ask>
        <goto>step_2</goto>
      </check>
    </check>

  </check>

</check>

</step>

<step n="2" goal="Coleta rápida de contexto (modo direto)">

<action>Identificar arquivos para modificar, encontrar padrões relevantes, notar dependências</action>

<action>Criar plano mental: tarefas, critérios de aceite, arquivos para tocar</action>

</step>

<step n="3" goal="Executar implementação" id="step_3">

<action>Para cada tarefa:

1. **Carregar Contexto** - ler arquivos da especificação ou relevantes para mudança
2. **Implementar** - seguir padrões, tratar erros, seguir convenções
3. **Testar** - escrever testes, executar testes existentes, verificar CA
4. **Marcar Completo** - marcar tarefa [x], continuar
   </action>

<action if="3 failures">PARAR e solicitar orientação</action>
<action if="tests fail">Consertar antes de continuar</action>

<critical>Continue através de TODAS as tarefas sem parar</critical>

</step>

<step n="4" goal="Verificar e completar">

<action>Verificar: todas as tarefas [x], testes passando, CA satisfeito, padrões seguidos</action>

<check if="using tech-spec">
  <action>Atualizar status da tech-spec para "Concluído", marcar todas as tarefas [x]</action>
</check>

<output>**Implementação Completa!**

**Resumo:** {{implementation_summary}}
**Arquivos Modificados:** {{files_list}}
**Testes:** {{test_summary}}
**Status CA:** {{ac_status}}

---

**Antes de comitar (Recomendado): Copie este prompt de revisão de código para um LLM diferente**

```
Você é um revisor de código cínico e cansado com zero paciência para trabalho desleixado. Estas mudanças não comitadas foram submetidas por uma doninha sem noção e você espera encontrar problemas. Encontre pelo menos cinco problemas para corrigir ou melhorar nele. Numere-os. Seja cético sobre tudo.
```

</output>

<action>Você deve explicar o que foi implementado com base em {user_skill_level}</action>

</step>

</workflow>
