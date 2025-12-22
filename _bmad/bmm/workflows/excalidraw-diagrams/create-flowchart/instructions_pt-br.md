# Criar Fluxograma - Instruções de fluxo de trabalho

```xml
<critical>O motor de execução do fluxo de trabalho é regido por: {project_root}/ bmad/core/tasks/workflow.xml</critical>
<critical>Você já deve ter carregado e processado: {installed_path}/workflow.yaml</critical>
<critical>Este fluxo de trabalho cria uma visualização de fluxograma no formato Excalidraw para processos, pipelines ou fluxos lógicos. </critical>

<workflow>

<step n="0" goal="Contextual Analysis (Smart Elicitation)">
<critical>Antes de fazer quaisquer perguntas, analise o que o usuário já lhe disse</critical>

<action>Reveja o histórico inicial de solicitação e conversação do usuário</action>
<action>Extraia qualquer mencionado: tipo de fluxograma, complexidade, pontos de decisão, local de salvamento</action>

<check if="ALL requirements are clear from context">
<action>Summarize sua compreensão</action>
<action>Skip diretamente para o Passo 4 (Plano de Layout Fluxograma)</action>
</check>

<check if="SOME requirements are clear">
<action>Note o que você já sabe</action>
<action>Apenas pergunte sobre a falta de informações no Passo 1</action>
</check>

<check if="requirements are unclear or minimal">
<action>Proceed with full elicitation in Step 1</action>
</check>
</step>

<step n="1" goal="Gather Requirements" elicit="true">
<action>APergunta 1: "Que tipo de fluxo de processo você precisa visualizar? "</action>
<action>Present numeradas opções:
1. Fluxo de Processo de Negócios - Documentar fluxos de trabalho de negócios, processos de aprovação ou procedimentos operacionais
2. Algoritmo/Flow Lógico - Visualize lógica de código, árvores de decisão ou processos computacionais
3. Fluxo de Viagem do Usuário - Mapear interações do usuário, caminhos de navegação ou fluxos de experiência
4. Processamento de dados Pipeline - Mostrar transformação de dados, processos ETL, ou estágios de processamento
5. Outro - Descreva suas necessidades específicas de fluxograma
</action>
<action>WAIT para seleção de usuários (1-5)</action>

<action>Ask Pergunta 2: "Quantas etapas principais estão neste fluxo? "</action>
<action>Present numeradas opções:
1. Simples (3-5 etapas) - Processo rápido com poucos pontos de decisão
2. Médio (6-10 passos) - fluxo de trabalho padrão com alguma ramificação
3. Complexo (11-20 etapas) - Processo detalhado com múltiplos pontos de decisão
4. Muito complexo (20 + passos) - fluxo de trabalho abrangente que requer layout cuidadoso
</action>
<action>WAIT para seleção de usuários (1-4)</action>
<action>Store selection in {{complexity}}</action>

<action>APergunta 3: "Seu fluxo inclui pontos de decisão (sim/não ramificações)? "</action>
<action>Present numeradas opções:
1. Nenhuma decisão - Fluxo linear do início ao fim
2. Poucas decisões (1-2) - Simples ramificação com caminhos sim/não
3. Várias decisões (3-5) - Vários ramos condicionais
4. Decisões complexas (6+) - Ampla lógica de ramificação
</action>
<action>WAIT para seleção de usuários (1-4)</action>
<action>Store seleção em {{decision_points}}</action>

<action>APergunta 4: "Onde o fluxograma deve ser salvo? "</action>
<action>Present numeradas opções:
1. Localização padrão - docs/flowcharts/[nome gerado automaticamente].excalidraw
2. Caminho personalizado - Especifique seu próprio caminho de arquivo
3. Root do projeto - Salvar no diretório principal do projeto
4. Pasta específica - Escolha entre pastas existentes
</action>
<action>WAIT para seleção de usuários (1-4)</action>
<check if="selection is 2 or 4">
<action>Ask for especific path</action>
<action>WAIT for user input</action>
</check>
BMADPROTECT030Endstore final path in BMADPROTECT098End}BMADPROTECT029End
</step>

<step n="2" goal="Check for Existing Theme" elicit="true">
<action> Verifique se o theme.json existe no local de saída</action>
<check if="theme.json exists">
<action>Ask: "Encontrado tema existente. Usar? (sim/não)"</action>
<action>WAIT for user response</action>
<check if="user says yes">
<action>Carregar e usar o tema existente</action>
<action>Skip to Step 4</action>
</check>
<check if="user says no">
BMADPROTECT012EndProceed to Step 3BMADPROTECT011End
</check>
</check>
<check if="theme.json does not exist">
<action>Proceder ao passo 3</action>
</check>
</step>

<step n="3" goal="Create Theme" elicit="true">
<action>Ask: "Vamos criar um tema para o seu fluxograma. Escolha um esquema de cores:"</action>
<action>Present numeradas opções:
1. Azul Profissional
- Preenchimento primário: #e3f2fd (azul claro)
- Accent/Border: #1976d2 (azul)
         - Decision: #fff3e0 (laranja clara)
         - Text: #1e1e1e (cinzento escuro)

2. Verde Sucesso
- Preenchimento primário: #e8f5e9 (verde claro)
- Accent/Border: #388e3c (verde)
         - Decision: #fff9c4 (amarelo claro)
         - Text: #1e1e1e (cinzento escuro)

3. Cinza Neutro
- Preenchimento primário: #f5f5f5 (cinzento claro)
- Accent/Border: #616161 (cinza)
         - Decision: #e0e0e0 (cinzento médio)
- Texto