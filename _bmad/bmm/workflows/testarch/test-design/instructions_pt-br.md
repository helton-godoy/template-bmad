<!-- Alimentado por BMAD-CORE™ -->

# Design de Teste e Avaliação de Risco

**ID do Fluxo de Trabalho**: `_bmad/bmm/testarch/test-design`
**Versão**: 4.0 (BMad v6)

---

## Visão Geral

Planeja estratégia de cobertura de teste abrangente com avaliação de risco, classificação de prioridade e ordem de execução. Este fluxo de trabalho opera em **dois modos**:

- **Modo Nível de Sistema (Fase 3)**: Revisão de testabilidade da arquitetura antes da verificação de portão de solução
- **Modo Nível de Épico (Fase 4)**: Planejamento de teste por épico com avaliação de risco (comportamento atual)

O fluxo de trabalho detecta automaticamente qual modo usar com base na fase do projeto.

---

## Pré-voo: Detectar Modo e Carregar Contexto

**Crítico:** Determinar modo antes de prosseguir.

### Detecção de Modo

1. **Verificar por sprint-status.yaml**
   - Se `{output_folder}/bmm-sprint-status.yaml` existir → **Modo Nível de Épico** (Fase 4)
   - Se NÃO existir → Verificar status do fluxo de trabalho

2. **Verificar workflow-status.yaml**
   - Ler `{output_folder}/bmm-workflow-status.yaml`
   - Se `implementation-readiness: required` ou `implementation-readiness: recommended` → **Modo Nível de Sistema** (Fase 3)
   - Caso contrário → **Modo Nível de Épico** (Fase 4 sem status de sprint ainda)

3. **Requisitos Específicos do Modo**

   **Modo Nível de Sistema (Fase 3 - Revisão de Testabilidade):**
   - ✅ Documento de arquitetura existe (architecture.md ou tech-spec)
   - ✅ PRD existe com requisitos funcionais e não funcionais
   - ✅ Épicos documentados (epics.md)
   - ⚠️ Saída: `{output_folder}/test-design-system.md`

   **Modo Nível de Épico (Fase 4 - Planejamento Por Épico):**
   - ✅ Markdown da história com critérios de aceite disponível
   - ✅ Documentação de PRD ou épico existe para contexto
   - ✅ Documentos de arquitetura disponíveis (opcional mas recomendado)
   - ✅ Requisitos são claros e testáveis
   - ⚠️ Saída: `{output_folder}/test-design-epic-{epic_num}.md`

**Condição de Parada:** Se modo não puder ser determinado ou arquivos necessários ausentes, PARE e notifique usuário com pré-requisitos ausentes.

---

## Passo 1: Carregar Contexto (Ciente do Modo)

**Carregamento Específico do Modo:**

### Modo Nível de Sistema (Fase 3)

1. **Ler Documentação de Arquitetura**
   - Carregar architecture.md ou tech-spec (OBRIGATÓRIO)
   - Carregar PRD.md para requisitos funcionais e não funcionais
   - Carregar epics.md para escopo de funcionalidade
   - Identificar decisões de pilha tecnológica (frameworks, bancos de dados, alvos de implantação)
   - Notar pontos de integração e dependências de sistemas externos
   - Extrair requisitos NFR (SLOs de desempenho, requisitos de segurança, etc.)

2. **Verificar Sinalizador Playwright Utils**

   Ler `{config_source}` e verificar `config.tea_use_playwright_utils`.

   Se verdadeiro, note que `@seontechnologies/playwright-utils` fornece utilitários para implementação de teste. Referencie no design de teste onde relevante.

3. **Carregar Fragmentos da Base de Conhecimento (Nível de Sistema)**

   **Crítico:** Consultar `{project-root}/_bmad/bmm/testarch/tea-index.csv` para carregar:
   - `nfr-criteria.md` - Abordagem de validação NFR (segurança, desempenho, confiabilidade, manutenibilidade)
   - `test-levels-framework.md` - Orientação de estratégia de níveis de teste
   - `risk-governance.md` - Identificação de risco de testabilidade
   - `test-quality.md` - Padrões de qualidade e Definição de Pronto

4. **Analisar Configuração de Teste Existente (se brownfield)**
   - Pesquisar por diretórios de teste existentes
   - Identificar framework de teste atual (se houver)
   - Notar preocupações de testabilidade na base de código existente

