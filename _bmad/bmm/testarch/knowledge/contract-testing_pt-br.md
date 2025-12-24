# Essenciais de Teste de Contrato (Pact)

## Princípio

Testes de contrato validam contratos de API entre serviços consumidores e provedores sem exigir testes integrados de ponta a ponta. Armazene contratos de consumidor junto com especificações de integração, versione contratos semanticamente e publique em cada execução de CI. A verificação do provedor antes do merge expõe mudanças que quebram imediatamente, enquanto o comportamento de fallback explícito (timeouts, tentativas, payloads de erro) captura garantias de resiliência nos contratos.

## Motivação

Testes de integração tradicionais requerem rodar tanto consumidor quanto provedor simultaneamente, criando testes lentos, instáveis e com setup complexo. Testes de contrato desacoplam serviços: consumidores definem expectativas (arquivos pact), provedores verificam contra essas expectativas independentemente. Isso permite desenvolvimento paralelo, captura mudanças que quebram cedo e documenta o comportamento da API como especificações executáveis. Emparelhe testes de contrato com smoke tests de API para validar mapeamento de dados e renderização de UI em conjunto.

## Exemplos de Padrões

### Exemplo 1: Teste de Consumidor Pact (Frontend → API Backend)

**Contexto**: Aplicação React consumindo uma API de gerenciamento de usuários, definindo interações esperadas.

**Implementação**:

```typescript
// tests/contract/user-api.pact.spec.ts
import { PactV3, MatchersV3 } from '@pact-foundation/pact';
import { getUserById, createUser, User } from '@/api/user-service';

const { like, eachLike, string, integer } = MatchersV3;

/**
 * Teste de Contrato Orientado ao Consumidor
 * - Consumidor (App React) define comportamento esperado da API
 * - Gera arquivo pact para o provedor verificar
 * - Roda isolado (sem backend real necessário)
 */

const provider = new PactV3({
  consumer: 'user-management-web',
  provider: 'user-api-service',
  dir: './pacts', // Diretório de saída para arquivos pact
  logLevel: 'warn',
});

describe('Contrato da API de Usuário', () => {
  describe('GET /users/:id', () => {
    it('deve retornar usuário quando usuário existe', async () => {
      // Arrange: Define interação esperada
      await provider
        .given('usuário com id 1 existe') // Estado do provedor
        .uponReceiving('uma requisição para usuário 1')
        .withRequest({
          method: 'GET',
          path: '/users/1',
          headers: {
            Accept: 'application/json',
            Authorization: like('Bearer token123'), // Matcher: qualquer string
          },
        })
        .willRespondWith({
          status: 200,
          headers: {
            'Content-Type': 'application/json',
          },
          body: like({
            id: integer(1),
            name: string('John Doe'),
            email: string('john@example.com'),
            role: string('user'),
            createdAt: string('2025-01-15T10:00:00Z'),
          }),
        })
        .executeTest(async (mockServer) => {
          // Act: Chama código do consumidor contra servidor mock
          const user = await getUserById(1, {
            baseURL: mockServer.url,
            headers: { Authorization: 'Bearer token123' },
          });

          // Assert: Valida comportamento do consumidor
          expect(user).toEqual(
            expect.objectContaining({
              id: 1,
              name: 'John Doe',
              email: 'john@example.com',
              role: 'user',
            }),
          );
        });
    });

    it('deve tratar 404 quando usuário não existe', async () => {
      await provider
        .given('usuário com id 999 não existe')
        .uponReceiving('uma requisição para usuário inexistente')
        .withRequest({
          method: 'GET',
          path: '/users/999',
          headers: { Accept: 'application/json' },
        })
        .willRespondWith({
          status: 404,
          headers: { 'Content-Type': 'application/json' },
          body: {
            error: 'User not found',
            code: 'USER_NOT_FOUND',
          },
        })
        .executeTest(async (mockServer) => {
          // Act & Assert: Consumidor trata 404 graciosamente
          await expect(getUserById(999, { baseURL: mockServer.url })).rejects.toThrow('User not found');
        });
    });
  });

  describe('POST /users', () => {
    it('deve criar usuário e retornar 201', async () => {
      const newUser: Omit<User, 'id' | 'createdAt'> = {
        name: 'Jane Smith',
        email: 'jane@example.com',
        role: 'admin',
      };

      await provider
        .given('não existem usuários')
        .uponReceiving('uma requisição para criar um usuário')
        .withRequest({
          method: 'POST',
          path: '/users',
          headers: {
            'Content-Type': 'application/json',
            Accept: 'application/json',
          },
          body: like(newUser),
        })
        .willRespondWith({
          status: 201,
          headers: { 'Content-Type': 'application/json' },
          body: like({
            id: integer(2),
            name: string('Jane Smith'),
            email: string('jane@example.com'),
            role: string('admin'),
            createdAt: string('2025-01-15T11:00:00Z'),
          }),
        })
        .executeTest(async (mockServer) => {
          const createdUser = await createUser(newUser, {
            baseURL: mockServer.url,
          });

          expect(createdUser).toEqual(
            expect.objectContaining({
              id: expect.any(Number),
              name: 'Jane Smith',
              email: 'jane@example.com',
              role: 'admin',
            }),
          );
        });
    });
  });
});
```

