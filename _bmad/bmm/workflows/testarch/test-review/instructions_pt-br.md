# Revisão da Qualidade do Teste - Instruções v4.0

**Fluxo de Trabalho:** `testarch-test-review`
**Objetivo:** Revisar a qualidade do teste usando a base de conhecimento abrangente do TEA e validar contra as melhores práticas para manutenibilidade, determinismo, isolamento e prevenção de flakiness
**Agente:** Arquiteto de Teste (TEA)
**Formato:** Markdown Puro v4.0 (sem blocos XML)

---

## Visão Geral

Este fluxo de trabalho realiza revisões abrangentes de qualidade de teste usando a base de conhecimento de melhores práticas do TEA. Ele valida testes contra padrões comprovados para arquitetura de fixture, salvaguardas network-first, fábricas de dados, determinismo, isolamento e prevenção de flakiness. A revisão gera feedback acionável com pontuação de qualidade.

**Capacidades Chave:**

- **Revisão Baseada em Conhecimento**: Aplica padrões de fragmentos do tea-index.csv
- **Pontuação de Qualidade**: Pontuação de 0-100 baseada em violações e melhores práticas
- **Multi-Escopo**: Revisar arquivo único, diretório ou suíte de teste inteira
- **Detecção de Padrões**: Identifica padrões flaky, esperas duras, condições de corrida
- **Validação de Melhores Práticas**: Formato BDD, IDs de teste, prioridades, asserções
- **Feedback Acionável**: Questões críticas (deve corrigir) vs recomendações (deveria corrigir)
- **Integração**: Funciona com arquivos de história, design de teste, critérios de aceitação

---

## Pré-requisitos

**Necessário:**

- Arquivo(s) de teste para revisar (autodescobertos ou fornecidos explicitamente)
- Configuração do framework de teste (playwright.config.ts, jest.config.js, etc.)

**Recomendado:**

- Arquivo de história com critérios de aceitação (para contexto)
- Documento de design de teste (para contexto de prioridade)
- Fragmentos da base de conhecimento disponíveis no tea-index.csv

**Condições de Parada:**

- Se o caminho do arquivo de teste for inválido ou o arquivo não existir, pare e solicite correção
- Se test_dir estiver vazio (nenhum teste encontrado), pare e notifique o usuário

---

## Passos do Fluxo de Trabalho

### Passo 1: Carregar Contexto e Base de Conhecimento

**Ações:**

1. Verificar flag playwright-utils:
   - Ler `{config_source}` e verificar `config.tea_use_playwright_utils`

2. Carregar fragmentos de conhecimento relevantes de `{project-root}/_bmad/bmm/testarch/tea-index.csv`:

   **Padrões Centrais (Sempre carregar):**
   - `test-quality.md` - Definição de Feito (testes determinísticos, isolados com limpeza, asserções explícitas, <300 linhas, <1.5 min)
   - `data-factories.md` - Funções de fábrica com faker: overrides, fábricas aninhadas, setup API-first
   - `test-levels-framework.md` - Adequação E2E vs API vs Componente vs Unidade com matriz de decisão
   - `selective-testing.md` - Detecção de cobertura duplicada
   - `test-healing-patterns.md` - Padrões de falha comuns: seletores obsoletos, condições de corrida, dados dinâmicos
   - `selector-resilience.md` - Melhores práticas de seletor
   - `timing-debugging.md` - Prevenção de condição de corrida e técnicas de depuração assíncrona

   **Se `config.tea_use_playwright_utils: true` (Todos Utilitários):**
   - `overview.md` - Melhores práticas de utilitários Playwright
   - `api-request.md` - Validar padrões de uso de apiRequest
   - `network-recorder.md` - Revisar implementação de gravação/reprodução HAR
   - `auth-session.md` - Verificar gerenciamento de token de autenticação
   - `intercept-network-call.md` - Validar interceptação de rede
   - `recurse.md` - Revisar padrões de polling
   - `log.md` - Verificar melhores práticas de log
   - `file-utils.md` - Validar padrões de operação de arquivo
   - `burn-in.md` - Revisar configuração de burn-in
   - `network-error-monitor.md` - Verificar configuração de monitoramento de erro
   - `fixtures-composition.md` - Validar uso de mergeTests

   **Se `config.tea_use_playwright_utils: false`:**
   - `fixture-architecture.md` - Composição Função Pura → Fixture → mergeTests com auto-limpeza
   - `network-first.md` - Interceptação de rota antes de navegar para prevenir condições de corrida
   - `playwright-config.md` - Configuração baseada em ambiente com validação fail-fast
   - `component-tdd.md` - Padrões Red-Green-Refactor com isolamento de provedor
   - `ci-burn-in.md` - Detecção de teste flaky com loop de burn-in de 10 iterações

