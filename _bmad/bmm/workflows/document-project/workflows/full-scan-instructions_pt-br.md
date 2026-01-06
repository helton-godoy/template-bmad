# Instruções de Varredura Completa do Projeto

<workflow>

<critical>Este fluxo de trabalho realiza a documentação completa do projeto (Passos 1-12)</critical>
<critical>Chamado por: document-project/instructions.md router</critical>
<critical>Lida com: modos initial_scan e full_rescan</critical>

<step n="0.5" goal="Carregar dados de requisitos de documentação para inícios frescos (não necessário para retomada)" if="resume_mode == false">
<critical>ESTRATÉGIA DE CARREGAMENTO DE DADOS - Entendendo o Sistema de Requisitos de Documentação:</critical>

<action>Exibir explicação para o usuário:

**Como Funciona a Detecção de Tipo de Projeto:**

Este fluxo de trabalho usa um único arquivo CSV abrangente para documentar inteligentemente seu projeto:

**documentation-requirements.csv** ({documentation_requirements_csv})

- Contém 12 tipos de projeto (web, mobile, backend, cli, library, desktop, game, data, extension, infra, embedded)
- Esquema de 24 colunas combinando detecção de tipo de projeto E requisitos de documentação
- **Colunas de detecção**: project_type_id, key_file_patterns (usado para identificar tipo de projeto da base de código)
- **Colunas de requisito**: requires_api_scan, requires_data_models, requires_ui_components, etc.
- **Colunas de padrão**: critical_directories, test_file_patterns, config_patterns, etc.
- Atua como um "guia de varredura" - diz ao fluxo de trabalho ONDE olhar e O QUE documentar
- Exemplo: Para project_type_id="web", key_file_patterns inclui "package.json;tsconfig.json;*.config.js" e requires_api_scan=true

**Quando Requisitos de Documentação são Carregados:**

- **Início Fresco (initial_scan)**: Carregar todas as 12 linhas → detectar tipo usando key_file_patterns → usar requisitos dessa linha
- **Retomada**: Carregar APENAS a(s) linha(s) de requisitos de doc para project_type_id(s) em cache
- **Re-escanear Completo**: Igual ao início fresco (pode re-detectar tipo de projeto)
- **Mergulho Profundo**: Carregar APENAS requisitos de doc para a parte sendo mergulhada
  </action>

<action>Agora carregando dados de requisitos de documentação para início fresco...</action>

<action>Carregar documentation-requirements.csv de: {documentation_requirements_csv}</action>
<action>Armazenar todas as 12 linhas indexadas por project_type_id para detecção de projeto e pesquisa de requisitos</action>
<action>Exibir: "Carregados requisitos de documentação para 12 tipos de projeto (web, mobile, backend, cli, library, desktop, game, data, extension, infra, embedded)"</action>

<action>Exibir: "✓ Requisitos de documentação carregados com sucesso. Pronto para começar análise do projeto."</action>
</step>

<step n="0.6" goal="Verificar por documentação existente e determinar modo de fluxo de trabalho">
<action>Verificar se {output_folder}/index.md existe</action>

<check if="index.md exists">
  <action>Ler index.md existente para extrair metadados (data, estrutura do projeto, contagem de partes)</action>
  <action>Armazenar como {{existing_doc_date}}, {{existing_structure}}</action>

<ask>Encontrei documentação existente gerada em {{existing_doc_date}}.

O que você gostaria de fazer?

1. **Re-escanear projeto inteiro** - Atualizar toda a documentação com as últimas mudanças
2. **Mergulho profundo em área específica** - Gerar documentação detalhada para um recurso/módulo/pasta particular
3. **Cancelar** - Manter documentação existente como está

Sua escolha [1/2/3]:
</ask>

  <check if="user selects 1">
    <action>Definir workflow_mode = "full_rescan"</action>
    <action>Continuar para seleção de nível de varredura abaixo</action>
  </check>

  <check if="user selects 2">
    <action>Definir workflow_mode = "deep_dive"</action>
    <action>Definir scan_level = "exhaustive"</action>
    <action>Inicializar arquivo de estado com mode=deep_dive, scan_level=exhaustive</action>
    <action>Pular para Passo 13</action>
  </check>

  <check if="user selects 3">
    <action>Exibir mensagem: "Mantendo documentação existente. Saindo do fluxo de trabalho."</action>
    <action>Sair do fluxo de trabalho</action>
  </check>
</check>

<check if="index.md does not exist">
  <action>Definir workflow_mode = "initial_scan"</action>
  <action>Continuar para seleção de nível de varredura abaixo</action>
</check>

<action if="workflow_mode != deep_dive">Selecionar Nível de Varredura</action>

<check if="workflow_mode == initial_scan OR workflow_mode == full_rescan">
  <ask>Escolha seu nível de profundidade de varredura:

**1. Varredura Rápida** (2-5 minutos) [PADRÃO]

- Análise baseada em padrões sem ler arquivos de código fonte
- Varre: Arquivos de configuração, manifestos de pacote, estrutura de diretório
- Melhor para: Visão geral rápida do projeto, entendimento inicial
- Leitura de arquivo: Mínima (configs, README, package.json, etc.)

**2. Varredura Profunda** (10-30 minutos)

- Lê arquivos em diretórios críticos com base no tipo de projeto
- Varre: Todos os caminhos críticos dos requisitos de documentação
- Melhor para: Documentação abrangente para PRD brownfield
- Leitura de arquivo: Seletiva (arquivos chave em diretórios críticos)

**3. Varredura Exaustiva** (30-120 minutos)

- Lê TODOS os arquivos de código fonte no projeto
- Varre: Cada arquivo de código fonte (exclui node_modules, dist, build)
- Melhor para: Análise completa, planejamento de migração, auditoria detalhada
- Leitura de arquivo: Completa (todos os arquivos de código fonte)

