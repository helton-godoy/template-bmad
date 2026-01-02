# Lista de Verificação de Navegação de Mudança

<critical>Esta lista de verificação é executada como parte de: {project-root}/_bmad/bmm/workflows/4-implementation/correct-course/workflow.yaml</critical>
<critical>Trabalhe através de cada seção sistematicamente com o usuário, registrando descobertas e impactos</critical>

<checklist>

<section n="1" title="Entender o Gatilho e Contexto">

<check-item id="1.1">
<prompt>Identifique a história de gatilho que revelou este problema</prompt>
<action>Documente o ID da história e uma breve descrição</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="1.2">
<prompt>Defina o problema central precisamente</prompt>
<action>Categorize o tipo de problema:</action>
  - Limitação técnica descoberta durante a implementação
  - Novo requisito surgido dos stakeholders
  - Má compreensão dos requisitos originais
  - Pivô estratégico ou mudança de mercado
  - Abordagem falha exigindo solução diferente
<action>Escreva uma declaração clara do problema</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="1.3">
<prompt>Avalie o impacto inicial e reúna evidências de apoio</prompt>
<action>Colete exemplos concretos, mensagens de erro, feedback das partes interessadas ou restrições técnicas</action>
<action>Documente evidências para referência posterior</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<halt-condition>
<action if="gatilho não está claro">PARAR: "Não é possível prosseguir sem entender o que causou a necessidade de mudança"</action>
<action if="nenhuma evidência fornecida">PARAR: "Precisa de evidências concretas ou exemplos do problema antes de analisar o impacto"</action>
</halt-condition>

</section>

<section n="2" title="Avaliação de Impacto Épico">

<check-item id="2.1">
<prompt>Avalie o épico atual contendo a história de gatilho</prompt>
<action>Este épico ainda pode ser concluído conforme planejado originalmente?</action>
<action>Se não, quais modificações são necessárias?</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="2.2">
<prompt>Determine as mudanças necessárias no nível épico</prompt>
<action>Verifique cada cenário:</action>
  - Modificar o escopo ou critérios de aceitação do épico existente
  - Adicionar novo épico para resolver o problema
  - Remover ou adiar épico que não é mais viável
  - Redefinir completamente o épico com base no novo entendimento
<action>Documente as mudanças épicas específicas necessárias</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="2.3">
<prompt>Revise todos os épicos planejados restantes para mudanças necessárias</prompt>
<action>Verifique cada épico futuro quanto ao impacto</action>
<action>Identifique dependências que podem ser afetadas</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="2.4">
<prompt>Verifique se o problema invalida épicos futuros ou necessita de novos</prompt>
<action>Essa mudança torna algum épico planejado obsoleto?</action>
<action>Novos épicos são necessários para preencher lacunas criadas por essa mudança?</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="2.5">
<prompt>Considere se a ordem ou prioridade do épico deve mudar</prompt>
<action>Os épicos devem ser resequenciados com base neste problema?</action>
<action>As prioridades precisam de ajuste?</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

</section>

<section n="3" title="Conflito de Artefato e Análise de Impacto">

<check-item id="3.1">
<prompt>Verifique o PRD para conflitos</prompt>
<action>O problema entra em conflito com os principais objetivos ou metas do PRD?</action>
<action>Os requisitos precisam de modificação, adição ou remoção?</action>
<action>O MVP definido ainda é alcançável ou o escopo precisa de ajuste?</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="3.2">
<prompt>Revise o documento de Arquitetura para conflitos</prompt>
<action>Verifique cada área quanto ao impacto:</action>
  - Componentes do sistema e suas interações
  - Padrões arquitetônicos e decisões de design
  - Escolhas de pilha de tecnologia
  - Modelos e esquemas de dados
  - Designs e contratos de API
  - Pontos de integração
<action>Documente seções específicas de arquitetura que exigem atualizações</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="3.3">
<prompt>Examine as especificações de UI/UX para conflitos</prompt>
<action>Verifique o impacto em:</action>
  - Componentes de interface do usuário
  - Fluxos e jornadas do usuário
  - Wireframes ou mockups
  - Padrões de interação
  - Considerações de acessibilidade
<action>Observe seções específicas de UI/UX que precisam de revisão</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="3.4">
<prompt>Considere o impacto em outros artefatos</prompt>
<action>Revise artefatos adicionais quanto ao impacto:</action>
  - Scripts de implantação
  - Infraestrutura como Código (IaC)
  - Configuração de monitoramento e observabilidade
  - Estratégias de teste
  - Documentação
  - Pipelines de CI/CD
<action>Documente quaisquer artefatos secundários que exijam atualizações</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

</section>

<section n="4" title="Avaliação do Caminho a Seguir">

<check-item id="4.1">
<prompt>Avalie a Opção 1: Ajuste Direto</prompt>
<action>O problema pode ser resolvido modificando histórias existentes?</action>
<action>Novas histórias podem ser adicionadas dentro da estrutura épica atual?</action>
<action>Essa abordagem manteria o cronograma e o escopo do projeto?</action>
<action>Estimativa de esforço: [Alto/Médio/Baixo]</action>
<action>Nível de risco: [Alto/Médio/Baixo]</action>
<status>[ ] Viável / [ ] Não viável</status>
</check-item>

