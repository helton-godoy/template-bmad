# ATDD Checklist - {epic_num}, História {story_num}: {story_title}

**Data:** {date}
**Autor:** {user_name}
**Nível de teste primário:** {primary_level}

---

## Story Summary

{Brief 2-3 sentence summary of the user story}

**As a** {user_role}
**I want** {feature_description}
**So that** {business_value}

---

## Critérios de aceitação

{List all testable acceptance criteria from the story}

1. {Acceptance criterion 1}
2. {Acceptance criterion 2}
3. {Acceptance criterion 3}

---

## Failing Tests Created (RED Phase)

### E2E Tests ({e2e_test_count} tests)

**File:** `{e2e_test_file_path}` ({line_count} lines)

{List each E2E test with its current status and expected failure reason}

- ✅ **Test:** {test_name}
  - **Status:** RED - {failure_reason}
  - **Verifies:** {what_this_test_validates}

### API Tests ({api_test_count} tests)

**File:** `{api_test_file_path}` ({line_count} lines)

{List each API test with its current status and expected failure reason}

- ✅ **Test:** {test_name}
  - **Status:** RED - {failure_reason}
  - **Verifies:** {what_this_test_validates}

### Component Tests ({component_test_count} tests)

**File:** `{component_test_file_path}` ({line_count} lines)

{List each component test with its current status and expected failure reason}

- ✅ **Test:** {test_name}
  - **Status:** RED - {failure_reason}
  - **Verifies:** {what_this_test_validates}

---

## Fábricas de dados criadas

{List all data factory files created with their exports}

### {Entity} Fábrica

**Ficheiro:** `tests/support/factories/{entity}.factory.ts`

**Exportações:**

- `create{Entity}(overrides?)` - Criar uma única entidade com sobreposições opcionais
- `create{Entity}s(count)` - Criar array de entidades

**Exemplo Uso:**

```typescript
const user = createUser({ email: 'specific@example.com' });
const users = createUsers(5); // Generate 5 random users

```

---

## Fixtures Created

{List all test fixture files created with their fixture names and descriptions}

### {Feature} Fixtures

**File:** `tests/support/fixtures/{feature}.fixture.ts`

**Fixtures:**

- `{fixtureName}` - {description_of_what_fixture_provides}
  - **Setup:** {what_setup_does}
  - **Provides:** {what_test_receives}
  - **Cleanup:** {what_cleanup_does}

**Example Usage:**

```typescript
import { test } from './fixtures/{feature}.fixture';

test('should do something', async ({ {fixtureName} }) => {
  // {fixtureName} is ready to use with auto-cleanup
});

```

---

## Requisitos de simulação

{Document external services that need mocking and their requirements}

### {Service Name} Mock

**Endpoint:** `{HTTP_METHOD} {endpoint_url}`

**Resposta ao sucesso:**

```json
{
  {success_response_example}
}

```

**Resposta negativa:**

```json
{
  {failure_response_example}
}

```

**Notas:** {any_special_mock_requirements}

---

## Required data-testid Attributes

{List all data-testid attributes required in UI implementation for test stability}

### {Page or Component Name}

- `{data-testid-name}` - {description_of_element}
- `{data-testid-name}` - {description_of_element}

**Implementation Example:**

```tsx
<button data-testid="login-button">Log In</button>
<input data-testid="email-input" type="email" />
<div data-testid="error-message">{errorText}</div>

```

---

## Implementation Lista de verificação

{Map each failing test to concrete implementation tasks that will make it pass}

### Ensaio: {test_name_1}

**Ficheiro:** `{test_file_path}`

**Pedidos para fazer este teste passar:**

- {Implementation task 1}
{Implementation task 2}
- {Implementation task 3}
- [ ] Adicionar os atributos de teste de dados necessários: {list_of_testids}
- [ ] Ensaio de execução: `{test_execution_command}`
- [ ] ✅ Passagens de ensaio (fase verde)

**Esforço estimado:** BMADPROTECT029End hours

---

### Test: {test_name_2}

**File:** `{test_file_path}`

**Tasks to make this test pass:**

- [ ] {Implementation task 1}
- [ ] {Implementation task 2}
- [ ] {Implementation task 3}
- [ ] Add required data-testid attributes: {list_of_testids}
- [ ] Run test: `{test_execution_command}`
- [ ] ✅ Test passes (green phase)

**Estimated Effort:** {effort_estimate} hours

---

## Ensaios em execução

```bash

# Run all failing tests for this story
{test_command_all}

# Run specific test file
{test_command_specific_file}

# Run tests in headed mode (see browser)
{test_command_headed}

# Debug specific test
{test_command_debug}

# Run tests with coverage
{test_command_coverage}

```

---

## Red-Green-Refactor Workflow

### RED Phase (Complete) ✅

**TEA Agent Responsibilities:**

- ✅ All tests written and failing
- ✅ Fixtures and factories created with auto-cleanup
- ✅ Mock requirements documented
- ✅ data-testid requirements listed
- ✅ Implementation checklist created

**Verification:**

- All tests run and fail as expected
- Failure messages are clear and actionable
- Tests fail due to missing implementation, not test bugs

---

### Fase GREEN (Equipa DEV - Passos Próximos)

**Responsabilidades do agente DEV:**

1. **Pick one failing test** da lista de verificação implementation (começar com hig