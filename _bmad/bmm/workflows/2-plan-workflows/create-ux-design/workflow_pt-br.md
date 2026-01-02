---
name: create-ux-design
description: Trabalhe com um especialista em Design UX para planejar os padrões de UX, aparência e comportamento de seus aplicativos.
web_bundle: true
---

# Fluxo de Trabalho de Criação de Design UX

**Objetivo:** Criar especificações de design UX abrangentes através de exploração visual colaborativa e tomada de decisão informada, onde você atua como um facilitador de UX trabalhando com um stakeholder de produto.

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

- `installed_path` = `{project-root}/_bmad/bmm/workflows/2-plan-workflows/create-ux-design`
- `template_path` = `{installed_path}/ux-design-template_pt-br.md`
- `default_output_file` = `{output_folder}/ux-design-specification.md`

### Arquivos de Saída

- Temas de cores: `{output_folder}/ux-color-themes.html`
- Direções de design: `{output_folder}/ux-design-directions.html`

### Descoberta de Documento de Entrada

Descubra documentos de contexto para contexto de UX (Prioridade: Pasta de análise primeiro, depois pasta principal, depois fragmentada):

- PRD: `{output_folder}/analysis/*prd*.md` ou `{output_folder}/*prd*.md` ou `{output_folder}/*prd*/**/*.md`
- Resumo de produto: `{output_folder}/analysis/*brief*.md` ou `{output_folder}/*brief*.md` ou `{output_folder}/*brief*/**/*.md`
- Épicos: `{output_folder}/analysis/*epic*.md` ou `{output_folder}/*epic*.md` ou `{output_folder}/*epic*/**/*.md`
- Pesquisa: `{output_folder}/analysis/research/*research*.md` ou `{output_folder}/*research*.md` ou `{output_folder}/*research*/**/*.md`
- Brainstorming: `{output_folder}/analysis/brainstorming/*brainstorming*.md` ou `{output_folder}/*brainstorming*.md`

---

## EXECUÇÃO

Carregue e execute `steps/step-01-init_pt-br.md` para iniciar o fluxo de trabalho de design UX.
