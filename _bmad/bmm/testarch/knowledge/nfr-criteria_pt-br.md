# Critérios de Requisitos Não Funcionais (NFR)

## Princípio

Requisitos não funcionais (segurança, performance, confiabilidade, manutenibilidade) são **validados através de testes automatizados**, não checklists. A avaliação de NFR usa critérios objetivos de passa/falha ligados a limites mensuráveis. Requisitos ambíguos padrão para PREOCUPAÇÕES até serem clarificados.

## Motivação

**O Problema**: Times enviam funcionalidades que "funcionam" funcionalmente mas falham sob carga, expõem vulnerabilidades de segurança ou carecem de recuperação de erro. NFRs são tratados como opcionais "bons de ter" em vez de bloqueadores de lançamento.

**A Solução**: Defina critérios NFR explícitos com validação automatizada. Testes de segurança verificam auth/authz e manipulação de segredos. Testes de performance impõem limites SLO/SLA com evidência de profiling. Testes de confiabilidade validam tratamento de erro, retentativas e verificações de saúde. Manutenibilidade é medida por cobertura de teste, duplicação de código e observabilidade.

**Por Que Isso Importa**:

- Previne incidentes de produção (brechas de segurança, degradação de performance, falhas em cascata)
- Fornece critérios de lançamento objetivos (sem "parece rápido o suficiente" subjetivo)
- Automatiza validação de conformidade (trilha de auditoria para ambientes regulados)
- Força clareza em requisitos ambíguos (padrão para PREOCUPAÇÕES)

## Exemplos de Padrões

### Exemplo 1: Validação de NFR de Segurança (Auth, Segredos, OWASP)

**Contexto**: Testes de segurança automatizados impondo autenticação, autorização e manipulação de segredos

**Implementação**:

```typescript
// tests/nfr/security.spec.ts
import { test, expect } from '@playwright/test';

test.describe('NFR de Segurança: Autenticação & Autorização', () => {
  test('usuários não autenticados não podem acessar rotas protegidas', async ({ page }) => {
    // Tentar acessar dashboard sem auth
    await page.goto('/dashboard');

    // Deve redirecionar para login (não expor dados)
    await expect(page).toHaveURL(/\/login/);
    await expect(page.getByText('Por favor entre')).toBeVisible();

    // Verificar se nenhum dado sensível vazou na resposta
    const pageContent = await page.content();
    expect(pageContent).not.toContain('user_id');
    expect(pageContent).not.toContain('api_key');
  });

  test('Tokens JWT expiram após 15 minutos', async ({ page, request }) => {
    // Login e capturar token
    await page.goto('/login');
    await page.getByLabel('Email').fill('test@example.com');
    await page.getByLabel('Senha').fill('SenhaValida123!');
    await page.getByRole('button', { name: 'Entrar' }).click();

    const token = await page.evaluate(() => localStorage.getItem('auth_token'));
    expect(token).toBeTruthy();

    // Esperar 16 minutos (usar relógio mock em testes reais)
    await page.clock.fastForward('00:16:00');

    // Token deve estar expirado, chamada de API deve falhar
    const response = await request.get('/api/user/profile', {
      headers: { Authorization: `Bearer ${token}` },
    });

    expect(response.status()).toBe(401);
    const body = await response.json();
    expect(body.error).toContain('expirado');
  });

  test('senhas nunca são logadas ou expostas em erros', async ({ page }) => {
    // Disparar erro de login
    await page.goto('/login');
    await page.getByLabel('Email').fill('test@example.com');
    await page.getByLabel('Senha').fill('SenhaErrada123!');

    // Monitorar console para vazamentos de senha
    const consoleLogs: string[] = [];
    page.on('console', (msg) => consoleLogs.push(msg.text()));

    await page.getByRole('button', { name: 'Entrar' }).click();

    // Erro mostrado ao usuário (mensagem genérica)
    await expect(page.getByText('Credenciais inválidas')).toBeVisible();

    // Verificar que senha NUNCA aparece no console, DOM ou rede
    const pageContent = await page.content();
    expect(pageContent).not.toContain('SenhaErrada123!');
    expect(consoleLogs.join('\n')).not.toContain('SenhaErrada123!');
  });

  test('RBAC: usuários só podem acessar recursos que possuem', async ({ page, request }) => {
    // Login como Usuário A
    const userAToken = await login(request, 'userA@example.com', 'senha');

    // Tentar acessar pedido do Usuário B
    const response = await request.get('/api/orders/user-b-order-id', {
      headers: { Authorization: `Bearer ${userAToken}` },
    });

    expect(response.status()).toBe(403); // Proibido
    const body = await response.json();
    expect(body.error).toContain('permissões insuficientes');
  });

  test('tentativas de injeção SQL são bloqueadas', async ({ page }) => {
    await page.goto('/search');

    // Tentar injeção SQL
    await page.getByPlaceholder('Buscar produtos').fill("'; DROP TABLE users; --");
    await page.getByRole('button', { name: 'Buscar' }).click();

    // Deve retornar resultados vazios, NÃO quebrar ou expor erro
    await expect(page.getByText('Nenhum resultado encontrado')).toBeVisible();

    // Verificar que app ainda funciona (tabela não removida)
    await page.goto('/dashboard');
    await expect(page.getByText('Bem-vindo')).toBeVisible();
  });

  test('tentativas de XSS são higienizadas', async ({ page }) => {
    await page.goto('/profile/edit');

    // Tentar injeção XSS
    const xssPayload = '<script>alert("XSS")</script>';
    await page.getByLabel('Bio').fill(xssPayload);
    await page.getByRole('button', { name: 'Salvar' }).click();

    // Recarregar e verificar que XSS é escapado (não executado)
    await page.reload();
    const bio = await page.getByTestId('user-bio').textContent();

    // Texto deve ser escapado, script NÃO deve executar
    expect(bio).toContain('&lt;script&gt;');
    expect(bio).not.toContain('<script>');
  });
});

// Helper
async function login(request: any, email: string, password: string): Promise<string> {
  const response = await request.post('/api/auth/login', {
    data: { email, password },
  });
  const body = await response.json();
  return body.token;
}
```

