# Criar Diagrama - Instruções de fluxo de trabalho

```xml
<critical>O motor de execução de fluxo de trabalho é regido por: {project_root}/ bmad/core/tasks/workflow.xml</critical>
<critical>Você já deve ter carregado e processado: {installed_path}/workflow.yaml</critical>
<critical>Este fluxo de trabalho cria diagramas de arquitetura do sistema, ERDs, diagramas UML ou diagramas técnicos gerais em formato Excalidraw. </critical>

<workflow>

<step n="0" goal="Contextual Analysis">
<action>Reveja o pedido e extrato do usuário: tipo de diagrama, componentes/entidades, relações, preferências de notação</action>
<check if="ALL requirements clear">BADPROTECT100 ENDSkip to Step 5</action>BADPROTECT098 END
<check if="SOME requirements clear">BAMADPROTECT096EndApenas pergunte sobre informações em falta em Passos 1-2</action>BADPROTECT094End
</step>

<step n="1" goal="Identify Diagram Type" elicit="true">
<action>Ask: "Que tipo de diagrama técnico você precisa? " </action>
<action>Present options:
1. Arquitetura do sistema
2. Diagrama de Entity-Relationship (ERD)
3. Diagrama de Classe UML
4. Diagrama de Sequência UML
5. Diagrama de caso de uso de UML
6. Diagrama de Rede
7. Outros
</action>
<action>WAIT for selection</action>
</step>

<step n="2" goal="Gather Requirements" elicit="true">
<action>Ask: "Descreva os componentes/entidades e suas relações"</action>
<action>Ask: "Que padrão de notação? (Standard/Simplified/Strict UML-ERD)"</action>
<action>WAIT for user input</action>
<action>Sumarizar o que será incluído e confirmar com o usuário</action>
</step>

<step n="3" goal="Check for Existing Theme" elicit="true">
<action> Verifique se o theme.json existe no local de saída</action>
<check if="exists">BADPROTECT070EndPeça para usá-lo, carregar se sim, então prossiga para Passo 4BMADPROTECT069EndBMADPROTECT068End
<check if="not exists">BADPROTECT066 EndProtect066EndProtect065 ENDBADPROTECT064End
</step>

<step n="4" goal="Create Theme" elicit="true">
<action>Ask: "Escolha um esquema de cores para o seu diagrama:"</action>
<action>Present numeradas opções:
1. Profissional
         - Component: #e3f2fd (azul claro)
         - Database: #e8f5e9 (verde claro)
         - Service: #fff3e0 (laranja clara)
         - Border: #1976d2 (azul)

2. Colorido
         - Component: #e1bee7 (púrpura clara)
         - Database: #c5e1a5 (limão leve)
         - Service: #ffccbc (corais leves)
         - Border: #7b1fa2 (roxo)

3. Mínimo
         - Component: #f5f5f5 (cinzento claro)
         - Database: #eeeeee (cinza)
         - Service: #e0e0e0 (cinzento médio)
         - Border: #616161 (cinzento escuro)

4. Personalizado - Defina suas próprias cores
</action>
<action>WAIT for selection</action>
<action>Create theme.json baseado na seleção</action>
<action>Mostrar visualização e confirmar</action>
</step>

<step n="5" goal="Plan Diagram Structure">
BMADPROTECT049EndLista de todos os componentes/entidadesBMADPROTECT048End
<action>Mapa de todas as relações</action>
<action>Show BMADPROTECT000End layout</action>
"A estrutura parece correcta? (sim/não)"</action>
BMADPROTECT041EndBMADPROTECT040EndAjustar e repetirBMADPROTECT039EndBMADPROTECT038End
</step>

<step n="6" goal="Load Resources">
<action>Carrega {{templates}} e extrair `diagram` secção </action>
<action>Lad BMADPROTECT119End}BMADPROTECT032End
<action>Load BMADPROTECT112End e merge com templateBMADPROTECT030End
<action>Carrega {{helpers}} para diretrizes </action>
</step>

<step n="7" goal="Build Diagram Elements">
<critical>Siga {{helpers}} para criação de elementos adequados</critical>

<substep> Para cada componente:
- Gerar IDs únicos (componente-id, texto-id, grupo-id)
- Criar forma com groupIds
- Calcular a largura do texto
- Criar texto com contêinerId e correspondente groupIds
- Adicionar elementos
</substep>

<substep> Para cada conexão:
- Determinar o tipo de seta (direta/cotovelo)
- Criar com startBinding e endBinding
- Actualizar os elementos em ambos os componentes
</substep>

<substep>Build Ordem por Tipo:
      - Architecture: Serviços → Bancos de Dados → Ligações → Etiquetas
      - ERD: Entidades → Atributos → Relações → Cardinalidade
- UML Classe: Classes → Atributos → Métodos → Relações
- Sequência UML: Atores → Lifelines → Mensagens → Returns
- Caso de uso UML: Atores → Casos de uso → Relacionamentos
</substep>

    <substep>Alignment:
- Ligar para 20px grid
      - Space: 40px entre componentes, 60px entre secções
</substep>
</step>

<step n="8" goal="Optimize and Save">
<action>Strip elementos e elementos não utilizados com isExcluídos: true</action>
BMADPROTECT011EndSave to BMADPROTECT116End}BMADPROTECT010End
</step>

<step n="9" goal="Validate JSON Syntax">
<critical>NEVER apagar o arquivo se a validação falhar - sempre corrigir erros de sintaxe</critical>
    <action>Run: node -e "JSON.parse(require('fs').readFileSync('{{default_output_file}}', 'utf8')); console.log('✓ Valid JSON')"</action>
<check if="validation fails (exit code 1)">
<action> Leia a mensagem de erro cuidadosamente - mostra