# Utilitário Network Recorder

## Princípio

Grave tráfego de rede em arquivos HAR durante execução de teste, então reproduza a partir do disco para teste offline. Permite que testes de frontend rodem em isolamento completo de serviços backend com detecção inteligente de CRUD stateful para comportamento realista de API.

## Motivação

Testes E2E tradicionais requerem serviços backend ativos:

- Lentos (latência de rede real)
- Instáveis (instabilidade de backend afeta testes)
- Caros (full stack rodando para testes de UI)
- Acoplados (testes de UI quebram quando API muda)

Gravação/reprodução baseada em HAR fornece:

- **Teste offline verdadeiro**: Testes de UI rodam sem backend
- **Comportamento determinístico**: Mesmas respostas toda vez
- **Execução rápida**: Sem latência de rede
- **Mocking stateful**: Operações CRUD funcionam naturalmente (não apenas somente-leitura)
- **Flexibilidade de ambiente**: Mapeia URLs para qualquer ambiente

## Exemplos de Padrões

### Exemplo 1: Gravação e Reprodução Básica

**Contexto**: O padrão fundamental - grave tráfego uma vez, reproduza para todas as execuções subsequentes.

**Implementação**:

```typescript
import { test } from '@seontechnologies/playwright-utils/network-recorder/fixtures';

// Definir modo no arquivo de teste (recomendado)
process.env.PW_NET_MODE = 'playback'; // ou 'record'

test('operações CRUD funcionam offline', async ({ page, context, networkRecorder }) => {
  // Setup gravador (grava ou reproduz baseado em PW_NET_MODE)
  await networkRecorder.setup(context);

  await page.goto('/');

  // Primeira vez (modo gravação): Grava todo tráfego de rede para HAR
  // Execuções subsequentes (modo reprodução): Reproduz a partir do HAR (sem backend!)
  await page.fill('#movie-name', 'Inception');
  await page.click('#add-movie');

  // Detecção inteligente de CRUD faz isso funcionar offline!
  await expect(page.getByText('Inception')).toBeVisible();
});
```

**Pontos Chave**:

- `PW_NET_MODE=record` captura tráfego para arquivos HAR
- `PW_NET_MODE=playback` reproduz a partir de arquivos HAR
- Defina modo no arquivo de teste ou via variável de ambiente
- Arquivos HAR auto-organizados por nome de teste
- Mocking stateful detecta operações CRUD

### Exemplo 2: Fluxo CRUD Completo com HAR

**Contexto**: Fluxo criar-ler-atualizar-deletar completo que funciona totalmente offline.

**Implementação**:

```typescript
process.env.PW_NET_MODE = 'playback';

test.describe('CRUD de Filmes - offline com network recorder', () => {
  test.beforeEach(async ({ page, networkRecorder, context }) => {
    await networkRecorder.setup(context);
    await page.goto('/');
  });

  test('deve adicionar, editar, deletar filme browser-only', async ({ page, interceptNetworkCall }) => {
    // Criar
    await page.fill('#movie-name', 'Inception');
    await page.fill('#year', '2010');
    await page.click('#add-movie');

    // Verificar criação (lê de HAR stateful)
    await expect(page.getByText('Inception')).toBeVisible();

    // Atualizar
    await page.getByText('Inception').click();
    await page.fill('#movie-name', "Inception Director's Cut");

    const updateCall = interceptNetworkCall({
      method: 'PUT',
      url: '/movies/*',
    });

    await page.click('#save');
    await updateCall; // Aguardar atualização

    // Verificar atualização (HAR reflete mudança de estado!)
    await page.click('#back');
    await expect(page.getByText("Inception Director's Cut")).toBeVisible();

    // Deletar
    await page.click(`[data-testid="delete-Inception Director's Cut"]`);

    // Verificar deleção (HAR reflete remoção!)
    await expect(page.getByText("Inception Director's Cut")).not.toBeVisible();
  });
});
```

**Pontos Chave**:

- Operações CRUD completas funcionam offline
- Mocking stateful HAR rastreia criações/atualizações/deleções
- Combine com `interceptNetworkCall` para esperas determinísticas
- Primeira execução grava, execuções subsequentes reproduzem

### Exemplo 3: Troca de Ambiente

**Contexto**: Gravar em ambiente dev, reproduzir em CI com URLs base diferentes.

**Implementação**:

```typescript
// playwright.config.ts - Mapear URLs para ambientes diferentes
export default defineConfig({
  use: {
    baseURL: process.env.CI ? 'https://app.ci.example.com' : 'http://localhost:3000',
  },
});

// Teste funciona em ambos ambientes
test('reprodução entre ambientes', async ({ page, context, networkRecorder }) => {
  await networkRecorder.setup(context);

  // Em dev: atinge http://localhost:3000/api/movies
  // Em CI: HAR reproduz com https://app.ci.example.com/api/movies
  await page.goto('/movies');

  // Network recorder auto-mapeia URLs
  await expect(page.getByTestId('movie-list')).toBeVisible();
});
```

**Pontos Chave**:

- Arquivos HAR gravam URLs absolutas
- Reprodução mapeia para baseURL atual
- Mesmo HAR funciona entre ambientes
- Nenhuma reescrita manual de URL necessária

### Exemplo 4: Controle de Modo Automático vs Manual

**Contexto**: Escolha entre troca baseada em ambiente ou controle de modo no teste.

**Implementação**:

```typescript
// Opção 1: Variável de ambiente (recomendado para CI)
PW_NET_MODE=record npm run test:pw   # Gravar tráfego
PW_NET_MODE=playback npm run test:pw # Reproduzir tráfego

// Opção 2: Controle no teste (recomendado para desenvolvimento)
process.env.PW_NET_MODE = 'record'  // Definir no topo do arquivo de teste

test('meu teste', async ({ page, context, networkRecorder }) => {
  await networkRecorder.setup(context)
  // ...
})

// Opção 3: Auto-fallback (grava se HAR faltar, senão reproduz)
// Este é o comportamento padrão quando PW_NET_MODE não definido
test('modo auto', async ({ page, context, networkRecorder }) => {
  await networkRecorder.setup(context)
  // Primeira execução: auto-grava
  // Execuções subsequentes: auto-reproduz
})
```

**Pontos Chave**:

- Três opções de modo: record, playback, auto
- Variável de ambiente `PW_NET_MODE`
- Atribuição `process.env.PW_NET_MODE` no teste
- Auto-fallback quando nenhum modo especificado

## Por Que Usar Isso em Vez de Playwright Nativo?

| Playwright Nativo (`routeFromHAR`) | Utilitário network-recorder    |
| ---------------------------------- | ------------------------------ |
| ~80 linhas boilerplate setup       | ~5 linhas total                |
| Gerenciamento manual arquivo HAR   | Organização automática arquivo |
| Setup/teardown complexo            | Limpeza automática via fixtures|
| **Testes somente-leitura**         | **Suporte CRUD completo**      |
| **Stateless**                      | **Mocking stateful**           |
| Mapeamento manual URL              | Mapeamento ambiente automático |

**O divisor de águas: Detecção CRUD Stateful**

Reprodução HAR nativa do Playwright é stateless - um POST criar seguido por GET lista não mostrará o item criado. Este utilitário rastreia inteligentemente operações CRUD em memória para refletir mudanças de estado, fazendo testes offline se comportarem como APIs reais.

## Integração com Outros Utilitários

**Com interceptNetworkCall** (esperas determinísticas):

```typescript
test('use ambos utilitários', async ({ page, context, networkRecorder, interceptNetworkCall }) => {
  await networkRecorder.setup(context);

  const createCall = interceptNetworkCall({
    method: 'POST',
    url: '/api/movies',
  });

  await page.click('#add-movie');
  await createCall; // Aguardar criar (funciona com HAR!)

  // Network recorder fornece reprodução, intercept fornece determinismo
});
```

## Fragmentos Relacionados

- `overview.md` - Instalação e padrões de fixture
- `intercept-network-call.md` - Combinar para testes offline determinísticos
- `auth-session.md` - Gravar tráfego autenticado
- `network-first.md` - Padrão core para interceptar-antes-navegar

## Anti-Padrões

**❌ Misturar gravar e reproduzir no mesmo teste:**

```typescript
process.env.PW_NET_MODE = 'record';
// ... algum código de teste ...
process.env.PW_NET_MODE = 'playback'; // Não troque no meio do teste
```

**✅ Um modo por teste:**

```typescript
process.env.PW_NET_MODE = 'playback'; // Defina uma vez no topo

test('meu teste', async ({ page, context, networkRecorder }) => {
  await networkRecorder.setup(context);
  // Teste inteiro usa modo reprodução
});
```

**❌ Esquecer de chamar setup:**

```typescript
test('quebrado', async ({ page, networkRecorder }) => {
  await page.goto('/'); // HAR não ativo!
});
```

**✅ Sempre chame setup antes da navegação:**

```typescript
test('correto', async ({ page, context, networkRecorder }) => {
  await networkRecorder.setup(context); // Deve configurar primeiro
  await page.goto('/'); // Agora HAR está ativo
});
```
