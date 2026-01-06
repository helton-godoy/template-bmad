# {{target_name}} - Documentação de Mergulho Profundo

**Gerado:** {{date}}
**Escopo:** {{target_path}}
**Arquivos Analisados:** {{file_count}}
**Linhas de Código:** {{total_loc}}
**Modo de Fluxo de Trabalho:** Mergulho Profundo Exaustivo

## Visão Geral

{{target_description}}

**Propósito:** {{target_purpose}}
**Principais Responsabilidades:** {{responsibilities}}
**Pontos de Integração:** {{integration_summary}}

## Inventário Completo de Arquivos

{{#each files_in_inventory}}

### {{file_path}}

**Propósito:** {{purpose}}
**Linhas de Código:** {{loc}}
**Tipo de Arquivo:** {{file_type}}

**O que Futuros Contribuidores Devem Saber:** {{contributor_note}}

**Exportações:**
{{#each exports}}

- `{{signature}}` - {{description}}
  {{/each}}

**Dependências:**
{{#each imports}}

- `{{import_path}}` - {{reason}}
  {{/each}}

**Usado Por:**
{{#each dependents}}

- `{{dependent_path}}`
  {{/each}}

**Detalhes Chave de Implementação:**

```{{language}}
{{key_code_snippet}}
```

{{implementation_notes}}

**Padrões Usados:**
{{#each patterns}}

- {{pattern_name}}: {{pattern_description}}
  {{/each}}

**Gerenciamento de Estado:** {{state_approach}}

**Efeitos Colaterais:**
{{#each side_effects}}

- {{effect_type}}: {{effect_description}}
  {{/each}}

**Tratamento de Erros:** {{error_handling_approach}}

**Testes:**

- Arquivo de Teste: {{test_file_path}}
- Cobertura: {{coverage_percentage}}%
- Abordagem de Teste: {{test_approach}}

**Comentários/TODOs:**
{{#each todos}}

- Linha {{line_number}}: {{todo_text}}
  {{/each}}

---

{{/each}}

## Checklist do Contribuidor

- **Riscos & Pegadinhas:** {{risks_notes}}
- **Passos de Verificação Pré-mudança:** {{verification_steps}}
- **Testes Sugeridos Antes de PR:** {{suggested_tests}}

## Arquitetura & Padrões de Design

### Organização de Código

{{organization_approach}}

### Padrões de Design

{{#each design_patterns}}

- **{{pattern_name}}**: {{usage_description}}
  {{/each}}

### Estratégia de Gerenciamento de Estado

{{state_management_details}}

### Filosofia de Tratamento de Erros

{{error_handling_philosophy}}

### Estratégia de Testes

{{testing_strategy}}

## Fluxo de Dados

{{data_flow_diagram}}

### Pontos de Entrada de Dados

{{#each entry_points}}

- **{{entry_name}}**: {{entry_description}}
  {{/each}}

### Transformações de Dados

{{#each transformations}}

- **{{transformation_name}}**: {{transformation_description}}
  {{/each}}

### Pontos de Saída de Dados

{{#each exit_points}}

- **{{exit_name}}**: {{exit_description}}
  {{/each}}

## Pontos de Integração

### APIs Consumidas

{{#each apis_consumed}}

- **{{api_endpoint}}**: {{api_description}}
  - Método: {{method}}
  - Autenticação: {{auth_requirement}}
  - Resposta: {{response_schema}}
    {{/each}}

### APIs Expostas

{{#each apis_exposed}}

- **{{api_endpoint}}**: {{api_description}}
  - Método: {{method}}
  - Requisição: {{request_schema}}
  - Resposta: {{response_schema}}
    {{/each}}

### Estado Compartilhado

{{#each shared_state}}

- **{{state_name}}**: {{state_description}}
  - Tipo: {{state_type}}
  - Acessado Por: {{accessors}}
    {{/each}}

### Eventos

{{#each events}}

- **{{event_name}}**: {{event_description}}
  - Tipo: {{publish_or_subscribe}}
  - Carga: {{payload_schema}}
    {{/each}}

### Acesso a Banco de Dados

{{#each database_operations}}

- **{{table_name}}**: {{operation_type}}
  - Consultas: {{query_patterns}}
  - Índices Usados: {{indexes}}
    {{/each}}

## Grafo de Dependência

{{dependency_graph_visualization}}

### Pontos de Entrada (Não Importados por Outros no Escopo)

{{#each entry_point_files}}

- {{file_path}}
  {{/each}}

### Nós Folha (Não Importam Outros no Escopo)

{{#each leaf_files}}

- {{file_path}}
  {{/each}}

### Dependências Circulares

{{#if has_circular_dependencies}}
⚠️ Dependências circulares detectadas:
{{#each circular_deps}}

- {{cycle_description}}
  {{/each}}
  {{else}}
  ✓ Nenhuma dependência circular detectada
  {{/if}}

## Análise de Testes

### Resumo de Cobertura de Teste

- **Declarações:** {{statements_coverage}}%
- **Ramos:** {{branches_coverage}}%
- **Funções:** {{functions_coverage}}%
- **Linhas:** {{lines_coverage}}%

### Arquivos de Teste

{{#each test_files}}

- **{{test_file_path}}**
  - Testes: {{test_count}}
  - Abordagem: {{test_approach}}
  - Estratégia de Mocking: {{mocking_strategy}}
    {{/each}}

### Utilitários de Teste Disponíveis

{{#each test_utilities}}

- `{{utility_name}}`: {{utility_description}}
  {{/each}}

### Lacunas de Teste

{{#each testing_gaps}}

- {{gap_description}}
  {{/each}}

## Código Relacionado & Oportunidades de Reuso

### Recursos Similares em Outro Lugar

{{#each similar_features}}

- **{{feature_name}}** (`{{feature_path}}`)
  - Similaridade: {{similarity_description}}
  - Pode Referenciar Para: {{reference_use_case}}
    {{/each}}

### Utilitários Reutilizáveis Disponíveis

{{#each reusable_utilities}}

- **{{utility_name}}** (`{{utility_path}}`)
  - Propósito: {{utility_purpose}}
  - Como Usar: {{usage_example}}
    {{/each}}

### Padrões a Seguir

{{#each patterns_to_follow}}

- **{{pattern_name}}**: Referencie `{{reference_file}}` para implementação
  {{/each}}

## Notas de Implementação

### Observações de Qualidade de Código

{{#each quality_observations}}

- {{observation}}
  {{/each}}

### TODOs e Trabalho Futuro

{{#each all_todos}}

- **{{file_path}}:{{line_number}}**: {{todo_text}}
  {{/each}}

### Problemas Conhecidos

{{#each known_issues}}

- {{issue_description}}
  {{/each}}

### Oportunidades de Otimização

{{#each optimizations}}

- {{optimization_suggestion}}
  {{/each}}

### Dívida Técnica

{{#each tech_debt_items}}

- {{debt_description}}
  {{/each}}

## Orientação de Modificação

### Para Adicionar Nova Funcionalidade

{{modification_guidance_add}}

### Para Modificar Funcionalidade Existente

{{modification_guidance_modify}}

### Para Remover/Deprecar

{{modification_guidance_remove}}

### Checklist de Teste para Mudanças

{{#each testing_checklist_items}}

- [ ] {{checklist_item}}
      {{/each}}

---

_Gerado pelo fluxo de trabalho `document-project` (modo mergulho profundo)_
_Documentação Base: docs/index.md_
_Data da Varredura: {{date}}_
_Modo de Análise: Exaustivo_
