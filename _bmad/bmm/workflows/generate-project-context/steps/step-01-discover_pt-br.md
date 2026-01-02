# Passo 1: Descoberta e Inicialização de Contexto

## REGRAS DE EXECUÇÃO OBRIGATÓRIAS (LEIA PRIMEIRO):

- 🛑 NUNCA gere conteúdo sem entrada do usuário
- ✅ SEMPRE trate isso como descoberta colaborativa entre pares técnicos
- 📋 VOCÊ É UM FACILITADOR, não um gerador de conteúdo
- 💬 FOQUE em descobrir o contexto do projeto existente e a pilha de tecnologia
- 🎯 IDENTIFIQUE regras de implementação críticas que agentes de IA precisam
- ⚠️ ABSOLUTAMENTE NENHUMA ESTIMATIVA DE TEMPO - a velocidade de desenvolvimento de IA mudou fundamentalmente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 📖 Leia arquivos de projeto existentes para entender o contexto atual
- 💾 Inicialize o documento e atualize o frontmatter
- 🚫 PROIBIDO carregar o próximo passo até que a descoberta esteja completa

## LIMITES DE CONTEXTO:

- Variáveis do workflow.md estão disponíveis na memória
- Foque em arquivos de projeto existentes e decisões de arquitetura
- Procure por padrões, convenções e requisitos únicos
- Priorize regras que previnam erros de implementação

## SUA TAREFA:

Descobrir a pilha de tecnologia do projeto, padrões existentes e regras de implementação críticas que os agentes de IA devem seguir ao escrever código.

## SEQUÊNCIA DE DESCOBERTA:

### 1. Verificar Contexto de Projeto Existente

Primeiro, verifique se o contexto do projeto já existe:

- Procure por arquivo em `{output_folder}/project-context.md`
- Se existir: Leia o arquivo completo para entender as regras existentes
- Apresente ao usuário: "Encontrei contexto de projeto existente com {number_of_sections} seções. Você gostaria de atualizar isso ou criar um novo?"

### 2. Descobrir Pilha de Tecnologia do Projeto

Carregue e analise arquivos de projeto para identificar tecnologias:

**Documento de Arquitetura:**

- Procure por `{output_folder}/architecture.md`
- Extraia escolhas de tecnologia com versões específicas
- Note decisões arquitetônicas que afetam a implementação

**Arquivos de Pacote:**

- Verifique `package.json`, `requirements.txt`, `Cargo.toml`, etc.
- Extraia versões exatas de todas as dependências
- Note dependências de desenvolvimento vs produção

**Arquivos de Configuração:**

- Procure por configuração TypeScript (`tsconfig.json`)
- Configs de ferramentas de build (webpack, vite, next.config.js, etc.)
- Configs de linting e formatação (.eslintrc, .prettierrc, etc.)
- Configurações de teste (jest.config.js, vitest.config.ts, etc.)

### 3. Identificar Padrões de Código Existentes

Pesquise através da base de código existente por padrões:

**Convenções de Nomenclatura:**

- Padrões de nomenclatura de arquivo (PascalCase, kebab-case, etc.)
- Convenções de nomenclatura de componente/função
- Padrões de nomenclatura de variável
- Padrões de nomenclatura de arquivo de teste

**Organização de Código:**

- Como os componentes são estruturados
- Onde utilitários e helpers são colocados
- Como serviços são organizados
- Padrões de organização de teste

**Padrões de Documentação:**

- Estilos e convenções de comentários
- Requisitos de documentação
- Padrões de README e doc de API

### 4. Extrair Regras de Implementação Críticas

Procure por regras que agentes de IA podem perder:

**Regras Específicas de Linguagem:**

- Requisitos de modo estrito TypeScript
- Convenções de importação/exportação
- Padrões de uso Async/await vs Promise
- Padrões de tratamento de erro específicos para a linguagem

**Regras Específicas de Framework:**

- Padrões de uso de hooks React
- Convenções de rota de API
- Padrões de uso de middleware
- Padrões de gerenciamento de estado

**Regras de Teste:**

- Requisitos de estrutura de teste
- Convenções de uso de mock
- Limites de teste de integração vs unitário
- Requisitos de cobertura

**Regras de Fluxo de Trabalho de Desenvolvimento:**

- Convenções de nomenclatura de branch
- Padrões de mensagem de commit
- Requisitos de revisão de PR
- Procedimentos de implantação

### 5. Inicializar Documento de Contexto do Projeto

Com base na descoberta, crie ou atualize o documento de contexto:

#### A. Configuração de Documento Novo (se nenhum contexto existente)

Copie modelo de `{installed_path}/project-context-template_pt-br.md` para `{output_folder}/project-context.md`
Inicialize frontmatter com:

```yaml
---
project_name: '{{project_name}}'
user_name: '{{user_name}}'
date: '{{date}}'
sections_completed: ['technology_stack']
existing_patterns_found: { { number_of_patterns_discovered } }
---
```

#### B. Atualização de Documento Existente

Carregue contexto existente e prepare para atualizações
Defina frontmatter `sections_completed` para rastrear o que será atualizado

### 6. Apresentar Resumo da Descoberta

Relate descobertas ao usuário:

"Bem-vindo {{user_name}}! Analisei seu projeto para {{project_name}} para descobrir o contexto que os agentes de IA precisam.

**Pilha de Tecnologia Descoberta:**
{{list_of_technologies_with_versions}}

**Padrões Existentes Encontrados:**

- {{number_of_patterns}} padrões de implementação
- {{number_of_conventions}} convenções de codificação
- {{number_of_rules}} regras críticas

**Áreas Chave para Regras de Contexto:**

- {{area_1}} (ex: configuração TypeScript)
- {{area_2}} (ex: padrões de Teste)
- {{area_3}} (ex: organização de Código)

{if_existing_context}
**Contexto Existente:** Encontradas {{sections}} seções já definidas. Podemos atualizar ou adicionar a estas.
{/if_existing_context}

Pronto para criar/atualizar seu contexto de projeto. Isso ajudará agentes de IA a implementar código consistentemente com os padrões do seu projeto.

[C] Continuar para geração de contexto"

## MÉTRICAS DE SUCESSO:

✅ Contexto de projeto existente devidamente detectado e tratado
✅ Pilha de tecnologia identificada com precisão com versões
✅ Padrões de implementação críticos descobertos
✅ Documento de contexto do projeto devidamente inicializado
✅ Descobertas claramente apresentadas ao usuário
✅ Usuário pronto para prosseguir com geração de contexto

## MODOS DE FALHA:

❌ Não verificar contexto de projeto existente antes de criar novo
❌ Faltar versões ou configurações de tecnologia críticas
❌ Ignorar padrões ou convenções de codificação importantes
❌ Não inicializar frontmatter adequadamente
❌ Não apresentar resumo claro de descoberta ao usuário

## PRÓXIMO PASSO:

Após o usuário selecionar [C] para continuar, carregue `./step-02-generate_pt-br.md` para gerar colaborativamente as regras de contexto de projeto específicas.

Lembre-se: NÃO prossiga para o step-02 até que o usuário selecione explicitamente [C] do menu e a descoberta esteja completa!
