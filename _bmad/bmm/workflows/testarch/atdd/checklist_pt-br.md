<!-- Powered by BMAD-CORE™ -->

# Checklist de Validação do Fluxo de Trabalho ATDD

Use este checklist para validar se o fluxo de trabalho ATDD foi executado corretamente e se todos os entregáveis atendem aos padrões de qualidade.

## Pré-requisitos

Antes de iniciar este fluxo de trabalho, verifique:

- [ ] História aprovada com critérios de aceitação claros (CA deve ser testável)
- [ ] Sandbox/ambiente de desenvolvimento pronto
- [ ] Scaffolding de framework existe (execute o fluxo de trabalho `framework` se estiver faltando)
- [ ] Configuração de framework de teste disponível (playwright.config.ts ou cypress.config.ts)
- [ ] Package.json tem dependências de teste instaladas (Playwright ou Cypress)

**Parar se faltando:** Scaffolding de framework ou critérios de aceitação da história

---

## Passo 1: Contexto e Requisitos da História

- [ ] Arquivo markdown da história carregado e analisado com sucesso
- [ ] Todos os critérios de aceitação identificados e extraídos
- [ ] Sistemas e componentes afetados identificados
- [ ] Restrições técnicas documentadas
- [ ] Configuração de framework carregada (playwright.config.ts ou cypress.config.ts)
- [ ] Estrutura de diretório de teste identificada da configuração
- [ ] Padrões de fixture existentes revisados para consistência
- [ ] Padrões de teste similares pesquisados e encontrados em `{test_dir}`
- [ ] Fragmentos de base de conhecimento carregados:
  - [ ] `fixture-architecture.md`
  - [ ] `data-factories.md`
  - [ ] `component-tdd.md`
  - [ ] `network-first.md`
  - [ ] `test-quality.md`

---

## Passo 2: Seleção e Estratégia de Nível de Teste

- [ ] Cada critério de aceitação analisado para nível de teste apropriado
- [ ] Framework de seleção de nível de teste aplicado (E2E vs API vs Componente vs Unitário)
- [ ] Testes E2E: Jornadas críticas de usuário e integração multi-sistema identificadas
- [ ] Testes de API: Lógica de negócios e contratos de serviço identificados
- [ ] Testes de componente: Comportamento de componente UI e interações identificados
- [ ] Testes unitários: Lógica pura e casos de borda identificados (se aplicável)
- [ ] Cobertura duplicada evitada (mesmo comportamento não testado em múltiplos níveis desnecessariamente)
- [ ] Testes priorizados usando framework P0-P3 (se documento de design de teste existir)
- [ ] Nível de teste primário definido na variável `primary_level` (tipicamente E2E ou API)
- [ ] Níveis de teste documentados no checklist ATDD

---

## Passo 3: Geração de Testes Falhando

### Estrutura de Arquivo de Teste Criada

- [ ] Arquivos de teste organizados em diretórios apropriados:
  - [ ] `tests/e2e/` para testes ponta-a-ponta
  - [ ] `tests/api/` para testes de API
  - [ ] `tests/component/` para testes de componente
  - [ ] `tests/support/` para infraestrutura (fixtures, factories, helpers)

### Testes E2E (Se Aplicável)

- [ ] Arquivos de teste E2E criados em `tests/e2e/`
- [ ] Todos os testes seguem formato Dado-Quando-Então (Given-When-Then)
- [ ] Testes usam seletores `data-testid` (não classes CSS ou seletores frágeis)
- [ ] Uma asserção por teste (design de teste atômico)
- [ ] Sem esperas ou sleeps fixos (apenas esperas explícitas)
- [ ] Padrão network-first aplicado (interceptação de rota ANTES da navegação)
- [ ] Testes falham inicialmente (fase VERMELHA verificada por execução local de teste)
- [ ] Mensagens de falha são claras e acionáveis

### Testes de API (Se Aplicável)

- [ ] Arquivos de teste de API criados em `tests/api/`
- [ ] Testes seguem formato Dado-Quando-Então
- [ ] Contratos de API validados (estrutura requisição/resposta)
- [ ] Códigos de status HTTP verificados
- [ ] Validação de corpo de resposta inclui todos os campos obrigatórios
- [ ] Casos de erro testados (400, 401, 403, 404, 500)
- [ ] Testes falham inicialmente (fase VERMELHA verificada)

