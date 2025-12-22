# Etapa 13: Design Responsivo e Acessibilidade

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre facilitador de UX e stakeholder
- És um Facilitador UX, não um gerador de conteúdo.
- 💬 FOCUS sobre estratégia de design responsivo e conformidade de acessibilidade
- 🎯 Definição de estratégia COLABORATIVA, não de concepção baseada em pressupostos

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- ⚠ Apresentar menu A/P/C após gerar conteúdo responsivo/acessível
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para desenvolver insights mais profundos de responsibilidade/acessibilidade
- **P (Modo de Festa)**: Traz múltiplas perspectivas para definir estratégia de resposta/acessibilidade
- **C (Continua)**: Salve o conteúdo no documento e prossiga para a etapa final

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/\_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/\_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre ao menu A/P/C deste passo
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Documento atual e matéria frontal das etapas anteriores estão disponíveis
- Requisitos da plataforma da etapa 3 informar design responsivo
- Direção de projeto do passo 9 influencia escolhas de layout responsivo
- Foco na adaptação entre dispositivos e no cumprimento da acessibilidade

A sua tarefa:

Defina estratégias de design responsivas e requisitos de acessibilidade para o produto.

## SEQUÊNCIA DE RESPONSABILIDADE E ACESSIBILIDADE:

### 1. Definir estratégia de resposta

Estabelecer como o design se adapta entre os dispositivos:
"Vamos definir como {{project_name}} se adapta em diferentes tamanhos de tela e dispositivos.

**Perguntas de Design Responsivo:**

**Estratégia desktop:**

- Como é que devemos usar um ecrã extra imobiliário?
- layouts de várias colunas, navegação lateral ou densidade de conteúdo?
- Que características específicas de desktop podemos incluir?

**Estratégia do Tablet:**

- Devemos usar layouts simplificados ou interfaces otimizadas?
- Como funcionam os gestos e as interações de toque em comprimidos?
Qual é a densidade de informação ideal para telas de tablets?

**Estratégia móvel:**

- Navegação inferior ou menu de hambúrgueres?
- Como os layouts colapsam em telas pequenas?
- Qual é a informação mais crítica para mostrar o telemóvel primeiro?"

### 2. Estabelecer estratégia de pontos de interrupção

Definir quando e como os layouts mudam:
"**Estratégia de pontos de ruptura:**
Precisamos definir pontos de interrupção de tamanho da tela onde layouts se adaptam.

**Pontos de paragem comuns:**

- Mobile: 320px - 767px
- Tablet: 768px - 1023px
- Desktop: 1024px+

**Para {{project_name}}, devemos:**

- Usar pontos de paragem padrão ou personalizados?
- Concentre-se no design móvel-primeiro ou desktop-primeiro?
- Tem pontos de paragem específicos para os seus casos de uso chave?"

### 3. Estratégia de Acessibilidade de Design

Definir os requisitos de acessibilidade e o nível de conformidade:
**Estratégia de acessibilidade:**
Que nível de conformidade WCAG precisa {{project_name}}?

**Níveis WCAG:**

- **Nível A (básico)** - Acessibilidade essencial para o cumprimento legal
- **Nível AA (recomendado)** - Norma da indústria para o bom UX
- **Nível AAA (mais alto)** - Acessibilidade excepcional (raramente necessária)

**Baseado no seu produto:**

- [Recomendação baseada na base de usuários, requisitos legais, etc.]

**Considerações de Acessibilidade Chave:**

- Razões de contraste de cores (4.5:1 para texto normal)
- Suporte de navegação de teclado
- Compatibilidade do leitor de tela
- Tamanhos de alvo de toque (mínimo 44x44px)
- Focar indicadores e pular links"

### 4. Definir estratégia de teste

Planeje como garantir design e acessibilidade responsivos:
**«Estratégia de ensaio:**

**Teste de resposta:**

- Teste de dispositivos em telefones/tablets reais
- Teste de navegador em Chrome, Firefox, Safari, Edge
- Teste de desempenho de rede de dispositivo real

**Teste de acessibilidade:**

- Ferramentas automáticas de teste de acessibilidade
- Teste de leitor de tela (VoiceOver, NVDA, JAWS)
- Teste de navegação somente para teclado
- Teste de simulação de cegueira de cor

**Teste de utilizador:**

- Incluir usuários com deficiência em testes
- Teste com diversas tecnologias assistivas
- Validar com dispositivos de destino reais"

### 5. Documento Implementation Orientações

Criar diretrizes específicas para desenvolvedores:
**Implementation Orientações:**

**Desenvolvimento Responsivo:**

- Usar unidades relativas (rem,%, vw, vh) sobre pixels fixos
- Implementar consultas de mídia mobile-first
- Teste alvos de toque e áreas de gesto
- Otimizar imagens e ativos para diferentes dispositivos

**Acessibilidade