Sua escolha [1/2/3] (padrão: 1):
</ask>

  <action if="user selects 1 OR user presses enter">
    <action>Definir scan_level = "quick"</action>
    <action>Exibir: "Usando Varredura Rápida (baseada em padrões, sem leitura de arquivo de código fonte)"</action>
  </action>

  <action if="user selects 2">
    <action>Definir scan_level = "deep"</action>
    <action>Exibir: "Usando Varredura Profunda (lendo arquivos críticos por tipo de projeto)"</action>
  </action>

  <action if="user selects 3">
    <action>Definir scan_level = "exhaustive"</action>
    <action>Exibir: "Usando Varredura Exaustiva (lendo todos os arquivos de código fonte)"</action>
  </action>

<action>Inicializar arquivo de estado: {output_folder}/project-scan-report.json</action>
<critical>Toda vez que você tocar no arquivo de estado, registre: step id, resumo legível por humanos (o que você realmente fez), timestamp preciso, e quaisquer saídas escritas. Frases vagas são inaceitáveis.</critical>
<action>Escrever estado inicial:
{
"workflow_version": "1.2.0",
"timestamps": {"started": "{{current_timestamp}}", "last_updated": "{{current_timestamp}}"},
"mode": "{{workflow_mode}}",
"scan_level": "{{scan_level}}",
"project_root": "{{project_root_path}}",
"output_folder": "{{output_folder}}",
"completed_steps": [],
"current_step": "step_1",
"findings": {},
"outputs_generated": ["project-scan-report.json"],
"resume_instructions": "Começando do passo 1"
}
</action>
<action>Continuar com fluxo de trabalho padrão do Passo 1</action>
</check>
</step>

<step n="1" goal="Detectar estrutura do projeto e classificar tipo de projeto" if="workflow_mode != deep_dive">
<action>Perguntar ao usuário: "Qual é o diretório raiz do projeto para documentar?" (padrão: diretório de trabalho atual)</action>
<action>Armazenar como {{project_root_path}}</action>

<action>Varrer {{project_root_path}} por indicadores chave:

- Estrutura de diretório (presença de client/, server/, api/, src/, app/, etc.)
- Arquivos chave (package.json, go.mod, requirements.txt, etc.)
- Marcadores de tecnologia correspondendo a detection_keywords de project-types.csv
  </action>

<action>Detectar se projeto é:

- **Monólito**: Base de código coesa única
- **Monorepo**: Múltiplas partes em um repositório
- **Multi-parte**: Arquitetura cliente/servidor separada ou similar
  </action>

<check if="multiple distinct parts detected (e.g., client/ and server/ folders)">
  <action>Listar partes detectadas com seus caminhos</action>
  <ask>Detectei múltiplas partes neste projeto:
  {{detected_parts_list}}

Isso está correto? Devo documentar cada parte separadamente? [s/n]
</ask>

<action if="user confirms">Definir repository_type = "monorepo" ou "multi-part"</action>
<action if="user confirms">Para cada parte detectada: - Identificar caminho raiz - Rodar detecção de tipo de projeto usando key_file_patterns de documentation-requirements.csv - Armazenar como parte no array project_parts
</action>

<action if="user denies or corrects">Pedir ao usuário para especificar partes corretas e seus caminhos</action>
</check>

<check if="single cohesive project detected">
  <action>Definir repository_type = "monolith"</action>
  <action>Criar parte única no array project_parts com root_path = {{project_root_path}}</action>
  <action>Rodar detecção de tipo de projeto usando key_file_patterns de documentation-requirements.csv</action>
</check>

<action>Para cada parte, corresponder tecnologias detectadas e padrões de arquivo contra coluna key_file_patterns em documentation-requirements.csv</action>
<action>Atribuir project_type_id para cada parte</action>
<action>Carregar linha documentation_requirements correspondente para cada parte</action>

<ask>Eu classifiquei este projeto:
{{project_classification_summary}}

Isso parece correto? [s/n/editar]
</ask>

<template-output>project_structure</template-output>
<template-output>project_parts_metadata</template-output>

<action>IMEDIATAMENTE atualizar arquivo de estado com conclusão de passo:

- Adicionar a completed_steps: {"step": "step_1", "status": "completed", "timestamp": "{{now}}", "summary": "Classificado como {{repository_type}} com {{parts_count}} partes"}
- Atualizar current_step = "step_2"
- Atualizar findings.project_classification com resumo de alto nível apenas
- **CACHE project_type_id(s)**: Adicionar array project_types: [{"part_id": "{{part_id}}", "project_type_id": "{{project_type_id}}", "display_name": "{{display_name}}"}]
- Esses dados em cache evitam recarregar todos os arquivos CSV na retomada - podemos carregar apenas a(s) linha(s) documentation_requirements necessária(s)
- Atualizar timestamp last_updated
- Escrever arquivo de estado
  </action>

<action>PURGAR resultados detalhados de varredura da memória, manter apenas resumo: "{{repository_type}}, {{parts_count}} partes, {{primary_tech}}"</action>
</step>

<step n="2" goal="Descobrir documentação existente e reunir contexto do usuário" if="workflow_mode != deep_dive">
<action>Para cada parte, varrer por documentação existente usando padrões:
- README.md, README.rst, README.txt
- CONTRIBUTING.md, CONTRIBUTING.rst
- ARCHITECTURE.md, ARCHITECTURE.txt, docs/architecture/
- DEPLOYMENT.md, DEPLOY.md, docs/deployment/
- API.md, docs/api/
- Quaisquer arquivos em pastas docs/, documentation/, .github/
</action>

<action>Criar inventário de existing_docs com:

- Caminho do arquivo
- Tipo de arquivo (readme, architecture, api, etc.)
- A qual parte pertence (se multi-parte)
  </action>

<ask>Encontrei estes arquivos de documentação existentes:
{{existing_docs_list}}

Existem outros documentos importantes ou áreas chave em que devo focar enquanto analiso este projeto? [Forneça caminhos ou orientação, ou digite 'nenhum']
</ask>

<action>Armazenar orientação do usuário como {{user_context}}</action>

<template-output>existing_documentation_inventory</template-output>
<template-output>user_provided_context</template-output>

<action>Atualizar arquivo de estado:

- Adicionar a completed_steps: {"step": "step_2", "status": "completed", "timestamp": "{{now}}", "summary": "Encontrado {{existing_docs_count}} docs existentes"}
- Atualizar current_step = "step_3"
- Atualizar timestamp last_updated
  </action>

<action>PURGAR conteúdos detalhados de doc da memória, manter apenas: "{{existing_docs_count}} docs encontrados"</action>
</step>

<step n="3" goal="Analisar pilha tecnológica para cada parte" if="workflow_mode != deep_dive">
<action>Para cada parte em project_parts:
  - Carregar key_file_patterns de documentation_requirements
  - Varrer raiz da parte por esses padrões
  - Analisar arquivos de manifesto de tecnologia (package.json, go.mod, requirements.txt, etc.)
  - Extrair: framework, linguagem, versão, banco de dados, dependências
  - Construir technology_table com colunas: Categoria, Tecnologia, Versão, Justificativa
</action>

<action>Determinar padrão de arquitetura com base na pilha tecnológica detectada:

- Usar project_type_id como indicador primário (e.g., "web" → layered/component-based, "backend" → service/API-centric)
- Considerar padrões de framework (e.g., React → hierarquia de componentes, Express → pipeline de middleware)
- Notar estilo arquitetural na tabela de tecnologia
- Armazenar como {{architecture_pattern}} para cada parte
  </action>

<template-output>technology_stack</template-output>
<template-output>architecture_patterns</template-output>

<action>Atualizar arquivo de estado:

- Adicionar a completed_steps: {"step": "step_3", "status": "completed", "timestamp": "{{now}}", "summary": "Pilha técnica: {{primary_framework}}"}
- Atualizar current_step = "step_4"
- Atualizar findings.technology_stack com resumo por parte
- Atualizar timestamp last_updated
  </action>

<action>PURGAR análise detalhada de tecnologia da memória, manter apenas: "{{framework}} em {{language}}"</action>
</step>

<step n="4" goal="Realizar análise condicional com base nos requisitos de tipo de projeto" if="workflow_mode != deep_dive">

<critical>ESTRATÉGIA DE LOTEAMENTO PARA VARREDURAS PROFUNDAS/EXAUSTIVAS</critical>

<check if="scan_level == deep OR scan_level == exhaustive">
  <action>Este passo requer leitura de arquivo. Aplicar estratégia de loteamento:</action>

<action>Identificar subpastas para processar com base em: - scan_level == "deep": Usar critical_directories de documentation_requirements - scan_level == "exhaustive": Obter TODAS as subpastas recursivamente (excluindo node_modules, .git, dist, build, coverage)
</action>

<action>Para cada subpasta para varrer: 1. Ler todos os arquivos na subpasta (considerar tamanho do arquivo - usar julgamento para arquivos >5000 LOC) 2. Extrair informações necessárias com base em sinalizadores condicionais abaixo 3. IMEDIATAMENTE escrever descobertas para arquivo de saída apropriado 4. Validar documento escrito (validação nível de seção) 5. Atualizar arquivo de estado com conclusão de lote 6. PURGAR descobertas detalhadas do contexto, manter apenas resumo de 1-2 frases 7. Mover para próxima subpasta
</action>

<action>Rastrear lotes no arquivo de estado:
findings.batches_completed: [
{"path": "{{subfolder_path}}", "files_scanned": {{count}}, "summary": "{{brief_summary}}"}
]
</action>
</check>

<check if="scan_level == quick">
  <action>Usar correspondência de padrão apenas - NÃO ler arquivos de código fonte</action>
  <action>Usar glob/grep para identificar localizações de arquivo e padrões</action>
  <action>Extrair informações de nomes de arquivo, estrutura de diretório e arquivos de configuração apenas</action>
</check>

<action>Para cada parte, verificar sinalizadores booleanos documentation_requirements e executar varreduras correspondentes:</action>

<check if="requires_api_scan == true">
  <action>Varrer por rotas de API e endpoints usando integration_scan_patterns</action>
  <action>Procurar por: controllers/, routes/, api/, handlers/, endpoints/</action>

  <check if="scan_level == quick">
    <action>Usar glob para encontrar arquivos de rota, extrair padrões de nomes de arquivo e estrutura de pasta</action>
  </check>

  <check if="scan_level == deep OR scan_level == exhaustive">
    <action>Ler arquivos em lotes (uma subpasta por vez)</action>
    <action>Extrair: métodos HTTP, caminhos, tipos de requisição/resposta do código real</action>
  </check>

<action>Construir catálogo de contratos de API</action>
<action>IMEDIATAMENTE escrever para: {output_folder}/api-contracts-{part_id}.md</action>
<action>Validar documento tem todas as seções necessárias</action>
<action>Atualizar arquivo de estado com saída gerada</action>
<action>PURGAR dados detalhados de API, manter apenas: "{{api_count}} endpoints documentados"</action>
<template-output>api_contracts\*{part_id}</template-output>
</check>

<check if="requires_data_models == true">
  <action>Varrer por modelos de dados usando schema_migration_patterns</action>
  <action>Procurar por: models/, schemas/, entities/, migrations/, prisma/, ORM configs</action>

  <check if="scan_level == quick">
    <action>Identificar arquivos de esquema via glob, analisar nomes de arquivo de migração para descoberta de tabela</action>
  </check>

  <check if="scan_level == deep OR scan_level == exhaustive">
    <action>Ler arquivos de modelo em lotes (uma subpasta por vez)</action>
    <action>Extrair: nomes de tabela, campos, relacionamentos, restrições do código real</action>
  </check>

<action>Construir documentação de esquema de banco de dados</action>
<action>IMEDIATAMENTE escrever para: {output_folder}/data-models-{part_id}.md</action>
<action>Validar completude do documento</action>
<action>Atualizar arquivo de estado com saída gerada</action>
<action>PURGAR dados detalhados de esquema, manter apenas: "{{table_count}} tabelas documentadas"</action>
<template-output>data_models\*{part_id}</template-output>
</check>

<check if="requires_state_management == true">
  <action>Analisar padrões de gerenciamento de estado</action>
  <action>Procurar por: Redux, Context API, MobX, Vuex, Pinia, padrões Provider</action>
  <action>Identificar: stores, reducers, actions, estrutura de estado</action>
  <template-output>state_management_patterns_{part_id}</template-output>
