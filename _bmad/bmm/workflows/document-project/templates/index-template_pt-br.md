# {{project_name}} Índice da documentação

**Tipo:** {{repository_type}}{{#if is_multi_part}} com {{parts_count}} partes{{/if}}
**Língua Primária:** {{primary_language}}
**Arquitetura:** {{architecture_type}}
**Última atualização:** BMADPROTECT127End}

## Visão geral do projeto

{{project_description}}

{{#if is_multi_part}}

## Estrutura do projeto

Este projeto consiste em {{parts_count}} partes:

{{#each project_parts}}

### {{part_name}} ({{part_id}})

- **Tipo:** {{project_type}}
- **Localização:** `{{root_path}}`
- **Tech Stack:** {{tech_stack_summary}}
- **Ponto de entrada:** {{entry_point}}
{{/each}}

## Integração cruzada

{{integration_summary}}

{{/if}}

## Referência rápida

{{#if is_single_part}}

- **Tech Stack:** {{tech_stack_summary}}
- **Ponto de entrada:** {{entry_point}}
- **Padrão de arquitectura:** {{architecture_pattern}}
- **Database:** {{database}}
- **Implantação:** {{deployment_platform}}
{{else}}
{{#each project_parts}}

### {{part_name}} Ref rápido

- **Stack:** {{tech_stack_summary}}
- **Entrada:** {{entry_point}}
- **Pattern:** {{architecture_pattern}}
{{/each}}
{{/if}}

## Documentação gerada

### Documentação Principal

- [Observação do projecto](./project-overview.md) - Resumo executivo e arquitetura de alto nível
- [Análise da Árvore Fonte](./source-tree-analysis.md) - Estrutura de diretório anotada

{{#if is_single_part}}

- [Arquitectura](./architecture.md) - Arquitetura técnica detalhada
- [Inventário Componente](./component-inventory.md) - Catálogo de componentes principais{{#if has_ui_components}} e elementos UIBADPROTECT098END}
- [Guia de Desenvolvimento](./development-guide.md) - Configuração local e fluxo de trabalho de desenvolvimento
{{#if has_api_docs}}- [API Contracts](./api-contracts.md) - Endpoints API e esquemas{{/if}}
{{#if has_data_models}}- [Data Models](./data-models.md) - Esquema e modelos de banco de dados{{/if}}
{{else}}

### Documentação Específica de Parte

{{#each project_parts}}

#### {{part_name}} ({{part_id}})

- [Arquitectura](./architecture-{{part_id}}.md) - Arquitetura técnica para {{part_name}}
{{#if has_components}}- [Componentes](./component-inventory-{{part_id}}.md) - Catálogo de componentes{{/if}}
- [Guia de Desenvolvimento](./development-guide-{{part_id}}.md) - Configuração e fluxo de trabalho dev
{{#if has_api}}- [Contratos APIBADPROTECT036END - Documentação APIBMADPROTECT085End}
{{#if has_data}}- [Data Models](./data-models-{{part_id}}.md) - Arquitetura de dados{{/if}}
{{/each}}

### Integração

- [Arquitectura de integração](./integration-architecture.md) - Como as peças se comunicam
- [Project Parts Metadata](./project-parts.json) - Estrutura legível por máquina
{{/if}}

### Documentação Opcional

{{#if has_deployment_guide}}- [Guia de implantação](./deployment-guide.md) - Processo de implantação e infraestrutura{{/if}}
{{#if has_contribution_guide}}- [Guia de contribuição](./contribution-guide.md) - Orientações e normas de contribuição{{/if}}

## Documentação existente

{{#if has_existing_docs}}
{{#each existing_docs}}

BMADPROTECT074End
BMADPROTECT072End}
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

### Executar Localmente

```bash
{{run_commands}}

```

### Executar testes

```bash
{{test_commands}}

```

{{else}}
{{#each project_parts}}

### {{part_name}} Configurar

**Prerequisitos:** {{prerequisites}}

**Instalar e executar:**

```bash
cd {{root_path}}
{{setup_command}}
{{run_command}}

```

{{/each}}
{{/if}}

## Para o desenvolvimento assistido por IA

Esta documentação foi gerada especificamente para permitir que os agentes de IA entendessem e estendessem esta base de código.

### Quando Planning novas características:

**Características exclusivas de UI:**
{{#if is_multi_part}}→ Referência: `architecture-{{ui_part_id}}.md`, `component-inventory-{{ui_part_id}}.md`BADPROTECT060END}→ Referência: `architecture.md`, `component-inventory.md`BADPROTECT059End}

**API/Backend features:**
{{#if is_multi_part}}→ Referência: BMADPROTECT013End, BMADPROTECT012End, `data-models-{{api_part_id}}.md`BADPROTECT057End}→ Referência: `architecture.md`BADPROTECT056END}, `api-contracts.md`BADPROTECT055END}{{#if has_data_models}}, `data-models.md`BADPROTECT053END}{{/if}}

**Características completas:**
→ Referência: Todos os documentos de arquitetura{{#if is_multi_part}} + `integration-architecture.md`BADPROTECT050END}

**Mudanças de emprego:**
{{#if has_deployment_guide}}→ Referência: `deployment-guide.md`BADPROTECT048End}→ Revisão das configurações do CI/CD no projetoBMADPROTECT047End}

---

*Documentação gerada pelo método BMAD `document-project` fluxo de trabalho*
