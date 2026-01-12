# Lista de Verificação de Validação do Fluxo de Trabalho de Automação

Use esta lista de verificação para validar se o fluxo de trabalho de automação foi executado corretamente e se todos os entregáveis atendem aos padrões de qualidade.

## Pré-requisitos

Antes de iniciar este fluxo de trabalho, verifique:

- [ ] Estrutura do framework configurada (playwright.config.ts ou cypress.config.ts existe)
- [ ] Estrutura do diretório de teste existe (pasta tests/ com subdiretórios)
- [ ] Dependências do framework de teste instaladas no package.json

**Pare apenas se:** A estrutura do framework estiver completamente ausente (execute o fluxo de trabalho `framework` primeiro)

**Nota:** Artefatos BMad (história, especificação técnica, PRD) são OPCIONAIS - o fluxo de trabalho pode rodar sem eles

---

## Passo 1: Determinação do Modo de Execução e Carregamento de Contexto

### Detecção de Modo

- [ ] Modo de execução determinado corretamente:
  - [ ] Modo Integrado ao BMad (variável story_file definida) OU
  - [ ] Modo Autônomo (target_feature ou target_files definidos) OU
  - [ ] Modo Auto-descoberta (sem alvos especificados)

### Artefatos BMad (Se Disponíveis - OPCIONAL)

- [ ] Markdown da história carregado (se `{story_file}` fornecido)
- [ ] Critérios de aceitação extraídos da história (se disponíveis)
- [ ] Tech-spec.md carregado (se `{use_tech_spec}` for verdadeiro e arquivo existir)
- [ ] Test-design.md carregado (se `{use_test_design}` for verdadeiro e arquivo existir)
- [ ] PRD.md carregado (se `{use_prd}` for verdadeiro e arquivo existir)
- [ ] **Nota**: Ausência de artefatos BMad NÃO interrompe o fluxo de trabalho

### Configuração do Framework

- [ ] Configuração do framework de teste carregada (playwright.config.ts ou cypress.config.ts)
- [ ] Estrutura do diretório de teste identificada em `{test_dir}`
- [ ] Padrões de teste existentes revisados
- [ ] Capacidades do executor de teste anotadas (execução paralela, fixtures, etc.)

### Análise de Cobertura

- [ ] Arquivos de teste existentes pesquisados em `{test_dir}` (se `{analyze_coverage}` for verdadeiro)
- [ ] Funcionalidades testadas vs não testadas identificadas
- [ ] Lacunas de cobertura mapeadas (testes para arquivos fonte)
- [ ] Padrões de fixture e fábrica existentes verificados

### Fragmentos da Base de Conhecimento Carregados

- [ ] `test-levels-framework.md` - Seleção de nível de teste
- [ ] `test-priorities.md` - Classificação de prioridade (P0-P3)
- [ ] `fixture-architecture.md` - Padrões de fixture com auto-limpeza
- [ ] `data-factories.md` - Padrões de fábrica usando faker
- [ ] `selective-testing.md` - Estratégias de execução de teste direcionadas
- [ ] `ci-burn-in.md` - Padrões de detecção de teste flaky
- [ ] `test-quality.md` - Princípios de design de teste

---

## Passo 2: Identificação de Alvos de Automação

### Determinação de Alvo

**Modo Integrado ao BMad (se história disponível):**

- [ ] Critérios de aceitação mapeados para cenários de teste
- [ ] Funcionalidades implementadas na história identificadas
- [ ] Testes ATDD existentes verificados (se houver)
- [ ] Expansão além do ATDD planejada (casos de borda, caminhos negativos)

**Modo Autônomo (se sem história):**

- [ ] Funcionalidade específica analisada (se `{target_feature}` especificada)
- [ ] Arquivos específicos analisados (se `{target_files}` especificados)
- [ ] Funcionalidades auto-descobertas (se `{auto_discover_features}` for verdadeiro)
- [ ] Funcionalidades priorizadas por:
  - [ ] Sem cobertura de teste (maior prioridade)
  - [ ] Lógica de negócios complexa
  - [ ] Integrações externas (API, banco de dados, auth)
  - [ ] Caminhos críticos do usuário (login, checkout, etc.)

