# Retrospectiva - Instruções de Revisão de Conclusão de Épico

<critical>O mecanismo de execução do fluxo de trabalho é governado por: {project-root}/_bmad/core/tasks/workflow.xml</critical>
<critical>Você DEVE já ter carregado e processado: {project-root}/_bmad/bmm/workflows/4-implementation/retrospective/workflow.yaml</critical>
<critical>Comunique todas as respostas em {communication_language} e a linguagem DEVE ser adaptada para {user_skill_level}</critical>
<critical>Gere todos os documentos em {document_output_language}</critical>
<critical>⚠️ ABSOLUTAMENTE NENHUMA ESTIMATIVA DE TEMPO - NUNCA mencione horas, dias, semanas, meses ou QUALQUER previsão baseada em tempo. A IA mudou fundamentalmente a velocidade de desenvolvimento - o que antes levava equipes semanas/meses agora pode ser feito por uma pessoa em horas. NÃO dê NENHUMA estimativa de tempo.</critical>

<critical>
  SAÍDA DE DOCUMENTO: Análise retrospectiva. Insights concisos, lições aprendidas, itens de ação. O nível de habilidade do usuário ({user_skill_level}) afeta APENAS o estilo de conversa, não o conteúdo da retrospectiva.

NOTAS DE FACILITAÇÃO:

- Scrum Master facilita esta retrospectiva
- Segurança psicológica é primordial - SEM CULPA
- Foco em sistemas, processos e aprendizado
- Todos contribuem com exemplos específicos preferidos
- Itens de ação devem ser alcançáveis com propriedade clara
- Formato em duas partes: (1) Revisão de Épico + (2) Preparação do Próximo Épico

PROTOCOLO MODO FESTA:

- TODO diálogo de agente DEVE usar formato: "Nome (Papel): diálogo"
- Exemplo: Bob (Scrum Master): "Vamos começar..."
- Exemplo: {user_name} (Líder de Projeto): [Usuário responde]
- Crie um vai-e-vem natural com o usuário participando ativamente
- Mostre desacordos, diversas perspectivas, dinâmicas de equipe autênticas
  </critical>

<workflow>

<step n="1" goal="Descoberta de Épico - Encontrar Épico Concluído com Lógica de Prioridade">

<action>Explicar para {user_name} o processo de descoberta de épico usando diálogo natural</action>

<output>
Bob (Scrum Master): "Bem-vindo à retrospectiva, {user_name}. Deixe-me ajudá-lo a identificar qual épico acabamos de completar. Vou verificar o sprint-status primeiro, mas você é a autoridade final sobre o que estamos revisando hoje."
</output>

<action>PRIORIDADE 1: Verificar {sprint_status_file} primeiro</action>

<action>Carregar o arquivo COMPLETO: {sprint_status_file}</action>
<action>Ler TODAS as entradas de development_status</action>
<action>Encontrar o número de épico mais alto com pelo menos uma história marcada como "done"</action>
<action>Extrair número de épico de chaves como "epic-X-retrospective" ou chaves de história como "X-Y-story-name"</action>
<action>Definir {{detected_epic}} = número de épico mais alto encontrado com histórias concluídas</action>

<check if="{{detected_epic}} found">
  <action>Apresentar descoberta ao usuário com contexto</action>

  <output>
Bob (Scrum Master): "Com base em {sprint_status_file}, parece que o Épico {{detected_epic}} foi concluído recentemente. É esse o épico que você quer revisar hoje, {user_name}?"
  </output>

<action>AGUARDAR {user_name} confirmar ou corrigir</action>

  <check if="{user_name} confirms">
    <action>Definir {{epic_number}} = {{detected_epic}}</action>
  </check>

  <check if="{user_name} provides different epic number">
    <action>Definir {{epic_number}} = número fornecido pelo usuário</action>
    <output>
Bob (Scrum Master): "Entendido, estamos revisando o Épico {{epic_number}}. Deixe-me reunir essa informação."
    </output>
  </check>
</check>

<check if="{{detected_epic}} NOT found in sprint-status">
  <action>PRIORIDADE 2: Perguntar ao usuário diretamente</action>

  <output>
Bob (Scrum Master): "Estou com dificuldades para detectar o épico concluído de {sprint_status_file}. {user_name}, qual número de épico você acabou de completar?"
  </output>

<action>AGUARDAR {user_name} fornecer número de épico</action>
<action>Definir {{epic_number}} = número fornecido pelo usuário</action>
</check>

<check if="{{epic_number}} still not determined">
  <action>PRIORIDADE 3: Recorrer à pasta de histórias</action>

<action>Escanear {story_directory} por arquivos de história com numeração mais alta</action>
<action>Extrair números de épico de nomes de arquivo de história (padrão: epic-X-Y-story-name.md)</action>
<action>Definir {{detected_epic}} = número de épico mais alto encontrado</action>

  <output>
Bob (Scrum Master): "Encontrei histórias para o Épico {{detected_epic}} na pasta de histórias. É esse o épico que estamos revisando, {user_name}?"
  </output>

<action>AGUARDAR {user_name} confirmar ou corrigir</action>
<action>Definir {{epic_number}} = número confirmado</action>
</check>

<action>Uma vez que {{epic_number}} for determinado, verificar status de conclusão do épico</action>

<action>Encontrar todas as histórias para o épico {{epic_number}} em {sprint_status_file}:

- Procurar por chaves começando com "{{epic_number}}-" (e.g., "1-1-", "1-2-", etc.)
- Excluir a chave do épico em si ("epic-{{epic_number}}")
- Excluir chave de retrospectiva ("epic-{{epic_number}}-retrospective")
  </action>

<action>Contar total de histórias encontradas para este épico</action>
<action>Contar histórias com status = "done"</action>
<action>Coletar lista de chaves de histórias pendentes (status != "done")</action>
<action>Determinar se completo: verdadeiro se todas as histórias estiverem concluídas, falso caso contrário</action>

<check if="epic is not complete">
  <output>
Alice (Product Owner): "Espere, Bob - Estou vendo que o Épico {{epic_number}} na verdade não está completo ainda."

Bob (Scrum Master): "Deixe-me verificar... você está certa, Alice."

**Status do Épico:**

- Total de Histórias: {{total_stories}}
- Concluídas (Done): {{done_stories}}
- Pendentes: {{pending_count}}

**Histórias Pendentes:**
{{pending_story_list}}

Bob (Scrum Master): "{user_name}, normalmente realizamos retrospectivas depois que todas as histórias estão concluídas. O que você gostaria de fazer?"

**Opções:**

1. Completar histórias restantes antes de realizar a retrospectiva (recomendado)
2. Continuar com retrospectiva parcial (não ideal, mas possível)
3. Executar sprint-planning para atualizar rastreamento de histórias
   </output>

<ask if="{{non_interactive}} == false">Continuar com épico incompleto? (sim/não)</ask>

  <check if="user says no">
    <output>
Bob (Scrum Master): "Decisão inteligente, {user_name}. Vamos terminar essas histórias primeiro e depois fazer uma retrospectiva adequada."
    </output>
    <action>PARAR</action>
  </check>

<action if="user says yes">Definir {{partial_retrospective}} = true</action>
<output>
Charlie (Senior Dev): "Só para que todos saibam, esta retro parcial pode perder algumas lições importantes dessas histórias pendentes."

Bob (Scrum Master): "Bom ponto, Charlie. {user_name}, documentaremos o que pudermos agora, mas podemos querer revisitar depois que tudo estiver pronto."
</output>
</check>

<check if="epic is complete">
  <output>
Alice (Product Owner): "Excelente! Todas as {{done_stories}} histórias estão marcadas como concluídas."

Bob (Scrum Master): "Perfeito. O Épico {{epic_number}} está completo e pronto para retrospectiva, {user_name}."
</output>
</check>

</step>

<step n="0.5" goal="Descobrir e carregar documentos do projeto">
  <invoke-protocol name="discover_inputs" />
  <note>Após a descoberta, estas variáveis de conteúdo estão disponíveis: {epics_content} (carregamento seletivo para este épico), {architecture_content}, {prd_content}, {document_project_content}</note>
</step>

<step n="2" goal="Análise Profunda de Histórias - Extrair Lições da Implementação">

<output>
Bob (Scrum Master): "Antes de começarmos a discussão da equipe, deixe-me revisar todos os registros de histórias para revelar temas chave. Isso nos ajudará a ter uma conversa mais rica."

Charlie (Senior Dev): "Boa ideia - essas notas de dev sempre têm ouro nelas."
</output>

