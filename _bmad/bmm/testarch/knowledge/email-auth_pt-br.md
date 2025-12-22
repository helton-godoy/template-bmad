# Teste de autenticação baseado em e- mail

## Princípio

Autenticação baseada em e-mail (links mágicos, códigos únicos, login sem senha) requer testes especializados com serviços de captura de e-mail como Mailosauro ou Ethereal. Extrair links mágicos via processamento HTML ou usar extração de links embutidos, preservar o armazenamento do navegador (local/sessão/cookies) ao processar links, cache e-mail cargas úteis para evitar esgotar quotas de caixa de entrada, e cobrir casos negativos (links expirados, links reutilizados, múltiplos pedidos rápidos). Registre IDs de e-mail e links para solução de problemas, mas limpe PII antes de cometer artefatos.

## Racional

A autenticação por e-mail introduz desafios únicos: entrega assíncrona de e-mail, limites de cotas (AWS Cognito: 50/dia), custo por e-mail e gestão complexa do estado (preservação da sessão através de cliques de link). Sem padrões adequados, os testes tornam-se lentos (esperar por e-mail cada vez), caros (exaustão de quota), e quebradiços (problemas de tempo, estado ausente). Usando serviços de captura de email + cache de sessão + padrões de preservação de estado torna testes de autenticação de email rápidos, confiáveis e econômicos.

## Exemplos de padrões

### Exemplo 1: Extração de ligação mágica com Mailosauro

**Contexto**: fluxo de login sem senha onde o usuário recebe o link mágico via e-mail, clica nele e é autenticado.

**Implementation**:

«``typescript
// testes/e2e/ligação mágica-auth.spec.ts
import { test, expect } de '@ playwright/test';

/**
* Fluxo de autenticação de ligação mágica
* 1. Usuário entra e-mail
* 2. Backend envia link mágico
* 3. Teste recupera e-mail via Mailosauro
* 4. Extrair e visitar o link mágico
* 5. Verifique o usuário está autenticado
*/

// Configuração do Mailosauro
BMADPROTECT047end MAILOSAUR_API_KEY = process.env.MAILOSAUR_API_KEY!;
BMADPROTECT046end MAILOSAUR_SERVER_ID = process.env.MAILOSAUR_SERVER_ID!;

/**
* Extrair href do corpo de e-mail HTML
* DOMParser fornece análise XML/HTML no Node.js
*/
function extractMagicLink( HTMLString: string): string □ null {
  const { JSDOM } = require( 'jsdom');
const dom = novo JSDOM( HTMLString);
const link = dom.window.document.querySelector('#magic-link-botton');
retornar link ? (link como HTMLAnchorElement). href : null;
}

/**
* Alternativa: Use a extração de link integrada do Mailossauro
* Mailossauro automaticamente analisa links - nenhum regex necessário!
*/
BMADPROTECT041End BMADPROTECT040End getMagicLinkFromEmail(email: string): PromessaBMADPROTECT005End BMADPROTECT062End,
{
      timeout: 30000, // 30 seconds
    },
);

// Mailossauro extrai links automaticamente - não é necessário analisar!
const magicLink = message.html?.links?.[0]?.href;

se (!magicLink) {
    throw new Error(`Magic link not found in email to ${email}`);
  }

console.log(`📧 Email received. Magic link extracted: ${magicLink}`);
Return magicLink;
}

test.describe ("Autenticação Mágica da Ligação", () => {
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

bMADPROTECT019END ({ page }) => bMADPROTECT056END);

bMADPROTECT013END ({ page }) = > {
const randomId = Math.floor(Math.random( * 1000000);
BMADPROTECT011Email = `user-${randomId}@${MAILOSAUR_SERVER_ID}.mailosaur.net`;

// Solicitar link mágico
await page.goto('/login');
await page.getByTest Id('email-input').fill(testEmail);
aw