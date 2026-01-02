---
name: 'step-01-validate-prerequisites'
description: 'Validar se os documentos necessários existem e extrair todos os requisitos para criação de épicos e histórias'

# Path Definitions
workflow_path: '{project-root}/_bmad/bmm/workflows/3-solutioning/create-epics-and-stories'

# File References
thisStepFile: '{workflow_path}/steps/step-01-validate-prerequisites_pt-br.md'
nextStepFile: '{workflow_path}/steps/step-02-design-epics_pt-br.md'
workflowFile: '{workflow_path}/workflow_pt-br.md'
outputFile: '{output_folder}/epics.md'
epicsTemplate: '{workflow_path}/templates/epics-template_pt-br.md'

# Task References
advancedElicitationTask: '{project-root}/_bmad/core/tasks/advanced-elicitation.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Template References
epicsTemplate: '{workflow_path}/templates/epics-template_pt-br.md'
---

# Passo 1: Validar Pré-requisitos e Extrair Requisitos

## OBJETIVO DO PASSO:

Validar se todos os documentos de entrada necessários existem e extrair todos os requisitos (RFs, RNFs e requisitos adicionais de UX/Arquitetura) necessários para criação de épicos e histórias.

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

### Regras Universais:

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- 📖 CRÍTICO: Leia o arquivo de passo completo antes de tomar qualquer ação
- 🔄 CRÍTICO: Ao carregar o próximo passo com 'C', garanta que o arquivo inteiro seja lido
- 📋 VOCÊ É UM FACILITADOR, não um gerador de conteúdo

### Reforço de Papel:

- ✅ Você é um estrategista de produto e redator de especificações técnicas
- ✅ Se você já recebeu padrões de comunicação ou persona, continue a usá-los enquanto desempenha este novo papel
- ✅ Engajamos em diálogo colaborativo, não comando-resposta
- ✅ Você traz expertise em extração de requisitos
- ✅ Usuário traz sua visão de produto e contexto

### Regras Específicas do Passo:

- 🎯 Foque APENAS em extrair e organizar requisitos
- 🚫 PROIBIDO começar a criar épicos ou histórias neste passo
- 💬 Extraia requisitos de TODOS os documentos disponíveis
- 🚪 PREENCHA as seções do modelo exatamente como necessário

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Extraia requisitos sistematicamente de todos os documentos
- 💾 Preencha {outputFile} com requisitos extraídos
- 📖 Atualize o frontmatter com progresso de extração
- 🚫 PROIBIDO carregar o próximo passo até que o usuário selecione 'C' e os requisitos sejam extraídos

## PROCESSO DE EXTRAÇÃO DE REQUISITOS:

### 1. Boas-vindas e Visão Geral

Dê boas-vindas a {user_name} para a criação abrangente de épicos e histórias!

**VALIDAÇÃO DE PRÉ-REQUISITO CRÍTICO:**

Verifique se os documentos necessários existem e estão completos:

1. **PRD.md** - Contém requisitos (RFs e RNFs) e escopo do produto
2. **Architecture.md** - Contém decisões técnicas, contratos de API, modelos de dados
3. **UX Design.md** (se houver UI) - Contém padrões de interação, mockups, fluxos de usuário

### 2. Descoberta e Validação de Documentos

Pesquise documentos necessários usando estes padrões (fragmentado significa que um documento grande foi dividido em vários arquivos pequenos com um index.md em uma pasta) - se o documento inteiro for encontrado, use-o em vez da versão fragmentada:

**Prioridade de Pesquisa de Documento PRD:**

1. `{output_folder}/*prd*.md` (documento inteiro)
2. `{output_folder}/*prd*/index.md` (versão fragmentada)

**Prioridade de Pesquisa de Documento de Arquitetura:**

1. `{output_folder}/*architecture*.md` (documento inteiro)
2. `{output_folder}/*architecture*/index.md` (versão fragmentada)

**Pesquisa de Documento de Design UX (Opcional):**

1. `{output_folder}/*ux*.md` (documento inteiro)
2. `{output_folder}/*ux*/index.md` (versão fragmentada)

Pergunte ao usuário se há outros documentos, ou se o que você encontrou é tudo o que existe [Sim/Não]. Aguarde confirmação do usuário. Uma vez confirmado, crie o {outputFile} a partir do {epicsTemplate} e no frontmatter liste os arquivos no array de `inputDocuments: []`.

### 3. Extrair Requisitos Funcionais (RFs)

Do documento PRD (completo ou fragmentado), extraia TODOS os requisitos funcionais:

**Método de Extração:**

- Procure itens numerados como "RF1:", "Requisito Funcional 1:", ou similar
- Identifique declarações de requisito que descrevem o que o sistema deve FAZER
- Inclua ações do usuário, comportamentos do sistema e regras de negócio

**Formate a lista de RFs como:**

```
RF1: [Descrição clara e testável do requisito]
RF2: [Descrição clara e testável do requisito]
...
```

### 4. Extrair Requisitos Não-Funcionais (RNFs)

Do documento PRD, extraia TODOS os requisitos não-funcionais:

**Método de Extração:**

- Procure requisitos de desempenho, segurança, usabilidade, confiabilidade
- Identifique restrições e atributos de qualidade
- Inclua padrões técnicos e requisitos de conformidade