</check>

<check if="requires_ui_components == true">
  <action>Inventariar biblioteca de componentes UI</action>
  <action>Varrer: pastas components/, ui/, widgets/, views/</action>
  <action>Categorizar: Layout, Form, Display, Navigation, etc.</action>
  <action>Identificar: Sistema de design, padrões de componente, elementos reutilizáveis</action>
  <template-output>ui_component_inventory_{part_id}</template-output>
</check>

<check if="requires_hardware_docs == true">
  <action>Procurar por esquemas de hardware usando hardware_interface_patterns</action>
  <ask>Este parece ser um projeto embarcado/hardware. Você tem:
  - Diagramas de pinagem
  - Esquemas de hardware
  - Layouts de PCB
  - Documentação de hardware

Se sim, por favor forneça caminhos ou links. [Forneça caminhos ou digite 'nenhum']
</ask>
<action>Armazenar referências de docs de hardware</action>
<template-output>hardware*documentation*{part_id}</template-output>
</check>

<check if="requires_asset_inventory == true">
  <action>Varrer e catalogar ativos usando asset_patterns</action>
  <action>Categorizar por: Imagens, Áudio, Modelos 3D, Sprites, Texturas, etc.</action>
  <action>Calcular: Tamanho total, contagens de arquivo, formatos usados</action>
  <template-output>asset_inventory_{part_id}</template-output>
</check>

<action>Varrer por padrões adicionais com base em requisitos de doc:

- config_patterns → Gerenciamento de configuração
- auth_security_patterns → Abordagem de autenticação/autorização
- entry_point_patterns → Pontos de entrada de aplicação e bootstrap
- shared_code_patterns → Bibliotecas compartilhadas e utilitários
- async_event_patterns → Arquitetura orientada a eventos
- ci_cd_patterns → Detalhes de pipeline CI/CD
- localization_patterns → Suporte i18n/l10n
  </action>

<action>Aplicar estratégia scan_level para cada varredura de padrão (quick=glob apenas, deep/exhaustive=ler arquivos)</action>

<template-output>comprehensive*analysis*{part_id}</template-output>

<action>Atualizar arquivo de estado:

- Adicionar a completed_steps: {"step": "step_4", "status": "completed", "timestamp": "{{now}}", "summary": "Análise condicional completa, {{files_generated}} arquivos escritos"}
- Atualizar current_step = "step_5"
- Atualizar timestamp last_updated
- Listar todas outputs_generated
  </action>

<action>PURGAR todos os resultados detalhados de varredura do contexto. Manter apenas resumos:

- "APIs: {{api_count}} endpoints"
- "Dados: {{table_count}} tabelas"
- "Componentes: {{component_count}} componentes"
  </action>
  </step>

<step n="5" goal="Gerar análise de árvore de código com anotações" if="workflow_mode != deep_dive">
<action>Para cada parte, gerar árvore de diretório completa usando critical_directories de requisitos de doc</action>

<action>Anotar a árvore com:

- Propósito de cada diretório crítico
- Pontos de entrada marcados
- Localizações de arquivos chave destacadas
- Pontos de integração notados (para projetos multi-parte)
  </action>

<action if="multi-part project">Mostrar como partes são organizadas e onde elas interagem</action>

<action>Criar árvore de código formatada com descrições:

```
project-root/
├── client/          # React frontend (Parte: client)
│   ├── src/
│   │   ├── components/  # Componentes UI reutilizáveis
│   │   ├── pages/       # Páginas baseadas em rota
│   │   └── api/         # Camada cliente API → Chama server/
├── server/          # Express API backend (Parte: api)
│   ├── src/
│   │   ├── routes/      # Endpoints API REST
│   │   ├── models/      # Modelos de banco de dados
│   │   └── services/    # Lógica de negócio
```

</action>

<template-output>source_tree_analysis</template-output>
<template-output>critical_folders_summary</template-output>

<action>IMEDIATAMENTE escrever source-tree-analysis.md para disco</action>
<action>Validar estrutura do documento</action>
<action>Atualizar arquivo de estado:

- Adicionar a completed_steps: {"step": "step_5", "status": "completed", "timestamp": "{{now}}", "summary": "Árvore de código documentada"}
- Atualizar current_step = "step_6"
- Adicionar saída: "source-tree-analysis.md"
  </action>
  <action>PURGAR árvore detalhada do contexto, manter apenas: "Árvore de código com {{folder_count}} pastas críticas"</action>
  </step>

<step n="6" goal="Extrair informações de desenvolvimento e operacionais" if="workflow_mode != deep_dive">
<action>Varrer por configuração de desenvolvimento usando key_file_patterns e docs existentes:
- Pré-requisitos (Versão Node, Versão Python, etc.)
- Passos de instalação (npm install, etc.)
- Configuração de ambiente (arquivos .env, config)
- Comandos de build (npm run build, make, etc.)
- Comandos de execução (npm start, go run, etc.)
- Comandos de teste usando test_file_patterns
</action>

<action>Procurar por configuração de implantação usando ci_cd_patterns:

- Dockerfile, docker-compose.yml
- Configs Kubernetes (k8s/, helm/)
- Pipelines CI/CD (.github/workflows/, .gitlab-ci.yml)
- Scripts de implantação
- Infraestrutura como Código (terraform/, pulumi/)
  </action>

<action if="CONTRIBUTING.md or similar found">
  <action>Extrair diretrizes de contribuição:
    - Regras de estilo de código
    - Processo de PR
    - Convenções de commit
    - Requisitos de teste
  </action>
</action>

<template-output>development_instructions</template-output>
<template-output>deployment_configuration</template-output>
<template-output>contribution_guidelines</template-output>

<action>Atualizar arquivo de estado:

- Adicionar a completed_steps: {"step": "step_6", "status": "completed", "timestamp": "{{now}}", "summary": "Guias Dev/implantação escritos"}
- Atualizar current_step = "step_7"
- Adicionar saídas geradas à lista
  </action>
  <action>PURGAR instruções detalhadas, manter apenas: "Configuração dev e implantação documentados"</action>
  </step>

