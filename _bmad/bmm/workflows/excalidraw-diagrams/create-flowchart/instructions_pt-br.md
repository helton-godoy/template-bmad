# Criar Fluxograma - Instruções do Fluxo de Trabalho

```xml
<critical>O mecanismo de execução do fluxo de trabalho é governado por: {project_root}/_bmad/core/tasks/workflow.xml</critical>
<critical>Você DEVE já ter carregado e processado: {installed_path}/workflow.yaml</critical>
<critical>Este fluxo de trabalho cria uma visualização de fluxograma em formato Excalidraw para processos, pipelines ou fluxos lógicos.</critical>

<workflow>

  <step n="0" goal="Análise Contextual (Elicitação Inteligente)">
    <critical>Antes de fazer qualquer pergunta, analise o que o usuário já lhe disse</critical>

    <action>Revisar a solicitação inicial do usuário e histórico de conversa</action>
    <action>Extrair qualquer menção de: tipo de fluxograma, complexidade, pontos de decisão, local de salvamento</action>

    <check if="TODOS os requisitos são claros do contexto">
      <action>Resumir seu entendimento</action>
      <action>Pular diretamente para o Passo 4 (Planejar Layout do Fluxograma)</action>
    </check>

    <check if="ALGUNS requisitos são claros">
      <action>Notar o que você já sabe</action>
      <action>Perguntar apenas sobre informações faltantes no Passo 1</action>
    </check>

    <check if="requisitos são pouco claros ou mínimos">
      <action>Prosseguir com elicitação completa no Passo 1</action>
    </check>
  </step>

  <step n="1" goal="Coletar Requisitos" elicit="true">
    <action>Perguntar Questão 1: "Que tipo de fluxo de processo você precisa visualizar?"</action>
    <action>Apresentar opções numeradas:
      1. Fluxo de Processo de Negócio - Documentar fluxos de trabalho de negócios, processos de aprovação ou procedimentos operacionais
      2. Fluxo de Algoritmo/Lógica - Visualizar lógica de código, árvores de decisão ou processos computacionais
      3. Fluxo de Jornada do Usuário - Mapear interações do usuário, caminhos de navegação ou fluxos de experiência
      4. Pipeline de Processamento de Dados - Mostrar transformação de dados, processos ETL ou estágios de processamento
      5. Outro - Descreva suas necessidades específicas de fluxograma
    </action>
    <action>AGUARDAR seleção do usuário (1-5)</action>

    <action>Perguntar Questão 2: "Quantos passos principais existem neste fluxo?"</action>
    <action>Apresentar opções numeradas:
      1. Simples (3-5 passos) - Processo rápido com poucos pontos de decisão
      2. Médio (6-10 passos) - Fluxo de trabalho padrão com alguma ramificação
      3. Complexo (11-20 passos) - Processo detalhado com múltiplos pontos de decisão
      4. Muito Complexo (20+ passos) - Fluxo de trabalho abrangente exigindo layout cuidadoso
    </action>
    <action>AGUARDAR seleção do usuário (1-4)</action>
    <action>Armazenar seleção em {{complexity}}</action>

    <action>Perguntar Questão 3: "Seu fluxo inclui pontos de decisão (ramificações sim/não)?"</action>
    <action>Apresentar opções numeradas:
      1. Sem decisões - Fluxo linear do início ao fim
      2. Poucas decisões (1-2) - Ramificação simples com caminhos sim/não
      3. Múltiplas decisões (3-5) - Várias ramificações condicionais
      4. Decisões complexas (6+) - Lógica de ramificação extensiva
    </action>
    <action>AGUARDAR seleção do usuário (1-4)</action>
    <action>Armazenar seleção em {{decision_points}}</action>

    <action>Perguntar Questão 4: "Onde o fluxograma deve ser salvo?"</action>
    <action>Apresentar opções numeradas:
      1. Localização padrão - docs/flowcharts/[nome-gerado-auto].excalidraw
      2. Caminho personalizado - Especifique seu próprio caminho de arquivo
      3. Raiz do projeto - Salvar no diretório principal do projeto
      4. Pasta específica - Escolher de pastas existentes
    </action>
    <action>AGUARDAR seleção do usuário (1-4)</action>
    <check if="seleção é 2 ou 4">
      <action>Pedir caminho específico</action>
      <action>AGUARDAR entrada do usuário</action>
    </check>
    <action>Armazenar caminho final em {{default_output_file}}</action>
  </step>

  <step n="2" goal="Verificar Tema Existente" elicit="true">
    <action>Verificar se theme.json existe na localização de saída</action>
    <check if="theme.json existe">
      <action>Perguntar: "Tema existente encontrado. Usá-lo? (sim/não)"</action>
      <action>AGUARDAR resposta do usuário</action>
      <check if="usuário diz sim">
        <action>Carregar e usar tema existente</action>
        <action>Pular para o Passo 4</action>
      </check>
      <check if="usuário diz não">
        <action>Prosseguir para o Passo 3</action>
      </check>
    </check>
    <check if="theme.json não existe">
      <action>Prosseguir para o Passo 3</action>
    </check>
  </step>

  <step n="3" goal="Criar Tema" elicit="true">
    <action>Perguntar: "Vamos criar um tema para seu fluxograma. Escolha um esquema de cores:"</action>
    <action>Apresentar opções numeradas:
      1. Azul Profissional
         - Preenchimento Primário: #e3f2fd (azul claro)
         - Acento/Borda: #1976d2 (azul)
         - Decisão: #fff3e0 (laranja claro)
         - Texto: #1e1e1e (cinza escuro)

      2. Verde Sucesso
         - Preenchimento Primário: #e8f5e9 (verde claro)
         - Acento/Borda: #388e3c (verde)
         - Decisão: #fff9c4 (amarelo claro)
         - Texto: #1e1e1e (cinza escuro)

      3. Cinza Neutro
         - Preenchimento Primário: #f5f5f5 (cinza claro)
         - Acento/Borda: #616161 (cinza)
         - Decisão: #e0e0e0 (cinza médio)
         - Texto: #1e1e1e (cinza escuro)

      4. Laranja Quente
         - Preenchimento Primário: #fff3e0 (laranja claro)
         - Acento/Borda: #f57c00 (laranja)
         - Decisão: #ffe0b2 (pêssego)
         - Texto: #1e1e1e (cinza escuro)

      5. Cores Personalizadas - Defina sua própria paleta de cores
    </action>
    <action>AGUARDAR seleção do usuário (1-5)</action>
    <action>Armazenar seleção em {{theme_choice}}</action>

    <check if="seleção é 5 (Personalizado)">
      <action>Perguntar: "Cor de preenchimento primário (código hex)?"</action>
      <action>AGUARDAR entrada do usuário</action>
      <action>Armazenar em {{custom_colors.primary_fill}}</action>
      <action>Perguntar: "Cor de acento/borda (código hex)?"</action>
      <action>AGUARDAR entrada do usuário</action>
      <action>Armazenar em {{custom_colors.accent}}</action>
      <action>Perguntar: "Cor de decisão (código hex)?"</action>
      <action>AGUARDAR entrada do usuário</action>
      <action>Armazenar em {{custom_colors.decision}}</action>
    </check>

    <action>Criar theme.json com as cores selecionadas</action>
    <action>Mostrar prévia do tema com todas as cores</action>
    <action>Perguntar: "O tema parece bom?"</action>
    <action>Apresentar opções numeradas:
      1. Sim, usar este tema - Prosseguir com o tema
      2. Não, ajustar cores - Modificar seleções de cor
      3. Começar de novo - Escolher predefinição diferente
    </action>
    <action>AGUARDAR seleção (1-3)</action>
    <check if="seleção é 2 ou 3">
      <action>Repetir Passo 3</action>
    </check>
  </step>

  <step n="4" goal="Planejar Layout do Fluxograma">
    <action>Listar todos os passos e pontos de decisão baseados nos requisitos coletados</action>
    <action>Mostrar ao usuário a estrutura planejada</action>
    <action>Perguntar: "A estrutura parece correta? (sim/não)"</action>
    <action>AGUARDAR resposta do usuário</action>
    <check if="usuário diz não">
      <action>Ajustar estrutura com base no feedback</action>
      <action>Repetir este passo</action>
    </check>
  </step>

  <step n="5" goal="Carregar Modelo e Recursos">
    <action>Carregar arquivo {{templates}}</action>
    <action>Extrair seção `flowchart` do YAML</action>
    <action>Carregar arquivo {{library}}</action>
    <action>Carregar theme.json e mesclar cores com modelo</action>
    <action>Carregar {{helpers}} para diretrizes de criação de elemento</action>
  </step>

  <step n="6" goal="Construir Elementos do Fluxograma">
    <critical>Seguir diretrizes de {{helpers}} para criação adequada de elementos</critical>

    <action>Construir UMA seção por vez seguindo estas regras:</action>

    <substep>Para Cada Forma com Rótulo:
      1. Gerar IDs únicos (shape-id, text-id, group-id)
      2. Criar forma com groupIds: [group-id]
      3. Calcular largura do texto: (texto.length × fontSize × 0.6) + 20, arredondar para 10 mais próximo
      4. Criar elemento de texto com:
         - containerId: shape-id
         - groupIds: [group-id] (MESMO que a forma)
         - textAlign: "center"
         - verticalAlign: "middle"
         - width: largura calculada
      5. Adicionar boundElements à forma referenciando texto
    </substep>

    <substep>Para Cada Seta:
      1. Determinar tipo de seta necessário:
         - Reta: Para fluxo direto (esquerda-para-direita, cima-para-baixo)
         - Cotovelo: Para fluxo ascendente, fluxo reverso ou roteamento complexo
      2. Criar seta com startBinding e endBinding
      3. Definir startBinding.elementId para ID da forma fonte
      4. Definir endBinding.elementId para ID da forma alvo
      5. Definir gap: 10 para ambas as ligações
      6. Se seta de cotovelo, adicionar pontos intermediários para mudanças de direção
      7. Atualizar boundElements em ambas as formas conectadas
    </substep>

    <substep>Alinhamento:
      - Ajustar todos x, y para grade de 20px
      - Alinhar formas verticalmente (mesmo x para fluxo vertical)
      - Espaçar elementos: 60px entre formas
    </substep>

    <substep>Ordem de Construção:
      1. Ponto de início (círculo) com rótulo
      2. Cada passo do processo (retângulo) com rótulo
      3. Cada ponto de decisão (diamante) com rótulo
      4. Ponto final (círculo) com rótulo
      5. Conectar tudo com setas ligadas
    </substep>
  </step>

  <step n="7" goal="Otimizar e Salvar">
    <action>Remover elementos não utilizados e elementos com isDeleted: true</action>
    <action>Salvar em {{default_output_file}}</action>
  </step>

  <step n="8" goal="Validar Sintaxe JSON">
    <critical>NUNCA delete o arquivo se a validação falhar - sempre corrija os erros de sintaxe</critical>
    <action>Executar: node -e "JSON.parse(require('fs').readFileSync('{{default_output_file}}', 'utf8')); console.log('✓ JSON Válido')"</action>
    <check if="validação falhar (código de saída 1)">
      <action>Ler a mensagem de erro cuidadosamente - ela mostra o erro de sintaxe e a posição</action>
      <action>Abrir o arquivo e navegar para a localização do erro</action>
      <action>Corrigir o erro de sintaxe (adicionar vírgula, colchete ou aspas faltando conforme indicado)</action>
      <action>Salvar o arquivo</action>
      <action>Reexecutar a validação com o mesmo comando</action>
      <action>Repetir até a validação passar</action>
    </check>
    <action>Uma vez que a validação passar, confirmar com o usuário: "Fluxograma criado em {{default_output_file}}. Abrir para visualizar?"</action>
  </step>

  <step n="9" goal="Validar Conteúdo">
    <invoke-task>Validar contra checklist em {{validation}} usando {_bmad}/core/tasks/validate-workflow.xml</invoke-task>
  </step>

</workflow>
```
