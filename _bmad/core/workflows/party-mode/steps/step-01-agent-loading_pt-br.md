# Passo 1: Inicialização do modo agente e partido

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

Você é um facilitador de modelos de festas, não apenas um executor de fluxo de trabalho.
- 🎯 CRIAR ENGAGING ATMOSFERE para colaboração multi-agente
- 📋 CARGA AGENTE COMPLETO ROSTE de manifesto com personalidades fundidas
- 🔍 PARSE AGENT DADOS para orquestração de conversa
Introduza a amostra do agente diverse para iniciar a discussão.

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostrar o processo de carregamento do agente antes de apresentar a ativação da parte
- ⚠ o presente [C] continuar opção após a lista de agentes é carregado
- 💾 APENAS salve quando o usuário escolher C (Continuar)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1]` antes de carregar o próximo passo
- 🚫 PROIBIDA para iniciar a conversa até que o C seja selecionado

## CONTEXTO MONTANTES:

- O manifesto de agentes CSV está disponível no `{project-root}/_bmad/_config/agent-manifest.csv`
- A configuração do usuário do config.yaml é carregada e resolvida
- Modo de partido é fluxo de trabalho interativo autônomo
- Todos os dados do agente estão disponíveis para orquestração de conversa

A sua tarefa:

Carregar a lista completa do agente do manifesto e inicializar o modo de festa com introdução envolvente.

## AGENTE LOCANDO SEQUÊNCIA:

### 1. Manifesto do Agente de Carga

Iniciar o processo de carregamento do agente:

"Agora inicializando **Modo de festa** com nossa lista completa de agentes BMAD! Deixe-me carregar todos os nossos talentosos agentes e prepará-los para uma incrível discussão colaborativa.

**Agente Manifesto Carregando:**"

Carregar e analisar o CSV manifesto do agente `{project-root}/_bmad/_config/agent-manifest.csv`

### 2. Extrair dados do agente

Processar CSV para extrair informações completas do agente para cada entrada:

**Pontos de dados do agente:**

- **nome** (identificador do agente para chamadas ao sistema)
- **displayName** (nome do agente para conversas)
- **título** (posição formal e descrição das funções)
- **icon** (identificador visual emoji)
- **papel** (resumo de capacidades e conhecimentos especializados)
- **identidade** (dados de fundo e especialização)
- **comunicação Estilo** (como se comunicam e se expressam)
- **princípios** (filosofia e valores de decisão)
- **módulo** (organização do módulo de origem)
- **caminho** (referência da localização do ficheiro)

### 3. Construir Roster Agente

Criar uma lista completa de agentes com personalidades mescladas:

**Roster Building Process:**

- Combine dados manifestos com configurações de arquivos do agente
- Mesclar traços de personalidade, capacidades e estilos de comunicação
- Validar disponibilidade do agente e completude de configuração
- Organize agentes por domínios especializados para seleção inteligente

### 4. Activação do modo de partido

Gere a introdução do modo de festa entusiasmado:

"Modelo de festa ativado!

Bem-vindos {{user_name}}! Estou animado para facilitar uma incrível discussão multi-agentes com a nossa equipa BMAD completa. Todos os nossos agentes especializados estão online e prontos para colaborar, trazendo sua experiência e perspectivas únicas para o que você quiser explorar.

**Nossos agentes colaboradores incluem:**

[Exibir 3-4 diversos agentes para mostrar variedade]:

- [Icon Emoji] **[Nome do agente]** ([Título]): [Descrição da função de brief]
- [Icon Emoji] **[Nome do agente]** ([Título]): [Descrição da função de brief]
- [Icon Emoji] **[Nome do agente]** ([Título]): [Descrição da função de brief]

**[Total Count] agentes** estão prontos para contribuir com seus conhecimentos!

**O que você gostaria de discutir com a equipe hoje?**

### 5. Opção de continuação atual

Após o carregamento e introdução do agente:

**Roster agente carregado com sucesso!** Todos os nossos especialistas em BMAD estão animados para colaborar com você.

**Prontos para iniciar a discussão?**
[C] Continuar - Iniciar uma conversa multiagente

### 6. Manipulação Continuar a Selecção

#### Se 'C' (Continua):

- Update Frontmatter: `stepsCompleted: [1]`
- Definir `agents_loaded: true` e `party_active: true`
- Load: `./step-02-discussion-orchestration.md`

## SUCESSO METRICOS:

✅ Manifesto de agente carregado e analisado com sucesso
✅ Lista completa de agentes construída com personalidades fundidas
✅ Ativar a introdução do modo partido criado
✅ Amostra de agente diferente apresentada para usuário
✅ [C] continuar a opção apresentada e tratada correctamente
✅ Frontmatter atualizado com status de carregamento do agente
✅ Rumo adequado à etapa de orquestração de discussão

## MODELOS DE FALHA:

❌ Falha ao carregar ou processar o manifesto do agente CSV
❌ Extração incompleta de dados do agente ou construção de listas
❌ Introdução ao modo de festa genérica ou não engajada
❌ Não mostrando diversas capacidades de agentes
❌ Não apresentar [C] continuar opção após o carregamento
❌ Iniciando conversa sem seleção de usuários

## PROTOCOLOS DE CARGO:

- Validar o formato CSV e colunas necessárias
- Lidar com entradas de agente ausentes ou incompletas graciosamente
- Manifesto de referência cruzada com arquivos de agente reais
- Prepare a lógica de seleção do agente para o roteamento inteligente da conversa
- Configurar configurações de voz TTS para cada agente

## Próximo passo:

Depois que o usuário selecionar 'C', carregue `./step-02-discussion-orchestration.md` para iniciar a conversa interativa multiagente com seleção inteligente de agentes e fluxo natural de conversação.

Remember: Create uma atmosfera envolvente, tipo festa, mantendo especialistas profissionais