# {{target_name}} - Documentação de mergulho profundo

**Geração:** {{date}}
**Scope:** {{target_path}}
**Arquivos analisados:** {{file_count}}
**Linhas de código:** {{total_loc}}
**Modo de fluxo de trabalho:**

## Visão geral

{{target_description}}

**Composição:** {{target_purpose}}
**Responsabilidades-chave:** {{responsibilities}}
**Pontos de integração:** {{integration_summary}}

## Inventário de Ficheiros Completos

{{#each files_in_inventory}}

### {{file_path}}

**Composto:** {{purpose}}
**Linhas de código:** {{loc}}
**Tipo de ficheiro:** {{file_type}}

**O que os futuros contribuintes devem saber:** {{contributor_note}}

**Exportações:**
{{#each exports}}

- `{{signature}}` - {{description}}
{{/each}}

**Dependências:**
{{#each imports}}

`{{import_path}}` {{reason}}
{{/each}}

**Usado por:**
{{#each dependents}}

- `{{dependent_path}}`
{{/each}}

**Key Implementation Details:**

```{{language}}
{{key_code_snippet}}

```

{{implementation_notes}}

**Padrões usados:**
{{#each patterns}}

- BMADPROTECT128End}: BMADPROTECT127End}
{{/each}}

**Gestão do Estado:** {{state_approach}}

**Efeitos secundários:**
{{#each side_effects}}

{{effect_type}}: {{effect_description}}
{{/each}}

**Manuseamento de erros:** {{error_handling_approach}}

**Testação:**

- Arquivo de teste: {{test_file_path}}
- Coverage: {{coverage_percentage}}
- Método de ensaio {{test_approach}}

**Comentários/TODOs:**
{{#each todos}}

- Linha {{line_number}}: {{todo_text}}
{{/each}}

---

{{/each}}

## Lista de Verificação do Contribuinte

- **Risks & Tickets:** {{risks_notes}}
- **Passos de verificação pré-mudança:** {{verification_steps}}
- **Testes sugeridos antes da RP:** {{suggested_tests}}

## Padrões de Arquitetura e Design

### Organização de Código

{{organization_approach}}

### Padrões de desenho

{{#each design_patterns}}

- **{{pattern_name}}**: {{usage_description}}
{{/each}}

### Estratégia de Gestão Estadual

{{state_management_details}}

### Erro ao lidar com a Filosofia

{{error_handling_philosophy}}

### Estratégia de ensaio

{{testing_strategy}}

## Fluxo de dados

{{data_flow_diagram}}

### Pontos de entrada de dados

{{#each entry_points}}

- **{{entry_name}}**: {{entry_description}}
{{/each}}

### Transformações de dados

{{#each transformations}}

- **{{transformation_name}}**: {{transformation_description}}
{{/each}}

### Pontos de saída de dados

BMADPROTECT091FEND}

- **{{exit_name}}**: {{exit_description}}
{{/each}}

## Pontos de Integração

### APIs Consumadas

{{#each apis_consumed}}

- **{{api_endpoint}}**: {{api_description}}
  - Method: {{method}}
  - Authentication: {{auth_requirement}}
  - Response: {{response_schema}}
{{/each}}

### APIs Expostas

{{#each apis_exposed}}

- **{{api_endpoint}}**: {{api_description}}
  - Method: {{method}}
BMADPROTECT164end BMADPROTECT076end}
BMADPROTECT163end BMADPROTECT075end}
{{/each}}

### Estado partilhado

{{#each shared_state}}

- **{{state_name}}**: {{state_description}}
BMADPROTECT162end BMADPROTECT070end}
- Acessado por: {{accessors}}
{{/each}}

### Eventos

{{#each events}}

- **{{event_name}}**: {{event_description}}
BMADPROTECT161end BMADPROTECT064end}
  - Payload: {{payload_schema}}
{{/each}}

### Acesso à Base de Dados

{{#each database_operations}}

- **{{table_name}}**: {{operation_type}}
BMADPROTECT159end BMADPROTECT058end}
- Índices usados: {{indexes}}
{{/each}}

## Gráfico de Dependência

{{dependency_graph_visualization}}

### Pontos de entrada (não importados por outros no âmbito de aplicação)

{{#each entry_point_files}}

- {{file_path}}
{{/each}}

### Nó de Folha (Não Importar Outros no Escopo)

{{#each leaf_files}}

{{file_path}}
{{/each}}

### Dependências Circulares

{{#if has_circular_dependencies}}
Dependências circulares detectadas:
{{#each circular_deps}}

{{cycle_description}}
{{/each}}
{{else}}
✓ Nenhuma dependência circular detectada
{{/if}}

## Análise de ensaio

### Resumo da cobertura de ensaio

- **Declarações:** {{statements_coverage}}
- **Branches:** {{branches_coverage}}
- **Funções:** {{functions_coverage}}
- **Linhas:** {{lines_coverage}}

### Ficheiros de Teste

{{#each test_files}}

- **{{test_file_path}}**
  - Tests: {{test_count}}
  - Approach: {{test_approach}}
- Estratégia de Mocking: {{mocking_strategy}
{{/each}}

### Utilitários de Teste Disponíveis

{{#each test_utilities}}

- `{{utility_name}}`: {{utility_description}}
BMADPROTECT030FEND}

### Intervalos de ensaio

{{#each testing_gaps}}

BMADPROTECT028FEND}
{{/each}}

## Código relacionado e oportunidades de reutilização

### Características semelhantes em outros lugares

{{#each similar_features}}

- **{{feature_name}}** (`{{feature_path}}`)
  - Similarity: {{similarity_description}}
- Referência de lata para: {{reference_use_case}}
{{/each}}

### Utilitários reutilizáveis disponíveis

{{#each reusable_utilities}}

- **{{utility_name}}** (`{{utility_path}}`)
BMADPROTECT154end BMADPROTECT019end}
- Como utilizar: {{usage_example}ER}
{{/each}}

### Padrões a Seguir

{{#each patterns_to_follow}}

- **{{pattern_name}}**: Referência `{{reference_file}}` para implementation
{{/each}}

## Implementation Notas

### Observações de qualidade do código

{{#each quality_observations}}

- {{observation}}
{{/each}}

### TOD