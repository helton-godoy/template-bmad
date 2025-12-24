# Utilitário API Request

## Princípio

Use um cliente HTTP tipado com validação de esquema integrada e retentativa automática para erros de servidor. O utilitário lida com resolução de URL, gerenciamento de headers, parsing de resposta e validação de resposta em linha única com suporte TypeScript adequado.

## Motivação

A API de request do Playwright puro requer boilerplate para padrões comuns:

- Parsing manual de JSON (`await response.json()`)
- Verificação de código de status repetitiva
- Sem lógica de retentativa integrada para falhas transitórias
- Sem validação de esquema
- Construção de URL complexa

O utilitário `apiRequest` fornece:

- **Parsing automático de JSON**: Corpo da resposta pré-parseado
- **Retentativa integrada**: Erros 5xx tentam novamente com backoff exponencial
- **Validação de esquema**: Validação em linha única (JSON Schema, Zod, OpenAPI)
- **Resolução de URL**: Estratégia de quatro níveis (explícito > config > Playwright > direto)
- **Genéricos TypeScript**: Corpos de resposta type-safe

## Exemplos de Padrões

### Exemplo 1: Requisição de API Básica

**Contexto**: Fazendo requisições de API autenticadas com retentativa automática e segurança de tipos.

**Implementação**:

```typescript
import { test } from '@seontechnologies/playwright-utils/api-request/fixtures';

test('deve buscar dados do usuário', async ({ apiRequest }) => {
  const { status, body } = await apiRequest<User>({
    method: 'GET',
    path: '/api/users/123',
    headers: { Authorization: 'Bearer token' },
  });

  expect(status).toBe(200);
  expect(body.name).toBe('John Doe'); // TypeScript sabe que body é User
});
```

**Pontos Chave**:

- Tipo genérico `<User>` fornece autocompletar TypeScript para `body`
- Status e body desestruturados da resposta
- Headers passados como objeto
- Retentativa automática para erros 5xx (configurável)

### Exemplo 2: Validação de Esquema (Linha Única)

**Contexto**: Validar respostas de API correspondendo ao esquema esperado com sintaxe de linha única.

**Implementação**:

```typescript
import { test } from '@seontechnologies/playwright-utils/api-request/fixtures';

test('deve validar esquema da resposta', async ({ apiRequest }) => {
  // Validação JSON Schema
  const response = await apiRequest({
    method: 'GET',
    path: '/api/users/123',
    validateSchema: {
      type: 'object',
      required: ['id', 'name', 'email'],
      properties: {
        id: { type: 'string' },
        name: { type: 'string' },
        email: { type: 'string', format: 'email' },
      },
    },
  });
  // Lança erro se validação de esquema falhar

  // Validação de esquema Zod
  import { z } from 'zod';

  const UserSchema = z.object({
    id: z.string(),
    name: z.string(),
    email: z.string().email(),
  });

  const response = await apiRequest({
    method: 'GET',
    path: '/api/users/123',
    validateSchema: UserSchema,
  });
  // Corpo da resposta é type-safe E validado
});
```

**Pontos Chave**:

- Parâmetro único `validateSchema`
- Suporta JSON Schema, Zod, arquivos YAML, specs OpenAPI
- Lança erro na falha de validação com erros detalhados
- Zero código boilerplate de validação

### Exemplo 3: POST com Body e Configuração de Retentativa

**Contexto**: Criando recursos com comportamento de retentativa personalizado para testes de erro.

**Implementação**:

```typescript
test('deve criar usuário', async ({ apiRequest }) => {
  const newUser = {
    name: 'Jane Doe',
    email: 'jane@example.com',
  };

  const { status, body } = await apiRequest({
    method: 'POST',
    path: '/api/users',
    body: newUser, // Automaticamente enviado como JSON
    headers: { Authorization: 'Bearer token' },
  });

  expect(status).toBe(201);
  expect(body.id).toBeDefined();
});

// Desativar retentativa para teste de erro
test('deve tratar erros 500', async ({ apiRequest }) => {
  await expect(
    apiRequest({
      method: 'GET',
      path: '/api/error',
      retryConfig: { maxRetries: 0 }, // Desativa retentativa
    }),
  ).rejects.toThrow('Request failed with status 500');
});
```

**Pontos Chave**:

- Parâmetro `body` auto-serializa para JSON
- Retentativa padrão: erros 5xx, 3 retries, backoff exponencial
- Desative retentativa com `retryConfig: { maxRetries: 0 }`
- Apenas erros 5xx tentam novamente (erros 4xx falham imediatamente)

### Exemplo 4: Estratégia de Resolução de URL

**Contexto**: Tratamento de URL flexível para diferentes ambientes e contextos de teste.

