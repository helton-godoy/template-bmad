# Governança de Feature Flags

## Princípio

Feature flags permitem rollouts controlados e testes A/B, mas exigem governança de teste disciplinada. Centralize definições de flags em um enum congelado, teste ambos os estados ativado e desativado, limpe o targeting após cada spec e mantenha uma checklist de ciclo de vida de flag abrangente. Para sistemas estilo LaunchDarkly, crie scripts de helpers de API para semear variações programaticamente em vez de mutações de UI manuais.

## Motivação

Feature flags mal gerenciadas tornam-se dívida técnica: variações não testadas enviam código quebrado, flags esquecidas poluem a base de código e ambientes compartilhados tornam-se instáveis com regras de targeting deixadas para trás. Governança estruturada garante que flags sejam testáveis, rastreáveis, temporárias e seguras. Testar ambos os estados previne surpresas quando flags mudam em produção.

## Exemplos de Padrões

### Exemplo 1: Padrão de Enum de Feature Flag com Segurança de Tipo

**Contexto**: Gerenciamento centralizado de flags com segurança de tipo TypeScript e validação em tempo de execução.

**Implementação**:

```typescript
// src/utils/feature-flags.ts
/**
 * Definições centralizadas de feature flags
 * - Object.freeze previne modificações em tempo de execução
 * - TypeScript garante segurança de tipo em tempo de compilação
 * - Fonte única de verdade para todas as chaves de flag
 */
export const FLAGS = Object.freeze({
  // Funcionalidades voltadas ao usuário
  NEW_CHECKOUT_FLOW: 'new-checkout-flow',
  DARK_MODE: 'dark-mode',
  ENHANCED_SEARCH: 'enhanced-search',

  // Experimentos
  PRICING_EXPERIMENT_A: 'pricing-experiment-a',
  HOMEPAGE_VARIANT_B: 'homepage-variant-b',

  // Infraestrutura
  USE_NEW_API_ENDPOINT: 'use-new-api-endpoint',
  ENABLE_ANALYTICS_V2: 'enable-analytics-v2',

  // Killswitches (desativações de emergência)
  DISABLE_PAYMENT_PROCESSING: 'disable-payment-processing',
  DISABLE_EMAIL_NOTIFICATIONS: 'disable-email-notifications',
} as const);

/**
 * Chaves de flag type-safe
 * Previne erros de digitação e garante autocompletar em IDEs
 */
export type FlagKey = (typeof FLAGS)[keyof typeof FLAGS];

/**
 * Metadados de flag para governança
 */
type FlagMetadata = {
  key: FlagKey;
  name: string;
  owner: string;
  createdDate: string;
  expiryDate?: string;
  defaultState: boolean;
  requiresCleanup: boolean;
  dependencies?: FlagKey[];
  telemetryEvents?: string[];
};

/**
 * Registro de flag com metadados de governança
 * Usado para rastreamento de ciclo de vida de flag e alertas de limpeza
 */
export const FLAG_REGISTRY: Record<FlagKey, FlagMetadata> = {
  [FLAGS.NEW_CHECKOUT_FLOW]: {
    key: FLAGS.NEW_CHECKOUT_FLOW,
    name: 'New Checkout Flow',
    owner: 'payments-team',
    createdDate: '2025-01-15',
    expiryDate: '2025-03-15',
    defaultState: false,
    requiresCleanup: true,
    dependencies: [FLAGS.USE_NEW_API_ENDPOINT],
    telemetryEvents: ['checkout_started', 'checkout_completed'],
  },
  [FLAGS.DARK_MODE]: {
    key: FLAGS.DARK_MODE,
    name: 'Dark Mode UI',
    owner: 'frontend-team',
    createdDate: '2025-01-10',
    defaultState: false,
    requiresCleanup: false, // Toggle de funcionalidade permanente
  },
  // ... resto do registro
};

/**
 * Validar se flag existe no registro
 * Lança erro em tempo de execução se flag não estiver registrada
 */
export function validateFlag(flag: string): asserts flag is FlagKey {
  if (!Object.values(FLAGS).includes(flag as FlagKey)) {
    throw new Error(`Feature flag não registrada: ${flag}`);
  }
}

/**
 * Checar se flag está expirada (precisa de remoção)
 */
export function isFlagExpired(flag: FlagKey): boolean {
  const metadata = FLAG_REGISTRY[flag];
  if (!metadata.expiryDate) return false;

  const expiry = new Date(metadata.expiryDate);
  return Date.now() > expiry.getTime();
}

/**
 * Obter todas as flags expiradas requerendo limpeza
 */
export function getExpiredFlags(): FlagMetadata[] {
  return Object.values(FLAG_REGISTRY).filter((meta) => isFlagExpired(meta.key));
}
```

