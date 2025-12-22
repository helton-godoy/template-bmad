# Instruções de verificação completa do projeto

<workflow>

<critical>Este fluxo de trabalho executa documentação completa do projeto (Passos 1-12)</critical>
<critical>Chamada por: document-project/instructions.md roteador </critical>
Modos <critical>Handles: initial_scan e full rescan </critical>

<step n="0.5" goal="Load documentation requirements data for fresh starts (not needed for resume)" if="resume_mode == false">
<critical>ATA ESTRATÉGIA DE EMBARQUE - Compreender o Sistema de Requisitos de Documentação:</critical>

<action>Explicação para o utilizador:

**Como funciona a detecção do tipo de projeto:**

Este fluxo de trabalho usa um único arquivo CSV abrangente para documentar inteligentemente seu projeto:

**documentation-requirements.csv** ({documentation_requirements_csv})

- Contém 12 tipos de projeto (web, mobile, backend, cli, biblioteca, desktop, jogo, dados, extensão, infra, incorporado)
- esquema de 24 colunas combinando detecção de tipo de projecto E requisitos de documentação
- **Columns Detection**: project type id, key file patterns (usado para identificar o tipo de projecto a partir da base de código)
- **Colunas de exigência**: require api scan, require data models, require ui components, etc.
- **Colunas de padrão**: directórios críticos, padrões teste, padrões config, etc.
- Atua como um "guia de varredura" - diz ao fluxo de trabalho ONDE procurar e O que documentar
- Example: Para project type id="web", key file padterns inclui "package.json;tsconfig.json;\*.config.js" e requires api scan=true

**Quando os requisitos de documentação são carregados:**

- **Fresh Start (inicial scan)**: Carregar todas as 12 linhas → detectar tipo usando key file patterns → usar os requisitos dessa linha
- **Resumir**: Carregar SOMENTE a(s) linha(s) de requisitos doc para 'project type id(s) em cache
- **Full Rescan**: O mesmo que o início novo (pode re-detectar o tipo de projecto)
- **Deep Dive**: Carregar SOMENTE requisitos de documento para a parte que está mergulhada
</action>

<action>Now carregando dados de requisitos de documentação para começar de novo...</action>

<action>Load documentation-requirements.csv de: {documentation_requirements_csv}BADPROTECT054END
<action>Store todas as 12 linhas indexadas por project type id para detecção de projetos e procura de requisitos</action>
<action>Exibição: "Requisitos de documentação carregados para 12 tipos de projeto (web, móvel, backend, cli, biblioteca, desktop, jogo, dados, extensão, infra, incorporado)"</action>

<action>Display: "✓ Requisitos de documentação carregados com sucesso. Pronto para começar a análise do projeto. " </action>
</step>

<step n="0.6" goal="Check for existing documentation and determine workflow mode">
<action> Verifique se {output_folder}/index.md existe</action>

<check if="index.md exists">
<action>Leia o index.md existente para extrair metadados (data, estrutura do projeto, contagem de peças)</action>
<action>Store como BMADPROTECT080End}, BMADPROTECT079End}BMADPROTECT039End

<ask>I encontrou documentação existente gerada no {{existing_doc_date}}.

O que gostarias de fazer?

1. **Re-scan projeto inteiro** - Atualizar toda a documentação com as últimas alterações
2. **Deep-dive em área específica** - Gerar documentação detalhada para um determinado recurso/módulo/pasta
3. **Cancelar** - Manter a documentação existente como está

A sua escolha [1/2/3]:
</ask>

<check if="user selects 1">
<action>Set workflow mode = "full rescan"</action>
<action>Continue a analisar a seleção do nível abaixo do </action>
</check>

<check if="user selects 2">
<action>Set workflow mode = "deep dive"BMADPROTECT028End
<action>Set scan level = "exaustive" </action>
<action>Iniciar arquivo de estado com mod=deep dive, scan level=exhaustive</action>
BMADPROTECT023EndJump to Step 13BMADPROTECT022End
</check>

<check if="user selects 3">
BMADPROTECT019EndDisplay message: "Mantendo a documentação existente. A sair do fluxo de trabalho. " </action>
BMADPROTECT017EndExit workflow</action>
</check>
</check>

<check if="index.md does not exist">
<action>Set workflow mode = "inicial scan"</action>
<action>Continue a analisar a seleção do nível abaixo do </action>
</check>

<action if="workflow_mode != deep_dive"> Scan Level</action>

<check if="workflow_mode == initial_scan OR workflow_mode == full_rescan">
<ask> Escolha o seu nível de profundidade de digitalização:

**1. Exame rápido** (2-5 minutos) [DEFAULT]

- Análise baseada em padrões sem ler arquivos fonte
- Scans: Arquivos de configuração, manifestos package, estrutura de diretórios
- Melhor para: Visão geral rápida do projeto, compreensão inicial
- Leitura de arquivos: Mínimo (configurações, README, package.json, etc.)

**2. Deep Scan** (10-30 minutos)

- Lê arquivos em diretórios críticos com base no tipo de projeto
- Scans: Todos os caminhos críticos dos requisitos de documentação
- Melhor para: Documentação abrangente para brownfield PRD
- Leitura de arquivos: Seletivo (arquivos de chaves em diretórios críticos)

**3. Exaustive Scan** (30-120 minutos)

- Lê TODOS os ficheiros de código no projecto
- Scans: Cada ficheiro de código (exclui os módulos de nó, dist, build)
- Melhor para: Análise completa, migração planning, auditoria detalhada
- Leitura do arquivo: Completa (todos os arquivos de origem)

Sua escolha [1/2/3] (padrão: 1):
</ask>

<action if="user selects 1 OR user presses enter">
<action>Set scan leve