**Pontos Chave**:

- Autenticação: Acesso não autenticado redirecionado (não exposto)
- Autorização: RBAC imposto (403 para permissões insuficientes)
- Expiração de token: JWT expira após 15 minutos (validação automatizada)
- Manipulação de segredo: Senhas nunca logadas ou expostas em erros
- OWASP Top 10: Injeção SQL e XSS bloqueados (higienização de entrada)

**Critérios NFR de Segurança**:

- ✅ PASSOU: Todos os 6 testes verdes (auth, authz, expiração de token, manipulação de segredo, injeção SQL, XSS)
- ⚠️ PREOCUPAÇÕES: 1-2 testes falhando com plano de mitigação e proprietário atribuído
- ❌ FALHOU: Exposição crítica (acesso não autenticado, vazamento de senha, injeção SQL sucede)

---

### Exemplo 2: Validação de NFR de Performance (Teste de Carga k6 para SLO/SLA)

**Contexto**: Use k6 para teste de carga, teste de estresse e imposição de SLO/SLA (NÃO Playwright)

**Implementação**:

```javascript
// tests/nfr/performance.k6.js
import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate, Trend } from 'k6/metrics';

// Métricas customizadas
const errorRate = new Rate('errors');
const apiDuration = new Trend('api_duration');

// Limites de performance (SLO/SLA)
export const options = {
  stages: [
    { duration: '1m', target: 50 }, // Subir para 50 usuários
    { duration: '3m', target: 50 }, // Ficar em 50 usuários por 3 minutos
    { duration: '1m', target: 100 }, // Pico para 100 usuários
    { duration: '3m', target: 100 }, // Ficar em 100 usuários
    { duration: '1m', target: 0 }, // Descer
  ],
  thresholds: {
    // SLO: 95% das requisições devem completar em <500ms
    http_req_duration: ['p(95)<500'],
    // SLO: Taxa de erro deve ser <1%
    errors: ['rate<0.01'],
    // SLA: Endpoints de API devem responder em <1s (percentil 99)
    api_duration: ['p(99)<1000'],
  },
};

export default function () {
  // Teste 1: Performance de carregamento da Homepage
  const homepageResponse = http.get(`${__ENV.BASE_URL}/`);
  check(homepageResponse, {
    'status homepage é 200': (r) => r.status === 200,
    'homepage carrega em <2s': (r) => r.timings.duration < 2000,
  });
  errorRate.add(homepageResponse.status !== 200);

  // Teste 2: Performance de endpoint de API
  const apiResponse = http.get(`${__ENV.BASE_URL}/api/products?limit=10`, {
    headers: { Authorization: `Bearer ${__ENV.API_TOKEN}` },
  });
  check(apiResponse, {
    'status API é 200': (r) => r.status === 200,
    'API responde em <500ms': (r) => r.timings.duration < 500,
  });
  apiDuration.add(apiResponse.timings.duration);
  errorRate.add(apiResponse.status !== 200);

  // Teste 3: Endpoint de busca sob carga
  const searchResponse = http.get(`${__ENV.BASE_URL}/api/search?q=laptop&limit=100`);
  check(searchResponse, {
    'status busca é 200': (r) => r.status === 200,
    'busca responde em <1s': (r) => r.timings.duration < 1000,
    'busca retorna resultados': (r) => JSON.parse(r.body).results.length > 0,
  });
  errorRate.add(searchResponse.status !== 200);

  sleep(1); // Tempo de pensamento do usuário realista
}

// Validação de limite (rodar após teste)
export function handleSummary(data) {
  const p95Duration = data.metrics.http_req_duration.values['p(95)'];
  const p99ApiDuration = data.metrics.api_duration.values['p(99)'];
  const errorRateValue = data.metrics.errors.values.rate;

  console.log(`Duração requisição P95: ${p95Duration.toFixed(2)}ms`);
  console.log(`Duração API P99: ${p99ApiDuration.toFixed(2)}ms`);
  console.log(`Taxa de erro: ${(errorRateValue * 100).toFixed(2)}%`);

  return {
    'summary.json': JSON.stringify(data),
    stdout: `
