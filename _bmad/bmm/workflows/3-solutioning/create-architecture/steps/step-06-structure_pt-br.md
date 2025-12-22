# Passo 6: Estrutura e Limites do Projeto

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

- 🛑 NUNCA gerar conteúdo sem entrada do usuário

- 📖 CRITICAL: SEMPRE leia o arquivo de passo completo antes de tomar qualquer ação - compreensão parcial leva a decisões incompletas
- 🔄 CRITICAL: Ao carregar o próximo passo com 'C', certifique-se de que todo o arquivo seja lido e compreendido antes de prosseguir
- ✅ Sempre trate isso como uma descoberta colaborativa entre pares arquitetônicos
És um facilitador, não um gerador de conteúdo.
- 💬 FOCUS na definição de estrutura completa do projecto e limites claros
- 🗺
A velocidade de desenvolvimento da IA mudou fundamentalmente

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Mostre sua análise antes de tomar qualquer ação
- 🗺 Criar uma árvore de projecto completa, não genérica
- ⚠; Apresentar menu A/P/C após gerar estrutura de projeto
- 💾 APENAS salve quando o usuário escolher C (Continuar)
- 📖 Actualizar a matéria frontal `stepsCompleted: [1, 2, 3, 4, 5, 6]` antes de carregar o próximo passo
- 🚫 PROIBIDA a carregar o próximo passo até que o C seja seleccionado

## COLABORAÇÃO MENUS (A/P/C):

Esta etapa irá gerar conteúdo e opções presentes:

- **A (Elicitação Avançada)**: Use protocolos de descoberta para explorar abordagens inovadoras de organização de projetos
- **P (Modo de Festa)**: Traz múltiplas perspectivas para avaliar trocas de estrutura de projecto
- **C (Continua)**: Salve a estrutura do projeto e prossiga para validação

## INTEGRAÇÃO PROTOCOLO:

- Quando 'A' seleccionado: Executar {project-root}/_bmad/core/tasks/advanced-elicitation.xml
- Quando 'P' seleccionado: Executar {project-root}/_bmad/core/workflows/party-mode/workflow.md
- PROTOCOLOS retornam sempre para exibir o menu A/P/C deste passo após o A ou P terem completado
- O usuário aceita/rejeita alterações de protocolo antes de prosseguir

## CONTEXTO MONTANTES:

- Todas as decisões arquitectónicas anteriores estão concluídas.
- Implementation padrões e regras de consistência são definidos
- Foco na estrutura física do projeto e limites de componentes
- Mapa de requisitos para arquivos e diretórios específicos

A sua tarefa:

Defina a estrutura completa do projeto e os limites arquitetônicos com base em todas as decisões tomadas, criando um guia implementation concreto para agentes de IA.

## SEQUÊNCIA DE ESTRUTURA DE PROJECTOS:

### 1. Analisar o Mapeamento dos Requisitos

Mapa dos requisitos do projeto para componentes arquitetônicos:

**De Epics (se disponível):**
"Épico: {{epic_name}} → Vive em {{module/directory/service}}"

- Histórias de usuários dentro do épico
- Dependências cruzadas
- Componentes compartilhados necessários

**Das categorias FR (se não houver épicos):**
"FR Categoria: {{fr_category_name}} → Vive em {{module/directory/service}}"

- Requisitos funcionais relacionados
- Funcionalidade compartilhada entre categorias
- Pontos de integração entre categorias

### 2. Defina a estrutura do diretório do projeto

Com base na pilha de tecnologia e padrões, crie a estrutura completa do projeto:

**Ficheiros de configuração de Root:**

- Arquivos de gerenciamento de pacotes (package.json, requirements.txt, etc.)
- Configuração de compilação e desenvolvimento
- Arquivos de configuração de ambiente
- Ficheiros CI/CD pipeline
- Arquivos de documentação

**Organização do Código Fonte:**

- Pontos de entrada da aplicação
- Estrutura de aplicação principal
- Organização de recursos/módulos
- Utilitários compartilhados e bibliotecas
- Arquivos de configuração e ambiente

**Organização de Teste:**

- Unidades de localização e estrutura de teste
- Organização de teste de integração
- Estrutura de teste de ponta a ponta
- Teste utilitários e acessórios

**Construir e distribuir:**

- Construir diretórios de saída
- Arquivos de distribuição
- Activos estáticos
- Construção de documentação

### 3. Definir limites de integração

Mapear como os componentes comunicam e onde existem limites:

**Fronteiras API:**

- Endpoints externos da API
- Fronteiras internas de serviço
- Limites de autenticação e autorização
- Limites da camada de acesso aos dados

**Fronteiras componentes:**

- Padrões de comunicação de componentes Frontend
- Fronteiras de gestão do Estado
- Padrões de comunicação de serviço
- Pontos de integração orientados para o evento

**Fronteiras de dados:**

- Limites do esquema de banco de dados
- Padrões de acesso aos dados
- Limites de cache
- Pontos de integração de dados externos

### 4. Criar árvore de projeto completa

Gere uma estrutura abrangente de diretórios mostrando todos os arquivos e diretórios:

**Exemplos de estrutura específica da tecnologia:**

**Next.js Full-Stack:**

```
project-name/
├── README.md
├── package.json
├── next.config.js
├── tailwind.config.js
├── tsconfig.json
├── .env.local
├── .env.example
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── app/
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/
│   │   ├── ui/
│   │   ├── forms/
│   │   └── features/
│   ├── lib/
│   │   ├── db.ts
│   │   ├── auth.ts
│   │   └── utils.ts
│   ├── types/
│   └── middleware.ts
├── prisma/
│   ├── schema.prisma
│   └── migrations/
├── tests/
│   ├── __mocks__/
│   ├── components/
│   └── e2e/
└── public/
    └── assets/

```

**Infra-estrutura API (NestJS):**

«``
nome do projeto/
package.json
nest-cli.jso