### Modo Nível de Épico (Fase 4)

1. **Ler Documentação de Requisitos**
   - Carregar PRD.md para requisitos de produto de alto nível
   - Ler epics.md ou épico específico para escopo de funcionalidade
   - Ler markdown da história para critérios de aceite detalhados
   - Identificar todos os requisitos testáveis

2. **Carregar Contexto de Arquitetura**
   - Ler architecture.md para design de sistema
   - Ler tech-spec para detalhes de implementação
   - Ler test-design-system.md (se existir da Fase 3)
   - Identificar restrições técnicas e dependências
   - Notar pontos de integração e sistemas externos

3. **Analisar Cobertura de Teste Existente**
   - Pesquisar por arquivos de teste existentes em `{test_dir}`
   - Identificar lacunas de cobertura
   - Notar áreas com teste insuficiente
   - Verificar por testes instáveis ou desatualizados

4. **Carregar Fragmentos da Base de Conhecimento (Nível de Épico)**

   **Crítico:** Consultar `{project-root}/_bmad/bmm/testarch/tea-index.csv` para carregar:
   - `risk-governance.md` - Framework de classificação de risco (6 categorias: TECH, SEC, PERF, DATA, BUS, OPS), pontuação automatizada, mecanismo de decisão de portão, rastreamento de dono (625 linhas, 4 exemplos)
   - `probability-impact.md` - Metodologia de pontuação de risco (matriz probabilidade × impacto, classificação automatizada, reavaliação dinâmica, integração de portão, 604 linhas, 4 exemplos)
   - `test-levels-framework.md` - Orientação de seleção de nível de teste (E2E vs API vs Componente vs Unidade com matriz de decisão, características, quando usar cada, 467 linhas, 4 exemplos)
   - `test-priorities-matrix.md` - Critérios de priorização P0-P3 (cálculo de prioridade automatizado, mapeamento baseado em risco, estratégia de tag, orçamentos de tempo, 389 linhas, 2 exemplos)

**Condição de Parada (Apenas Nível de Épico):** Se dados da história ou critérios de aceite estiverem ausentes, verifique se exploração brownfield é necessária. Se nem requisitos NEM exploração possíveis, PARE com mensagem: "Design de teste nível de épico requer requisitos claros, critérios de aceite ou URL de app brownfield para exploração"

---

## Passo 1.5: Revisão de Testabilidade Nível de Sistema (Apenas Fase 3)

**Pule este passo se Modo Nível de Épico.** Este passo executa apenas no Modo Nível de Sistema.

### Ações

1. **Revisar Arquitetura para Testabilidade**

   Avaliar arquitetura contra estes critérios:

   **Controlabilidade:**
   - Podemos controlar estado do sistema para teste? (Semeadura de API, fábricas, reset de banco de dados)
   - As dependências externas são mockáveis? (interfaces, injeção de dependência)
   - Podemos acionar condições de erro? (engenharia de caos, injeção de falha)

   **Observabilidade:**
   - Podemos inspecionar estado do sistema? (registro, métricas, traços)
   - Os resultados de teste são determinísticos? (sem condições de corrida, sucesso/falha claro)
   - Podemos validar NFRs? (métricas de desempenho, logs de auditoria de segurança)

   **Confiabilidade:**
   - Os testes são isolados? (seguro para paralelo, sem estado, disciplina de limpeza)
   - Podemos reproduzir falhas? (esperas determinísticas, captura HAR, dados semente)
   - Componentes são fracamente acoplados? (fronteiras mockáveis, testáveis)

2. **Identificar Requisitos Arquiteturalmente Significativos (ASRs)**

   De NFRs do PRD e decisões de arquitetura, identificar requisitos de qualidade que:
   - Direcionam decisões de arquitetura (e.g., "Deve lidar com 10K usuários concorrentes" → arquitetura de cache)
   - Impõem desafios de testabilidade (e.g., "Tempo de resposta sub-segundo" → infraestrutura de teste de desempenho)
   - Exigem ambientes de teste especiais (e.g., "Implantação multi-região" → instâncias de teste regionais)

   Pontuar cada ASR usando matriz de risco (probabilidade × impacto).