### Seleção de Nível de Teste

- [ ] Framework de seleção de nível de teste aplicado (de `test-levels-framework.md`)
- [ ] Testes E2E identificados: Jornadas críticas do usuário, integração multi-sistema
- [ ] Testes de API identificados: Lógica de negócios, contratos de serviço, transformações de dados
- [ ] Testes de Componente identificados: Comportamento de UI, interações, gerenciamento de estado
- [ ] Testes Unitários identificados: Lógica pura, casos de borda, tratamento de erro

### Prevenção de Cobertura Duplicada

- [ ] Mesmo comportamento NÃO testado em múltiplos níveis desnecessariamente
- [ ] E2E usado apenas para caminho feliz crítico
- [ ] Testes de API usados para variações de lógica de negócios
- [ ] Testes de Componente usados para casos de borda de interação de UI
- [ ] Testes Unitários usados para casos de borda de lógica pura

### Atribuição de Prioridade

- [ ] Prioridades de teste atribuídas usando framework `test-priorities.md`
- [ ] Testes P0: Caminhos críticos, segurança crítica, integridade de dados
- [ ] Testes P1: Funcionalidades importantes, pontos de integração, tratamento de erro
- [ ] Testes P2: Casos de borda, variações menos críticas, desempenho
- [ ] Testes P3: Desejáveis, funcionalidades raramente usadas, exploratórios
- [ ] Variáveis de prioridade respeitadas:
  - [ ] `{include_p0}` = true (sempre incluir)
  - [ ] `{include_p1}` = true (alta prioridade)
  - [ ] `{include_p2}` = true (média prioridade)
  - [ ] `{include_p3}` = false (baixa prioridade, pular por padrão)

### Plano de Cobertura Criado

- [ ] Plano de cobertura de teste documentado
- [ ] O que será testado em cada nível listado
- [ ] Prioridades atribuídas a cada teste
- [ ] Estratégia de cobertura clara (caminhos críticos, abrangente ou seletiva)

---

## Passo 3: Infraestrutura de Teste Gerada

### Arquitetura de Fixture

- [ ] Fixtures existentes verificadas em `tests/support/fixtures/`
- [ ] Arquitetura de fixture criada/aprimorada (se `{generate_fixtures}` for verdadeiro)
- [ ] Todas as fixtures usam padrão `test.extend()` do Playwright
- [ ] Todas as fixtures têm auto-limpeza no teardown
- [ ] Fixtures comuns criadas/aprimoradas:
  - [ ] authenticatedUser (com auto-deleção)
  - [ ] apiRequest (cliente autenticado)
  - [ ] mockNetwork (simulação de serviço externo)
  - [ ] testDatabase (com auto-limpeza)

### Fábricas de Dados

- [ ] Fábricas existentes verificadas em `tests/support/factories/`
- [ ] Arquitetura de fábrica criada/aprimorada (se `{generate_factories}` for verdadeiro)
- [ ] Todas as fábricas usam `@faker-js/faker` para dados aleatórios (sem valores fixos)
- [ ] Todas as fábricas suportam overrides para cenários específicos
- [ ] Fábricas comuns criadas/aprimoradas:
  - [ ] Fábrica de usuário (email, senha, nome, papel)
  - [ ] Fábrica de produto (nome, preço, SKU)
  - [ ] Fábrica de pedido (itens, total, status)
- [ ] Helpers de limpeza fornecidos (ex: deleteUser(), deleteProduct())

### Utilitários Auxiliares

- [ ] Helpers existentes verificados em `tests/support/helpers/` (se `{update_helpers}` for verdadeiro)
- [ ] Utilitários comuns criados/aprimorados:
  - [ ] waitFor (polling para condições complexas)
  - [ ] retry (helper de retentativa para operações instáveis)
  - [ ] testData (geração de dados de teste)
  - [ ] assertions (helpers de asserção personalizados)

---

## Passo 4: Arquivos de Teste Gerados

### Estrutura de Arquivo de Teste

- [ ] Arquivos de teste organizados corretamente:
  - [ ] `tests/e2e/` para testes E2E
  - [ ] `tests/api/` para testes de API
  - [ ] `tests/component/` para testes de componente
  - [ ] `tests/unit/` para testes unitários
  - [ ] `tests/support/` para fixtures/fábricas/helpers

