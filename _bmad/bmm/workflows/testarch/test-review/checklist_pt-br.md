# Revisão da Qualidade do Teste - Lista de Verificação de Validação

Use esta lista de verificação para validar que o fluxo de trabalho de revisão da qualidade do teste completou com sucesso e todos os critérios de qualidade foram devidamente avaliados.

---

## Prerequisites

### Test File Discovery

- [ ] Test file(s) identified for review (single/directory/suite scope)
- [ ] Test files exist and are readable
- [ ] Test framework detected (Playwright, Jest, Cypress, Vitest, etc.)
- [ ] Test framework configuration found (playwright.config.ts, jest.config.js, etc.)

### Knowledge Base Loading

- [ ] tea-index.csv loaded successfully
- [ ] `test-quality.md` loaded (Definition of Done)
- [ ] `fixture-architecture.md` loaded (Pure function → Fixture patterns)
- [ ] `network-first.md` loaded (Route intercept before navigate)
- [ ] `data-factories.md` loaded (Factory patterns)
- [ ] `test-levels-framework.md` loaded (E2E vs API vs Component vs Unit)
- [ ] All other enabled fragments loaded successfully

### Context Gathering

- [ ] Story file discovered or explicitly provided (if available)
- [ ] Test design document discovered or explicitly provided (if available)
- [ ] Acceptance criteria extracted from story (if available)
- [ ] Priority context (P0/P1/P2/P3) extracted from test-design (if available)

---

## Passos do processo

### Passo 1: Carregando o Contexto

- [ ] Âmbito de análise determinado (single/directório/suite)
- [ ] Testar os caminhos dos ficheiros recolhidos
Artefactos relacionados descobertos.
- [ ] Fragmentos de base de conhecimento carregados com sucesso
- [ ] Parâmetros de critérios de qualidade lidos de variáveis de fluxo de trabalho

### Passo 2: Processamento do arquivo de teste

**Para cada arquivo de teste:**

- [ ] Arquivo lido com sucesso
- [ ] Tamanho do arquivo medido (linhas, KB)
- [ ] Estrutura do arquivo analisada (descrever blocos, blocos)
- [ ] IDs de ensaio extraídos (se presente)
- [ ] Marcadores prioritários extraídos (se presente)
- [ ] Importações analisadas
- Dependências identificadas

**Análise da estrutura do teste:**

- [ ] Descreva a contagem de blocos calculada
- [ ] Contagem de blocos de ensaio/elemento calculado
- [ ] Estrutura BDD identificada (Daqui a pouco)
- [ ] Utilização de fixação detectada
- [ ] Uso de fábrica de dados detectado
- [ ] Padrões de intercepção de rede identificados
- Asserções contadas
- Esperas e intervalos catalogados
- [ ] Condicionais (se/outro) detectados
- [ ] Tentar/capturar blocos detectados
- [ ] Estado compartilhado ou global detectado

### Etapa 3: Validação dos critérios de qualidade

**Para cada critério habilitado:**

#### Formato BDD (se `check_given_when_then: true`)

- [ ] Dada a estrutura quando-então avaliado
- [ ] Estatuto atribuído (PASS/WARN/FAIL)
Violações registadas com números de linha
- [ ] Exemplos de bons / maus padrões observados

#### IDs de ensaio (se `check_test_ids: true`)

- [ ] Presença do ID do teste validada
- [ ] Formato do ID de ensaio verificado (por exemplo, 1.3-E2E-001)
- [ ] Estatuto atribuído (PASS/WARN/FAIL)
- [ ] Identidades desaparecidas catalogadas

#### Marcadores prioritários (se `check_priority_markers: true`)

- [ ] Classificação P0/P1/P2/P3 validada
- [ ] Estatuto atribuído (PASS/WARN/FAIL)
- [ ] Faltam prioridades catalogadas

#### Esperas duras (se `check_hard_waits: true`)

- [ ] sleep(), waitForTimeout(), atrasos codificados detectados
- [ ] Comentários de justificação verificados
- [ ] Estatuto atribuído (PASS/WARN/FAIL)
- [ ] Violações registradas com números de linha e correções recomendadas

#### Determinação (se `check_determinism: true`)

- [ ] Condicionais (se/else/switch) detectados
- [ ] Abuso de tentativa/captura detectado
- [ ] Valores aleatórios (Math.random, Date.now) detectados
- [ ] Estatuto atribuído (PASS/WARN/FAIL)
- [ ] Violações gravadas com correções recomendadas

#### Isolamento (se `check_isolation: true`)

- [ ] Ganchos de limpeza (apósCada/depois deTodos) validados
- [ ] Estado compartilhado detectado
- [ ] Mutações variáveis globais detectadas
- [ ] Limpeza de recursos verificada
- [ ] Estatuto atribuído (PASS/WARN/FAIL)
- [ ] Violações gravadas com correções recomendadas

#### Padrões de fixação (se `check_fixture_patterns: true`)

- [ ] Dispositivos detectados (test.extend)
- [ ] Funções puras validadas
- [ ] mergeTestes de utilização verificados
- [ ] antes de cada complexidade analisada
- [ ] Estatuto atribuído (PASS/WARN/FAIL)
- [ ] Violações gravadas com correções recomendadas

#### Fábricas de dados (se `check_data_factories: true`)

- Funções de fábrica detectadas
- [ ] Dados com código rígido (correntes/números mágicos) detectados
- [ ] Faker.js ou utilização semelhante validada
- [ ] API-primeira configuração padrão verificado
- [ ] Estatuto atribuído (PASS/WARN/FAIL)
- [ ] Violações gravadas com correções recomendadas

#### Primeiro da rede (se `check_network_first: true`)

- [ ] page.route() before page.goto() validated
- [ ] Condições de corrida detectadas (rota após navegação)
- [ ] espera para responder padrões verificados
- [ ] Estatuto atribuído (PASS/WARN/FAIL)
- [ ] Violações gravadas com correções recomendadas

#### Asserções (se `check_assertions: true`)

- [ ] Asserções explícitas contadas
- [ ] Implícito espera sem afirmações detectadas
- [ ] Especificidade da declaração validada
- [ ] Estatuto atribuído (PASS/WARN/FAIL)
- [ ] Violações gravadas com correções recomendadas

#### Comprimento do ensaio (se `check_test_length: true`)

- [ ] Contagem de linha de arquivo calculada
- [