**scripts package.json**:

```json
{
  "scripts": {
    "test:contract": "jest tests/contract --testTimeout=30000",
    "pact:publish": "pact-broker publish ./pacts --consumer-app-version=$GIT_SHA --broker-base-url=$PACT_BROKER_URL --broker-token=$PACT_BROKER_TOKEN"
  }
}
```

**Pontos Chave**:

- **Orientado ao Consumidor**: Frontend define expectativas, não backend
- **Matchers**: `like`, `string`, `integer` para correspondência flexível
- **Estados do Provedor**: given() configura pré-condições de teste
- **Isolamento**: Nenhum backend real necessário, roda rápido
- **Geração de Pact**: Automaticamente cria arquivos pact JSON

---

### Exemplo 2: Verificação do Provedor Pact (Backend valida contratos)

**Contexto**: API Node.js/Express verificando pacts publicados por consumidores.

**Implementação**:

```typescript
// tests/contract/user-api.provider.spec.ts
import { Verifier, VerifierOptions } from '@pact-foundation/pact';
import { server } from '../../src/server'; // Sua app Express/Fastify
import { seedDatabase, resetDatabase } from '../support/db-helpers';

/**
 * Teste de Verificação do Provedor
 * - Provedor (API backend) verifica contra pacts publicados
 * - State handlers configuram dados de teste para cada interação
 * - Roda antes do merge para capturar mudanças que quebram
 */

describe('Verificação de Provedor Pact', () => {
  let serverInstance;
  const PORT = 3001;

  beforeAll(async () => {
    // Inicia servidor provedor
    serverInstance = server.listen(PORT);
    console.log(`Servidor provedor rodando na porta ${PORT}`);
  });

  afterAll(async () => {
    // Limpeza
    await serverInstance.close();
  });

  it('deve verificar pacts de todos os consumidores', async () => {
    const opts: VerifierOptions = {
      // Detalhes do provedor
      provider: 'user-api-service',
      providerBaseUrl: `http://localhost:${PORT}`,

      // Configuração do Pact Broker
      pactBrokerUrl: process.env.PACT_BROKER_URL,
      pactBrokerToken: process.env.PACT_BROKER_TOKEN,
      publishVerificationResult: process.env.CI === 'true',
      providerVersion: process.env.GIT_SHA || 'dev',

      // State handlers: Configura estado do provedor para cada interação
      stateHandlers: {
        'usuário com id 1 existe': async () => {
          await seedDatabase({
            users: [
              {
                id: 1,
                name: 'John Doe',
                email: 'john@example.com',
                role: 'user',
                createdAt: '2025-01-15T10:00:00Z',
              },
            ],
          });
          return 'Usuário semeado com sucesso';
        },

        'usuário com id 999 não existe': async () => {
          // Garante que usuário não existe
          await resetDatabase();
          return 'Database resetado';
        },

        'não existem usuários': async () => {
          await resetDatabase();
          return 'Database vazio';
        },
      },

      // Filtros de requisição: Adiciona headers de auth a todas as requisições
      requestFilter: (req, res, next) => {
        // Mock autenticação para verificação
        req.headers['x-user-id'] = 'test-user';
        req.headers['authorization'] = 'Bearer valid-test-token';
        next();
      },

      // Timeout para verificação
      timeout: 30000,
    };

    // Roda verificação
    await new Verifier(opts).verifyProvider();
  });
});
```

**Integração CI**:

```yaml
# .github/workflows/pact-provider.yml
name: Verificação de Provedor Pact
on:
  pull_request:
  push:
    branches: [main]