### Testes E2E (Se Aplicável)

- [ ] Arquivos de teste E2E criados em `tests/e2e/`
- [ ] Todos os testes seguem formato Dado-Quando-Então
- [ ] Todos os testes têm tags de prioridade ([P0], [P1], [P2], [P3]) no nome do teste
- [ ] Todos os testes usam seletores data-testid (não classes CSS)
- [ ] Uma asserção por teste (design atômico)
- [ ] Sem esperas duras ou sleeps (apenas esperas explícitas)
- [ ] Padrão network-first aplicado (interceptação de rota ANTES da navegação)
- [ ] Comentários claros Dado-Quando-Então no código de teste

### Testes de API (Se Aplicável)

- [ ] Arquivos de teste de API criados em `tests/api/`
- [ ] Todos os testes seguem formato Dado-Quando-Então
- [ ] Todos os testes têm tags de prioridade no nome do teste
- [ ] Contratos de API validados (estrutura de requisição/resposta)
- [ ] Códigos de status HTTP verificados
- [ ] Validação do corpo da resposta inclui campos obrigatórios
- [ ] Casos de erro testados (400, 401, 403, 404, 500)
- [ ] Formato de token JWT validado (se testes de auth)

### Testes de Componente (Se Aplicável)

- [ ] Arquivos de teste de componente criados em `tests/component/`
- [ ] Todos os testes seguem formato Dado-Quando-Então
- [ ] Todos os testes têm tags de prioridade no nome do teste
- [ ] Montagem de componente funciona corretamente
- [ ] Teste de interação cobre ações do usuário (clique, hover, teclado)
- [ ] Gerenciamento de estado validado
- [ ] Props e eventos testados

### Testes Unitários (Se Aplicável)

- [ ] Arquivos de teste unitário criados em `tests/unit/`
- [ ] Todos os testes seguem formato Dado-Quando-Então
- [ ] Todos os testes têm tags de prioridade no nome do teste
- [ ] Lógica pura testada (sem dependências)
- [ ] Casos de borda cobertos
- [ ] Tratamento de erro testado

### Padrões de Qualidade Aplicados

- [ ] Todos os testes usam formato Dado-Quando-Então com comentários claros
- [ ] Todos os testes têm nomes descritivos com tags de prioridade
- [ ] Sem testes duplicados (mesmo comportamento testado múltiplas vezes)
- [ ] Sem padrões instáveis (condições de corrida, problemas de tempo)
- [ ] Sem interdependências de teste (testes podem rodar em qualquer ordem)
- [ ] Testes são determinísticos (mesma entrada sempre produz mesmo resultado)
- [ ] Todos os testes usam seletores data-testid (testes E2E)
- [ ] Sem esperas duras: `await page.waitForTimeout()` (proibido)
- [ ] Sem fluxo condicional: `if (await element.isVisible())` (proibido)
- [ ] Sem try-catch para lógica de teste (apenas para limpeza)
- [ ] Sem dados de teste fixos (usar fábricas com faker)
- [ ] Sem classes page object (testes são diretos e simples)
- [ ] Sem estado compartilhado entre testes

### Padrão Network-First Aplicado

- [ ] Interceptação de rota configurada ANTES da navegação (testes E2E com requisições de rede)
- [ ] `page.route()` chamado antes de `page.goto()` para prevenir condições de corrida
- [ ] Padrão network-first verificado em todos os testes E2E que fazem chamadas de API

---

## Passo 5: Validação e Cura de Teste (NOVO - Fase 2.5)

### Configuração de Cura

- [ ] Configuração de cura verificada:
  - [ ] Configuração `{auto_validate}` anotada (padrão: true)
  - [ ] Configuração `{auto_heal_failures}` anotada (padrão: false)
  - [ ] Configuração `{max_healing_iterations}` anotada (padrão: 3)
  - [ ] Configuração `{use_mcp_healing}` anotada (padrão: true)

### Fragmentos de Conhecimento de Cura Carregados (Se Cura Habilitada)

