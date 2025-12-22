# Configuração do Quadro de Teste - Lista de Verificação de Validação

Esta lista de verificação garante que o fluxo de trabalho do framework completa com sucesso e todos os resultados atendem aos padrões de qualidade.

---

## Prerequisites

Before starting the workflow:

- [ ] Project root contains valid `package.json`
- [ ] No existing modern E2E framework detected (`playwright.config.*`, `cypress.config.*`)
- [ ] Project type identifiable (React, Vue, Angular, Next.js, Node, etc.)
- [ ] Bundler identifiable (Vite, Webpack, Rollup, esbuild) or not applicable
- [ ] User has write permissions to create directories and files

---

## Passos do processo

### Passo 1: Verificação prévia de voo

- [ ] package.json lido e analisado com sucesso
- [ ] Tipo de projeto extraído corretamente
- [ ] Bundler identificado (ou marcado como N/A para projetos de infra-estrutura)
- [ ] Nenhum conflito de framework detectado
- [ ] Documentos de arquitectura localizados (se disponíveis)

### Passo 2: Seleção de Framework

- [ ] Framework auto-detecção lógica executada
- [ ] Escolha do quadro justificada (Playwright vs Cypress)
- [ ] Preferência-quadro respeitada (se explicitamente definida)
- [ ] Utilizador notificado da selecção e justificação do quadro

### Etapa 3: Estrutura de diretório

- [ ] `tests/` diretório raiz criado
- [ ] `tests/e2e/` diretório criado (ou estrutura preferida do usuário)
- [ ] `tests/support/` diretório criado (padrão crítico)
- [ ] `tests/support/fixtures/` diretório criado
- [ ] `tests/support/fixtures/factories/` diretório criado
- [ ] `tests/support/helpers/` directory criado
- [ ] `tests/support/page-objects/` directório criado (se aplicável)
- [ ] Todos os diretórios têm permissões corretas

**Nota**: A organização do ensaio é flexível (e2e/, api/, integration/). A pasta **suporte/** é o padrão chave.

### Passo 4: Ficheiros de Configuração

- [ ] Arquivo de configuração de framework criado (`playwright.config.ts` ou `cypress.config.ts`)
- [ ] Arquivo de configuração usa TypeScript (se `use_typescript: true`)
- [ ] Tempo limite configurado corretamente (ação: 15s, navegação: 30s, teste: 60s)
- [ ] URL base configurado com recurso à variável de ambiente
- [ ] Trace/screenshot/vídeo definido para reter-em-falha
- [ ] Múltiplos repórteres configurados (HTML + JUnit + console)
- [ ] Execução paralela habilitada
- [ ] Configurações específicas do CI configuradas (retornos, trabalhadores)
- [ ] Arquivo de configuração é sintáticamente válido (sem erros de compilação)

### Passo 5: Configuração do Ambiente

- [ ] `.env.example` criado na raiz do projeto
- [ ] `TEST_ENV` variável definida
- [ ] `BASE_URL` variável definida com padrão
- [ ] `API_URL` variável definida (se aplicável)
- [ ] Variáveis de autenticação definidas (se aplicável)
- [ ] Variáveis do indicador de características definidas (se aplicável)
- [ ] `.nvmrc` criado com a versão apropriada do Nó

### Passo 6: Arquitetura de fixação

- [ ] `tests/support/fixtures/index.ts` criado
- [ ] Suporte de base estendido de Playwright/Cypress
- [ ] Definições de tipo para os acessórios criados
- [ ] mergeTestes padrão implementado (se múltiplos dispositivos)
- [ ] Lógica de limpeza automática incluída nos acessórios
- A arquitetura de fixação segue padrões de base de conhecimento

### Passo 7: Fábricas de dados

- [ ] Pelo menos uma fábrica criada (por exemplo, UserFactory)
- [ ] Fábricas usam @faker-js/faker para dados realistas
- [ ] As fábricas rastreiam entidades criadas (para limpeza)
- [ ] Fábricas aplicam o método `cleanup()`
- [ ] Fábricas se integram com acessórios
- As fábricas seguem padrões de base de conhecimento.

### Etapa 8: Testes de amostras

- [ ] Arquivo de teste de exemplo criado (`tests/e2e/example.spec.ts`)
- [ ] Teste usa arquitetura de dispositivos
- [ ] Teste demonstra a utilização da fábrica de dados
- [ ] O teste utiliza uma estratégia de selecção adequada (dados-teste)
- [ ] O teste segue a estrutura Given-When-Then
- [ ] O teste inclui afirmações adequadas
- [ ] Intercepção da rede demonstrada (se aplicável)

### Passo 9: Utilitários de Ajuda

- [ ] API helper criado (se o teste API necessário)
- [ ] Ajudador de rede criado (se necessário zombar da rede)
- [ ] Auth helper criado (se a autenticação necessária)
- [ ] Os ajudantes seguem padrões funcionais
- [ ] Os ajudantes têm o tratamento adequado de erros

### Passo 10: Documentação

- [ ] `tests/README.md` criado
- [ ] Instruções de configuração incluídas
- [ ] Secção de ensaios de execução incluída
- [ ] seção visão geral da arquitetura incluído
- [ ] Seção de melhores práticas incluídas
- [ ] Secção de integração da IC incluída
- [ ] Referências à base de conhecimentos incluídas
- [ ] Seção de solução de problemas incluída

### Etapa 11: Package.json Atualizações

- [ ] Script de teste mínimo adicionado ao package.json: `test:e2e`
- [ ] A dependência do framework de teste foi adicionada (se ainda não estiver presente)
- [ ] Definições de tipo adicionadas (se TypeScript)
- [ ] Os usuários podem estender com scripts adicionais conforme necessário

---

## Validação de Saída

### Validação de Configuração

- [ ] O arquivo de configuração carrega sem erros
- [ ] Arquivo de configuração passa linting (se linter configurado)
- [ ] Arquivo de configuração usa sintaxe correta para o framework escolhido
- [ ] Todos os caminhos na configuração resolvem corretamente
- [ ] Os diretórios de saída do repórter existem ou são criados na execução do teste

### Validação da Execução de Teste

- [ ] O teste de amostra é executado com sucesso
- [ ] Execução de teste produz expec