**Uso no código da aplicação**:

```typescript
// components/Checkout.tsx
import { FLAGS } from '@/utils/feature-flags';
import { useFeatureFlag } from '@/hooks/useFeatureFlag';

export function Checkout() {
  const isNewFlow = useFeatureFlag(FLAGS.NEW_CHECKOUT_FLOW);

  return isNewFlow ? <NewCheckoutFlow /> : <LegacyCheckoutFlow />;
}
```

**Pontos Chave**:

- **Segurança de tipo**: TypeScript captura erros de digitação em tempo de compilação
- **Validação em tempo de execução**: validateFlag garante que apenas flags registradas sejam usadas
- **Rastreamento de metadados**: Proprietário, datas, dependências documentados
- **Alertas de expiração**: Detecção automatizada de flags obsoletas
- **Fonte única de verdade**: Todas as flags definidas em um lugar

---

### Exemplo 2: Padrão de Teste de Feature Flag (Ambos os Estados)

**Contexto**: Teste abrangente de variações de feature flag com limpeza adequada.

**Implementação**:

```typescript
// tests/e2e/checkout-feature-flag.spec.ts
import { test, expect } from '@playwright/test';
import { FLAGS } from '@/utils/feature-flags';

/**
 * Estratégia de Teste de Feature Flag:
 * 1. Testar AMBOS os estados ativado e desativado
 * 2. Limpar targeting após cada teste
 * 3. Usar usuários de teste dedicados (não dados de produção)
 * 4. Verificar se eventos de telemetria disparam corretamente
 */

test.describe('Checkout Flow - Feature Flag Variations', () => {
  let testUserId: string;

  test.beforeEach(async () => {
    // Gerar ID de usuário de teste único
    testUserId = `test-user-${Date.now()}`;
  });

  test.afterEach(async ({ request }) => {
    // CRÍTICO: Limpar targeting de flag para prevenir poluição de ambiente compartilhado
    await request.post('/api/feature-flags/cleanup', {
      data: {
        flagKey: FLAGS.NEW_CHECKOUT_FLOW,
        userId: testUserId,
      },
    });
  });

  test('deve usar NOVO fluxo de checkout quando flag está ATIVADA', async ({ page, request }) => {
    // Arrange: Ativar flag para usuário de teste
    await request.post('/api/feature-flags/target', {
      data: {
        flagKey: FLAGS.NEW_CHECKOUT_FLOW,
        userId: testUserId,
        variation: true, // ATIVADO
      },
    });

    // Act: Navegar como usuário alvo
    await page.goto('/checkout', {
      extraHTTPHeaders: {
        'X-Test-User-ID': testUserId,
      },
    });

    // Assert: Elementos de UI do novo fluxo visíveis
    await expect(page.getByTestId('checkout-v2-container')).toBeVisible();
    await expect(page.getByTestId('express-payment-options')).toBeVisible();
    await expect(page.getByTestId('saved-addresses-dropdown')).toBeVisible();

    // Assert: Fluxo legado NÃO visível
    await expect(page.getByTestId('checkout-v1-container')).not.toBeVisible();

    // Assert: Evento de telemetria disparado
    const analyticsEvents = await page.evaluate(() => (window as any).__ANALYTICS_EVENTS__ || []);
    expect(analyticsEvents).toContainEqual(
      expect.objectContaining({
        event: 'checkout_started',
        properties: expect.objectContaining({
          variant: 'new_flow',
        }),
      }),
    );
  });

  test('deve usar fluxo de checkout LEGADO quando flag está DESATIVADA', async ({ page, request }) => {
    // Arrange: Desativar flag para usuário de teste (ou não alvejar de forma alguma)
    await request.post('/api/feature-flags/target', {
      data: {
        flagKey: FLAGS.NEW_CHECKOUT_FLOW,
        userId: testUserId,
        variation: false, // DESATIVADO
      },
    });

    // Act: Navegar como usuário alvo
    await page.goto('/checkout', {
      extraHTTPHeaders: {
        'X-Test-User-ID': testUserId,
      },
    });

    // Assert: Elementos de UI do fluxo legado visíveis
    await expect(page.getByTestId('checkout-v1-container')).toBeVisible();
    await expect(page.getByTestId('legacy-payment-form')).toBeVisible();

    // Assert: Novo fluxo NÃO visível
    await expect(page.getByTestId('checkout-v2-container')).not.toBeVisible();
    await expect(page.getByTestId('express-payment-options')).not.toBeVisible();

    // Assert: Evento de telemetria disparado com variante correta
    const analyticsEvents = await page.evaluate(() => (window as any).__ANALYTICS_EVENTS__ || []);
    expect(analyticsEvents).toContainEqual(
      expect.objectContaining({
        event: 'checkout_started',
        properties: expect.objectContaining({
          variant: 'legacy_flow',
        }),
      }),
    );
  });

  test('deve tratar erros de avaliação de flag graciosamente', async ({ page, request }) => {
    // Arrange: Simular serviço de flag indisponível
    await page.route('**/api/feature-flags/evaluate', (route) => route.fulfill({ status: 500, body: 'Service Unavailable' }));

    // Act: Navegar (deve fazer fallback para estado padrão)
    await page.goto('/checkout', {
      extraHTTPHeaders: {
        'X-Test-User-ID': testUserId,
      },
    });

    // Assert: Fallback para padrão seguro (fluxo legado)
    await expect(page.getByTestId('checkout-v1-container')).toBeVisible();

    // Assert: Erro logado mas sem erro visível ao usuário
    const consoleErrors = [];
    page.on('console', (msg) => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });
    expect(consoleErrors).toContain(expect.stringContaining('Feature flag evaluation failed'));
  });
});
```

