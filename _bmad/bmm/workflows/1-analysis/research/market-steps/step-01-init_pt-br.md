# Pesquisa de Mercado Passo 1: Inicialização da Pesquisa de Mercado

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

- 🛑 NUNCA gere conteúdo de pesquisa no passo init
- ✅ SEMPRE confirme entendimento dos objetivos de pesquisa do usuário
- 📋 VOCÊ É UM FACILITADOR DE PESQUISA DE MERCADO, não gerador de conteúdo
- 💬 FOQUE em esclarecer escopo e abordagem
- 🔍 SEM PESQUISA WEB em init - isso é para passos posteriores
- 📖 CRÍTICO: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - entendimento parcial leva a pesquisa incompleta
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido e entendido antes de prosseguir

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Confirme entendimento da pesquisa antes de prosseguir
- ⚠️ Apresente opção [C] continuar após clarificação de escopo
- 💾 Escreva documento de escopo inicial imediatamente
- 📖 Atualize frontmatter `stepsCompleted: [1]` antes de carregar o próximo passo
- 🚫 PROIBIDO carregar o próximo passo até que C seja selecionado

## LIMITES DE CONTEXTO:

- Documento atual e frontmatter da descoberta do fluxo de trabalho principal estão disponíveis
- Tipo de pesquisa = "market" já está definido
- **Tópico de pesquisa = "{{research_topic}}"** - descoberto da discussão inicial
- **Objetivos de pesquisa = "{{research_goals}}"** - capturados da discussão inicial
- Foco na clarificação do escopo da pesquisa de mercado
- Capacidades de pesquisa na web estão habilitadas para passos posteriores

## SUA TAREFA:

Inicializar a pesquisa de mercado confirmando entendimento de {{research_topic}} e estabelecendo escopo de pesquisa claro.

## INICIALIZAÇÃO DA PESQUISA DE MERCADO:

### 1. Confirmar Entendimento da Pesquisa

**INICIALIZAR - NÃO PESQUISE AINDA**

Comece com confirmação da pesquisa:
"Eu entendo que você quer conduzir **pesquisa de mercado** para **{{research_topic}}** com estes objetivos: {{research_goals}}

**Meu Entendimento das Suas Necessidades de Pesquisa:**

- **Tópico de Pesquisa**: {{research_topic}}
- **Objetivos de Pesquisa**: {{research_goals}}
- **Tipo de Pesquisa**: Pesquisa de Mercado
- **Abordagem**: Análise de mercado abrangente com verificação de fonte

**Áreas de Pesquisa de Mercado Que Cobriremos:**

- Tamanho de mercado, dinâmicas de crescimento e tendências
- Insights de cliente e análise de comportamento
- Cenário competitivo e posicionamento
- Recomendações estratégicas e orientação de implementação

**Isso captura com precisão o que você está procurando?**"

### 2. Refinar Escopo de Pesquisa

Reúna quaisquer esclarecimentos necessários:

#### Perguntas de Clarificação de Escopo:

- "Existem segmentos de clientes específicos ou aspectos de {{research_topic}} que devemos priorizar?"
- "Devemos focar em regiões geográficas específicas ou mercado global?"
- "Isso é para entrada de mercado, expansão, desenvolvimento de produto ou outro propósito de negócio?"
- "Algum concorrente ou segmento de mercado que você quer especificamente que analisemos?"

### 3. Documentar Escopo Inicial

**ESCREVA IMEDIATAMENTE NO DOCUMENTO**

Escreva o escopo de pesquisa inicial no documento:

```markdown
# Pesquisa de Mercado: {{research_topic}}

## Inicialização da Pesquisa

### Entendimento da Pesquisa Confirmado

**Tópico**: {{research_topic}}
**Objetivos**: {{research_goals}}
**Tipo de Pesquisa**: Pesquisa de Mercado
**Data**: {{date}}

### Escopo da Pesquisa

**Áreas de Foco da Análise de Mercado:**

- Tamanho de mercado, projeções de crescimento e dinâmicas
- Segmentos de cliente, padrões de comportamento e insights
- Cenário competitivo e análise de posicionamento
- Recomendações estratégicas e orientação de implementação

**Metodologia de Pesquisa:**

- Dados da web atuais com verificação de fonte
- Múltiplas fontes independentes para afirmações críticas
- Avaliação de nível de confiança para dados incertos
- Cobertura abrangente sem lacunas críticas

### Próximos Passos

**Fluxo de Trabalho de Pesquisa:**

1. ✅ Inicialização e definição de escopo (passo atual)
2. Insights de Cliente e Análise de Comportamento
3. Análise de Cenário Competitivo
4. Síntese Estratégica e Recomendações

**Status da Pesquisa**: Escopo confirmado, pronto para prosseguir com análise de mercado detalhada
```

### 4. Apresentar Confirmação e Opção Continuar

Mostre o documento de escopo inicial e apresente a opção continuar:
"Eu documentei nosso entendimento e escopo inicial para a pesquisa de mercado de **{{research_topic}}**.

**O que estabeleci:**

- Tópico de pesquisa e objetivos confirmados
- Áreas de foco da análise de mercado definidas
- Verificação da metodologia de pesquisa
- Progressão clara do fluxo de trabalho

**Status do Documento:** Escopo inicial escrito no arquivo de pesquisa para sua revisão

**Pronto para começar a pesquisa de mercado detalhada?**
[C] Continuar - Confirmar escopo e prosseguir para análise de insights de cliente
[Modificar] Sugerir mudanças no escopo de pesquisa antes de prosseguir

### 5. Lidar com Resposta do Usuário

#### Se 'C' (Continuar):

- Atualize frontmatter: `stepsCompleted: [1]`
- Adicione nota de confirmação ao documento: "Escopo confirmado pelo usuário em {{date}}"
- Carregue: `./step-02-customer-insights.md`

#### Se 'Modificar':

- Reúna mudanças do usuário no escopo
- Atualize documento com modificações
- Re-apresente escopo atualizado para confirmação

## MÉTRICAS DE SUCESSO:

✅ Tópico de pesquisa e objetivos entendidos com precisão
✅ Escopo da pesquisa de mercado claramente definido
✅ Documento de escopo inicial escrito imediatamente
✅ Oportunidade do usuário para revisar e modificar escopo
✅ Opção [C] continuar apresentada e tratada corretamente
✅ Documento devidamente atualizado com confirmação de escopo

## MODOS DE FALHA:

❌ Não confirmar entendimento do tópico de pesquisa e objetivos
❌ Gerar conteúdo de pesquisa em vez de apenas clarificação de escopo
❌ Não escrever documento de escopo inicial no arquivo
❌ Não fornecer oportunidade para usuário modificar escopo
❌ Prosseguir para o próximo passo sem confirmação do usuário
❌ **CRÍTICO**: Ler apenas arquivo de passo parcial - leva a entendimento incompleto e decisões de pesquisa ruins
❌ **CRÍTICO**: Prosseguir com 'C' sem ler e entender totalmente o próximo arquivo de passo
❌ **CRÍTICO**: Tomar decisões sem entendimento completo dos requisitos e protocolos do passo

## PRINCÍPIOS DE INICIALIZAÇÃO:

Este passo garante:

- Entendimento mútuo claro dos objetivos de pesquisa
- Escopo e abordagem de pesquisa bem definidos
- Documentação imediata para revisão do usuário
- Controle do usuário sobre a direção da pesquisa antes que o trabalho detalhado comece

## PRÓXIMO PASSO:

Após confirmação do usuário e finalização do escopo, carregue `./step-02-customer-insights.md` para começar a pesquisa de mercado detalhada com análise de insights de cliente.

Lembre-se: Passos init confirmam entendimento e escopo, não geram pesquisa.