3. Determinar escopo da revisão:
   - **single**: Revisar um arquivo de teste (`test_file_path` fornecido)
   - **directory**: Revisar todos os testes no diretório (`test_dir` fornecido)
   - **suite**: Revisar suíte de teste inteira (descobrir todos os arquivos de teste)

4. Autodescobrir artefatos relacionados (se `auto_discover_story: true`):
   - Extrair ID do teste do nome do arquivo (ex: `1.3-E2E-001.spec.ts` -> história 1.3)
   - Procurar por arquivo de história (`story-1.3.md`)
   - Procurar por design de teste (`test-design-story-1.3.md` ou `test-design-epic-1.md`)

5. Ler arquivo de história para contexto (se disponível):
   - Extrair critérios de aceitação
   - Extrair classificação de prioridade
   - Extrair IDs de teste esperados

**Saída:** Base de conhecimento completa carregada, escopo de revisão determinado, contexto reunido

---

### Passo 2: Descobrir e Analisar Arquivos de Teste

**Ações:**

1. **Descobrir arquivos de teste** baseado no escopo:
   - **single**: Usar variável `test_file_path`
   - **directory**: Usar `glob` para encontrar todos os arquivos de teste em `test_dir`
   - **suite**: Usar `glob` para encontrar todos os arquivos de teste recursivamente a partir da raiz do projeto

2. **Analisar metadados do arquivo de teste**:
   - Caminho e nome do arquivo
   - Tamanho do arquivo (aviso se >15 KB ou >300 linhas)
   - Framework de teste detectado
   - Importações e dependências
   - Estrutura de teste (blocos describe/context/it)

3. **Extrair estrutura de teste**:
   - Contagem de blocos describe
   - Contagem de blocos it/test
   - IDs de teste (se presentes)
   - Marcadores de prioridade (se presentes)
   - Estrutura BDD (comentários ou passos Dado-Quando-Então)

4. **Identificar padrões de teste**:
   - Fixtures usadas
   - Fábricas de dados usadas
   - Padrões de interceptação de rede
   - Asserções usadas
   - Esperas e timeouts
   - Condicionais
   - Blocos try/catch
   - Estado compartilhado ou globais

**Saída:** Inventário completo de arquivos de teste com análise de estrutura e padrão

---

### Passo 3: Validar Contra Critérios de Qualidade

**Ações:**

Para cada arquivo de teste, validar contra critérios de qualidade:

#### 1. Validação de Formato BDD (se `check_given_when_then: true`)

- ✅ **PASS**: Testes usam estrutura Dado-Quando-Então
- ⚠️ **WARN**: Testes têm alguma estrutura mas não GWT explícito
- ❌ **FAIL**: Testes faltam estrutura clara

**Fragmento de Conhecimento**: test-quality.md, tdd-cycles.md

---

#### 2. Convenções de ID de Teste (se `check_test_ids: true`)

- ✅ **PASS**: IDs de teste presentes e seguem convenção
- ⚠️ **WARN**: Alguns IDs de teste faltando ou inconsistentes
- ❌ **FAIL**: Sem IDs de teste

**Fragmento de Conhecimento**: traceability.md, test-quality.md

---

#### 3. Marcadores de Prioridade (se `check_priority_markers: true`)

- ✅ **PASS**: Testes classificados como P0/P1/P2/P3
- ⚠️ **WARN**: Algumas classificações de prioridade faltando
- ❌ **FAIL**: Sem classificação de prioridade

**Fragmento de Conhecimento**: test-priorities.md, risk-governance.md

---

#### 4. Detecção de Esperas Duras (se `check_hard_waits: true`)

- ✅ **PASS**: Nenhuma espera dura detectada
- ⚠️ **WARN**: Algumas esperas duras usadas mas com justificativa
- ❌ **FAIL**: Esperas duras detectadas sem justificativa

**Padrões para detectar:** `sleep()`, `setTimeout()`, `page.waitForTimeout()`

**Fragmento de Conhecimento**: test-quality.md, network-first.md

---

#### 5. Verificação de Determinismo (se `check_determinism: true`)

