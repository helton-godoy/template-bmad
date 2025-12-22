# Teste de autenticação baseado em e- mail

## Princípio

A autenticação baseada em e-mail (links mágicos, códigos únicos, login sem senha) requer testes especializados com serviços de captura de e-mail como Mailosauro ou Ethereal. Extrair links mágicos através de processamento HTML ou usar extração de links embutidos, preservar o armazenamento do navegador (local/sessão/cookies) ao processar links, cache e-mail cargas úteis para evitar esgotar quotas de caixa de entrada, e cobrir casos negativos (links expirados, links reutilizados, várias solicitações rápidas). Registre IDs de e-mail e links para solução de problemas, mas limpe PII antes de cometer artefatos.

## Racional

A autenticação por e-mail introduz desafios únicos: entrega de e-mail assíncrona, limites de cotas (AWS Cognito: 50/dia), custo por e-mail e gestão de estado complexa (preservação de sessão através de cliques de link). Sem padrões adequados, os testes tornam-se lentos (esperar por e-mail cada vez), caros (exaustão de quotas) e frágeis (problemas de chegada, estado perdido). Usando serviços de captura de e-mail + cache de sessão + padrões de preservação de estado faz testes de e-mail rápido, confiável e econômico.

## Exemplos de padrões

### Exemplo 1: Extração de ligação mágica com Mailosauro

**Context**: Fluxo de login sem senha onde o usuário recebe link mágico via e-mail, clica nele e é autenticado.

**Implementation**:

```typescript
// tests/e2e/magic-link-auth.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Magic Link Authentication Flow
 * 1. User enters email
 * 2. Backend sends magic link
 * 3. Test retrieves email via Mailosaur
 * 4. Extract and visit magic link
 * 5. Verify user is authenticated
 */

// Mailosaur configuration
const MAILOSAUR_API_KEY = process.env.MAILOSAUR_API_KEY!;
const MAILOSAUR_SERVER_ID = process.env.MAILOSAUR_SERVER_ID!;

/**
 * Extract href from HTML email body
 * DOMParser provides XML/HTML parsing in Node.js
 */
function extractMagicLink(htmlString: string): string | null {
  const { JSDOM } = require('jsdom');
  const dom = new JSDOM(htmlString);
  const link = dom.window.document.querySelector('#magic-link-button');
  return link ? (link as HTMLAnchorElement).href : null;
}

/**
 * Alternative: Use Mailosaur's built-in link extraction
 * Mailosaur automatically parses links - no regex needed!
 */
async function getMagicLinkFromEmail(email: string): Promise<string> {
  const MailosaurClient = require('mailosaur');
  const mailosaur = new MailosaurClient(MAILOSAUR_API_KEY);

  // Wait for email (timeout: 30 seconds)
  const message = await mailosaur.messages.get(
    MAILOSAUR_SERVER_ID,
    {
      sentTo: email,
    },
    {
      timeout: 30000, // 30 seconds
    },
  );

  // Mailosaur extracts links automatically - no parsing needed!
  const magicLink = message.html?.links?.[0]?.href;

  if (!magicLink) {
    throw new Error(`Magic link not found in email to ${email}`);
  }

  console.log(`📧 Email received. Magic link extracted: ${magicLink}`);
  return magicLink;
}

test.describe('Magic Link Authentication', () => {
  test('should authenticate user via magic link', async ({ page, context }) => {
    // Arrange: Generate unique test email
    const randomId = Math.floor(Math.random() * 1000000);
    const testEmail = `user-${randomId}@${MAILOSAUR_SERVER_ID}.mailosaur.net`;

    // Act: Request magic link
    await page.goto('/login');
    await page.getByTestId('email-input').fill(testEmail);
    await page.getByTestId('send-magic-link').click();

    // Assert: Success message
    await expect(page.getByTestId('check-email-message')).toBeVisible();
    await expect(page.getByTestId('check-email-message')).toContainText('Check your email');

    // Retrieve magic link from email
    const magicLink = await getMagicLinkFromEmail(testEmail);

    // Visit magic link
    await page.goto(magicLink);

    // Assert: User is authenticated
    await expect(page.getByTestId('user-menu')).toBeVisible();
    await expect(page.getByTestId('user-email')).toContainText(testEmail);

    // Verify session storage preserved
    const localStorage = await page.evaluate(() => JSON.stringify(window.localStorage));
    expect(localStorage).toContain('authToken');
  });

  test('should handle expired magic link', async ({ page }) => {
    // Use pre-expired link (older than 15 minutes)
    const expiredLink = 'http://localhost:3000/auth/verify?token=expired-token-123';

    await page.goto(expiredLink);

    // Assert: Error message displayed
    await expect(page.getByTestId('error-message')).toBeVisible();
    await expect(page.getByTestId('error-message')).toContainText('link has expired');

    // Assert: User NOT authenticated
    await expect(page.getByTestId('user-menu')).not.toBeVisible();
  });

  test('should prevent reusing magic link', async ({ page }) => {
    const randomId = Math.floor(Math.random() * 1000000);
    const testEmail = `user-${randomId}@${MAILOSAUR_SERVER_ID}.mailosaur.net`;

    // Request magic link
    await page.goto('/login');
    await page.getByTestId('email-input').fill(testEmail);
    await page.getByTestId('send-magic-link').click();

    const magicLink = await getMagicLinkFromEmail(testEmail);

    // Visit link first time (success)
    await page.goto(magicLink);
    await expect(page.getByTestId('user-menu')).toBeVisible();

    // Sign out
    await page.getByTestId('sign-out').click();

    // Try to reuse same link (should fail)
    await page.goto(magicLink);
    await expect(page.getByTestId('error-message')).toBeVisible();
    await expect(page.getByTestId('error-message')).toContainText('link has already been used');
  });
});

```