<step n="7" goal="Detectar arquitetura de integração multi-parte" if="workflow_mode != deep_dive and project has multiple parts">
<action>Analisar como partes se comunicam:
- Varrer integration_scan_patterns através das partes
- Identificar: chamadas REST, consultas GraphQL, gRPC, filas de mensagem, bancos de dados compartilhados
- Documentar: contratos de API entre partes, fluxo de dados, fluxo de autenticação
</action>

<action>Criar array integration_points com:

- from: parte fonte
- to: parte alvo
- type: API REST, GraphQL, gRPC, Barramento de Evento, etc.
- details: Endpoints, protocolos, formatos de dados
  </action>

<action>IMEDIATAMENTE escrever integration-architecture.md para disco</action>
<action>Validar completude do documento</action>

<template-output>integration_architecture</template-output>

<action>Atualizar arquivo de estado:

- Adicionar a completed_steps: {"step": "step_7", "status": "completed", "timestamp": "{{now}}", "summary": "Arquitetura de integração documentada"}
- Atualizar current_step = "step_8"
  </action>
  <action>PURGAR detalhes de integração, manter apenas: "{{integration_count}} pontos de integração"</action>
  </step>

<step n="8" goal="Gerar documentação de arquitetura para cada parte" if="workflow_mode != deep_dive">
<action>Para cada parte em project_parts:
  - Usar modelo de arquitetura correspondente do Passo 3 como estrutura base
  - Preencher todas as seções com informações descobertas:
    * Resumo Executivo
    * Pilha Tecnológica (do Passo 3)
    * Padrão de Arquitetura (da correspondência de registro)
    * Arquitetura de Dados (da varredura de modelos de dados do Passo 4)
    * Design de API (da varredura de API do Passo 4 se aplicável)
    * Visão Geral de Componentes (da varredura de componentes do Passo 4 se aplicável)
    * Árvore de Código (do Passo 5)
    * Fluxo de Trabalho de Desenvolvimento (do Passo 6)
    * Arquitetura de Implantação (do Passo 6)
    * Estratégia de Teste (de padrões de teste)
</action>

<action if="single part project">
  - Gerar: architecture.md (sem sufixo de parte)
</action>

<action if="multi-part project">
  - Gerar: architecture-{part_id}.md para cada parte
</action>

<action>Para cada arquivo de arquitetura gerado:

- IMEDIATAMENTE escrever arquivo de arquitetura para disco
- Validar contra esquema de modelo de arquitetura
- Atualizar arquivo de estado com saída
- PURGAR arquitetura detalhada do contexto, manter apenas: "Arquitetura para {{part_id}} escrita"
  </action>

<template-output>architecture_document</template-output>

<action>Atualizar arquivo de estado:

- Adicionar a completed_steps: {"step": "step_8", "status": "completed", "timestamp": "{{now}}", "summary": "Docs de arquitetura escritos para {{parts_count}} partes"}
- Atualizar current_step = "step_9"
  </action>
  </step>

<step n="9" goal="Gerar arquivos de documentação de suporte" if="workflow_mode != deep_dive">
<action>Gerar project-overview.md com:
- Nome e propósito do projeto (do README ou entrada do usuário)
- Resumo executivo
- Tabela resumo de pilha técnica
- Classificação de tipo de arquitetura
- Estrutura de repositório (monólito/monorepo/multi-parte)
- Links para docs detalhadas
</action>

<action>Gerar source-tree-analysis.md com:

- Árvore de diretório anotada completa do Passo 5
- Pastas críticas explicadas
- Pontos de entrada documentados
- Estrutura multi-parte (se aplicável)
  </action>

<action>IMEDIATAMENTE escrever project-overview.md para disco</action>
<action>Validar seções do documento</action>

<action>Gerar source-tree-analysis.md (se não já escrito no Passo 5)</action>
<action>IMEDIATAMENTE escrever para disco e validar</action>

<action>Gerar component-inventory.md (ou versões por parte) com:

- Todos os componentes descobertos do Passo 4
- Categorizados por tipo
- Componentes reutilizáveis vs específicos
- Elementos de sistema de design (se encontrados)
  </action>
  <action>IMEDIATAMENTE escrever cada inventário de componente para disco e validar</action>

<action>Gerar development-guide.md (ou versões por parte) com:

- Pré-requisitos e dependências
- Instruções de configuração de ambiente
- Comandos de desenvolvimento local
- Processo de build
- Abordagem de teste e comandos
- Tarefas comuns de desenvolvimento
  </action>
  <action>IMEDIATAMENTE escrever cada guia de desenvolvimento para disco e validar</action>

<action if="deployment configuration found">
  <action>Gerar deployment-guide.md com:
    - Requisitos de infraestrutura
    - Processo de implantação
    - Configuração de ambiente
    - Detalhes de pipeline CI/CD
  </action>
  <action>IMEDIATAMENTE escrever para disco e validar</action>
</action>

<action if="contribution guidelines found">
  <action>Gerar contribution-guide.md com:
    - Estilo de código e convenções
    - Processo de PR
    - Requisitos de teste
    - Padrões de documentação
  </action>
  <action>IMEDIATAMENTE escrever para disco e validar</action>
</action>

<action if="API contracts documented">
  <action>Gerar api-contracts.md (ou por parte) com:
    - Todos os endpoints de API
    - Esquemas de requisição/resposta
    - Requisitos de autenticação
    - Requisições de exemplo
  </action>
  <action>IMEDIATAMENTE escrever para disco e validar</action>
</action>

<action if="Data models documented">
  <action>Gerar data-models.md (ou por parte) com:
    - Esquema de banco de dados
    - Relacionamentos de tabela
    - Modelos de dados e entidades
    - Estratégia de migração
  </action>
  <action>IMEDIATAMENTE escrever para disco e validar</action>
</action>

<action if="multi-part project">
  <action>Gerar integration-architecture.md com:
    - Como partes se comunicam
    - Diagrama/descrição de pontos de integração
    - Fluxo de dados entre partes
    - Dependências compartilhadas
  </action>
  <action>IMEDIATAMENTE escrever para disco e validar</action>

