<!-- Powered by BMAD-CORE™ -->

# Desenvolvimento Guiado por Testes de Aceitação (ATDD)

**ID do Fluxo de Trabalho**: `_bmad/bmm/testarch/atdd`
**Versão**: 4.0 (BMad v6)

---

## Visão Geral

Gera testes de aceitação falhando ANTES da implementação seguindo o ciclo red-green-refactor do TDD. Este fluxo de trabalho cria cobertura de teste abrangente em níveis apropriados (E2E, API, Componente) com infraestrutura de suporte (fixtures, fábricas, mocks) e fornece uma lista de verificação de implementação para guiar o desenvolvimento.

**Princípio Central**: Testes falham primeiro (fase vermelha), depois guiam o desenvolvimento para o verde, então permitem refatoração confiante.

---

## Requisitos de Pré-voo

**Crítico:** Verifique estes requisitos antes de prosseguir. Se algum falhar, PARE e notifique o usuário.

- ✅ História aprovada com critérios de aceitação claros
- ✅ Sandbox/ambiente de desenvolvimento pronto
- ✅ Estrutura do framework existe (execute o fluxo de trabalho `framework` se estiver faltando)
- ✅ Configuração do framework de teste disponível (playwright.config.ts ou cypress.config.ts)

---

## Passo 1: Carregar Contexto da História e Requisitos

### Ações

1. **Ler Markdown da História**
   - Carregar arquivo de história da variável `{story_file}`
   - Extrair critérios de aceitação (todos os requisitos testáveis)
   - Identificar sistemas e componentes afetados
   - Notar quaisquer restrições técnicas ou dependências

2. **Carregar Configuração do Framework**
   - Ler config do framework (playwright.config.ts ou cypress.config.ts)
   - Identificar estrutura de diretório de teste
   - Verificar padrões de fixture existentes
   - Notar capacidades do executor de teste

3. **Carregar Padrões de Teste Existentes**
   - Pesquisar `{test_dir}` por testes similares
   - Identificar fixtures e helpers reutilizáveis
   - Verificar padrões de fábrica de dados
   - Notar convenções de nomenclatura

4. **Verificar Flag de Utilitários Playwright**

   Ler `{config_source}` e verificar `config.tea_use_playwright_utils`.

5. **Carregar Fragmentos da Base de Conhecimento**

   **Crítico:** Consulte `{project-root}/_bmad/bmm/testarch/tea-index.csv` para carregar:

   **Padrões Centrais (Sempre carregar):**
   - `data-factories.md` - Padrões de fábrica usando faker
   - `component-tdd.md` - Estratégias de teste de componente
   - `test-quality.md` - Princípios de design de teste
   - `test-healing-patterns.md` - Padrões de falha comuns e estratégias de cura
   - `selector-resilience.md` - Melhores práticas de seletores
   - `timing-debugging.md` - Prevenção de condição de corrida e depuração assíncrona

   **Se `config.tea_use_playwright_utils: true` (Todos Utilitários):**
   - `overview.md` - Utilitários Playwright para padrões ATDD
   - `api-request.md` - Exemplos de teste de API
   - `network-recorder.md` - Gravação/reprodução HAR
   - `auth-session.md` - Configuração de autenticação
   - `intercept-network-call.md` - Interceptação de rede
   - `recurse.md` - Polling para critérios assíncronos
   - `log.md` - Logging em testes ATDD
   - `file-utils.md` - Validação de download de arquivo
   - `network-error-monitor.md` - Monitor de erro de rede
   - `fixtures-composition.md` - Composição de fixtures

   **Se `config.tea_use_playwright_utils: false`:**
   - `fixture-architecture.md` - Padrões de fixture de teste com auto-limpeza
   - `network-first.md` - Padrões de interceptação de rota

**Condição de Parada:** Se a história não tiver critérios de aceitação ou o framework estiver faltando, PARE com a mensagem: "ATDD requer critérios de aceitação claros e configuração de framework de teste"

---

## Passo 1.5: Seleção de Modo de Geração (NOVO - Fase 2.5)

### Ações

