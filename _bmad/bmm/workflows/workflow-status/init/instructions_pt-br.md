# Init de Fluxo de Trabalho - Instruções de Configuração de Projeto

<critical>O mecanismo de execução do fluxo de trabalho é governado por: {project-root}/_bmad/core/tasks/workflow.xml</critical>
<critical>Você DEVE já ter carregado e processado: workflow-init/workflow.yaml</critical>
<critical>Comunique em {communication_language} com {user_name}</critical>
<critical>Este fluxo de trabalho lida AMBOS novos projetos E projetos legados seguindo o Método BMad</critical>

<workflow>

<step n="1" goal="Varrer por trabalho existente">
<output>Bem-vindo ao Método BMad, {user_name}!</output>

<action>Realizar varredura abrangente por trabalho existente:

- Artefatos BMM: PRD, épicos, arquitetura, UX, brief, pesquisa, brainstorm
- Implementação: histórias, status de sprint, status de fluxo de trabalho
- Base de código: diretórios fonte, arquivos de pacote, repo git
- Verificar ambas as localizações {output_folder} e {sprint_artifacts}
  </action>

<action>Categorizar em um destes estados:

- LIMPO: Sem artefatos ou código (ou apenas andaime)
- PLANEJAMENTO: Tem PRD/especificação mas sem implementação
- ATIVO: Tem histórias ou status de sprint
- LEGADO: Tem código mas sem artefatos BMM
- POUCO CLARO: Estado misto precisa de esclarecimento
  </action>