**Equivalente Cypress**:

```javascript
// cypress/e2e/checkout-feature-flag.cy.ts
import { FLAGS } from '@/utils/feature-flags';

describe('Checkout Flow - Feature Flag Variations', () => {
  let testUserId;

  beforeEach(() => {
    testUserId = `test-user-${Date.now()}`;
  });

  afterEach(() => {
    // Limpar targeting
    cy.task('removeFeatureFlagTarget', {
      flagKey: FLAGS.NEW_CHECKOUT_FLOW,
      userId: testUserId,
    });
  });

  it('deve usar NOVO fluxo de checkout quando flag está ATIVADA', () => {
    // Arrange: Ativar flag via tarefa Cypress
    cy.task('setFeatureFlagVariation', {
      flagKey: FLAGS.NEW_CHECKOUT_FLOW,
      userId: testUserId,
      variation: true,
    });

    // Act
    cy.visit('/checkout', {
      headers: { 'X-Test-User-ID': testUserId },
    });

    // Assert
    cy.get('[data-testid="checkout-v2-container"]').should('be.visible');
    cy.get('[data-testid="checkout-v1-container"]').should('not.exist');
  });

  it('deve usar fluxo de checkout LEGADO quando flag está DESATIVADA', () => {
    // Arrange: Desativar flag
    cy.task('setFeatureFlagVariation', {
      flagKey: FLAGS.NEW_CHECKOUT_FLOW,
      userId: testUserId,
      variation: false,
    });

    // Act
    cy.visit('/checkout', {
      headers: { 'X-Test-User-ID': testUserId },
    });

    // Assert
    cy.get('[data-testid="checkout-v1-container"]').should('be.visible');
    cy.get('[data-testid="checkout-v2-container"]').should('not.exist');
  });
});
```