<action>Gerar arquivo de metadados project-parts.json:
`json
    {
      "repository_type": "monorepo",
      "parts": [ ... ],
      "integration_points": [ ... ]
    }
    `
</action>
<action>IMEDIATAMENTE escrever para disco</action>
</action>

<template-output>supporting_documentation</template-output>

<action>Atualizar arquivo de estado:

- Adicionar a completed_steps: {"step": "step_9", "status": "completed", "timestamp": "{{now}}", "summary": "Todas as docs de suporte escritas"}
- Atualizar current_step = "step_10"
- Listar todas as saídas recém geradas
  </action>

<action>PURGAR todos os conteúdos de documento do contexto, manter apenas lista de arquivos gerados</action>
</step>

<step n="10" goal="Gerar índice mestre como fonte primária de recuperação de IA" if="workflow_mode != deep_dive">

<critical>CONVENÇÃO DE MARCADOR DE DOCUMENTAÇÃO INCOMPLETA:
Quando um documento DEVERIA ser gerado mas não foi (devido a varredura rápida, dados ausentes, requisitos condicionais não atendidos):

- Use EXATAMENTE este marcador: _(To be generated)_
- Coloque-o no final da linha de link markdown
- Exemplo: - [Contratos de API - Servidor](./api-contracts-server.md) _(To be generated)_
- Isso permite que o Passo 11 detecte e ofereça completar esses itens
- SEMPRE use este formato exato para consistência e detecção automatizada
  </critical>

<action>Criar index.md com navegação inteligente baseada na estrutura do projeto</action>

<action if="single part project">
  <action>Gerar índice simples com:
    - Nome e tipo do projeto
    - Referência rápida (pilha técnica, tipo de arquitetura)
    - Links para todas as docs geradas
    - Links para docs existentes descobertas
    - Seção de começando
  </action>
</action>

<action if="multi-part project">
  <action>Gerar índice abrangente com:
    - Visão geral do projeto e resumo da estrutura
    - Seção de navegação baseada em parte
    - Referência rápida por parte
    - Links de integração entre partes
    - Links para todas as docs geradas e existentes
    - Começando por parte
  </action>
</action>

<action>Incluir em index.md:

## Índice de Documentação do Projeto

### Visão Geral do Projeto