<check-item id="4.2">
<prompt>Avalie a Opção 2: Reversão Potencial (Rollback)</prompt>
<action>Reverter histórias concluídas recentemente simplificaria a resolução deste problema?</action>
<action>Quais histórias precisariam ser revertidas?</action>
<action>O esforço de reversão é justificado pela simplificação obtida?</action>
<action>Estimativa de esforço: [Alto/Médio/Baixo]</action>
<action>Nível de risco: [Alto/Médio/Baixo]</action>
<status>[ ] Viável / [ ] Não viável</status>
</check-item>

<check-item id="4.3">
<prompt>Avalie a Opção 3: Revisão do PRD MVP</prompt>
<action>O PRD MVP original ainda é alcançável com este problema?</action>
<action>O escopo do MVP precisa ser reduzido ou redefinido?</action>
<action>Os objetivos principais precisam de modificação com base em novas restrições?</action>
<action>O que seria adiado para pós-MVP se o escopo for reduzido?</action>
<action>Estimativa de esforço: [Alto/Médio/Baixo]</action>
<action>Nível de risco: [Alto/Médio/Baixo]</action>
<status>[ ] Viável / [ ] Não viável</status>
</check-item>

<check-item id="4.4">
<prompt>Selecione o caminho recomendado a seguir</prompt>
<action>Com base na análise de todas as opções, escolha o melhor caminho</action>
<action>Forneça uma justificativa clara considerando:</action>
  - Esforço de implementação e impacto no cronograma
  - Risco técnico e complexidade
  - Impacto no moral da equipe e impulso
  - Sustentabilidade e manutenibilidade a longo prazo
  - Expectativas das partes interessadas e valor comercial
<action>Abordagem selecionada: [Opção 1 / Opção 2 / Opção 3 / Híbrida]</action>
<action>Justificativa: [Documentar raciocínio]</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

</section>

<section n="5" title="Componentes da Proposta de Mudança de Sprint">

<check-item id="5.1">
<prompt>Crie um resumo do problema identificado</prompt>
<action>Escreva uma declaração de problema clara e concisa</action>
<action>Inclua contexto sobre descoberta e impacto</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="5.2">
<prompt>Documente o impacto épico e as necessidades de ajuste de artefatos</prompt>
<action>Resuma as descobertas da Avaliação de Impacto Épico (Seção 2)</action>
<action>Resuma as descobertas da Análise de Conflito de Artefato (Seção 3)</action>
<action>Seja específico sobre quais mudanças são necessárias e por que</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="5.3">
<prompt>Apresente o caminho recomendado a seguir com justificativa</prompt>
<action>Inclua a abordagem selecionada da Seção 4</action>
<action>Forneça justificativa completa para recomendação</action>
<action>Aborde trade-offs e alternativas consideradas</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="5.4">
<prompt>Defina o impacto no PRD MVP e o plano de ação de alto nível</prompt>
<action>Declare claramente se o MVP é afetado</action>
<action>Descreva os principais itens de ação necessários para implementação</action>
<action>Identifique dependências e sequenciamento</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="5.5">
<prompt>Estabeleça o plano de transferência do agente</prompt>
<action>Identifique quais papéis/agentes executarão as mudanças:</action>
  - Equipe de desenvolvimento (para implementação)
  - Product Owner / Scrum Master (para mudanças no backlog)
  - Gerente de Produto / Arquiteto (para mudanças estratégicas)
<action>Defina responsabilidades para cada papel</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

</section>

<section n="6" title="Revisão Final e Transferência">

<check-item id="6.1">
<prompt>Revise a conclusão da lista de verificação</prompt>
<action>Verifique se todas as seções aplicáveis foram abordadas</action>
<action>Confirme se todos os itens de [Ação necessária] foram documentados</action>
<action>Garanta que a análise seja abrangente e acionável</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="6.2">
<prompt>Verifique a precisão da Proposta de Mudança de Sprint</prompt>
<action>Revise a proposta completa quanto à consistência e clareza</action>
<action>Garanta que todas as recomendações sejam bem apoiadas pela análise</action>
<action>Verifique se a proposta é acionável e específica</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="6.3">
<prompt>Obtenha aprovação explícita do usuário</prompt>
<action>Apresente a proposta completa ao usuário</action>
<action>Obtenha aprovação clara de sim/não para prosseguir</action>
<action>Documente a aprovação e quaisquer condições</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<check-item id="6.4">
<prompt>Confirme os próximos passos e o plano de transferência</prompt>
<action>Revise as responsabilidades de transferência com o usuário</action>
<action>Garanta que todas as partes interessadas entendam seus papéis</action>
<action>Confirme o cronograma e os critérios de sucesso</action>
<status>[ ] Feito / [ ] N/A / [ ] Ação necessária</status>
</check-item>

<halt-condition>
<action if="qualquer seção crítica não puder ser concluída">PARAR: "Não é possível prosseguir para a proposta sem análise de impacto completa"</action>
<action if="aprovação do usuário não obtida">PARAR: "Deve ter aprovação explícita antes de implementar mudanças"</action>
<action if="responsabilidades de transferência não claras">PARAR: "Deve definir claramente quem executará as mudanças propostas"</action>
</halt-condition>

</section>

</checklist>

<execution-notes>
<note>Esta lista de verificação é para mudanças SIGNIFICATIVAS que afetam a direção do projeto</note>
<note>Trabalhe interativamente com o usuário - eles tomam as decisões finais</note>
<note>Seja factual, não orientado a culpa ao analisar problemas</note>
<note>Lide com as mudanças profissionalmente como oportunidades para melhorar o projeto</note>
<note>Mantenha o contexto da conversa em todo o processo - este é um trabalho colaborativo</note>
</execution-notes>