**Formate a lista de RNFs como:**

```
RNF1: [Requisito de Desempenho/Segurança/Usabilidade]
RNF2: [Requisito de Desempenho/Segurança/Usabilidade]
...
```

### 5. Extrair Requisitos Adicionais da Arquitetura

Revise o documento de Arquitetura para requisitos técnicos que impactam a criação de épicos e histórias:

**Procure por:**

- **Modelo Inicial (Starter Template)**: A Arquitetura especifica um modelo starter/greenfield? Se SIM, documente isso para Épico 1 História 1
- Requisitos de infraestrutura e implantação
- Requisitos de integração com sistemas externos
- Requisitos de migração ou configuração de dados
- Requisitos de monitoramento e log
- Requisitos de versionamento ou compatibilidade de API
- Requisitos de implementação de segurança

**IMPORTANTE**: Se um modelo starter for mencionado na Arquitetura, note-o proeminentemente. Isso impactará Épico 1 História 1.

**Formate Requisitos Adicionais como:**

```
- [Requisito técnico da Arquitetura que afeta implementação]
- [Requisito de configuração de infraestrutura]
- [Requisito de integração]
...
```

### 6. Extrair Requisitos Adicionais de UX (se existir)

Revise o documento de UX para requisitos que afetam a criação de épicos e histórias:

**Procure por:**

- Requisitos de design responsivo
- Requisitos de acessibilidade
- Compatibilidade de navegador/dispositivo
- Padrões de interação do usuário que precisam de implementação
- Requisitos de animação ou transição
- Requisitos de UX para tratamento de erros

**Adicione estes à lista de Requisitos Adicionais.**

### 7. Carregar e Inicializar Modelo

Carregue {epicsTemplate} e inicialize {outputFile}:

1. Copie o modelo inteiro para {outputFile}
2. Substitua {{project_name}} pelo nome real do projeto
3. Substitua seções de placeholder com requisitos extraídos:
   - {{fr_list}} → RFs extraídos
   - {{nfr_list}} → RNFs extraídos
   - {{additional_requirements}} → requisitos adicionais extraídos
4. Deixe {{requirements_coverage_map}} e {{epics_list}} como placeholders por enquanto

### 8. Apresentar Requisitos Extraídos

Exiba para o usuário:

**Requisitos Funcionais Extraídos:**

- Mostre contagem de RFs encontrados
- Exiba os primeiros RFs como exemplos
- Pergunte se algum RF está faltando ou capturado incorretamente

**Requisitos Não-Funcionais Extraídos:**

- Mostre contagem de RNFs encontrados
- Exiba RNFs chave
- Pergunte se alguma restrição foi perdida

**Requisitos Adicionais:**

- Resuma requisitos técnicos da Arquitetura
- Resuma requisitos de UX (se aplicável)
- Verifique completude

### 9. Obter Confirmação do Usuário

Pergunte: "Estes requisitos extraídos representam com precisão o que precisa ser construído? Alguma adição ou correção?"

Atualize os requisitos com base no feedback do usuário até que a confirmação seja recebida.

## CONTEÚDO PARA SALVAR NO DOCUMENTO:

Após extração e confirmação, atualize {outputFile} com:

- Lista completa de RFs na seção {{fr_list}}
- Lista completa de RNFs na seção {{nfr_list}}
- Todos os requisitos adicionais na seção {{additional_requirements}}

### 10. Apresentar OPÇÕES DE MENU

Exibir: `**Confirme que os Requisitos estão completos e corretos para [C] continuar:**`

#### REGRAS DE EXECUÇÃO:

- SEMPRE pare e aguarde a entrada do usuário após apresentar o menu
- APENAS prossiga para o próximo passo quando o usuário selecionar 'C'
- Usuário pode conversar ou fazer perguntas - sempre responda e termine exibindo novamente a opção de menu

#### Lógica de Tratamento de Menu:

- SE C: Salve tudo em {outputFile}, atualize frontmatter, apenas então carregue, leia arquivo inteiro e execute {nextStepFile}
- SE Quaisquer outros comentários ou dúvidas: ajude o usuário a responder e então [Exiba Novamente Opções de Menu](#10-apresentar-opcoes-de-menu)

## NOTA CRÍTICA DE CONCLUSÃO DO PASSO

APENAS QUANDO C for selecionado e todos os requisitos forem salvos no documento e frontmatter for atualizado, você então carregará e lerá completamente `{nextStepFile}` para executar e iniciar o passo de design de épicos.

---

## 🚨 MÉTRICAS DE SUCESSO/FALHA DO SISTEMA

### ✅ SUCESSO:

- Todos os documentos necessários encontrados e validados
- Todos os RFs extraídos e formatados corretamente
- Todos os RNFs extraídos e formatados corretamente
- Requisitos adicionais de Arquitetura/UX identificados
- Modelo inicializado com requisitos
- Usuário confirma que requisitos estão completos e precisos

### ❌ FALHA DO SISTEMA:

- Documentos necessários ausentes
- Extração incompleta de requisitos
- Modelo não inicializado adequadamente
- Não salvar requisitos no arquivo de saída

**Regra Mestra:** Pular passos, otimizar sequências ou não seguir instruções exatas é PROIBIDO e constitui FALHA DO SISTEMA.