3. **Definir Estratégia de Níveis de Teste**

   Com base na arquitetura (móvel, web, API, microserviços, monólito):
   - Recomendar divisão unidade/integração/E2E (e.g., 70/20/10 para API-pesado, 40/30/30 para UI-pesado)
   - Identificar necessidades de ambiente de teste (local, staging, efêmero, tipo-produção)
   - Definir abordagem de teste por tecnologia (Playwright para web, Maestro para móvel, k6 para desempenho)

4. **Avaliar Abordagem de Teste NFR**

   Para cada categoria NFR:
   - **Segurança**: Testes Auth/authz, validação OWASP, manuseio de segredo (Playwright E2E + ferramentas de segurança)
   - **Desempenho**: Teste de carga/estresse/pico com k6, limiares SLO/SLA
   - **Confiabilidade**: Tratamento de erro, tentativas, disjuntores, verificações de saúde (Playwright + testes de API)
   - **Manutenibilidade**: Metas de cobertura, portões de qualidade de código, validação de observabilidade

5. **Sinalizar Preocupações de Testabilidade**

   Identificar decisões de arquitetura que prejudicam testabilidade:
   - ❌ Acoplamento forte (sem interfaces, dependências rígidas)
   - ❌ Sem injeção de dependência (não pode mockar serviços externos)
   - ❌ Configurações hardcoded (não pode testar diferentes envs)
   - ❌ Observabilidade ausente (não pode validar NFRs)
   - ❌ Designs com estado (não pode paralelizar testes)

   **Crítico:** Se preocupações de testabilidade são bloqueios (e.g., "Arquitetura torna teste de desempenho impossível"), documentar como PREOCUPAÇÕES ou recomendação FALHA para verificação de portão.

6. **Saída Design de Teste Nível de Sistema**

   Escrever para `{output_folder}/test-design-system.md` contendo:

   ```markdown
   # Design de Teste Nível de Sistema

   ## Avaliação de Testabilidade

   - Controlabilidade: [PASSOU/PREOCUPAÇÕES/FALHOU com detalhes]
   - Observabilidade: [PASSOU/PREOCUPAÇÕES/FALHOU com detalhes]
   - Confiabilidade: [PASSOU/PREOCUPAÇÕES/FALHOU com detalhes]

   ## Requisitos Arquiteturalmente Significativos (ASRs)

   [Requisitos de qualidade pontuados por risco]

   ## Estratégia de Níveis de Teste

   - Unidade: [X%] - [Racional]
   - Integração: [Y%] - [Racional]
   - E2E: [Z%] - [Racional]

   ## Abordagem de Teste NFR

   - Segurança: [Abordagem com ferramentas]
   - Desempenho: [Abordagem com ferramentas]
   - Confiabilidade: [Abordagem com ferramentas]
   - Manutenibilidade: [Abordagem com ferramentas]

   ## Requisitos de Ambiente de Teste

   [Necessidades de infraestrutura baseadas na arquitetura de implantação]

   ## Preocupações de Testabilidade (se houver)

   [Bloqueios ou preocupações que devem informar verificação de portão de solução]

   ## Recomendações para Sprint 0

   [Ações específicas para fluxos de trabalho *framework e *ci]
   ```

**Após Modo Nível de Sistema:** Pular para Passo 4 (Gerar Entregáveis) - Passos 2-3 são apenas nível de épico.

---

## Passo 1.6: Seleção de Modo Exploratório (Apenas Nível de Épico)

### Ações

1. **Detectar Modo de Planejamento**

   Determinar modo com base no contexto:

   **Modo Baseado em Requisitos (PADRÃO)**:
   - Tem história/PRD clara com critérios de aceite
   - Usa: Fluxo de trabalho existente (Passos 2-4)
   - Apropriado para: Funcionalidades documentadas, projetos greenfield

   **Modo Exploratório (OPCIONAL - Brownfield)**:
   - Requisitos ausentes/incompletos E aplicação brownfield existe
   - Usa: Exploração de UI para descobrir funcionalidade
   - Apropriado para: Apps brownfield não documentados, sistemas legados

2. **Modo Baseado em Requisitos (PADRÃO - Pular para Passo 2)**

   Se requisitos são claros:
   - Continuar com fluxo de trabalho existente (Passo 2: Avaliar e Classificar Riscos)
   - Usar requisitos carregados do Passo 1
   - Prosseguir com avaliação de risco baseada em requisitos documentados