- [ ] `test-healing-patterns.md` carregado (padrões comuns de falha e correções)
- [ ] `selector-resilience.md` carregado (guia de refatoração de seletor)
- [ ] `timing-debugging.md` carregado (correções de condição de corrida)

### Execução e Validação de Teste

- [ ] Testes gerados executados (se `{auto_validate}` for verdadeiro)
- [ ] Resultados de teste capturados:
  - [ ] Total de testes executados
  - [ ] Contagem de testes aprovados
  - [ ] Contagem de testes falhando
  - [ ] Mensagens de erro e stack traces capturados

### Loop de Cura (Se Habilitado e Testes Falharam)

- [ ] Loop de cura iniciado (se `{auto_heal_failures}` for verdadeiro E testes falharam)
- [ ] Para cada teste falhando:
  - [ ] Padrão de falha identificado (seletor, tempo, dados, rede, espera dura)
  - [ ] Estratégia de cura apropriada aplicada:
    - [ ] Seletor obsoleto -> Substituído por data-testid ou papel ARIA
    - [ ] Condição de corrida -> Adicionada interceptação network-first ou esperas de estado
    - [ ] Dados dinâmicos -> Valores fixos substituídos por regex/geração dinâmica
    - [ ] Erro de rede -> Adicionada simulação de rota
    - [ ] Espera dura -> Substituída por espera baseada em evento
  - [ ] Teste curado re-executado para validar correção
  - [ ] Contagem de iteração rastreada (máx 3 tentativas)

### Tratamento de Testes Não Corrigíveis

- [ ] Testes que não puderam ser curados após 3 iterações marcados com `test.fixme()` (se `{mark_unhealable_as_fixme}` for verdadeiro)
- [ ] Comentário detalhado adicionado aos testes test.fixme():
  - [ ] Qual falha ocorreu
  - [ ] Qual cura foi tentada (3 iterações)
  - [ ] Por que a cura falhou
  - [ ] Passos de investigação manual necessários
- [ ] Lógica original do teste preservada em comentários

### Relatório de Cura Gerado

- [ ] Relatório de cura gerado (se cura tentada)
- [ ] Relatório inclui:
  - [ ] Status auto-heal habilitado
  - [ ] Modo de cura (Assistido por MCP ou Baseado em Padrão)
  - [ ] Iterações permitidas (max_healing_iterations)
  - [ ] Resultados de validação (total, aprovados, falhando)
  - [ ] Testes curados com sucesso (contagem, arquivo:linha, correção aplicada)
  - [ ] Testes incapazes de curar (contagem, arquivo:linha, motivo)
  - [ ] Padrões de cura aplicados (correções de seletor, correções de tempo, correções de dados)
  - [ ] Referências da base de conhecimento usadas

---

## Passo 6: Documentação e Scripts Atualizados

### README de Teste Atualizado

- [ ] `tests/README.md` criado ou atualizado (se `{update_readme}` for verdadeiro)
- [ ] Visão geral da estrutura da suíte de teste incluída
- [ ] Instruções de execução de teste fornecidas (todos, arquivos específicos, por prioridade)
- [ ] Exemplos de uso de fixture fornecidos
- [ ] Exemplos de uso de fábrica fornecidos
- [ ] Convenção de tag de prioridade explicada ([P0], [P1], [P2], [P3])
- [ ] Como escrever novos testes documentado
- [ ] Padrões comuns documentados
- [ ] Anti-padrões documentados (o que evitar)

### Scripts package.json Atualizados

- [ ] Scripts package.json adicionados/atualizados (se `{update_package_scripts}` for verdadeiro)
- [ ] Script `test:e2e` para todos os testes E2E
- [ ] Script `test:e2e:p0` apenas para testes P0
- [ ] Script `test:e2e:p1` para testes P0 + P1
- [ ] Script `test:api` para testes de API
- [ ] Script `test:component` para testes de componente
- [ ] Script `test:unit` para testes unitários (se aplicável)

### Suíte de Teste Executada

- [ ] Suíte de teste executada localmente (se `{run_tests_after_generation}` for verdadeiro)
- [ ] Resultados de teste capturados (contagens de aprovação/reprovação)
- [ ] Nenhum padrão instável detectado (testes são determinísticos)
- [ ] Requisitos de configuração documentados (se houver)
- [ ] Problemas conhecidos documentados (se houver)

