# Passo 2: Geração de Regras de Contexto

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- ✅ Sempre trate isto como uma descoberta colaborativa entre pares técnicos
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS sobre regras não óbvias que os agentes de IA precisam ser lembrados
- 🎯 MANTER O CONTENT LEAN - otimizar para a eficiência de contexto LLM
A velocidade de desenvolvimento da IA mudou fundamentalmente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 📝 Concentre-se em regras específicas e accionáveis em vez de aconselhamento geral
- ⚠
- 💾 APENAS salve quando o usuário escolher C (Continue)
- 📖 Actualizar o material frontal com secções completas
- 🚫 PROIBIDA a carregar o próximo passo até que todas as secções estejam completas

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e apresentar escolhas para cada categoria de regra:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para explorar regras implementation nuances
- **P (Modo de Festa)**: Traga várias perspectivas para identificar casos críticos de borda
- **C (Continua)**: Salve as regras atuais e prossiga para a próxima categoria

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/_bmad/core/workflows/party-mode
- PROTOCOLOS retornam sempre para exibir o menu A/P/C deste passo após o A ou P terem completado
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Os resultados da descoberta da etapa 1 estão disponíveis
- Pilha tecnológica e padrões existentes são identificados
- Foco em regras que impedem erros implementation
- Priorizar detalhes não óbvios que agentes de IA podem perder

A sua tarefa:

Colaborativamente gerar regras específicas e críticas que os agentes de IA devem seguir ao implementar o código neste projeto.

## CONTEXTO GENERAÇÃO SEQUÊNCIA:

### 1. Pilha de tecnologia e versões

Documente a pilha de tecnologia exata da descoberta:

**Core Technologies:**
Com base no nível de habilidade do usuário, apresentam achados:

**Modo de especialista:**
"Pasta de tecnologia de sua arquitetura e arquivos package:
{{exact_technologies_with_versions}}

Alguma restrição de versão crítica que eu deva documentar para agentes?"

**Modo intermediário:**
"Encontrei a sua pilha de tecnologia:

**Core Technologies:**
{{main_technologies_with_versions}}

**Dependências-chave:**
{{important_dependencies_with_versions}}

Há alguma restrição de versão ou os agentes de notas de compatibilidade devem saber sobre?"

**Modo de início:**
"Aqui estão as tecnologias que você está usando:

**Main Technologies:**
{{friendly_description_of_tech_stack}}

**Notas importantes:**
{{key_things_agents_need_to_know_about_versions}}

Devo documentar quaisquer regras especiais de versão ou requisitos de compatibilidade?"

### 2. Regras específicas da língua

Foco em padrões de linguagem não óbvios agentes podem perder:

**TypeScript/JavaScript Rules:**
"Baseado na sua base de códigos, noto alguns padrões específicos:

**Requisitos de configuração:**
{{typescript_config_rules}}

**Padrões de importação/exportação:**
{{import_export_conventions}}

**Padrões de manipulação de erros:**
{{error_handling_requirements}}

Estes padrões estão corretos? Quaisquer outras regras específicas de linguagem que os agentes devem seguir?"

**Python/Ruby/Other Language Rules:**
Adaptar-se à linguagem real em uso com perguntas focais semelhantes.

### 3. Regras específicas-quadro

Padrões específicos do quadro de documentos:

**Regras de reacção (se aplicável):**
"Para o desenvolvimento do React, vejo estes padrões:

**Uso Hooks:**
{{hooks_usage_patterns}}

**Estrutura do componente:**
{{component_organization_rules}}

**Gestão do Estado:**
{{state_management_patterns}}

**Regras de desempenho:**
{{performance_optimization_requirements}}

Devo adicionar outras regras específicas do React?"

**Outras regras-quadro:**
Adaptar para Vue, Angular, Next.js, Express, etc.

### 4. Regras de ensaio

Foco em padrões de teste que garantem consistência:

**Regras de estrutura de teste:**
"Sua configuração de teste mostra estes padrões:

**Organização de Teste:**
{{test_file_organization}}

**Uso Mack:**
{{mock_patterns_and_conventions}}

**Requisitos de cobertura do teste:**
{{coverage_expectations}}

**Regras de integração contra teste unitário:**
{{test_boundary_patterns}}

Há regras de teste que os agentes devem sempre seguir?"

### 5. Regras de qualidade e estilo de código

Documentar regras críticas de estilo e qualidade:

**Linting/Formating:**
"Sua configuração de estilo de código requer:

**ESLint/Prettier Rules:**
{{specific_linting_rules}}

**Organização de Código:**
{{file_and_folder_structure_rules}}

**Convenções de navegação:**
{{naming_patterns_agents_must_follow}}

**Requisitos de documentação:**
{{comment_and_documentation_patterns}}

Alguma regra de qualidade de código adicional?"

### 6. Regras de fluxo de trabalho de desenvolvimento

Padrões de fluxo de trabalho do documento que afetam implementation:

**Regras Git/Repositório:**
"Seu projeto usa estes padrões:

**Branch Naming:**
{{branch_naming_conventions}}

**Commit Message Format:**
{{commit_message_patterns}

**Requisitos PR:**
{{pull request che