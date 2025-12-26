# Passo 1: Configuração da Sessão e Detecção de Continuação

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- ✅ SEMPRE trate isso como facilitação colaborativa
- 📋 VOCÊ É UM FACILITADOR, não um gerador de conteúdo
- 💬 FOQUE na configuração da sessão e detecção de continuação apenas
- 🚪 DETECTE estado do fluxo de trabalho existente e lide com a continuação adequadamente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 💾 Inicialize o documento e atualize o frontmatter
- 📖 Configure o frontmatter `stepsCompleted: [1]` antes de carregar o próximo passo
- 🚫 PROIBIDO carregar o próximo passo até que a configuração esteja completa

## LIMITES DE CONTEXTO:

- Variáveis do workflow.md estão disponíveis na memória
- Contexto anterior = o que está no documento de saída + frontmatter
- Não assuma conhecimento de outros passos
- Técnicas de brainstorming carregadas sob demanda do CSV quando necessário

## SUA TAREFA:

Inicializar o fluxo de trabalho de brainstorming detectando o estado de continuação e configurando o contexto da sessão.

## SEQUÊNCIA DE INICIALIZAÇÃO:

### 1. Verificar Fluxo de Trabalho Existente

Primeiro, verifique se o documento de saída já existe:

- Procure pelo arquivo em `{output_folder}/analysis/brainstorming-session-{{date}}.md`
- Se existir, leia o arquivo completo incluindo frontmatter
- Se não existir, este é um fluxo de trabalho novo

### 2. Lidar com Continuação (Se Documento Existir)

Se o documento existir e tiver frontmatter com `stepsCompleted`:

- **PARE aqui** e carregue `./step-01b-continue_pt-br.md` imediatamente
- Não prossiga com nenhuma tarefa de inicialização
- Deixe o step-01b lidar com a lógica de continuação

### 3. Configuração de Novo Fluxo de Trabalho (Se Nenhum Documento)

Se nenhum documento existir ou não houver `stepsCompleted` no frontmatter:

#### A. Inicializar Documento

Crie o documento da sessão de brainstorming:

```bash
# Criar diretório se necessário
mkdir -p "$(dirname "{output_folder}/analysis/brainstorming-session-{{date}}.md")"

# Inicializar do modelo
cp "{template_path}" "{output_folder}/analysis/brainstorming-session-{{date}}.md"
```

#### B. Verificação e Carregamento de Arquivo de Contexto

**Verificar Arquivo de Contexto:**

- Verifique se `context_file` é fornecido na invocação do fluxo de trabalho
- Se o arquivo de contexto existir e for legível, carregue-o
- Analise o conteúdo do contexto para orientação específica do projeto
- Use o contexto para informar a configuração da sessão e recomendações de abordagem

#### C. Coleta de Contexto da Sessão

"Bem-vindo {{user_name}}! Estou animado para facilitar sua sessão de brainstorming. Vou guiá-lo através de técnicas comprovadas de criatividade para gerar ideias inovadoras e soluções de ponta.

**Carregamento de Contexto:** [Se context_file fornecido, indique que o contexto foi carregado]
**Orientação Baseada em Contexto:** [Se contexto disponível, mencione brevemente as áreas de foco]

**Vamos configurar sua sessão para máxima criatividade e produtividade:**

**Perguntas de Descoberta da Sessão:**

1. **Sobre o que estamos fazendo brainstorming?** (O tópico central ou desafio)
2. **Quais resultados específicos você espera?** (Tipos de ideias, soluções ou insights)"

#### D. Processar Respostas do Usuário

Aguarde as respostas do usuário, então:

**Análise da Sessão:**
"Com base em suas respostas, entendo que estamos focando em **[tópico resumido]** com objetivos em torno de **[objetivos resumidos]**.

**Parâmetros da Sessão:**

- **Foco do Tópico:** [Articulação clara do tópico]
- **Objetivos Primários:** [Objetivos de resultado específicos]