- **Tipo:** {{repository_type}} {{#if multi-part}}com {{parts.length}} partes{{/if}}
- **Linguagem Primária:** {{primary_language}}
- **Arquitetura:** {{architecture_type}}

### Referência Rápida

{{#if single_part}}

- **Pilha Técnica:** {{tech_stack_summary}}
- **Ponto de Entrada:** {{entry_point}}
- **Padrão de Arquitetura:** {{architecture_pattern}}
  {{else}}
  {{#each parts}}

#### {{part_name}} ({{part_id}})

- **Tipo:** {{project_type}}
- **Pilha Técnica:** {{tech_stack}}
- **Raiz:** {{root_path}}
  {{/each}}
  {{/if}}

### Documentação Gerada

- [Visão Geral do Projeto](./project-overview.md)
- [Arquitetura](./architecture{{#if multi-part}}-{part\*id}{{/if}}.md){{#unless architecture_file_exists}} (To be generated) {{/unless}}
- [Análise da Árvore de Código](./source-tree-analysis.md)
- [Inventário de Componentes](./component-inventory{{#if multi-part}}-{part\*id}{{/if}}.md){{#unless component_inventory_exists}} (To be generated) {{/unless}}
- [Guia de Desenvolvimento](./development-guide{{#if multi-part}}-{part\*id}{{/if}}.md){{#unless dev_guide_exists}} (To be generated) {{/unless}}
  {{#if deployment_found}}- [Guia de Implantação](./deployment-guide.md){{#unless deployment_guide_exists}} (To be generated) {{/unless}}{{/if}}
  {{#if contribution_found}}- [Guia de Contribuição](./contribution-guide.md){{/if}}
  {{#if api_documented}}- [Contratos de API](./api-contracts{{#if multi-part}}-{part_id}{{/if}}.md){{#unless api_contracts_exists}} (To be generated) {{/unless}}{{/if}}
  {{#if data_models_documented}}- [Modelos de Dados](./data-models{{#if multi-part}}-{part_id}{{/if}}.md){{#unless data_models_exists}} (To be generated) {{/unless}}{{/if}}
  {{#if multi-part}}- [Arquitetura de Integração](./integration-architecture.md){{#unless integration_arch_exists}} (To be generated) {{/unless}}{{/if}}

### Documentação Existente

{{#each existing_docs}}

- [{{title}}]({{relative_path}}) - {{description}}
  {{/each}}

### Começando

{{getting_started_instructions}}
</action>

<action>Antes de escrever index.md, verificar quais arquivos esperados realmente existem:

- Para cada documento que deveria ter sido gerado, verificar se arquivo existe no disco
- Definir sinalizadores de existência: architecture_file_exists, component_inventory_exists, dev_guide_exists, etc.
- Esses sinalizadores determinam se deve adicionar o marcador _(To be generated)_
- Rastrear quais arquivos estão faltando em {{missing_docs_list}} para relatório
  </action>

<action>IMEDIATAMENTE escrever index.md para disco com marcadores _(To be generated)_ apropriados para arquivos ausentes</action>
<action>Validar índice tem todas as seções necessárias e links são válidos</action>

<template-output>index</template-output>

<action>Atualizar arquivo de estado:

- Adicionar a completed_steps: {"step": "step_10", "status": "completed", "timestamp": "{{now}}", "summary": "Índice mestre gerado"}
- Atualizar current_step = "step_11"
- Adicionar saída: "index.md"
  </action>

<action>PURGAR conteúdo do índice do contexto</action>
</step>

<step n="11" goal="Validar e revisar documentação gerada" if="workflow_mode != deep_dive">
<action>Mostrar resumo de todos os arquivos gerados:
Gerado em {{output_folder}}/:
{{file_list_with_sizes}}
</action>

<action>Rodar checklist de validação de {validation}</action>

<critical>DETECÇÃO DE DOCUMENTAÇÃO INCOMPLETA:

1. VARREDURA PRIMÁRIA: Procurar por marcador exato: _(To be generated)_
2. VARREDURA DE RETROCESSO: Procurar por padrões difusos (caso agente tenha sido preguiçoso):
   - _(TBD)_
   - _(TODO)_
   - _(Em breve)_
   - _(Ainda não gerado)_
   - _(Pendente)_
3. Extrair metadados do documento de cada correspondência para seleção do usuário
   </critical>

<action>Ler {output_folder}/index.md</action>

<action>Varrer por marcadores de documentação incompleta:
Passo 1: Pesquisar por padrão exato "_(To be generated)_" (case-sensitive)
Passo 2: Para cada correspondência encontrada, extrair a linha inteira
Passo 3: Analisar linha para extrair:

- Título do documento (texto dentro de [colchetes] ou **negrito**)
- Caminho do arquivo (de link markdown ou inferível do título)
- Tipo de documento (inferir do nome do arquivo: architecture, api-contracts, data-models, component-inventory, development-guide, deployment-guide, integration-architecture)
- ID da parte se aplicável (extrair de nome de arquivo como "architecture-server.md" → part_id: "server")
  Passo 4: Adicionar ao array {{incomplete_docs_strict}}
  </action>

<action>Varredura difusa de retrocesso para marcadores alternativos:
Pesquisar por padrões: _(TBD)_, _(TODO)_, _(Em breve)_, _(Ainda não gerado)_, _(Pendente)_
Para cada correspondência difusa:

- Extrair mesmos metadados que varredura estrita
- Adicionar ao array {{incomplete_docs_fuzzy}} com sinalizador fuzzy_match
  </action>

<action>Combinar resultados:
Definir {{incomplete_docs_list}} = {{incomplete_docs_strict}} + {{incomplete_docs_fuzzy}}
Para cada item armazenar estrutura:
{
"title": "Arquitetura – Servidor",
"file\*path": "./architecture-server.md",
"doc_type": "architecture",
"part_id": "server",
"line_text": "- [Arquitetura – Servidor](./architecture-server.md) (To be generated)",
"fuzzy_match": false
}
</action>

<ask>Geração de documentação completa!

Resumo:

- Tipo de Projeto: {{project_type_summary}}
- Partes Documentadas: {{parts_count}}
- Arquivos Gerados: {{files_count}}
- Total de Linhas: {{total_lines}}

{{#if incomplete_docs_list.length > 0}}
⚠️ **Documentação Incompleta Detectada:**

Encontrei {{incomplete_docs_list.length}} item(ns) marcados como incompletos:

{{#each incomplete_docs_list}}
{{@index + 1}}. **{{title}}** ({{doc_type}}{{#if part_id}} para {{part_id}}{{/if}}){{#if fuzzy_match}} ⚠️ [marcador não padrão]{{/if}}
{{/each}}

{{/if}}

Você gostaria de:

{{#if incomplete_docs_list.length > 0}}

1. **Gerar documentação incompleta** - Completar quaisquer dos {{incomplete_docs_list.length}} itens acima
2. Revisar qualquer seção específica [digite nome da seção]
3. Adicionar mais detalhes a qualquer área [digite nome da área]
4. Gerar documentação personalizada adicional [descreva o que]
5. Finalizar e completar [digite 'feito']
   {{else}}
6. Revisar qualquer seção específica [digite nome da seção]
7. Adicionar mais detalhes a qualquer área [digite nome da área]
8. Gerar documentação adicional [descreva o que]
9. Finalizar e completar [digite 'feito']
   {{/if}}

Sua escolha:
</ask>

<check if="user selects option 1 (generate incomplete)">
  <ask>Quais itens incompletos você gostaria de gerar?

{{#each incomplete_docs_list}}
{{@index + 1}}. {{title}} ({{doc_type}}{{#if part_id}} - {{part_id}}{{/if}})
{{/each}}
{{incomplete_docs_list.length + 1}}. Todos eles

Insira número(s) separados por vírgulas (e.g., "1,3,5"), ou digite 'todos':
</ask>

<action>Analisar seleção do usuário:

- Se "todos", definir {{selected_items}} = todos itens em {{incomplete_docs_list}}
- Se números separados por vírgula, extrair itens selecionados por índice
- Armazenar resultado no array {{selected_items}}
  </action>

  <action>Exibir: "Gerando {{selected_items.length}} documento(s)..."</action>

  <action>Para cada item em {{selected_items}}:

1. **Identificar a parte e requisitos:**
   - Extrair part_id do item (se existir)
   - Consultar dados da parte no array project_parts do arquivo de estado
   - Carregar documentation_requirements para o project_type_id dessa parte

2. **Roteador para subpasso de geração apropriado baseado em doc_type:**

   **Se doc_type == "architecture":**
   - Exibir: "Gerando documentação de arquitetura para {{part_id}}..."
   - Carregar architecture_match para esta parte do arquivo de estado (Passo 3 cache)
   - Re-executar lógica de geração de arquitetura do Passo 8 APENAS para esta parte específica
   - Usar modelo correspondente e preencher com dados em cache do arquivo de estado
   - Escrever architecture-{{part_id}}.md para disco
   - Validar completude

   **Se doc_type == "api-contracts":**
   - Exibir: "Gerando contratos de API para {{part_id}}..."
   - Carregar dados da parte e documentation_requirements
   - Re-executar subpasso de varredura de API do Passo 4 visando APENAS esta parte
   - Usar scan_level do arquivo de estado (rápido/profundo/exaustivo)
   - Gerar api-contracts-{{part_id}}.md
   - Validar estrutura do documento

   **Se doc_type == "data-models":**
   - Exibir: "Gerando documentação de modelos de dados para {{part_id}}..."
   - Re-executar subpasso de varredura de modelos de dados do Passo 4 visando APENAS esta parte
   - Usar schema_migration_patterns de documentation_requirements
   - Gerar data-models-{{part_id}}.md
   - Validar completude

   **Se doc_type == "component-inventory":**
   - Exibir: "Gerando inventário de componentes para {{part_id}}..."
   - Re-executar geração de inventário de componentes do Passo 9 para esta parte específica
   - Varrer pastas components/, ui/, widgets/
   - Gerar component-inventory-{{part_id}}.md
   - Validar estrutura

   **Se doc_type == "development-guide":**
   - Exibir: "Gerando guia de desenvolvimento para {{part_id}}..."
   - Re-executar geração de guia de desenvolvimento do Passo 9 para esta parte específica
   - Usar key_file_patterns e test_file_patterns de documentation_requirements
   - Gerar development-guide-{{part_id}}.md
   - Validar completude

   **Se doc_type == "deployment-guide":**
   - Exibir: "Gerando guia de implantação..."
   - Re-executar varredura de configuração de implantação do Passo 6
   - Re-executar geração de guia de implantação do Passo 9
   - Gerar deployment-guide.md
   - Validar estrutura

   **Se doc_type == "integration-architecture":**
   - Exibir: "Gerando arquitetura de integração..."
   - Re-executar análise de integração do Passo 7 para todas as partes
   - Gerar integration-architecture.md
   - Validar completude

3. **Ações pós-geração:**
   - Confirmar que arquivo foi escrito com sucesso
   - Atualizar arquivo de estado com saída recém gerada
   - Adicionar à lista de rastreamento {{newly_generated_docs}}
   - Exibir: "✓ Gerado: {{file_path}}"

4. **Tratar erros:**
   - Se geração falhar, registrar erro e continuar com próximo item
   - Rastrear itens falhos na lista {{failed_generations}}
     </action>

<action>Depois que todos os itens selecionados forem processados:

**Atualizar index.md para remover marcadores:**

1. Ler conteúdo atual de index.md
2. Para cada item em {{newly_generated_docs}}:
   - Encontrar a linha contendo o link do arquivo e marcador
   - Remover o texto _(To be generated)_ ou marcador difuso
   - Deixar o link markdown intacto
3. Escrever index.md atualizado de volta para o disco
4. Atualizar arquivo de estado para registrar modificação de index.md
   </action>

<action>Exibir resumo de geração:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ **Geração de Documentação Completa!**

**Gerado com Sucesso:**
{{#each newly_generated_docs}}

- {{title}} → {{file_path}}
  {{/each}}

{{#if failed_generations.length > 0}}
**Falha ao Gerar:**
{{#each failed_generations}}

- {{title}} ({{error_message}})
  {{/each}}
  {{/if}}

**Atualizado:** index.md (marcadores incompletos removidos)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
</action>

<action>Atualizar arquivo de estado com todas as atividades de geração</action>

<action>Retornar ao menu do Passo 11 (loop de volta para verificar quaisquer itens incompletos restantes)</action>
</check>

<action if="user requests other changes (options 2-3)">Fazer modificações solicitadas e regenerar arquivos afetados</action>
<action if="user selects finalize (option 4 or 5)">Prosseguir para conclusão do Passo 12</action>

<check if="not finalizing">
  <action>Atualizar arquivo de estado:
- Adicionar a completed_steps: {"step": "step_11_iteration", "status": "completed", "timestamp": "{{now}}", "summary": "Iteração de revisão completa"}
- Manter current_step = "step_11" (para loop de volta)
- Atualizar timestamp last_updated
  </action>
  <action>Loop de volta para início do Passo 11 (re-escanear para docs incompletos restantes)</action>
</check>

<check if="finalizing">
  <action>Atualizar arquivo de estado:
- Adicionar a completed_steps: {"step": "step_11", "status": "completed", "timestamp": "{{now}}", "summary": "Validação e revisão completas"}
- Atualizar current_step = "step_12"
  </action>
  <action>Prosseguir para Passo 12</action>
</check>
</step>

<step n="12" goal="Finalizar e fornecer próximos passos" if="workflow_mode != deep_dive">
<action>Criar relatório de resumo final</action>
<action>Compilar variáveis de recapitulação de verificação:
  - Definir {{verification_summary}} para os testes concretos, validações ou scripts que você executou (ou "nenhum rodado").
  - Definir {{open_risks}} para quaisquer riscos restantes ou acompanhamentos TODO (ou "nenhum").
  - Definir {{next_checks}} para ações recomendadas antes de mesclar/implantar (ou "nenhum").
</action>

<action>Exibir mensagem de conclusão:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Documentação de Projeto Completa! ✓

**Localização:** {{output_folder}}/

**Índice Mestre:** {{output_folder}}/index.md
👆 Este é seu ponto de entrada primário para desenvolvimento assistido por IA

**Documentação Gerada:**
{{generated_files_list}}

**Próximos Passos:**

1. Revise o index.md para se familiarizar com a estrutura da documentação
2. Ao criar um PRD brownfield, aponte o fluxo de trabalho de PRD para: {{output_folder}}/index.md
3. Para recursos apenas UI: Referência {{output_folder}}/architecture-{{ui_part_id}}.md
4. Para recursos apenas API: Referência {{output_folder}}/architecture-{{api_part_id}}.md
5. Para recursos full-stack: Referência arquiteturas de ambas partes + integration-architecture.md

**Recapitulação de Verificação:**

- Testes/extrações executados: {{verification_summary}}
- Riscos pendentes ou acompanhamentos: {{open_risks}}
- Próximas verificações recomendadas antes de PR: {{next_checks}}

**Comando de PRD Brownfield:**
Quando pronto para planejar novos recursos, execute o fluxo de trabalho PRD e forneça este índice como entrada.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
</action>

<action>FINALIZAR arquivo de estado:

- Adicionar a completed_steps: {"step": "step_12", "status": "completed", "timestamp": "{{now}}", "summary": "Fluxo de trabalho completo"}
- Atualizar timestamps.completed = "{{now}}"
- Atualizar current_step = "completed"
- Escrever arquivo de estado final
  </action>

<action>Exibir: "Arquivo de estado salvo: {{output_folder}}/project-scan-report.json"</action>

</workflow>