- ✅ **PASS**: Testes são determinísticos
- ⚠️ **WARN**: Algumas condicionais mas com justificativa clara
- ❌ **FAIL**: Testes usam if/else, switch, ou try/catch para controle de fluxo

**Fragmento de Conhecimento**: test-quality.md, data-factories.md

---

#### 6. Validação de Isolamento (se `check_isolation: true`)

- ✅ **PASS**: Testes limpam recursos, sem estado compartilhado
- ⚠️ **WARN**: Alguma limpeza faltando mas isolado o suficiente
- ❌ **FAIL**: Testes compartilham estado, dependem da ordem de execução

**Fragmento de Conhecimento**: test-quality.md, data-factories.md

---

#### 7. Padrões de Fixture (se `check_fixture_patterns: true`)

- ✅ **PASS**: Usa padrão Função Pura → Fixture → mergeTests
- ⚠️ **WARN**: Algumas fixtures usadas mas não consistentemente
- ❌ **FAIL**: Sem fixtures, testes repetem código de setup

**Fragmento de Conhecimento**: fixture-architecture.md

---

#### 8. Fábricas de Dados (se `check_data_factories: true`)

- ✅ **PASS**: Usa funções de fábrica com overrides
- ⚠️ **WARN**: Algumas fábricas usadas mas também dados hardcoded
- ❌ **FAIL**: Dados de teste hardcoded

**Fragmento de Conhecimento**: data-factories.md

---

#### 9. Padrão Network-First (se `check_network_first: true`)

- ✅ **PASS**: Interceptação de rota configurada ANTES da navegação
- ⚠️ **WARN**: Algumas rotas interceptadas corretamente, outras após navegação
- ❌ **FAIL**: Interceptação de rota após navegação

**Fragmento de Conhecimento**: network-first.md

---

#### 10. Asserções (se `check_assertions: true`)

- ✅ **PASS**: Asserções explícitas presentes
- ⚠️ **WARN**: Alguns testes dependem de esperas implícitas
- ❌ **FAIL**: Asserções ausentes

**Fragmento de Conhecimento**: test-quality.md

---

#### 11. Comprimento do Teste (se `check_test_length: true`)

- ✅ **PASS**: Arquivo de teste <= 200 linhas (ideal), <= 300 linhas (aceitável)
- ⚠️ **WARN**: Arquivo de teste 301-500 linhas
- ❌ **FAIL**: Arquivo de teste > 500 linhas

**Fragmento de Conhecimento**: test-quality.md

---

#### 12. Duração do Teste (se `check_test_duration: true`)

- ✅ **PASS**: Testes individuais <= 1.5 minutos
- ⚠️ **WARN**: Alguns testes 1.5-3 minutos
- ❌ **FAIL**: Testes > 3 minutos

**Fragmento de Conhecimento**: test-quality.md, selective-testing.md

---

#### 13. Padrões de Flakiness (se `check_flakiness_patterns: true`)

- ✅ **PASS**: Nenhum padrão flaky detectado
- ⚠️ **WARN**: Alguns padrões flaky potenciais
- ❌ **FAIL**: Múltiplos padrões flaky detectados

**Fragmento de Conhecimento**: test-quality.md, network-first.md, ci-burn-in.md

---

### Passo 4: Calcular Pontuação de Qualidade

**Ações:**

1. **Contar violações** por severidade:
   - **Crítico (P0)**: Esperas duras, sem asserções, condições de corrida, estado compartilhado
   - **Alto (P1)**: IDs de teste faltando, sem estrutura BDD, dados hardcoded, fixtures faltando
   - **Médio (P2)**: Arquivos de teste longos, prioridades faltando, algumas condicionais
   - **Baixo (P3)**: Problemas menores de estilo, limpeza incompleta, testes verbosos

2. **Calcular pontuação de qualidade**:

```
Pontuação Inicial: 100

Violações Críticas: -10 pontos cada
Violações Altas: -5 pontos cada
Violações Médias: -2 pontos cada
Violações Baixas: -1 ponto cada

Pontos Bônus:
+ Excelente estrutura BDD: +5
+ Fixtures abrangentes: +5
+ Fábricas de dados abrangentes: +5
+ Padrão Network-first: +5
+ Isolamento perfeito: +5
+ Todos IDs de teste presentes: +5

Pontuação de Qualidade: max(0, min(100, Pontuação Inicial - Violações + Bônus))
```

3. **Grau de Qualidade**:
   - **90-100**: Excelente (A+)
   - **80-89**: Bom (A)
   - **70-79**: Aceitável (B)
   - **60-69**: Precisa Melhorar (C)
   - **<60**: Questões Críticas (F)