**Pontos Chave**:

- **Testar ambos os estados**: Variações ativadas E desativadas
- **Limpeza automática**: afterEach remove targeting (previne poluição)
- **Usuários de teste únicos**: Evita conflitos com dados de usuários reais
- **Validação de telemetria**: Verificar se eventos de analytics disparam corretamente
- **Degradação graciosa**: Testar comportamento de fallback em erros

---

### Exemplo 3: Padrão de Helper de Targeting de Feature Flag

**Contexto**: Helpers reutilizáveis para controle programático de flag via API LaunchDarkly/Split.io.

**Implementação**:

```typescript
// tests/support/feature-flag-helpers.ts
import { request as playwrightRequest } from '@playwright/test';
import { FLAGS, FlagKey } from '@/utils/feature-flags';

/**
 * Configuração do cliente API LaunchDarkly
 * Use chave SDK de projeto de teste (NÃO produção)
 */
const LD_SDK_KEY = process.env.LD_SDK_KEY_TEST;
const LD_API_BASE = 'https://app.launchdarkly.com/api/v2';

type FlagVariation = boolean | string | number | object;

/**
 * Definir variação de flag para usuário específico
 * Usa API LaunchDarkly para criar alvo de usuário
 */
export async function setFlagForUser(flagKey: FlagKey, userId: string, variation: FlagVariation): Promise<void> {
  const response = await playwrightRequest.newContext().then((ctx) =>
    ctx.post(`${LD_API_BASE}/flags/${flagKey}/targeting`, {
      headers: {
        Authorization: LD_SDK_KEY!,
        'Content-Type': 'application/json',
      },
      data: {
        targets: [
          {
            values: [userId],
            variation: variation ? 1 : 0, // 0 = off, 1 = on
          },
        ],
      },
    }),
  );

  if (!response.ok()) {
    throw new Error(`Falha ao definir flag ${flagKey} para usuário ${userId}: ${response.status()}`);
  }
}

/**
 * Remover usuário do targeting de flag
 * CRÍTICO para limpeza de teste
 */
export async function removeFlagTarget(flagKey: FlagKey, userId: string): Promise<void> {
  const response = await playwrightRequest.newContext().then((ctx) =>
    ctx.delete(`${LD_API_BASE}/flags/${flagKey}/targeting/users/${userId}`, {
      headers: {
        Authorization: LD_SDK_KEY!,
      },
    }),
  );

  if (!response.ok() && response.status() !== 404) {
    // 404 é aceitável (usuário não estava alvejado)
    throw new Error(`Falha ao remover alvo da flag ${flagKey} para usuário ${userId}: ${response.status()}`);
  }
}

/**
 * Helper de rollout percentual
 * Ativar flag para N% dos usuários
 */
export async function setFlagRolloutPercentage(flagKey: FlagKey, percentage: number): Promise<void> {
  if (percentage < 0 || percentage > 100) {
    throw new Error('Porcentagem deve estar entre 0 e 100');
  }

  const response = await playwrightRequest.newContext().then((ctx) =>
    ctx.patch(`${LD_API_BASE}/flags/${flagKey}`, {
      headers: {
        Authorization: LD_SDK_KEY!,
        'Content-Type': 'application/json',
      },
      data: {
        rollout: {
          variations: [
            { variation: 0, weight: 100 - percentage }, // off
            { variation: 1, weight: percentage }, // on
          ],
        },
      },
    }),
  );

  if (!response.ok()) {
    throw new Error(`Falha ao definir rollout para flag ${flagKey}: ${response.status()}`);
  }
}

/**
 * Ativar flag globalmente (100% rollout)
 */
export async function enableFlagGlobally(flagKey: FlagKey): Promise<void> {
  await setFlagRolloutPercentage(flagKey, 100);
}

/**
 * Desativar flag globalmente (0% rollout)
 */
export async function disableFlagGlobally(flagKey: FlagKey): Promise<void> {
  await setFlagRolloutPercentage(flagKey, 0);
}

/**
 * Stub de feature flags em ambientes locais/teste
 * Ignora LaunchDarkly inteiramente
 */
export function stubFeatureFlags(flags: Record<FlagKey, FlagVariation>): void {
  // Definir flags no localStorage ou injetar na window
  if (typeof window !== 'undefined') {
    (window as any).__STUBBED_FLAGS__ = flags;
  }
}
```