Resultados NFR de Performance:
- Duração requisição P95: ${p95Duration < 500 ? '✅ PASSOU' : '❌ FALHOU'} (${p95Duration.toFixed(2)}ms / 500ms limite)
- Duração API P99: ${p99ApiDuration < 1000 ? '✅ PASSOU' : '❌ FALHOU'} (${p99ApiDuration.toFixed(2)}ms / 1000ms limite)
- Taxa de erro: ${errorRateValue < 0.01 ? '✅ PASSOU' : '❌ FALHOU'} (${(errorRateValue * 100).toFixed(2)}% / 1% limite)
    `,
  };
}
```

**Rodar testes k6:**

```bash
# Smoke test local (10 VUs, 30s)
k6 run --vus 10 --duration 30s tests/nfr/performance.k6.js

# Teste de carga completo (estágios definidos no script)
k6 run tests/nfr/performance.k6.js

# Integração CI com limites
k6 run --out json=performance-results.json tests/nfr/performance.k6.js
```

**Pontos Chave**:

- **k6 é a ferramenta certa** para teste de carga (NÃO Playwright)
- Limites SLO/SLA impostos automaticamente (`p(95)<500`, `rate<0.01`)
- Simulação de carga realista (subida, carga sustentada, teste de pico)
- Métricas abrangentes (p50, p95, p99, taxa de erro, vazão)
- Amigável para CI (saída JSON, códigos de saída baseados em limites)

**Critérios NFR de Performance**:

- ✅ PASSOU: Todos os alvos SLO/SLA atendidos com evidência de profiling k6 (p95 < 500ms, taxa de erro < 1%)
- ⚠️ PREOCUPAÇÕES: Tendendo para limites (ex: p95 = 480ms aproximando 500ms) ou baselines faltando
- ❌ FALHOU: SLO/SLA violado (ex: p95 > 500ms) ou taxa de erro > 1%

**Níveis de Teste de Performance (do curso Arquiteto de Teste):**

- **Teste de carga**: Comportamento do sistema sob carga esperada
- **Teste de estresse**: Comportamento do sistema sob carga extrema (ponto de quebra)
- **Teste de pico**: Aumentos repentinos de carga (picos de tráfego)
- **Teste de resistência/Soak**: Comportamento do sistema sob carga sustentada (vazamentos de memória, exaustão de recursos)
- **Benchmarking**: Medidas de base para comparação

**Nota**: Playwright pode validar **performance percebida** (Core Web Vitals via Lighthouse), mas k6 valida **performance do sistema** (vazão, latência, limites de recurso sob carga)

---

