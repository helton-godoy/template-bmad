# Criar Tech-Spec - Engenharia de Especificação para Desenvolvimento de IA

<workflow>

<critical>Comunique em {communication_language}, adaptado para {user_skill_level}</critical>
<critical>Gere documentos em {document_output_language}</critical>
<critical>Engenharia de especificação conversacional - faça perguntas, investigue código, produza especificação completa</critical>
<critical>A especificação deve conter TODO o contexto que um agente dev novo precisa para implementá-la</critical>

<checkpoint-handlers>
  <on-select key="a">Carregar e executar {advanced_elicitation}, depois retornar ao passo atual</on-select>
  <on-select key="p">Carregar e executar {party_mode_workflow}, depois retornar ao passo atual</on-select>
  <on-select key="b">Carregar e executar {quick_dev_workflow} com o arquivo tech-spec</on-select>
</checkpoint-handlers>

<step n="1" goal="Entender o que o usuário quer construir">

<action>Cumprimentar {user_name} e pedir para descrever o que desejam construir ou mudar.</action>

<action>Fazer perguntas de esclarecimento: problema, quem é afetado, escopo, restrições, código existente?</action>

<action>Verificar contexto existente em {output_folder} e {sprint_artifacts}</action>

<checkpoint title="Problem Understanding">
[a] Elicitação Avançada  [c] Continuar  [p] Modo Festa
</checkpoint>

</step>

<step n="2" goal="Investigar código existente (se aplicável)">

<action>Se brownfield: obter caminhos de arquivo, ler código, identificar padrões/convenções/dependências</action>

<action>Documentar: pilha técnica, padrões de código, arquivos para modificar, padrões de teste</action>

<checkpoint title="Context Gathered">
[a] Elicitação Avançada  [c] Continuar  [p] Modo Festa
</checkpoint>

</step>

<step n="3" goal="Gerar a especificação técnica">

<action>Criar tech-spec usando esta estrutura:

```markdown
# Tech-Spec: {title}

**Criado:** {date}
**Status:** Pronto para Desenvolvimento

## Visão Geral

### Declaração do Problema

### Solução

### Escopo (Dentro/Fora)

## Contexto para Desenvolvimento

### Padrões de Base de Código

### Arquivos para Referência

### Decisões Técnicas

## Plano de Implementação

### Tarefas

- [ ] Tarefa 1: Descrição
- [ ] Tarefa 2: Descrição

### Critérios de Aceite

- [ ] CA 1: Dado/Quando/Então
- [ ] CA 2: ...

## Contexto Adicional

### Dependências

### Estratégia de Teste

### Notas
```

</action>

<action>Salvar em {sprint_artifacts}/tech-spec-{slug}.md</action>

</step>

<step n="4" goal="Revisar e finalizar">

<action>Apresentar especificação para {user_name}, perguntar se captura a intenção, fazer mudanças conforme necessário</action>

<output>**Tech-Spec Completa!**

Salva em: {sprint_artifacts}/tech-spec-{slug}.md

[a] Elicitação Avançada - refinar mais
[b] Começar Desenvolvimento (não recomendado - contexto novo é melhor)
[d] Feito - sair
[p] Modo Festa - obter feedback

**Recomendado:** Execute `dev-spec {sprint_artifacts}/tech-spec-{slug}.md` em contexto novo.
</output>

<ask>Escolha (a/b/d/p):</ask>

</step>

</workflow>