jobs:
  verify-contracts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version-file: '.nvmrc'

      - name: Instalar dependências
        run: npm ci

      - name: Iniciar banco de dados
        run: docker-compose up -d postgres

      - name: Rodar migrações
        run: npm run db:migrate

      - name: Verificar pacts
        run: npm run test:contract:provider
        env:
          PACT_BROKER_URL: ${{ secrets.PACT_BROKER_URL }}
          PACT_BROKER_TOKEN: ${{ secrets.PACT_BROKER_TOKEN }}
          GIT_SHA: ${{ github.sha }}
          CI: true

      - name: Posso Fazer Deploy?
        run: |
          npx pact-broker can-i-deploy \
            --pacticipant user-api-service \
            --version ${{ github.sha }} \
            --to-environment production
        env:
          PACT_BROKER_BASE_URL: ${{ secrets.PACT_BROKER_URL }}
          PACT_BROKER_TOKEN: ${{ secrets.PACT_BROKER_TOKEN }}
```

**Pontos Chave**:

- **State handlers**: Configura dados do provedor para cada estado given()
- **Filtros de requisição**: Adiciona auth/headers para requisições de verificação
- **Publicação CI**: Resultados de verificação enviados para o broker
- **can-i-deploy**: Verificação de segurança antes do deploy em produção
- **Isolamento de banco**: Reset entre state handlers

---

### Exemplo 3: Integração CI de Contrato (Fluxo Consumidor & Provedor)

**Contexto**: Fluxo CI/CD completo coordenando publicação de pact do consumidor e verificação do provedor.

**Implementação**:

```yaml
# .github/workflows/pact-consumer.yml (Lado Consumidor)
name: Testes de Consumidor Pact
on:
  pull_request:
  push:
    branches: [main]

jobs:
  consumer-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version-file: '.nvmrc'

      - name: Instalar dependências
        run: npm ci

      - name: Rodar testes de contrato do consumidor
        run: npm run test:contract

      - name: Publicar pacts no broker
        if: github.ref == 'refs/heads/main' || github.event_name == 'pull_request'
        run: |
          npx pact-broker publish ./pacts \
            --consumer-app-version ${{ github.sha }} \
            --branch ${{ github.head_ref || github.ref_name }} \
            --broker-base-url ${{ secrets.PACT_BROKER_URL }} \
            --broker-token ${{ secrets.PACT_BROKER_TOKEN }}

      - name: Tag pact com ambiente (main branch apenas)
        if: github.ref == 'refs/heads/main'
        run: |
          npx pact-broker create-version-tag \
            --pacticipant user-management-web \
            --version ${{ github.sha }} \
            --tag production \
            --broker-base-url ${{ secrets.PACT_BROKER_URL }} \
            --broker-token ${{ secrets.PACT_BROKER_TOKEN }}
```

```yaml
# .github/workflows/pact-provider.yml (Lado Provedor)
name: Verificação de Provedor Pact
on:
  pull_request:
  push:
    branches: [main]
  repository_dispatch:
    types: [pact_changed] # Webhook do Pact Broker

