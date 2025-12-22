# Essenciais de ensaio de contratos (Pacto)

## Princípio

Testes de contrato validam contratos de API entre serviços de consumidores e fornecedores sem exigir testes integrados de ponta a ponta. Armazene contratos de consumidor ao lado de especificações de integração, contratos de versão semanticamente e publique em cada corrida de CI. A verificação do provedor antes de mesclar superfícies quebrando as alterações imediatamente, enquanto o comportamento de retrocesso explícito (tempos, repetições, cargas de erro) captura garantias de resiliência em contratos.

## Racional

Testes de integração tradicionais requerem executar simultaneamente tanto o consumidor quanto o provedor, criando testes lentos e flácidos com configuração complexa. Testes de contrato dissociam serviços: os consumidores definem expectativas (arquivos de pact), os fornecedores verificam de forma independente contra essas expectativas. Isso permite o desenvolvimento paralelo, captura quebrando as alterações precocemente e documenta o comportamento da API como especificações executáveis. Emparelhe testes de contrato com testes de fumaça API para validar o mapeamento de dados e renderização de UI em conjunto.

## Exemplos de padrões

### Exemplo 1: Teste do Consumidor Pacto (Frontende → API da infra-estrutura)

**Contexto**: Reagir o aplicativo consumindo uma API de gerenciamento de usuários, definindo interações esperadas.

**Implementation**:

«``typescript
// testes/contrato/utilizador-api.pact.spec.ts
BMADPROTECT022end BMADPROTECT046end de '@ pact- foundation/pact';
import BMADPROTECT045End de '@/api/user-service';

BMADPROTECT020end { like, eachLike, string, integer } = MatchersV3;

/**
* Teste de contrato conduzido pelo consumidor
* - Consumer (React app) define o comportamento esperado da API
* - Gera o arquivo pact para o provedor verificar
* - Executa em isolamento (sem necessidade de infraestrutura real)
*/

BMADPROTECT019End fornecedor = novo PactoV3({
  consumer: 'user-management-web',
  provider: 'user-api-service',
  dir: './pacts', // Output directory for pact files
  logLevel: 'warn',
});

Description('User API Contract', () => {
  describe('GET /users/:id', () => {
    it('should return user when user exists', async () => {
      // Arrange: Define expected interaction
      await provider
        .given('user with id 1 exists') // Provider state
        .uponReceiving('a request for user 1')
        .withRequest({
          method: 'GET',
          path: '/users/1',
          headers: {
            Accept: 'application/json',
            Authorization: like('Bearer token123'), // Matcher: any string
          },
})
.Responderá({
          status: 200,
          headers: {
            'Content-Type': 'application/json',
          },
          body: like ({
            id: integer(1),
            name: string('John Doe'),
            email: string('john@example.com'),
            role: string('user'),
            createdAt: string('2025-01-15T10:00:00Z'),
          }),
})
.executeTest(async (mockServer) => {
          // Act: Call consumer code against mock server
          const user = await getUserById(1, {
            baseURL: mockServer.url,
            headers: { Authorization: 'Bearer token123' },
});

// Assert: Validar o comportamento do consumidor
espera( utilizador). para igual(
object.
);
});
});

bMADPROTECT013END () => {
      await provider
        .given('user with id 999 does not exist')
        .uponReceiving('a request for non-existent user')
        .withRequest({
          method: 'GET',
          path: '/users/999',
          headers: { Accept: 'application/json' },
})
.Responderá({
          status: 404,
          headers: { 'Content-Type': 'application/json' },
          body: {
            error: 'User not found',
            code: 'USER_NOT_FOUND',
          },
})
.executeTest(async (mockServer) => {
          // Act & Assert: Consumer handles 404 gracefully
          await expect(getUserById(999, { baseURL: mockServer.url })).rejeita.paraJogar('User not found');
});
});
});

descrever('POST/usuários', () => {
    it('should create user and return 201', async () => {
      const newUser: Omit<User, 'id' | 'createdAt'> = {
        name: 'Jane Smith',
        email: 'jane@example.com',
        role: 'admin',
      };

BMADPROTECT007End fornecedor
. given('não existem utilizadores')
.uponReceiveing('uma solicitação para criar um usuário')
.comPedido({
          method: 'POST',
          path: '/users',
          headers: {
            'Content-Type': 'application/json',
            Accept: 'application/json',
          },
          body: like (novo utilizador),
})
.Responderá({
          status: 201,
          headers: { 'Content-Type': 'application/json' },
          body: like ({
            id: integer(2),
            name: string('Jane Smith'),
            email: string (**jane@example.com**)
            role: string('Admin'),
            createdAt: string('2025-01-15T11:00Z')