# Criar Diagrama de Fluxo de Dados - Instruções do Fluxo de Trabalho

```xml
<critical>O mecanismo de execução do fluxo de trabalho é governado por: {project_root}/_bmad/core/tasks/workflow.xml</critical>
<critical>Você DEVE já ter carregado e processado: {installed_path}/workflow.yaml</critical>
<critical>Este fluxo de trabalho cria diagramas de fluxo de dados (DFD) no formato Excalidraw.</critical>

<workflow>

  <step n="0" goal="Análise Contextual">
    <action>Revisar a solicitação do usuário e extrair: nível do DFD, processos, depósitos de dados, entidades externas</action>
    <check if="TODOS os requisitos claros"><action>Pular para o Passo 4</action></check>
  </step>

  <step n="1" goal="Identificar Nível do DFD" elicit="true">
    <action>Perguntar: "Qual nível de DFD você precisa?"</action>
    <action>Apresentar opções:
      1. Diagrama de Contexto (Nível 0) - Processo único mostrando limites do sistema
      2. DFD Nível 1 - Processos principais e fluxos de dados
      3. DFD Nível 2 - Subprocessos detalhados
      4. Personalizado - Especifique seus requisitos
    </action>
    <action>AGUARDAR seleção</action>
  </step>

  <step n="2" goal="Coletar Requisitos" elicit="true">
    <action>Perguntar: "Descreva os processos, depósitos de dados e entidades externas no seu sistema"</action>
    <action>AGUARDAR descrição do usuário</action>
    <action>Resumir o que será incluído e confirmar com o usuário</action>
  </step>

  <step n="3" goal="Configuração do Tema" elicit="true">
    <action>Verificar se theme.json existe, perguntar para usar se existir</action>
    <check if="nenhum tema existente">
      <action>Perguntar: "Escolha um esquema de cores para o DFD:"</action>
      <action>Apresentar opções numeradas:
        1. DFD Padrão
           - Processo: #e3f2fd (azul claro)
           - Depósito de Dados: #e8f5e9 (verde claro)
           - Entidade Externa: #f3e5f5 (roxo claro)
           - Borda: #1976d2 (azul)

        2. DFD Colorido
           - Processo: #fff9c4 (amarelo claro)
           - Depósito de Dados: #c5e1a5 (limão claro)
           - Entidade Externa: #ffccbc (coral claro)
           - Borda: #f57c00 (laranja)

        3. DFD Minimalista
           - Processo: #f5f5f5 (cinza claro)
           - Depósito de Dados: #eeeeee (cinza)
           - Entidade Externa: #e0e0e0 (cinza médio)
           - Borda: #616161 (cinza escuro)

        4. Personalizado - Defina suas próprias cores
      </action>
      <action>AGUARDAR seleção</action>
      <action>Criar theme.json com base na seleção</action>
    </check>
  </step>

  <step n="4" goal="Planejar Estrutura do DFD">
    <action>Listar todos os processos com números (1.0, 2.0, etc.)</action>
    <action>Listar todos os depósitos de dados (D1, D2, etc.)</action>
    <action>Listar todas as entidades externas</action>
    <action>Mapear todos os fluxos de dados com rótulos</action>
    <action>Mostrar estrutura planejada, confirmar com o usuário</action>
  </step>

  <step n="5" goal="Carregar Recursos">
    <action>Carregar {{templates}} e extrair a seção `dataflow`</action>
    <action>Carregar {{library}}</action>
    <action>Carregar theme.json</action>
    <action>Carregar {{helpers}}</action>
  </step>

  <step n="6" goal="Construir Elementos do DFD">
    <critical>Seguir a notação DFD padrão de {{helpers}}</critical>

    <substep>Ordem de Construção:
      1. Entidades externas (retângulos, borda negrito)
      2. Processos (círculos/elipses com números)
      3. Depósitos de dados (linhas paralelas ou retângulos)
      4. Fluxos de dados (setas rotuladas)
    </substep>

    <substep>Regras do DFD:
      - Processos: Numerados (1.0, 2.0), frases verbais
      - Depósitos de dados: Nomeados (D1, D2), frases nominais
      - Entidades externas: Nomeadas, frases nominais
      - Fluxos de dados: Rotulados com nomes de dados, setas mostram direção
      - Nenhum fluxo direto entre entidades externas
      - Nenhum fluxo direto entre depósitos de dados
    </substep>

    <substep>Layout:
      - Entidades externas nas bordas
      - Processos no centro
      - Depósitos de dados entre processos
      - Minimizar cruzamento de fluxos
      - Fluxo da esquerda para a direita ou de cima para baixo
    </substep>
  </step>

  <step n="7" goal="Otimizar e Salvar">
    <action>Verificar conformidade com as regras do DFD</action>
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
    <action>Uma vez que a validação passar, confirmar com o usuário</action>
  </step>

  <step n="9" goal="Validar Conteúdo">
    <invoke-task>Validar contra {{validation}}</invoke-task>
  </step>

</workflow>
```
