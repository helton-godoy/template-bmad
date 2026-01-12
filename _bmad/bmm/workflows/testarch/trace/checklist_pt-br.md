# Requisitos Rastreabilidade e decisão da porta - Lista de verificação de validação

**Fluxo de trabalho:** `testarch-trace`
**Proporção:** Assegurar uma matriz de rastreabilidade completa com análise de lacunas acionáveis e tomar uma decisão de disponibilidade para a implantação (PASS/CONCERNS/FAIL/WAIVED)

Esta lista abrange **duas fases sequenciais**:

- **FASE 1**: Requisitos de rastreabilidade (sempre executado)
- **FASE 2**: Decisão relativa à porta de qualidade (executada se `enable_gate_decision: true`)

---

# FASE 1: RASTREABILIDADE DE REQUISITOS

## Validação de Pré-requisitos

- [ ] Critérios de aceitação estão disponíveis (do arquivo de história OU inline)
- [ ] Suite de teste existe (ou lacunas são reconhecidas e documentadas)
- [ ] Caminho do diretório de teste está correto (variável `test_dir`)
- [ ] Arquivo de história é acessível (se usando modo BMad)
- [ ] Base de conhecimento carregada (test-priorities, traceability, risk-governance)

---

## Carregando Contexto

- [ ] Arquivo de história lido com sucesso (se aplicável)
- [ ] Critérios de aceitação extraídos correctamente
- ID da história identificada (por exemplo, 1.3)
- [ ] `test-design.md` carregado (se disponível)
- [ ] `tech-spec.md` carregado (se disponível)
- [ ] `PRD.md` carregado (se disponível)
- [ ] Fragmentos de conhecimento relevantes carregados da `tea-index.csv`

---

## Descoberta e Catalogação de Testes

- [ ] Testes autodescobertos usando múltiplas estratégias (IDs de teste, blocos describe, caminhos de arquivo)
- [ ] Testes categorizados por nível (E2E, API, Componente, Unidade)
- [ ] Metadados de teste extraídos:
  - [ ] IDs de teste (ex: 1.3-E2E-001)
  - [ ] Blocos Describe/contexto
  - [ ] Blocos It (casos de teste individuais)
  - [ ] Estrutura Dado-Quando-Então (se BDD)
  - [ ] Marcadores de prioridade (P0/P1/P2/P3)
- [ ] Todos os arquivos de teste relevantes encontrados (nenhum teste perdido devido a convenções de nomenclatura)

---

## Mapeamento de critérios a testes

- [ ] Cada critério de aceitação mapeado para testes (ou marcado como NENHUMA)
- [ ] Referências explícitas encontradas ( IDs de teste, descrever blocos que mencionam critério)
- [ ] Nível de teste documentado (E2E, API, Componente, Unidade)
- [ ] dado-quando-então narrativa verificada para alinhamento
- [ ] tabela de matriz de rastreabilidade gerada:
- ID do critério
- [ ] Descrição
- [ ] ID do teste
- [ ] Testar o Ficheiro
- [ ] Nível de ensaio
- Status da cobertura

---

## Classificação de Cobertura

- [ ] Status de cobertura classificado para cada critério:
  - [ ] **COMPLETA** - Todos os cenários validados no(s) nível(is) apropriado(s)
  - [ ] **PARCIAL** - Alguma cobertura mas faltando casos de borda ou níveis
  - [ ] **NENHUMA** - Nenhuma cobertura de teste em qualquer nível
  - [ ] **APENAS-UNIDADE** - Apenas testes de unidade (faltando validação de integração/E2E)
  - [ ] **APENAS-INTEGRAÇÃO** - Apenas testes de API/Componente (faltando confiança de unidade)
- [ ] Justificativas de classificação fornecidas
- [ ] Casos de borda considerados na determinação COMPLETA vs PARCIAL

---

## Detecção de Cobertura Duplicada

- [ ] Cobertura duplicada verificada entre os níveis de teste
- [ ] Sobreposição aceitável identificada (defesa em profundidade para caminhos críticos)
- [ ] Duplicação inaceitável assinalada (a mesma validação em múltiplos níveis)
- [ ] Recomendações para a consolidação
- [ ] Princípios de ensaio seletivos aplicados

---

## Análise de Lacunas

- [ ] Lacunas de cobertura identificadas:
  - [ ] Critérios com status NENHUMA
  - [ ] Critérios com status PARCIAL
  - [ ] Critérios com status APENAS-UNIDADE
  - [ ] Critérios com status APENAS-INTEGRAÇÃO
- [ ] Lacunas priorizadas por nível de risco usando estrutura de prioridades de teste:
  - [ ] **CRÍTICO** - Critérios P0 sem cobertura COMPLETA (BLOQUEADOR)
  - [ ] **ALTO** - Critérios P1 sem cobertura COMPLETA (bloqueador de PR)
  - [ ] **MÉDIO** - Critérios P2 sem cobertura COMPLETA (lacuna noturna)
  - [ ] **BAIXO** - Critérios P3 sem cobertura COMPLETA (aceitável)
- [ ] Recomendações de teste específicas fornecidas para cada lacuna:
  - [ ] Nível de teste sugerido (E2E, API, Componente, Unidade)
  - [ ] Descrição do teste (Dado-Quando-Então)
  - [ ] ID de teste recomendado (ex: 1.3-E2E-004)
  - [ ] Explicação de por que o teste é necessário

---

## Métrica de cobertura

- [ ] Percentagem global de cobertura calculada (cobertura completa / critérios totais)
- [ ] Percentagem de cobertura P0 calculada
- [ ] Percentagem de cobertura P1 calculada
- [ ] Percentagem de cobertura P2 calculada (se aplicável)
- [ ] Cobertura por nível calculado:
- [ ] Cobertura E2E %
- [ ] Cobertura API %
- [ ] Cobertura do componente %
- [ ] Cobertura da unidade %

---

## Verificação da qualidade do ensaio

Para cada teste mapeado, verificar:

- [ ] Asserções explícitas estão presentes (não escondidas em ajudantes)
- [ ] O teste segue a estrutura Given-When-Then
- [ ] Sem esperas duras ou sonos (só espera determinística)
- [ ] Auto-limpeza (o teste limpa os seus dados)
- [ ] Tamanho do arquivo < 300 linhas
- [ ] Duração do ensaio < 90 segundos

Questões de qualidade assinaladas:

- [ ] Questões **BLOCKER** identificadas (afirmações em falta, esperas difíceis, padrões de flaky)
- [ ] Questões identificadas de **ARRANQUE** (grandes ficheiros, testes lentos, estrutura pouco clara)
- [ ] Questões **INFO** identificadas (inconsistências de estilo, documentação em falta)

Fragmentos de conhecimento referenciados:

- [ ] `test-quality.md` para a definição de feito
- [ ] `fixture-architecture.md` para padrões de autolimpeza
- [ ] `network-first.md` para as melhores práticas dos dramaturgos
- [ ] `data-factory.md` para gerenciamento de dados de teste
- [ ] `mock-strategy.md` para padrões de simulação de API

### Critérios de Sucesso:
- Todos os requisitos são rastreáveis para testes
- A cobertura de teste é visualizada e verificada
- Links de rastreabilidade são mantidos no código e na documentação