### Testes de Componente (Se Aplicável)

- [ ] Arquivos de teste de componente criados em `tests/component/`
- [ ] Testes seguem formato Dado-Quando-Então
- [ ] Montagem de componente funciona corretamente
- [ ] Teste de interação cobre ações do usuário (clique, hover, teclado)
- [ ] Gerenciamento de estado dentro do componente validado
- [ ] Props e eventos testados
- [ ] Testes falham inicialmente (fase VERMELHA verificada)

### Validação de Qualidade de Teste

- [ ] Todos os testes usam estrutura Dado-Quando-Então com comentários claros
- [ ] Todos os testes têm nomes descritivos explicando o que testam
- [ ] Sem testes duplicados (mesmo comportamento testado múltiplas vezes)
- [ ] Sem padrões flaky (condições de corrida, problemas de tempo)
- [ ] Sem interdependências de teste (testes podem rodar em qualquer ordem)
- [ ] Testes são determinísticos (mesma entrada sempre produz mesmo resultado)

---

## Passo 4: Construção de Infraestrutura de Dados

### Data Factories Criadas

- [ ] Arquivos de factory criados em `tests/support/factories/`
- [ ] Todas as factories usam `@faker-js/faker` para geração de dados aleatórios (sem valores hardcoded)
- [ ] Factories suportam sobrescritas para cenários de teste específicos
- [ ] Factories geram objetos válidos completos correspondendo a contratos de API
- [ ] Funções auxiliares para criação em massa fornecidas (ex: `createUsers(count)`)
- [ ] Exportações de factory são propriamente tipadas (TypeScript)

### Fixtures de Teste Criadas

- [ ] Arquivos de fixture criados em `tests/support/fixtures/`
- [ ] Todas as fixtures usam padrão `test.extend()` do Playwright
- [ ] Fixtures têm fase de configuração (arranjar pré-condições de teste)
- [ ] Fixtures fornecem dados para testes via `await use(data)`
- [ ] Fixtures têm fase de desmontagem com auto-limpeza (deletar dados criados)
- [ ] Fixtures são compusáveis (podem usar outras fixtures se necessário)
- [ ] Fixtures são isoladas (cada teste recebe dados frescos)
- [ ] Fixtures são tipo-seguras (tipos TypeScript definidos)

### Requisitos de Mock Documentados

- [ ] Requisitos de mock de serviço externo identificados
- [ ] Endpoints de mock documentados com URLs e métodos
- [ ] Exemplos de resposta de sucesso fornecidos
- [ ] Exemplos de resposta de falha fornecidos
- [ ] Requisitos de mock documentados no checklist ATDD para equipe DEV

### Requisitos de data-testid Listados

- [ ] Todos os atributos data-testid obrigatórios identificados de testes E2E
- [ ] Lista de data-testid organizada por página ou componente
- [ ] Cada data-testid tem descrição clara do elemento que alveja
- [ ] Lista de data-testid incluída no checklist ATDD para equipe DEV

---

## Passo 5: Criação de Checklist de Implementação

- [ ] Checklist de implementação criado com estrutura clara
- [ ] Cada teste falhando mapeado para tarefas concretas de implementação
- [ ] Tarefas incluem:
  - [ ] Criação de rota/componente
  - [ ] Implementação de lógica de negócios
  - [ ] Integração de API
  - [ ] Adições de atributo data-testid
  - [ ] Tratamento de erros
  - [ ] Comando de execução de teste
  - [ ] Caixa de seleção de conclusão
- [ ] Fluxo de trabalho Red-Green-Refactor documentado no checklist
- [ ] Fase VERMELHA marcada como completa (responsabilidade TEA)
- [ ] Tarefas da fase VERDE listadas para equipe DEV
- [ ] Orientação da fase REFATORAR fornecida
- [ ] Comandos de execução fornecidos:
  - [ ] Rodar todos os testes: `npm run test:e2e`
  - [ ] Rodar arquivo de teste específico
  - [ ] Rodar em modo com cabeça (headed)
  - [ ] Depurar teste específico
- [ ] Esforço estimado incluído (horas ou pontos de história)

---

## Passo 6: Entregáveis Gerados

### Documento de Checklist ATDD Criado

