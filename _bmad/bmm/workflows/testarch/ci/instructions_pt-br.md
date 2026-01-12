<!-- Powered by BMAD-CORE™ -->

# Configuração de Pipeline CI/CD

**ID do Fluxo de Trabalho**: `_bmad/bmm/testarch/ci`
**Versão**: 4.0 (BMad v6)

---

## Visão Geral

Estrutura um pipeline de qualidade CI/CD pronto para produção com execução de testes, loops de burn-in para detecção de testes flaky, sharding paralelo, coleta de artefatos e configuração de notificação. Este fluxo de trabalho cria configuração de CI específica da plataforma otimizada para feedback rápido e execução confiável de testes.

---

## Requisitos de Pré-voo

**Crítico:** Verifique estes requisitos antes de prosseguir. Se algum falhar, PARE e notifique o usuário.

- ✅ Repositório Git inicializado (diretório `.git/` existe)
- ✅ Suíte de teste local passa (`npm run test:e2e` tem sucesso)
- ✅ Framework de teste configurado (do fluxo de trabalho `framework`)
- ✅ Equipe concorda com a plataforma de CI alvo (GitHub Actions, GitLab CI, Circle CI, etc.)
- ✅ Acesso às configurações/segredos da plataforma de CI disponível (se atualizando pipeline existente)

---

## Passo 1: Executar Verificações de Pré-voo

### Ações

1. **Verificar Repositório Git**
   - Verificar diretório `.git/`
   - Confirmar repositório remoto configurado (`git remote -v`)
   - Se não inicializado, PARE com a mensagem: "Repositório Git necessário para configuração de CI/CD"

2. **Validar Framework de Teste**
   - Procurar por `playwright.config.*` ou `cypress.config.*`
   - Ler configuração do framework para extrair:
     - Localização do diretório de teste
     - Comando de teste
     - Configuração do repórter
     - Configurações de timeout
   - Se não encontrado, PARE com a mensagem: "Execute o fluxo de trabalho `framework` primeiro para configurar a infraestrutura de teste"

3. **Executar Testes Locais**
   - Executar `npm run test:e2e` (ou equivalente do package.json)
   - Garantir que testes passem antes da configuração de CI
   - Se testes falharem, PARE com a mensagem: "Corrija os testes falhando antes de configurar CI/CD"

4. **Detectar Plataforma de CI**
   - Verificar configuração de CI existente:
     - `.github/workflows/*.yml` (GitHub Actions)
     - `.gitlab-ci.yml` (GitLab CI)
     - `.circleci/config.yml` (Circle CI)
     - `Jenkinsfile` (Jenkins)
   - Se encontrado, pergunte ao usuário: "Atualizar configuração de CI existente ou criar nova?"
   - Se não encontrado, detectar plataforma do remoto git:
     - `github.com` -> GitHub Actions (padrão)
     - `gitlab.com` -> GitLab CI
     - Perguntar ao usuário se incapaz de auto-detectar

5. **Ler Configuração de Ambiente**
   - Usar `.nvmrc` para versão do Node se presente
   - Se ausente, padronizar para um LTS atual (Node 24) ou mais novo em vez de uma versão antiga fixa
   - Ler `package.json` para identificar dependências (afeta estratégia de cache)

**Condição de Parada:** Se verificações de pré-voo falharem, pare imediatamente e reporte qual requisito falhou.

---

## Passo 2: Estruturar Pipeline CI

### Ações

1. **Selecionar Template de Plataforma CI**

   Baseado na detecção ou preferência do usuário, use o template apropriado:

   **GitHub Actions** (`.github/workflows/test.yml`):
   - Plataforma mais comum
   - Excelente suporte a cache e matriz
   - Gratuito para repositórios públicos, nível gratuito generoso para privados

   **GitLab CI** (`.gitlab-ci.yml`):
   - Integrado com GitLab
   - Registro e executores embutidos
   - Recursos poderosos de pipeline

   **Circle CI** (`.circleci/config.yml`):
   - Execução rápida com paralelismo
   - Abordagem Docker-first
   - Recursos empresariais

   **Jenkins** (`Jenkinsfile`):
   - Opção self-hosted
   - Customização máxima
   - Requer gerenciamento de infraestrutura