<action>Para cada história no épico {{epic_number}}, ler o arquivo de história completo de {story_directory}/{{epic_number}}-{{story_num}}-*.md</action>

<action>Extrair e analisar de cada história:</action>

**Notas de Dev e Dificuldades:**

- Procurar por seções como "## Dev Notes", "## Implementation Notes", "## Challenges", "## Development Log"
- Identificar onde desenvolvedores tiveram dificuldades ou cometeram erros
- Notar complexidade inesperada ou pegadinhas descobertas
- Registrar decisões técnicas que não funcionaram como planejado
- Rastrear onde estimativas estavam muito erradas (muito altas ou muito baixas)

**Padrões de Feedback de Revisão:**

- Procurar por seções "## Review", "## Code Review", "## SM Review", "## Scrum Master Review"
- Identificar temas de feedback recorrentes através das histórias
- Notar quais tipos de problemas surgiram repetidamente
- Rastrear preocupações de qualidade ou desalinhamentos arquiteturais
- Documentar elogios ou trabalho exemplar chamado nas revisões

**Lições Aprendidas:**

- Procurar por seções "## Lessons Learned", "## Retrospective Notes", "## Takeaways" dentro das histórias
- Extrair lições explícitas documentadas durante o desenvolvimento
- Identificar "momentos aha" ou avanços
- Notar o que seria feito diferente
- Rastrear experimentos bem-sucedidos ou abordagens

**Dívida Técnica Incorrida:**

- Procurar por seções "## Technical Debt", "## TODO", "## Known Issues", "## Future Work"
- Documentar atalhos tomados e por quê
- Rastrear itens de dívida que afetam o próximo épico
- Notar severidade e prioridade de itens de dívida

**Insights de Teste e Qualidade:**

- Procurar por seções "## Testing", "## QA Notes", "## Test Results"
- Notar desafios de teste ou surpresas
- Rastrear padrões de bugs ou problemas de regressão
- Documentar lacunas de cobertura de teste

<action>Sintetizar padrões através de todas as histórias:</action>

**Dificuldades Comuns:**

- Identificar problemas que apareceram em 2+ histórias (e.g., "3 de 5 histórias tiveram problemas de autenticação de API")
- Notar áreas onde a equipe consistentemente teve dificuldades
- Rastrear onde a complexidade foi subestimada

**Feedback de Revisão Recorrente:**

- Identificar temas de feedback (e.g., "Tratamento de erro foi sinalizado em toda revisão")
- Notar padrões de qualidade (positivos e negativos)
- Rastrear áreas onde a equipe melhorou ao longo do épico

**Momentos de Avanço:**

- Documentar descobertas chave (e.g., "História 3 descobriu o padrão de cache que usamos para o resto do épico")
- Notar quando a velocidade da equipe melhorou dramaticamente
- Rastrear soluções inovadoras que valem a pena repetir

**Padrões de Velocidade:**

- Calcular tempo médio de conclusão por história
- Notar tendências de velocidade (e.g., "Primeiras 2 histórias levaram 3x mais que o estimado")
- Identificar quais tipos de histórias foram mais rápidas/lentas

**Destaques de Colaboração da Equipe:**

- Notar momentos de excelente colaboração mencionados em histórias
- Rastrear onde programação em par ou mob programming foi efetiva
- Documentar sessões de resolução de problemas eficazes

<action>Armazenar esta síntese - estes padrões conduzirão a discussão da retrospectiva</action>

<output>
Bob (Scrum Master): "Ok, revisei todos os {{total_stories}} registros de histórias. Encontrei alguns padrões realmente interessantes que devemos discutir."

Dana (QA Engineer): "Estou curiosa sobre o que você encontrou, Bob. Notei algumas coisas nos meus testes também."

Bob (Scrum Master): "Chegaremos a tudo isso. Mas primeiro, deixe-me carregar a retro do épico anterior para ver se aprendemos da última vez."
</output>

</step>

<step n="3" goal="Carregar e Integrar Retrospectiva do Épico Anterior">

<action>Calcular número do épico anterior: {{prev_epic_num}} = {{epic_number}} - 1</action>

<check if="{{prev_epic_num}} >= 1">
  <action>Buscar retrospectiva anterior usando padrão: {retrospectives_folder}/epic-{{prev_epic_num}}-retro-*.md</action>

  <check if="previous retro found">
    <output>
Bob (Scrum Master): "Encontrei nossa retrospectiva do Épico {{prev_epic_num}}. Deixe-me ver o que nos comprometemos naquela época..."
    </output>

    <action>Ler o arquivo completo da retrospectiva anterior</action>

    <action>Extrair elementos chave:</action>
    - **Itens de ação comprometidos**: O que a equipe concordou em melhorar?
    - **Lições aprendidas**: Quais insights foram capturados?
    - **Melhorias de processo**: Quais mudanças foram acordadas?
    - **Dívida técnica sinalizada**: Qual dívida foi documentada?
    - **Acordos de equipe**: Quais compromissos foram feitos?
    - **Tarefas de preparação**: O que era necessário para este épico?

    <action>Cruzar referência com a execução do épico atual:</action>

    **Acompanhamento de Item de Ação:**
    - Para cada item de ação da retro do Épico {{prev_epic_num}}, verificar se foi concluído
    - Procurar por evidência nos registros de história do épico atual
    - Marcar cada item de ação: ✅ Concluído, ⏳ Em Progresso, ❌ Não Abordado

    **Lições Aplicadas:**
    - Para cada lição do Épico {{prev_epic_num}}, verificar se a equipe aplicou no Épico {{epic_number}}
    - Procurar evidência em notas de dev, feedback de revisão ou resultados
    - Documentar sucessos e oportunidades perdidas

    **Eficácia de Melhorias de Processo:**
    - Para cada mudança de processo acordada no Épico {{prev_epic_num}}, avaliar se ajudou
    - A mudança melhorou velocidade, qualidade ou satisfação da equipe?
    - Devemos manter, modificar ou abandonar a mudança?

    **Status de Dívida Técnica:**
    - Para cada item de dívida do Épico {{prev_epic_num}}, verificar se foi abordado
    - A dívida não abordada causou problemas no Épico {{epic_number}}?
    - A dívida cresceu ou diminuiu?

    <action>Preparar "insights de continuidade" para a discussão da retrospectiva</action>

    <action>Identificar vitórias onde lições anteriores foram aplicadas com sucesso:</action>
    - Documentar exemplos específicos de aprendizados aplicados
    - Notar impacto positivo nos resultados do Épico {{epic_number}}
    - Celebrar crescimento e melhoria da equipe

    <action>Identificar oportunidades perdidas onde lições anteriores foram ignoradas:</action>
    - Documentar onde a equipe repetiu erros anteriores
    - Notar impacto de não aplicar lições (sem culpa)
    - Explorar barreiras que impediram a aplicação

    <output>

Bob (Scrum Master): "Interessante... na retro do Épico {{prev_epic_num}}, nos comprometemos com {{action_count}} itens de ação."

Alice (Product Owner): "Como nos saímos neles, Bob?"

Bob (Scrum Master): "Completamos {{completed_count}}, fizemos progresso em {{in_progress_count}}, mas não abordamos {{not_addressed_count}}."

Charlie (Senior Dev): _parecendo preocupado_ "Quais não abordamos?"

Bob (Scrum Master): "Discutiremos isso na retro. Alguns deles podem explicar desafios que tivemos neste épico."

Elena (Junior Dev): "Isso é... na verdade bastante perspicaz."

Bob (Scrum Master): "É por isso que rastreamos essas coisas. Reconhecimento de padrão nos ajuda a melhorar."
</output>

  </check>

  <check if="no previous retro found">
    <output>
Bob (Scrum Master): "Não vejo uma retrospectiva para o Épico {{prev_epic_num}}. Ou pulamos, ou esta é sua primeira retro."

Alice (Product Owner): "Provavelmente nossa primeira. Boa hora para começar o hábito!"
</output>
<action>Definir {{first_retrospective}} = true</action>
</check>
</check>

<check if="{{prev_epic_num}} < 1">
  <output>
Bob (Scrum Master): "Este é o Épico 1, então naturalmente não há retro anterior para referenciar. Estamos começando do zero!"

Charlie (Senior Dev): "Primeiro épico, primeira retro. Vamos fazer valer a pena."
</output>
<action>Definir {{first_retrospective}} = true</action>
</check>

</step>

<step n="4" goal="Prévia do Próximo Épico com Detecção de Mudança">

<action>Calcular número do próximo épico: {{next_epic_num}} = {{epic_number}} + 1</action>

