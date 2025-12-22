# {{project_name}} - Visão geral do projecto

**Data:** {{date}}
**Tipo:** {{project_type}}
**Arquitectura:** {{architecture_type}}

## Resumo executivo

{{executive_summary}}

## Classificação do projecto

- **Tipo de repositório:** {{repository_type}}
- **Tipo(s) de projecto:** {{project_types_list}}
- **Língua(s) primária(s):** {{primary_languages}}
- **Padrão de arquitectura:** {{architecture_pattern}}

{{#if is_multi_part}}

## Estrutura múltipla

Este projeto consiste em {{parts_count}} partes distintas:

{{#each project_parts}}

### {{part_name}}

- **Tipo:** {{project_type}}
- **Localização:** `{{root_path}}`
- **Composto:** {{purpose}}
- **Tech Stack:** {{tech_stack}}
{{/each}}

### Como as peças integram

{{integration_description}}
{{/if}}

## Resumo da pilha de tecnologia

BMADPROTECT036FEND}
{{technology_table}}
{{else}}
{{#each project_parts}}

### {{part_name}} Pilha

{{technology_table}}
BMADPROTECT030FEND}
{{/if}}

## Características Principais

{{key_features}}

## Realces de Arquitetura

{{architecture_highlights}}

## Visão geral do desenvolvimento

### Pré-requisitos

{{prerequisites}}

### Começando

{{getting_started_summary}}

### Comandos de teclas

{{#if is_single_part}}

- **Instalar:** `{{install_command}}`
- **Dev:** `{{dev_command}}`
- **Construir:** `{{build_command}}`
- **Teste:** `{{test_command}}`
{{else}}
{{#each project_parts}}

#### {{part_name}ER]

- **Instalar:** `{{install_command}}`
- **Dev:** `{{dev_command}}`
{{/each}}
{{/if}}

## Estrutura do repositório

{{repository_structure_summary}}

## Mapa de Documentação

Para informações pormenorizadas, consultar:

- [BMADPROTECT013EndBMADPROTECT017End - Índice de documentação mestre
Arquitectura detalhada
- [source-tree-analysis.mdBADPROTECT015END - Estrutura da pasta
- [BMADPROTECT008EndBMADPROTECT014End - Desenvolvimento do fluxo de trabalho

---

* Gerado usando o método BMAD `document-project` fluxo de trabalho*
