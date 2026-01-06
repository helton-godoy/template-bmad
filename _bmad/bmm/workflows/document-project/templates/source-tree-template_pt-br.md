# {{project_name}} - Análise da Árvore de Código

**Data:** {{date}}

## Visão Geral

{{source_tree_overview}}

{{#if is_multi_part}}

## Estrutura Multi-Parte

Este projeto é organizado em {{parts_count}} partes distintas:

{{#each project_parts}}

- **{{part_name}}** (`{{root_path}}`): {{purpose}}
  {{/each}}
  {{/if}}

## Estrutura Completa de Diretórios

```
{{complete_source_tree}}
```

## Diretórios Críticos

{{#each critical_folders}}

### `{{folder_path}}`

{{description}}

**Propósito:** {{purpose}}
**Contém:** {{contents_summary}}
{{#if entry_points}}**Pontos de Entrada:** {{entry_points}}{{/if}}
{{#if integration_note}}**Integração:** {{integration_note}}{{/if}}

{{/each}}

{{#if is_multi_part}}

## Árvores Específicas de Parte

{{#each project_parts}}

### Estrutura {{part_name}}

```
{{source_tree}}
```

**Diretórios Chave:**
{{#each critical_directories}}

- **`{{path}}`**: {{description}}
  {{/each}}

{{/each}}

## Pontos de Integração

{{#each integration_points}}

### {{from_part}} → {{to_part}}

- **Localização:** `{{integration_path}}`
- **Tipo:** {{integration_type}}
- **Detalhes:** {{details}}
  {{/each}}

{{/if}}

## Pontos de Entrada

{{#if is_single_part}}

- **Entrada Principal:** `{{main_entry_point}}`
  {{#if additional_entry_points}}
- **Adicional:**
  {{#each additional_entry_points}}
  - `{{path}}`: {{description}}
    {{/each}}
    {{/if}}
    {{else}}
    {{#each project_parts}}

### {{part_name}}

- **Ponto de Entrada:** `{{entry_point}}`
- **Bootstrap:** {{bootstrap_description}}
  {{/each}}
  {{/if}}

## Padrões de Organização de Arquivos

{{file_organization_patterns}}

## Tipos de Arquivos Chave

{{#each file_type_patterns}}

### {{file_type}}

- **Padrão:** `{{pattern}}`
- **Propósito:** {{purpose}}
- **Exemplos:** {{examples}}
  {{/each}}

## Localizações de Ativos

{{#if has_assets}}
{{#each asset_locations}}

- **{{asset_type}}**: `{{location}}` ({{file_count}} arquivos, {{total_size}})
  {{/each}}
  {{else}}
  Nenhum ativo significativo detectado.
  {{/if}}

## Arquivos de Configuração

{{#each config_files}}

- **`{{path}}`**: {{description}}
  {{/each}}

## Notas para Desenvolvimento

{{development_notes}}

---

_Gerado usando o fluxo de trabalho `document-project` do Método BMAD_