---

## Passo 6: Resumo de Automação Gerado

### Documento de Resumo de Automação

- [ ] Arquivo de saída criado em `{output_summary}`
- [ ] Documento inclui modo de execução (Integrado ao BMad, Autônomo, Auto-descoberta)
- [ ] Análise de funcionalidade incluída (arquivos fonte, lacunas de cobertura) - Modo Autônomo
- [ ] Testes criados listados (E2E, API, Componente, Unidade) com contagens e caminhos
- [ ] Infraestrutura criada listada (fixtures, fábricas, helpers)
- [ ] Instruções de execução de teste fornecidas
- [ ] Análise de cobertura incluída:
  - [ ] Contagem total de testes
  - [ ] Detalhamento de prioridade (contagens P0, P1, P2, P3)
  - [ ] Detalhamento de nível de teste (contagens E2E, API, Componente, Unidade)
  - [ ] Porcentagem de cobertura (se calculada)
  - [ ] Status de cobertura (critérios de aceitação cobertos, lacunas identificadas)
- [ ] Checklist de Definição de Feito incluído
- [ ] Próximos passos fornecidos
- [ ] Recomendações incluídas (se modo Autônomo)

### Resumo Fornecido ao Usuário

- [ ] Saída de resumo concisa fornecida
- [ ] Total de testes criados através dos níveis de teste
- [ ] Detalhamento de prioridade (contagens P0, P1, P2, P3)
- [ ] Contagens de infraestrutura (fixtures, fábricas, helpers)
- [ ] Comando de execução de teste fornecido
- [ ] Caminho do arquivo de saída fornecido
- [ ] Próximos passos listados

---

## Verificações de Qualidade

### Qualidade de Design de Teste

- [ ] Testes são legíveis (estrutura clara Dado-Quando-Então)
- [ ] Testes são manuteníveis (usam fábricas/fixtures, não dados fixos)
- [ ] Testes são isolados (sem estado compartilhado entre testes)
- [ ] Testes são determinísticos (sem condições de corrida ou padrões instáveis)
- [ ] Testes são atômicos (uma asserção por teste)
- [ ] Testes são rápidos (sem esperas ou atrasos desnecessários)
- [ ] Testes são enxutos (arquivos com menos de {max_file_lines} linhas)

### Integração da Base de Conhecimento

- [ ] Framework de seleção de nível de teste aplicado (de `test-levels-framework.md`)
- [ ] Classificação de prioridade aplicada (de `test-priorities.md`)
- [ ] Padrões de arquitetura de fixture aplicados (de `fixture-architecture.md`)
- [ ] Padrões de fábrica de dados aplicados (de `data-factories.md`)
- [ ] Estratégias de teste seletivo consideradas (de `selective-testing.md`)
- [ ] Padrões de detecção de teste flaky considerados (de `ci-burn-in.md`)
- [ ] Princípios de qualidade de teste aplicados (de `test-quality.md`)

### Qualidade de Código

- [ ] Todos os tipos TypeScript estão corretos e completos
- [ ] Sem erros de linting nos arquivos de teste gerados
- [ ] Convenções de nomenclatura consistentes seguidas
- [ ] Importações organizadas e corretas
- [ ] Código segue guia de estilo do projeto
- [ ] Sem console.log ou declarações de debug no código de teste

---

## Pontos de Integração

### Com Fluxo de Trabalho de Framework

- [ ] Configuração do framework de teste detectada e usada
- [ ] Estrutura de diretório corresponde à configuração do framework
- [ ] Fixtures e helpers seguem padrões estabelecidos
- [ ] Convenções de nomenclatura consistentes com padrões do framework

### Com Fluxos de Trabalho BMad (Se Disponíveis - OPCIONAL)

**Com Fluxo de Trabalho de História:**

- [ ] ID da história referenciado corretamente na saída (se história disponível)
- [ ] Critérios de aceitação da história refletidos nos testes (se história disponível)
- [ ] Restrições técnicas da história consideradas (se história disponível)

**Com Fluxo de Trabalho de test-design:**

