# Document Project Workflow - Lista de Verificação de Validação

## Nível de digitalização e Resumebilidade (v1.2.2)

- [ ] Scan seleção de nível oferecido (rápido/deep/exaustive) para inicial scan e full rescan modos
- [ ] Modo de mergulho profundo automaticamente usa varredura exaustiva (sem escolha dada)
- [ ] Pesquisa rápida não lê arquivos de origem (somente padrões, configurações, manifestos)
- [ ] Deep scan lê arquivos em diretórios críticos por tipo de projeto
- [ ] Exaustive scan lê ALL source files (excluindo nó módulos, dist, build)
- [ ] Arquivo de estado (project-scan-report.json) criado no início do fluxo de trabalho
- [ ] Arquivo de estado atualizado após cada etapa de conclusão
- [ ] O ficheiro de estado contém todos os campos obrigatórios por esquema
- [ ] Prompt de recuperação mostrado se o arquivo de estado existe e é <24 hours old
- [ ] Old state files (>24 horas) automaticamente arquivado
- [ ] Continuar a funcionalidade carrega o estado anterior corretamente
- [ ] Fluxo de trabalho pode saltar para corrigir o passo ao retomar

## Write-as-you-go Arquitetura

- [ ] Cada documento escrito no disco imediatamente após a geração
- [ ] Validação do documento realizada logo após a escrita (nível de secção)
- [ ] Arquivo de estado atualizado após cada documento ser escrito
- [ ] Resultados detalhados apagados do contexto após a escrita (apenas resumos mantidos)
- [ ] Contexto contém apenas resumos de alto nível (1-2 frases por seção)
- [ ] Sem acumulação de análise completa do projeto na memória

## Estratégia de contracção (exames profundos/exaustivos)

- [ ] Batting aplicado para níveis de varredura profunda e exaustiva
- [ ] Batches organizados por SUBFOLDER (não contagem arbitrária de arquivos)
- [ ] Arquivos grandes (>5000 LOC) tratados com julgamento adequado
- [ ] Cada lote: ler arquivos, extrair informações, gravar saída, validar, limpar contexto
- [ ] Completação de lote rastreada no arquivo de estado (array batchs completed)
- [ ] Resumos em lote mantidos no contexto (1-2 frases máx.)

## Detecção e Classificação do Projecto

- [ ] Tipo de projeto corretamente identificado e corresponde à pilha de tecnologia real
- [ ] Multi-parte vs estrutura de uma só parte detectada com precisão
- [ ] Todas as partes do projeto identificadas se multi-parte (sem cliente em falta/servidor/etc.)
- [ ] Requisitos de documentação carregados para cada tipo de peça
- [ ] Match de registro de arquitetura é apropriado para pilha detectada

## Análise da pilha de tecnologia

- [ ] Todas as principais tecnologias identificadas (quadro, linguagem, base de dados, etc.)
- [ ] Versões capturadas quando disponíveis
- [ ] A tabela de decisão tecnológica é completa e precisa
- [ ] dependências e bibliotecas documentadas
- [ ] Ferramentas de construção e gerenciadores package identificados

## Completude de Análise de Base de Código

- [ ] Todos os diretórios críticos digitalizados com base no tipo de projeto
- [ ] Endpoints da API documentados (se requires api scan = true)
- [ ] Modelos de dados capturados (se required data models = true)
- [ ] Padrões de gestão do Estado identificados (se requires state management = true)
- [ ] Componentes de IU inventariados (se requires ui components = true)
- [ ] Arquivos de configuração localizados e documentados
- [ ] Padrões de autenticação/segurança identificados
- [ ] Pontos de entrada corretamente identificados
- [ ] Pontos de integração mapeados (para projetos multi-partes)
- [ ] Arquivos de teste e padrões documentados

## Análise da Árvore de Origem

- [ ] Árvore de diretório completa gerada sem omissões principais
- [ ] Pastas críticas realçadas e descritas
- [ ] Pontos de entrada claramente marcados
- [ ] Caminhos de integração anotados (para multi-parte)
- [ ] Locais de activos identificados (se aplicável)
- [ ] Padrões de organização de arquivos explicados

## Qualidade da documentação de arquitetura

- [ ] Documento de arquitectura utiliza o modelo adequado do registo
- [ ] Todas as secções do modelo preenchidas com informações relevantes (sem espaços)
- [ ] A seção de pilha de tecnologia é abrangente
- [ ] Padrão de arquitetura claramente explicado
- [ ] Arquitetura de dados documentada (se aplicável)
- [ ] Design de API documentado (se aplicável)
- [ ] Estrutura do componente explicada (se aplicável)
- [ ] Árvore fonte incluída e anotada
- [ ] Estratégia de teste documentada
- [ ] Arquitetura de implantação capturada (se a configuração for encontrada)

## Documentação sobre Desenvolvimento e Operações

- [ ] Pré-requisitos claramente listados
- [ ] Passos de instalação documentados
- [ ] Instruções de configuração do ambiente fornecidas
- [ ] Comandos de execução local especificados
- [ ] Processo de compilação documentado
- [ ] Comandos de teste e abordagem explicados
- [ ] Processo de implantação documentado (se aplicável)
- [ ] Detalhes do gasoduto CI/CD capturados (se encontrados)
- [ ] Orientações de contribuição extraídas (se for encontrada)

## Específico do Projeto Multiparte (se aplicável)

- [ ] Cada parte documentada separadamente
- [ ] Arquivos de arquitetura específicos de partes criados (arquitetura-{part_id}.md)
- [ ] Inventários de componentes específicos da parte criados (se aplicável)
- [ ] Guias de desenvolvimento parcialmente específicos criados
- [ ] Documento de arquitetura de integração criado
- [ ] Pontos de integração claramente definidos com tipo e detalhes
- [ ] Fluxo de dados entre as partes explicadas
- [ ] Arquivo de metadados project-parts.json criado

## Índice e Navegação

- [ ] index.md criado como ponto de entrada principal
- [ ] Estrutura do projecto claramente resumida no índice
- Rápido.