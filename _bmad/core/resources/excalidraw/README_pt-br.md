# Recursos principais do Excalidraw

Conhecimento universal para criar diagramas Excalidraw. Todos os agentes que criam arquivos Excalidraw devem referenciar esses recursos.

## Objecto

Fornece o **HOW**(conhecimento universal) enquanto os agentes fornecem o**WHAT** (aplicação específica do domínio).

**Core = "Como criar elementos Excalidraw"**

- Como agrupar formas com rótulos de texto
- Como calcular a largura do texto
- Como criar setas com ligações adequadas
- Como validar a sintaxe JSON
- Estrutura de base e primitivos

**Agentes = "Que diagramas criar"**

- Frame Expert (BMM): Fluxogramas técnicos, diagramas de arquitetura, wireframes
- Mestre de Apresentação (CIS): Decks, visuais criativos, máquinas Rube Goldberg
- Tech Writer (BMM): diagramas de documentação, explicações de conceito

## Arquivos nesta pasta

### excalidraw-helpers.md

**Padrões de criação de elementos universais**

- Cálculo da largura do texto
- Regras de agrupamento de elementos (formas + rótulos)
- Alinhamento da grade
- Criação de setas (direita, cotovelo)
- Aplicação de tema
- Verificação de validação
- Regras de otimização

**Os agentes referem-se a:**

- Criar formas devidamente agrupadas
- Calcular dimensões de texto
- Ligar elementos com setas
- Assegurar estrutura válida

### validate-json-instructions.md

**Processo universal de validação da JSON**

- Como validar Excalidraw JSON
- Erros e correções comuns
- Integração do fluxo de trabalho
- Recuperação de erros

**Os agentes referem-se a:**

- Validar arquivos após a criação
- Corrigir erros de sintaxe
- Certifique-se de que os arquivos podem ser abertos em Excalidraw

### library-loader.md (Futuro)

**Como carregar arquivos .excalidrawlib externos**

- Carregamento de biblioteca programática
- Integração da biblioteca comunitária
- Gestão personalizada de bibliotecas

**Estatus:** A ser desenvolvido ao implementar suporte de biblioteca externa.

## Como os agentes usam esses recursos

### Exemplo: Especialista em molduras (Diagramas Técnicos)

```yaml

# workflows/excalidraw-diagrams/create-flowchart/workflow.yaml
helpers: '{project-root}/_bmad/core/resources/excalidraw/excalidraw-helpers.md'
json_validation: '{project-root}/_bmad/core/resources/excalidraw/validate-json-instructions.md'

```

**Adições específicas do domínio:**

```yaml

# workflows/excalidraw-diagrams/_shared/flowchart-templates.yaml
flowchart:
  start_node:
    type: ellipse
    width: 120
    height: 60
  process_box:
    type: rectangle
    width: 160
    height: 80
  decision_diamond:
    type: diamond
    width: 140
    height: 100

```

### Exemplo: Mestre de Apresentação (visual Criativo)

```yaml

# workflows/create-visual-metaphor/workflow.yaml
helpers: '{project-root}/_bmad/core/resources/excalidraw/excalidraw-helpers.md'
json_validation: '{project-root}/_bmad/core/resources/excalidraw/validate-json-instructions.md'

```

**Adições específicas do domínio:**

```yaml

# workflows/_shared/creative-templates.yaml
rube_goldberg:
  whimsical_connector:
    type: arrow
    strokeStyle: dashed
    roughness: 2
  playful_box:
    type: rectangle
    roundness: 12

```

## O que não pertence ao núcleo

**Elementos específicos do domínio:**

- Modelos específicos de fluxograma (pertencente em quadros)
- Disposição do convés (pertencente ao Mestre da Apresentação)
- Estilos específicos da documentação (pertence ao Tech Writer)

**Agent Workflows:**

- Como criar um fluxograma (Frame Expert workflow)
- Como criar uma plataforma de pitch (workflow Master Apresentação)
- Criação de diagrama passo-a-passo (agente específico)

**Theming:**

- Atualmente em fluxos de trabalho de agentes
- **Futuro:** Será refactorado para núcleo como temas configuráveis pelo utilizador

## Princípio da arquitectura

**Fonte Única da Verdade:**

- O núcleo detém o conhecimento universal
- Núcleo de referência dos agentes, não duplicar
- Atualizações para beneficiar todos os agentes
- Agentes especializados com conhecimento de domínio

**DRY (Não se repita):**

- Lógica de criação de elementos: uma vez no núcleo
- Cálculo da largura do texto: ONCE no núcleo
- Processo de validação: Uma vez no núcleo
- Padrões de ligação de setas: ONCE no núcleo

## Melhorias futuras

1. **Library carregador externo** - Carregar arquivos .excalidrawlib de libraries.excalidraw.com
2. **Theme Management** - Temas de cores configuráveis pelo usuário salvos no núcleo
3. **Biblioteca Component** - Componentes reutilizáveis partilhados entre agentes
4. **Algoritmos de Layout** - Ajudadores de auto-layout para elementos de posicionamento