**Implementação**:

```typescript
// Estratégia 1: baseUrl explícito (prioridade mais alta)
await apiRequest({
  method: 'GET',
  path: '/users',
  baseUrl: 'https://api.example.com', // Usa https://api.example.com/users
});

// Estratégia 2: Config baseURL (da fixture)
import { test } from '@seontechnologies/playwright-utils/api-request/fixtures';

test.use({ configBaseUrl: 'https://staging-api.example.com' });

test('usa config baseURL', async ({ apiRequest }) => {
  await apiRequest({
    method: 'GET',
    path: '/users', // Usa https://staging-api.example.com/users
  });
});

// Estratégia 3: Playwright baseURL (do playwright.config.ts)
// playwright.config.ts
export default defineConfig({
  use: {
    baseURL: 'https://api.example.com',
  },
});

test('usa Playwright baseURL', async ({ apiRequest }) => {
  await apiRequest({
    method: 'GET',
    path: '/users', // Usa https://api.example.com/users
  });
});

// Estratégia 4: Caminho direto (URL completa)
await apiRequest({
  method: 'GET',
  path: 'https://api.example.com/users', // URL completa funciona também
});
```

**Pontos Chave**:

- Resolução de quatro níveis: explícito > config > Playwright > direto
- Barras finais normalizadas automaticamente
- BaseUrl específico do ambiente fácil de configurar

### Exemplo 5: Integração com Recurse (Polling)

**Contexto**: Aguardando operações assíncronas completarem (jobs em segundo plano, consistência eventual).

**Implementação**:

```typescript
import { test } from '@seontechnologies/playwright-utils/fixtures';

test('deve fazer polling até o job completar', async ({ apiRequest, recurse }) => {
  // Cria job
  const { body } = await apiRequest({
    method: 'POST',
    path: '/api/jobs',
    body: { type: 'export' },
  });

  const jobId = body.id;

  // Poll até estar pronto
  const completedJob = await recurse(
    () => apiRequest({ method: 'GET', path: `/api/jobs/${jobId}` }),
    (response) => response.body.status === 'completed',
    { timeout: 60000, interval: 2000 },
  );

  expect(completedJob.body.result).toBeDefined();
});
```

**Pontos Chave**:

- `apiRequest` retorna objeto de resposta completo
- `recurse` faz polling até o predicado retornar verdadeiro
- Utilitários combináveis funcionam juntos sem problemas

## Comparação com Playwright Puro

| Playwright Puro                                | playwright-utils apiRequest                                                        |
| ---------------------------------------------- | ---------------------------------------------------------------------------------- |
| `const resp = await request.get('/api/users')` | `const { status, body } = await apiRequest({ method: 'GET', path: '/api/users' })` |
| `const body = await resp.json()`               | Resposta já parseada                                                               |
| `expect(resp.ok()).toBeTruthy()`               | Código de status diretamente acessível                                             |
| Sem lógica de retentativa                      | Auto-retry erros 5xx com backoff                                                   |
| Sem validação de esquema                       | Validação multiformato integrada                                                   |
| Tratamento de erro manual                      | Mensagens de erro descritivas                                                      |

## Quando Usar

**Use apiRequest para:**

- ✅ Teste de endpoint de API
- ✅ Chamadas de API em segundo plano em testes de UI
- ✅ Necessidades de validação de esquema
- ✅ Testes requerendo lógica de retentativa
- ✅ Respostas de API tipadas

**Fique com Playwright puro para:**

- Requisições únicas simples onde overhead do utilitário não vale a pena
- Testar recursos nativos do Playwright especificamente
- Testes legados onde migração não é justificada

## Fragmentos Relacionados

- `overview.md` - Instalação e princípios de design
- `auth-session.md` - Gerenciamento de token de autenticação
- `recurse.md` - Polling para operações assíncronas
- `fixtures-composition.md` - Combinando utilitários com mergeTests
- `log.md` - Logging de requisições de API

## Anti-Padrões

**❌ Ignorar falhas de retentativa:**

```typescript
try {
  await apiRequest({ method: 'GET', path: '/api/unstable' });
} catch {
  // Falha silenciosa - perde informação de retentativa
}
```

**✅ Deixe retentativas acontecerem, trate falha final:**

```typescript
await expect(apiRequest({ method: 'GET', path: '/api/unstable' })).rejects.toThrow(); // Retentativas acontecem automaticamente, então erro final capturado
```

**❌ Desativar benefícios do TypeScript:**

```typescript
const response: any = await apiRequest({ method: 'GET', path: '/users' });
```

**✅ Use tipos genéricos:**

```typescript
const { body } = await apiRequest<User[]>({ method: 'GET', path: '/users' });
// body é tipado como User[]
```
