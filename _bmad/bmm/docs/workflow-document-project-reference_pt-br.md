# Document Project Workflow - Referência Técnica

**Módulo:** BMM (módulo de método BMAD)
**Tipo:** Fluxo de trabalho de ação (Gerador de documentação)

---

## Purpose

Analyzes and documents brownfield projects by scanning codebase, architecture, and patterns to create comprehensive reference documentation for AI-assisted development. Generates a master index and multiple documentation files tailored to project structure and type.

**NEW in v1.2.0:** Context-safe architecture with scan levels, resumability, and write-as-you-go pattern to prevent context exhaustion.

---

## Características Principais

- **Multi-Project Type Support**: Lida com projetos web, backend, mobile, CLI, game, incorporado, data, infra, biblioteca, desktop e extensão
- **Detecção de várias partes**: Detecta e documenta automaticamente projectos com cliente/servidor separado ou vários serviços
- **Três Níveis de Varredura** (NOVO v1.2.2): Rápido (2-5 min), Profundo (10-30 min), Exaustivo (30-120 min)
- **Resumibilidade** (NOVO v1.2.2): Interromper e retomar os fluxos de trabalho sem perder o progresso
- **Write-as-you-go** (NOVO v1.2.2): Documentos escritos imediatamente para evitar o esgotamento do contexto
- **Intelligent Batching** (NOVO v1.2.2): Processamento baseado em subpastas para análises profundas/exaustivas
- **Análise de Dados**: utiliza os requisitos de detecção e documentação de tipo de projecto baseados em CSV
- **Examinagem compreensiva**: Analisa APIs, modelos de dados, componentes de interface, configuração, padrões de segurança e muito mais
- **Architecture Matching**: Combina projetos com modelos de arquitetura 170+ do registro de solução
- **Brownfield PRD Ready**: Gera documentação especificamente concebida para agentes de IA planning novas funcionalidades

---

## How to Invoke

```bash
workflow document-project

```

Or from BMAD CLI:

```bash
/bmad:bmm:workflows:document-project

```

---

## Níveis de digitalização (NOVO em v1.2.2)

Escolha a profundidade de varredura certa para suas necessidades:

### 1. Pesquisa Rápida (Padrão)

**Duração:** 2-5 minutos
**O que faz:** Análise baseada em padrões sem ler arquivos fonte
**Leia:** Arquivos de configuração, package manifesta, estrutura de diretório, README
**Usar quando:**

- Você precisa de uma visão rápida do projeto
- Compreensão inicial da estrutura do projeto
- PlanningER os próximos passos antes de uma análise mais profunda

**Não se lê:** Arquivos de código fonte (`_.js`, `_.ts`, `_.py`, `_.go`, etc.)

### 2.

**Duração:** 10-30 minutos
**O que faz:** Lê ficheiros em pastas críticas com base no tipo de projecto
**Leia:** Arquivos em caminhos críticos definidos pelos requisitos de documentação
**Usar quando:**

- Criação de documentação abrangente para PRD brownfield
- Precisa de análise detalhada das áreas-chave
- Quero equilíbrio entre profundidade e velocidade

**Exemplo:** Para uma aplicação Web, lê controladores/, modelos/, componentes/, mas não todos os ficheiros utilitários

### 3. Exaustive Scan

**Duração:** 30-120 minutos
**O que faz:** Lê TODOS os ficheiros de código no projecto
**Leia:** Cada arquivo de código fonte (exclui nó módulos, dist, build, .git)
**Usar quando:**

- Análise completa do projeto necessária
- Migração planning requer compreensão completa
- Auditoria detalhada de toda a base de códigos
- Avaliação profunda da dívida técnica

**Nota:** Modo de mergulho profundo SEMPRE usa varredura exaustiva (sem escolha)

---

## Resumability (NEW in v1.2.0)

The workflow can be interrupted and resumed without losing progress:

- **State Tracking:** Progress saved in `project-scan-report.json`
- **Auto-Detection:** Workflow detects incomplete runs (<24 hours old)
- **Resume Prompt:** Choose to resume or start fresh
- **Step-by-Step:** Resume from exact step where interrupted
- **Archiving:** Old state files automatically archived

**Example Resume Flow:**

```
> workflow document-project

I found an in-progress workflow state from 2025-10-11 14:32:15.

Current Progress:
- Mode: initial_scan
- Scan Level: deep
- Completed Steps: 5/12
- Last Step: step_5

Would you like to:
1. Resume from where we left off - Continue from step 6
2. Start fresh - Archive old state and begin new scan
3. Cancel - Exit without changes

Your choice [1/2/3]:

```

---

## O que faz

### Processo passo a passo

1. **Detects Project Structure** - Identifica se o projecto é uma única parte ou multi-parte (cliente/servidor/etc.)
2. **Classifica Tipo de Projecto** - Corresponde com 12 tipos de projecto (web, infra-estrutura, telemóvel, etc.)
3. **Descubra a Documentação** - Encontra os ficheiros existentes README, CONTRIBUIÇÃO, ARQUITETURA
4. **Analyzes Tech Stack** - Processar arquivos package, identifica frameworks, versões, dependências
5. **Conditional Scanning** - Realiza análise orientada com base nos requisitos do tipo de projecto:
- Rotas de API e terminais
- Modelos de banco de dados e esquemas
- Padrões de gestão do Estado
- Bibliotecas de componentes de UI
- Configuração e segurança
- Configurações CI/CD e implantação
6. **Gerates Source Tree** - Cria uma estrutura de diretório anotada com caminhos críticos
7. **Extracts Dev Instructions** - Configuração de documentos, compilação, execução e comandos de teste
8. **Cria Documentos de Arquitetura** - Gera arquitetura detalhada usando modelos combinados
9. **Construi o índice mestre** - Cria i abrangente