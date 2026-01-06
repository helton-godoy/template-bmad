# Instruções de Documentação de Mergulho Profundo

<workflow>

<critical>Este fluxo de trabalho realiza documentação exaustiva de mergulho profundo de áreas específicas</critical>
<critical>Chamado por: ../document-project/instructions.md router</critical>
<critical>Lida com: deep_dive mode only</critical>

<step n="13" goal="Documentação de mergulho profundo de área específica" if="workflow_mode == deep_dive">
<critical>Modo de mergulho profundo requer revisão literal de arquivo completo. Amostragem, adivinhação ou confiar apenas na saída de ferramentas é PROIBIDO.</critical>
<action>Carregar estrutura de projeto existente de index.md e project-parts.json (se existir)</action>
<action>Carregar análise de árvore de código para entender áreas disponíveis</action>

<step n="13a" goal="Identificar área para mergulho profundo">
  <action>Analisar documentação existente para sugerir opções de mergulho profundo</action>

<ask>Em qual área você gostaria de fazer um mergulho profundo?

**Áreas Sugeridas Com Base na Estrutura do Projeto:**

{{#if has_api_routes}}

## Rotas de API ({{api_route_count}} endpoints encontrados)

{{#each api_route_groups}}
{{group_index}}. {{group_name}} - {{endpoint_count}} endpoints em `{{path}}`
{{/each}}
{{/if}}

{{#if has_feature_modules}}

## Módulos de Recurso ({{feature_count}} recursos)

{{#each feature_modules}}
{{module_index}}. {{module_name}} - {{file_count}} arquivos em `{{path}}`
{{/each}}
{{/if}}

{{#if has_ui_components}}

### Áreas de Componentes UI

{{#each component_groups}}
{{group_index}}. {{group_name}} - {{component_count}} componentes em `{{path}}`
{{/each}}
{{/if}}

{{#if has_services}}

### Serviços/Lógica de Negócio

{{#each service_groups}}
{{service_index}}. {{service_name}} - `{{path}}`
{{/each}}
{{/if}}

**Ou especifique personalizado:**

- Caminho da pasta (e.g., "client/src/features/dashboard")
- Caminho do arquivo (e.g., "server/src/api/users.ts")
- Nome do recurso (e.g., "authentication system")

Insira sua escolha (número ou caminho personalizado):
</ask>

<action>Analisar entrada do usuário para determinar: - target_type: "folder" | "file" | "feature" | "api_group" | "component_group" - target_path: Caminho absoluto para varrer - target_name: Nome legível por humanos para documentação - target_scope: Lista de todos os arquivos para analisar
</action>

<action>Armazenar como {{deep_dive_target}}</action>

<action>Exibir confirmação:
Alvo: {{target_name}}
Tipo: {{target_type}}
Caminho: {{target_path}}
Arquivos estimados para analisar: {{estimated_file_count}}

Isso lerá CADA arquivo nesta área. Prosseguir? [s/n]
</action>

<action if="user confirms 'n'">Retornar ao Passo 13a (selecionar área diferente)</action>
</step>

<step n="13b" goal="Varredura exaustiva abrangente da área alvo">
  <action>Definir scan_mode = "exhaustive"</action>
  <action>Inicializar file_inventory = []</action>
  <critical>Você deve ler cada linha de cada arquivo no escopo e capturar uma explicação em linguagem simples (o que o arquivo faz, efeitos colaterais, por que importa) que futuros agentes desenvolvedores possam agir. Sem atalhos.</critical>

  <check if="target_type == folder">
    <action>Obter lista recursiva completa de arquivos de {{target_path}}</action>
    <action>Filtrar: node_modules/, .git/, dist/, build/, coverage/, *.min.js, *.map</action>
    <action>Para CADA arquivo restante na pasta:
      - Ler conteúdo completo do arquivo (todas as linhas)
      - Extrair todas as exportações (funções, classes, tipos, interfaces, constantes)
      - Extrair todas as importações (dependências)
      - Identificar propósito a partir de comentários e estrutura de código
      - Escrever 1-2 frases (mínimo) em linguagem natural descrevendo comportamento, efeitos colaterais, suposições e qualquer coisa que um desenvolvedor deve saber antes de modificar o arquivo
      - Extrair assinaturas de função com tipos de parâmetro e tipos de retorno
      - Notar quaisquer TODOs, FIXMEs ou comentários
      - Identificar padrões (hooks, componentes, serviços, controladores, etc.)
      - Capturar orientação de contribuidor por arquivo: `contributor_note`, `risks`, `verification_steps`, `suggested_tests`
      - Armazenar em file_inventory
    </action>
  </check>

  <check if="target_type == file">
    <action>Ler arquivo completo em {{target_path}}</action>
    <action>Extrair todas as informações conforme acima</action>
    <action>Ler todos os arquivos que ele importa (seguir cadeia de importação 1 nível de profundidade)</action>
    <action>Encontrar todos os arquivos que importam este arquivo (dependentes via grep)</action>
    <action>Armazenar tudo em file_inventory</action>
  </check>

  <check if="target_type == api_group">
    <action>Identificar todos os arquivos de rota/controlador no grupo de API</action>
    <action>Ler todos os manipuladores de rota completamente</action>
    <action>Ler middleware associado, controladores, serviços</action>
    <action>Ler modelos de dados e esquemas usados</action>
    <action>Extrair esquemas completos de requisição/resposta</action>
    <action>Documentar requisitos de autenticação e autorização</action>
    <action>Armazenar tudo em file_inventory</action>
  </check>

  <check if="target_type == feature">
    <action>Pesquisar base de código por todos os arquivos relacionados ao nome do recurso</action>
    <action>Incluir: componentes UI, endpoints de API, modelos, serviços, testes</action>
    <action>Ler cada arquivo completamente</action>
    <action>Armazenar tudo em file_inventory</action>
  </check>

  <check if="target_type == component_group">
    <action>Obter todos os arquivos de componente no grupo</action>
    <action>Ler cada componente completamente</action>
    <action>Extrair: Interfaces de Props, hooks usados, componentes filhos, gerenciamento de estado</action>
    <action>Armazenar tudo em file_inventory</action>
  </check>

<action>Para cada arquivo em file\*inventory, documentar: - **Caminho do Arquivo:** Caminho completo - **Propósito:** O que este arquivo faz (1-2 frases) - **Linhas de Código:** Total LOC - **Exportações:** Lista completa com assinaturas

- Funções: `functionName(param: Type): ReturnType` - Descrição
  - Classes: `ClassName` - Descrição com métodos chave
  - Tipos/Interfaces: `TypeName` - Descrição
  - Constantes: `CONSTANT_NAME: Type` - Descrição - **Importações/Dependências:** O que ele usa e por que - **Usado Por:** Arquivos que importam este (dependentes) - **Detalhes Chave de Implementação:** Lógica importante, algoritmos, padrões - **Gerenciamento de Estado:** Se aplicável (Redux, Context, estado local) - **Efeitos Colaterais:** Chamadas de API, consultas de banco de dados, E/S de arquivo, serviços externos - **Tratamento de Erros:** Blocos try/catch, limites de erro, validação - **Testes:** Arquivos de teste associados e cobertura - **Comentários/TODOs:** Qualquer documentação inline ou trabalho planejado
    </action>

<template-output>comprehensive_file_inventory</template-output>
</step>

<step n="13c" goal="Analisar relacionamentos e fluxo de dados">
  <action>Construir grafo de dependência para área varrida:
    - Criar grafo com arquivos como nós
    - Adicionar arestas para relacionamentos de importação
    - Identificar dependências circulares se houver
    - Encontrar pontos de entrada (arquivos não importados por outros no escopo)
    - Encontrar nós folha (arquivos que não importam outros no escopo)
  </action>

<action>Rastrear fluxo de dados através do sistema: - Seguir chamadas de função e transformações de dados - Rastrear chamadas de API e suas respostas - Documentar atualizações de estado e propagação - Mapear consultas de banco de dados e mutações
</action>

<action>Identificar pontos de integração: - APIs externas consumidas - APIs/serviços internos chamados - Estado compartilhado acessado - Eventos publicados/assinados - Tabelas de banco de dados acessadas
</action>

<template-output>dependency_graph</template-output>
<template-output>data_flow_analysis</template-output>
<template-output>integration_points</template-output>
</step>

<step n="13d" goal="Encontrar código relacionado e padrões similares">
  <action>Pesquisar base de código FORA da área varrida por:
    - Padrões de nomeação de arquivo/pasta similares
    - Assinaturas de função similares
    - Estruturas de componente similares
    - Padrões de API similares
    - Utilitários reutilizáveis que poderiam ser usados
  </action>

<action>Identificar oportunidades de reuso de código: - Utilitários compartilhados disponíveis - Padrões de design usados em outro lugar - Bibliotecas de componentes disponíveis - Funções auxiliares que poderiam aplicar
</action>

<action>Encontrar implementações de referência: - Recursos similares em outras partes da base de código - Padrões estabelecidos para seguir - Abordagens de teste usadas em outro lugar
</action>

<template-output>related_code_references</template-output>
<template-output>reuse_opportunities</template-output>
</step>

<step n="13e" goal="Gerar documentação de mergulho profundo abrangente">
  <action>Criar nome de arquivo de documentação: deep-dive-{{sanitized_target_name}}.md</action>
  <action>Agregar insights de contribuidor através dos arquivos:
    - Combinar notas de risco/pegadinha únicas em {{risks_notes}}
    - Combinar passos de verificação que desenvolvedores devem executar antes de mudanças em {{verification_steps}}
    - Combinar comandos de teste recomendados em {{suggested_tests}}
  </action>

<action>Carregar modelo de mergulho profundo completo de: {installed_path}/templates/deep-dive-template_pt-br.md</action>
<action>Preencher modelo com todos os dados coletados dos passos 13b-13d</action>
<action>Escrever modelo preenchido para: {output_folder}/deep-dive-{{sanitized_target_name}}.md</action>
<action>Validar completude do documento de mergulho profundo</action>

<template-output>deep_dive_documentation</template-output>

<action>Atualizar arquivo de estado: - Adicionar ao array deep_dive_targets: {"target_name": "{{target_name}}", "target_path": "{{target_path}}", "files_analyzed": {{file_count}}, "output_file": "deep-dive-{{sanitized_target_name}}.md", "timestamp": "{{now}}"} - Adicionar saída para outputs_generated - Atualizar timestamp last_updated
</action>
</step>

<step n="13f" goal="Atualizar índice mestre com link de mergulho profundo">
  <action>Ler index.md existente</action>

<action>Verificar se a seção "Documentação de Mergulho Profundo" existe</action>

  <check if="section does not exist">
    <action>Adicionar nova seção após "Documentação Gerada":

## Documentação de Mergulho Profundo

Análise exaustiva detalhada de áreas específicas:

    </action>

  </check>

<action>Adicionar link para nova doc de mergulho profundo:

- [Mergulho Profundo {{target_name}}](./deep-dive-{{sanitized_target_name}}.md) - Análise abrangente de {{target_description}} ({{file_count}} arquivos, {{total_loc}} LOC) - Gerado {{date}}
  </action>

  <action>Atualizar metadados do índice:
  Última Atualização: {{date}}
  Mergulhos Profundos: {{deep_dive_count}}
  </action>

  <action>Salvar index.md atualizado</action>

  <template-output>updated_index</template-output>
  </step>

<step n="13g" goal="Oferecer para continuar ou completar">
  <action>Exibir resumo:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Documentação de Mergulho Profundo Completa! ✓

**Gerado:** {output_folder}/deep-dive-{{target_name}}.md
**Arquivos Analisados:** {{file_count}}
**Linhas de Código Varridas:** {{total_loc}}
**Tempo Gasto:** ~{{duration}}

**Documentação Inclui:**

- Inventário de arquivo completo com todas as exportações
- Grafo de dependência e fluxo de dados
- Pontos de integração e contratos de API
- Análise de teste e cobertura
- Código relacionado e oportunidades de reuso
- Orientação de implementação

**Índice Atualizado:** {output_folder}/index.md agora inclui link para este mergulho profundo

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
</action>

<ask>Você gostaria de:

1. **Fazer mergulho profundo em outra área** - Analisar outro recurso/módulo/pasta
2. **Terminar** - Completar fluxo de trabalho

Sua escolha [1/2]:
</ask>

  <action if="user selects 1">
    <action>Limpar deep_dive_target atual</action>
    <action>Ir para Passo 13a (selecionar nova área)</action>
  </action>

  <action if="user selects 2">
    <action>Exibir mensagem final:

Toda documentação de mergulho profundo completa!

**Índice Mestre:** {output_folder}/index.md
**Mergulhos Profundos Gerados:** {{deep_dive_count}}

Estas docs abrangentes estão agora prontas para:

- Revisão de arquitetura
- Planejamento de implementação
- Entendimento de código
- Criação de PRD Brownfield

Obrigado por usar o fluxo de trabalho document-project!
</action>
<action>Sair do fluxo de trabalho</action>
</action>
</step>
</step>

</workflow>
