# Índice de Documentação {{project_name}}

**Tipo:** {{repository_type}}{{#if is_multi_part}} com {{parts_count}} partes{{/if}}
**Linguagem Primária:** {{primary_language}}
**Arquitetura:** {{architecture_type}}
**Última Atualização:** {{date}}

## Visão Geral do Projeto

{{project_description}}

{{#if is_multi_part}}

## Estrutura do Projeto

Este projeto consiste em {{parts_count}} partes:

{{#each project_parts}}

### {{part_name}} ({{part_id}})

- **Tipo:** {{project_type}}
- **Localização:** `{{root_path}}`
- **Pilha Técnica:** {{tech_stack_summary}}
- **Ponto de Entrada:** {{entry_point}}
  {{/each}}

## Integração Entre Partes

{{integration_summary}}

{{/if}}

## Referência Rápida

{{#if is_single_part}}

- **Pilha Técnica:** {{tech_stack_summary}}
- **Ponto de Entrada:** {{entry_point}}
- **Padrão de Arquitetura:** {{architecture_pattern}}
- **Banco de Dados:** {{database}}
- **Implantação:** {{deployment_platform}}
  {{else}}
  {{#each project_parts}}

### Ref Rápida {{part_name}}

- **Pilha:** {{tech_stack_summary}}
- **Entrada:** {{entry_point}}
- **Padrão:** {{architecture_pattern}}
  {{/each}}
  {{/if}}

## Documentação Gerada

### Documentação Central

- [Visão Geral do Projeto](./project-overview.md) - Resumo executivo e arquitetura de alto nível
- [Análise da Árvore de Código](./source-tree-analysis.md) - Estrutura de diretórios anotada

{{#if is_single_part}}

- [Arquitetura](./architecture.md) - Arquitetura técnica detalhada
- [Inventário de Componentes](./component-inventory.md) - Catálogo de componentes principais{{#if has_ui_components}} e elementos de UI{{/if}}
- [Guia de Desenvolvimento](./development-guide.md) - Configuração local e fluxo de trabalho de desenvolvimento
  {{#if has_api_docs}}- [Contratos de API](./api-contracts.md) - Endpoints de API e esquemas{{/if}}
  {{#if has_data_models}}- [Modelos de Dados](./data-models.md) - Esquema de banco de dados e modelos{{/if}}
  {{else}}

### Documentação Específica de Parte

{{#each project_parts}}

#### {{part_name}} ({{part_id}})

- [Arquitetura](./architecture-{{part_id}}.md) - Arquitetura técnica para {{part_name}}
  {{#if has_components}}- [Componentes](./component-inventory-{{part_id}}.md) - Catálogo de componentes{{/if}}
- [Guia de Desenvolvimento](./development-guide-{{part_id}}.md) - Configuração e fluxo de trabalho dev
  {{#if has_api}}- [Contratos de API](./api-contracts-{{part_id}}.md) - Documentação de API{{/if}}
  {{#if has_data}}- [Modelos de Dados](./data-models-{{part_id}}.md) - Arquitetura de dados{{/if}}
  {{/each}}

### Integração

- [Arquitetura de Integração](./integration-architecture.md) - Como as partes se comunicam
- [Metadados de Partes do Projeto](./project-parts.json) - Estrutura legível por máquina
  {{/if}}

### Documentação Opcional

{{#if has_deployment_guide}}- [Guia de Implantação](./deployment-guide.md) - Processo de implantação e infraestrutura{{/if}}
{{#if has_contribution_guide}}- [Guia de Contribuição](./contribution-guide.md) - Diretrizes e padrões de contribuição{{/if}}

## Documentação Existente

{{#if has_existing_docs}}
{{#each existing_docs}}

- [{{title}}]({{path}}) - {{description}}
  {{/each}}
  {{else}}
  Nenhum arquivo de documentação existente foi encontrado no projeto.
  {{/if}}

## Começando

{{#if is_single_part}}

### Pré-requisitos

{{prerequisites}}

### Configuração

```bash
{{setup_commands}}
```

### Rodar Localmente

```bash
{{run_commands}}
```

### Rodar Testes

```bash
{{test_commands}}
```

{{else}}
{{#each project_parts}}

### Configuração {{part_name}}

**Pré-requisitos:** {{prerequisites}}

**Instalar & Rodar:**

```bash
cd {{root_path}}
{{setup_command}}
{{run_command}}
```

{{/each}}
{{/if}}

## Para Desenvolvimento Assistido por IA

Esta documentação foi gerada especificamente para permitir que agentes de IA entendam e estendam esta base de código.

### Ao Planejar Novos Recursos:

**Recursos apenas UI:**
{{#if is_multi_part}}→ Referência: `architecture-{{ui_part_id}}.md`, `component-inventory-{{ui_part_id}}.md`{{else}}→ Referência: `architecture.md`, `component-inventory.md`{{/if}}

**Recursos API/Backend:**
{{#if is_multi_part}}→ Referência: `architecture-{{api_part_id}}.md`, `api-contracts-{{api_part_id}}.md`, `data-models-{{api_part_id}}.md`{{else}}→ Referência: `architecture.md`{{#if has_api_docs}}, `api-contracts.md`{{/if}}{{#if has_data_models}}, `data-models.md`{{/if}}{{/if}}

**Recursos full-stack:**
→ Referência: Todas as docs de arquitetura{{#if is_multi_part}} + `integration-architecture.md`{{/if}}

**Mudanças de implantação:**
{{#if has_deployment_guide}}→ Referência: `deployment-guide.md`{{else}}→ Revise configs de CI/CD no projeto{{/if}}

---

_Documentação gerada pelo fluxo de trabalho `document-project` do Método BMAD_