1. **Detectar Modo de Geração**

   Determine o modo baseado na complexidade do cenário:

   **Modo de Geração IA (PADRÃO)**:
   - Critérios de aceitação claros com padrões padrão
   - Usa: Testes gerados por IA a partir de requisitos
   - Apropriado para: CRUD, auth, navegação, testes de API
   - Abordagem mais rápida

   **Modo de Gravação (OPCIONAL - UI Complexa)**:
   - Interações de UI complexas (arrastar-soltar, assistentes, fluxos multi-página)
   - Usa: Gravação de teste interativa com Playwright MCP
   - Apropriado para: Fluxos de trabalho visuais, requisitos pouco claros
   - Apenas se config.tea_use_mcp_enhancements for true E MCP disponível

2. **Modo de Geração IA (PADRÃO - Continue para Passo 2)**

   Para cenários padrão:
   - Continue com fluxo de trabalho existente (Passo 2: Selecionar Níveis e Estratégia de Teste)
   - IA gera testes baseados em critérios de aceitação do Passo 1
   - Use padrões da base de conhecimento para estrutura de teste

3. **Modo de Gravação (OPCIONAL - Apenas UI Complexa)**

   Para cenários de UI complexos E config.tea_use_mcp_enhancements é true:

   **A. Verificar Disponibilidade MCP**

   Se ferramentas Playwright MCP estiverem disponíveis na sua IDE:
   - Use modo de gravação MCP (Passo 3.B)

   Se MCP indisponível:
   - Fallback para modo de geração IA (silencioso, automático)
   - Continue para Passo 2

   **B. Gravação de Teste Interativa (Baseada em MCP)**

   Use ferramentas test-generator do Playwright MCP:

   **Configuração:**

   ```
   1. Use generator_setup_page para inicializar sessão de gravação
   2. Navegue para URL inicial da aplicação (do contexto da história)
   3. Pronto para gravar interações do usuário
   ```

   **Processo de Gravação (Por Critério de Aceitação):**

   ```
   4. Leia critério de aceitação da história
   5. Execute manualmente cenário de teste usando ferramentas browser_*:
      - browser_navigate: Navegar para páginas
      - browser_click: Clicar botões, links, elementos
      - browser_type: Preencher campos de formulário
      - browser_select: Selecionar opções dropdown
      - browser_check: Marcar/desmarcar checkboxes
   6. Adicione passos de verificação usando ferramentas browser_verify_*:
      - browser_verify_text: Verificar conteúdo de texto
      - browser_verify_visible: Verificar visibilidade de elemento
      - browser_verify_url: Verificar navegação de URL
   7. Capture log de interação com generator_read_log
   8. Gere arquivo de teste com generator_write_test
   9. Repita para o próximo critério de aceitação
   ```

   **Aprimoramento Pós-Gravação:**

   ```
   10. Revise código de teste gerado
   11. Melhore com padrões da base de conhecimento:
       - Adicione comentários Dado-Quando-Então
       - Substitua seletores gravados por data-testid (se necessário)
       - Adicione interceptação network-first (de network-first.md)
       - Adicione fixtures para setup de auth/dados (de fixture-architecture.md)
       - Use fábricas para dados de teste (de data-factories.md)
   12. Verifique se testes falham (implementação ausente)
   13. Continue para Passo 4 (Construir Infraestrutura de Dados)
   ```

   **Quando Usar Modo de Gravação:**
   - ✅ Interações de UI complexas
   - ✅ Fluxos de trabalho visuais
   - ✅ Requisitos pouco claros
   - ✅ Fluxos multi-página
   - ❌ NÃO para CRUD simples
   - ❌ NÃO para testes apenas de API

   **Quando Usar Geração IA (Padrão):**
   - ✅ Critérios de aceitação claros disponíveis
   - ✅ Padrões padrão (login, CRUD, navegação)
   - ✅ Precisa de muitos testes rapidamente
   - ✅ Testes de API/backend

4. **Prosseguir para Seleção de Nível de Teste**

   Após seleção de modo:
   - Geração IA: Continue para Passo 2
   - Gravação: Pule para Passo 4 - testes já gerados

---

## Passo 2: Selecionar Níveis e Estratégia de Teste

### Ações

1. **Analisar Critérios de Aceitação**

   Para cada critério de aceitação, determine:
   - Requer jornada completa do usuário? -> Teste E2E
   - Testa lógica de negócios/contrato de API? -> Teste de API
   - Valida comportamento de componente UI? -> Teste de Componente
   - Pode ser testado unitariamente? -> Teste de Unidade