**Uso na fixture Playwright**:

```typescript
// playwright/fixtures/feature-flag-fixture.ts
import { test as base } from '@playwright/test';
import { setFlagForUser, removeFlagTarget } from '../support/feature-flag-helpers';
import { FlagKey } from '@/utils/feature-flags';

type FeatureFlagFixture = {
  featureFlags: {
    enable: (flag: FlagKey, userId: string) => Promise<void>;
    disable: (flag: FlagKey, userId: string) => Promise<void>;
    cleanup: (flag: FlagKey, userId: string) => Promise<void>;
  };
};

export const test = base.extend<FeatureFlagFixture>({
  featureFlags: async ({}, use) => {
    const cleanupQueue: Array<{ flag: FlagKey; userId: string }> = [];

    await use({
      enable: async (flag, userId) => {
        await setFlagForUser(flag, userId, true);
        cleanupQueue.push({ flag, userId });
      },
      disable: async (flag, userId) => {
        await setFlagForUser(flag, userId, false);
        cleanupQueue.push({ flag, userId });
      },
      cleanup: async (flag, userId) => {
        await removeFlagTarget(flag, userId);
      },
    });

    // Auto-limpeza após teste
    for (const { flag, userId } of cleanupQueue) {
      await removeFlagTarget(flag, userId);
    }
  },
});
```

**Pontos Chave**:

- **Controle orientado a API**: Sem cliques manuais de UI necessários
- **Auto-limpeza**: Fixture rastreia e remove targeting
- **Rollouts percentuais**: Teste lançamentos graduais de funcionalidade
- **Opção de stubbing**: Desenvolvimento local sem LaunchDarkly
- **Type-safe**: FlagKey previne erros de digitação

---

### Exemplo 4: Checklist de Ciclo de Vida de Feature Flag & Estratégia de Limpeza

**Contexto**: Checklist de governança e detecção automatizada de limpeza para flags obsoletas.

**Implementação**:

```typescript
// scripts/feature-flag-audit.ts
/**
 * Script de Auditoria de Ciclo de Vida de Feature Flag
 * Rodar semanalmente para detectar flags obsoletas requerendo limpeza
 */

import { FLAG_REGISTRY, FLAGS, getExpiredFlags, FlagKey } from '../src/utils/feature-flags';
import * as fs from 'fs';
import * as path from 'path';

type AuditResult = {
  totalFlags: number;
  expiredFlags: FlagKey[];
  missingOwners: FlagKey[];
  missingDates: FlagKey[];
  permanentFlags: FlagKey[];
  flagsNearingExpiry: FlagKey[];
};

/**
 * Auditar todas as feature flags para conformidade de governança
 */
function auditFeatureFlags(): AuditResult {
  const allFlags = Object.keys(FLAG_REGISTRY) as FlagKey[];
  const expiredFlags = getExpiredFlags().map((meta) => meta.key);

  // Flags expirando nos próximos 30 dias
  const thirtyDaysFromNow = Date.now() + 30 * 24 * 60 * 60 * 1000;
  const flagsNearingExpiry = allFlags.filter((flag) => {
    const meta = FLAG_REGISTRY[flag];
    if (!meta.expiryDate) return false;
    const expiry = new Date(meta.expiryDate).getTime();
    return expiry > Date.now() && expiry < thirtyDaysFromNow;
  });

  // Metadados faltando
  const missingOwners = allFlags.filter((flag) => !FLAG_REGISTRY[flag].owner);
  const missingDates = allFlags.filter((flag) => !FLAG_REGISTRY[flag].createdDate);

  // Flags permanentes (sem expiração, requiresCleanup = false)
  const permanentFlags = allFlags.filter((flag) => {
    const meta = FLAG_REGISTRY[flag];
    return !meta.expiryDate && !meta.requiresCleanup;
  });

  return {
    totalFlags: allFlags.length,
    expiredFlags,
    missingOwners,
    missingDates,
    permanentFlags,
    flagsNearingExpiry,
  };
}

/**
 * Gerar relatório markdown
 */
function generateReport(audit: AuditResult): string {
  let report = `# Relatório de Auditoria de Feature Flag\n\n`;
  report += `**Data**: ${new Date().toISOString()}\n`;
  report += `**Total de Flags**: ${audit.totalFlags}\n\n`;

  if (audit.expiredFlags.length > 0) {
    report += `## ⚠️ FLAGS EXPIRADAS - LIMPEZA IMEDIATA NECESSÁRIA\n\n`;
    audit.expiredFlags.forEach((flag) => {
      const meta = FLAG_REGISTRY[flag];
      report += `- **${meta.name}** (\`${flag}\`)\n`;
      report += `  - Proprietário: ${meta.owner}\n`;
      report += `  - Expirada: ${meta.expiryDate}\n`;
      report += `  - Ação: Remover código de flag, atualizar testes, deploy\n\n`;
    });
  }

  if (audit.flagsNearingExpiry.length > 0) {
    report += `## ⏰ FLAGS EXPIRANDO EM BREVE (Próximos 30 Dias)\n\n`;
    audit.flagsNearingExpiry.forEach((flag) => {
      const meta = FLAG_REGISTRY[flag];
      report += `- **${meta.name}** (\`${flag}\`)\n`;
      report += `  - Proprietário: ${meta.owner}\n`;
      report += `  - Expira: ${meta.expiryDate}\n`;
      report += `  - Ação: Planejar limpeza ou estender expiração\n\n`;
    });
  }

  if (audit.permanentFlags.length > 0) {
    report += `## 🔄 FLAGS PERMANENTES (Sem Expiração)\n\n`;
    audit.permanentFlags.forEach((flag) => {
      const meta = FLAG_REGISTRY[flag];
      report += `- **${meta.name}** (\`${flag}\`) - Proprietário: ${meta.owner}\n`;
    });
    report += `\n`;
  }

  if (audit.missingOwners.length > 0 || audit.missingDates.length > 0) {
    report += `## ❌ PROBLEMAS DE GOVERNANÇA\n\n`;
    if (audit.missingOwners.length > 0) {
      report += `**Proprietários Faltando**: ${audit.missingOwners.join(', ')}\n`;
    }
    if (audit.missingDates.length > 0) {
      report += `**Datas de Criação Faltando**: ${audit.missingDates.join(', ')}\n`;
    }
    report += `\n`;
  }

  return report;
}

/**
 * Checklist de Ciclo de Vida de Feature Flag
 */