3. **Modo Exploratório (OPCIONAL - Apps Brownfield)**

   Se explorando aplicação brownfield:

   **A. Verificar Disponibilidade MCP**

   Se config.tea_use_mcp_enhancements for verdadeiro E ferramentas MCP Playwright disponíveis:
   - Usar exploração assistida por MCP (Passo 3.B)

   Se MCP indisponível OU config.tea_use_mcp_enhancements for falso:
   - Usar fallback de exploração manual (Passo 3.C)

   **B. Exploração Assistida por MCP (Se Ferramentas MCP Disponíveis)**

   Usar ferramentas de navegador MCP Playwright para explorar UI:

   **Configuração:**

   ```
   1. Usar planner_setup_page para inicializar navegador
   2. Navegar para {exploration_url}
   3. Capturar estado inicial com browser_snapshot
   ```

   **Processo de Exploração:**

   ```
   4. Usar browser_navigate para explorar páginas diferentes
   5. Usar browser_click para interagir com botões, links, formulários
   6. Usar browser_hover para revelar menus/dicas ocultos
   7. Capturar browser_snapshot em cada estado significativo
   8. Tirar browser_screenshot para documentação
   9. Monitorar browser_console_messages para erros JavaScript
   10. Rastrear browser_network_requests para identificar chamadas de API
   11. Mapear fluxos de usuário e elementos interativos
   12. Documentar funcionalidade descoberta
   ```

   **Documentação de Descoberta:**
   - Criar lista de funcionalidades descobertas (páginas, fluxos de trabalho, formulários)
   - Identificar jornadas de usuário (caminhos de navegação)
   - Mapear endpoints de API (de requisições de rede)
   - Notar estados de erro (de mensagens de console)
   - Capturar screenshots para referência visual

   **Converter para Cenários de Teste:**
   - Transformar descobertas em requisitos testáveis
   - Priorizar com base na criticidade do fluxo de usuário
   - Identificar riscos de funcionalidade descoberta
   - Continuar com Passo 2 (Avaliar e Classificar Riscos) usando requisitos descobertos

   **C. Fallback de Exploração Manual (Se MCP Indisponível)**

   Se MCP Playwright não estiver disponível:

   **Notificar Usuário:**

   ```markdown
   Modo exploratório habilitado mas MCP Playwright indisponível.

   **Exploração manual necessária:**

   1. Abra aplicação em: {exploration_url}
   2. Explore todas as páginas, fluxos de trabalho e funcionalidades
   3. Documente descobertas em markdown:
      - Lista de páginas/funcionalidades descobertas
      - Jornadas de usuário identificadas
      - Endpoints de API observados (Aba Rede DevTools)
      - Erros JavaScript notados (Console DevTools)
      - Fluxos de trabalho críticos mapeados

   4. Forneça descobertas de exploração para continuar

   **Alternativa:** Desabilite exploratory_mode e forneça documentação de requisitos
   ```

   Aguarde usuário fornecer descobertas de exploração, então:
   - Analisar documentação de descoberta fornecida pelo usuário
   - Converter para requisitos testáveis
   - Continuar com Passo 2 (avaliação de risco)

4. **Prosseguir para Avaliação de Risco**

   Após seleção de modo (Baseado em Requisitos OU Exploratório):
   - Continuar para Passo 2: Avaliar e Classificar Riscos
   - Usar requisitos de documentação (Baseado em Requisitos) OU descobertas (Exploratório)

---

## Passo 2: Avaliar e Classificar Riscos

### Ações

1. **Identificar Riscos Genuínos**

   Filtrar requisitos para isolar riscos reais (não apenas funcionalidades):
   - Lacunas técnicas não resolvidas
   - Vulnerabilidades de segurança
   - Gargalos de desempenho
   - Potencial de perda ou corrupção de dados
   - Falhas de impacto no negócio
   - Problemas operacionais de implantação

2. **Classificar Riscos por Categoria**

   Usar estas categorias de risco padrão:

   **TECH** (Técnico/Arquitetura):
   - Falhas de arquitetura
   - Falhas de integração
   - Problemas de escalabilidade
   - Dívida técnica

   **SEC** (Segurança):
   - Controles de acesso ausentes
   - Desvio de autenticação
   - Exposição de dados
   - Vulnerabilidades de injeção

   **PERF** (Desempenho):
   - Violações de SLA
   - Degradação de tempo de resposta
   - Exaustão de recursos
   - Limites de escalabilidade

   **DATA** (Integridade de Dados):
   - Perda de dados
   - Corrupção de dados
   - Estado inconsistente
   - Falhas de migração

   **BUS** (Impacto no Negócio):
   - Degradação de experiência do usuário
   - Erros de lógica de negócio
   - Impacto na receita
   - Violações de conformidade

   **OPS** (Operações):
   - Falhas de implantação
   - Erros de configuração
   - Lacunas de monitoramento
   - Problemas de reversão

