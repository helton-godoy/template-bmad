# Alterar lista de verificação de navegação

<critical>Esta lista de verificação é executada como parte de: {project-root}/\ bmad/bmm/workflows/4-implementation/correct-course/workflow.yaml</critical>
<critical>Trabalhe através de cada seção sistematicamente com o usuário, registrando achados e impactos</critical>

<checklist>

<section n="1" title="Understand the Trigger and Context">

<check-item id="1.1">
<prompt>Identificar a história desencadeante que revelou esta edição</prompt>
<action>Document story ID e breve descrição</action>
<status> [] Feito / [] N/A / [ ] BMADPROTECT126FEND
</check-item>

<check-item id="1.2">
<prompt>Define o problema central precisamente </prompt>
<action>Categorize issue type:</action>
- Limitação técnica descoberta durante o implementation
- Nova exigência surgiu das partes interessadas
- Mal-entendido dos requisitos originais
- Mudança estratégica do pivô ou do mercado
- Abordagem falha requerendo solução diferente
<action>Escreva uma declaração de problema clara</action>
<status> [] Feito / [] N/A / [ ] </status>
</check-item>

<check-item id="1.3">
<prompt>Avaliar o impacto inicial e recolher provas de apoio</prompt>
<action>Colecione exemplos concretos, mensagens de erro, feedback das partes interessadas ou restrições técnicas</action>
<action>Documento para referência posterior </action>
<status> [] Feito / [] N/A / [ ] Acção necessária </status>
</check-item>

<halt-condition>
<action if="trigger is unclear">HALT: "Não pode prosseguir sem entender o que causou a necessidade de mudança"</action>
<action if="no evidence provided">HALT: "Precisa de evidências concretas ou exemplos da questão antes de analisar o impacto"</action>
</halt-condition>

</section>

<section n="2" title="Epic Impact Assessment">

<check-item id="2.1">
<prompt>Avaliar o épico atual que contém a história do gatilho</prompt>
<action>Este épico ainda pode ser concluído como originalmente planned?</action>
<action>Se não, que modificações são necessárias? </action>
<status> [] Feito / [] N/A / [ ] Acção necessária </status>
</check-item>

<check-item id="2.2">
<prompt>Determine as alterações necessárias ao nível épico</prompt>
BMADPROTECT083EndVerifique cada cenário:</action>
- Modificar o âmbito épico existente ou critérios de aceitação
- Adicionar novo épico para abordar o problema
- Remover ou adiar épico que já não é viável
- Completamente redefinir épico com base em novo entendimento
<action>Mudanças épicas específicas necessárias</action>
<status> [] Feito / [] N/A / [ ] </status>
</check-item>

<check-item id="2.3">
<prompt>Rever todos os restantes planned épicos para alterações necessárias</prompt>
<action>Verifique cada épico futuro para impacto</action>
<action>Identificar dependências que podem ser afetadas</action>
<status> [] Feito / [] N/A / [ ] Acção necessária </status>
</check-item>

<check-item id="2.4">
<prompt>Verifique se a questão invalida futuros épicos ou requer novos </prompt>
<action>Esta alteração torna qualquer planned épicos obsoletos? </action>
<action>São novos épicos necessários para resolver lacunas criadas por esta alteração? </action>
<status> [] Feito / [] N/A / [ ] Action-necessária</status>
</check-item>

<check-item id="2.5">
<prompt>Considere se ordem ou prioridade épica deve mudar </prompt>
<action>S devem ser resequenciados épicos com base nesta questão? </action>
<action>As prioridades precisam de ajustamento? </action>
<status> [] Feito / [] N/A / [ ] </status>
</check-item>

</section>

<section n="3" title="Artifact Conflict and Impact Analysis">

<check-item id="3.1">
<prompt> Check PRD para conflitos</prompt>
<action>E emite conflitos com os principais objetivos ou objetivos PRD? </action>
<action>Precisa de modificação, adição ou remoção? </action>
<action>O MVP definido ainda é possível ou o escopo precisa de ajuste? </action>
<status> [] Feito / [] N/A / [ ] Acção necessária BMADPROTECT034End
</check-item>

<check-item id="3.2">
<prompt>Review Architecture document for conflicts</prompt>
<action>Verifique cada área para o impacto:</action>
- Componentes do sistema e suas interações
- Padrões de arquitetura e decisões de design
- Escolhas de pilha de tecnologia
- Modelos de dados e esquemas
- Projetos e contratos de API
- Pontos de integração
<action>Seções de arquitetura específicas de documentos que exigem atualizações</action>
<status> [] Feito / [] N/A / [ ] </status>
</check-item>

<check-item id="3.3">
<prompt>Examine especificações UI/UX para conflitos</prompt>
BMADPROTECT019EndVerificar o impacto em:</action>
- Componentes de interface do usuário
- Fluxos de usuários e viagens
- Wireframes ou maquetes
- Padrões de interacção
- Considerações de acessibilidade
<action>Note secções específicas de UI/UX que necessitam de revisão</action>
<status> [] Feito / [] N/A / [ ] </status>
</check-item>

<check-item id="3.4">
BMADPROTECT011EndConsidere o impacto em outros artefatos</prompt>
<action>Reveja artefatos adicionais para impacto:</action>
- Programas de implantação
- Infra-estrutura como código (IaC)
- Instalação de monitoramento e observação
- Estratégias de teste
- Documentação
- Oleodutos CI/CD
<action>Documento quaisquer artefatos secundários que necessitem de atualizações</action>
<status> [] Feito / [] N/A / [