- [ ] Cenários P0 do test-design priorizados (se test-design disponível)
- [ ] Avaliação de risco do test-design considerada (se test-design disponível)
- [ ] Estratégia de cobertura alinhada com test-design (se test-design disponível)

**Com Fluxo de Trabalho atdd:**

- [ ] Testes ATDD existentes verificados (se história teve fluxo ATDD executado)
- [ ] Expansão além do ATDD planejada (casos de borda, caminhos negativos)
- [ ] Sem cobertura duplicada com testes ATDD

### Com Pipeline CI

- [ ] Testes podem rodar em ambiente CI
- [ ] Testes são paralelizáveis (sem estado compartilhado)
- [ ] Testes têm timeouts apropriados
- [ ] Testes limpam seus dados (sem poluição do ambiente CI)

---

## Critérios de Conclusão

Tudo o que segue deve ser verdadeiro antes de marcar este fluxo de trabalho como completo:

- [ ] **Modo de execução determinado** (Integrado ao BMad, Autônomo, ou Auto-descoberta)
- [ ] **Configuração do framework carregada** e validada
- [ ] **Análise de cobertura concluída** (lacunas identificadas se analyze_coverage for verdadeiro)
- [ ] **Alvos de automação identificados** (o que precisa ser testado)
- [ ] **Níveis de teste selecionados** apropriadamente (E2E, API, Componente, Unidade)
- [ ] **Cobertura duplicada evitada** (mesmo comportamento não testado em múltiplos níveis)
- [ ] **Prioridades de teste atribuídas** (P0, P1, P2, P3)
- [ ] **Arquitetura de fixture criada/aprimorada** com auto-limpeza
- [ ] **Fábricas de dados criadas/aprimoradas** usando faker (sem dados fixos)
- [ ] **Utilitários auxiliares criados/aprimorados** (se necessário)
- [ ] **Arquivos de teste gerados** em níveis apropriados (E2E, API, Componente, Unidade)
- [ ] **Formato Dado-Quando-Então usado** consistentemente em todos os testes
- [ ] **Tags de prioridade adicionadas** a todos os nomes de teste ([P0], [P1], [P2], [P3])
- [ ] **Seletores data-testid usados** em testes E2E (não classes CSS)
- [ ] **Padrão network-first aplicado** (interceptação de rota antes da navegação)
- [ ] **Padrões de qualidade reforçados** (sem esperas duras, sem padrões instáveis, auto-limpeza, determinístico)
- [ ] **README de teste atualizado** com instruções de execução e padrões
- [ ] **Scripts package.json atualizados** com comandos de execução de teste
- [ ] **Suíte de teste executada localmente** (se run_tests_after_generation for verdadeiro)
- [ ] **Testes validados** (se auto_validate habilitado)
- [ ] **Falhas curadas** (se auto_heal_failures habilitado e testes falharam)
- [ ] **Relatório de cura gerado** (se cura tentada)
- [ ] **Testes não corrigíveis marcados** com test.fixme() e comentários detalhados (se houver)
- [ ] **Resumo de automação criado** e salvo no local correto
- [ ] **Arquivo de saída formatado corretamente**
- [ ] **Referências da base de conhecimento aplicadas** e documentadas (incluindo fragmentos de cura se usados)
- [ ] **Sem problemas de qualidade de teste** (padrões instáveis, condições de corrida, dados fixos, page objects)

---

## Problemas Comuns e Resoluções

### Problema: Artefatos BMad não encontrados

**Problema:** Arquivos de história, tech-spec ou PRD não encontrados quando variáveis estão definidas.

**Resolução:**

- **automate NÃO requer artefatos BMad** - eles são melhorias OPCIONAIS
- Se arquivos não encontrados, mude para Modo Autônomo automaticamente
- Analise código fonte diretamente sem contexto BMad
- Continue fluxo de trabalho sem parar

### Problema: Configuração do framework não encontrada

**Problema:** Nenhum playwright.config.ts ou cypress.config.ts encontrado.

**Resolução:**

- **PARE o fluxo de trabalho** - framework é necessário
- Mensagem: "Estrutura do framework necessária. Execute `bmad tea *framework` primeiro."
- Usuário deve executar fluxo de trabalho de framework antes de automatizar

