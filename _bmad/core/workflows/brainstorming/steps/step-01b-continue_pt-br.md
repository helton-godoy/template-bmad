# Passo 1b: Continuação do fluxo de trabalho

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- Você é um facilitador contínuo, não um novato.
- 🎯 RESPEITO AO ESTADO DE FLORES DE TRABALHO EM VIGOR e progresso
- 📋 CONTEXTO E Resultados DA SESSÃO ANTERIOR
- 🔍 RESUME SEM MESMO de onde o utilizador parou
- 💬

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Carregar e analisar completamente o documento existente
- 💾 Atualizar a matéria frontal com o estado de continuação
- 📖 Apresentar claramente o estado actual e as opções seguintes
- 🚫 PROIBIDO repetir o trabalho concluído ou fazer as mesmas perguntas

## CONTEXTO MONTANTES:

- Documento existente com matéria frontal está disponível
- Os passos anteriores concluídos indicam o progresso da sessão
- Técnicas cerebrais CSV carregadas quando necessário para os passos restantes
- O usuário pode querer continuar, modificar ou reiniciar

A sua tarefa:

Analise o estado de sessão de brainstorming existente e forneça opções de continuação perfeitas.

## SEQUÊNCIA DE CONTINUAÇÃO:

### 1. Analisar a Sessão Existente

Carregar o documento existente e analisar o estado actual:

**Análise do Documento:**

- Ler `{output_folder}/analysis/brainstorming-session-{{date}}.md` existente
- Examine o material frontal para `stepsCompleted`, `session_topic`, `session_goals`
- Reveja conteúdo para entender o progresso da sessão e resultados
- Identificar o estágio atual e os próximos passos lógicos

**Avaliação do estado da sessão:**
Bem-vindo de volta {{user_name}}! Posso ver sua sessão de brainstorming em **[session topic]**de**[date]**.

**Status atual da sessão:**

- **Passos completados:** [Lista completa]
- **Técnicas utilizadas:** [Técnicas de lista de matéria frontal]
- **Ideias geradas:** [Número de matéria frontal]
- **Estágio atual:** [Avaliar onde pararam]

**Progresso da Sessão:**
[Sumário da intimidade do que foi realizado e o que permanece]"

### 2. Opções de continuação presentes

Com base na análise de sessão, fornecer opções adequadas:

**Se a sessão for concluída:**
"Sua sessão de brainstorming parece estar completa!

**Opções:**
[1] Resultados da Revisão - Veja suas ideias e insights documentados
[2] Iniciar nova sessão - Comece brainstorming sobre um novo tópico
[3) Extend Session - Adicione mais técnicas ou explore novos ângulos"

**Se sessão em progresso:**
"Vamos continuar onde paramos!

**Progresso atual:**
[Descrição da fase atual e realizações]

**Próximos Passos:**
[Continue com o próximo passo apropriado com base no estado do fluxo de trabalho]"

### 3. Lidar com a escolha do usuário

Rota para o próximo passo apropriado com base na seleção:

**Resultados da revisão:** Carregar o passo de revisão/navegação adequado
**Nova Sessão:** Iniciar uma nova inicialização do fluxo de trabalho
**Extender sessão:** Continuar com a próxima técnica ou fase
**Progresso contínuo:** Continuar a partir da etapa atual do fluxo de trabalho

### 4. Actualizar o Estado da Sessão

Atualizar a matéria frontal para refletir a continuação:

```yaml
---
stepsCompleted: [existing_steps]
session_continued: true
continuation_date: { { current_date } }
---

```

## SUCESSO METRICOS:

✅ Estado de sessão existente analisado e compreendido com precisão
✅ Continuação sem emendas sem perda de contexto ou conexão
✅ Opções de continuação adequadas apresentadas com base no progresso
✅ Escolha do usuário corretamente encaminhada para o próximo passo de fluxo de trabalho
✅ Continuidade da sessão mantida ao longo da interação

## MODELOS DE FALHA:

❌ Não analisar corretamente o estado do documento existente
❌ Pedir ao utilizador para repetir as informações já fornecidas
❌ Perda de continuidade no fluxo ou contexto da sessão
❌ Não fornecendo opções de continuação adequadas

## PROTOCOLOS DE CONTINUAÇÃO:

- Sempre reconhecer trabalhos anteriores e progresso
- Manter o relacionamento estabelecido e dinâmica de sessão
- Construir ideias e insights existentes em vez de recomeçar
- Respeitar o tempo do usuário, evitando perguntas repetitivas

## Próximo passo:

Rota para passo de fluxo de trabalho apropriado com base na escolha de continuação do usuário e estado de sessão atual.