### Exemplo 3: Validação de NFR de Confiabilidade (Playwright para Resiliência de UI)

**Contexto**: Testes de confiabilidade automatizados validando degradação graciosa e caminhos de recuperação

**Implementação**:

```typescript
// tests/nfr/reliability.spec.ts
import { test, expect } from '@playwright/test';

test.describe('NFR de Confiabilidade: Tratamento de Erro & Recuperação', () => {
  test('app permanece funcional quando API retorna erro 500', async ({ page, context }) => {
    // Mock falha de API
    await context.route('**/api/products', (route) => {
      route.fulfill({ status: 500, body: JSON.stringify({ error: 'Erro Interno do Servidor' }) });
    });

    await page.goto('/products');

    // Usuário vê mensagem de erro (não página branca ou crash)
    await expect(page.getByText('Incapaz de carregar produtos. Por favor tente novamente.')).toBeVisible();
    await expect(page.getByRole('button', { name: 'Tentar Novamente' })).toBeVisible();

    // Navegação do app ainda funciona (degradação graciosa)
    await page.getByRole('link', { name: 'Início' }).click();
    await expect(page).toHaveURL('/');
  });

  test('cliente API tenta novamente em falhas transitórias (3 tentativas)', async ({ page, context }) => {
    let attemptCount = 0;

    await context.route('**/api/checkout', (route) => {
      attemptCount++;

      // Falha primeiras 2 tentativas, sucede na 3ª
      if (attemptCount < 3) {
        route.fulfill({ status: 503, body: JSON.stringify({ error: 'Serviço Indisponível' }) });
      } else {
        route.fulfill({ status: 200, body: JSON.stringify({ orderId: '12345' }) });
      }
    });

    await page.goto('/checkout');
    await page.getByRole('button', { name: 'Fazer Pedido' }).click();

    // Deve suceder após 3 tentativas
    await expect(page.getByText('Pedido realizado com sucesso')).toBeVisible();
    expect(attemptCount).toBe(3);
  });

  test('app lida com desconexão de rede graciosamente', async ({ page, context }) => {
    await page.goto('/dashboard');

    // Simular modo offline
    await context.setOffline(true);

    // Disparar ação requerendo rede
    await page.getByRole('button', { name: 'Atualizar Dados' }).click();

    // Usuário vê indicador offline (não crash)
    await expect(page.getByText('Você está offline. Mudanças sincronizarão quando reconectado.')).toBeVisible();

    // Reconectar
    await context.setOffline(false);
    await page.getByRole('button', { name: 'Atualizar Dados' }).click();

    // Dados carregam com sucesso
    await expect(page.getByText('Dados atualizados')).toBeVisible();
  });

  test('endpoint de verificação de saúde retorna status do serviço', async ({ request }) => {
    const response = await request.get('/api/health');

    expect(response.status()).toBe(200);

    const health = await response.json();
    expect(health).toHaveProperty('status', 'saudavel');
    expect(health).toHaveProperty('timestamp');
    expect(health).toHaveProperty('services');

    // Verificar serviços críticos monitorados
    expect(health.services).toHaveProperty('database');
    expect(health.services).toHaveProperty('cache');
    expect(health.services).toHaveProperty('queue');

    // Todos serviços devem estar UP
    expect(health.services.database.status).toBe('UP');
    expect(health.services.cache.status).toBe('UP');
    expect(health.services.queue.status).toBe('UP');
  });

  test('circuit breaker abre após 5 falhas consecutivas', async ({ page, context }) => {
    let failureCount = 0;

    await context.route('**/api/recommendations', (route) => {
      failureCount++;
      route.fulfill({ status: 500, body: JSON.stringify({ error: 'Erro de Serviço' }) });
    });

    await page.goto('/product/123');

    // Aguardar circuit breaker abrir (UI de fallback aparece)
    await expect(page.getByText('Recomendações temporariamente indisponíveis')).toBeVisible({ timeout: 10000 });

    // Verificar que circuit breaker parou de fazer requisições após limite (deve ser ≤5)
    expect(failureCount).toBeLessThanOrEqual(5);
  });

  test('limite de taxa lida graciosamente com respostas 429', async ({ page, context }) => {
    let requestCount = 0;

    await context.route('**/api/search', (route) => {
      requestCount++;

      if (requestCount > 10) {
        // Limite de taxa excedido
        route.fulfill({
          status: 429,
          headers: { 'Retry-After': '5' },
          body: JSON.stringify({ error: 'Limite de taxa excedido' }),
        });
      } else {
        route.fulfill({ status: 200, body: JSON.stringify({ results: [] }) });
      }
    });

    await page.goto('/search');

    // Fazer 15 requisições de busca rapidamente
    for (let i = 0; i < 15; i++) {
      await page.getByPlaceholder('Buscar').fill(`query-${i}`);
      await page.getByRole('button', { name: 'Buscar' }).click();
    }

    // Usuário vê mensagem de limite de taxa (não crash)
    await expect(page.getByText('Muitas requisições. Por favor aguarde um momento.')).toBeVisible();
  });
});
```