jobs:
  verify-contracts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version-file: '.nvmrc'

      - name: Instalar dependências
        run: npm ci

      - name: Iniciar dependências
        run: docker-compose up -d

      - name: Rodar verificação do provedor
        run: npm run test:contract:provider
        env:
          PACT_BROKER_URL: ${{ secrets.PACT_BROKER_URL }}
          PACT_BROKER_TOKEN: ${{ secrets.PACT_BROKER_TOKEN }}
          GIT_SHA: ${{ github.sha }}
          CI: true

      - name: Publicar resultados da verificação
        if: always()
        run: echo "Resultados de verificação publicados no broker"

      - name: Posso Fazer Deploy para Produção?
        if: github.ref == 'refs/heads/main'
        run: |
          npx pact-broker can-i-deploy \
            --pacticipant user-api-service \
            --version ${{ github.sha }} \
            --to-environment production \
            --broker-base-url ${{ secrets.PACT_BROKER_URL }} \
            --broker-token ${{ secrets.PACT_BROKER_TOKEN }} \
            --retry-while-unknown 6 \
            --retry-interval 10

      - name: Registrar deploy (se can-i-deploy passou)
        if: success() && github.ref == 'refs/heads/main'
        run: |
          npx pact-broker record-deployment \
            --pacticipant user-api-service \
            --version ${{ github.sha }} \
            --environment production \
            --broker-base-url ${{ secrets.PACT_BROKER_URL }} \
            --broker-token ${{ secrets.PACT_BROKER_TOKEN }}
```

**Configuração de Webhook do Pact Broker**:

```json
{
  "events": [
    {
      "name": "contract_content_changed"
    }
  ],
  "request": {
    "method": "POST",
    "url": "https://api.github.com/repos/sua-org/user-api/dispatches",
    "headers": {
      "Authorization": "Bearer ${user.githubToken}",
      "Content-Type": "application/json",
      "Accept": "application/vnd.github.v3+json"
    },
    "body": {
      "event_type": "pact_changed",
      "client_payload": {
        "pact_url": "${pactbroker.pactUrl}",
        "consumer": "${pactbroker.consumerName}",
        "provider": "${pactbroker.providerName}"
      }
    }
  }
}
```

**Pontos Chave**:

- **Gatilho automático**: Mudanças no pact do consumidor disparam verificação do provedor via webhook
- **Rastreamento de branch**: Pacts publicados por branch para teste de feature
- **can-i-deploy**: Portão de segurança antes do deploy em produção
- **Registrar deploy**: Rastreia qual versão está em cada ambiente
- **Dev Paralelo**: Times de consumidor e provedor trabalham independentemente

---

### Exemplo 4: Cobertura de Resiliência (Testando Comportamento de Fallback)

**Contexto**: Capturar comportamento de timeout, retentativa e tratamento de erro explicitamente em contratos.

**Implementação**:

```typescript
// tests/contract/user-api-resilience.pact.spec.ts
import { PactV3, MatchersV3 } from '@pact-foundation/pact';
import { getUserById, ApiError } from '@/api/user-service';

const { like, string } = MatchersV3;

const provider = new PactV3({
  consumer: 'user-management-web',
  provider: 'user-api-service',
  dir: './pacts',
});

