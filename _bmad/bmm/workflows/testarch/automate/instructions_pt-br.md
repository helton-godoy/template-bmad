<!-- Powered by BMAD-CORE™ -->

# Expansão de Automação de Teste

**ID do fluxo de trabalho**: `_bmad/bmm/testarch/automate`
**Versão**: 4.0 (BMad v6)

---

## Overview

Expands test automation coverage by generating comprehensive test suites at appropriate levels (E2E, API, Component, Unit) with supporting infrastructure. This workflow operates in **dual mode**:

1. **BMad-Integrated Mode**: Works WITH BMad artifacts (story, tech-spec, PRD, test-design) to expand coverage after story implementation
2. **Standalone Mode**: Works WITHOUT BMad artifacts - analyzes existing codebase and generates tests independently

**Core Principle**: Generate prioritized, deterministic tests that avoid duplicate coverage and follow testing best practices.

---

## Requisitos de pré-voo

**Flexível:** Este fluxo de trabalho pode ser executado com pré-requisitos mínimos. Apenas HALT se a estrutura estiver completamente ausente.

### Obrigatória (sempre)

- ✅ Framework scaffolding configurado (correr `framework` workflow se faltar)
- ✅ Configuração do framework de teste disponível (playwright. config.ts ou cipreste.config.ts)

### Opcional (modo integrado no BMad)

- Marcação da história com critérios de aceitação (melhores metas de cobertura)
- Especificações técnicas ou PRD (fornece contexto arquitetônico)
- Documento de projecto de ensaio (fornece um contexto de risco/prioridade)

### Opcional (modo padrão)

- Código-fonte para analisar (feature implementation)
- Testes existentes (para análise de gap)

**Se o framework está faltando:** HALT com mensagem: "Framework andaimes necessários. Executar `bmad tea *framework` primeiro."

---

## Passo 1: Determinar o modo de execução e o contexto de carga

### Acções

1. **Detect Execution Mode**

Verifique se os artefatos BMad estão disponíveis:
- Se a variável `{story_file}` estiver definida → Modo Integrado BMad
- Se o `{target_feature}` ou o `{target_files}` conjunto → Modo independente
- Se nenhum dos dois set → Modo Auto-descobrir (scan codebase para recursos que necessitam de testes)

2. **Carregar os artefactos BMad (se disponíveis)**

**Modo Integrado no BMad:**
- Leia a história de `{story_file}`
- Critérios de aceitação dos extractos e requisitos técnicos
- Carregar tech-spec.md se `{use_tech_spec}` for true
- Carregar test-design.md se `{use_test_design}` for true
- Carregar PRD.md se `{use_prd}` for true
   - Note: Estes são **melhoramentos opcionais**, não requisitos difíceis

**Modo Standalone:**
- Saltar carregamento de artefatos BMad
- Prossiga diretamente para análise de código fonte

3. **Configuração do quadro de carga**
- Leia a configuração do framework de teste (playwright. config.ts ou cipreste.config.ts)
- Identificar a estrutura do diretório de teste de `{test_dir}`
- Verificar os padrões de teste existentes no `{test_dir}`
- Note capacidades de corredor de teste (execução paralela, acessórios, etc.)

4. **Analisar a cobertura de teste existente**

Se `{analyze_coverage}` for true:
- Procurar `{test_dir}` para arquivos de teste existentes
- Identificar características testadas vs características não testadas
- Mapa testes para arquivos de origem (gaps de cobertura)
- Verificar os padrões existentes e de fábrica

5. **Verificar Playwright utiliza bandeira**

Leia BMADPROTECT025End e verifique BMADPROTECT024End.

6. **Carregar Fragmentos de Base de Conhecimento**

**Crítico:** Consulte `{project-root}/_bmad/bmm/testarch/tea-index.csv`ER à carga:

**Padrões de teste de core (carga sempre):**
- `test-levels-framework.md` - Seleção de nível de teste (E2E vs API vs Componente vs Unidade com matriz de decisão, 467 linhas, 4 exemplos)
- `test-priorities-matrix.md` - Classificação prioritária (P0-P3 com pontuação automatizada, mapeamento de risco, 389 linhas, 2 exemplos)
- `data-factories.md` - Padrões de fábrica com falsificador (sobrescritos, fábricas aninhadas, semeadura API, 498 linhas, 5 exemplos)
- `selective-testing.md` - Estratégias de execução de testes orientadas (baseadas em etiquetas, filtros de especificações, regras de promoção baseadas em diff, 727 linhas, 4 exemplos)
- `ci-burn-in.md` - Padrões de detecção de testes flácidos (10-iterações de queima, estilhaçamento, execução seletiva, 678 linhas, 4 exemplos)
- `test-quality.md` - Princípios de concepção de ensaios (determinados, isolados, afirmações explícitas, limites comprimento/tempo, 658 linhas, 5 exemplos)

**Se `config.tea_use_playwright_utils: true` (Playwright utiliza a integração - Todos os utilitários):**
- `overview.md` - Instalação de utils do dramaturgo, princípios de projeto, padrões de fixação
- `api-request.md` - Cliente HTTP digitado com validação de esquema
- `network-recorder.md` - HAR registro / playback para testes offline
- `auth-session.md` - Persistência do token e suporte multi-usuário
- `intercept-network-call.md` - Espião de rede com processamento automático JSON
- `recurse.md` - Pesquisa ao estilo Cypress para condições async
- `log.md` - Registo integrado por relatórios de dramaturgos
- `file-utils.md` - leitura e validação CSV/XLSX/PDF/ZIP
- `burn-in.md` - Seleção de teste inteligente (relevante para geração de teste CI)
- `network-error-monitor.md` - Detecção automática de erros HTTP
- `fixtures-composition.md` - mergeTestes padrões de composição

**Se `config.tea_use_playwright_utils: false` (Padrões Tradicionais):**
- `fixture-architecture.md` - Teste padrões de fixação (functi puro