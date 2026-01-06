# Checklist ATDD - Épico {epic_num}, História {story_num}: {story_title}

**Data:** {date}
**Autor:** {user_name}
**Nível de Teste Primário:** {primary_level}

---

## Resumo da História

{Resumo breve de 2-3 frases da história de usuário}

**Como um** {user_role}
**Eu quero** {feature_description}
**Para que** {business_value}

---

## Critérios de Aceite

{Listar todos os critérios de aceite testáveis da história}

1. {Critério de aceite 1}
2. {Critério de aceite 2}
3. {Critério de aceite 3}

---

## Testes com Falha Criados (Fase VERMELHA)

### Testes E2E ({e2e_test_count} testes)

**Arquivo:** `{e2e_test_file_path}` ({line_count} linhas)

{Listar cada teste E2E com seu status atual e razão de falha esperada}

- ✅ **Teste:** {test_name}
  - **Status:** VERMELHO - {failure_reason}
  - **Verifica:** {what_this_test_validates}

### Testes de API ({api_test_count} testes)

**Arquivo:** `{api_test_file_path}` ({line_count} linhas)

{Listar cada teste de API com seu status atual e razão de falha esperada}

- ✅ **Teste:** {test_name}
  - **Status:** VERMELHO - {failure_reason}
  - **Verifica:** {what_this_test_validates}

### Testes de Componente ({component_test_count} testes)

**Arquivo:** `{component_test_file_path}` ({line_count} linhas)

{Listar cada teste de componente com seu status atual e razão de falha esperada}

- ✅ **Teste:** {test_name}
  - **Status:** VERMELHO - {failure_reason}
  - **Verifica:** {what_this_test_validates}

---

## Fábricas de Dados Criadas

{Listar todos os arquivos de fábrica de dados criados com suas exportações}

### Fábrica de {Entity}

**Arquivo:** `tests/support/factories/{entity}.factory.ts`

**Exportações:**

- `create{Entity}(overrides?)` - Criar entidade única com substituições opcionais
- `create{Entity}s(count)` - Criar array de entidades

**Exemplo de Uso:**

```typescript
const user = createUser({ email: 'especifico@exemplo.com' });
const users = createUsers(5); // Gerar 5 usuários aleatórios
```

---

## Fixtures Criadas

{Listar todos os arquivos de fixture de teste criados com seus nomes e descrições}

### Fixtures de {Feature}

**Arquivo:** `tests/support/fixtures/{feature}.fixture.ts`

**Fixtures:**

- `{fixtureName}` - {description_of_what_fixture_provides}
  - **Configuração:** {what_setup_does}
  - **Fornece:** {what_test_receives}
  - **Limpeza:** {what_cleanup_does}

**Exemplo de Uso:**

```typescript
import { test } from './fixtures/{feature}.fixture';

test('deve fazer algo', async ({ {fixtureName} }) => {
  // {fixtureName} está pronto para uso com auto-limpeza
});
```

---

## Requisitos de Mock

{Documentar serviços externos que precisam de mock e seus requisitos}

### Mock de {Service Name}

**Endpoint:** `{HTTP_METHOD} {endpoint_url}`

**Resposta de Sucesso:**

```json
{
  {success_response_example}
}
```

**Resposta de Falha:**

```json
{
  {failure_response_example}
}
```

**Notas:** {any_special_mock_requirements}

---

## Atributos data-testid Necessários

{Listar todos os atributos data-testid necessários na implementação da UI para estabilidade do teste}

### {Page or Component Name}

- `{data-testid-name}` - {description_of_element}
- `{data-testid-name}` - {description_of_element}

**Exemplo de Implementação:**

```tsx
<button data-testid="login-button">Entrar</button>
<input data-testid="email-input" type="email" />
<div data-testid="error-message">{errorText}</div>
```

---

## Checklist de Implementação

{Mapear cada teste com falha para tarefas concretas de implementação que farão ele passar}

### Teste: {test_name_1}

**Arquivo:** `{test_file_path}`

**Tarefas para fazer este teste passar:**

- [ ] {Tarefa de implementação 1}
- [ ] {Tarefa de implementação 2}
- [ ] {Tarefa de implementação 3}
- [ ] Adicionar atributos data-testid necessários: {list_of_testids}
- [ ] Rodar teste: `{test_execution_command}`
- [ ] ✅ Teste passa (fase verde)

**Esforço Estimado:** {effort_estimate} horas

---

### Teste: {test_name_2}

**Arquivo:** `{test_file_path}`

**Tarefas para fazer este teste passar:**

- [ ] {Tarefa de implementação 1}
- [ ] {Tarefa de implementação 2}
- [ ] {Tarefa de implementação 3}
- [ ] Adicionar atributos data-testid necessários: {list_of_testids}
- [ ] Rodar teste: `{test_execution_command}`
- [ ] ✅ Teste passa (fase verde)

**Esforço Estimado:** {effort_estimate} horas

---

## Rodando Testes

```bash
# Rodar todos os testes com falha para esta história
{test_command_all}

# Rodar arquivo de teste específico
{test_command_specific_file}

# Rodar testes em modo headed (ver navegador)
{test_command_headed}

# Depurar teste específico
{test_command_debug}

# Rodar testes com cobertura
{test_command_coverage}
```