2. **Gerar Configuração de Pipeline**

   Use templates do diretório `{installed_path}/`:
   - `github-actions-template.yml`
   - `gitlab-ci-template.yml`

   **Estágios chave do pipeline:**

   ```yaml
   stages:
     - lint # Verificações de qualidade de código
     - test # Execução de teste (shards paralelos)
     - burn-in # Detecção de teste flaky
     - report # Agregar resultados e publicar
   ```

3. **Configurar Execução de Teste**

   **Sharding Paralelo:**

   ```yaml
   strategy:
     fail-fast: false
     matrix:
       shard: [1, 2, 3, 4]

   steps:
     - name: Run tests
       run: npm run test:e2e -- --shard=${{ matrix.shard }}/${{ strategy.job-total }}
   ```

   **Objetivo:** Divide testes em N trabalhos paralelos para execução mais rápida (alvo: <10 min por shard)

4. **Adicionar Loop de Burn-In**

   **Padrão crítico de sistemas de produção:**

   ```yaml
   burn-in:
     name: Flaky Test Detection
     runs-on: ubuntu-latest
     steps:
       - uses: actions/checkout@v4

       - name: Setup Node
         uses: actions/setup-node@v4
         with:
           node-version-file: '.nvmrc'

       - name: Install dependencies
         run: npm ci

       - name: Run burn-in loop (10 iterations)
         run: |
           for i in {1..10}; do
             echo "🔥 Burn-in iteration $i/10"
             npm run test:e2e || exit 1
           done

       - name: Upload failure artifacts
         if: failure()
         uses: actions/upload-artifact@v4
         with:
           name: burn-in-failures
           path: test-results/
           retention-days: 30
   ```

   **Objetivo:** Roda testes múltiplas vezes para capturar falhas não determinísticas antes de alcançarem a branch principal.

   **Quando rodar:**
   - Em pull requests para main/develop
   - Semanalmente em agendamento cron
   - Após mudanças significativas na infraestrutura de teste

5. **Configurar Cache**

   **Cache de módulos Node:**

   ```yaml
   - name: Cache dependencies
     uses: actions/cache@v4
     with:
       path: ~/.npm
       key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
       restore-keys: |
         ${{ runner.os }}-node-
   ```

   **Cache de binários do navegador (Playwright):**

   ```yaml
   - name: Cache Playwright browsers
     uses: actions/cache@v4
     with:
       path: ~/.cache/ms-playwright
       key: ${{ runner.os }}-playwright-${{ hashFiles('**/package-lock.json') }}
   ```

   **Objetivo:** Reduz tempo de execução de CI em 2-5 minutos por execução.

6. **Configurar Coleta de Artefatos**

   **Apenas artefatos de falha:**

   ```yaml
   - name: Upload test results
     if: failure()
     uses: actions/upload-artifact@v4
     with:
       name: test-results-${{ matrix.shard }}
       path: |
         test-results/
         playwright-report/
       retention-days: 30
   ```

   **Artefatos para coletar:**
   - Traces (Playwright) - contexto completo de depuração
   - Screenshots - evidência visual de falhas
   - Vídeos - reprodução de interação
   - Relatórios HTML - resultados detalhados de teste
   - Logs de console - mensagens de erro e avisos

7. **Adicionar Lógica de Retentativa**

   ```yaml
   - name: Run tests with retries
     uses: nick-invision/retry@v2
     with:
       timeout_minutes: 30
       max_attempts: 3
       retry_on: error
       command: npm run test:e2e
   ```

   **Objetivo:** Lida com falhas transientes (problemas de rede, condições de corrida)

8. **Configurar Notificações** (Opcional)

   Se `notify_on_failure` estiver habilitado:

   ```yaml
   - name: Notify on failure
     if: failure()
     uses: 8398a7/action-slack@v3
     with:
       status: ${{ job.status }}
       text: 'Test failures detected in PR #${{ github.event.pull_request.number }}'
       webhook_url: ${{ secrets.SLACK_WEBHOOK }}
   ```

9. **Gerar Scripts Auxiliares**

   **Script de teste seletivo** (`scripts/test-changed.sh`):

   ```bash
   #!/bin/bash
   # Run only tests for changed files

   CHANGED_FILES=$(git diff --name-only HEAD~1)

   if echo "$CHANGED_FILES" | grep -q "src/.*\.ts$"; then
     echo "Running affected tests..."
     npm run test:e2e -- --grep="$(echo $CHANGED_FILES | sed 's/src\///g' | sed 's/\.ts//g')"
   else
     echo "No test-affecting changes detected"
   fi
   ```

   **Script de espelho local** (`scripts/ci-local.sh`):

   ```bash
   #!/bin/bash
   # Mirror CI execution locally for debugging

   echo "🔍 Running CI pipeline locally..."

   # Lint
   npm run lint || exit 1

   # Tests
   npm run test:e2e || exit 1

   # Burn-in (reduced iterations)
   for i in {1..3}; do
     echo "🔥 Burn-in $i/3"
     npm run test:e2e || exit 1
   done

   echo "✅ Local CI pipeline passed"
   ```

