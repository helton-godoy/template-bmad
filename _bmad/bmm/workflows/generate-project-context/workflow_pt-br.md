---
name: generate-project-context
description: "Generate a comprehensive project-context.md file that guides AI agents on project standards, patterns, and architecture. This workflow analyzes the existing codebase and configuration to create authoritative rules for consistent AI implementation."
web_bundle: true
---

# Fluxo de Trabalho de Geração de Contexto do Projeto

**Objetivo:** Gerar um arquivo abrangente `project-context.md` que guia agentes de IA sobre padrões de projeto, padrões e arquitetura. Este fluxo de trabalho analisa a base de código existente e a configuração para criar regras autoritárias para implementação consistente de IA.

---

## ARQUITETURA DO FLUXO DE TRABALHO

Isso usa **arquitetura de micro-arquivo** para execução disciplinada:

- Cada passo é um arquivo autônomo com regras incorporadas
- Progressão sequencial com controle do usuário em cada passo
- Estado do documento rastreado no frontmatter
- Construção de documento apenas-anexar através de conversa

---

## INICIALIZAÇÃO

### Carregamento de Configuração

Carregue a configuração de `{project-root}/_bmad/bmm/config.yaml` e resolva:

- `project_name`, `output_folder`, `user_name`
- `communication_language`, `document_output_language`, `user_skill_level`
- `date` como data e hora atual gerada pelo sistema

### Caminhos

- `installed_path` = `{project-root}/_bmad/bmm/workflows/generate-project-context`
- `template_path` = `{installed_path}/project-context-template_pt-br.md`
- `default_output_file` = `{output_folder}/project-context.md`

### Descoberta de Documento de Entrada

Analisa automaticamente os arquivos do projeto para preencher o contexto:

- `package.json` / arquivos de dependência
- `tsconfig.json` / arquivos de configuração
- `architecture.md` (se existir)
- Padrões de código existentes na árvore de origem

---

## EXECUÇÃO

Carregue e execute `steps/step-01-discover_pt-br.md` para iniciar o fluxo de trabalho de geração de contexto.
