# Fábricas de dados e API-Primeira Configuração

## Princípio

Prefere funções de fábrica que aceitem sobreposições e devolva objetos completos (`createUser(overrides)`). O estado de teste de sementes através de APIs, tarefas ou ajudadores diretos de DB antes de visitar a UI — nunca através de interações lentas de UI. IU é apenas para validação, não para configuração.

## Racional

As fixações estáticas (arquivos JSON, objetos codificados) criam testes quebradiços que:

- Falha quando os esquemas evoluem (faltando novos campos obrigatórios)
- Causa colisões em execução paralela (mesmo IDs de usuário)
- Esconder intenção de teste (o que importa para *this* teste?)

Fábricas dinâmicas com sobreposições fornecer:

- **Segurança paralela**: UUIDs e timestamps evitam colisões
- **Evolução do esquema**: Os padrões adaptam-se automaticamente às alterações do esquema
- **Intenção explícita**: Sobrescritos mostram o que importa para cada teste
- **Speed**: A configuração da API é 10-50x mais rápida do que a UI

## Exemplos de padrões

### Exemplo 1: Função de fábrica com substituições

**Contexto**: Ao criar dados de teste, construa funções de fábrica com padrões sensíveis e sobreposições explícitas. Use `faker` para valores dinâmicos que evitam colisões.

**Implementation**:

```typescript
// test-utils/factories/user-factory.ts
import { faker } from '@faker-js/faker';

type User = {
  id: string;
  email: string;
  name: string;
  role: 'user' | 'admin' | 'moderator';
  createdAt: Date;
  isActive: boolean;
};

export const createUser = (overrides: Partial<User> = {}): User => ({
  id: faker.string.uuid(),
  email: faker.internet.email(),
  name: faker.person.fullName(),
  role: 'user',
  createdAt: new Date(),
  isActive: true,
  ...overrides,
});

// test-utils/factories/product-factory.ts
type Product = {
  id: string;
  name: string;
  price: number;
  stock: number;
  category: string;
};

export const createProduct = (overrides: Partial<Product> = {}): Product => ({
  id: faker.string.uuid(),
  name: faker.commerce.productName(),
  price: parseFloat(faker.commerce.price()),
  stock: faker.number.int({ min: 0, max: 100 }),
  category: faker.commerce.department(),
  ...overrides,
});

// Usage in tests:
test('admin can delete users', async ({ page, apiRequest }) => {
  // Default user
  const user = createUser();

  // Admin user (explicit override shows intent)
  const admin = createUser({ role: 'admin' });

  // Seed via API (fast!)
  await apiRequest({ method: 'POST', url: '/api/users', data: user });
  await apiRequest({ method: 'POST', url: '/api/users', data: admin });

  // Now test UI behavior
  await page.goto('/admin/users');
  await page.click(`[data-testid="delete-user-${user.id}"]`);
  await expect(page.getByText(`User ${user.name} deleted`)).toBeVisible();
});

```

**Pontos-chave**

- `Partial<User>` permite sobrescrever qualquer campo sem quebrar a segurança do tipo
- Faker gera valores únicos – sem colisões em testes paralelos
- Substituir mostra intenção de teste: BMADPROTECCT004END é explícito
- Fábrica vive em `test-utils/factories/` para fácil reutilização

### Exemplo 2: Padrão de fábrica aninhado

**Contexto**: Ao testar relações (ordens com usuários e produtos), fábricas de ninhos para criar gráficos de objetos completos. Controle os dados de relacionamento explicitamente.

**Implementation**:

«``typescript
// test-utils/factories/order-factory.ts
BMADPROTECT029end BMADPROTECT046end de './usuário-fábrica';
import { createProduct } from './product-factory';

Tipo OrderItem = {
  product: Product;
  quantity: number;
  price: number;
};

Tipo Ordem = {
  id: string;
  user: User;
  items: OrderItem[];
  total: number;
  status: 'pending' | 'paid' | 'shipped' | 'delivered';
  createdAt: Date;
};

export BMADPROTECT026End createOrderItem = (sobrerrogação: Parcial<OrderItem> = {}): OrderItem => BMADPROTECT042End);

{
    product,
    quantity,
    price: product.price * quantity,
    ...overrides,
  } de retorno;
};

BMADPROTECT023End BMADPROTECT022End createOrder = (sobrescritos: ParcialBMADPROTECT008End = {}): Ordem => {
  const items = overrides.items || [createOrderItem(), createOrderItem()];
  const total = items.reduce((sum, item) => sum + item.price, 0);

  return {
    id: faker.string.uuid(),
    user: overrides.user || createUser(),
    items,
    total,
    status: 'pending',
    createdAt: new Date(),
    ...overrides,
  };
};

// Uso em testes:
bMADPROTECT019END ({ page, apiRequest }) => bMADPROTECT038END);
const product1 = createProduct({ name: 'Widget A', price: 10.0 });
const product2 = createProduct({ name: 'Widget B', price: 15.0 });

// Relacionamentos explícitos
const order = createOrder({
    user,
    items: [
      createOrderItem({ product: product1, quantity: 2 }), // $20
createOrderItem( { product: product2, quantity: 1 }), // $15
],
});

// Sementes via API
await apiRequest({ method: 'POST', url: '/api/users', data: user });
await apiRequest({ method: 'POST', url: '/api/products', data: product1 });
await apiPedido( { método: 'POST', url: '/api/prod