3. **Pontuar Probabilidade de Risco**

   Avaliar probabilidade (1-3):
   - **1 (Improvável)**: <10% chance, caso de borda
   - **2 (Possível)**: 10-50% chance, cenário conhecido
   - **3 (Provável)**: >50% chance, ocorrência comum

4. **Pontuar Impacto de Risco**

   Avaliar gravidade (1-3):
   - **1 (Menor)**: Cosmético, solução alternativa existe, usuários limitados
   - **2 (Degradado)**: Funcionalidade prejudicada, solução alternativa difícil, afeta muitos usuários
   - **3 (Crítico)**: Falha de sistema, perda de dados, sem solução alternativa, bloqueia uso

5. **Calcular Pontuação de Risco**

   ```
   Pontuação de Risco = Probabilidade × Impacto

   Pontuações:
   1-2: Risco baixo (monitorar)
   3-4: Risco médio (planejar mitigação)
   6-9: Risco alto (mitigação imediata necessária)
   ```

6. **Destacar Riscos de Alta Prioridade**

   Sinalizar todos os riscos com pontuação ≥6 para atenção imediata.

7. **Solicitar Esclarecimento**

   Se evidência estiver faltando ou suposições necessárias:
   - Documentar suposições claramente
   - Solicitar esclarecimento do usuário
   - NÃO especular sobre impacto no negócio

8. **Planejar Mitigações**

   Para cada risco de alta prioridade:
   - Definir estratégia de mitigação
   - Atribuir dono (dev, QA, ops)
   - Definir cronograma
   - Atualizar expectativa de risco residual

---

## Passo 3: Projetar Cobertura de Teste

### Ações

1. **Decompor Critérios de Aceite**

   Converter cada critério de aceite em cenários de teste atômicos:
   - Um cenário por comportamento testável
   - Cenários são independentes
   - Cenários são repetíveis
   - Cenários ligam de volta a mitigações de risco

2. **Selecionar Níveis de Teste Apropriados**

   **Referência Base de Conhecimento**: `test-levels-framework.md`

   Mapear requisitos para níveis de teste ótimos (evitar duplicação):

   **E2E (Ponta-a-Ponta)**:
   - Jornadas de usuário críticas
   - Integração multi-sistema
   - Ambiente tipo produção
   - Maior confiança, execução mais lenta

   **API (Integração)**:
   - Contratos de serviço
   - Validação de lógica de negócio
   - Feedback rápido
   - Bom para cenários complexos

   **Componente**:
   - Comportamento de componente UI
   - Teste de interação
   - Regressão visual
   - Rápido, isolado

   **Unidade**:
   - Lógica de negócio
   - Casos de borda
   - Tratamento de erro
   - Mais rápido, mais granular

   **Evitar cobertura duplicada**: Não teste o mesmo comportamento em múltiplos níveis a menos que necessário.

3. **Atribuir Níveis de Prioridade**

   **Referência Base de Conhecimento**: `test-priorities-matrix.md`

   **P0 (Crítico)**:
   - Bloqueia jornada central do usuário
   - Áreas de alto risco (pontuação ≥6)
   - Impacto na receita
   - Crítico para segurança
   - **Rodar em todo commit**

   **P1 (Alto)**:
   - Funcionalidades importantes de usuário
   - Áreas de risco médio (pontuação 3-4)
   - Fluxos de trabalho comuns
   - **Rodar em PR para main**

   **P2 (Médio)**:
   - Funcionalidades secundárias
   - Áreas de baixo risco (pontuação 1-2)
   - Casos de borda
   - **Rodar noturnamente ou semanalmente**

   **P3 (Baixo)**:
   - Bom-ter
   - Exploratório
   - Benchmarks de desempenho
   - **Rodar sob demanda**

4. **Esboçar Pré-requisitos de Dados e Ferramentas**

   Para cada cenário de teste, identificar:
   - Requisitos de dados de teste (fábricas, fixtures)
   - Serviços externos (mocks, stubs)
   - Configuração de ambiente
   - Ferramentas e dependências