2. **Aplicar Framework de Seleção de Nível de Teste**

   **Referência da Base de Conhecimento**: `test-levels-framework.md`

   **E2E (Ponta-a-Ponta)**:
   - Jornadas críticas do usuário
   - Integração multi-sistema
   - Critérios de aceitação voltados para o usuário
   - **Características**: Alta confiança, execução lenta, frágil

   **API (Integração)**:
   - Validação de lógica de negócios
   - Contratos de serviço
   - Transformações de dados
   - **Características**: Feedback rápido, bom equilíbrio, estável

   **Componente**:
   - Comportamento de componente UI
   - Teste de interação
   - Regressão visual
   - **Características**: Rápido, isolado, granular

   **Unidade**:
   - Lógica de negócios pura
   - Casos de borda
   - Tratamento de erro
   - **Características**: Mais rápido, mais granular

3. **Evitar Cobertura Duplicada**

   Não teste o mesmo comportamento em múltiplos níveis a menos que necessário.

4. **Priorizar Testes**

   Se documento de design de teste existir, alinhe com níveis de prioridade (P0/P1/P2/P3).

**Ponto de Decisão:** Defina variável `primary_level` para o nível de teste principal para esta história.

---

## Passo 3: Gerar Testes Falhando

### Ações

1. **Criar Estrutura de Arquivo de Teste**

   ```
   tests/
   ├── e2e/
   │   └── {feature-name}.spec.ts        # Testes de aceitação E2E
   ├── api/
   │   └── {feature-name}.api.spec.ts    # Testes de contrato API
   ├── component/
   │   └── {ComponentName}.test.tsx      # Testes de componente
   └── support/
       ├── fixtures/                      # Fixtures de teste
       ├── factories/                     # Fábricas de dados
       └── helpers/                       # Funções utilitárias
   ```

2. **Escrever Testes E2E Falhando (Se Aplicável)**

   **Use formato Dado-Quando-Então**

   **Padrões críticos:**
   - Uma asserção por teste
   - Esperas explícitas (sem esperas duras/sleeps)
   - Abordagem network-first
   - Seletores data-testid
   - Estrutura clara Dado-Quando-Então

3. **Aplicar Padrão Network-First**

   **Referência da Base de Conhecimento**: `network-first.md`

4. **Escrever Testes de API Falhando (Se Aplicável)**

5. **Escrever Testes de Componente Falhando (Se Aplicável)**

6. **Verificar se Testes Falham Inicialmente**

   **Verificação crítica:**
   - Execute testes localmente para confirmar que falham
   - Falha deve ser devido à implementação ausente, não erros de teste
   - Mensagens de falha devem ser claras e acionáveis
   - Todos os testes devem estar na fase VERMELHA

**Importante:** Testes DEVEM falhar inicialmente. Se um teste passa antes da implementação, não é um teste de aceitação válido.

---

## Passo 4: Construir Infraestrutura de Dados

### Ações

1. **Criar Fábricas de Dados**

   **Referência da Base de Conhecimento**: `data-factories.md`

   **Princípios de fábrica:**
   - Use faker para dados aleatórios
   - Suporte overrides
   - Gere objetos válidos completos
   - Inclua funções auxiliares para criação em massa

2. **Criar Fixtures de Teste**

   **Referência da Base de Conhecimento**: `fixture-architecture.md`

   **Princípios de fixture:**
   - Auto-limpeza
   - Componível
   - Isolado
   - Tipo seguro

3. **Documentar Requisitos de Mock**

   Se serviços externos precisarem de simulação, documente requisitos.

4. **Listar Atributos data-testid Necessários**

---

## Passo 5: Criar Lista de Verificação de Implementação

### Ações

1. **Mapear Testes para Tarefas de Implementação**

   Para cada teste falhando, crie tarefa de implementação correspondente.

2. **Incluir Orientação Red-Green-Refactor**

   **Fase VERMELHA** (Completa):
   - ✅ Todos os testes escritos e falhando
   - ✅ Fixtures e fábricas criadas
   - ✅ Requisitos de mock documentados

   **Fase VERDE** (Equipe DEV):
   1. Escolha um teste falhando
   2. Implemente código mínimo para fazê-lo passar
   3. Execute teste para verificar verde
   4. Mova para próximo teste
   5. Repita até que todos os testes passem

   **Fase REFATORAR** (Equipe DEV):
   1. Todos os testes passando (verde)
   2. Melhore qualidade do código
   3. Extraia duplicações
   4. Otimize desempenho
   5. Garanta que testes ainda passem

3. **Adicionar Comandos de Execução**

---

## Passo 6: Gerar Entregáveis

