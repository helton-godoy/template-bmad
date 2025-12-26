# Passo 1 de Pesquisa de Mercado: Inicialização de Pesquisa de Mercado

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

- 🛑 NUNCA gere conteúdo de pesquisa na etapa de inicialização
- ✅ SEMPRE confirme a compreensão dos objetivos de pesquisa do usuário
- 📋 VOCÊ É UM FACILITADOR DE PESQUISA DE MERCADO, não um gerador de conteúdo
- 💬 FOQUE em esclarecer escopo e abordagem
- 🔍 SEM PESQUISA NA WEB na inicialização - isso é para etapas posteriores
- 📖 CRÍTICO: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a pesquisas incompletas
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido e compreendido antes de prosseguir

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Confirme a compreensão da pesquisa antes de prosseguir
- ⚠️ Apresente a opção [C] continuar após o esclarecimento do escopo
- 💾 Escreva o documento de escopo inicial imediatamente
- 📖 Atualize o frontmatter `stepsCompleted: [1]` antes de carregar o próximo passo
- 🚫 PROIBIDO carregar o próximo passo até que C seja selecionado

## LIMITES DE CONTEXTO:

- Documento atual e frontmatter da descoberta principal do fluxo de trabalho estão disponíveis
- Tipo de pesquisa = "market" já está definido
- **Tópico de pesquisa = "{{research_topic}}"** - descoberto da discussão inicial
- **Objetivos de pesquisa = "{{research_goals}}"** - capturados da discussão inicial
- Foco no esclarecimento do escopo da pesquisa de mercado
- Capacidades de pesquisa na web estão habilitadas para etapas posteriores

## SUA TAREFA:

Inicialize a pesquisa de mercado confirmando a compreensão de {{research_topic}} e estabelecendo um escopo de pesquisa claro.

## INICIALIZAÇÃO DA PESQUISA DE MERCADO:

### 1. Confirmar Compreensão da Pesquisa

**INICIALIZAR - NÃO PESQUISE AINDA**

Comece com a confirmação da pesquisa:
"Eu entendo que você quer realizar **pesquisa de mercado** para **{{research_topic}}** com estes objetivos: {{research_goals}}

**Minha Compreensão das Suas Necessidades de Pesquisa:**

- **Tópico de Pesquisa**: {{research_topic}}
- **Objetivos de Pesquisa**: {{research_goals}}
- **Tipo de Pesquisa**: Pesquisa de Mercado
- **Abordagem**: Análise de mercado abrangente com verificação de fonte

**Áreas de Pesquisa de Mercado Que Cobriremos:**

- Tamanho do mercado, dinâmica de crescimento e tendências
- Insights de clientes e análise de comportamento
- Cenário competitivo e posicionamento
- Recomendações estratégicas e orientação de implementação

**Isso captura com precisão o que você está procurando?**"

### 2. Refinar Escopo da Pesquisa

Reúna quaisquer esclarecimentos necessários:

#### Perguntas de Esclarecimento de Escopo:

- "Existem segmentos de clientes específicos ou aspectos de {{research_topic}} que devemos priorizar?"
- "Devemos focar em regiões geográficas específicas ou mercado global?"
- "Isso é para entrada no mercado, expansão, desenvolvimento de produto ou outro propósito de negócios?"
- "Algum concorrente ou segmento de mercado que você queira especificamente que analisemos?"

### 3. Documentar Escopo Inicial

**ESCREVA IMEDIATAMENTE NO DOCUMENTO**

Escreva o escopo inicial da pesquisa no documento:

```markdown
# Market Research: {{research_topic}}

## Research Initialization

### Research Understanding Confirmed

**Topic**: {{research_topic}}
**Goals**: {{research_goals}}
**Research Type**: Market Research
**Date**: {{date}}

### Research Scope

**Market Analysis Focus Areas:**

- Market size, growth projections, and dynamics
- Customer segments, behavior patterns, and insights
- Competitive landscape and positioning analysis
- Strategic recommendations and implementation guidance

**Research Methodology:**

- Current web data with source verification
- Multiple independent sources for critical claims
- Confidence level assessment for uncertain data
- Comprehensive coverage with no critical gaps

### Next Steps

**Research Workflow:**

1. ✅ Initialization and scope setting (current step)
2. Customer Insights and Behavior Analysis
3. Competitive Landscape Analysis
4. Strategic Synthesis and Recommendations

**Research Status**: Scope confirmed, ready to proceed with detailed market analysis
```

### 4. Apresentar Confirmação e Opção Continuar

Mostre o documento de escopo inicial e apresente a opção continuar:
"Documentei nossa compreensão e escopo inicial para a pesquisa de mercado de **{{research_topic}}**.

**O que estabeleci:**

- Tópico e objetivos de pesquisa confirmados
- Áreas de foco da análise de mercado definidas
- Verificação da metodologia de pesquisa
- Progressão clara do fluxo de trabalho

**Status do Documento:** Escopo inicial escrito no arquivo de pesquisa para sua revisão

**Pronto para começar a pesquisa de mercado detalhada?**
[C] Continuar - Confirmar escopo e prosseguir para análise de insights de clientes
[Modificar] Sugerir alterações no escopo da pesquisa antes de prosseguir

### 5. Lidar com Resposta do Usuário

#### Se 'C' (Continuar):

- Atualize frontmatter: `stepsCompleted: [1]`
- Adicione nota de confirmação ao documento: "Scope confirmed by user on {{date}}"
- Carregue: `./step-02-customer-insights_pt-br.md`

#### Se 'Modificar':

- Reúna alterações do usuário no escopo
- Atualize o documento com as modificações
- Re-apresente o escopo atualizado para confirmação

## MÉTRICAS DE SUCESSO:

✅ Tópico e objetivos de pesquisa compreendidos com precisão
✅ Escopo de pesquisa de mercado claramente definido
✅ Documento de escopo inicial escrito imediatamente
✅ Oportunidade do usuário para revisar e modificar o escopo
✅ Opção [C] continuar apresentada e tratada corretamente
✅ Documento devidamente atualizado com confirmação de escopo

## MODOS DE FALHA:

❌ Não confirmar a compreensão do tópico e objetivos de pesquisa
❌ Gerar conteúdo de pesquisa em vez de apenas esclarecimento de escopo
❌ Não escrever o documento de escopo inicial no arquivo
❌ Não fornecer oportunidade para o usuário modificar o escopo
❌ Prosseguir para o próximo passo sem confirmação do usuário
❌ **CRÍTICO**: Ler apenas parte do arquivo de passo - leva a compreensão incompleta e más decisões de pesquisa
❌ **CRÍTICO**: Prosseguir com 'C' sem ler e compreender totalmente o próximo arquivo de passo
❌ **CRÍTICO**: Tomar decisões sem compreensão completa dos requisitos e protocolos do passo

## PRINCÍPIOS DE INICIALIZAÇÃO:

Este passo garante:

- Clareza mútua compreensão dos objetivos de pesquisa
- Escopo e abordagem de pesquisa bem definidos
- Documentação imediata para revisão do usuário
- Controle do usuário sobre a direção da pesquisa antes que o trabalho detalhado comece

## PRÓXIMO PASSO:

Após a confirmação do usuário e finalização do escopo, carregue `./step-02-customer-insights_pt-br.md` para iniciar a pesquisa de mercado detalhada com análise de insights de clientes.

Lembre-se: Passos de inicialização confirmam compreensão e escopo, não geram conteúdo de pesquisa!
