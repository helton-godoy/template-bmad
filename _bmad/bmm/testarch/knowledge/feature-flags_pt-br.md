# Governação da Bandeira de Caracteres

## Princípio

Bandeiras de recurso permitem lançamentos controlados e testes A/B, mas requerem governança de testes disciplinados. Centralizar definições de bandeira em um enum congelado, testar estados habilitados e desativados, limpar o alvo após cada especificação e manter uma lista de verificação abrangente do ciclo de vida da bandeira. Para sistemas de estilo LaunchDarkly, assistentes de API de script para as variações de sementes programáticamente ao invés de mutações manuais de UI.

## Racional

Bandeiras de recursos mal gerenciadas tornam-se dívida técnica: variações não testadas enviam código quebrado, bandeiras esquecidas bagunçam a base de códigos e ambientes compartilhados tornam-se instáveis a partir de regras de alvo sobras. A governança estruturada garante que as bandeiras sejam testáveis, rastreáveis, temporárias e seguras. Testando ambos os estados evita surpresas quando bandeiras flip na produção.

## Exemplos de padrões

### Exemplo 1: Padrão Enum da bandeira da característica com segurança do tipo

**Contexto**: Gestão centralizada de bandeiras com segurança do tipo TypeScript e validação em tempo de execução.

**Implementation**:

```typescript
// src/utils/feature-flags.ts
/**
 * Centralized feature flag definitions
 * - Object.freeze prevents runtime modifications
 * - TypeScript ensures compile-time type safety
 * - Single source of truth for all flag keys
 */
export const FLAGS = Object.freeze({
  // User-facing features
  NEW_CHECKOUT_FLOW: 'new-checkout-flow',
  DARK_MODE: 'dark-mode',
  ENHANCED_SEARCH: 'enhanced-search',

  // Experiments
  PRICING_EXPERIMENT_A: 'pricing-experiment-a',
  HOMEPAGE_VARIANT_B: 'homepage-variant-b',

  // Infrastructure
  USE_NEW_API_ENDPOINT: 'use-new-api-endpoint',
  ENABLE_ANALYTICS_V2: 'enable-analytics-v2',

  // Killswitches (emergency disables)
  DISABLE_PAYMENT_PROCESSING: 'disable-payment-processing',
  DISABLE_EMAIL_NOTIFICATIONS: 'disable-email-notifications',
} as const);

/**
 * Type-safe flag keys
 * Prevents typos and ensures autocomplete in IDEs
 */
export type FlagKey = (typeof FLAGS)[keyof typeof FLAGS];

/**
 * Flag metadata for governance
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
 * Flag registry with governance metadata
 * Used for flag lifecycle tracking and cleanup alerts
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
    requiresCleanup: false, // Permanent feature toggle
  },
  // ... rest of registry
};

/**
 * Validate flag exists in registry
 * Throws at runtime if flag is unregistered
 */
export function validateFlag(flag: string): asserts flag is FlagKey {
  if (!Object.values(FLAGS).includes(flag as FlagKey)) {
    throw new Error(`Unregistered feature flag: ${flag}`);
  }
}

/**
 * Check if flag is expired (needs removal)
 */
export function isFlagExpired(flag: FlagKey): boolean {
  const metadata = FLAG_REGISTRY[flag];
  if (!metadata.expiryDate) return false;

  const expiry = new Date(metadata.expiryDate);
  return Date.now() > expiry.getTime();
}

/**
 * Get all expired flags requiring cleanup
 */
export function getExpiredFlags(): FlagMetadata[] {
  return Object.values(FLAG_REGISTRY).filter((meta) => isFlagExpired(meta.key));
}

```

**Usagem em código de aplicação**:

```typescript
// components/Checkout.tsx
import { FLAGS } from '@/utils/feature-flags';
import { useFeatureFlag } from '@/hooks/useFeatureFlag';

export function Checkout() {
  const isNewFlow = useFeatureFlag(FLAGS.NEW_CHECKOUT_FLOW);

  return isNewFlow ? <NewCheckoutFlow /> : <LegacyCheckoutFlow />;
}

```

**Pontos-chave**

- **Segurança do tipo**: TipoScript capturas erros no momento da compilação
- **Validação em tempo real**: validateFlag garante apenas bandeiras registadas utilizadas
- **Metadata tracking**: Proprietário, datas, dependências documentadas
- **Alertas de expiração**: Detecção automática de bandeiras antigas
- **Fonte única da verdade**: Todas as bandeiras definidas num só lugar

---

### Exemplo 2: Padrão de teste da bandeira de recurso (ambos os estados)

**Contexto**: Teste abrangente de variações de bandeira de características com limpeza adequada.

**Implementation**:

«``typescript
// testes/e2e/checkout-feature-flag.spec.ts
import BMADPROTECT008End de '@ playwright/test';
BMADPROTECT005end BMADPROTECT007end de '@/utils/feature-flags';

/**
* Estratégia de Teste da Bandeira de Característica:
* 1. Teste ambos estados habilitados e desativados
* 2. Limpar o alvo após cada teste
* 3. Use usuários de teste dedicados (não dados de produção)
* 4. Verifique o fogo de eventos de telemetria corretamente
*/

test.describe('Fundo de Verificação