### Problema: Nenhum alvo de automação identificado

**Problema:** Nem história, target_feature, nem target_files especificados, e auto-descoberta não encontra nada.

**Resolução:**

- Verifique se variável source_dir está correta
- Verifique se código fonte existe no projeto
- Peça ao usuário para especificar target_feature ou target_files explicitamente
- Forneça exemplos: `target_feature: "src/auth/"` ou `target_files: "src/auth/login.ts,src/auth/session.ts"`

### Problema: Cobertura duplicada detectada

**Problema:** Mesmo comportamento testado em múltiplos níveis (E2E + API + Componente).

**Resolução:**

- Revise framework de seleção de nível de teste (test-levels-framework.md)
- Use E2E para caminho feliz crítico APENAS
- Use API para variações de lógica de negócios
- Use Componente para casos de borda de UI
- Remova testes redundantes que duplicam cobertura

### Problema: Testes têm dados fixos

**Problema:** Testes usam endereços de email, senhas ou outros dados fixos.

**Resolução:**

- Substitua todos os dados fixos por chamadas de função de fábrica
- Use faker para toda geração de dados aleatórios
- Atualize data-factories para suportar todos os cenários de teste necessários
- Exemplo: `createUser({ email: faker.internet.email() })`

### Problema: Testes são instáveis (flaky)

**Problema:** Testes falham intermitentemente, passam na retentativa.

**Resolução:**

- Remova todas as esperas duras (`page.waitForTimeout()`)
- Use esperas explícitas (`page.waitForSelector()`)
- Aplique padrão network-first (interceptação de rota antes da navegação)
- Remova fluxo condicional (`if (await element.isVisible())`)
- Garanta que testes são determinísticos (sem condições de corrida)
- Execute loop de burn-in (10 iterações) para detectar instabilidade

### Problema: Fixtures não limpam dados

**Problema:** Dados de teste persistem após execução do teste, causando poluição de teste.

**Resolução:**

- Garanta que todas as fixtures tenham limpeza na fase teardown
- Limpeza acontece APÓS `await use(data)`
- Chame funções de deleção/limpeza (deleteUser, deleteProduct, etc.)
- Verifique se limpeza funciona checando banco de dados/armazenamento após execução do teste

### Problema: Testes muito lentos

**Problema:** Testes demoram mais de 90 segundos (max_test_duration).

**Resolução:**

- Remova esperas e atrasos desnecessários
- Use execução paralela onde possível
- Simule serviços externos (não faça chamadas de API reais)
- Use testes de API em vez de E2E para lógica de negócios
- Otimize criação de dados de teste (use banco de dados em memória, etc.)

---

## Notas para Agente TEA

- **automate é flexível:** Pode trabalhar com ou sem artefatos BMad (história, tech-spec, PRD são OPCIONAIS)
- **Modo Autônomo é poderoso:** Analise qualquer base de código e gere testes independentemente
- **Modo Auto-descoberta:** Escaneie base de código por funcionalidades precisando de testes quando nenhum alvo especificado
- **Framework é o ÚNICO requisito rígido:** PARE se config do framework faltar, caso contrário prossiga
- **Evite cobertura duplicada:** E2E para caminhos críticos apenas, API/Componente para variações
- **Tags de prioridade permitem execução seletiva:** Testes P0 rodam em cada commit, P1 no PR, P2 noturnamente
- **Padrão network-first previne condições de corrida:** Interceptação de rota ANTES da navegação
- **Sem page objects:** Mantenha testes simples, diretos e manuteníveis
- **Use base de conhecimento:** Carregue fragmentos relevantes (test-levels, test-priorities, fixture-architecture, data-factories, healing patterns) para orientação
- **Apenas testes determinísticos:** Sem esperas duras, sem fluxo condicional, sem padrões instáveis permitidos
- **Cura opcional:** auto_heal_failures desativado por padrão (opt-in para cura automática de teste)
- **Degradação graciosa:** Cura funciona sem Playwright MCP (fallback baseado em padrão)
- **Testes não corrigíveis tratados:** Marque com test.fixme() e comentários detalhados (não silenciosamente quebrados)
