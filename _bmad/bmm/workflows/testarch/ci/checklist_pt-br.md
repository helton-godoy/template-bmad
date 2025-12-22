# Configuração do Pipeline CI/CD - Lista de Verificação de Validação

## Pré-requisitos

- [ ] O repositório Git inicializado (o `.git/` existe)
- [ ] Git remoto configurado (`git remote -v` mostra origem)
- [ ] Estrutura de teste configurada (`playwright.config._` ou `cypress.config._`)
- Passagem de testes locais (`npm run test:e2e` sucede)
- [ ] A equipe concorda com a plataforma CI
- [ ] Acesso às configurações da plataforma CI (se atualizar)

## Passos do processo

### Passo 1: Verificação prévia de voo

- [ ] O repositório Git foi validado
- [ ] Configuração de framework detectada
- [ ] Execução local de teste bem sucedida
- [ ] Plataforma CI detectada ou seleccionada
- [ ] Versão Nó identificada (. nvmrc ou padrão)
- [ ] Nenhum problema de bloqueio encontrado

### Passo 2: Configuração do Pipeline CI

- [ ] Arquivo de configuração CI criado (`.github/workflows/test.yml` ou `.gitlab-ci.yml`)
- [ ] O arquivo é sintáticamente válido (sem erros YAML)
- [ ] Comandos corretos de framework configurados
- [ ] A versão do nó corresponde ao projecto
- [ ] Corrigir os caminhos das pastas de teste

### Passo 3: Paralelo de corte

- [ ] Estratégia de matriz configurada (4 fragmentos padrão)
- [ ] Shard sintaxe correta para framework
- Conjunto rápido de falha para false
- [ ] Contagem de shard apropriada para o tamanho do conjunto de testes

### Passo 4: Burn-In Loop

- [ ] Burn-in trabalho criado
- 10 iterações configuradas
- [ ] Saída adequada na falha (`|| exit 1`)
- [ ] Corre em gatilhos apropriados (PR, cron)
- Artefactos de falha carregados.

### Passo 5: Configuração do cache

- [ ] Cache de dependência configurado (npm/yarn)
- [ ] Chave de cache usa hash de arquivo de bloqueio
- [ ] Cache de navegador configurado (Playwright/Cypress)
- [ ] Restaurar-chaves definidas para retrocesso
- [ ] Caminhos de cache corretos para a plataforma

### Passo 6: Coleção de artefatos

- [ ] Artefactos carregados apenas em falhas
- [ ] Caminhos de artefacto correctos (resultados-teste/, vestígios/, etc.)
- [ ] dias de retenção definidos (30 padrão)
- Nomes de artefactos únicos por caco
- [ ] Nenhum dado sensível em artefatos

### Passo 7: Repetir a Lógica

- [ ] Repetir a ação/estratégia configurada
- Tentativas máximas: 2-3
- [ ] Tempo- limite adequado (30 min)
- [ ] Tente novamente apenas em erros transitórios

### Passo 8: Programas de Ajuda

- [ ] `scripts/test-changed.sh` criado
- [ ] `scripts/ci-local.sh` criado
- [ ] `scripts/burn-in.sh` criado (opcional)
- [ ] Scripts são executáveis (`chmod +x`)
- [ ] Scripts usam comandos de teste corretos
- [ ] Shebang presente (`#!/bin/bash`)

### Passo 9: Documentação

- [ ] `docs/ci.md` criado com guia de tubulação
- [ ] `docs/ci-secrets-checklist.md` criado
- [ ] Segredos necessários documentados
- [ ] Instruções de configuração limpas
- [ ] Seção de solução de problemas incluída
- [ ] URLs do distintivo fornecidos (opcional)

## Validação de Saída

### Validação de Configuração

- [ ] O ficheiro CI carrega sem erros
- [ ] Todos os caminhos resolvem corretamente
- [ ] Não existem valores codificados (use env vars)
- [ ] Gatilhos configurados (empurrar, puxar, solicitar, agendar)
- [ ] Sintaxe específica da plataforma correta

### Validação de Execução

- [ ] Primeira execução CI accionado (empurrar para o comando)
- [ ] Pipeline começa sem erros
- [ ] Todas as tarefas aparecem no painel CI
O cache funciona.
- [ ] Testes executados em paralelo
- [ ] Artefactos recolhidos por falha

### Validação de desempenho

- Estágio do revestimento: < 2 minutos
- [ ] Fase de ensaio (por caco): < 10 minutos
- Estágio de queimadura: < 30 minutos
- Oleoduto total: < 45 minutos
- [ ] Cache reduz o tempo de instalação em 2-5 minutos

## Controlos de qualidade

### Cumprimento das melhores práticas

- [ ] Burn-in laço segue padrões de produção
- [ ] Corte paralelo configurado optimamente
- Colecção de artefactos só com falhas
- [ ] Testes seletivos ativados (opcional)
- [ ] A lógica de repetição lida apenas com falhas transitórias
- [ ] Nenhum segredo nos arquivos de configuração

### Alinhamento da base de conhecimento

- O padrão de gravação corresponde ao `ci-burn-in.md`
- [ ] Testes seletivos correspondem `selective-testing.md`
- [ ] Colecção de artefactos corresponde `visual-debugging.md`
- [ ] A qualidade do teste corresponde à `test-quality.md`

### Controlos de segurança

- [ ] Sem credenciais na configuração do CI
- Os segredos usam a gestão secreta da plataforma.
- [ ] Variáveis de ambiente para dados sensíveis
- [ ] Retenção de artefactos apropriada (não muito longa)
- [ ] Sem saída de depuração expondo segredos

## Pontos de Integração

### Integração do Ficheiro de Estado

- [ ] `bmm-workflow-status.md` existe
- [ ] Configuração do CI logada na secção Qualidade & Teste de Progresso
- [ ] Estado actualizado com data de conclusão
- Plataforma e configuração anotadas

### Integração com a Base de Conhecimento

- [ ] Fragmentos de conhecimento relevantes carregados
- [ ] Padrões aplicados a partir de base de conhecimento
- [ ] Documentação referencia base de conhecimento
- [ ] Referências de base de conhecimento em README

### Dependências do fluxo de trabalho

- [ ] `framework` fluxo de trabalho concluído primeiro
- [ ] Pode prosseguir para o fluxo de trabalho `atdd` após a configuração do CI
- [ ] Pode prosseguir para o fluxo de trabalho `automate`
- [ ] CI integra-se com o fluxo de trabalho `gate`

## Critérios de conclusão

**Todos devem ser true:**

- [ ] Todos os pré-requisitos cumpridos
- [ ] Todas as etapas do processo concluídas
- [ ] Todas as validações de saída passaram
- [ ] Todos os controlos de qualidade aprovados
- [ ] Todos os pontos de integração verificados
- O primeiro CI foi bem sucedido.
- Performance ta