# {{project_name}} - Análise de Árvores de Origem

**Data:** {{date}}

## Visão geral

{{source_tree_overview}}

{{#if is_multi_part}}

## Estrutura múltipla

Este projeto está organizado em {{parts_count}} partes distintas:

BMADPROTECT072End}

- **{{part_name}}** (`{{root_path}}`): {{purpose}}
{{/each}}
{{/if}}

## Estrutura completa do diretório

```
{{complete_source_tree}}

```

## Directórios Críticos

{{#each critical_folders}}

### `{{folder_path}}`

{{description}}

**Pós:** {{purpose}}
**Contém:** {{contents_summary}}
BMADPROTECT063end}**Pontos de entrada:** BMADPROTECT062end}BMADPROTECT061end}
{{#if integration_note}}**Integração:** BMADPROTECT059End}BMADPROTECT058End}

{{/each}}

{{#if is_multi_part}}

## Árvores específicas da parte

{{#each project_parts}}

### {{part_name}} Estrutura

```
{{source_tree}}

```

**Diretórios-chave:**
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

## Pontos de entrada

{{#if is_single_part}}

- **Entrada principal:** `{{main_entry_point}}`
{{#if additional_entry_points}}
- **Adicional:**
{{#each additional_entry_points}}
BMADPROTECT078end BMADPROTECT039end}
{{/each}}
{{/if}}
BMADPROTECT036FEND}
{{#each project_parts}}

### {{part_name}}

- **Ponto de entrada:** `{{entry_point}}`
- **Bootstrap:** {{bootstrap_description}}
{{/each}}
{{/if}}

## Padrões de Organização de Ficheiros

BMADPROTECT030FEND}

## Tipos de Ficheiros de Chave

{{#each file_type_patterns}}

### {{file_type}}

- **Pattern:** `{{pattern}}`
- **Composto:** {{purpose}}
- **Exemplos:** {{examples}}
{{/each}}

## Localidades do Activo

{{#if has_assets}}
{{#each asset_locations}}

- **{{asset_type}}**: ficheiros `{{location}}` ({{file_count}}, {{total_size}})
{{/each}}
{{else}}
Não foram detectados activos significativos.
{{/if}}

## Arquivos de configuração

{{#each config_files}}

- **`{{path}}`**: {{description}}
{{/each}}

## Notas relativas ao desenvolvimento

{{development_notes}}

---

* Gerado usando o método BMAD `document-project` workflow*