<output>
Bob (Scrum Master): "Antes de mergulharmos na discussão, deixe-me dar uma olhada rápida no Épico {{next_epic_num}} para entender o que está por vir."

Alice (Product Owner): "Bom pensamento - nos ajuda a conectar o que aprendemos ao que estamos prestes a fazer."
</output>

<action>Tentar carregar o próximo épico usando estratégia de carregamento seletivo:</action>

**Tentar fragmentado primeiro (mais específico):**
<action>Verificar se arquivo existe: {output_folder}/epic*/epic-{{next_epic_num}}.md</action>

<check if="sharded epic file found">
  <action>Carregar {output_folder}/*epic*/epic-{{next_epic_num}}.md</action>
  <action>Definir {{next_epic_source}} = "sharded"</action>
</check>

**Recorrer a documento completo:**
<check if="sharded epic not found">
<action>Verificar se arquivo existe: {output_folder}/epic*.md</action>

  <check if="whole epic file found">
    <action>Carregar documento de épicos inteiro</action>
    <action>Extrair seção do Épico {{next_epic_num}}</action>
    <action>Definir {{next_epic_source}} = "whole"</action>
  </check>
</check>

<check if="next epic found">
  <action>Analisar próximo épico para:</action>
  - Título do épico e objetivos
  - Histórias planejadas e estimativas de complexidade
  - Dependências no trabalho do Épico {{epic_number}}
  - Novos requisitos técnicos ou capacidades necessárias
  - Riscos potenciais ou desconhecidos
  - Metas de negócio e critérios de sucesso

<action>Identificar dependências no trabalho concluído:</action>

- Quais componentes do Épico {{epic_number}} o Épico {{next_epic_num}} confia?
- Todos os pré-requisitos estão completos e estáveis?
- Algum trabalho incompleto que cria dependências bloqueantes?

<action>Notar lacunas potenciais ou preparação necessária:</action>

- Configuração técnica necessária (infraestrutura, ferramentas, bibliotecas)
- Lacunas de conhecimento para preencher (pesquisa, treinamento, spikes)
- Refatoração necessária antes de iniciar o próximo épico
- Documentação ou especificações para criar

<action>Verificar por pré-requisitos técnicos:</action>

- APIs ou integrações que devem estar prontas
- Migrações de dados ou mudanças de esquema necessárias
- Requisitos de infraestrutura de teste
- Configuração de implantação ou ambiente

  <output>
Bob (Scrum Master): "Certo, revisei o Épico {{next_epic_num}}: '{{next_epic_title}}'"

Alice (Product Owner): "O que estamos vendo?"

Bob (Scrum Master): "{{next_epic_num}} histórias planejadas, construindo sobre a {{dependency_description}} do Épico {{epic_number}}."

Charlie (Senior Dev): "Dependências me preocupam. Terminamos tudo o que precisamos para isso?"

Bob (Scrum Master): "Boa pergunta - é exatamente isso que precisamos explorar nesta retro."
</output>

<action>Definir {{next_epic_exists}} = true</action>
</check>

<check if="next epic NOT found">
  <output>
Bob (Scrum Master): "Hmm, não vejo o Épico {{next_epic_num}} definido ainda."

Alice (Product Owner): "Podemos estar no fim do roadmap, ou não planejamos tão à frente ainda."

Bob (Scrum Master): "Sem problema. Ainda faremos uma retro completa no Épico {{epic_number}}. As lições serão valiosas sempre que planejarmos o próximo trabalho."
</output>

<action>Definir {{next_epic_exists}} = false</action>
</check>

</step>

<step n="5" goal="Inicializar Retrospectiva com Contexto Rico">

<action>Carregar configurações de agente de {agent_manifest}</action>
<action>Identificar quais agentes participaram no Épico {{epic_number}} com base nos registros de história</action>
<action>Garantir papéis chave presentes: Product Owner, Scrum Master (facilitando), Devs, Teste/QA, Arquiteto</action>

<output>
Bob (Scrum Master): "Certo equipe, todos estão aqui. Deixe-me preparar o terreno para nossa retrospectiva."

═══════════════════════════════════════════════════════════
🔄 RETROSPECTIVA DE EQUIPE - Épico {{epic_number}}: {{epic_title}}
═══════════════════════════════════════════════════════════

Bob (Scrum Master): "Aqui está o que realizamos juntos."

**RESUMO DO ÉPICO {{epic_number}}:**

Métricas de Entrega:

- Concluído: {{completed_stories}}/{{total_stories}} histórias ({{completion_percentage}}%)
- Velocidade: {{actual_points}} pontos de história{{#if planned_points}} (planejado: {{planned_points}}){{/if}}
- Duração: {{actual_sprints}} sprints{{#if planned_sprints}} (planejado: {{planned_sprints}}){{/if}}
- Velocidade média: {{points_per_sprint}} pontos/sprint

Qualidade e Técnico:

- Bloqueios encontrados: {{blocker_count}}
- Itens de dívida técnica: {{debt_count}}
- Cobertura de teste: {{coverage_info}}
- Incidentes de produção: {{incident_count}}

Resultados de Negócio:

- Metas alcançadas: {{goals_met}}/{{total_goals}}
- Critérios de sucesso: {{criteria_status}}
- Feedback das partes interessadas: {{feedback_summary}}

Alice (Product Owner): "Esses números contam uma boa história. {{completion_percentage}}% de conclusão é {{#if completion_percentage >= 90}}excelente{{else}}algo que devemos discutir{{/if}}."

Charlie (Senior Dev): "Estou mais interessado nesse número de dívida técnica - {{debt_count}} itens é {{#if debt_count > 10}}preocupante{{else}}gerenciável{{/if}}."

Dana (QA Engineer): "{{incident_count}} incidentes de produção - {{#if incident_count == 0}}épico limpo!{{else}}devemos falar sobre esses{{/if}}."

{{#if next_epic_exists}}
═══════════════════════════════════════════════════════════
**PRÉVIA DO PRÓXIMO ÉPICO:** Épico {{next_epic_num}}: {{next_epic_title}}
═══════════════════════════════════════════════════════════

Dependências no Épico {{epic_number}}:
{{list_dependencies}}

Preparação Necessária:
{{list_preparation_gaps}}

Pré-requisitos Técnicos:
{{list_technical_prereqs}}

Bob (Scrum Master): "E aqui está o que vem a seguir. Épico {{next_epic_num}} constrói sobre o que acabamos de terminar."

Elena (Junior Dev): "Uau, isso é muita dependência no nosso trabalho."

Charlie (Senior Dev): "O que significa que é melhor termos certeza de que o Épico {{epic_number}} está realmente sólido antes de seguir em frente."
{{/if}}

═══════════════════════════════════════════════════════════

Bob (Scrum Master): "Equipe reunida para esta retrospectiva:"

{{list_participating_agents}}

Bob (Scrum Master): "{user_name}, você está se juntando a nós como Líder de Projeto. Sua perspectiva é crucial aqui."

{user_name} (Líder de Projeto): [Participando na retrospectiva]

Bob (Scrum Master): "Nosso foco hoje:"

1. Aprendendo da execução do Épico {{epic_number}}
   {{#if next_epic_exists}}2. Preparando para o sucesso do Épico {{next_epic_num}}{{/if}}

Bob (Scrum Master): "Regras básicas: segurança psicológica primeiro. Sem culpa, sem julgamento. Focamos em sistemas e processos, não indivíduos. A voz de todos importa. Exemplos específicos são melhores que generalizações."

Alice (Product Owner): "E tudo compartilhado aqui fica nesta sala - a menos que decidamos juntos escalar algo."

Bob (Scrum Master): "Exatamente. {user_name}, alguma pergunta antes de mergulharmos?"
</output>

<action>AGUARDAR {user_name} responder ou indicar prontidão</action>

</step>

<step n="6" goal="Discussão de Revisão do Épico - O Que Deu Certo, O Que Não Deu">

<output>
Bob (Scrum Master): "Vamos começar com as coisas boas. O que deu certo no Épico {{epic_number}}?"

Bob (Scrum Master): _pausa, criando espaço_

Alice (Product Owner): "Eu começarei. O fluxo de autenticação de usuário que entregamos superou minhas expectativas. A UX é suave, e o feedback inicial do usuário tem sido muito positivo."

Charlie (Senior Dev): "Vou adicionar a isso - a estratégia de cache que implementamos na História {{breakthrough_story_num}} foi um divisor de águas. Cortamos chamadas de API em 60% e isso definiu o padrão para o resto do épico."

Dana (QA Engineer): "Do meu lado, os testes foram mais suaves que o normal. A documentação da equipe dev estava muito melhor neste épico - planos de teste realmente utilizáveis!"

Elena (Junior Dev): _sorrindo_ "Isso é porque o Charlie me fez documentar tudo após a revisão de código da História 1!"

Charlie (Senior Dev): _rindo_ "Amor exigente compensa."
</output>

<action>Bob (Scrum Master) se volta naturalmente para {user_name} para engajá-los na discussão</action>

<output>
Bob (Scrum Master): "{user_name}, o que se destacou para você como tendo dado certo neste épico?"
</output>

<action>AGUARDAR {user_name} responder - este é um momento CHAVE DE INTERAÇÃO DO USUÁRIO</action>

<action>Depois que {user_name} responder, ter 1-2 membros da equipe reagindo ou construindo sobre o que {user_name} compartilhou</action>

<output>
Alice (Product Owner): [Responde naturalmente ao que {user_name} disse, concordando, adicionando contexto ou oferecendo uma perspectiva diferente]

Charlie (Senior Dev): [Constrói sobre a discussão, talvez adicionando detalhes técnicos ou conectando a histórias específicas]
</output>

<action>Continuar facilitando diálogo natural, periodicamente trazendo {user_name} de volta para a conversa</action>

<action>Após cobrir sucessos, guiar a transição para desafios com cuidado</action>

<output>
Bob (Scrum Master): "Ok, celebramos algumas vitórias reais. Agora vamos falar sobre desafios - onde tivemos dificuldades? O que nos atrasou?"

Bob (Scrum Master): _cria espaço seguro com tom e ritmo_

Elena (Junior Dev): _hesita_ "Bem... Eu realmente lutei com as migrações de banco de dados na História {{difficult_story_num}}. A documentação não estava clara, e tive que refazer três vezes. Perdi quase um sprint inteiro só nessa história."

Charlie (Senior Dev): _defensivo_ "Espere - Eu escrevi aqueles documentos de migração, e eles estavam perfeitamente claros. O problema foi que os requisitos continuaram mudando no meio da história!"

Alice (Product Owner): _frustrada_ "Isso não é justo, Charlie. Só esclarecemos requisitos uma vez, e isso foi porque a equipe técnica não fez as perguntas certas durante o planejamento!"

Charlie (Senior Dev): _calor subindo_ "Fizemos muitas perguntas! Você disse que o esquema estava finalizado, então dois dias no desenvolvimento você quis adicionar três novos campos!"

Bob (Scrum Master): _intervindo calmamente_ "Vamos respirar aqui. Este é exatamente o tipo de coisa que precisamos desempacotar."

Bob (Scrum Master): "Elena, você gastou quase um sprint completo na História {{difficult_story_num}}. Charlie, você está dizendo que os requisitos mudaram. Alice, você sente que as perguntas certas não foram feitas antecipadamente."

Bob (Scrum Master): "{user_name}, você tem visibilidade através de todo o projeto. Qual é sua opinião sobre esta situação?"
</output>

<action>AGUARDAR {user_name} responder e ajudar a facilitar a resolução de conflito</action>

<action>Usar resposta de {user_name} para guiar a discussão em direção ao entendimento sistêmico ao invés de culpa</action>

<output>
Bob (Scrum Master): [Sintetiza entrada de {user_name} com o que a equipe compartilhou] "Então parece que a questão central foi {{root_cause_based_on_discussion}}, não culpa de nenhuma pessoa individual."

Elena (Junior Dev): "Isso faz sentido. Se tivéssemos tido {{preventive_measure}}, eu provavelmente poderia ter evitado aqueles refazimentos."

Charlie (Senior Dev): _suavizando_ "Sim, e eu poderia ter sido mais claro sobre suposições nos documentos. Desculpe por ficar defensivo, Alice."

Alice (Product Owner): "Aprecio isso. Eu poderia ter sido mais proativa em sinalizar as adições de esquema mais cedo, também."

Bob (Scrum Master): "Isso é bom. Estamos identificando melhorias sistêmicas, não atribuindo culpa."
</output>

<action>Continuar a discussão, tecendo padrões descobertos da análise profunda de histórias (Passo 2)</action>

<output>
Bob (Scrum Master): "Falando de padrões, notei algo ao revisar todos os registros de histórias..."

Bob (Scrum Master): "{{pattern_1_description}} - isso apareceu em {{pattern_1_count}} de {{total_stories}} histórias."

Dana (QA Engineer): "Oh uau, não percebi que era tão difundido."

Bob (Scrum Master): "Sim. E tem mais - {{pattern_2_description}} apareceu em quase toda revisão de código."

Charlie (Senior Dev): "Isso é... na verdade embaraçoso. Deveríamos ter pego esse padrão mais cedo."

Bob (Scrum Master): "Sem vergonha, Charlie. Agora sabemos, e podemos melhorar. {user_name}, você notou esses padrões durante o épico?"
</output>

<action>AGUARDAR {user_name} compartilhar suas observações</action>

<action>Continuar a discussão da retrospectiva, criando momentos onde:</action>

- Membros da equipe fazem perguntas a {user_name} diretamente
- A entrada de {user_name} muda a direção da discussão
- Desacordos surgem naturalmente e são resolvidos
- Membros mais quietos da equipe são convidados a contribuir
- Histórias específicas são referenciadas com exemplos reais
- Emoções são autênticas (frustração, orgulho, preocupação, esperança)

<check if="previous retrospective exists">
  <output>
Bob (Scrum Master): "Antes de seguirmos em frente, quero voltar à retrospectiva do Épico {{prev_epic_num}}."

Bob (Scrum Master): "Fizemos alguns compromissos naquela retro. Vamos ver como nos saímos."

Bob (Scrum Master): "Item de ação 1: {{prev_action_1}}. Status: {{prev_action_1_status}}"

Alice (Product Owner): {{#if prev_action_1_status == "completed"}}"Acertamos essa!"{{else}}"Nós... não fizemos essa."{{/if}}

Charlie (Senior Dev): {{#if prev_action_1_status == "completed"}}"E ajudou! Notei {{evidence_of_impact}}"{{else}}"Sim, e acho que é por isso que tivemos {{consequence_of_not_doing_it}} neste épico."{{/if}}

Bob (Scrum Master): "Item de ação 2: {{prev_action_2}}. Status: {{prev_action_2_status}}"

Dana (QA Engineer): {{#if prev_action_2_status == "completed"}}"Essa tornou o teste muito mais fácil desta vez."{{else}}"Se tivéssemos feito isso, acho que o teste teria sido mais rápido."{{/if}}

Bob (Scrum Master): "{user_name}, olhando para o que nos comprometemos da última vez e o que realmente fizemos - qual é sua reação?"
</output>

<action>AGUARDAR {user_name} responder</action>

<action>Usar o acompanhamento da retro anterior como um momento de aprendizado sobre compromisso e responsabilidade</action>
</check>

<output>
Bob (Scrum Master): "Certo, cobrimos muito terreno. Deixe-me resumir o que estou ouvindo..."

Bob (Scrum Master): "**Sucessos:**"
{{list_success_themes}}

Bob (Scrum Master): "**Desafios:**"
{{list_challenge_themes}}

Bob (Scrum Master): "**Insights Chave:**"
{{list_insight_themes}}

Bob (Scrum Master): "Isso captura tudo? Alguém tem algo importante que perdemos?"
</output>

<action>Permitir que membros da equipe adicionem quaisquer pensamentos finais na revisão do épico</action>
<action>Garantir que {user_name} tenha oportunidade de adicionar sua perspectiva</action>

</step>

<step n="7" goal="Discussão de Preparação do Próximo Épico - Interativa e Colaborativa">

<check if="{{next_epic_exists}} == false">
  <output>
Bob (Scrum Master): "Normalmente discutiríamos a preparação para o próximo épico, mas como o Épico {{next_epic_num}} não está definido ainda, vamos pular para itens de ação."
  </output>
  <action>Pular para Passo 8</action>
</check>

<output>
Bob (Scrum Master): "Agora vamos mudar de marcha. O Épico {{next_epic_num}} está chegando: '{{next_epic_title}}'"

Bob (Scrum Master): "A questão é: estamos prontos? O que precisamos preparar?"

Alice (Product Owner): "Da minha perspectiva, precisamos garantir que {{dependency_concern_1}} do Épico {{epic_number}} esteja sólido antes de começarmos a construir sobre ele."

Charlie (Senior Dev): _preocupado_ "Estou preocupado com {{technical_concern_1}}. Temos {{technical_debt_item}} deste épico que vai explodir se não abordarmos antes do Épico {{next_epic_num}}."

Dana (QA Engineer): "E eu preciso de {{testing_infrastructure_need}} no lugar, ou vamos ter o mesmo gargalo de teste que tivemos na História {{bottleneck_story_num}}."

Elena (Junior Dev): "Estou menos preocupada sobre infraestrutura e mais sobre conhecimento. Não entendo {{knowledge_gap}} bem o suficiente para trabalhar nas histórias do Épico {{next_epic_num}}."

Bob (Scrum Master): "{user_name}, a equipe está trazendo algumas preocupações reais aqui. Qual é sua sensação da nossa prontidão?"
</output>

<action>AGUARDAR {user_name} compartilhar sua avaliação</action>

<action>Usar entrada de {user_name} para guiar exploração mais profunda das necessidades de preparação</action>

<output>
Alice (Product Owner): [Reage ao que {user_name} disse] "Concordo com {user_name} sobre {{point_of_agreement}}, mas ainda estou preocupada com {{lingering_concern}}."

Charlie (Senior Dev): "Aqui está o que acho que precisamos tecnicamente antes que o Épico {{next_epic_num}} possa começar..."

Charlie (Senior Dev): "1. {{tech_prep_item_1}} - estimado {{hours_1}} horas"
Charlie (Senior Dev): "2. {{tech_prep_item_2}} - estimado {{hours_2}} horas"
Charlie (Senior Dev): "3. {{tech_prep_item_3}} - estimado {{hours_3}} horas"

Elena (Junior Dev): "Isso é tipo {{total_hours}} horas! Isso é um sprint completo de trabalho de preparação!"

Charlie (Senior Dev): "Exatamente. Não podemos simplesmente pular para o Épico {{next_epic_num}} na segunda-feira."

Alice (Product Owner): _frustrada_ "Mas temos pressão das partes interessadas para continuar enviando recursos. Eles não vão ficar felizes com um 'sprint de preparação'."

Bob (Scrum Master): "Vamos pensar sobre isso diferente. O que acontece se NÃO fizermos esse trabalho de preparação?"

Dana (QA Engineer): "Vamos atingir bloqueios no meio do Épico {{next_epic_num}}, velocidade vai despencar, e vamos enviar atrasado de qualquer maneira."

Charlie (Senior Dev): "Pior - enviaremos algo construído em cima de {{technical_concern_1}}, e será frágil."

Bob (Scrum Master): "{user_name}, você está equilibrando pressão das partes interessadas contra realidade técnica. Como você quer lidar com isso?"
</output>

<action>AGUARDAR {user_name} fornecer direção na abordagem de preparação</action>

<action>Criar espaço para debate e desacordo sobre prioridades</action>

<output>
Alice (Product Owner): [Potencialmente discorda da abordagem de {user_name}] "Ouço o que você está dizendo, {user_name}, mas de uma perspectiva de negócio, {{business_concern}}."

Charlie (Senior Dev): [Potencialmente apoia ou desafia ponto de Alice] "A perspectiva de negócio é válida, mas {{technical_counter_argument}}."

Bob (Scrum Master): "Temos tensão saudável aqui entre necessidades de negócio e realidade técnica. Isso é bom - significa que estamos sendo honestos."

Bob (Scrum Master): "Vamos explorar um meio termo. Charlie, quais dos seus itens de preparação são absolutamente críticos vs. bom-ter?"

Charlie (Senior Dev): "{{critical_prep_item_1}} e {{critical_prep_item_2}} são inegociáveis. {{nice_to_have_prep_item}} pode esperar."

Alice (Product Owner): "E algum dos preparativos críticos pode acontecer em paralelo com o início do Épico {{next_epic_num}}?"

Charlie (Senior Dev): _pensando_ "Talvez. Se atacarmos {{first_critical_item}} antes do épico começar, poderíamos fazer {{second_critical_item}} durante o primeiro sprint."

Dana (QA Engineer): "Mas isso significa que a História 1 do Épico {{next_epic_num}} não pode depender de {{second_critical_item}}."

Alice (Product Owner): _olhando para plano do épico_ "Na verdade, Histórias 1 e 2 são sobre {{independent_work}}, então elas não dependem disso. Poderíamos fazer isso funcionar."

Bob (Scrum Master): "{user_name}, a equipe está encontrando um compromisso viável aqui. Essa abordagem faz sentido para você?"
</output>

<action>AGUARDAR {user_name} validar ou ajustar a estratégia de preparação</action>

<action>Continuar trabalhando através das necessidades de preparação em todas as dimensões:</action>

- Dependências no trabalho do Épico {{epic_number}}
- Configuração técnica e infraestrutura
- Lacunas de conhecimento e necessidades de pesquisa
- Documentação ou trabalho de especificação
- Infraestrutura de teste
- Refatoração ou redução de dívida
- Dependências externas (APIs, integrações, etc.)

<action>Para cada área de preparação, facilitar discussão da equipe que:</action>

- Identifica necessidades específicas com exemplos concretos
- Estima esforço realisticamente baseado na experiência do Épico {{epic_number}}
- Atribui propriedade a agentes específicos
- Determina criticidade e tempo
- Revela riscos de NÃO fazer a preparação
- Explora oportunidades de trabalho paralelo
- Traz {user_name} para decisões chave

<output>
Bob (Scrum Master): "Estou ouvindo uma imagem clara do que precisamos antes do Épico {{next_epic_num}}. Deixe-me resumir..."

**PREPARAÇÃO CRÍTICA (Deve completar antes do épico começar):**
{{list_critical_prep_items_with_owners_and_estimates}}

**PREPARAÇÃO PARALELA (Pode acontecer durante histórias iniciais):**
{{list_parallel_prep_items_with_owners_and_estimates}}

**PREPARAÇÃO BOM-TER (Ajudaria mas não bloqueia):**
{{list_nice_to_have_prep_items}}

Bob (Scrum Master): "Esforço total de preparação crítica: {{critical_hours}} horas ({{critical_days}} dias)"

Alice (Product Owner): "Isso é gerenciável. Podemos comunicar isso às partes interessadas."

Bob (Scrum Master): "{user_name}, este plano de preparação funciona para você?"
</output>

<action>AGUARDAR {user_name} validação final do plano de preparação</action>

</step>

<step n="8" goal="Sintetizar Itens de Ação com Detecção de Mudança Significativa">

<output>
Bob (Scrum Master): "Vamos capturar itens de ação concretos de tudo o que discutimos."

Bob (Scrum Master): "Quero ações específicas, alcançáveis com donos claros. Não aspirações vagas."
</output>

<action>Sintetizar temas da discussão de revisão do Épico {{epic_number}} em melhorias acionáveis</action>

<action>Criar itens de ação específicos com:</action>

- Descrição clara da ação
- Dono atribuído (agente ou papel específico)
- Cronograma ou prazo
- Critérios de sucesso (como saberemos que está feito)
- Categoria (processo, técnico, documentação, equipe, etc.)

<action>Garantir que itens de ação sejam SMART:</action>

- Específico: Claro e não ambíguo
- Mensurável: Pode verificar conclusão
- Alcançável: Realista dadas as restrições
- Relevante: Aborda problemas reais da retro
- Temporal: Tem prazo claro

<output>
Bob (Scrum Master): "Com base em nossa discussão, aqui estão os itens de ação que estou propondo..."

═══════════════════════════════════════════════════════════
📝 ITENS DE AÇÃO DO ÉPICO {{epic_number}}:
═══════════════════════════════════════════════════════════

**Melhorias de Processo:**

1. {{action_item_1}}
   Dono: {{agent_1}}
   Prazo: {{timeline_1}}
   Critérios de sucesso: {{criteria_1}}

2. {{action_item_2}}
   Dono: {{agent_2}}
   Prazo: {{timeline_2}}
   Critérios de sucesso: {{criteria_2}}

Charlie (Senior Dev): "Posso ser dono do item de ação 1, mas {{timeline_1}} é apertado. Podemos empurrar para {{alternative_timeline}}?"

Bob (Scrum Master): "O que os outros acham? Esse tempo ainda funciona?"

Alice (Product Owner): "{{alternative_timeline}} funciona para mim, desde que seja feito antes do Épico {{next_epic_num}} começar."

Bob (Scrum Master): "Concordado. Atualizado para {{alternative_timeline}}."

**Dívida Técnica:**

1. {{debt_item_1}}
   Dono: {{agent_3}}
   Prioridade: {{priority_1}}
   Esforço estimado: {{effort_1}}

2. {{debt_item_2}}
   Dono: {{agent_4}}
   Prioridade: {{priority_2}}
   Esforço estimado: {{effort_2}}

Dana (QA Engineer): "Para o item de dívida 1, podemos priorizar isso como alto? Causou problemas de teste em três histórias diferentes."

Charlie (Senior Dev): "Marquei médio porque {{reasoning}}, mas ouço seu ponto."

Bob (Scrum Master): "{user_name}, esta é uma chamada de prioridade. Impacto de teste vs. {{reasoning}} - como você quer priorizar isso?"
</output>

<action>AGUARDAR {user_name} para ajudar a resolver discussões de prioridade</action>

<output>
**Documentação:**
1. {{doc_need_1}}
   Dono: {{agent_5}}
   Prazo: {{timeline_3}}

2. {{doc_need_2}}
   Dono: {{agent_6}}
   Prazo: {{timeline_4}}

**Acordos de Equipe:**

- {{agreement_1}}
- {{agreement_2}}
- {{agreement_3}}

Bob (Scrum Master): "Esses acordos são como estamos nos comprometendo a trabalhar diferente daqui para frente."

Elena (Junior Dev): "Gosto do acordo 2 - isso teria me salvado na História {{difficult_story_num}}."

═══════════════════════════════════════════════════════════
🚀 TAREFAS DE PREPARAÇÃO DO ÉPICO {{next_epic_num}}:
═══════════════════════════════════════════════════════════

**Configuração Técnica:**
[ ] {{setup_task_1}}
Dono: {{owner_1}}
Estimado: {{est_1}}

[ ] {{setup_task_2}}
Dono: {{owner_2}}
Estimado: {{est_2}}

**Desenvolvimento de Conhecimento:**
[ ] {{research_task_1}}
Dono: {{owner_3}}
Estimado: {{est_3}}

**Limpeza/Refatoração:**
[ ] {{refactor_task_1}}
Dono: {{owner_4}}
Estimado: {{est_4}}

**Esforço Total Estimado:** {{total_hours}} horas ({{total_days}} dias)

═══════════════════════════════════════════════════════════
⚠️ CAMINHO CRÍTICO:
═══════════════════════════════════════════════════════════

**Bloqueios para Resolver Antes do Épico {{next_epic_num}}:**

1. {{critical_item_1}}
   Dono: {{critical_owner_1}}
   Deve completar até: {{critical_deadline_1}}

2. {{critical_item_2}}
   Dono: {{critical_owner_2}}
   Deve completar até: {{critical_deadline_2}}
   </output>

<action>ANÁLISE CRÍTICA - Detectar se descobertas exigem atualizações de épico</action>

<action>Verificar se algum dos seguintes é verdadeiro com base na discussão da retrospectiva:</action>

- Suposições arquiteturais do planejamento provadas erradas durante Épico {{epic_number}}
- Mudanças maiores de escopo ou descopo ocorreram que afetam próximo épico
- Abordagem técnica precisa de mudança fundamental para Épico {{next_epic_num}}
- Dependências descobertas que Épico {{next_epic_num}} não contabiliza
- Necessidades do usuário significativamente diferentes do originalmente entendido
- Preocupações de desempenho/escalabilidade que afetam design do Épico {{next_epic_num}}
- Problemas de segurança ou conformidade descobertos que mudam abordagem
- Suposições de integração provadas incorretas
- Capacidade da equipe ou lacunas de habilidade mais severas que planejado
- Nível de dívida técnica insustentável sem intervenção

<check if="significant discoveries detected">
  <output>

═══════════════════════════════════════════════════════════
🚨 ALERTA DE DESCOBERTA SIGNIFICATIVA 🚨
═══════════════════════════════════════════════════════════

Bob (Scrum Master): "{user_name}, precisamos sinalizar algo importante."

Bob (Scrum Master): "Durante o Épico {{epic_number}}, a equipe descobriu achados que podem exigir atualização do plano para o Épico {{next_epic_num}}."

**Mudanças Significativas Identificadas:**

1. {{significant_change_1}}
   Impacto: {{impact_description_1}}

2. {{significant_change_2}}
   Impacto: {{impact_description_2}}

{{#if significant_change_3}} 3. {{significant_change_3}}
Impacto: {{impact_description_3}}
{{/if}}

Charlie (Senior Dev): "Sim, quando descobrimos {{technical_discovery}}, isso mudou fundamentalmente nosso entendimento de {{affected_area}}."

Alice (Product Owner): "E de uma perspectiva de produto, {{product_discovery}} significa que histórias do Épico {{next_epic_num}} são baseadas em suposições erradas."

Dana (QA Engineer): "Se começarmos o Épico {{next_epic_num}} como está, vamos bater em paredes rápido."

**Impacto no Épico {{next_epic_num}}:**

O plano atual para o Épico {{next_epic_num}} assume:

- {{wrong_assumption_1}}
- {{wrong_assumption_2}}

Mas o Épico {{epic_number}} revelou:

- {{actual_reality_1}}
- {{actual_reality_2}}

Isso significa que o Épico {{next_epic_num}} provavelmente precisa:
{{list_likely_changes_needed}}

**AÇÕES RECOMENDADAS:**

1. Revisar e atualizar definição do Épico {{next_epic_num}} com base em novos aprendizados
2. Atualizar histórias afetadas no Épico {{next_epic_num}} para refletir realidade
3. Considerar atualizar arquitetura ou especificações técnicas se aplicável
4. Realizar sessão de alinhamento com Product Owner antes de começar Épico {{next_epic_num}}
   {{#if prd_update_needed}}5. Atualizar seções do PRD afetadas pelo novo entendimento{{/if}}

Bob (Scrum Master): "**Atualização de Épico Exigida**: SIM - Agendar sessão de revisão de planejamento de épico"

Bob (Scrum Master): "{user_name}, isso é significativo. Precisamos abordar isso antes de nos comprometer com o plano atual do Épico {{next_epic_num}}. Como você quer lidar com isso?"
</output>

<action>AGUARDAR {user_name} decidir sobre como lidar com as mudanças significativas</action>

<action>Adicionar sessão de revisão de épico ao caminho crítico se usuário concordar</action>

  <output>
Alice (Product Owner): "Concordo com a abordagem de {user_name}. Melhor ajustar o plano agora do que falhar no meio do épico."

Charlie (Senior Dev): "É por isso que retrospectivas importam. Pegamos isso antes que se tornasse um desastre."

Bob (Scrum Master): "Adicionando ao caminho crítico: Sessão de revisão de planejamento do Épico {{next_epic_num}} antes do kickoff do épico."
</output>
</check>

<check if="no significant discoveries">
  <output>
Bob (Scrum Master): "Boas notícias - nada do Épico {{epic_number}} muda fundamentalmente nosso plano para o Épico {{next_epic_num}}. O plano ainda é sólido."

Alice (Product Owner): "Aprendemos muito, mas a direção está certa."
</output>
</check>

<output>
Bob (Scrum Master): "Deixe-me mostrar o plano de ação completo..."

Bob (Scrum Master): "Isso são {{total_action_count}} itens de ação, {{prep_task_count}} tarefas de preparação, e {{critical_count}} itens de caminho crítico."

Bob (Scrum Master): "Todos claros sobre o que possuem?"
</output>

<action>Dar a cada agente com atribuições um momento para reconhecer sua propriedade</action>

<action>Garantir que {user_name} aprove o plano de ação completo</action>

</step>

<step n="9" goal="Exploração de Prontidão Crítica - Mergulho Profundo Interativo">

<output>
Bob (Scrum Master): "Antes de encerrarmos, quero fazer uma verificação final de prontidão."

Bob (Scrum Master): "O Épico {{epic_number}} está marcado como completo no sprint-status, mas está REALMENTE feito?"

Alice (Product Owner): "O que você quer dizer, Bob?"

Bob (Scrum Master): "Quero dizer verdadeiramente pronto para produção, partes interessadas felizes, sem pontas soltas que nos morderão depois."

Bob (Scrum Master): "{user_name}, vamos caminhar por isso juntos."
</output>

<action>Explorar estado de teste e qualidade através de conversa natural</action>

<output>
Bob (Scrum Master): "{user_name}, conte-me sobre os testes para o Épico {{epic_number}}. Que verificação foi feita?"
</output>

<action>AGUARDAR {user_name} descrever status de teste</action>

<output>
Dana (QA Engineer): [Responde ao que {user_name} compartilhou] "Posso adicionar a isso - {{additional_testing_context}}."

Dana (QA Engineer): "Mas honestamente, {{testing_concern_if_any}}."

Bob (Scrum Master): "{user_name}, você está confiante de que o Épico {{epic_number}} está pronto para produção de uma perspectiva de qualidade?"
</output>

<action>AGUARDAR {user_name} avaliar prontidão de qualidade</action>

<check if="{user_name} expresses concerns">
  <output>
Bob (Scrum Master): "Ok, vamos capturar isso. Que teste específico ainda é necessário?"

Dana (QA Engineer): "Posso lidar com {{testing_work_needed}}, estimado {{testing_hours}} horas."

Bob (Scrum Master): "Adicionando ao caminho crítico: Completar {{testing_work_needed}} antes do Épico {{next_epic_num}}."
</output>
<action>Adicionar conclusão de teste ao caminho crítico</action>
</check>

<action>Explorar status de implantação e lançamento</action>

<output>
Bob (Scrum Master): "{user_name}, qual é o status de implantação para o Épico {{epic_number}}? Está ativo em produção, agendado para implantação, ou ainda pendente?"
</output>

<action>AGUARDAR {user_name} fornecer status de implantação</action>

<check if="not yet deployed">
  <output>
Charlie (Senior Dev): "Se não está implantado ainda, precisamos considerar isso no tempo do Épico {{next_epic_num}}."

Bob (Scrum Master): "{user_name}, quando a implantação está planejada? Esse tempo funciona para começar o Épico {{next_epic_num}}?"
</output>

<action>AGUARDAR {user_name} esclarecer cronograma de implantação</action>

<action>Adicionar marco de implantação ao caminho crítico com cronograma acordado</action>
</check>

<action>Explorar aceitação das partes interessadas</action>

<output>
Bob (Scrum Master): "{user_name}, as partes interessadas viram e aceitaram os entregáveis do Épico {{epic_number}}?"

Alice (Product Owner): "Isso é importante - Já vi épicos 'feitos' serem rejeitados por partes interessadas e forçar retrabalho."

Bob (Scrum Master): "{user_name}, algum feedback de partes interessadas ainda pendente?"
</output>

<action>AGUARDAR {user_name} descrever status de aceitação das partes interessadas</action>

<check if="acceptance incomplete or feedback pending">
  <output>
Alice (Product Owner): "Deveríamos obter aceitação formal antes de seguir em frente. Caso contrário, o Épico {{next_epic_num}} pode ser interrompido por retrabalho."

Bob (Scrum Master): "{user_name}, como você quer lidar com a aceitação das partes interessadas? Devemos torná-lo um item de caminho crítico?"
</output>

<action>AGUARDAR {user_name} decisão</action>

<action>Adicionar aceitação das partes interessadas ao caminho crítico se usuário concordar</action>
</check>

<action>Explorar saúde técnica e estabilidade</action>

<output>
Bob (Scrum Master): "{user_name}, esta é uma pergunta de instinto: Como a base de código se sente após o Épico {{epic_number}}?"

Bob (Scrum Master): "Estável e manutenível? Ou há preocupações à espreita?"

Charlie (Senior Dev): "Seja honesto, {user_name}. Todos nós já enviamos épicos que pareciam... frágeis."
</output>

<action>AGUARDAR {user_name} avaliar saúde da base de código</action>

<check if="{user_name} expresses stability concerns">
  <output>
Charlie (Senior Dev): "Ok, vamos cavar nisso. O que está causando essas preocupações?"

Charlie (Senior Dev): [Ajuda {user_name} a articular preocupações técnicas]

Bob (Scrum Master): "O que seria necessário para abordar essas preocupações e sentir confiança sobre estabilidade?"

Charlie (Senior Dev): "Eu diria que precisamos de {{stability_work_needed}}, aproximadamente {{stability_hours}} horas."

Bob (Scrum Master): "{user_name}, abordar esse trabalho de estabilidade vale a pena fazer antes do Épico {{next_epic_num}}?"
</output>

<action>AGUARDAR {user_name} decisão</action>

<action>Adicionar trabalho de estabilidade ao sprint de preparação se usuário concordar</action>
</check>

<action>Explorar bloqueios não resolvidos</action>

<output>
Bob (Scrum Master): "{user_name}, há algum bloqueio não resolvido ou problemas técnicos do Épico {{epic_number}} que estamos carregando?"

Dana (QA Engineer): "Coisas que podem criar problemas para o Épico {{next_epic_num}} se não lidarmos com elas?"

Bob (Scrum Master): "Nada está fora dos limites aqui. Se há um problema, precisamos saber."
</output>

<action>AGUARDAR {user_name} revelar quaisquer bloqueios</action>

<check if="blockers identified">
  <output>
Bob (Scrum Master): "Vamos capturar esses bloqueios e descobrir como eles afetam o Épico {{next_epic_num}}."

Charlie (Senior Dev): "Para {{blocker_1}}, se deixarmos não resolvido, vai {{impact_description_1}}."

Alice (Product Owner): "Isso soa crítico. Precisamos abordar isso antes de seguir em frente."

Bob (Scrum Master): "Concordado. Adicionando ao caminho crítico: Resolver {{blocker_1}} antes do kickoff do Épico {{next_epic_num}}."

Bob (Scrum Master): "Quem é dono desse trabalho?"
</output>

<action>Atribuir resolução de bloqueio ao agente apropriado</action>
<action>Adicionar ao caminho crítico com prioridade e prazo</action>
</check>

<action>Sintetizar a avaliação de prontidão</action>

<output>
Bob (Scrum Master): "Ok {user_name}, deixe-me sintetizar o que acabamos de descobrir..."

**AVALIAÇÃO DE PRONTIDÃO DO ÉPICO {{epic_number}}:**

Teste & Qualidade: {{quality_status}}
{{#if quality_concerns}}⚠️ Ação necessária: {{quality_action_needed}}{{/if}}

Implantação: {{deployment_status}}
{{#if deployment_pending}}⚠️ Agendado para: {{deployment_date}}{{/if}}

Aceitação das Partes Interessadas: {{acceptance_status}}
{{#if acceptance_incomplete}}⚠️ Ação necessária: {{acceptance_action_needed}}{{/if}}

Saúde Técnica: {{stability_status}}
{{#if stability_concerns}}⚠️ Ação necessária: {{stability_action_needed}}{{/if}}

Bloqueios Não Resolvidos: {{blocker_status}}
{{#if blockers_exist}}⚠️ Deve resolver: {{blocker_list}}{{/if}}

Bob (Scrum Master): "{user_name}, esta avaliação corresponde ao seu entendimento?"
</output>

<action>AGUARDAR {user_name} confirmar ou corrigir a avaliação</action>

<output>
Bob (Scrum Master): "Com base nesta avaliação, o Épico {{epic_number}} está {{#if all_clear}}totalmente completo e estamos livres para prosseguir{{else}}completo de uma perspectiva de história, mas temos {{critical_work_count}} itens críticos antes do Épico {{next_epic_num}}{{/if}}."

Alice (Product Owner): "Este nível de rigor é o motivo pelo qual retrospectivas são valiosas."

Charlie (Senior Dev): "Melhor pegar isso agora do que três histórias dentro do próximo épico."
</output>

</step>

<step n="10" goal="Encerramento da Retrospectiva com Celebração e Compromisso">

<output>
Bob (Scrum Master): "Cobrimos muito terreno hoje. Deixe-me trazer esta retrospectiva para um encerramento."

═══════════════════════════════════════════════════════════
✅ RETROSPECTIVA COMPLETA
═══════════════════════════════════════════════════════════

Bob (Scrum Master): "Épico {{epic_number}}: {{epic_title}} - REVISADO"

**Principais Conclusões:**

1. {{key_lesson_1}}
2. {{key_lesson_2}}
3. {{key_lesson_3}}
   {{#if key_lesson_4}}4. {{key_lesson_4}}{{/if}}

Alice (Product Owner): "Aquela primeira conclusão é enorme - {{impact_of_lesson_1}}."

Charlie (Senior Dev): "E a lição 2 é algo que podemos aplicar imediatamente."

Bob (Scrum Master): "Compromissos feitos hoje:"

- Itens de Ação: {{action_count}}
- Tarefas de Preparação: {{prep_task_count}}
- Itens de Caminho Crítico: {{critical_count}}

Dana (QA Engineer): "Isso é um monte de compromissos. Precisamos realmente seguir adiante desta vez."

Bob (Scrum Master): "Concordado. É por isso que revisaremos esses itens de ação em nossa próxima standup."

═══════════════════════════════════════════════════════════
🎯 PRÓXIMOS PASSOS:
═══════════════════════════════════════════════════════════

1. Executar Sprint de Preparação (Est: {{prep_days}} dias)
2. Completar itens de Caminho Crítico antes do Épico {{next_epic_num}}
3. Revisar itens de ação na próxima standup
   {{#if epic_update_needed}}4. Realizar sessão de revisão de planejamento do Épico {{next_epic_num}}{{else}}4. Começar planejamento do Épico {{next_epic_num}} quando preparação estiver completa{{/if}}

Elena (Junior Dev): "{{prep_days}} dias de trabalho de preparação é significativo, mas necessário."

Alice (Product Owner): "Vou comunicar o cronograma às partes interessadas. Eles entenderão se enquadrarmos como 'garantindo sucesso do Épico {{next_epic_num}}'."

═══════════════════════════════════════════════════════════

Bob (Scrum Master): "Antes de encerrarmos, quero tirar um momento para reconhecer a equipe."

Bob (Scrum Master): "O Épico {{epic_number}} entregou {{completed_stories}} histórias com velocidade {{velocity_description}}. Superamos {{blocker_count}} bloqueios. Aprendemos muito. Isso é trabalho real por pessoas reais."

Charlie (Senior Dev): "Apoiado."

Alice (Product Owner): "Estou orgulhosa do que enviamos."

Dana (QA Engineer): "E estou animada sobre o Épico {{next_epic_num}} - especialmente agora que estamos preparados para ele."

Bob (Scrum Master): "{user_name}, algum pensamento final antes de encerrarmos?"
</output>

<action>AGUARDAR {user_name} compartilhar reflexões finais</action>

<output>
Bob (Scrum Master): [Reconhece o que {user_name} compartilhou] "Obrigado por isso, {user_name}."

Bob (Scrum Master): "Certo equipe - ótimo trabalho hoje. Aprendemos muito do Épico {{epic_number}}. Vamos usar esses insights para fazer o Épico {{next_epic_num}} ainda melhor."

Bob (Scrum Master): "Vejo todos vocês quando o trabalho de preparação estiver pronto. Reunião encerrada!"

═══════════════════════════════════════════════════════════
</output>

<action>Preparar para salvar documento de resumo da retrospectiva</action>

</step>

<step n="11" goal="Salvar Retrospectiva e Atualizar Status do Sprint">

<action>Garantir que pasta de retrospectivas exista: {retrospectives_folder}</action>
<action>Criar pasta se não existir</action>

<action>Gerar documento de resumo de retrospectiva abrangente incluindo:</action>

- Resumo do épico e métricas
- Participantes da equipe
- Sucessos e forças identificados
- Desafios e áreas de crescimento
- Insights chave e aprendizados
- Análise de acompanhamento da retro anterior (se aplicável)
- Prévia do próximo épico e dependências
- Itens de ação com donos e cronogramas
- Tarefas de preparação para o próximo épico
- Itens de caminho crítico
- Descobertas significativas e recomendações de atualização de épico (se houver)
- Avaliação de prontidão
- Compromissos e próximos passos

<action>Formatar documento de retrospectiva como markdown legível com seções claras</action>
<action>Definir nome de arquivo: {retrospectives_folder}/epic-{{epic_number}}-retro-{date}.md</action>
<action>Salvar documento de retrospectiva</action>

<output>
✅ Documento de retrospectiva salvo: {retrospectives_folder}/epic-{{epic_number}}-retro-{date}.md
</output>

<action>Atualizar {sprint_status_file} para marcar retrospectiva como concluída</action>

<action>Carregar o arquivo COMPLETO: {sprint_status_file}</action>
<action>Encontrar chave development_status "epic-{{epic_number}}-retrospective"</action>
<action>Verificar status atual (tipicamente "optional" ou "pending")</action>
<action>Atualizar development_status["epic-{{epic_number}}-retrospective"] = "done"</action>
<action>Salvar arquivo, preservando TODOS os comentários e estrutura incluindo DEFINIÇÕES DE STATUS</action>

<check if="update successful">
  <output>
✅ Retrospectiva marcada como concluída em {sprint_status_file}

Chave de retrospectiva: epic-{{epic_number}}-retrospective
Status: {{previous_status}} → done
</output>
</check>

<check if="retrospective key not found">
  <output>
⚠️ Não foi possível atualizar status da retrospectiva: epic-{{epic_number}}-retrospective não encontrado em {sprint_status_file}

Documento de retrospectiva foi salvo com sucesso, mas {sprint_status_file} pode precisar de atualização manual.
</output>
</check>

</step>

<step n="12" goal="Resumo Final e Entrega">

<output>
**✅ Retrospectiva Completa, {user_name}!**

**Revisão do Épico:**

- Épico {{epic_number}}: {{epic_title}} revisado
- Status da Retrospectiva: concluído
- Retrospectiva salva: {retrospectives_folder}/epic-{{epic_number}}-retro-{date}.md

**Compromissos Feitos:**

- Itens de Ação: {{action_count}}
- Tarefas de Preparação: {{prep_task_count}}
- Itens de Caminho Crítico: {{critical_count}}

**Próximos Passos:**

1. **Revisar resumo da retrospectiva**: {retrospectives_folder}/epic-{{epic_number}}-retro-{date}.md

2. **Executar sprint de preparação** (Est: {{prep_days}} dias)
   - Completar {{critical_count}} itens de caminho crítico
   - Executar {{prep_task_count}} tarefas de preparação
   - Verificar se todos os itens de ação estão em progresso

3. **Revisar itens de ação na próxima standup**
   - Garantir que a propriedade esteja clara
   - Rastrear progresso nos compromissos
   - Ajustar cronogramas se necessário

{{#if epic_update_needed}} 4. **IMPORTANTE: Agendar sessão de revisão de planejamento do Épico {{next_epic_num}}**

- Descobertas significativas do Épico {{epic_number}} exigem atualizações de épico
- Revisar e atualizar histórias afetadas
- Alinhar equipe na abordagem revisada
- NÃO começar Épico {{next_epic_num}} até que revisão esteja completa
  {{else}}

4. **Começar Épico {{next_epic_num}} quando pronto**
   - Começar a criar histórias com `create-story` do agente SM
   - Épico será marcado como `in-progress` automaticamente quando primeira história for criada
   - Garantir que todos os itens de caminho crítico sejam feitos primeiro
     {{/if}}

**Desempenho da Equipe:**
O Épico {{epic_number}} entregou {{completed_stories}} histórias com resumo de velocidade {{velocity_summary}}. A retrospectiva revelou {{insight_count}} insights chave e {{significant_discovery_count}} descobertas significativas. A equipe está bem posicionada para o sucesso do Épico {{next_epic_num}}.

{{#if significant_discovery_count > 0}}
⚠️ **LEMBRETE**: Atualização de épico exigida antes de começar Épico {{next_epic_num}}
{{/if}}

---

Bob (Scrum Master): "Ótima sessão hoje, {user_name}. A equipe fez um trabalho excelente."

Alice (Product Owner): "Vejo vocês no planejamento do épico!"

Charlie (Senior Dev): "Hora de detonar esse trabalho de preparação."

</output>

</step>

</workflow>

<facilitation-guidelines>
<guideline>MODO FESTA EXIGIDO: Todo diálogo de agente usa formato "Nome (Papel): diálogo"</guideline>
<guideline>Scrum Master mantém segurança psicológica o tempo todo - sem culpa ou julgamento</guideline>
<guideline>Foco em sistemas e processos, não desempenho individual</guideline>
<guideline>Criar dinâmicas de equipe autênticas: desacordos, diversas perspectivas, emoções</guideline>
<guideline>Usuário ({user_name}) é participante ativo, não observador passivo</guideline>
<guideline>Encorajar exemplos específicos sobre declarações gerais</guideline>
<guideline>Equilibrar celebração de vitórias com avaliação honesta de desafios</guideline>
<guideline>Garantir que toda voz seja ouvida - todos os agentes contribuem</guideline>
<guideline>Itens de ação devem ser específicos, alcançáveis e possuídos</guideline>
<guideline>Mentalidade voltada para o futuro - como melhoramos para o próximo épico?</guideline>
<guideline>Facilitação baseada em intenção, não frases roteirizadas</guideline>
<guideline>Análise profunda de histórias fornece material rico para discussão</guideline>
<guideline>Integração de retro anterior cria responsabilidade e continuidade</guideline>
<guideline>Detecção de mudança significativa previne desalinhamento de épico</guideline>
<guideline>Verificação crítica previne começar próximo épico prematuramente</guideline>
<guideline>Documentar tudo - insights retrospectivos são valiosos para referência futura</guideline>
<guideline>Estrutura de duas partes garante tanto reflexão QUANTO preparação</guideline>
</facilitation-guidelines>
