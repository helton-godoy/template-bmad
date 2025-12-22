# Criar Diagrama de fluxo de dados - Instruções de fluxo de trabalho

```xml
<critical>O motor de execução de fluxo de trabalho é regido por: {project_root}/ bmad/core/tasks/workflow.xml</critical>
<critical>Você já deve ter carregado e processado: {installed_path}/workflow.yaml</critical>
<critical>Este fluxo de trabalho cria diagramas de fluxo de dados (DFD) no formato Excalidraw. </critical>

<workflow>

<step n="0" goal="Contextual Analysis">
<action>Reveja o pedido e extração do usuário: nível DFD, processos, armazenamento de dados, entidades externas</action>
<check if="ALL requirements clear">BADPROTECT099 ENDSkip to Step 4</action>BADPROTECT097 END
</step>

<step n="1" goal="Identify DFD Level" elicit="true">
<action>Ask: "Que nível de DFD você precisa? " </action>
BMADPROTECT092EndPresent opções:
1. Diagrama de Contexto (Nível 0) - Processo único mostrando limites do sistema
2. Nível 1 DFD - Principais processos e fluxos de dados
3. Nível 2 DFD - sub-processos detalhados
4. Personalizado - Especifique seus requisitos
</action>
<action>WAIT for selection</action>
</step>

<step n="2" goal="Gather Requirements" elicit="true">
<action>Ask: "Descreva os processos, armazenamentos de dados e entidades externas em seu sistema"</action>
<action>WAIT para descrição do usuário</action>
<action>Sumarizar o que será incluído e confirmar com o usuário</action>
</step>

<step n="3" goal="Theme Setup" elicit="true">
<action>Verifique se existe theme.json existente, peça para usar se existe </action>
<check if="no existing theme">
<action>Ask: "Escolha um esquema de cores DFD:"</action>
<action>Present numeradas opções:
1. DFD padrão
           - Process: #e3f2fd (azul claro)
- Data Store: #e8f5e9 (verde claro)
- Entidade Externa: #f3e5f5 (púrpura)
           - Border: #1976d2 (azul)

2. DFD colorido
           - Process: #fff9c4 (amarelo claro)
- Loja de dados: #c5e1a5 (limão leve)
- Entidade Externa: #ffccbc (corais leves)
           - Border: #f57c00 (laranja)

3. DFD mínima
           - Process: #f5f5f5 (cinzento claro)
- Data Store: #eeeeee (cinzento)
- Entidade Externa: #e0e0e0 (cinzento médio)
           - Border: #616161 (cinzento escuro)

4. Personalizado - Defina suas próprias cores
</action>
<action>WAIT for selection</action>
<action>Create theme.json baseado na seleção</action>
</check>
</step>

<step n="4" goal="Plan DFD Structure">
<action>Lista todos os processos com números (1.0, 2.0, etc.)</action>
<action>List all data stores (D1, D2, etc.)</action>
BMADPROTECT060EndLista de todas as entidades externasBMADPROTECT059End
<action>Map todos os fluxos de dados com etiquetas</action>
<action>Mostrar estrutura BMADPROTECT000End, confirmar com o usuário </action>
</step>

<step n="5" goal="Load Resources">
<action>{{templates}} e extrair `dataflow` secção </action>
<action>BMADPROTECT117End}BMADPROTECT049End
<action>Lad theme.json</action>
BMADPROTECT046EndLad BMADPROTECT116end}BMADPROTECT045End
</step>

<step n="6" goal="Build DFD Elements">
<critical>Siga a notação padrão DFD de {{helpers}}</critical>

<substep>Build Order:
1. Entidades externas (retângulos, fronteira em negrito)
2. Processos (círculos/ellipses com números)
3. Armazenamento de dados (linhas paralelas ou retângulos)
4. Fluxos de dados (setas marcadas)
</substep>

<substep>DFD Regras:
      - Processes: Numerado (1.0, 2.0), frases verbais
- Armazenamento de dados: Nome (D1, D2), frases de substantivo
- Entidades externas: Frases nomeadas, substantivos
- Fluxos de dados: Marcado com nomes de dados, setas mostram direção
- Nenhum fluxo direto entre entidades externas
- Não há fluxo directo entre as lojas de dados
</substep>

    <substep>Layout:
- Entidades externas nas bordas
- Processos no centro
- Armazenamento de dados entre processos
- Minimizar fluxos de cruzamento
- Fluxo da esquerda para a direita ou de cima para baixo
</substep>
</step>

<step n="7" goal="Optimize and Save">
<action>Verify DFD regulations compliance</action>
<action>Strip elementos não utilizados e elementos com isExcluídos: true</action>
BMADPROTECT028EndSave to BMADPROTECT114End}BMADPROTECT027End
</step>

<step n="8" goal="Validate JSON Syntax">
<critical>NEVER excluir o arquivo se a validação falhar - sempre corrigir erros de sintaxe</critical>
    <action>Run: node -e "JSON.parse(require('fs').readFileSync('{{default_output_file}}', 'utf8')); console.log('✓ Valid JSON')"</action>
<check if="validation fails (exit code 1)">
<action>Leia cuidadosamente a mensagem de erro - mostra o erro de sintaxe e a posição</action>
<action>Abra o arquivo e navegue para o local de erro</action>
<action> Corrigir o erro de sintaxe (adicionar vírgula, parêntese, ou citação como indicado)</action>
<action>Salve o arquivo</action>
validação <action>Re-run com o mesmo comando</action>
<action>Repetir até que passes de validação</action>
</check>
<action>Uma vez aprovada a validação, confirme com user</action>
</step>

<step n="9" goal="Validate Content">
<invoke-task>Validate