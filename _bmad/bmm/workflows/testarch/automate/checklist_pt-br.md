# Lista de Verificação de Validação Automatizada do Fluxo de Trabalho

Use esta lista de verificação para validar que o fluxo de trabalho de automatização foi executado corretamente e todas as entregas atendem aos padrões de qualidade.

## Pré-requisitos

Antes de iniciar este fluxo de trabalho, verifique:

O andaime está configurado. config.ts ou cipreste.config.ts existe)
- [ ] A estrutura do diretório de teste existe (testes/ pasta com subdiretórios)
- [ ] Package.json tem dependências do framework de teste instalado

**Halt apenas se:** Framework andaimes está completamente faltando (correr `framework` fluxo de trabalho primeiro)

**Nota:** Os artefatos BMad (história, tech-spec, PRD) são OPTIONAL - o fluxo de trabalho pode ser executado sem eles

---

## Step 1: Execution Mode Determination and Context Loading

### Mode Detection

- [ ] Execution mode correctly determined:
  - [ ] BMad-Integrated Mode (story_file variable set) OR
  - [ ] Standalone Mode (target_feature or target_files set) OR
  - [ ] Auto-discover Mode (no targets specified)

### BMad Artifacts (If Available - OPTIONAL)

- [ ] Story markdown loaded (if `{story_file}` provided)
- [ ] Acceptance criteria extracted from story (if available)
- [ ] Tech-spec.md loaded (if `{use_tech_spec}` true and file exists)
- [ ] Test-design.md loaded (if `{use_test_design}` true and file exists)
- [ ] PRD.md loaded (if `{use_prd}` true and file exists)
- [ ] **Note**: Absence of BMad artifacts does NOT halt workflow

### Framework Configuration

- [ ] Test framework config loaded (playwright.config.ts or cypress.config.ts)
- [ ] Test directory structure identified from `{test_dir}`
- [ ] Existing test patterns reviewed
- [ ] Test runner capabilities noted (parallel execution, fixtures, etc.)

### Coverage Analysis

- [ ] Existing test files searched in `{test_dir}` (if `{analyze_coverage}` true)
- [ ] Tested features vs untested features identified
- [ ] Coverage gaps mapped (tests to source files)
- [ ] Existing fixture and factory patterns checked

### Knowledge Base Fragments Loaded

- [ ] `test-levels-framework.md` - Test level selection
- [ ] `test-priorities.md` - Priority classification (P0-P3)
- [ ] `fixture-architecture.md` - Fixture patterns with auto-cleanup
- [ ] `data-factories.md` - Factory patterns using faker
- [ ] `selective-testing.md` - Targeted test execution strategies
- [ ] `ci-burn-in.md` - Flaky test detection patterns
- [ ] `test-quality.md` - Test design principles

---

## Etapa 2: Identificação de alvos de automação

### Determinação-alvo

**Modo Integrado no BMad (se disponível):**

- [ ] Critérios de aceitação mapeados para cenários de teste
- [ ] Características implementadas na história identificada
- [ ] Testes ATDD existentes verificados (se houver)
- [ ] Expansão para além de ATDD planned (casos de borda, caminhos negativos)

**Modo Standalone (se não houver história):**

- [ ] Características específicas analisadas (se o `{target_feature}` especificado)
- [ ] Arquivos específicos analisados (se `{target_files}` especificado)
- [ ] Características auto-descobertas (se `{auto_discover_features}` true)
- Características priorizadas por:
- [ ] Nenhuma cobertura de teste (prioridade máxima)
- [ ] Lógica empresarial complexa
- [ ] Integrações externas (API, base de dados, autenticação)
- [ ] Caminhos críticos do usuário (login, checkout, etc.)

### Seleção do nível de teste

- [ ] Quadro de selecção do nível de ensaio aplicado (de `test-levels-framework.md`)
- [ ] Testes E2E identificados: Viagens críticas do utilizador, integração multi-sistema
- [ ] Testes API identificados: lógica de negócios, contratos de serviços, transformações de dados
- [ ] Testes de componentes identificados: comportamento da IU, interações, gestão do estado
- [ ] Testes unitários identificados: Lógica pura, casos de borda, manipulação de erros

### Evitação de Cobertura Duplicada

- [ ] Mesmo comportamento NÃO testado em múltiplos níveis desnecessariamente
- [ ] E2E usado apenas para o caminho crítico feliz
- [ ] Testes API usados para variações lógicas de negócios
- [ ] Testes de componentes utilizados para casos de interfaces de interface
- [ ] Testes unitários usados para casos de borda lógica pura

### Atribuição Prioritária

- [ ] Prioridades de teste atribuídas usando `test-priorities.md` framework
- [ ] Testes P0: Caminhos críticos, segurança crítica, integridade de dados
- [ ] Testes P1: Características importantes, pontos de integração, manipulação de erros
- [ ] Testes P2: Casos de borda, variações menos críticas, desempenho
- [ ] Testes de P3: Nice-to-have, recursos raramente usados, exploratório
- Variáveis prioritárias respeitadas:
- [ ] `{include_p0}` = true (inclui sempre)
- [ ] `{include_p1}` = true (alta prioridade)
- [ ] `{include_p2}` = true (prioridade média)
- [ ] `{include_p3}` = false (baixa prioridade, saltar por padrão)

### Plano de Cobertura Criado

- [ ] Plano de cobertura do ensaio documentado
- [ ] O que será testado em cada nível listado
- [ ] Prioridades atribuídas a cada teste
- [ ] Estratégia de cobertura clara (caminhos críticos, abrangente ou selectiva)

---

## Etapa 3: Infraestrutura de teste gerada

### Arquitetura de fixação

- [ ] Dispositivos existentes verificados no `tests/support/fixtures/`
- [ ] Arquitetura de fixação criada/melhorada (se `{generate_fixtures}` true)
- [ ] Todos os acessórios usam o padrão `test.extend()` da Playwright
- [ ] Todos os dispositivos têm limpeza automática i