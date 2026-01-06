# Planejamento de Sprint - Gerador de Status de Sprint

<critical>O mecanismo de execução do fluxo de trabalho é governado por: {project-root}/_bmad/core/tasks/workflow.xml</critical>
<critical>Você DEVE já ter carregado e processado: {project-root}/_bmad/bmm/workflows/4-implementation/sprint-planning/workflow.yaml</critical>

## 📚 Descoberta de Documentos - Carregamento Completo de Épicos

**Estratégia**: O planejamento de sprint precisa de TODOS os épicos e histórias para construir um rastreamento de status completo.

**Processo de Descoberta de Épicos:**

1. **Procurar documento inteiro primeiro** - Procure por `epics.md`, `bmm-epics.md`, ou qualquer arquivo `*epic*.md`
2. **Verificar versão fragmentada** - Se documento inteiro não encontrado, procure por `epics/index.md`
3. **Se versão fragmentada encontrada**:
   - Leia `index.md` para entender a estrutura do documento
   - Leia TODOS os arquivos de seção de épico listados no índice (e.g., `epic-1.md`, `epic-2.md`, etc.)
   - Processe todos os épicos e suas histórias do conteúdo combinado
   - Isso garante cobertura completa de status de sprint
4. **Prioridade**: Se ambas as versões inteira e fragmentada existirem, use o documento inteiro

**Correspondência difusa**: Seja flexível com nomes de documentos - usuários podem usar variações como `epics.md`, `bmm-epics.md`, `user-stories.md`, etc.

<workflow>

<step n="1" goal="Analisar arquivos de épico e extrair todos os itens de trabalho">
<action>Comunicar em {communication_language} com {user_name}</action>
<action>Procurar todos os arquivos correspondentes a `{epics_pattern}` em {epics_location}</action>
<action>Pode ser um único arquivo `epics.md` ou múltiplos arquivos `epic-1.md`, `epic-2.md`</action>

<action>Para cada arquivo de épico encontrado, extrair:</action>

- Números de épico de cabeçalhos como `## Epic 1:` ou `## Epic 2:`
- IDs de história e títulos de padrões como `### Story 1.1: User Authentication`
- Converter formato de história de `Epic.Story: Title` para chave kebab-case: `epic-story-title`

**Regras de Conversão de ID de História:**

- Original: `### Story 1.1: User Authentication`
- Substituir ponto por traço: `1-1`
- Converter título para kebab-case: `user-authentication`
- Chave final: `1-1-user-authentication`

<action>Construir inventário completo de todos os épicos e histórias de todos os arquivos de épico</action>
</step>

  <step n="0.5" goal="Descobrir e carregar documentos do projeto">
    <invoke-protocol name="discover_inputs" />
    <note>Após a descoberta, estas variáveis de conteúdo estão disponíveis: {epics_content} (todos os épicos carregados - usa estratégia FULL_LOAD)</note>
  </step>

<step n="2" goal="Construir estrutura de status de sprint">
<action>Para cada épico encontrado, criar entradas nesta ordem:</action>

1. **Entrada de Épico** - Chave: `epic-{num}`, Status padrão: `backlog`
2. **Entradas de História** - Chave: `{epic}-{story}-{title}`, Status padrão: `backlog`
3. **Entrada de Retrospectiva** - Chave: `epic-{num}-retrospective`, Status padrão: `optional`

**Exemplo de estrutura:**

```yaml
development_status:
  epic-1: backlog
  1-1-user-authentication: backlog
  1-2-account-management: backlog
  epic-1-retrospective: optional
```

</step>

<step n="3" goal="Aplicar detecção inteligente de status">
<action>Para cada história, detectar status atual verificando arquivos:</action>

**Detecção de arquivo de história:**

- Verificar: `{story_location_absolute}/{story-key}.md` (e.g., `stories/1-1-user-authentication.md`)
- Se existe → atualizar status para pelo menos `ready-for-dev`

**Regra de preservação:**

- Se `{status_file}` existente existir e tiver status mais avançado, preservá-lo
- Nunca rebaixar status (e.g., não mudar `done` para `ready-for-dev`)

**Referência de Fluxo de Status:**

- Épico: `backlog` → `in-progress` → `done`
- História: `backlog` → `ready-for-dev` → `in-progress` → `review` → `done`
- Retrospectiva: `optional` ↔ `done`
  </step>

<step n="4" goal="Gerar arquivo de status de sprint">
<action>Criar ou atualizar {status_file} com:</action>

**Estrutura de Arquivo:**