describe('Contrato de Resiliência da API de Usuário', () => {
  /**
   * Teste de tratamento de erro 500
   * Verifica se o consumidor trata erros de servidor graciosamente
   */
  it('deve tratar erros 500 com lógica de retentativa', async () => {
    await provider
      .given('servidor está experimentando erros')
      .uponReceiving('uma requisição que retorna 500')
      .withRequest({
        method: 'GET',
        path: '/users/1',
        headers: { Accept: 'application/json' },
      })
      .willRespondWith({
        status: 500,
        headers: { 'Content-Type': 'application/json' },
        body: {
          error: 'Internal server error',
          code: 'INTERNAL_ERROR',
          retryable: true,
        },
      })
      .executeTest(async (mockServer) => {
        // Consumidor deve tentar novamente no 500
        try {
          await getUserById(1, {
            baseURL: mockServer.url,
            retries: 3,
            retryDelay: 100,
          });
          fail('Deveria ter lançado erro após retentativas');
        } catch (error) {
          expect(error).toBeInstanceOf(ApiError);
          expect((error as ApiError).code).toBe('INTERNAL_ERROR');
          expect((error as ApiError).retryable).toBe(true);
        }
      });
  });

  /**
   * Teste de rate limiting 429
   * Verifica se o consumidor respeita rate limits
   */
  it('deve tratar rate limit 429 com backoff', async () => {
    await provider
      .given('rate limit excedido para usuário')
      .uponReceiving('uma requisição que é limitada por taxa')
      .withRequest({
        method: 'GET',
        path: '/users/1',
      })
      .willRespondWith({
        status: 429,
        headers: {
          'Content-Type': 'application/json',
          'Retry-After': '60', // Tentar novamente após 60 segundos
        },
        body: {
          error: 'Too many requests',
          code: 'RATE_LIMIT_EXCEEDED',
        },
      })
      .executeTest(async (mockServer) => {
        try {
          await getUserById(1, {
            baseURL: mockServer.url,
            respectRateLimit: true,
          });
          fail('Deveria ter lançado erro de rate limit');
        } catch (error) {
          expect(error).toBeInstanceOf(ApiError);
          expect((error as ApiError).code).toBe('RATE_LIMIT_EXCEEDED');
          expect((error as ApiError).retryAfter).toBe(60);
        }
      });
  });

  /**
   * Teste de tratamento de timeout
   * Verifica se o consumidor tem configuração de timeout apropriada
   */
  it('deve dar timeout após 10 segundos', async () => {
    await provider
      .given('servidor está lento para responder')
      .uponReceiving('uma requisição que dá timeout')
      .withRequest({
        method: 'GET',
        path: '/users/1',
      })
      .willRespondWith({
        status: 200,
        headers: { 'Content-Type': 'application/json' },
        body: like({ id: 1, name: 'John' }),
      })
      .withDelay(15000) // Simula atraso de 15 segundos
      .executeTest(async (mockServer) => {
        try {
          await getUserById(1, {
            baseURL: mockServer.url,
            timeout: 10000, // timeout de 10 segundos
          });
          fail('Deveria ter dado timeout');
        } catch (error) {
          expect(error).toBeInstanceOf(ApiError);
          expect((error as ApiError).code).toBe('TIMEOUT');
        }
      });
  });

  /**
   * Teste de resposta parcial (campos opcionais)
   * Verifica se o consumidor lida com dados opcionais faltando
   */
  it('deve tratar resposta com campos opcionais faltando', async () => {
    await provider
      .given('usuário existe com dados mínimos')
      .uponReceiving('uma requisição para usuário com dados parciais')
      .withRequest({
        method: 'GET',
        path: '/users/1',
      })
      .willRespondWith({
        status: 200,
        headers: { 'Content-Type': 'application/json' },
        body: {
          id: integer(1),
          name: string('John Doe'),
          email: string('john@example.com'),
          // role, createdAt, etc. omitidos (campos opcionais)
        },
      })
      .executeTest(async (mockServer) => {
        const user = await getUserById(1, { baseURL: mockServer.url });

        // Consumidor trata campos opcionais faltando graciosamente
        expect(user.id).toBe(1);
        expect(user.name).toBe('John Doe');
        expect(user.role).toBeUndefined(); // Campo opcional
        expect(user.createdAt).toBeUndefined(); // Campo opcional
      });
  });
});
```

**Cliente API com lógica de retentativa**:

```typescript
// src/api/user-service.ts
import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';

export class ApiError extends Error {
  constructor(
    message: string,
    public code: string,
    public retryable: boolean = false,
    public retryAfter?: number,
  ) {
    super(message);
  }
}

/**
 * Cliente de API de Usuário com tratamento de erro e retentativa
 */
