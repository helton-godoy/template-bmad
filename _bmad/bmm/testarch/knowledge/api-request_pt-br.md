# Utilitário de Pedido de API

## Princípio

Use o cliente HTTP digitado com validação de esquema incorporada e tentativa automática para erros de servidor. O utilitário lida com resolução de URL, gerenciamento de cabeçalhos, análise de respostas e validação de resposta de uma única linha com suporte adequado ao TypeScript.

## Racional

A API de pedido de Vanilla Playwright requer caldeira para padrões comuns:

- Processamento manual JSON (`await response.json()`)
- Verificação do estado repetitivo
- Nenhuma lógica de repetição incorporada para falhas transitórias
- Não há validação do esquema
- Construção de URL complexa

O utilitário `apiRequest` fornece:

- **Automatic JSON análise**: corpo de resposta pré-parsed
- **Built-in retry**: erros 5xx retry com backoff exponencial
- **Validação do esquema**: validação de linha única (JSON Schema, Zod, OpenAPI)
- **Resolução URL**: Estratégia de quatro níveis (explicável > configuração > dramaturgo > directo)
- **TypeScript generics**: organismos de resposta seguros

## Exemplos de padrões

### Exemplo 1: Pedido básico da API

**Contexto**: Fazer pedidos de API autenticados com repetição automática e segurança de tipo.

**Implementation**:

```typescript
import { test } from '@seontechnologies/playwright-utils/api-request/fixtures';

test('should fetch user data', async ({ apiRequest }) => {
  const { status, body } = await apiRequest<User>({
    method: 'GET',
    path: '/api/users/123',
    headers: { Authorization: 'Bearer token' },
  });

  expect(status).toBe(200);
  expect(body.name).toBe('John Doe'); // TypeScript knows body is User
});

```

**Pontos-chave**

- Tipo genérico `<User>` fornece autocompleto TipoScript para `body`
- Estatuto e corpo desestruturados da resposta
- Cabeçalhos passados como objeto
- Repetição automática de erros de 5xx (configurável)

### Exemplo 2: Validação do esquema (linha única)

**Contexto**: Validar as respostas API correspondem ao esquema esperado com sintaxe de linha única.

**Implementation**:

```typescript
import { test } from '@seontechnologies/playwright-utils/api-request/fixtures';

test('should validate response schema', async ({ apiRequest }) => {
  // JSON Schema validation
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
  // Throws if schema validation fails

  // Zod schema validation
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
  // Response body is type-safe AND validated
});

```

**Pontos-chave**

- Parâmetro `validateSchema` único
- Suporta arquivos JSON Schema, Zod, YAML, especificações OpenAPI
- Lança falha na validação com erros detalhados
- Código de validação da placa de caldeira zero

### Exemplo 3: POST com Configuração de Corpo e Repetição

**Contexto**: Criando recursos com comportamento de repetição personalizado para testar erros.

**Implementation**:

```typescript
test('should create user', async ({ apiRequest }) => {
  const newUser = {
    name: 'Jane Doe',
    email: 'jane@example.com',
  };

  const { status, body } = await apiRequest({
    method: 'POST',
    path: '/api/users',
    body: newUser, // Automatically sent as JSON
    headers: { Authorization: 'Bearer token' },
  });

  expect(status).toBe(201);
  expect(body.id).toBeDefined();
});

// Disable retry for error testing
test('should handle 500 errors', async ({ apiRequest }) => {
  await expect(
    apiRequest({
      method: 'GET',
      path: '/api/error',
      retryConfig: { maxRetries: 0 }, // Disable retry
    }),
  ).rejects.toThrow('Request failed with status 500');
});

```

**Pontos-chave**

- parâmetro `body` auto-serializa para JSON
- Repetição padrão: erros de 5xx, 3 repetições, recuo exponencial
- Desactivar a repetição com `retryConfig: { maxRetries: 0 }`
- Apenas erros 5xx repetir (4 erros xx falhar imediatamente)

### Exemplo 4: Estratégia de resolução de URL

**Contexto**: Tratamento flexível de URLs para diferentes ambientes e contextos de teste.

**Implementation**:

«``typescript
// Estratégia 1: Base explícitaUrl (maior prioridade)
await apiRequest({
  method: 'GET',
  path: '/users',
  baseUrl: 'https://api.example.com', // Uses https://api.example.com/users
});

// Estratégia 2: Base de configuraçãoURL (do dispositivo)
import { test } de '@seontechnologies/playwright-utils/api-request/fixtures';

ensaio.uso({ configBaseUrl: 'https://staging-api.example.com' });

Teste('usa baseURL', async ({ apiRequest }) => {
  await apiRequest({
    method: 'GET',
    path: '/users', // Uses https://staging-api.example.com/users
  });
});

// Estratégia 3: Base do dramaturgoURL (do dramaturgo. config.ts)
// dramaturgo.config.ts
export defineConfig ({
  use: {
    baseURL: 'https://api.example.com',
  },
});

Teste('usa baseURL', async ({ apiRequest }) = > {
BMADPROTECT021End apir