- [ ] Arquivo de saída criado em `{output_folder}/atdd-checklist-{story_id}.md`
- [ ] Documento segue estrutura de template de `atdd-checklist-template.md`
- [ ] Documento inclui todas as seções obrigatórias:
  - [ ] Resumo da história
  - [ ] Quebra de critérios de aceitação
  - [ ] Testes falhando criados (caminhos e contagens de linha)
  - [ ] Data factories criadas
  - [ ] Fixtures criadas
  - [ ] Requisitos de mock
  - [ ] Atributos data-testid necessários
  - [ ] Checklist de implementação
  - [ ] Fluxo de trabalho Red-green-refactor
  - [ ] Comandos de execução
  - [ ] Próximos passos para equipe DEV

### Todos os Testes Verificados Falhando (Fase VERMELHA)

- [ ] Suíte de teste completa rodada localmente antes de finalizar
- [ ] Todos os testes falham como esperado (fase VERMELHA confirmada)
- [ ] Nenhum teste passando antes da implementação (se passando, teste é inválido)
- [ ] Mensagens de falha documentadas no checklist ATDD
- [ ] Falhas são devido a implementação faltando, não bugs de teste
- [ ] Saída de execução de teste capturada para referência

### Resumo Fornecido

- [ ] Resumo inclui:
  - [ ] ID da História
  - [ ] Nível de teste primário
  - [ ] Contagens de teste (E2E, API, Componente)
  - [ ] Caminhos de arquivo de teste
  - [ ] Contagem de factory
  - [ ] Contagem de fixture
  - [ ] Contagem de requisitos de mock
  - [ ] Contagem de data-testid
  - [ ] Contagem de tarefa de implementação
  - [ ] Esforço estimado
  - [ ] Próximos passos para equipe DEV
  - [ ] Caminho do arquivo de saída
  - [ ] Referências de base de conhecimento aplicadas

---

## Verificações de Qualidade

### Qualidade de Design de Teste

- [ ] Testes são legíveis (estrutura Dado-Quando-Então clara)
- [ ] Testes são manuteníveis (usam factories e fixtures, não dados hardcoded)
- [ ] Testes são isolados (sem estado compartilhado entre testes)
- [ ] Testes são determinísticos (sem condições de corrida ou padrões flaky)
- [ ] Testes são atômicos (uma asserção por teste)
- [ ] Testes são rápidos (sem esperas ou atrasos desnecessários)

### Integração de Base de Conhecimento

- [ ] Padrões de fixture-architecture.md aplicados a todas as fixtures
- [ ] Padrões de data-factories.md aplicados a todas as factories
- [ ] Padrões de network-first.md aplicados a testes E2E com requisições de rede
- [ ] Padrões de component-tdd.md aplicados a testes de componente
- [ ] Princípios de test-quality.md aplicados a todo design de teste

### Qualidade de Código

- [ ] Todos os tipos TypeScript estão corretos e completos
- [ ] Sem erros de lint nos arquivos de teste gerados
- [ ] Convenções de nomenclatura consistentes seguidas
- [ ] Importações são organizadas e corretas
- [ ] Código segue guia de estilo do projeto

---

## Pontos de Integração

### Com Agente DEV

- [ ] Checklist ATDD fornece orientação clara de implementação
- [ ] Tarefas de implementação são granulares e acionáveis
- [ ] Requisitos de data-testid são completos e claros
- [ ] Requisitos de mock incluem todos os detalhes necessários
- [ ] Comandos de execução funcionam corretamente

### Com Fluxo de Trabalho de História

- [ ] ID da História corretamente referenciado em arquivos de saída
- [ ] Critérios de aceitação da história refletidos com precisão nos testes
- [ ] Restrições técnicas da história consideradas no design de teste

### Com Fluxo de Trabalho de Framework

- [ ] Configuração de framework de teste corretamente detectada e usada
- [ ] Estrutura de diretório corresponde à configuração de framework
- [ ] Fixtures e auxiliares seguem padrões estabelecidos
- [ ] Convenções de nomenclatura consistentes com padrões de framework

### Com Fluxo de Trabalho test-design (Se Disponível)

- [ ] Cenários P0 de test-design priorizados em ATDD
- [ ] Avaliação de risco de test-design considerada na cobertura de teste
- [ ] Estratégia de cobertura de test-design alinhada com testes ATDD

---

## Critérios de Conclusão

Tudo o que segue deve ser verdadeiro antes de marcar este fluxo de trabalho como completo:

- [ ] **Critérios de aceitação da história analisados** e mapeados para níveis de teste apropriados
- [ ] **Testes falhando criados** em todos os níveis apropriados (E2E, API, Componente)
- [ ] **Formato Dado-Quando-Então** usado consistentemente em todos os testes
- [ ] **Fase VERMELHA verificada** por execução local de teste (todos os testes falhando como esperado)
- [ ] **Padrão network-first** aplicado a testes E2E com requisições de rede
- [ ] **Data factories criadas** usando faker (sem dados de teste hardcoded)
- [ ] **Fixtures criadas** com auto-limpeza na desmontagem
- [ ] **Requisitos de mock documentados** para serviços externos
- [ ] **Atributos data-testid listados** para equipe DEV
- [ ] **Checklist de implementação criado** mapeando testes para tarefas de código
- [ ] **Fluxo de trabalho Red-green-refactor documentado** no checklist ATDD
- [ ] **Comandos de execução fornecidos** e verificados para funcionar
- [ ] **Documento de checklist ATDD criado** e salvo no local correto
- [ ] **Arquivo de saída formatado corretamente** usando estrutura de template
- [ ] **Referências de base de conhecimento aplicadas** e documentadas no resumo
- [ ] **Sem problemas de qualidade de teste** (padrões flaky, condições de corrida, dados hardcoded)

---

## Problemas Comuns e Resoluções

### Problema: Testes passam antes da implementação

**Problema:** Um teste passa mesmo que nenhum código de implementação exista ainda.

**Resolução:**

- Revisar teste para garantir que está testando comportamento real, não comportamento mockado/stubbado
- Verificar se teste está usando acidentalmente funcionalidade existente
- Verificar se asserções de teste são corretas e significativas
- Reescrever teste para falhar até que implementação esteja completa

### Problema: Padrão network-first não aplicado

**Problema:** Interceptação de rota acontece após navegação, causando condições de corrida.

**Resolução:**

- Mover chamadas `await page.route()` ANTES de `await page.goto()`
- Revisar fragmento de conhecimento `network-first.md`
- Atualizar todos os testes E2E para seguir padrão network-first

### Problema: Dados de teste hardcoded em testes

**Problema:** Testes usam strings/números hardcoded em vez de factories.

**Resolução:**

- Substituir todos os dados hardcoded por chamadas de função factory
- Usar `faker` para toda geração de dados aleatórios
- Atualizar data-factories para suportar todos os cenários de teste necessários

### Problema: Fixtures faltando auto-limpeza

**Problema:** Fixtures criam dados mas não limpam na desmontagem.

**Resolução:**

- Adicionar lógica de limpeza após `await use(data)` na fixture
- Chamar funções de deleção/limpeza na desmontagem
- Verificar se limpeza funciona checando banco de dados/armazenamento após execução de teste

### Problema: Testes têm múltiplas asserções

**Problema:** Testes verificam múltiplos comportamentos em teste único (não atômico).

**Resolução:**

- Dividir em testes separados (uma asserção por teste)
- Cada teste deve verificar exatamente um comportamento
- Usar nomes de teste descritivos para esclarecer o que cada teste verifica

### Problema: Testes dependem da ordem de execução

**Problema:** Testes falham quando rodados em isolamento ou ordem diferente.

**Resolução:**

- Remover estado compartilhado entre testes
- Cada teste deve criar seus próprios dados de teste
- Usar fixtures para configuração consistente entre testes
- Verificar se testes podem rodar com flag `.only`

---

## Notas para Agente TEA

- **Parada pré-voo é crítica:** Não prossiga se história não tiver critérios de aceitação ou framework estiver faltando
- **Verificação da fase VERMELHA é mandatória:** Testes devem falhar antes de compartilhar com equipe DEV
- **Padrão network-first:** Interceptação de rota ANTES da navegação previne condições de corrida
- **Uma asserção por teste:** Testes atômicos fornecem diagnóstico claro de falha
- **Auto-limpeza é inegociável:** Toda fixture deve limpar dados na desmontagem
- **Use base de conhecimento:** Carregue fragmentos relevantes (fixture-architecture, data-factories, network-first, component-tdd, test-quality) para orientação
- **Compartilhe com agente DEV:** Checklist ATDD fornece roteiro de implementação do vermelho ao verde