**Saída:** Pontuação de qualidade calculada com detalhamento de violação

---

### Passo 5: Gerar Relatório de Revisão

**Ações:**

1. **Criar relatório de revisão** usando `test-review-template.md`:

   - Seção de Cabeçalho (Arquivo, Data, Escopo, Pontuação)
   - Resumo Executivo (Avaliação Geral, Pontos Fortes, Fraquezas, Recomendação)
   - Avaliação de Critérios de Qualidade (Tabela de status)
   - Questões Críticas (Deve Corrigir)
   - Recomendações (Deveria Corrigir)
   - Exemplos de Melhores Práticas
   - Referências da Base de Conhecimento

2. **Gerar comentários inline** (se habilitado)
3. **Gerar badge de qualidade** (se habilitado)
4. **Anexar ao arquivo de história** (se habilitado)

**Saída:** Relatório de revisão abrangente com feedback acionável

---

### Passo 6: Salvar Saídas e Notificar

**Ações:**

1. Salvar relatório de revisão em `{output_file}`
2. Salvar comentários inline
3. Salvar badge de qualidade
4. Atualizar arquivo de história
5. Gerar mensagem de resumo para usuário

**Saída:** Todos os artefatos de revisão salvos e usuário notificado

---

## Matriz de Decisão de Critérios de Qualidade

| Critério | PASS | WARN | FAIL | Fragmento de Conhecimento |
| :--- | :--- | :--- | :--- | :--- |
| Formato BDD | GWT presente | Alguma estrutura | Sem estrutura | test-quality.md |
| IDs de Teste | Todos têm IDs | Alguns faltando | Sem IDs | traceability.md |
| Marcadores Prioridade | Todos classificados | Alguns faltando | Sem classificação | test-priorities.md |
| Esperas Duras | Nenhuma | Algumas justificadas | Presentes | test-quality.md |
| Determinismo | Sem condicionais | Alguns justificados | Condicionais | test-quality.md |
| Isolamento | Limpeza OK | Algumas lacunas | Estado compartilhado | test-quality.md |
| Padrões Fixture | Função Pura -> Fixture | Algumas fixtures | Sem fixtures | fixture-architecture.md |
| Fábricas Dados | Funções fábrica | Algumas fábricas | Dados hardcoded | data-factories.md |
| Network-First | Antes de navegar | Alguns corretos | Condições corrida | network-first.md |
| Asserções | Explícitas | Algumas implícitas | Ausentes | test-quality.md |
| Comprimento Teste | <=300 linhas | 301-500 linhas | >500 linhas | test-quality.md |
| Duração Teste | <=1.5 min | 1.5-3 min | >3 min | test-quality.md |
| Padrões Flakiness | Nenhum | Alguns potenciais | Múltiplos | ci-burn-in.md |

---

## Exemplo de Resumo de Revisão

(Ver versão em inglês para exemplo completo)

---

## Integração com Outros Fluxos de Trabalho

### Antes da Revisão de Teste

- **atdd**: Gerar testes de aceitação
- **automate**: Expandir suíte de regressão
- **dev story**: Desenvolvedor escreve testes de implementação

### Depois da Revisão de Teste

- **Desenvolvedor**: Aborda questões críticas
- **gate**: Revisão de qualidade alimenta decisão de porta

---

## Notas Importantes

1. **Não Prescritivo**: Revisão fornece orientação, não regras rígidas
2. **Contexto Importa**: Algumas violações podem ser justificadas
3. **Baseado em Conhecimento**: Todo feedback fundamentado em padrões do tea-index.csv
4. **Acionável**: Cada questão inclui correção recomendada
5. **Pontuação de Qualidade**: Use como indicador, não medida absoluta
6. **Melhoria Contínua**: Revise os mesmos testes periodicamente

---

## Solução de Problemas

**Problema: Nenhum arquivo de teste encontrado**
- Verifique caminho `test_dir`
- Verifique extensões de arquivo de teste
- Garanta que arquivos existem

**Problema: Pontuação parece muito baixa/alta**
- Revise contagens de violação
- Considere contexto
- Foque em questões críticas primeiro

**Problema: Comentários inline não gerados**
- Verifique `generate_inline_comments: true`
- Verifique permissões de escrita

**Problema: Fragmentos de conhecimento não carregando**
- Verifique existência do `tea-index.csv`
- Verifique caminhos dos fragmentos
