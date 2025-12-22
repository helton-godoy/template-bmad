# Curso Correto - Instruções de Gestão de Mudança de Sprint

<critical>O motor de execução de fluxo de trabalho é regido por: {project-root}/\ bmad/core/tasks/workflow.xml</critical>
<critical>Você já deve ter carregado e processado: {project-root}/\ bmad/bmm/workflows/4-implementation/correct-course/workflow.yaml</critical>
<critical> Comunicar todas as respostas em {communication_language} e a linguagem DEVE ser adaptada ao {user_skill_level}BADPROTECT072END
<critical>Gere todos os documentos em {document_output_language}BADPROTECT070END

<critical>DOCUMENT OUTPUT: Seções atualizadas de épicos, histórias ou PRD. Mudanças claras e acionáveis. Nível de habilidade do usuário ({user_skill_level}) afeta o estilo de conversação SOMENTE, não atualizações de documentos. </critical>

<workflow>

<step n="1" goal="Initialize Change Navigation">
<action>Confirme o gatilho de mudança e reúna a descrição do usuário do problema</action>
<action>Ask: "Que problema específico ou mudança foi identificada que requer navegação? " </action>
<action>Verify access to required project documents:</action>
- PRD (Documento dos requisitos do produto)
- Épicos e Histórias atuais
- Documentação de arquitectura
- Especificações UI/UX
<action>Pergunte ao usuário para preferência de modo:</action>
- **Incremental** (recomendado): Refinar cada edição em colaboração
- **Lote**: apresentar todas as alterações de uma vez para revisão
<action>Store seleção de modo para uso ao longo do fluxo de trabalho</action>

<action if="change trigger is unclear">HALT: "Não pode navegar na mudança sem entender claramente o problema desencadeante. Por favor, forneça detalhes específicos sobre o que precisa mudar e por quê. " </action>

<action if="core documents are unavailable">HALT: "Precisa de acesso a documentos de projeto (PRD, Epics, Architecture, UI/UX) para avaliar o impacto da mudança. Certifique-se de que estes documentos estão acessíveis. " </action>
</step>

<step n="0.5" goal="Discover and load project documents">
<invoke-protocol name="discover_inputs" />
<note>Após a descoberta, estas variáveis de conteúdo estão disponíveis: BMADPROTECT084End, BMADPROTECT083End, BMADPROTECT082End, BMADPROTECT081End, BMADPROTECT080End, {document_project_content}BADPROTECT047End
</step>

<step n="2" goal="Execute Change Analysis Checklist">
<action>Load e executar a análise sistemática de: {checklist}BADPROTECT043END
<action>Trabalhar através de cada secção de lista de verificação interactivamente com o utilizador</action>
<action>Status de gravação para cada item da lista de verificação:</action>
Ponto concluído com sucesso
- [N/A] Skip - Item não aplicável a esta alteração
- [!] Necessário ação - Item requer atenção ou acompanhamento
<action>Manter notas de execução de resultados e impactos descobertos</action>
<action>Progresso da lista de verificação apresentada após cada secção principal</action>

<action if="checklist cannot be completed">Identifique problemas de bloqueio e trabalhe com o usuário para resolver antes de continuar </action>
</step>

<step n="3" goal="Draft Specific Change Proposals">
<action>Com base em resultados de checklist, crie propostas de edição explícita para cada artefato identificado</action>

BMADPROTECT028EndFor Story changes:</action>

- Mostrar antigo → novo formato de texto
- Incluir ID de história e seção sendo modificada
- Fornecer razões para cada mudança
- Formato de exemplo:

```
  Story: [STORY-123] User Authentication
  Section: Acceptance Criteria

  OLD:
  - User can log in with email/password

  NEW:
  - User can log in with email/password
  - User can enable 2FA via authenticator app

  Rationale: Security requirement identified during implementation
  ```

BMADPROTECT026EndFor PRD modifications:BMADPROTECT025End

- Especifique seções exatas para atualizar
- Mostrar o conteúdo actual e as alterações propostas
- Explicar o impacto no âmbito e requisitos MVP

<action>For Architecture changes:</action>

- Identificar componentes, padrões ou escolhas tecnológicas afetados
- Descreva as atualizações do diagrama necessárias
- Observe quaisquer efeitos ondulantes em outros componentes

<action>Para atualizações da especificação UI/UX:</action>

- Ecrãs ou componentes específicos de referência
- Mostrar alterações de fluxo ou wireframe necessárias
- Conecte alterações ao impacto da experiência do usuário

<check if="mode is Incremental">
<action>Presente cada proposta de edição individualmente</action>
<ask>Reveja e refine esta alteração? Opções: Aprovar [a], Editar [e], Ignorar [s]</ask>
<action>Iterar em cada proposta com base no feedback do usuário</action>
</check>

<action if="mode is Batch">Coletar todas as propostas de edição e apresentar juntos no final do passo</action>

</step>

<step n="4" goal="Generate Sprint Change Proposal">
<action>Compilar documento abrangente Sprint Change Proposta com as seguintes seções:</action>

<action>Esecção 1: Resumo da questão</action>

- Limpar instrução de problema descrevendo o que desencadeou a mudança
- Contexto sobre quando/como o problema foi descoberto
- Provas ou exemplos que demonstrem a questão

<action>Ssecção 2: Análise de Impacto</action>

- Impacto épico: Quais épicos são afetados e como
- Impacto da História: Histórias atuais e futuras que exigem mudanças
- Conflitos de Artefatos: PRD, Arquitetura, UI/UX documentos que necessitam de atualizações
- Impacto técnico: Código, infra-estrutura ou implantação i