10. **Gerar Documentação**

    **README CI** (`docs/ci.md`):
    - Estágios do pipeline e objetivo
    - Como rodar localmente
    - Depurando execuções de CI falhas
    - Segredos e variáveis de ambiente necessários
    - Configuração de notificação
    - URLs de badge para README

    **Checklist de segredos** (`docs/ci-secrets-checklist.md`):
    - Lista de segredos necessários (SLACK_WEBHOOK, etc.)
    - Onde configurar na plataforma de CI
    - Melhores práticas de segurança

---

## Passo 3: Entregáveis

### Artefatos Primários Criados

1. **Arquivo de Configuração CI**
   - `.github/workflows/test.yml` (GitHub Actions)
   - `.gitlab-ci.yml` (GitLab CI)
   - `.circleci/config.yml` (Circle CI)

2. **Estágios do Pipeline**
   - **Lint**: Verificações de qualidade de código (ESLint, Prettier)
   - **Test**: Execução paralela de teste (4 shards)
   - **Burn-in**: Detecção de teste flaky (10 iterações)
   - **Report**: Agregação de resultado e publicação

3. **Scripts Auxiliares**
   - `scripts/test-changed.sh` - Teste seletivo
   - `scripts/ci-local.sh` - Espelho local de CI
   - `scripts/burn-in.sh` - Execução de burn-in autônoma

4. **Documentação**
   - `docs/ci.md` - Guia de pipeline CI
   - `docs/ci-secrets-checklist.md` - Segredos necessários
   - Comentários inline na configuração de CI

5. **Recursos de Otimização**
   - Cache de dependência (npm, binários do navegador)
   - Sharding paralelo (4 trabalhos padrão)
   - Lógica de retentativa (2 tentativas em falha)
   - Upload de artefato apenas em falha

### Metas de Desempenho

- **Estágio Lint**: <2 minutos
- **Estágio Test** (por shard): <10 minutos
- **Estágio Burn-in**: <30 minutos (10 iterações)
- **Pipeline Total**: <45 minutos

**Aceleração:** 20x mais rápido que execução sequencial através de paralelismo e cache.

---

## Notas Importantes

### Integração da Base de Conhecimento

**Crítico:** Verifique configuração e carregue fragmentos apropriados.

Leia `{config_source}` e verifique `config.tea_use_playwright_utils`.

**Padrões Centrais CI (Sempre carregar):**

- `ci-burn-in.md` - Padrões de loop de burn-in: detecção de 10 iterações, fluxo GitHub Actions, orquestração de shard, execução seletiva
- `selective-testing.md` - Estratégias de detecção de teste alterado: baseadas em tag, filtros de spec, seleção baseada em diff, regras de promoção
- `visual-debugging.md` - Melhores práticas de coleta de artefato: visualizador de trace, gravação HAR, artefatos personalizados, integração de acessibilidade
- `test-quality.md` - Critérios de qualidade de teste específicos de CI: testes determinísticos, isolados com limpeza, asserções explícitas, otimização de tempo/comprimento
- `playwright-config.md` - Configuração otimizada para CI: paralelização, saída de artefato, dependências de projeto, sharding

**Se `config.tea_use_playwright_utils: true`:**

Carregue fragmentos relevantes para CI de playwright-utils:

- `burn-in.md` - Seleção inteligente de teste com análise de git diff (muito importante para otimização CI)
- `network-error-monitor.md` - Detecção automática de HTTP 4xx/5xx (recomendado em pipelines CI)

Recomendação:

- Adicione script de burn-in para validação de pull request
- Habilite monitor de erro de rede em fixtures combinadas para capturar falhas silenciosas
- Referencie documentos completos em fluxos de trabalho `*framework` e `*automate`

### Orientação Específica de Plataforma CI

**GitHub Actions:**

- Use `actions/cache` para cache
- Estratégia de matriz para paralelismo
- Segredos nas configurações do repositório
- Gratuito 2000 minutos/mês para repositórios privados