**Cypress equivalente com o plugin Mailosauro**:

```javascript
// cypress/e2e/magic-link-auth.cy.ts
describe('Magic Link Authentication', () => {
  it('should authenticate user via magic link', () => {
    const serverId = Cypress.env('MAILOSAUR_SERVERID');
    const randomId = Cypress._.random(1e6);
    const testEmail = `user-${randomId}@${serverId}.mailosaur.net`;

    // Request magic link
    cy.visit('/login');
    cy.get('[data-cy="email-input"]').type(testEmail);
    cy.get('[data-cy="send-magic-link"]').click();
    cy.get('[data-cy="check-email-message"]').should('be.visible');

    // Retrieve and visit magic link
    cy.mailosaurGetMessage(serverId, { sentTo: testEmail })
      .its('html.links.0.href') // Mailosaur extracts links automatically!
      .should('exist')
      .then((magicLink) => {
        cy.log(`Magic link: ${magicLink}`);
        cy.visit(magicLink);
      });

    // Verify authenticated
    cy.get('[data-cy="user-menu"]').should('be.visible');
    cy.get('[data-cy="user-email"]').should('contain', testEmail);
  });
});

```

**Key Pontos**:

- * *Mailosaur auto- extração**: `html.links[0].href` ou `html.codes[0].value`
- **Unique emails**: ID aleatório evita colisões
- **Negative testing**: Links expirados e reutilizados testados
- **State verificação**: localStorage/sessão verificada
- **Fast recuperação de e-mail**: 30 segundo tempo- limite típico

---

### Example 2: State Preservation Pattern with cy.session / Playwright storageState

**Context**: Cache authenticated session to avoid requesting magic link on every test.

**Implementation**:

```typescript
// playwright/fixtures/email-auth-fixture.ts
import { test as base } from '@playwright/test';
import { getMagicLinkFromEmail } from '../support/mailosaur-helpers';

type EmailAuthFixture = {
  authenticatedUser: { email: string; token: string };
};

export const test = base.extend<EmailAuthFixture>({
  authenticatedUser: async ({ page, context }, use) => {
    const randomId = Math.floor(Math.random() * 1000000);
    const testEmail = `user-${randomId}@${process.env.MAILOSAUR_SERVER_ID}.mailosaur.net`;

    // Check if we have cached auth state for this email
    const storageStatePath = `./test-results/auth-state-${testEmail}.json`;

    try {
      // Try to reuse existing session
      await context.storageState({ path: storageStatePath });
      await page.goto('/dashboard');

      // Validate session is still valid
      const isAuthenticated = await page.getByTestId('user-menu').isVisible({ timeout: 2000 });

      if (isAuthenticated) {
        console.log(`✅ Reusing cached session for ${testEmail}`);
        await use({ email: testEmail, token: 'cached' });
        return;
      }
    } catch (error) {
      console.log(`📧 No cached session, requesting magic link for ${testEmail}`);
    }

    // Request new magic link
    await page.goto('/login');
    await page.getByTestId('email-input').fill(testEmail);
    await page.getByTestId('send-magic-link').click();

    // Get magic link from email
    const magicLink = await getMagicLinkFromEmail(testEmail);

    // Visit link and authenticate
    await page.goto(magicLink);
    await expect(page.getByTestId('user-menu')).toBeVisible();

    // Extract auth token from localStorage
    const authToken = await page.evaluate(() => localStorage.getItem('authToken'));

    // Save session state for reuse
    await context.storageState({ path: storageStatePath });

    console.log(`💾 Cached session for ${testEmail}`);

    await use({ email: testEmail, token: authToken || '' });
  },
});

```

**Cypress equivalent with cy.session + data-session**:

```javascript
// cypress/support/commands/email-auth.js
import { dataSession } from 'cypress-data-session';

/**
 * Authenticate via magic link with session caching
 * - First run: Requests email, extracts link, authenticates
 * - Subsequent runs: Reuses cached session (no email)
 */
Cypress.Commands.add('authViaMagicLink', (email) => {
  return dataSession({
    name: `magic-link-${email}`,

    // First-time setup: Request and process magic link
    setup: () => {
      cy.visit('/login');
      cy.get('[data-cy="email-input"]').type(email);
      cy.get('[data-cy="send-magic-link"]').click();

      // Get magic link from Mailosaur
      cy.mailosaurGetMessage(Cypress.env('MAILOSAUR_SERVERID'), {
        sentTo: email,
      })
        .its('html.links.0.href')
        .should('exist')
        .then((magicLink) => {
          cy.visit(magicLink);
        });

      // Wait for authentication
      cy.get('[data-cy="user-menu"]', { timeout: 10000 }).should('be.visible');

      // Preserve authentication state
      return cy.getAllLocalStorage().then((storage) => {
        return { storage, email };
      });
    },

    // Validate cached session is still valid
    validate: (cached) => {
      return cy.wrap(Boolean(cached?.storage));
    },

    // Recreate session from cache (no email needed)
    recreate: (cached) => {
      // Restore localStorage
      cy.setLocalStorage(cached.storage);
      cy.visit('/dashboard');
      cy.get('[data-cy="user-menu"]', { timeout: 5000 }).should('be.visible');
    },

    shareAcrossSpecs: true, // Share session across all tests
  });
});

```

**Usage in tests**:

```javascript
// cypress/e2e/dashboard.cy.ts
describe('Dashboard', () => {
  const serverId = Cypress.env('MAILOSAUR_SERVERID');
  const testEmail = `test-user@${serverId}.mailosaur.net`;

  beforeEach(() => {
    // First test: Requests magic link
    // Subsequent tests: Reuses cached session (no email!)
    cy.authViaMagicLink(testEmail);
  });

  it('should display user dashboard', () => {
    cy.get('[data-cy="dashboard-content"]').should('be.visible');
  });

  it('should show user profile', () => {
    cy.get('[data-cy="user-email"]').should('contain', testEmail);
  });

  // Both tests share same session - only 1 email consumed!
});

```

**Key Points**:

- **Session caching**: First test requests email, rest reuse session
- **State preservation**: localStorage/cookies saved and restored
- **Validation**: Check cached session is still valid
- **Quota optimization**: Massive reduction in email consumption
- **Fast tests**: Cached auth takes seconds vs. minutes

---

### Exemplo 3: Testes de Fluxo Negativo (Expirados, Inválidos, Reutilizados)

**Context**: Teste negativo abrangente para casos de borda de autenticação de email.

**Implementation**:

```typescript
// tests/e2e/email-auth-negative.spec.ts
import { test, expect } from '@playwright/test';
import { getMagicLinkFromEmail } from '../support/mailosaur-helpers';

const MAILOSAUR_SERVER_ID = process.env.MAILOSAUR_SERVER_ID!;

test.describe('Email Auth Negative Flows', () => {
  test('should reject expired magic link', async ({ page }) => {
    // Generate expired link (simulate 24 hours ago)
    const expiredToken = Buffer.from(
      JSON.stringify({
        email: 'test@example.com',
        exp: Date.now() - 24 * 60 * 60 * 1000, // 24 hours ago
      }),
    ).toString('base64');

    const expiredLink = `http://localhost:3000/auth/verify?token=${expiredToken}`;

    // Visit expired link
    await page.goto(expiredLink);

    // Assert: Error displayed
    await expect(page.getByTestId('error-message')).toBeVisible();
    await expect(page.getByTestId('error-message')).toContainText(/link.*expired|expired.*link/i);

    // Assert: Link to request new one
    await expect(page.getByTestId('request-new-link')).toBeVisible();

    // Assert: User NOT authenticated
    await expect(page.getByTestId('user-menu')).not.toBeVisible();
  });

  test('should reject invalid magic link token', async ({ page }) => {
    const invalidLink = 'http://localhost:3000/auth/verify?token=invalid-garbage';

    await page.goto(invalidLink);

    // Assert: Error displayed
    await expect(page.getByTestId('error-message')).toBeVisible();
    await expect(page.getByTestId('error-message')).toContainText(/invalid.*link|link.*invalid/i);

    // Assert: User not authenticated
    await expect(page.getByTestId('user-menu')).not.toBeVisible();
  });

  test('should reject already-used magic link', async ({ page, context }) => {
    const randomId = Math.floor(Math.random() * 1000000);
    const testEmail = `user-${randomId}@${MAILOSAUR_SERVER_ID}.mailosaur.net`;

    // Request magic link
    await page.goto('/login');
    await page.getByTestId('email-input').fill(testEmail);
    await page.getByTestId('send-magic-link').click();

    const magicLink = await getMagicLinkFromEmail(testEmail);

    // Visit link FIRST time (success)
    await page.goto(magicLink);
    await expect(page.getByTestId('user-menu')).toBeVisible();

    // Sign out
    await page.getByTestId('user-menu').click();
    await page.getByTestId('sign-out').click();
    await expect(page.getByTestId('user-menu')).not.toBeVisible();

    // Try to reuse SAME link (should fail)
    await page.goto(magicLink);

    // Assert: Link already used error
    await expect(page.getByTestId('error-message')).toBeVisible();
    await expect(page.getByTestId('error-message')).toContainText(/already.*used|link.*used/i);

    // Assert: User not authenticated
    await expect(page.getByTestId('user-menu')).not.toBeVisible();
  });

  test('should handle rapid successive link requests', async ({ page }) => {
    const randomId = Math.floor(Math.random() * 1000000);
    const testEmail = `user-${randomId}@${MAILOSAUR_SERVER_ID}.mailosaur.net`;

    // Request magic link 3 times rapidly
    for (let i = 0; i < 3; i++) {
      await page.goto('/login');
      await page.getByTestId('email-input').fill(testEmail);
      await page.getByTestId('send-magic-link').click();
      await expect(page.getByTestId('check-email-message')).toBeVisible();
    }

    // Only the LATEST link should work
    const MailosaurClient = require('mailosaur');
    const mailosaur = new MailosaurClient(process.env.MAILOSAUR_API_KEY);

    const messages = await mailosaur.messages.list(MAILOSAUR_SERVER_ID, {
      sentTo: testEmail,
    });

    // Should receive 3 emails
    expect(messages.items.length).toBeGreaterThanOrEqual(3);

    // Get the LATEST magic link
    const latestMessage = messages.items[0]; // Most recent first
    const latestLink = latestMessage.html.links[0].href;

    // Latest link works
    await page.goto(latestLink);
    await expect(page.getByTestId('user-menu')).toBeVisible();

    // Older links should NOT work (if backend invalidates previous)
    await page.getByTestId('sign-out').click();
    const olderLink = messages.items[1].html.links[0].href;

    await page.goto(olderLink);
    await expect(page.getByTestId('error-message')).toBeVisible();
  });

  test('should rate-limit excessive magic link requests', async ({ page }) => {
    const randomId = Math.floor(Math.random() * 1000000);
    const testEmail = `user-${randomId}@${MAILOSAUR_SERVER_ID}.mailosaur.net`;

    // Request magic link 10 times rapidly (should hit rate limit)
    for (let i = 0; i < 10; i++) {
      await page.goto('/login');
      await page.getByTestId('email-input').fill(testEmail);
      await page.getByTestId('send-magic-link').click();

      // After N requests, should show rate limit error
      const errorVisible = await page
        .getByTestId('rate-limit-error')
        .isVisible({ timeout: 1000 })
        .catch(() => false);

      if (errorVisible) {
        console.log(`Rate limit hit after ${i + 1} requests`);
        await expect(page.getByTestId('rate-limit-error')).toContainText(/too many.*requests|rate.*limit/i);
        return;
      }
    }

    // If no rate limit after 10 requests, log warning
    console.warn('⚠️  No rate limit detected after 10 requests');
  });
});

