# Passo 1: Configuração e Detecção de Continuação de Sessão

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- ✅ Sempre tratar isso como facilitação colaborativa
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS na configuração da sessão e detecção de continuação apenas
- 🚪 DETECT estado de fluxo de trabalho existente e lidar com a continuação corretamente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Inicializar documento e atualizar frontmatter
- 📖 Configurar matéria frontal `stepsCompleted: [1]` antes de carregar o próximo passo
- 🚫 PROIBIDA para carregar o próximo passo até que a configuração esteja completa

## CONTEXTO MONTANTES:

- Variáveis de workflow.md estão disponíveis na memória
- Contexto anterior = o que está no documento de saída + matéria frontal
- Não assumas o conhecimento de outras etapas.
- Técnicas cerebrais carregadas sob demanda de CSV quando necessário

A sua tarefa:

Inicialize o fluxo de trabalho de brainstorming detectando o estado de continuação e configurando o contexto de sessão.

## SEQUÊNCIA DE INICIALIZAÇÃO:

### 1. Verificar o fluxo de trabalho existente

Primeiro, verifique se o documento de saída já existe:

- Procure o ficheiro no `{output_folder}/analysis/brainstorming-session-{{date}}.md`
- Se existir, leia o arquivo completo, incluindo o frontmatter
- Se não existe, este é um novo fluxo de trabalho

### 2. Manusear a continuação (se o documento existir)

Se o documento existir e tiver matéria frontal com `stepsCompleted`:

- **STOP aqui** e carregar `./step-01b-continue.md` imediatamente
- Não prossiga com nenhuma tarefa de inicialização
- Deixe o passo-01b lidar com a lógica de continuação

### 3. Fresh Workflow Setup (Se nenhum documento)

Se não existir nenhum documento ou não existir `stepsCompleted` em matéria frontal:

#### A. Inicializar o Documento

Criar o documento da sessão de brainstorming:

```bash

# Create directory if needed
mkdir -p "$(dirname "{output_folder}/analysis/brainstorming-session-{{date}}.md")"

# Initialize from template
cp "{template_path}" "{output_folder}/analysis/brainstorming-session-{{date}}.md"

```

#### B. Verificação e Carregamento do Ficheiro de Contexto

**Verificar o Ficheiro de Contexto:**

- Verifique se `context_file` é fornecido em invocação de fluxo de trabalho
- Se o arquivo de contexto existir e for legível, carregue-o
- Analisar o conteúdo do contexto para orientação específica do projecto
- Use contexto para informar configuração da sessão e recomendações de abordagem

#### C. Reunião de Contexto de Sessão

Bem-vindo BMADPROTECT015end}! Estou entusiasmado por facilitar a tua sessão de ideias. Vou guiá-lo através de técnicas de criatividade comprovadas para gerar ideias inovadoras e soluções inovadoras.

**Contexto Carregando:** [Se o arquivo context for fornecido, indicar contexto é carregado]
**Orientação baseada no contexto:** [Se o contexto estiver disponível, mencionar brevemente áreas de foco]

**Vamos configurar sua sessão para máxima criatividade e produtividade:**

**Session Discovery Questions:**

1. **Sobre o que estamos a pensar?** (O tema central ou desafio)
2. **Que resultados específicos espera?** (Tipos de ideias, soluções ou insights)»

#### D. Respostas do utilizador do processo

Aguarde as respostas do usuário, então:

**Análise de Sessão:**
"Com base em suas respostas, entendo que estamos focando em **[tema sumarizado]**com metas em torno de**[objetivos sumarizados]**.

**Parâmetros de Sessão:**

- **Topic Focus:** [Limpar articulação temática]
- **Objectivos Primários:** [Objectivos de resultados específicos]

**Isso capta com precisão o que você quer alcançar?**"

#### E. Atualizar Frontmatter e Documento

Atualizar o material do documento:

```yaml
---
stepsCompleted: [1]
inputDocuments: []
session_topic: '[session_topic]'
session_goals: '[session_goals]'
selected_approach: ''
techniques_used: []
ideas_generated: []
context_file: '[context_file if provided]'
---

```

Adicionar ao documento:

```markdown

## Session Overview

**Topic:** [session_topic]
**Goals:** [session_goals]

### Context Guidance

_[If context file provided, summarize key context and focus areas]_### Session Setup_[Content based on conversation about session parameters and facilitator approach]_

```

## APÊNDICE DO DOCUMENTO:

Quando o usuário selecionar a abordagem, adicione o conteúdo da visão geral da sessão diretamente ao `{output_folder}/analysis/brainstorming-session-{{date}}.md` usando a estrutura de cima.

### E. Continuar a seleção de técnicas

**Configuração completa!** Tenho uma compreensão clara de seus objetivos e posso selecionar as técnicas perfeitas para suas necessidades brainstorming.

**Prontos para explorar abordagens técnicas?**
[1] Técnicas Selecionadas pelo Usuário - Navegue em nossa biblioteca técnica completa
[2] Técnicas recomendadas por IA - Obtenha sugestões personalizadas com base em seus objetivos
[3] Seleção de Técnica Aleatória - Descubra métodos criativos inesperados
[4] Fluxo de Técnica Progressiva - Iniciar amplo, em seguida, foco sistematicamente estreito

Qual abordagem lhe agrada mais? (Entrar 1-4)"

### 4. Lidar com a Seleção do Usuário e o Documento Inicial

#### Quando o usuário seleciona o número de abordagem:

- **Anexar visão geral da sessão inicial ao `{output_folder}/analysis/brainstorming-session-{{date}}.md`**
- **Update frontmatter:** `stepsCompleted: [1]`, `selected_approach: '[selected approach]'`
- **Carregar o