---

## Fluxo de Trabalho Red-Green-Refactor

### Fase VERMELHA (Completa) ✅

**Responsabilidades do Agente TEA:**

- ✅ Todos os testes escritos e falhando
- ✅ Fixtures e fábricas criadas com auto-limpeza
- ✅ Requisitos de mock documentados
- ✅ Requisitos de data-testid listados
- ✅ Checklist de implementação criado

**Verificação:**

- Todos os testes rodam e falham como esperado
- Mensagens de falha são claras e acionáveis
- Testes falham devido à implementação ausente, não bugs de teste

---

### Fase VERDE (Equipe DEV - Próximos Passos)

**Responsabilidades do Agente DEV:**

1. **Escolher um teste com falha** do checklist de implementação (começar com maior prioridade)
2. **Ler o teste** para entender o comportamento esperado
3. **Implementar código mínimo** para fazer aquele teste específico passar
4. **Rodar o teste** para verificar que agora passa (verde)
5. **Marcar a tarefa** no checklist de implementação
6. **Mover para o próximo teste** e repetir

**Princípios Chave:**

- Um teste de cada vez (não tente consertar tudo de uma vez)
- Implementação mínima (não super-engenhar)
- Rodar testes frequentemente (feedback imediato)
- Usar checklist de implementação como roteiro

**Rastreamento de Progresso:**

- Marcar tarefas conforme completar
- Compartilhar progresso no standup diário
- Marcar história como EM PROGRESSO em `bmm-workflow-status.md`

---

### Fase REFATORAR (Equipe DEV - Após Todos os Testes Passarem)

**Responsabilidades do Agente DEV:**

1. **Verificar que todos os testes passam** (fase verde completa)
2. **Revisar código para qualidade** (legibilidade, manutenibilidade, desempenho)
3. **Extrair duplicações** (princípio DRY)
4. **Otimizar desempenho** (se necessário)
5. **Garantir que testes ainda passam** após cada refatoração
6. **Atualizar documentação** (se contratos de API mudarem)

**Princípios Chave:**

- Testes fornecem rede de segurança (refatorar com confiança)
- Fazer pequenas refatorações (mais fácil de depurar se testes falharem)
- Rodar testes após cada mudança
- Não mudar comportamento do teste (apenas implementação)

**Conclusão:**

- Todos os testes passam
- Qualidade do código atende aos padrões da equipe
- Sem duplicações ou code smells
- Pronto para revisão de código e aprovação da história

---

## Próximos Passos

1. **Revisar este checklist** com a equipe no standup ou planejamento
2. **Rodar testes com falha** para confirmar fase VERMELHA: `{test_command_all}`
3. **Começar implementação** usando checklist de implementação como guia
4. **Trabalhar um teste de cada vez** (vermelho → verde para cada)
5. **Compartilhar progresso** no standup diário
6. **Quando todos os testes passarem**, refatorar código para qualidade
7. **Quando refatoração completa**, atualizar manualmente status da história para 'done' em sprint-status.yaml

---

## Referências da Base de Conhecimento Aplicadas

Este fluxo de trabalho ATDD consultou os seguintes fragmentos de conhecimento:

- **fixture-architecture.md** - Padrões de fixture de teste com configuração/desmontagem e auto-limpeza usando `test.extend()` do Playwright
- **data-factories.md** - Padrões de fábrica usando `@faker-js/faker` para geração de dados de teste aleatórios com suporte a substituições
- **component-tdd.md** - Estratégias de teste de componente usando Teste de Componente Playwright
- **network-first.md** - Padrões de interceptação de rota (interceptar ANTES da navegação para prevenir condições de corrida)
- **test-quality.md** - Princípios de design de teste (Dado-Quando-Então, uma afirmação por teste, determinismo, isolamento)
- **test-levels-framework.md** - Framework de seleção de nível de teste (E2E vs API vs Componente vs Unidade)

Veja `tea-index.csv` para mapeamento completo de fragmentos de conhecimento.

---

## Evidência de Execução de Teste

### Execução Inicial de Teste (Verificação de Fase VERMELHA)

**Comando:** `{test_command_all}`

**Resultados:**

```
{paste_test_run_output_showing_all_tests_failing}
```

**Resumo:**

- Total de testes: {total_test_count}
- Passando: 0 (esperado)
- Falhando: {total_test_count} (esperado)
- Status: ✅ Fase VERMELHA verificada

**Mensagens de Falha Esperadas:**
{list_expected_failure_messages_for_each_test}

---

## Notas

{Quaisquer notas adicionais, contexto ou considerações especiais para esta história}

- {Nota 1}
- {Nota 2}
- {Nota 3}

---

## Contato

**Perguntas ou Problemas?**

- Pergunte no standup da equipe
- Marque @{tea_agent_username} no Slack/Discord
- Consulte `./bmm/docs/tea-README.md` para documentação do fluxo de trabalho
- Consulte `./bmm/testarch/knowledge` para melhores práticas de teste

---

**Gerado pelo Agente BMad TEA** - {date}