```

**Key Pontos**:

- * Ligações *Expired**: Teste fichas de 24 horas
- **Invalid tokens**: Informações ou fichas de lixo rejeitadas
- **Reuse prevenção**: O mesmo link não pode ser usado duas vezes
- **Rapid requisitions**: Vários pedidos tratados graciosamente
- * *Rate limitante**: Pedidos excessivos bloqueados

---

### Example 4: Caching Strategy with cypress-data-session / Playwright Projects

**Context**: Minimize email consumption by sharing authentication state across tests and specs.

**Implementation**:

```javascript
// cypress/support/commands/register-and-sign-in.js
import { dataSession } from 'cypress-data-session';

/**
 * Email Authentication Caching Strategy
 * - One email per test run (not per spec, not per test)
 * - First spec: Full registration flow (form → email → code → sign in)
 * - Subsequent specs: Only sign in (reuse user)
 * - Subsequent tests in same spec: Session already active (no sign in)
 */

// Helper: Fill registration form
function fillRegistrationForm({ fullName, userName, email, password }) {
  cy.intercept('POST', 'https://cognito-idp*').as('cognito');
  cy.contains('Register').click();
  cy.get('#reg-dialog-form').should('be.visible');
  cy.get('#first-name').type(fullName, { delay: 0 });
  cy.get('#last-name').type(lastName, { delay: 0 });
  cy.get('#email').type(email, { delay: 0 });
  cy.get('#username').type(userName, { delay: 0 });
  cy.get('#password').type(password, { delay: 0 });
  cy.contains('button', 'Create an account').click();
  cy.wait('@cognito').its('response.statusCode').should('equal', 200);
}

// Helper: Confirm registration with email code
function confirmRegistration(email) {
  return cy
    .mailosaurGetMessage(Cypress.env('MAILOSAUR_SERVERID'), { sentTo: email })
    .its('html.codes.0.value') // Mailosaur auto-extracts codes!
    .then((code) => {
      cy.intercept('POST', 'https://cognito-idp*').as('cognito');
      cy.get('#verification-code').type(code, { delay: 0 });
      cy.contains('button', 'Confirm registration').click();
      cy.wait('@cognito');
      cy.contains('You are now registered!').should('be.visible');
      cy.contains('button', /ok/i).click();
      return cy.wrap(code); // Return code for reference
    });
}

// Helper: Full registration (form + email)
function register({ fullName, userName, email, password }) {
  fillRegistrationForm({ fullName, userName, email, password });
  return confirmRegistration(email);
}

// Helper: Sign in
function signIn({ userName, password }) {
  cy.intercept('POST', 'https://cognito-idp*').as('cognito');
  cy.contains('Sign in').click();
  cy.get('#sign-in-username').type(userName, { delay: 0 });
  cy.get('#sign-in-password').type(password, { delay: 0 });
  cy.contains('button', 'Sign in').click();
  cy.wait('@cognito');
  cy.contains('Sign out').should('be.visible');
}

/**
 * Register and sign in with email caching
 * ONE EMAIL PER MACHINE (cypress run or cypress open)
 */
