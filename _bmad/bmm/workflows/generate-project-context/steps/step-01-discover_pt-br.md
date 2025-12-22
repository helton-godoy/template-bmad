# Passo 1: Descoberta de Contexto e Inicialização

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário
- ✅ Sempre trate isto como uma descoberta colaborativa entre pares técnicos
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS para descobrir o contexto do projeto existente e a pilha de tecnologia
- 🎯 IDENTIFY critica implementation regras que os agentes de IA necessitam
A velocidade de desenvolvimento da IA mudou fundamentalmente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 📖 Leia os arquivos de projeto existentes para entender o contexto atual
- 💾 Inicializar documento e atualizar frontmatter
- 🚫 PROIBIDA a carregar o próximo passo até que a descoberta esteja completa

## CONTEXTO MONTANTES:

- Variáveis de workflow.md estão disponíveis na memória
- Foco em arquivos de projeto existentes e decisões de arquitetura
- Procure padrões, convenções e requisitos únicos
- Priorizar regras que previnem erros implementation

A sua tarefa:

Descubra a pilha de tecnologia do projeto, padrões existentes e regras críticas implementation que os agentes de IA devem seguir ao escrever código.

## DESCOVERY SEQUÊNCIA:

### 1. Verificar o Contexto do Projeto existente

Primeiro, verifique se o contexto do projeto já existe:

- Procura o ficheiro no `{output_folder}/project-context.md`
- Se existe: Leia o arquivo completo para entender as regras existentes
- Presente ao usuário: "Encontrado contexto de projeto existente com {number_of_sections} seções. Você gostaria de atualizar isso ou criar um novo?"

### 2. Discover Project Technology Stack

Carregar e analisar arquivos de projeto para identificar tecnologias:

**Documento de arquitectura:**

- Procure `{output_folder}/architecture.md`
- Opções de tecnologia de extração com versões específicas
- Note decisões arquitetônicas que afetam implementation

**Arquivos de embalagem:**

- Verificação do `package.json`, `requirements.txt`, `Cargo.toml`, etc.
- Extrair versões exatas de todas as dependências
- Note desenvolvimento vs dependências de produção

**Arquivos de configuração:**

- Procure a configuração do TypeScript (`tsconfig.json`)
- Configuração da ferramenta de compilação (webpack, vite, a seguir. config.js, etc.)
- Configurações de forro e formatação (.eslintrc, .prettierrc, etc.)
- Configuração de teste (jest.config.js, vitest.config.ts, etc.)

### 3. Identificar os padrões de código existentes

Procurar por padrões existentes na base de códigos:

**Convenções de navegação:**

- Padrões de nomes de ficheiros (PascalCase, kebab-case, etc.)
- Convenções de nomenclatura Componente/function
- Padrões de nomenclatura de variáveis
- Teste padrões de nomeação de arquivos

**Organização de Código:**

- Como os componentes são estruturados
- Onde são colocados utilitários e ajudantes
- Como os serviços são organizados
- Teste padrões de organização

**Padrões de documentação:**

- Estilos de comentários e convenções
- Requisitos de documentação
- Padrões de documento README e API

### 4. Extrair Implementation crítico Regras

Procure por regras que os agentes de IA podem perder:

**Regras específicas da língua:**

- Requisitos de modo rígido TypeScript
- Convenções de importação/export
- Assync/await vs Promessa padrões de uso
- Erro no tratamento de padrões específicos do idioma

**Regras específicas da obra:**

- Reagir ganchos padrões de uso
- Convenções de rotas API
- Padrões de uso do Middleware
- Padrões de gestão do Estado

**Regras de Teste:**

- Requisitos da estrutura de ensaio
- Convenções de uso de farsa
- Limites de integração vs teste unitário
- Requisitos de cobertura

**Regras de fluxo de trabalho de desenvolvimento:**

- Convenções de nomeação de ramos
- Enviar padrões de mensagens
- Requisitos de revisão PR
- Procedimentos de implantação

### 5. Inicializar o Documento de Contexto do Projeto

Com base na descoberta, criar ou atualizar o documento de contexto:

#### A. Nova Configuração do Documento (se não existir um contexto)

Modelo de cópia do `{installed_path}/project-context-template.md` para `{output_folder}/project-context.md`
Inicializar o material frontal com:

```yaml
---
project_name: '{{project_name}}'
user_name: '{{user_name}}'
date: '{{date}}'
sections_completed: ['technology_stack']
existing_patterns_found: { { number_of_patterns_discovered } }
---

```

#### B. Actualização do documento existente

Carregar o contexto existente e preparar-se para atualizações
Definir a matéria frontal `sections_completed` para rastrear o que será atualizado

### 6. Apresentar Resumo da Descoberta

Comunique as conclusões ao usuário:

Bem-vindo BMADPROTECT035nd}! Analisei seu projeto para {{project_name}} para descobrir o contexto que agentes de IA precisam.

**Technology Stack Discovered:**
{{list_of_technologies_with_versions}}

**Existem padrões encontrados:**

- {{number_of_patterns}} implementation padrões
- Convenções de codificação {{number_of_conventions}}
- {{number_of_rules}} regras críticas

**Áreas-chave para regras de contexto:**

- {{area_1}} (por exemplo, configuração TypeScript)
- {{area_2}} (por exemplo, testes padrões)
- {{area_3}} (por exemplo, organização de códigos)

{if_existing_context}
**Contexto existente:** Encontradas seções {{sections}} já definidas. Podemos atualizar ou adicionar a estes.
{/if_existing_context}

Pronto para criar/atualizar o contexto do seu projeto. Isso ajudará os agentes de IA a implementar código consistentemente com os padrões do seu projeto.

[C] Continuar a geração de contexto"

## SUCE