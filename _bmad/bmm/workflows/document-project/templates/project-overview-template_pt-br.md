# {{project_name}} - Visão Geral do Projeto

**Data:** {{date}}
**Tipo:** {{project_type}}
**Arquitetura:** {{architecture_type}}

## Resumo Executivo

{{executive_summary}}

## Classificação do Projeto

- **Tipo de Repositório:** {{repository_type}}
- **Tipo(s) de Projeto:** {{project_types_list}}
- **Linguagem(ns) Primária(s):** {{primary_languages}}
- **Padrão de Arquitetura:** {{architecture_pattern}}

{{#if is_multi_part}}

## Estrutura Multi-Parte

Este projeto consiste em {{parts_count}} partes distintas:

{{#each project_parts}}

### {{part_name}}

- **Tipo:** {{project_type}}
- **Localização:** `{{root_path}}`
- **Propósito:** {{purpose}}
- **Pilha Técnica:** {{tech_stack}}
  {{/each}}

### Como as Partes se Integram

{{integration_description}}
{{/if}}

## Resumo da Pilha Tecnológica

{{#if is_single_part}}
{{technology_table}}
{{else}}
{{#each project_parts}}

### Pilha {{part_name}}

{{technology_table}}
{{/each}}
{{/if}}

## Principais Recursos

{{key_features}}

## Destaques da Arquitetura

{{architecture_highlights}}

## Visão Geral de Desenvolvimento

### Pré-requisitos

{{prerequisites}}

### Começando

{{getting_started_summary}}

### Comandos Principais

{{#if is_single_part}}

- **Instalar:** `{{install_command}}`
- **Dev:** `{{dev_command}}`
- **Build:** `{{build_command}}`
- **Teste:** `{{test_command}}`
  {{else}}
  {{#each project_parts}}

#### {{part_name}}

- **Instalar:** `{{install_command}}`
- **Dev:** `{{dev_command}}`
  {{/each}}
  {{/if}}

## Estrutura do Repositório

{{repository_structure_summary}}

## Mapa de Documentação

Para informações detalhadas, veja:

- [index.md](./index.md) - Índice mestre de documentação
- [architecture.md](./architecture{{#if is_multi_part}}-{part_id}{{/if}}.md) - Arquitetura detalhada
- [source-tree-analysis.md](./source-tree-analysis.md) - Estrutura de diretórios
- [development-guide.md](./development-guide{{#if is_multi_part}}-{part_id}{{/if}}.md) - Fluxo de trabalho de desenvolvimento

---

_Gerado usando o fluxo de trabalho `document-project` do Método BMAD_