Cypress.Commands.add('registerAndSignIn', ({ fullName, userName, email, password }) => {
  return dataSession({
    name: email, // Unique session per email

    // First time: Full registration (form → email → code)
    init: () => register({ fullName, userName, email, password }),

    // Subsequent specs: Just check email exists (code already used)
    setup: () => confirmRegistration(email),

    // Always runs after init/setup: Sign in
    recreate: () => signIn({ userName, password }),

    // Share across ALL specs (one email for entire test run)
    shareAcrossSpecs: true,
  });
});

```

**Usage across multiple specs**:

```javascript
// cypress/e2e/place-order.cy.ts
describe('Place Order', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.registerAndSignIn({
      fullName: Cypress.env('fullName'), // From cypress.config
      userName: Cypress.env('userName'),
      email: Cypress.env('email'), // SAME email across all specs
      password: Cypress.env('password'),
    });
  });

  it('should place order', () => {
    /*...*/
  });
  it('should view order history', () => {
    /*...*/
  });
});

// cypress/e2e/profile.cy.ts
describe('User Profile', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.registerAndSignIn({
      fullName: Cypress.env('fullName'),
      userName: Cypress.env('userName'),
      email: Cypress.env('email'), // SAME email - no new email sent!
      password: Cypress.env('password'),
    });
  });

  it('should update profile', () => {
    /*...*/
  });
});

```

**Playwright equivalent with storageState**:

```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  projects: [
    {
      name: 'setup',
      testMatch: /global-setup\.ts/,
    },
    {
      name: 'authenticated',
      testMatch: /.*\.spec\.ts/,
      dependencies: ['setup'],
      use: {
        storageState: '.auth/user-session.json', // Reuse auth state
      },
    },
  ],
});

```

```typescript
// tests/global-setup.ts (runs once)
import { test as setup } from '@playwright/test';
import { getMagicLinkFromEmail } from './support/mailosaur-helpers';

const authFile = '.auth/user-session.json';

setup('authenticate via magic link', async ({ page }) => {
  const testEmail = process.env.TEST_USER_EMAIL!;

  // Request magic link
  await page.goto('/login');
  await page.getByTestId('email-input').fill(testEmail);
  await page.getByTestId('send-magic-link').click();

  // Get and visit magic link
  const magicLink = await getMagicLinkFromEmail(testEmail);
  await page.goto(magicLink);

  // Verify authenticated
  await expect(page.getByTestId('user-menu')).toBeVisible();

  // Save authenticated state (ONE TIME for all tests)
  await page.context().storageState({ path: authFile });

  console.log('✅ Authentication state saved to', authFile);
});

```

**Key Points**:

- **One email per run**: Global setup authenticates once
- **State reuse**: All tests use cached storageState
- **cypress-data-session**: Intelligently manages cache lifecycle
- **shareAcrossSpecs**: Session shared across all spec files
- **Massive savings**: 500 tests = 1 email (not 500!)

---

## Lista de verificação de testes de autenticação de e- mail

Antes de implementar testes de autenticação de email, verifique:

- [ ] **Email service**: Mailosauro/Ethereal/MailHog configurado com chaves API
- [ ] **Link extraction**: Use a análise integrada (html.links[0].href) sobre regex
- [ ] **State preservation**: localStorage/session/cookies salvas e restauradas
- [ ] **Session caching**: cypress-data-sessão ou armazenamentoState previne e-mails redundantes
- [ ] * Fluxos *Negative**: Expirados, inválidos, reutilizados, pedidos rápidos testados
- [ ] **Quota conscience**: Um email por execução (não por teste)
- [ ] **PII limpeza**: IDs de email registrados para depuração, mas esfregados de artefatos
- [ ] **Timeout manipulação**: 30 segundo tempo de recuperação de e-mail configurado

## Pontos de Integração

- Usado em fluxos de trabalho: `*framework` (setup de autenticação de email), `*automate` (geração de teste de autenticação de email)
- Fragmentos relacionados: `fixture-architecture.md`, `test-quality.md`
- Serviços de e-mail: Mailosauro (recomendado), Ethereal (gratuito), MailHog (self-hosted)
- Plugins: cipreste-mailossauro, Cipreste-sessão de dados

_Source: Email blog de autenticação, kit de ferramentas de teste Murat, documentação Mailossauro