<ask>Como seu projeto se chama? {{#if project_name}}(Config mostra: {{project_name}}){{/if}}</ask>
<action>Armazenar project_name</action>
<template-output>project_name</template-output>
</step>

<step n="2" goal="Escolher caminho de configuração">
<check if="state == CLEAN">
  <output>Perfeito! Novo começo detectado.</output>
  <action>Continuar para passo 3</action>
</check>

<check if="state == ACTIVE AND workflow_status exists">
  <output>✅ Você já tem rastreamento de fluxo de trabalho em: {{workflow_status_path}}

Para verificar progresso: Carregue qualquer agente BMM e execute /bmad:bmm:workflows:workflow-status

Boa construção! 🚀</output>
<action>Sair do fluxo de trabalho (já inicializado)</action>
</check>

<check if="state != CLEAN">
  <output>Encontrado trabalho existente:
{{summary_of_findings}}</output>

<ask>Como você gostaria de prosseguir?

1. **Continuar** - Trabalhar com artefatos existentes
2. **Arquivar & Começar do Zero** - Mover trabalho antigo para arquivo
3. **Configuração Expressa** - Eu sei exatamente o que preciso
4. **Configuração Guiada** - Guie-me através das opções

Escolha [1-4]</ask>

  <check if="choice == 1">
    <action>Definir continuing_existing = true</action>
    <action>Armazenar artefatos encontrados</action>
    <action>Continuar para passo 7 (detectar trilha a partir de artefatos)</action>
  </check>

  <check if="choice == 2">
    <ask>Arquivar trabalho existente? (s/n)</ask>
    <action if="s">Mover artefatos para {output_folder}/archive/</action>
    <output>Pronto para novo começo!</output>
    <action>Continuar para passo 3</action>
  </check>

  <check if="choice == 3">
    <action>Pular para passo 3 (caminho expresso)</action>
  </check>

  <check if="choice == 4">
    <action>Continuar para passo 4 (caminho guiado)</action>
  </check>
</check>

<check if="state == CLEAN">
  <ask>Abordagem de configuração:

1. **Expressa** - Eu sei o que preciso
2. **Guiada** - Mostre-me as opções

Escolha [1 ou 2]:</ask>

  <check if="choice == 1">
    <action>Continuar para passo 3 (expresso)</action>
  </check>

  <check if="choice == 2">
    <action>Continuar para passo 4 (guiado)</action>
  </check>
</check>
</step>

<step n="3" goal="Caminho de configuração expressa">
<ask>Isso é para:
1. **Novo projeto** (greenfield)
2. **Base de código existente** (brownfield)

Escolha [1/2]:</ask>
<action>Definir field_type baseado na escolha</action>

<ask>Abordagem de planejamento:

1. **Método BMad** - Planejamento completo para projetos complexos
2. **Método Empresarial** - Planejamento estendido com segurança/DevOps

Escolha [1/2]:</ask>
<action>Mapear para selected_track: method/enterprise</action>

<output>🚀 **Para Quick Flow (planejamento mínimo, direto para código):**
Carregue o agente **quick-flow-solo-dev** em vez disso - use o agente Quick Flow para desenvolvimento mais rápido</output>

<template-output>field_type</template-output>
<template-output>selected_track</template-output>
<action>Pular para passo 6 (opções de descoberta)</action>
</step>

<step n="4" goal="Configuração guiada - entender projeto">
<ask>Me conte sobre o que você está trabalhando. Qual é o objetivo?</ask>
<action>Armazenar user_description</action>

<action>Analisar por indicadores de tipo de campo:

- Brownfield: "existente", "atual", "aprimorar", "modificar"
- Greenfield: "novo", "construir", "criar", "do zero"
- Se base de código existe, padrão para brownfield a menos que usuário indique andaime
  </action>

<check if="field_type unclear AND codebase exists">
  <ask>Vejo código existente. Você está:
1. **Modificando** base de código existente (brownfield)
2. **Começando do zero** - código é apenas andaime (greenfield)

Escolha [1/2]:</ask>
<action>Definir field_type baseado na resposta</action>
</check>

<action if="field_type not set">Definir baseado na presença de base de código</action>

<action>Verificar por palavras-chave de desenvolvimento de jogo</action>
<check if="game_detected">
<output>🎮 **DESENVOLVIMENTO DE JOGO DETECTADO**

Para desenvolvimento de jogo, instale o módulo BMGD:

```bash
bmad install bmgd
```

Continuar com fluxos de trabalho de software? (s/n)</output>
<ask>Escolha:</ask>
<action if="n">Sair do fluxo de trabalho</action>
</check>

<template-output>user_description</template-output>
<template-output>field_type</template-output>
<action>Continuar para passo 5</action>
</step>

<step n="5" goal="Configuração guiada - selecionar trilha">
<output>Com base no seu projeto, aqui estão suas opções de planejamento do Método BMad:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**1. Método BMad** 🎯 {{#if recommended}}(RECOMENDADO){{/if}}

- Planejamento completo: PRD + UX + Arquitetura
- Melhor para: Produtos, plataformas, recursos complexos
- Benefício: Agentes de IA têm contexto completo para melhores resultados

**2. Método Empresarial** 🏢

- Estendido: Método + Segurança + DevOps + Teste
- Melhor para: Empresa, conformidade, missão crítica
- Benefício: Planejamento abrangente para sistemas complexos

**🚀 Para Quick Flow (planejamento mínimo, direto para código):**
Carregue o agente **quick-flow-solo-dev** em vez disso - use o agente Quick Flow para desenvolvimento mais rápido

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{{#if brownfield}}
💡 Arquitetura cria design de solução focado a partir da sua base de código, mantendo agentes de IA na trilha.
{{/if}}</output>

<ask>Qual abordagem do Método BMad se encaixa melhor?

1. Método BMad {{#if recommended}}(recomendado){{/if}}
2. Método Empresarial
3. Ajude-me a decidir
4. Mudar para Quick Flow (usar agente quick-flow-solo-dev)

Escolha [1/2/3/4]:</ask>

<check if="choice == 4">
  <output>🚀 **Mudando para Quick Flow!**

Carregue o agente **quick-flow-solo-dev** em vez disso:

- Comece um novo chat
- Carregue o agente quick-flow-solo-dev
- Use Quick Flow para planejamento mínimo e desenvolvimento mais rápido

Quick Flow é perfeito para:

- Recursos simples e correções de bug
- Prototipagem rápida
- Quando você quer ir direto para o código

Boa codificação! 🚀</output>
<action>Sair do fluxo de trabalho</action>
</check>

<check if="choice == 3">
  <ask>O que te preocupa sobre escolher?</ask>
  <action>Fornecer orientação personalizada baseada em preocupações</action>
  <action>Voltar para escolha</action>
</check>

<action>Mapear escolha para selected_track</action>
<template-output>selected_track</template-output>
</step>

<step n="6" goal="Seleção de fluxos de trabalho de descoberta (unificado)">
<action>Determinar fluxos de trabalho de descoberta disponíveis baseado em:
- field_type (greenfield recebe opção product-brief)
- selected_track (opções method/enterprise)
</action>

<check if="field_type == greenfield AND selected_track in [method, enterprise]">
  <output>Fluxos de trabalho de descoberta opcionais podem ajudar a esclarecer sua visão:</output>
  <ask>Selecione quaisquer que gostaria de incluir:

1. 🧠 **Brainstorm** - Exploração criativa e ideação
2. 🔍 **Pesquisa** - Análise técnica/competitiva
3. 📋 **Brief do Produto** - Planejamento estratégico de produto (recomendado)

Insira números (e.g., "1,3" ou "todos" ou "nenhum"): </ask>
</check>

<check if="field_type == brownfield AND selected_track in [method, enterprise]">
  <output>Fluxos de trabalho de descoberta opcionais:</output>
  <ask>Incluir algum destes?

1. 🧠 **Brainstorm** - Exploração criativa
2. 🔍 **Pesquisa** - Análise de domínio

Insira números (e.g., "1,2" ou "nenhum"): </ask>
</check>

<action>Analisar seleções e definir:

- brainstorm_requested
- research_requested
- product_brief_requested (se aplicável)
  </action>

<template-output>brainstorm_requested</template-output>
<template-output>research_requested</template-output>
<template-output>product_brief_requested</template-output>

<check if="brownfield">
  <output>💡 **Nota:** Para projetos brownfield, execute fluxo de trabalho document-project primeiro para analisar sua base de código.</output>
</check>
</step>

<step n="7" goal="Detectar trilha a partir de artefatos" if="continuing_existing OR migrating_legacy">
<action>Analisar artefatos para detectar trilha:
- Tem PRD → Método BMad
- Tem Segurança/DevOps → Método Empresarial
- Tem apenas especificação técnica → Sugerir mudar para agente quick-flow-solo-dev
</action>

<output>Detectado: **{{detected_track}}** com base em {{found_artifacts}}</output>
<ask>Correto? (s/n)</ask>

<ask if="n">Qual trilha do Método BMad em vez disso?

1. Método BMad
2. Método Empresarial
3. Mudar para Quick Flow (usar agente quick-flow-solo-dev)

Escolha:</ask>

<action>Definir selected_track</action>
<template-output>selected_track</template-output>
</step>

<step n="8" goal="Gerar caminho de fluxo de trabalho">
<action>Carregar arquivo de caminho: {path_files}/{{selected_track}}-{{field_type}}.yaml</action>
<action>Construir workflow_items do arquivo de caminho</action>
<action>Varrer por trabalho concluído existente e atualizar status</action>
<action>Definir data gerada</action>

<template-output>generated</template-output>
<template-output>workflow_path_file</template-output>
<template-output>workflow_items</template-output>
</step>

<step n="9" goal="Criar arquivo de rastreamento">
<output>Seu caminho de fluxo de trabalho BMad:

**Trilha:** {{selected_track}}
**Tipo:** {{field_type}}
**Projeto:** {{project_name}}

{{#if brownfield}}Pré-requisitos: document-project{{/if}}
{{#if has_discovery}}Descoberta: {{list_selected_discovery}}{{/if}}

{{workflow_path_summary}}
</output>

<ask>Criar arquivo de rastreamento de fluxo de trabalho? (s/n)</ask>

<check if="s">
  <action>Gerar YAML a partir do modelo com todas as variáveis</action>
  <action>Salvar em {output_folder}/bmm-workflow-status.yaml</action>
  <action>Identificar próximo fluxo de trabalho e agente</action>

<output>✅ **Criado:** {output_folder}/bmm-workflow-status.yaml

**Próximo:** {{next_workflow_name}}
**Agente:** {{next_agent}}
**Comando:** /bmad:bmm:workflows:{{next_workflow_id}}

{{#if next_agent not in [analyst, pm]}}
💡 Comece um novo chat com o agente **{{next_agent}}** primeiro.
{{/if}}

Para verificar progresso: /bmad:bmm:workflows:workflow-status

Boa construção! 🚀</output>
</check>

</step>

</workflow>