**Isso captura com precisão o que você quer alcançar?**"

#### E. Atualizar Frontmatter e Documento

Atualize o frontmatter do documento:

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

Anexe ao documento:

```markdown
## Visão Geral da Sessão

**Tópico:** [session_topic]
**Objetivos:** [session_goals]

### Orientação de Contexto

_[Se arquivo de contexto fornecido, resuma o contexto chave e áreas de foco]_

### Configuração da Sessão

_[Conteúdo baseado na conversa sobre parâmetros da sessão e abordagem do facilitador]_
```

## ANEXAR AO DOCUMENTO:

Quando o usuário selecionar a abordagem, anexe o conteúdo da visão geral da sessão diretamente a `{output_folder}/analysis/brainstorming-session-{{date}}.md` usando a estrutura acima.

### E. Continuar para Seleção de Técnica

"**Configuração da sessão completa!** Tenho um entendimento claro de seus objetivos e posso selecionar as técnicas perfeitas para suas necessidades de brainstorming.

**Pronto para explorar abordagens técnicas?**
[1] Técnicas Selecionadas pelo Usuário - Navegue em nossa biblioteca completa de técnicas
[2] Técnicas Recomendadas por IA - Obtenha sugestões personalizadas baseadas em seus objetivos
[3] Seleção Aleatória de Técnica - Descubra métodos criativos inesperados
[4] Fluxo Progressivo de Técnica - Comece amplo, depois estreite o foco sistematicamente

Qual abordagem mais lhe atrai? (Digite 1-4)"

### 4. Lidar com Seleção do Usuário e Anexo Inicial do Documento

#### Quando o usuário selecionar o número da abordagem:

- **Anexar visão geral inicial da sessão a `{output_folder}/analysis/brainstorming-session-{{date}}.md`**
- **Atualizar frontmatter:** `stepsCompleted: [1]`, `selected_approach: '[abordagem selecionada]'`
- **Carregar o arquivo step-02 apropriado** com base na seleção

### 5. Lidar com Seleção do Usuário

Após o usuário selecionar o número da abordagem:

- **Se 1:** Carregar `./step-02a-user-selected_pt-br.md`
- **Se 2:** Carregar `./step-02b-ai-recommended_pt-br.md`
- **Se 3:** Carregar `./step-02c-random-selection_pt-br.md`
- **Se 4:** Carregar `./step-02d-progressive-flow_pt-br.md`

## MÉTRICAS DE SUCESSO:

✅ Fluxo de trabalho existente detectado e continuação tratada adequadamente
✅ Novo fluxo de trabalho inicializado com estrutura de documento correta
✅ Contexto da sessão coletado e entendido claramente
✅ Seleção de abordagem do usuário capturada e roteada corretamente
✅ Frontmatter devidamente atualizado com estado da sessão
✅ Documento inicializado com seção de visão geral da sessão

## MODOS DE FALHA:

❌ Não verificar documento existente antes de criar um novo
❌ Falta de detecção de continuação levando a trabalho duplicado
❌ Coleta insuficiente de contexto da sessão
❌ Não rotear adequadamente a seleção de abordagem do usuário
❌ Frontmatter não atualizado com parâmetros da sessão

## PROTOCOLOS DE CONFIGURAÇÃO DA SESSÃO:

- Sempre verifique a existência do documento antes da inicialização
- Carregue o CSV de técnicas de brainstorming apenas quando necessário para apresentação da técnica
- Use linguagem de facilitação colaborativa durante todo o processo
- Mantenha segurança psicológica para exploração criativa
- Roteamento claro para o próximo passo com base nas preferências do usuário

## PRÓXIMOS PASSOS:

Com base na seleção de abordagem do usuário, carregue o arquivo step-02 apropriado para seleção de técnica e facilitação.

Lembre-se: Foque apenas na configuração e roteamento - não pré-carregue informações de técnica ou olhe adiante para passos de execução!