**Pontos Chave**:

- Tratamento de erro: Degradação graciosa (erro 500 → mensagem amigável + botão tentar novamente)
- Retentativas: 3 tentativas em falhas transitórias (503 → eventual sucesso)
- Tratamento offline: Desconexão de rede detectada (sincronizar quando reconectado)
- Verificações de saúde: `/api/health` monitora banco de dados, cache, fila
- Circuit breaker: Abre após 5 falhas (UI de fallback, parar retentativas)
- Limite de taxa: Resposta 429 tratada (header Retry-After respeitado)

**Critérios NFR de Confiabilidade**:

- ✅ PASSOU: Tratamento de erro, retentativas, verificações de saúde verificados (todos os 6 testes verdes)
- ⚠️ PREOCUPAÇÕES: Cobertura parcial (ex: circuit breaker faltando) ou sem telemetria
- ❌ FALHOU: Sem caminho de recuperação (erro 500 quebra app) ou cenários de crash não resolvidos

---

### Exemplo 4: Validação de NFR de Manutenibilidade (Ferramentas CI, Não Playwright)

**Contexto**: Use ferramentas de CI adequadas para validação de qualidade de código (cobertura, duplicação, vulnerabilidades)

**Implementação**:

```yaml
# .github/workflows/nfr-maintainability.yml
name: NFR - Manutenibilidade

on: [push, pull_request]

jobs:
  test-coverage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4

      - name: Instalar dependências
        run: npm ci

      - name: Rodar testes com cobertura
        run: npm run test:coverage

      - name: Verificar limite de cobertura (80% mínimo)
        run: |
          COVERAGE=$(jq '.total.lines.pct' coverage/coverage-summary.json)
          echo "Cobertura: $COVERAGE%"
          if (( $(echo "$COVERAGE < 80" | bc -l) )); then
            echo "❌ FALHOU: Cobertura $COVERAGE% abaixo do limite de 80%"
            exit 1
          else
            echo "✅ PASSOU: Cobertura $COVERAGE% atende limite de 80%"
          fi

  code-duplication:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4

      - name: Verificar duplicação de código (<5% permitido)
        run: |
          npx jscpd src/ --threshold 5 --format json --output duplication.json
          DUPLICATION=$(jq '.statistics.total.percentage' duplication.json)
          echo "Duplicação: $DUPLICATION%"
          if (( $(echo "$DUPLICATION >= 5" | bc -l) )); then
            echo "❌ FALHOU: Duplicação $DUPLICATION% excede limite de 5%"
            exit 1
          else
            echo "✅ PASSOU: Duplicação $DUPLICATION% abaixo do limite de 5%"
          fi

  vulnerability-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4

      - name: Instalar dependências
        run: npm ci

      - name: Rodar npm audit (sem vulnerabilidades críticas/altas)
        run: |
          npm audit --json > audit.json || true
          CRITICAL=$(jq '.metadata.vulnerabilities.critical' audit.json)
          HIGH=$(jq '.metadata.vulnerabilities.high' audit.json)
          echo "Críticas: $CRITICAL, Altas: $HIGH"
          if [ "$CRITICAL" -gt 0 ] || [ "$HIGH" -gt 0 ]; then
            echo "❌ FALHOU: Encontradas $CRITICAL críticas e $HIGH altas vulnerabilidades"
            npm audit
            exit 1
          else
            echo "✅ PASSOU: Sem vulnerabilidades críticas/altas"
          fi
```

**Testes Playwright para Observabilidade (Validação E2E):**