**GitLab CI:**

- Use `.gitlab-ci.yml` na raiz
- Diretiva `cache:` para cache
- Execução paralela com `parallel: 4`
- Variáveis nas configurações de CI/CD do projeto

**Circle CI:**

- Use `.circleci/config.yml`
- Executores Docker recomendados
- Paralelismo com `parallelism: 4`
- Contexto para segredos compartilhados

### Estratégia de Loop de Burn-In

**Quando rodar:**

- ✅ Em PRs para branches main/develop
- ✅ Semanalmente em agendamento (cron)
- ✅ Após mudanças de infraestrutura de teste
- ❌ Não em todo commit (muito lento)

**Iterações:**

- **10 iterações** para detecção completa
- **3 iterações** para feedback rápido
- **100 iterações** para estabilidade de alta confiança

**Limite de falha:**

- Até MESMO UMA falha em burn-in -> testes são flaky
- Deve corrigir antes de fundir

### Retenção de Artefato

**Apenas artefatos de falha:**

- Economiza custos de armazenamento
- Mantém capacidade de depuração
- Retenção padrão de 30 dias

**Tipos de artefato:**

- Traces (Playwright) - 5-10 MB por teste
- Screenshots - 100-500 KB por screenshot
- Vídeos - 2-5 MB por teste
- Relatórios HTML - 1-2 MB por execução

### Teste Seletivo

**Detectar arquivos alterados:**

```bash
git diff --name-only HEAD~1
```

**Rodar apenas testes afetados:**

- Feedback mais rápido para pequenas mudanças
- Suíte completa ainda roda na branch main
- Reduz tempo de CI em 50-80% para PRs focados

**Compromisso:**

- Pode perder problemas de integração
- Rodar suíte completa pelo menos na fusão

### Espelho Local de CI

**Objetivo:** Depurar falhas de CI localmente

**Uso:**

```bash
./scripts/ci-local.sh
```

**Espelha ambiente CI:**

- Mesma versão Node
- Mesmo comando de teste
- Mesmos estágios (lint -> test -> burn-in)
- Iterações de burn-in reduzidas (3 vs 10)

---

## Resumo de Saída

Após completar este fluxo de trabalho, forneça um resumo:

```markdown
## Pipeline CI/CD Completo

**Plataforma**: GitHub Actions (ou GitLab CI, etc.)

**Artefatos Criados**:

- ✅ Configuração de pipeline: .github/workflows/test.yml
- ✅ Loop de burn-in: 10 iterações para detecção flaky
- ✅ Sharding paralelo: 4 trabalhos para execução rápida
- ✅ Cache: Dependências + binários do navegador
- ✅ Coleta de artefatos: Traces/screenshots/vídeos apenas em falha
- ✅ Scripts auxiliares: test-changed.sh, ci-local.sh, burn-in.sh
- ✅ Documentação: docs/ci.md, docs/ci-secrets-checklist.md

**Desempenho:**

- Lint: <2 min
- Test (por shard): <10 min
- Burn-in: <30 min
- Total: <45 min (20x aceleração vs sequencial)

**Próximos Passos**:

1. Commit configuração CI: `git add .github/workflows/test.yml && git commit -m "ci: add test pipeline"`
2. Push para remoto: `git push`
3. Configurar segredos necessários nas configurações da plataforma CI (veja docs/ci-secrets-checklist.md)
4. Abrir um PR para acionar a primeira execução de CI
5. Monitorar execução do pipeline e ajustar paralelismo se necessário

**Referências da Base de Conhecimento Aplicadas**:

- Padrão de loop de burn-in (ci-burn-in.md)
- Estratégia de teste seletivo (selective-testing.md)
- Coleta de artefato (visual-debugging.md)
- Critérios de qualidade de teste (test-quality.md)
```

---

## Validação

Após completar todos os passos, verifique:

- [ ] Arquivo de configuração CI criado e sintaticamente válido
- [ ] Loop de burn-in configurado (10 iterações)
- [ ] Sharding paralelo habilitado (4 trabalhos)
- [ ] Cache configurado (dependências + navegadores)
- [ ] Coleta de artefato apenas em falha
- [ ] Scripts auxiliares criados e executáveis (`chmod +x`)
- [ ] Documentação completa (ci.md, checklist de segredos)
- [ ] Sem erros ou avisos durante estruturação

Consulte `checklist.md` para critérios de validação abrangentes.