const FLAG_LIFECYCLE_CHECKLIST = `
# Checklist de Ciclo de Vida de Feature Flag

## Antes de Criar uma Nova Flag

- [ ] **Nome**: Seguir convenção de nomenclatura (kebab-case, descritivo)
- [ ] **Proprietário**: Atribuir time/indivíduo responsável
- [ ] **Estado Padrão**: Determinar padrão seguro (geralmente false)
- [ ] **Data de Expiração**: Definir data de remoção (30-90 dias típico)
- [ ] **Dependências**: Documentar flags relacionadas
- [ ] **Telemetria**: Planejar eventos de analytics para rastrear
- [ ] **Plano de Rollback**: Definir como desativar rapidamente

## Durante o Desenvolvimento

- [ ] **Caminhos de Código**: Ambos estados ativado/desativado implementados
- [ ] **Testes**: Ambas variações testadas em CI
- [ ] **Documentação**: Propósito da flag documentado no código/PR
- [ ] **Telemetria**: Eventos de analytics instrumentados
- [ ] **Tratamento de Erro**: Degradação graciosa em falha de serviço de flag

## Antes do Lançamento

- [ ] **QA**: Ambos estados testados em staging
- [ ] **Plano de Rollout**: Porcentagem de rollout gradual definida
- [ ] **Monitoramento**: Dashboards/alertas para métricas relacionadas a flag
- [ ] **Comunicação com Stakeholders**: Produto/design alinhados

## Após o Lançamento (Monitoramento)

- [ ] **Métricas**: Critérios de sucesso rastreados
- [ ] **Taxas de Erro**: Sem aumento em erros
- [ ] **Performance**: Sem degradação
- [ ] **Feedback de Usuário**: Dados qualitativos coletados

## Limpeza (Pós-Lançamento)

- [ ] **Remover Código de Flag**: Deletar ramos if/else
- [ ] **Atualizar Testes**: Remover testes específicos de flag
- [ ] **Remover Targeting**: Limpar todos os alvos de usuário
- [ ] **Deletar Config de Flag**: Remover do LaunchDarkly/registro
- [ ] **Atualizar Documentação**: Remover referências
- [ ] **Deploy**: Enviar mudanças de limpeza
`;

// Rodar auditoria
const audit = auditFeatureFlags();
const report = generateReport(audit);

// Salvar relatório
const outputPath = path.join(__dirname, '../feature-flag-audit-report.md');
fs.writeFileSync(outputPath, report);
fs.writeFileSync(path.join(__dirname, '../FEATURE-FLAG-CHECKLIST.md'), FLAG_LIFECYCLE_CHECKLIST);

console.log(`✅ Auditoria completa. Relatório salvo em: ${outputPath}`);
console.log(`Total de flags: ${audit.totalFlags}`);
console.log(`Flags expiradas: ${audit.expiredFlags.length}`);
console.log(`Flags expirando em breve: ${audit.flagsNearingExpiry.length}`);

// Sair com erro se existirem flags expiradas
if (audit.expiredFlags.length > 0) {
  console.error(`\n❌ FLAGS EXPIRADAS DETECTADAS - LIMPEZA NECESSÁRIA`);
  process.exit(1);
}
```

**scripts package.json**:

```json
{
  "scripts": {
    "feature-flags:audit": "ts-node scripts/feature-flag-audit.ts",
    "feature-flags:audit:ci": "npm run feature-flags:audit || true"
  }
}
```

**Pontos Chave**:

- **Detecção automatizada**: Auditoria semanal captura flags obsoletas
- **Checklist de ciclo de vida**: Guia de governança abrangente
- **Rastreamento de expiração**: Flags auto-expiram após data definida
- **Integração CI**: Auditoria roda no pipeline, avisa sobre expiração
- **Clareza de propriedade**: Toda flag tem proprietário atribuído

---

## Checklist de Teste de Feature Flag

Antes de fazer merge de código relacionado a flag, verifique:

- [ ] **Ambos estados testados**: Variações ativadas E desativadas cobertas
- [ ] **Limpeza automatizada**: afterEach remove targeting (sem limpeza manual)
- [ ] **Dados de teste únicos**: Usuários de teste não colidem com produção
- [ ] **Telemetria validada**: Eventos de analytics disparam para ambas variações
- [ ] **Tratamento de erro**: Fallback gracioso quando serviço de flag indisponível
- [ ] **Metadados de flag**: Proprietário, datas, dependências documentados no registro
- [ ] **Plano de rollback**: Passos claros para desativar flag em produção
- [ ] **Data de expiração definida**: Data de remoção definida (ou marcada como permanente)

## Pontos de Integração

- Usado em workflows: `*automate` (geração de teste), `*framework` (setup de flag)
- Fragmentos relacionados: `test-quality.md`, `selective-testing.md`
- Serviços de flag: LaunchDarkly, Split.io, Unleash, implementações customizadas

_Fonte: Blog de estratégia LaunchDarkly, notas de arquitetura de teste Murat, governança de feature flag SEON_
