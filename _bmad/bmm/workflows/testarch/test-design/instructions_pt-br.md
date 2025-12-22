<!-- Powered by BMAD-CORE™ -->

# Desenho do ensaio e avaliação dos riscos

**ID do fluxo de trabalho**: `_bmad/bmm/testarch/test-design`
**Versão**: 4.0 (BMad v6)

---

## Overview

Plans comprehensive test coverage strategy with risk assessment, priority classification, and execution ordering. This workflow operates in **two modes**:

- **System-Level Mode (Phase 3)**: Testability review of architecture before solutioning gate check
- **Epic-Level Mode (Phase 4)**: Per-epic test planning with risk assessment (current behavior)

The workflow auto-detects which mode to use based on project phase.

---

## Pré-voo: Detectar o Modo e o Contexto de Carga

**Crítico:** Determinar o modo antes de prosseguir.

### Detecção do modo

1. **Verificar sprint-status.yaml**
- Se o `{output_folder}/bmm-sprint-status.yaml` existir → **Modo de Nível Epico** (Fase 4)
- Se NÃO existe → Verificar o estado do fluxo de trabalho

2. **Verificar workflow-status.yaml**
- Leia `{output_folder}/bmm-workflow-status.yaml`
- Se `implementation-readiness: required` ou `implementation-readiness: recommended` → **Modo de nível do sistema** (Fase 3)
- Caso contrário → **Modo Epic-Level** (Fase 4 sem sprint status ainda)

3. **Requisitos específicos do modelo**

**Modo de nível do sistema (Fase 3 - Revisão da testabilidade):**
- ✅ Existe um documento de arquitectura (architecture.md ou tech-spec)
- ✅ O PRD existe com requisitos funcionais e não funcionais
- ✅ Épicos documentados (epics.md)
- ⚠; Saída: `{output_folder}/test-design-system.md`

**Modo de nível épico (Fase 4 - Planning por nível épico):**
- ✅ Marcação da história com critérios de aceitação disponíveis
- ✅ PRD ou documentação épica existe para o contexto
- ✅ Documentos de arquitectura disponíveis (opcional mas recomendado)
- ✅ Os requisitos são claros e testáveis
- ⚠' Saída: `{output_folder}/test-design-epic-{epic_num}.md`

**Condição de hált:** Se o modo não puder ser determinado ou arquivos necessários faltando, HALT e notificar o usuário com pré-requisitos faltando.

---

## Passo 1: Carregar o Contexto (Mode-Aware)

**Carregamento Específico do Modo:**

### Modo Nível do Sistema (Fase 3)

1. **Leia a documentação da arquitetura**
- Carregar architecture.md ou tech-spec (REQUIRED)
- Carregar PRD.md para requisitos funcionais e não funcionais
- Carregar epics.md para escopo de recursos
- Identificar decisões de pilha de tecnologia (frameworks, bases de dados, metas de implantação)
- Nota pontos de integração e dependências do sistema externo
- Extrair requisitos NFR (SLOs de desempenho, requisitos de segurança, etc.)

2. **Verificar Playwright usa bandeira**

Leia BMADPROTECT020End e verifique BMADPROTECT019End.

Se true, note que `@seontechnologies/playwright-utils` fornece utilitários para teste implementation. Referência na concepção do ensaio, se for caso disso.

3. **Carregar Fragmentos de Base de Conhecimento (Sistema-Nível)**

**Crítico:** Consulte `{project-root}/_bmad/bmm/testarch/tea-index.csv`ER à carga:
- `nfr-criteria.md` - Método de validação NFR (segurança, desempenho, confiabilidade, manutenção)
- `test-levels-framework.md` - Guia de estratégia de níveis de teste
- `risk-governance.md` - Identificação do risco de testabilidade
- `test-quality.md` - Normas de qualidade e definição de feito

4. **Analisar configuração de teste existente (se brownfield)**
- Procurar diretórios de testes existentes
- Identificar o quadro de ensaio actual (se existir)
- Preocupações de testabilidade no banco de códigos existente

### Modo de Nível Épico (Fase 4)

1. **Leia a documentação dos requisitos**
- Carregar PRD.md para exigências de produtos de alto nível
- Leia epics.md ou épico específico para escopo de recursos
- Leia a marcação da história para critérios de aceitação detalhados
- Identificar todos os requisitos testáveis

2. **Contexto de Arquitetura de Carga**
- Leia architecture.md para o projeto do sistema
- Leia o tech-spec para implementation detalhes
- Leia test-design-system.md (se existir a partir da Fase 3)
- Identificar restrições técnicas e dependências
- Nota pontos de integração e sistemas externos

3. **Análise existente cobertura de teste**
- Pesquisa de arquivos de teste existentes em `{test_dir}`
- Identificar lacunas de cobertura
- Note áreas com testes insuficientes
- Verifique se há testes flácidos ou ultrapassados

4. **Fragmentos de Base de Conhecimento de Carga (Nível Epic)**

**Crítico:** Consulte `{project-root}/_bmad/bmm/testarch/tea-index.csv`ER à carga:
- `risk-governance.md` - Quadro de classificação de risco (6 categorias: TECH, SEC, PERF, DADOS, BUS, OPS), pontuação automatizada, motor de decisão de portão, rastreamento proprietário (625 linhas, 4 exemplos)
- `probability-impact.md` - Metodologia de pontuação de risco (probabilidade × matriz de impacto, classificação automatizada, reavaliação dinâmica, integração de portas, 604 linhas, 4 exemplos)
- `test-levels-framework.md` - Guia de seleção de nível de teste (E2E vs API vs Componente vs Unidade com matriz de decisão, características, quando usar cada, 467 linhas, 4 exemplos)
- `test-priorities-matrix.md` - Critérios de priorização P0-P3 (calculamento automático de prioridade, mapeamento baseado em risco, estratégia de marcação, orçamentos temporais, 389 linhas, 2 exemplos)

**Condição de sal (apenas nível épico):** Se os dados da história ou acc