export async function getUserById(
  id: number,
  config?: AxiosRequestConfig & { retries?: number; retryDelay?: number; respectRateLimit?: boolean },
): Promise<User> {
  const { retries = 3, retryDelay = 1000, respectRateLimit = true, ...axiosConfig } = config || {};

  let lastError: Error;

  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      const response = await axios.get(`/users/${id}`, axiosConfig);
      return response.data;
    } catch (error: any) {
      lastError = error;

      // Trata rate limiting
      if (error.response?.status === 429) {
        const retryAfter = parseInt(error.response.headers['retry-after'] || '60');
        throw new ApiError('Too many requests', 'RATE_LIMIT_EXCEEDED', false, retryAfter);
      }

      // Tenta novamente em erros 500
      if (error.response?.status === 500 && attempt < retries) {
        await new Promise((resolve) => setTimeout(resolve, retryDelay * attempt));
        continue;
      }

      // Trata 404
      if (error.response?.status === 404) {
        throw new ApiError('User not found', 'USER_NOT_FOUND', false);
      }

      // Trata timeout
      if (error.code === 'ECONNABORTED') {
        throw new ApiError('Request timeout', 'TIMEOUT', true);
      }

      break;
    }
  }

  throw new ApiError('Request failed after retries', 'INTERNAL_ERROR', true);
}
```

**Pontos Chave**:

- **Contratos de resiliência**: Timeouts, retentativas, erros testados explicitamente
- **State handlers**: Provedor configura cada cenário de teste
- **Tratamento de erro**: Consumidor valida degradação graciosa
- **Lógica de retentativa**: Backoff exponencial testado
- **Campos opcionais**: Consumidor lida com respostas parciais

---

### Exemplo 4: Manutenção & Gerenciamento de Ciclo de Vida do Pact Broker

**Contexto**: Manutenção automatizada do broker para prevenir expansão descontrolada e ruído de contrato.

**Implementação**:

```typescript
// scripts/pact-broker-housekeeping.ts
/**
 * Script de Manutenção do Pact Broker
 * - Arquivar contratos substituídos
 * - Expirar pacts não utilizados
 * - Taggear releases para rastreamento de ambiente
 */

import { execSync } from 'child_process';

const PACT_BROKER_URL = process.env.PACT_BROKER_URL!;
const PACT_BROKER_TOKEN = process.env.PACT_BROKER_TOKEN!;
const PACTICIPANT = 'user-api-service';

/**
 * Taggear release com ambiente
 */
function tagRelease(version: string, environment: 'staging' | 'production') {
  console.log(`🏷️  Tagging ${PACTICIPANT} v${version} as ${environment}`);

  execSync(
    `npx pact-broker create-version-tag \
      --pacticipant ${PACTICIPANT} \
      --version ${version} \
      --tag ${environment} \
      --broker-base-url ${PACT_BROKER_URL} \
      --broker-token ${PACT_BROKER_TOKEN}`,
    { stdio: 'inherit' },
  );
}

/**
 * Registrar deploy para ambiente
 */
function recordDeployment(version: string, environment: 'staging' | 'production') {
  console.log(`📝 Recording deployment of ${PACTICIPANT} v${version} to ${environment}`);

  execSync(
    `npx pact-broker record-deployment \
      --pacticipant ${PACTICIPANT} \
      --version ${version} \
      --environment ${environment} \
      --broker-base-url ${PACT_BROKER_URL} \
      --broker-token ${PACT_BROKER_TOKEN}`,
    { stdio: 'inherit' },
  );
}

/**
 * Limpar versões antigas de pact (política de retenção)
 * Manter: últimos 30 dias, todas as tags de produção, mais recente de cada branch
 */
function cleanupOldPacts() {
  console.log(`🧹 Cleaning up old pacts for ${PACTICIPANT}`);

  execSync(
    `npx pact-broker clean \
      --pacticipant ${PACTICIPANT} \
      --broker-base-url ${PACT_BROKER_URL} \
      --broker-token ${PACT_BROKER_TOKEN} \
      --keep-latest-for-branch 1 \
      --keep-min-age 30`,
    { stdio: 'inherit' },
  );
}

/**
 * Verificar compatibilidade de deploy
 */
function canIDeploy(version: string, toEnvironment: string): boolean {
  console.log(`🔍 Checking if ${PACTICIPANT} v${version} can deploy to ${toEnvironment}`);

  try {
    execSync(
      `npx pact-broker can-i-deploy \
        --pacticipant ${PACTICIPANT} \
        --version ${version} \
        --to-environment ${toEnvironment} \
        --broker-base-url ${PACT_BROKER_URL} \
        --broker-token ${PACT_BROKER_TOKEN} \
        --retry-while-unknown 6 \
        --retry-interval 10`,
      { stdio: 'inherit' },
    );
    return true;
  } catch (error) {
    console.error(`❌ Cannot deploy to ${toEnvironment}`);
    return false;
  }
}

/**
 * Fluxo principal de manutenção
 */