```typescript
// tests/nfr/observability.spec.ts
import { test, expect } from '@playwright/test';

test.describe('NFR de Manutenibilidade: Validação de Observabilidade', () => {
  test('erros críticos são reportados para serviço de monitoramento', async ({ page, context }) => {
    const sentryEvents: any[] = [];

    // Mock SDK Sentry para verificar rastreamento de erro
    await context.addInitScript(() => {
      (window as any).Sentry = {
        captureException: (error: Error) => {
          console.log('SENTRY_CAPTURE:', JSON.stringify({ message: error.message, stack: error.stack }));
        },
      };
    });

    page.on('console', (msg) => {
      if (msg.text().includes('SENTRY_CAPTURE:')) {
        sentryEvents.push(JSON.parse(msg.text().replace('SENTRY_CAPTURE:', '')));
      }
    });

    // Disparar erro mockando falha de API
    await context.route('**/api/products', (route) => {
      route.fulfill({ status: 500, body: JSON.stringify({ error: 'Erro de Banco de Dados' }) });
    });

    await page.goto('/products');

    // Aguardar UI de erro e captura Sentry
    await expect(page.getByText('Incapaz de carregar produtos')).toBeVisible();

    // Verificar que erro foi capturado pelo monitoramento
    expect(sentryEvents.length).toBeGreaterThan(0);
    expect(sentryEvents[0]).toHaveProperty('message');
    expect(sentryEvents[0]).toHaveProperty('stack');
  });

  test('tempos de resposta de API são rastreados em telemetria', async ({ request }) => {
    const response = await request.get('/api/products?limit=10');

    expect(response.ok()).toBeTruthy();

    // Verificar header Server-Timing para APM (Application Performance Monitoring)
    const serverTiming = response.headers()['server-timing'];

    expect(serverTiming).toBeTruthy();
    expect(serverTiming).toContain('db'); // Tempo de query de banco de dados
    expect(serverTiming).toContain('total'); // Tempo total de processamento
  });

  test('logging estruturado presente na aplicação', async ({ request }) => {
    // Fazer chamada de API que gera logs
    const response = await request.post('/api/orders', {
      data: { productId: '123', quantity: 2 },
    });

    expect(response.ok()).toBeTruthy();

    // Nota: Em cenários reais, valide logs no sistema de monitoramento (Datadog, CloudWatch)
    // Este teste valida que o contrato de logging existe (Server-Timing, IDs de trace em headers)
    const traceId = response.headers()['x-trace-id'];
    expect(traceId).toBeTruthy(); // Confirma logging estruturado com IDs de correlação
  });
});
```

**Pontos Chave**:

- **Cobertura/duplicação**: Jobs CI (GitHub Actions), não testes Playwright
- **Scan de vulnerabilidade**: npm audit no CI, não testes Playwright
- **Observabilidade**: Playwright valida rastreamento de erro (Sentry) e headers de telemetria
- **Logging estruturado**: Valide contrato de logging (trace IDs, headers Server-Timing)
- **Separação de preocupações**: Verificações em tempo de build (cobertura, auditoria) vs verificações em tempo de execução (rastreamento de erro, telemetria)

**Critérios NFR de Manutenibilidade**:

- ✅ PASSOU: Código limpo (80%+ cobertura do CI, <5% duplicação do CI), observabilidade validada em E2E, sem vulnerabilidades críticas do npm audit
- ⚠️ PREOCUPAÇÕES: Duplicação >5%, cobertura 60-79%, ou propriedade pouco clara
- ❌ FALHOU: Testes ausentes (<60%), implementações emaranhadas (>10% duplicação), ou sem observabilidade

---

## Checklist de Avaliação de NFR

Antes do portão de lançamento:

- [ ] **Segurança** (Playwright E2E + Ferramentas de Segurança):
  - [ ] Testes de Auth/authz verdes (redirecionamento não autenticado, RBAC imposto)
  - [ ] Segredos nunca logados ou expostos em erros
  - [ ] OWASP Top 10 validado (injeção SQL bloqueada, XSS higienizado)
  - [ ] Auditoria de segurança completa (scan de vulnerabilidade, teste de penetração se aplicável)