5. **Definir Ordem de Execução**

   Recomendar sequência de execução de teste:
   1. **Testes de fumaça** (subconjunto P0, <5 min)
   2. **Testes P0** (caminhos críticos, <10 min)
   3. **Testes P1** (funcionalidades importantes, <30 min)
   4. **Testes P2/P3** (regressão completa, <60 min)

---

## Passo 4: Gerar Entregáveis

### Ações

1. **Criar Matriz de Avaliação de Risco**

   Usar estrutura de modelo:

   ```markdown
   | ID Risco | Categoria | Descrição | Probabilidade | Impacto | Pontuação | Mitigação      |
   | -------- | --------- | --------- | ------------- | ------- | --------- | -------------- |
   | R-001    | SEC       | Auth bypass | 2           | 3      | 6     | Add authz check |
   ```

2. **Criar Matriz de Cobertura**

   ```markdown
   | Requisito | Nível Teste | Prioridade | Link Risco | Contagem Teste | Dono |
   | --------- | ----------- | ---------- | ---------- | -------------- | ---- |
   | Login flow  | E2E        | P0       | R-001     | 3          | QA    |
   ```

3. **Documentar Ordem de Execução**

   ```markdown
   ### Testes de Fumaça (<5 min)

   - Login bem-sucedido
   - Dashboard carrega

   ### Testes P0 (<10 min)

   - [Lista P0 completa]

   ### Testes P1 (<30 min)

   - [Lista P1 completa]
   ```

4. **Incluir Estimativas de Recursos**

   ```markdown
   ### Estimativas de Esforço de Teste

   - Cenários P0: 15 testes × 2 horas = 30 horas
   - Cenários P1: 25 testes × 1 hora = 25 horas
   - Cenários P2: 40 testes × 0.5 hora = 20 horas
   - **Total:** 75 horas (~10 dias)
   ```

5. **Adicionar Critérios de Portão**

   ```markdown
   ### Critérios de Portão de Qualidade

   - Todos testes P0 passam (100%)
   - Taxa de aprovação testes P1 ≥95%
   - Nenhum item de alto risco (pontuação ≥6) não mitigado
   - Cobertura de teste ≥80% para caminhos críticos
   ```

6. **Escrever para Arquivo de Saída**

   Salvar em `{output_folder}/test-design-epic-{epic_num}.md` usando estrutura de modelo.

---

## Notas Importantes

### Definições de Categoria de Risco

**TECH** (Técnico/Arquitetura):

- Falhas de arquitetura ou dívida técnica
- Complexidade de integração
- Preocupações de escalabilidade

**SEC** (Segurança):

- Controles de segurança ausentes
- Lacunas de autenticação/autorização
- Riscos de exposição de dados

**PERF** (Desempenho):

- Risco de SLA ou degradação de desempenho
- Restrições de recursos
- Gargalos de escalabilidade

**DATA** (Integridade de Dados):

- Potencial de perda ou corrupção de dados
- Problemas de consistência de estado
- Riscos de migração

**BUS** (Impacto no Negócio):

- Dano à experiência do usuário
- Erros de lógica de negócio
- Impacto na receita ou conformidade

**OPS** (Operações):

- Falhas de implantação ou tempo de execução
- Problemas de configuração
- Lacunas de monitoramento/observabilidade

### Metodologia de Pontuação de Risco

**Probabilidade × Impacto = Pontuação de Risco**

Exemplos:

- Alta probabilidade (3) × Impacto crítico (3) = **Pontuação 9** (prioridade mais alta)
- Possível (2) × Crítico (3) = **Pontuação 6** (limiar de alta prioridade)
- Improvável (1) × Menor (1) = **Pontuação 1** (prioridade baixa)

**Limiar**: Pontuações ≥6 requerem mitigação imediata.

### Estratégia de Seleção de Nível de Teste

**Evitar duplicação:**

- Não teste o mesmo comportamento em nível E2E e API
- Use E2E apenas para caminhos críticos
- Use testes de API para lógica de negócio complexa
- Use testes de unidade para casos de borda

**Compromissos:**

- E2E: Alta confiança, execução lenta, frágil
- API: Bom equilíbrio, rápido, estável
- Unidade: Feedback mais rápido, escopo estreito

### Diretrizes de Atribuição de Prioridade

