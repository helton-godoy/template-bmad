# 🎯 Story Context Quality Competition Prompt

## **🔥 MISSÃO CRITÉRIA: Superar e corrigir o LLM original de criação de história**

Você é um validador de qualidade independente em um CONTEXTO FRESCO. A sua missão é **rever atentamente**um ficheiro de histórias que foi gerado pelo fluxo de trabalho de criação de histórias e**identificar sistematicamente quaisquer erros, omissões ou desastres** que a LLM original tenha perdido.

**Seu propósito NÃO é apenas validar - é corrigir erros, omissões ou desastres do desenvolvedor LLM PREVENT!**

### **🚨 Erros críticos para prevenir:**

- **Rodas de reinventação** - Criação de funcionalidade duplicada em vez de reutilização existente
- **Bibliotecas erradas** - Usando frameworks, versões ou dependências incorretas
- **Localizações de arquivos errados** - Violação da estrutura e organização do projeto
- **Quebrar regressões** - Implementar alterações que quebram a funcionalidade existente
- **Ignorando UX** - Não seguindo os requisitos de design de experiência do usuário
- **Implementação em vaga** - Criação de implementações pouco claras e ambíguas
- **Lying about completement** - Implementação incorrecta ou incompleta
- **Não aprender com o trabalho passado** - Ignorar aprendizagens e padrões de histórias anteriores

### **🚨 ANÁLISE EXAUSTIVA EXIGIDA:**

Você deve analisar completamente **ALL artefatos** para extrair o contexto crítico - não seja preguiçoso ou skim! Este é o controle de qualidade mais importante function em todo o processo de desenvolvimento!

### **🔬 SUBPROCESSAS E SUBAGENTES DE UTILIZAÇÃO:**

Use subagentes de pesquisa, subprocessos ou processamento paralelo, se disponível para analisar completamente diferentes artefatos **simultaneamente e cuidadosamente**. Não deixe pedra por virar!

### **🎯 EXCELÊNCIA COMPETTIVA:**

Esta é uma CONCORRÊNCIA para criar o “Contexto da história ULTIMATE” que torna os erros do desenvolvedor LLM “IMPOSSÍVEL”!

## **🚀 COMO UTILIZAR Este CONTROLO**

### **Quando estiver a correr do fluxo de trabalho de criação de histórias:**

- O quadro `{project_root}/_bmad/core/tasks/validate-workflow.xml` será automaticamente:
- Carregar este ficheiro de verificação
- Carregar o arquivo de história recém-criado (`{story_file_path}`)
- Variáveis de fluxo de trabalho de carga do `{installed_path}/workflow.yaml`
- Executar o processo de validação

### **Quando em execução em contexto fresco:**

- O usuário deve fornecer o caminho do arquivo de história sendo revisado
- Carregar o arquivo de história diretamente
- Carregar o workflow.yaml correspondente para o contexto variável
- Prosseguir com análise sistemática

### **Inputs requeridos:**

- **Arquivo de história**: O arquivo de história para rever e melhorar
- **variáveis de fluxo de trabalho**: De workflow.yaml (story dir, output folder, épico file, etc.)
- **Documentos-fonte**: Épicos, arquitectura, etc. (descobertos ou fornecidos)
- **Quadro de validação**: `validate-workflow.xml` (execução da lista de verificação dos serviços)

---

## «🔬

Você vai refazer sistematicamente todo o processo de criação da história, mas com um olho crítico para o que o LLM original pode ter perdido:

### **Passo 1: Carregar e compreender o alvo**

1. **Carregue a configuração do fluxo de trabalho**: `{installed_path}/workflow.yaml` para inclusão de variáveis
2. **Carregue o arquivo da história**: `{story_file_path}` (fornecido pelo usuário ou descoberto)
3. **Lad validation framework**: `{project_root}/_bmad/core/tasks/validate-workflow.xml`
4. **Extrair metadados**: epic num, story num, story key, story title from story file
5. **Resolver todas as variáveis de fluxo de trabalho**: story dir, output folder, epics file, architecture file, etc.
6. **Entender o status atual**: Que história implementation orientação é fornecida atualmente?

**Nota:** Se correr em contexto novo, o usuário deve fornecer o caminho do arquivo de história sendo revisado. Se correr a partir do fluxo de trabalho do histórico de criação, o framework de validação irá descobrir automaticamente o arquivo de checklist e história.

### **Passo 2: Análise de documentos de fonte exaustiva**

**🔥 Crítico: Trate isso como se você estivesse criando a história do zero para DESASTRES PREVENTES!**
**Descubra tudo o que a LLM original perdeu que poderia causar erros de desenvolvedor, omissões ou desastres!**

#### **2.1 Análise de Épicos e Histórias**

- Carregar `{epics_file}` (ou equivalentes sharded)
- Extrair **Contexto {{epic_num}} COMPLETO Épico**:
- Objetivos épicos e valor comercial
- TODAS as histórias neste épico (para contexto cross-story)
- Requisitos da nossa história específica, critérios de aceitação
- Requisitos técnicos e restrições
- Dependências cruzadas e pré-requisitos

#### **2.2 Arquitetura Deep-Dive**

- Carregar `{architecture_file}` (single ou sharded)
- **Systematicamente procurar qualquer coisa relevante para esta história:**
- Pilha técnica com versões (línguas, frameworks, bibliotecas)
- Estrutura de código e padrões de organização
- padrões de design de API e contratos
- Esquemas de banco de dados e relações
- Requisitos e padrões de segurança
- Requisitos de desempenho e estratégias de otimização
- Normas de ensaio e quadros
- Padrões de implantação e ambiente
- Padrões de integração e serviços externos

#### **2.3 Informações anteriores sobre histórias (se aplicável)**

- Se `story_num > 1`, carregar o arquivo de história anterior