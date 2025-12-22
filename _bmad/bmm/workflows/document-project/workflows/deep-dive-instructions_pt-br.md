# Instruções de documentação de mergulho profundo

<workflow>

<critical>Este fluxo de trabalho realiza documentação exaustiva de mergulho profundo de áreas específicas</critical>
<critical> Chamado por: ../document-project/instructions.md roteador </critical>
BMADPROTECT135End somente modo BMADPROTECT080End

<step n="13" goal="Deep-dive documentation of specific area" if="workflow_mode == deep_dive">
O modo <critical>Deep-dive requer revisão literal de arquivo completo. Amostragem, adivinhação ou depender apenas da saída de ferramentas é FORBIDEN.</critical>
<action>Carrega estrutura de projeto existente de index.md e project-parts.json (se existir)</action>
<action>A análise de árvores de origem para entender áreas disponíveis</action>

<step n="13a" goal="Identify area for deep-dive">
<action>A Analisar a documentação existente para sugerir opções de mergulho profundo</action>

<ask> Em que área gostarias de mergulhar?

**Áreas sugeridas com base na estrutura do projeto:**

{{#if has_api_routes}}

## Rotas API (BMADPROTECT129End} foram encontradas)

{{#each api_route_groups}}
{{group_index}}. {{group_name}} - {{endpoint_count}} em `{{path}}`
{{/each}}
{{/if}}

{{#if has_feature_modules}}

## Módulos de Característica ({{feature_count}})

{{#each feature_modules}}
BMADPROTECT119end}. {{module_name}} - {{file_count}} ficheiros no `{{path}}`
{{/each}}
{{/if}}

{{#if has_ui_components}}

### Áreas de Componente de IU

{{#each component_groups}}
BMADPROTECT112nd}. {{group_name}} - {{component_count}} componentes em `{{path}}`
{{/each}}
{{/if}}

{{#if has_services}}

### Serviços/Lógica de negócios

{{#each service_groups}}
BMADPROTECT105end}. {{service_name}} - `{{path}}`
{{/each}}
{{/if}}

**Ou especifique personalizado:**

- Caminho da pasta (por exemplo, "client/src/features/dashboard")
- Localização do ficheiro (por exemplo, "server/src/api/users.ts")
- Nome do recurso (por exemplo, "sistema de autenticação")

Digite sua escolha (número ou caminho personalizado):
</ask>

<action> Processar a entrada do usuário para determinar: - target type: "pasta" "! Lista de todos os ficheiros a analisar
</action>

<action>Store como {{deep_dive_target}}</action>

Confirmação <action>Display:
Target: {{target_name}}
Type: {{target_type}}
Path: {{target_path}}
Arquivos estimados para analisar: {{estimated_file_count}}

Isto irá ler TODOS os arquivos nesta área. Prossigam?
</action>

<action if="user confirms 'n'">Retorno ao Passo 13a (selecionar área diferente)</action>
</step>

<step n="13b" goal="Comprehensive exhaustive scan of target area">
<action>Set scan mode = "exaustivo"</action>
<action> Iniciar arquivo inventário = []</action>
<critical>Você deve ler todas as linhas de cada arquivo no escopo e capturar uma explicação em linguagem simples (o que o arquivo faz, efeitos colaterais, por que isso importa) que os futuros agentes de desenvolvimento podem agir. Sem atalhos. </critical>

<check if="target_type == folder">
<action> Obtenha uma lista completa de arquivos recursivos de {{target_path}}</action>
<action>Filter out: node  modules/, git/, dist/, build/, coverage/, *. min.js, *. map</action>
<action>For TODOS os arquivos restantes na pasta:
- Leia o conteúdo completo do arquivo (todas as linhas)
- Extrair todas as exportações (funções, classes, tipos, interfaces, constantes)
- Extrair todas as importações (dependências)
- Identificar finalidade a partir de comentários e estrutura de código
- Escreva 1-2 frases (mínimo) em linguagem natural descrevendo comportamento, efeitos colaterais, suposições, e qualquer coisa que um desenvolvedor deve saber antes de modificar o arquivo
- Extrair assinaturas function com tipos de parâmetros e tipos de retorno
- Observe quaisquer TODOS, FIXMEs ou comentários
- Identificar padrões (ganchos, componentes, serviços, controladores, etc.)
- Captura por ficheiro de orientação do contribuinte: `contributor_note`, `risks`, `verification_steps`, `suggested_tests`
- Guardar no arquivo inventário
</action>
</check>

<check if="target_type == file">
<action>Leia o arquivo completo no {{target_path}}</action>
<action>Extraia todas as informações como acima </action>
<action>Leia todos os arquivos que importa (seguir import chain 1 level deep)</action>
<action>Encontrar todos os arquivos que importER este arquivo (dependentes via grep)</action>
<action>Store all in file inventory</action>
</check>

<check if="target_type == api_group">
<action>Identify all route/controller files in API group</action>
<action>Leia todos os manipuladores de rota completamente </action>
<action>Ler middleware associado, controladores, serviços</action>
<action>Leia modelos de dados e esquemas usados</action>
<action>Extrair esquemas completos de pedido/resposta</action>
<action> Requisitos de autenticação e autorização de documentos</action>
<action>Store tudo em arquivo inventário</action>
</check>

<check if="target_type == feature">
<action>Search codebase para todos os arquivos relacionados ao nome do recurso</action>
    <action>Include: UI componentes, endpoints de API, modelos, serviços, testes</action>
BMADPROTECT010EndLeia cada arquivo completamente</action>
<action>Store a