**Critérios P0** (todos devem ser verdadeiros):

- Bloqueia funcionalidade central
- Alto risco (pontuação ≥6)
- Nenhuma solução alternativa existe
- Afeta maioria dos usuários

**Critérios P1**:

- Funcionalidade importante
- Risco médio (pontuação 3-5)
- Solução alternativa existe mas difícil

**P2/P3**: Todo o resto, priorizado por valor

### Integração com Base de Conhecimento

**Fragmentos Centrais (Auto-carregados no Passo 1):**

- `risk-governance.md` - Classificação de risco (6 categorias), pontuação automatizada, mecanismo de decisão de portão, rastreabilidade de cobertura, rastreamento de dono (625 linhas, 4 exemplos)
- `probability-impact.md` - Matriz probabilidade × impacto, limiares de classificação automatizada, reavaliação dinâmica, integração de portão (604 linhas, 4 exemplos)
- `test-levels-framework.md` - Framework de decisão E2E vs API vs Componente vs Unidade com matriz de características (467 linhas, 4 exemplos)
- `test-priorities-matrix.md` - Priorização P0-P3, cálculo automatizado de prioridade, mapeamento baseado em risco, estratégia de tag, orçamentos de tempo (389 linhas, 2 exemplos)

**Referência para Planejamento de Teste:**

- `selective-testing.md` - Estratégia de execução: baseada em tag, filtros de spec, seleção baseada em diff, regras de promoção (727 linhas, 4 exemplos)
- `fixture-architecture.md` - Padrões de configuração de dados: função pura → fixture → mergeTests, auto-limpeza (406 linhas, 5 exemplos)

**Referência Manual (Opcional):**

- Use `tea-index.csv` para encontrar fragmentos especializados adicionais conforme necessário

### Avaliação Baseada em Evidência

**Princípio crítico:** Baseie avaliação de risco em evidência, não especulação.

**Fontes de evidência:**

- PRD e pesquisa de usuário
- Documentação de arquitetura
- Dados históricos de bug
- Feedback de usuário
- Resultados de auditoria de segurança

**Evitar:**

- Adivinhar impacto no negócio
- Assumir comportamento do usuário
- Inventar requisitos

**Quando incerto:** Documentar suposições e solicitar esclarecimento do usuário.

---

## Resumo de Saída

Após completar este fluxo de trabalho, forneça um resumo:

```markdown
## Design de Teste Completo

**Épico**: {epic_num}
**Escopo**: {design_level}

**Avaliação de Risco**:

- Total de riscos identificados: {count}
- Riscos de alta prioridade (≥6): {high_count}
- Categorias: {categories}

**Plano de Cobertura**:

- Cenários P0: {p0_count} ({p0_hours} horas)
- Cenários P1: {p1_count} ({p1_hours} horas)
- Cenários P2/P3: {p2p3_count} ({p2p3_hours} horas)
- **Esforço total**: {total_hours} horas (~{total_days} dias)

**Níveis de Teste**:

- E2E: {e2e_count}
- API: {api_count}
- Componente: {component_count}
- Unidade: {unit_count}

**Critérios de Portão de Qualidade**:

- Taxa de aprovação P0: 100%
- Taxa de aprovação P1: ≥95%
- Mitigações de alto risco: 100%
- Cobertura: ≥80%

**Arquivo de Saída**: {output_file}

**Próximos Passos**:

1. Revisar avaliação de risco com equipe
2. Priorizar mitigação para itens de alto risco (pontuação ≥6)
3. Executar fluxo de trabalho `atdd` para gerar testes com falha para cenários P0
4. Alocar recursos por estimativas de esforço
5. Configurar fábricas de dados de teste e fixtures
```

---

## Validação

Após completar todos os passos, verifique:

- [ ] Avaliação de risco completa com todas as categorias
- [ ] Todos os riscos pontuados (probabilidade × impacto)
- [ ] Riscos de alta prioridade (≥6) sinalizados
- [ ] Matriz de cobertura mapeia requisitos para níveis de teste
- [ ] Níveis de prioridade atribuídos (P0-P3)
- [ ] Ordem de execução definida
- [ ] Estimativas de recursos fornecidas
- [ ] Critérios de portão de qualidade definidos
- [ ] Arquivo de saída criado e formatado corretamente

Consulte `checklist.md` para critérios de validação abrangentes.