- [ ] **Performance** (Teste de Carga k6):
  - [ ] Alvos SLO/SLA atendidos com evidência k6 (p95 <500ms, taxa de erro <1%)
  - [ ] Teste de carga completo (carga esperada)
  - [ ] Teste de estresse completo (ponto de quebra identificado)
  - [ ] Teste de pico completo (lida com picos de tráfego)
  - [ ] Teste de resistência completo (sem vazamentos de memória sob carga sustentada)

- [ ] **Confiabilidade** (Playwright E2E + Testes de API):
  - [ ] Tratamento de erro gracioso (500 → mensagem amigável + retentativa)
  - [ ] Retentativas implementadas (3 tentativas em falhas transitórias)
  - [ ] Verificações de saúde monitoradas (endpoint /api/health)
  - [ ] Circuit breaker testado (abre após limite de falha)
  - [ ] Tratamento offline validado (desconexão de rede graciosa)

- [ ] **Manutenibilidade** (Ferramentas CI):
  - [ ] Cobertura de teste ≥80% (do relatório de cobertura CI)
  - [ ] Duplicação de código <5% (do job CI jscpd)
  - [ ] Sem vulnerabilidades críticas/altas (do job CI npm audit)
  - [ ] Logging estruturado validado (Playwright valida headers de telemetria)
  - [ ] Rastreamento de erro configurado (Sentry/integração de monitoramento validada)

- [ ] **Requisitos ambíguos**: Padrão para PREOCUPAÇÕES (forçar time a clarificar limites e evidência)
- [ ] **Critérios NFR documentados**: Limites mensuráveis definidos (não "rápido o suficiente" subjetivo)
- [ ] **Validação automatizada**: Testes NFR rodam no pipeline CI (não checklists manuais)
- [ ] **Seleção de ferramenta**: Ferramenta certa para cada NFR (k6 para performance, Playwright para segurança/confiabilidade E2E, ferramentas CI para manutenibilidade)

## Matriz de Decisão de Portão NFR

| Categoria           | Critérios PASSA                              | Critérios PREOCUPAÇÕES                       | Critérios FALHA                                |
| ------------------- | -------------------------------------------- | -------------------------------------------- | ---------------------------------------------- |
| **Segurança**       | Auth/authz, manipulação de segredo, OWASP verificado | Pequenas lacunas com proprietários claros | Exposição crítica ou controles faltando        |
| **Performance**     | Métricas atendem SLO/SLA com evidência de profiling | Tendendo para limites ou baselines faltando | SLO/SLA violado ou vazamentos de recursos detectados |
| **Confiabilidade**  | Tratamento de erro, retentativas, verificações de saúde OK | Cobertura parcial ou telemetria faltando | Sem caminho de recuperação ou cenários de crash não resolvidos |
| **Manutenibilidade**| Código limpo, testes, docs enviados juntos   | Duplicação, baixa cobertura, propriedade pouco clara | Testes ausentes, código emaranhado, sem observabilidade |

**Padrão**: Se alvos ou evidência são indefinidos → **PREOCUPAÇÕES** (forçar time a clarificar antes da aprovação)

## Pontos de Integração

- **Usado em workflows**: `*nfr-assess` (validação automatizada de NFR), `*trace` (decisão de portão Fase 2), `*test-design` (avaliação de risco NFR via Árvore de Utilidade)
- **Fragmentos relacionados**: `risk-governance.md` (pontuação de risco NFR), `probability-impact.md` (avaliação de impacto NFR), `test-quality.md` (padrões de manutenibilidade), `test-levels-framework.md` (teste de nível de sistema para NFRs)
- **Ferramentas por Categoria NFR**:
  - **Segurança**: Playwright (E2E auth/authz), OWASP ZAP, Burp Suite, npm audit, Snyk
  - **Performance**: k6 (carga/estresse/pico/resistência), Lighthouse (Core Web Vitals), Artillery
  - **Confiabilidade**: Playwright (tratamento de erro E2E), Testes de API (retentativas, verificações de saúde), Ferramentas de Engenharia de Caos
  - **Manutenibilidade**: GitHub Actions (cobertura, duplicação, auditoria), jscpd, Playwright (validação de observabilidade)

_Fonte: Curso Arquiteto de Teste (abordagens de teste NFR, Árvore de Utilidade, Cenários de Qualidade), ISO/IEC 25010 Características de Qualidade de Software, OWASP Top 10, documentação k6_
