# Critérios não funcionais (NFR)

## Princípio

Os requisitos não funcionais (segurança, desempenho, confiabilidade, manutenção) são **validados através de testes automatizados**, não de checklists. A avaliação NFR utiliza critérios objetivos de aprovação/fracasso ligados a limiares mensuráveis. Requisitos ambíguos por omissão para CONCENTRAÇÃO até ser clarificado.

## Racional

**The Problem**: Equipes enviam características que "trabalham" funcionalmente, mas falham sob carga, expõem vulnerabilidades de segurança ou falta de recuperação de erros. NFRs são tratados como opcionais "bom-para-haves" em vez de bloqueadores de liberação.

**A Solução**: Defina critérios NFR explícitos com validação automatizada. Testes de segurança verificam auth/authz e manipulação secreta. Os testes de desempenho impõem limiares SLO/SLA com evidências de perfil. Testes de confiabilidade validam o manuseio de erros, tentativas e verificações de saúde. A manutenção é medida por cobertura de teste, duplicação de código e observação.

**Por que isso importa**:

- Evita incidentes de produção (violências de segurança, degradação de desempenho, falhas em cascata)
- Fornece critérios objetivos de liberação (sem subjetiva "sentir rápido o suficiente")
- Automatiza validação de conformidade (via de auditoria para ambientes regulamentados)
- Força a clareza sobre os requisitos ambíguos (por omissão para CONCENTRAÇÃO)

## Exemplos de padrões

### Exemplo 1: Validação NFR de segurança (Autenticação, Segredos, OWASP)

**Contexto**: Testes de segurança automatizados que impõem autenticação, autorização e manipulação secreta

**Implementation**:

«``typescript
// testes/nfr/segurança.spec.ts
BMADPROTECT051end BMADPROTECT065end de '@ playwright/test';

test.describe('Security NFR: Autenticação & Autorização', () => {
  test('unauthenticated users cannot access protected routes', async ({ page }) => {
    // Attempt to access dashboard without auth
    await page.goto('/dashboard');

    // Should redirect to login (not expose data)
    await expect(page).toHaveURL(/\/login/);
    await expect(page.getByText('Please sign in')).toBeVisible();

    // Verify no sensitive data leaked in response
    const pageContent = await page.content();
    expect(pageContent).not.toContain('user_id');
    expect(pageContent).not.toContain('api_key');
  });

teste ("tokens JWT expiram após 15 minutos", async ({ page, request }) => {
    // Login and capture token
    await page.goto('/login');
    await page.getByLabel('Email').fill('test@example.com');
    await page.getByLabel('Password').fill('ValidPass123!');
    await page.getByRole('button', { name: 'Sign In' }).clique();

const token = await page.avaliar(() => localStorage.getItem('auth token'));
Esperar(conhecido).ser verdade();

// Espere 16 minutos (use relógio simulado em testes reais)
BMADPROTECT037End page.clock.fastForward('BMADPROTECT052End');

// Token deve ser expirado, chamada API deve falhar
const = await request.get('/api/usuário/perfil', {
      headers: { Authorization: `Bearer ${token}` },
});

esperar(response.status().toBe( 401);
BMADPROTECT034end corpo = BMADPROTECT033end BMADPROTECT007end();
esperar(corpo.error).Conter('expirado');
});

bMADPROTECT032END ({ page }) => bMADPROTECT058END.clique();

// Erro mostrado ao usuário (mensagem genérica)
await expect(page.getByText('Certificações inválidas')).toBeVisible();

// Verificar senha NUNCA aparece no console, DOM ou rede
const pageContent = await page.content();
espera( pageContent). not. toContain('WrongPassword123!');
espera(consoleLogs.join('\n')). not. toContain('WrongPassword123!');
});

test('RBAC: os utilizadores só podem aceder aos recursos que possuem', async ({ page, request }) => {
    // Login as User A
    const userAToken = await login(request, 'userA@example.com', 'password');

    // Try to access User B's order
    const response = await request.get('/api/orders/user-b-order-id', {
      headers: { Authorization: `Bearer ${userAToken}` },
});

expect( response.status ().toBe( 403); // Proibido
const corpo = await response.json();
esperar(body.error).Conter('permissões insuficientes');
});

bmadprotect016END ({ page }) => bmadprotect054END.clique();

// Deve retornar resultados vazios, NÃO falhar ou expor erro
await expect(page.getByText('Nenhum resultado encontrado')). toBeVisible();

// Verificar aplicativo ainda funciona (table not droped)
BMADPROTECT011End page.goto('/dashboard');
await expect(page.getByText('Welcome')). toBeVisible();
});

teste('As tentativas de XSS são higienizadas', async ({ page }) =>