```yaml
# generated: {date}
# project: {project_name}
# project_key: {project_key}
# tracking_system: {tracking_system}
# story_location: {story_location}

# STATUS DEFINITIONS:
# ==================
# Epic Status:
#   - backlog: Epic not yet started
#   - in-progress: Epic actively being worked on
#   - done: All stories in epic completed
#
# Epic Status Transitions:
#   - backlog → in-progress: Automatically when first story is created (via create-story)
#   - in-progress → done: Manually when all stories reach 'done' status
#
# Story Status:
#   - backlog: Story only exists in epic file
#   - ready-for-dev: Story file created in stories folder
#   - in-progress: Developer actively working on implementation
#   - review: Ready for code review (via Dev's code-review workflow)
#   - done: Story completed
#
# Retrospective Status:
#   - optional: Can be completed but not required
#   - done: Retrospective has been completed
#
# WORKFLOW NOTES:
# ===============
# - Epic transitions to 'in-progress' automatically when first story is created
# - Stories can be worked in parallel if team capacity allows
# - SM typically creates next story after previous one is 'done' to incorporate learnings
# - Dev moves story to 'review', then runs code-review (fresh context, different LLM recommended)

generated: { date }
project: { project_name }
project_key: { project_key }
tracking_system: { tracking_system }
story_location: { story_location }

development_status:
  # All epics, stories, and retrospectives in order
```

<action>Escrever o YAML de status de sprint completo para {status_file}</action>
<action>CRÍTICO: Metadados aparecem DUAS VEZES - uma vez como comentários (#) para documentação, uma vez como campos chave:valor YAML para análise</action>
<action>Garantir que todos os itens estejam ordenados: épico, suas histórias, sua retrospectiva, próximo épico...</action>
</step>

<step n="5" goal="Validar e relatar">
<action>Realizar verificações de validação:</action>

- [ ] Todo épico em arquivos de épico aparece em {status_file}
- [ ] Toda história em arquivos de épico aparece em {status_file}
- [ ] Todo épico tem uma entrada de retrospectiva correspondente
- [ ] Nenhum item em {status_file} que não exista em arquivos de épico
- [ ] Todos os valores de status são legais (correspondem às definições da máquina de estado)
- [ ] Arquivo é sintaxe YAML válida

<action>Contar totais:</action>

- Total de épicos: {{epic_count}}
- Total de histórias: {{story_count}}
- Épicos em progresso: {{in_progress_count}}
- Histórias concluídas: {{done_count}}

<action>Exibir resumo de conclusão para {user_name} em {communication_language}:</action>

**Status de Sprint Gerado com Sucesso**

- **Localização do Arquivo:** {status_file}
- **Total de Épicos:** {{epic_count}}
- **Total de Histórias:** {{story_count}}
- **Épicos Em Progresso:** {{epics_in_progress_count}}
- **Histórias Concluídas:** {{done_count}}

**Próximos Passos:**

1. Revise o gerado {status_file}
2. Use este arquivo para rastrear progresso de desenvolvimento
3. Agentes atualizarão status à medida que trabalham
4. Reexecute este fluxo de trabalho para atualizar status detectados automaticamente

</step>

</workflow>

## Documentação Adicional

### Máquina de Estado de Status

**Fluxo de Status de Épico:**

```
backlog → in-progress → done
```

- **backlog**: Épico ainda não iniciado
- **in-progress**: Épico sendo trabalhado ativamente (histórias sendo criadas/implementadas)
- **done**: Todas as histórias no épico concluídas

**Fluxo de Status de História:**

```
backlog → ready-for-dev → in-progress → review → done
```

- **backlog**: História existe apenas no arquivo de épico
- **ready-for-dev**: Arquivo de história criado (e.g., `stories/1-3-plant-naming.md`)
- **in-progress**: Desenvolvedor trabalhando ativamente
- **review**: Pronto para revisão de código (via fluxo de revisão de código do Dev)
- **done**: Concluído

**Status de Retrospectiva:**

```
optional ↔ done
```

- **optional**: Pronto para ser conduzido mas não obrigatório
- **done**: Finalizado

### Diretrizes

1. **Ativação de Épico**: Marque épico como `in-progress` ao iniciar trabalho em sua primeira história
2. **Padrão Sequencial**: Histórias são tipicamente trabalhadas em ordem, mas trabalho paralelo é suportado
3. **Trabalho Paralelo Suportado**: Múltiplas histórias podem estar `in-progress` se a capacidade da equipe permitir
4. **Revisão Antes de Concluído**: Histórias devem passar por `review` antes de `done`
5. **Transferência de Aprendizado**: SM tipicamente cria próxima história após anterior estar `done` para incorporar aprendizados
