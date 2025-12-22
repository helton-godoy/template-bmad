# Sprint Planning - Sprint Status Generator

<critical>O motor de execução do fluxo de trabalho é regido por: {project-root}/\ bmad/core/tasks/workflow.xml</critical>
<critical>Você já deve ter carregado e processado: {project-root}/\ bmad/bmm/workflows/4-implementation/sprint-planning/workflow.yaml</critical>

## 📚 Document Discovery - Full Epic Loading

**Estratégia**: O Sprint planning precisa de TODOS os épicos e histórias para criar o acompanhamento completo do estado.

**Epic Discovery Process:**

1. **Procurar o documento inteiro primeiro** - Procurar `epics.md`, `bmm-epics.md`, ou qualquer arquivo `*epic*.md`
2. **Verificar para a versão sharded** - Se documento inteiro não encontrado, procurar `epics/index.md`
3. **Se for encontrada uma versão em cacos**:
- Leia `index.md`ER para entender a estrutura do documento
- Leia TODOS os arquivos de seção épicos listados no índice (por exemplo, `epic-1.md`, `epic-2.md`, etc.)
- Processar todos os épicos e suas histórias a partir do conteúdo combinado
- Isso garante completa cobertura de status sprint
4. **Prioridade**: Se existirem versões inteiras e estilhaçadas, utilize o documento completo

**Fuzzy matching**: Seja flexível com nomes de documentos - os usuários podem usar variações como `epics.md`, `bmm-epics.md`, `user-stories.md`, etc.

<workflow>

<step n="1" goal="Parse epic files and extract all work items">
<action>Comunicar em {communication_language} com {user_name}BADPROTECT086End
<action>Procure todos os arquivos correspondentes `{epics_pattern}` no {epics_location}BADPROTECT084END
<action>Pode ser um único arquivo BMADPROTECT049End ou vários arquivos `epic-1.md`, BMADPROTECT047End

<action> Para cada arquivo épico encontrado, extrair:</action>

- Números épicos de cabeçalhos como `## Epic 1:` ou `## Epic 2:`
- Identidades de histórias e títulos de padrões como `### Story 1.1: User Authentication`
- Converter formato de história de `Epic.Story: Title` para chave de caso de kebab: `epic-story-title`

**Regras de conversão do ID da história:**
BMADPROTECT111end BMADPROTECT041end
- Substituir período com traço: `1-1`
- Converter título para kebab- case: `user-authentication`
- Chave final: `1-1-user-authentication`

<action>Inventário completo de todos os épicos e histórias de todos os arquivos épicos</action>
</step>

<step n="0.5" goal="Discover and load project documents">
<invoke-protocol name="discover_inputs" />
<note>Após a descoberta, estas variáveis de conteúdo estão disponíveis: {epics_content} (todos os épicos carregados - usa a estratégia FULL_LOAD)
</step>

<step n="2" goal="Build sprint status structure">
<action>Para cada épico encontrado, crie entradas nesta ordem: </action>

1. **Entrada épica** - Chave: `epic-{num}`, Estado por omissão: `backlog`
2. **Inscrições de história** - Chave: `{epic}-{story}-{title}`, Estado por omissão: `backlog`
3. **Inserção retrospectiva** - Chave: `epic-{num}-retrospective`, Estado por omissão: `optional`

**Exemplo estrutura:**

```yaml
development_status:
  epic-1: backlog
  1-1-user-authentication: backlog
  1-2-account-management: backlog
  epic-1-retrospective: optional

```

</step>

<step n="3" goal="Apply intelligent status detection">
<action> Para cada história, detecte o status atual verificando arquivos:</action>

**Detecção de arquivos de história:**

- Check: `{story_location_absolute}/{story-key}.md` (por exemplo, `stories/1-1-user-authentication.md`)
- Se existe → status de atualização para pelo menos `ready-for-dev`

**Regra de preservação:**

- Se o `{status_file}` existente existir e tiver estado mais avançado, preservá- lo
- Estado nunca inferior (por exemplo, não mude `done` para `ready-for-dev`)

**Referência de fluxo de estado:**
BMADPROTECT109end BMADPROTECT025end → BMADPROTECT024end → BMADPROTECT023end
BMADPROTECT108end BMADPROTECT022end → BMADPROTECT021end → BMADPROTECT020end → BMADPROTECT019end → BMADPROTECT018end
BMADPROTECT107end BMADPROTECT017end ↔ BMADPROTECT016end
</step>

<step n="4" goal="Generate sprint status file">
<action>Create or update {status_file} com:</action>

**Estrutura do ficheiro:**

«```yaml

# gerado: {date}

# projecto: {project_name}

# chave do projeto: {project_key}

# tracking system: {tracking_system}

# story location: {story_location}

# DEFINIÇÕES DE ESTATUTO:
== Ligações externas ==

# Estado épico:

# - backlog: Épico ainda não iniciado

# - em andamento: Épico a ser trabalhado

# - done: Todas as histórias em épico concluídas

## Transições Épicas de Estado:

# - backlog → in-progress: Automaticamente quando a primeira história é criada (via create-story)

# - em andamento → done: Manualmente quando todas as histórias atingem o status de 'done'
Status da história:

# - backlog: História só existe em arquivo épico

# - pronto-para-dev: Arquivo de história criado na pasta de histórias

# - em andamento: Desenvolvedor trabalhando ativamente em implementation

# - revisão: Pronto para revisão de código (via fluxo de trabalho de revisão de código de Dev)

# - done: História concluída

## Estado retrospectivo:

# - opcional: Pode ser completado, mas não exigido

# - done: A retrospectiva foi concluída

## Notas de fluxo de trabalho:

# ===============

# - Transições épicas para 'em progresso' automaticamente quando a primeira história é criada

# - Histórias podem ser trabalhadas em paralelo se a capacidade da equipe permitir

# - SM normalmente cria a próxima história depois que a anterior é 'done' para incorporar aprendizagens

# - Dev move a história para 'review', então executa a revisão de código (contexto novo, LLM diferente recomendado)
