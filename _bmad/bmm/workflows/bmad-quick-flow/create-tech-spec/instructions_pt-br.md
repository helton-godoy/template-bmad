# Crie Tech-Spec - Engenharia de Especificações para Desenvolvimento de IA

<workflow>

<critical>Comunicar em BMADPROTECT066End, adaptado a {user_skill_level}BADPROTECT050End
<critical>Gerar documentos em {document_output_language}BADPROTECT048END
<critical>Engenharia de especificações conversacionais - fazer perguntas, investigar código, produzir especificações completas
<critical>Spec deve conter TODO o contexto que um novo agente de dev precisa para implementá-lo</critical>

<checkpoint-handlers>
<on-select key="a">Carregar e executar {advanced_elicitation}, em seguida, retornar ao passo atual</on-select>
<on-select key="p">Carregar e executar {party_mode_workflow}, em seguida, voltar à etapa atual</on-select>
<on-select key="b">Carregue e execute {quick_dev_workflow} com o arquivo tech-spec</on-select>
</checkpoint-handlers>

<step n="1" goal="Understand what the user wants to build">

<action>Greet {user_name} e peça-lhes para descrever o que querem construir ou mudar. </action>

<action>Ask questões esclarecedoras: problema, quem é afetado, escopo, restrições, código existente? </action>

<action> Verificação do contexto existente no {output_folder} e {sprint_artifacts}BADPROTECT029END

<checkpoint title="Problem Understanding">
[a] Elicitação avançada [c] Continuar [p] Modo de partido
</checkpoint>

</step>

<step n="2" goal="Investigate existing code (if applicable)">

<action>Se brownfield: obter caminhos de arquivos, ler código, identificar padrões/convenções/dependênciasBMAADPROTECT023END

<action>Document: tech pilha, padrões de código, arquivos para modificar, testes padrões</action>

<checkpoint title="Context Gathered">
[a] Elicitação avançada [c] Continuar [p] Modo de partido
</checkpoint>

</step>

<step n="3" goal="Generate the technical specification">

<action>Create tech-spec utilizando esta estrutura:

```markdown

# Tech-Spec: {title}

**Created:** {date}
**Status:** Ready for Development

## Overview

### Problem Statement

### Solution

### Scope (In/Out)

## Context for Development

### Codebase Patterns

### Files to Reference

### Technical Decisions

## Implementation Plan

### Tasks

- [ ] Task 1: Description
- [ ] Task 2: Description

### Acceptance Criteria

- [ ] AC 1: Given/When/Then
- [ ] AC 2: ...

## Additional Context

### Dependencies

### Testing Strategy

### Notes

```

</action>

<action>Save to {sprint_artifacts}/tech-spec-{slug}.md</action>

</step>

<step n="4" goal="Review and finalize">

<action>Present spec to {user_name}, pergunte se captura intenção, faça alterações conforme necessário</action>

<output>**Tech-Spec Complete!**

Salvo em: {sprint_artifacts}/tech-spec-{slug}.md

[a] Elicitação avançada - refinar ainda mais
[b] Iniciar o Desenvolvimento (não recomendado - contexto fresco melhor)
[d] Feito - saída
[p] Party Mode - obter feedback

**Recomendado:** Execute `dev-spec {sprint_artifacts}/tech-spec-{slug}.md` em contexto fresco.
</output>

<ask>Choice (a/b/d/p):</ask>

</step>

</workflow>
