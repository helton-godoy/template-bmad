# Instruções de revisão retrospectivas - Epic Completion Review

<critical>O motor de execução do fluxo de trabalho é regido por: {project-root}/\ bmad/core/tasks/workflow.xml</critical>
<critical>Você já deve ter carregado e processado: {project-root}/\ bmad/bmm/workflows/4-implementation/retrospective/workflow.yaml</critical>
<critical>Comunicar todas as respostas em {communication_language} e linguagem DEVE ser adaptado ao {user_skill_level}BADPROTECT087END
<critical>Gere todos os documentos em {document_output_language}BADPROTECT085END
<critical>⚠; ABSOLUTAMENTE NO TEMPO ESTIMATES - NUNCA mencionar horas, dias, semanas, meses, ou quaisquer previsões baseadas no tempo. A IA mudou fundamentalmente a velocidade de desenvolvimento - o que uma vez levou as equipes semanas/meses agora pode ser done por uma pessoa em horas. NÃO dê estimativas de tempo. </critical>

<critical>
DOCUMENTO: Análise retrospectiva. Insights concisos, lições aprendidas, itens de ação. Nível de habilidade do usuário ({user_skill_level}) afeta o estilo de conversação SOMENTE, não conteúdo retrospectivo.

NOTAS DE FABRICO:

- Scrum Master facilita esta retrospectiva
- Segurança psicológica é primordial - NÃO
- Foco em sistemas, processos e aprendizagem
- Todos contribuem com exemplos específicos preferidos
- Os itens de ação devem ser alcançados com uma propriedade clara
- Formato de duas partes: (1) Revisão épica + (2) Preparação épica seguinte

PROTOCOLO DE MODELO DE PARTE:

- TODA a janela do agente DEVE usar o formato: "Nome (Role): dialog"
"Vamos começar..."
- Example: {user_name} (Project Lead): [O utilizador responde]
- Criar back-and-forth natural com o usuário participando ativamente
- Mostrar desentendimentos, perspectivas diversas, dinâmicas de equipe autênticas
</critical>

<workflow>

<step n="1" goal="Epic Discovery - Find Completed Epic with Priority Logic">

<action>Explicar ao BMADPROTECT122End o processo épico de descoberta usando o diálogo natural</action>

<output>
"Bem-vindo à retrospectiva, {user_name}. Deixa-me ajudar-te a identificar qual épico acabámos de completar. Vou verificar o sprint-status primeiro, mas você é a autoridade máxima sobre o que estamos revisando hoje."
</output>

<action>Priority 1: Verifique {sprint_status_file} first</action>

<action>Carregue o arquivo completo: {sprint_status_file}BAMADPROTECT071END
<action>Leia todas as entradas de desenvolvimento status</action>
<action>Encontrar o maior número épico com pelo menos uma história marcada "done"</action>
<action>Extrair número épico de chaves como "epic-X-retrospective" ou teclas de história como "X-Y-story-name"</action>
<action>Set {{detected_epic}} = maior número épico encontrado com histórias completas</action>

<check if="{{detected_epic}} found">
BMADPROTECT061EndPresent finding to user with context</action>

<output>
Bob (Scrum Master): "Com base no {sprint_status_file}, parece que o Epic {{detected_epic}} foi recentemente concluído. É esse o épico que você quer rever hoje, {user_name}?"
</output>

<action>WAIT para {user_name} para confirmar ou corrigir </action>

<check if="{user_name} confirms">
BMADPROTECT054EndSet BMADPROTECT113End} = BMADPROTECT112End}BMADPROTECT053End
</check>

<check if="{user_name} provides different epic number">
<action>Set {{epic_number}} = número fornecido pelo utilizador</action>
<output>
"Entendido, estamos a rever a Epic {{epic_number}}. Deixe-me recolher essa informação."
</output>
</check>
</check>

<check if="{{detected_epic}} NOT found in sprint-status">
<action>Priority 2: Pergunte diretamente ao usuário</action>

<output>
Bob (Scrum Master): "Estou tendo problemas para detectar o épico completo da {sprint_status_file}. {user_name}, que número épico acabaste de completar?"
</output>

<action>WAIT para {user_name} para fornecer número épico</action>
<action>Set {{epic_number}} = número fornecido pelo utilizador</action>
</check>

<check if="{{epic_number}} still not determined">
<action>Priority 3: Regresso à pasta de histórias</action>

<action>Scan {story_directory} para arquivos de histórias numerados mais elevados</action>
<action>Extraia números épicos de nomes de arquivos de histórias (padrão: epic-X-Y-story-name.md)</action>
<action>Set {{detected_epic}} = maior número épico encontrado</action>

<output>
Bob (Scrum Master): "Encontrei histórias para {{detected_epic}} na pasta de histórias. É esse o épico que estamos a rever, {user_name}?"
</output>

<action>WAIT para {user_name} para confirmar ou corrigir </action>
BMADPROTECT021EndSet BMADPROTECT100End} = número confirmado BMADPROTECT020End
</check>

<action> Uma vez determinado o {{epic_number}}, verifique o estado de conclusão épico </action>

<action>Encontrar todas as histórias para o épico {{epic_number}} em {sprint_status_file}:

- Procure por chaves que comecem com "{{epic_number}}" (por exemplo, "1-1-", "1-2-", etc.)
- Excluir a própria chave épica ("epic-{{epic_number}}")
- Excluir a chave retrospectiva ("epic- {{epic_number}}- retrospective")
</action>

<action>Conte as histórias totais encontradas para este épico </action>
<action>Count storys with status = "done"</action>
<action>Colectar a lista de chaves pendentes de história (status != "done")</action>
<action>Determine se completo: BMADPROTECT133End se todas as histórias são done, BMADPROTECT132End caso contrário </action>

<check if="epic is not complete">