### Ações

1. **Criar Documento de Lista de Verificação ATDD**

   Use estrutura de template em `{installed_path}/atdd-checklist-template.md`.

2. **Verificar se Todos os Testes Falham**

   Antes de finalizar:
   - Execute suíte de teste completa localmente
   - Confirme todos os testes na fase VERMELHA
   - Documente mensagens de falha esperadas

3. **Escrever para Arquivo de Saída**

   Salve em `{output_folder}/atdd-checklist-{story_id}.md`

---

## Notas Importantes

### Ciclo Red-Green-Refactor

**Fase VERMELHA** (responsabilidade TEA):
- Escreva testes falhando primeiro
- Testes definem comportamento esperado
- Testes devem falhar pelo motivo certo

**Fase VERDE** (responsabilidade DEV):
- Implemente código mínimo
- Um teste de cada vez

**Fase REFATORAR** (responsabilidade DEV):
- Melhore qualidade com confiança
- Testes fornecem rede de segurança

### Estrutura Dado-Quando-Então

**DADO** (Setup):
- Organize pré-condições

**QUANDO** (Ação):
- Execute o comportamento

**ENTÃO** (Asserção):
- Verifique resultado esperado

### Teste Network-First

**Padrão crítico:** Intercepte ANTES da navegação.

### Melhores Práticas de Fábrica de Dados

- Use faker para todos os dados de teste
- Princípio de auto-limpeza

### Uma Asserção Por Teste

**Design de teste atômico:** Se a segunda asserção falhar, você não sabe se a primeira ainda é válida.

### Integração da Base de Conhecimento

**Fragmentos Centrais (Auto-carregados no Passo 1):**
- `fixture-architecture.md`
- `data-factories.md`
- `component-tdd.md`
- `network-first.md`
- `test-quality.md`
- `test-healing-patterns.md`
- `selector-resilience.md`
- `timing-debugging.md`

**Referência Manual (Opcional):**
- Use `tea-index.csv`

---

## Resumo de Saída

Após completar este fluxo de trabalho, forneça um resumo:

```markdown
## ATDD Completo - Testes na Fase VERMELHA

**História**: {story_id}
**Nível de Teste Principal**: {primary_level}

**Testes Falhando Criados**:

- Testes E2E: {e2e_count} testes em {e2e_files}
- Testes de API: {api_count} testes em {api_files}
- Testes de Componente: {component_count} testes em {component_files}

**Infraestrutura de Suporte**:

- Fábricas de dados: {factory_count} fábricas criadas
- Fixtures: {fixture_count} fixtures com auto-limpeza
- Requisitos de mock: {mock_count} serviços documentados

**Lista de Verificação de Implementação**:

- Total de tarefas: {task_count}
- Esforço estimado: {effort_estimate} horas

**Atributos data-testid Necessários**: {data_testid_count} atributos documentados

**Próximos Passos para Equipe DEV**:

1. Execute testes falhando: `npm run test:e2e`
2. Revise lista de verificação de implementação
3. Implemente um teste de cada vez (VERMELHO -> VERDE)
4. Refatore com confiança (testes fornecem rede de segurança)
5. Compartilhe progresso na standup diária

**Arquivo de Saída**: {output_file}

**Referências da Base de Conhecimento Aplicadas**:

- Padrões de arquitetura de fixture
- Padrões de fábrica de dados com faker
- Interceptação de rota network-first
- Estratégias TDD de componente
- Princípios de qualidade de teste
```

---

## Validação

Após completar todos os passos, verifique:

- [ ] Critérios de aceitação da história analisados e mapeados para testes
- [ ] Níveis de teste apropriados selecionados (E2E, API, Componente)
- [ ] Todos os testes escritos no formato Dado-Quando-Então
- [ ] Todos os testes falham inicialmente (fase VERMELHA verificada)
- [ ] Padrão network-first aplicado (interceptação de rota antes da navegação)
- [ ] Fábricas de dados criadas com faker
- [ ] Fixtures criadas com auto-limpeza
- [ ] Requisitos de mock documentados para equipe DEV
- [ ] Atributos data-testid necessários listados
- [ ] Lista de verificação de implementação criada com tarefas claras
- [ ] Fluxo de trabalho red-green-refactor documentado
- [ ] Comandos de execução fornecidos
- [ ] Arquivo de saída criado e formatado corretamente

Consulte `checklist.md` para critérios de validação abrangentes.
