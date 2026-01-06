# Criar Diagrama - Instruções do Fluxo de Trabalho

```xml
<critical>O mecanismo de execução do fluxo de trabalho é governado por: {project_root}/_bmad/core/tasks/workflow.xml</critical>
<critical>Você DEVE já ter carregado e processado: {installed_path}/workflow.yaml</critical>
<critical>Este fluxo de trabalho cria diagramas de arquitetura de sistema, ERDs, diagramas UML ou diagramas técnicos gerais no formato Excalidraw.</critical>

<workflow>

  <step n="0" goal="Análise Contextual">
    <action>Revisar a solicitação do usuário e extrair: tipo de diagrama, componentes/entidades, relacionamentos, preferências de notação</action>
    <check if="TODOS os requisitos claros"><action>Pular para o Passo 5</action></check>
    <check if="ALGUNS requisitos claros"><action>Perguntar apenas sobre informações faltantes nos Passos 1-2</action></check>
  </step>

  <step n="1" goal="Identificar Tipo de Diagrama" elicit="true">
    <action>Perguntar: "Qual tipo de diagrama técnico você precisa?"</action>
    <action>Apresentar opções:
      1. Arquitetura de Sistema
      2. Diagrama Entidade-Relacionamento (ERD)
      3. Diagrama de Classes UML
      4. Diagrama de Sequência UML
      5. Diagrama de Casos de Uso UML
      6. Diagrama de Rede
      7. Outro
    </action>
    <action>AGUARDAR seleção</action>
  </step>

  <step n="2" goal="Coletar Requisitos" elicit="true">
    <action>Perguntar: "Descreva os componentes/entidades e seus relacionamentos"</action>
    <action>Perguntar: "Qual padrão de notação? (Padrão/Simplificado/UML-ERD Estrito)"</action>
    <action>AGUARDAR entrada do usuário</action>
    <action>Resumir o que será incluído e confirmar com o usuário</action>
  </step>

  <step n="3" goal="Verificar Tema Existente" elicit="true">
    <action>Verificar se theme.json existe na localização de saída</action>
    <check if="existe"><action>Perguntar para usar, carregar se sim, senão prosseguir para Passo 4</action></check>
    <check if="não existe"><action>Prosseguir para Passo 4</action></check>
  </step>

  <step n="4" goal="Criar Tema" elicit="true">
    <action>Perguntar: "Escolha um esquema de cores para seu diagrama:"</action>
    <action>Apresentar opções numeradas:
      1. Profissional
         - Componente: #e3f2fd (azul claro)
         - Banco de Dados: #e8f5e9 (verde claro)
         - Serviço: #fff3e0 (laranja claro)
         - Borda: #1976d2 (azul)

      2. Colorido
         - Componente: #e1bee7 (roxo claro)
         - Banco de Dados: #c5e1a5 (limão claro)
         - Serviço: #ffccbc (coral claro)
         - Borda: #7b1fa2 (roxo)

      3. Minimalista
         - Componente: #f5f5f5 (cinza claro)
         - Banco de Dados: #eeeeee (cinza)
         - Serviço: #e0e0e0 (cinza médio)
         - Borda: #616161 (cinza escuro)

      4. Personalizado - Defina suas próprias cores
    </action>
    <action>AGUARDAR seleção</action>
    <action>Criar theme.json com base na seleção</action>
    <action>Mostrar prévia e confirmar</action>
  </step>

  <step n="5" goal="Planejar Estrutura do Diagrama">
    <action>Listar todos os componentes/entidades</action>
    <action>Mapear todos os relacionamentos</action>
    <action>Mostrar layout planejado</action>
    <action>Perguntar: "A estrutura parece correta? (sim/não)"</action>
    <check if="não"><action>Ajustar e repetir</action></check>
  </step>

  <step n="6" goal="Carregar Recursos">
    <action>Carregar {{templates}} e extrair a seção `diagram`</action>
    <action>Carregar {{library}}</action>
    <action>Carregar theme.json e mesclar com o modelo</action>
    <action>Carregar {{helpers}} para diretrizes</action>
  </step>

  <step n="7" goal="Construir Elementos do Diagrama">
    <critical>Seguir {{helpers}} para criação adequada de elementos</critical>

    <substep>Para Cada Componente:
      - Gerar IDs únicos (component-id, text-id, group-id)
      - Criar forma com groupIds
      - Calcular largura do texto
      - Criar texto com containerId e groupIds correspondentes
      - Adicionar boundElements
    </substep>

    <substep>Para Cada Conexão:
      - Determinar tipo de seta (reta/cotovelo)
      - Criar com startBinding e endBinding
      - Atualizar boundElements em ambos os componentes
    </substep>

    <substep>Ordem de Construção por Tipo:
      - Arquitetura: Serviços → Bancos de Dados → Conexões → Rótulos
      - ERD: Entidades → Atributos → Relacionamentos → Cardinalidade
      - UML Classe: Classes → Atributos → Métodos → Relacionamentos
      - UML Sequência: Atores → Linhas de Vida → Mensagens → Retornos
      - UML Casos de Uso: Atores → Casos de Uso → Relacionamentos
    </substep>

    <substep>Alinhamento:
      - Ajustar à grade de 20px
      - Espaço: 40px entre componentes, 60px entre seções
    </substep>
  </step>

  <step n="8" goal="Otimizar e Salvar">
    <action>Remover elementos não utilizados e elementos com isDeleted: true</action>
    <action>Salvar em {{default_output_file}}</action>
  </step>

  <step n="9" goal="Validar Sintaxe JSON">
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
    <action>Uma vez que a validação passar, confirmar: "Diagrama criado em {{default_output_file}}. Abrir para visualizar?"</action>
  </step>

  <step n="10" goal="Validar Conteúdo">
    <invoke-task>Validar contra {{validation}} usando {_bmad}/core/tasks/validate-workflow.xml</invoke-task>
  </step>

</workflow>
```