async function main() {
  const command = process.argv[2];
  const version = process.argv[3];
  const environment = process.argv[4] as 'staging' | 'production';

  switch (command) {
    case 'tag-release':
      tagRelease(version, environment);
      break;

    case 'record-deployment':
      recordDeployment(version, environment);
      break;

    case 'can-i-deploy':
      const canDeploy = canIDeploy(version, environment);
      process.exit(canDeploy ? 0 : 1);

    case 'cleanup':
      cleanupOldPacts();
      break;

    default:
      console.error('Comando desconhecido. Use: tag-release | record-deployment | can-i-deploy | cleanup');
      process.exit(1);
  }
}

main();
```

**scripts package.json**:

```json
{
  "scripts": {
    "pact:tag": "ts-node scripts/pact-broker-housekeeping.ts tag-release",
    "pact:record": "ts-node scripts/pact-broker-housekeeping.ts record-deployment",
    "pact:can-deploy": "ts-node scripts/pact-broker-housekeeping.ts can-i-deploy",
    "pact:cleanup": "ts-node scripts/pact-broker-housekeeping.ts cleanup"
  }
}
```

**Integração de fluxo de deploy**:

```yaml
# .github/workflows/deploy-production.yml
name: Deploy para Produção
on:
  push:
    tags:
      - 'v*'

jobs:
  verify-contracts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Verificar compatibilidade pact
        run: npm run pact:can-deploy ${{ github.ref_name }} production
        env:
          PACT_BROKER_URL: ${{ secrets.PACT_BROKER_URL }}
          PACT_BROKER_TOKEN: ${{ secrets.PACT_BROKER_TOKEN }}

  deploy:
    needs: verify-contracts
    runs-on: ubuntu-latest
    steps:
      - name: Deploy para produção
        run: ./scripts/deploy.sh production

      - name: Registrar deploy no Pact Broker
        run: npm run pact:record ${{ github.ref_name }} production
        env:
          PACT_BROKER_URL: ${{ secrets.PACT_BROKER_URL }}
          PACT_BROKER_TOKEN: ${{ secrets.PACT_BROKER_TOKEN }}
```

**Limpeza agendada**:

```yaml
# .github/workflows/pact-housekeeping.yml
name: Manutenção do Pact Broker
on:
  schedule:
    - cron: '0 2 * * 0' # Semanalmente no domingo às 2 AM

jobs:
  cleanup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Limpar pacts antigos
        run: npm run pact:cleanup
        env:
          PACT_BROKER_URL: ${{ secrets.PACT_BROKER_URL }}
          PACT_BROKER_TOKEN: ${{ secrets.PACT_BROKER_TOKEN }}
```

**Pontos Chave**:

- **Tagging automatizado**: Releases taggeados com ambiente
- **Rastreamento de deploy**: Broker sabe qual versão está onde
- **Portão de segurança**: can-i-deploy bloqueia deploys incompatíveis
- **Política de retenção**: Manter pacts recentes, de produção e mais recentes de branch
- **Gatilhos de webhook**: Verificação do provedor roda em mudanças do consumidor

---

## Checklist de Teste de Contrato

Antes de implementar teste de contrato, verifique:

- [ ] **Setup do Pact Broker**: Hospedado (Pactflow) ou self-hosted broker configurado
- [ ] **Testes de consumidor**: Geram pacts no CI, publicam no broker no merge
- [ ] **Verificação de provedor**: Roda no PR, verifica todos os pacts de consumidor
- [ ] **State handlers**: Provedor implementa todos os estados given()
- [ ] **can-i-deploy**: Bloqueia deploy se contratos incompatíveis
- [ ] **Webhooks configurados**: Mudanças no consumidor disparam verificação do provedor
- [ ] **Política de retenção**: Pacts antigos arquivados (manter 30 dias, todas as tags de produção)
- [ ] **Resiliência testada**: Timeouts, retentativas, códigos de erro nos contratos

## Pontos de Integração

- Usado em workflows: `*automate` (geração de teste de integração), `*ci` (setup de CI de contrato)
- Fragmentos relacionados: `test-levels-framework.md`, `ci-burn-in.md`
- Ferramentas: Pact.js, Pact Broker (Pactflow ou self-hosted), Pact CLI

_Fonte: Repos de amostra consumidor/provedor Pact, blog de teste de contrato Murat, documentação oficial Pact_
