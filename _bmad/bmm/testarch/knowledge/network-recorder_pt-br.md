# Utilitário de Gravador de Rede

## Princípio

Grave o tráfego de rede para arquivos HAR durante a execução do teste, em seguida, jogar de volta do disco para testes offline. Permite que testes frontend sejam executados em completo isolamento de serviços backend com detecção de CRUD de estado inteligente para um comportamento API realista.

## Racional

Testes tradicionais E2E requerem serviços de infraestrutura ao vivo:

- Lento (latenza real da rede)
- Flaky (instabilidade de backend afeta testes)
- Caro (pilha completa em execução para testes de UI)
- Juntado (os testes UI quebram quando a API muda)

A gravação/reprodução baseada no HAR fornece:

- **True off-line tests**: testes de IU executados sem infra-estrutura
- **Comportamento determinístico**: As mesmas respostas sempre
- **Execução rápida**: Sem latência de rede
- **Socagem de Estado**: as operações CRUD funcionam naturalmente (não apenas para leitura)
- **Flexibilidade do ambiente**: URLs do mapa para qualquer ambiente

## Exemplos de padrões

### Exemplo 1: Registro básico e reprodução

**Contexto**: O padrão fundamental - gravar tráfego uma vez, reproduzir para todas as corridas subsequentes.

**Implementation**:

```typescript
import { test } from '@seontechnologies/playwright-utils/network-recorder/fixtures';

// Set mode in test file (recommended)
process.env.PW_NET_MODE = 'playback'; // or 'record'

test('CRUD operations work offline', async ({ page, context, networkRecorder }) => {
  // Setup recorder (records or plays back based on PW_NET_MODE)
  await networkRecorder.setup(context);

  await page.goto('/');

  // First time (record mode): Records all network traffic to HAR
  // Subsequent runs (playback mode): Plays back from HAR (no backend!)
  await page.fill('#movie-name', 'Inception');
  await page.click('#add-movie');

  // Intelligent CRUD detection makes this work offline!
  await expect(page.getByText('Inception')).toBeVisible();
});

```

**Pontos-chave**

- `PW_NET_MODE=record` captura tráfego para arquivos HAR
- `PW_NET_MODE=playback` replays de arquivos HAR
- Definir modo no arquivo de teste ou via variável de ambiente
- Arquivos HAR auto-organizados pelo nome do teste
- A zombaria estatal detecta operações CRUD

### Exemplo 2: CRUD completo Fluxo com HAR

**Contexto**: Fluxo completo de criação-leitura-atualização-delete que funciona completamente offline.

**Implementation**:

```typescript
process.env.PW_NET_MODE = 'playback';

test.describe('Movie CRUD - offline with network recorder', () => {
  test.beforeEach(async ({ page, networkRecorder, context }) => {
    await networkRecorder.setup(context);
    await page.goto('/');
  });

  test('should add, edit, delete movie browser-only', async ({ page, interceptNetworkCall }) => {
    // Create
    await page.fill('#movie-name', 'Inception');
    await page.fill('#year', '2010');
    await page.click('#add-movie');

    // Verify create (reads from stateful HAR)
    await expect(page.getByText('Inception')).toBeVisible();

    // Update
    await page.getByText('Inception').click();
    await page.fill('#movie-name', "Inception Director's Cut");

    const updateCall = interceptNetworkCall({
      method: 'PUT',
      url: '/movies/*',
    });

    await page.click('#save');
    await updateCall; // Wait for update

    // Verify update (HAR reflects state change!)
    await page.click('#back');
    await expect(page.getByText("Inception Director's Cut")).toBeVisible();

    // Delete
    await page.click(`[data-testid="delete-Inception Director's Cut"]`);

    // Verify delete (HAR reflects removal!)
    await expect(page.getByText("Inception Director's Cut")).not.toBeVisible();
  });
});

```

**Pontos-chave**

- Operações CRUD completas funcionam offline
- Faixas de zombaria HAR estatal cria/atualiza/deleta
- Combine com `interceptNetworkCall` para esperas determinísticas
- Primeiro registo de execução, posterior repetição de execuções

### Exemplo 3: Mudança de ambiente

**Contexto**: Gravar em ambiente dev, reproduzir em CI com URLs de base diferentes.

**Implementation**:

```typescript
// playwright.config.ts - Map URLs for different environments
export default defineConfig({
  use: {
    baseURL: process.env.CI ? 'https://app.ci.example.com' : 'http://localhost:3000',
  },
});

// Test works in both environments
test('cross-environment playback', async ({ page, context, networkRecorder }) => {
  await networkRecorder.setup(context);

  // In dev: hits http://localhost:3000/api/movies
  // In CI: HAR replays with https://app.ci.example.com/api/movies
  await page.goto('/movies');

  // Network recorder auto-maps URLs
  await expect(page.getByTestId('movie-list')).toBeVisible();
});

```

**Pontos-chave**

- Arquivos HAR registram URLs absolutas
- Reproduzir mapas para a base atualURL
- O mesmo HAR funciona em ambientes
- Não é necessário reescrever URL manual

### Exemplo 4: Controle automático contra modo manual

**Contexto**: Escolha entre comutação baseada em ambiente ou controle em modo de teste.

**Implementation**:

«``typescript
// Opção 1: Variável ambiente (recomendada para IC)
PW_NET_MODE=record npm run test:pw # Registro de tráfego
PW_NET_MODE=playback npm run test:pw # Tráfego de reprodução

// Opção 2: Controlo no ensaio (recomendado para