# Fluxos de Trabalho de Solução BMM (Fase 3)

## Visão Geral

Fluxos de trabalho da Fase 3 (Solução) traduzem **o que** construir (do Planejamento) em **como** construir (design técnico). Esta fase previne conflitos de agentes em projetos multi-épico ao documentar decisões arquiteturais antes da implementação começar.

**Princípio chave:** Torne decisões técnicas explícitas e documentadas para que todos os agentes implementem consistentemente. Previna um agente de escolher REST enquanto outro escolhe GraphQL.

**Obrigatório para:** Método BMad (projetos complexos), Método Enterprise

**Opcional para:** Método BMad (projetos simples), Quick Flow (pule inteiramente)

---

## Visão Geral do Fluxo de Trabalho de Solução Fase 3

A Solução Fase 3 tem caminhos diferentes baseados na trilha de planejamento selecionada:

### Caminho Quick Flow

- Do Planejamento: tech-spec completo
- Ação: Pular Fase 3 inteiramente
- Próximo: Fase 4 (Implementação)

### Caminho Método BMad & Enterprise

- Do Planejamento: PRD com RFs/RNFs completo
- Opcional: create-ux-design (se UX é crítica)
- Obrigatório: architecture - Design de sistema com ADRs
- Obrigatório: create-epics-and-stories - Quebrar requisitos em estórias implementáveis
- Obrigatório: implementation-readiness - Validação de gate check
- Adições Enterprise: security-architecture e devops-strategy opcionais (fluxos futuros)

### Resultados do Gate Check

- **APROVADO** - Todos critérios atendidos, proceda para Fase 4
- **PREOCUPAÇÕES** - Lacunas menores identificadas, proceda com cautela
- **REPROVADO** - Problemas críticos, deve resolver antes da Fase 4

---

## Referência Rápida

| Fluxo de Trabalho            | Agente      | Trilha                  | Propósito                                      |
| ---------------------------- | ----------- | ----------------------- | ---------------------------------------------- |
| **create-ux-design**         | Designer UX | Método BMad, Enterprise | Design UX opcional (após PRD, antes arch)      |
| **architecture**             | Arquiteto   | Método BMad, Enterprise | Arquitetura técnica e decisões de design       |
| **create-epics-and-stories** | PM          | Método BMad, Enterprise | Quebrar RFs/RNFs em épicos após arquitetura    |
| **implementation-readiness** | Arquiteto   | BMad Complex, Enterprise| Validar completude de planejamento/solução     |

**Quando Pular Solução:**

- **Quick Flow:** Mudanças simples não precisam de arquitetura → Pule para Fase 4

**Quando Solução é Obrigatória:**

- **Método BMad:** Projetos multi-épico precisam de arquitetura para prevenir conflitos
- **Enterprise:** Mesmo que Método BMad, mais fluxos estendidos opcionais (arquitetura de teste, segurança, estratégia devops) adicionados APÓS arquitetura mas ANTES de gate check

---

## Por Que Solução Importa

### O Problema Sem Solução

```
Agente 1 implementa Épico 1 usando REST API
Agente 2 implementa Épico 2 usando GraphQL
Resultado: Design de API inconsistente, pesadelo de integração
```

### A Solução Com Solução

```
Fluxo architecture decide: "Usar GraphQL para todas as APIs"
Todos os agentes seguem decisões de arquitetura
Resultado: Implementação consistente, sem conflitos
```

### Solução vs Planejamento

| Aspecto  | Planejamento (Fase 2)   | Solução (Fase 3)                 |
| -------- | ----------------------- | -------------------------------- |
| Questão  | O que e Por quê?        | Como? Então Quais unidades de trabalho? |
| Saída    | RFs/RNFs (Requisitos)   | Arquitetura + Épicos/Estórias    |
| Agente   | PM                      | Arquiteto → PM                   |
| Público  | Stakeholders            | Desenvolvedores                  |
| Documento| PRD (RFs/RNFs)          | Arquitetura + Arquivos de Épico  |
| Nível    | Lógica de Negócio       | Design Técnico + Quebra de Trabalho |

---

## Descrições de Fluxo de Trabalho

### architecture

**Propósito:** Tornar decisões técnicas explícitas para prevenir conflitos de agentes. Produz documento de arquitetura focado em decisão otimizado para consistência de IA.

**Agente:** Arquiteto

**Quando Usar:**

- Projetos multi-épico (BMad Complex, Enterprise)
- Preocupações técnicas transversais
- Múltiplos agentes implementando partes diferentes
- Complexidade de integração existe
- Escolhas de tecnologia precisam de alinhamento

**Quando Pular:**

- Quick Flow (mudanças simples)
- BMad Method Simple com stack tecnológico direto
- Épico único com abordagem técnica clara

**Abordagem de Conversação Adaptativa:**

Isso NÃO é um preenchimento de template. O fluxo de arquitetura:

1. **Descobre** necessidades técnicas através de conversa
2. **Propõe** opções arquiteturais com trade-offs
3. **Documenta** decisões que previnem conflitos de agentes
4. **Foca** em pontos de decisão, não documentação exaustiva

**Saídas Chave:**

**architecture.md** contendo:

1. **Visão Geral de Arquitetura** - Contexto do sistema, princípios, estilo
2. **Arquitetura de Sistema** - Diagrama alto nível, interações de componente, padrões de comunicação
3. **Arquitetura de Dados** - Design de banco, gestão de estado, cache, fluxo de dados
4. **Arquitetura de API** - Estilo de API (REST/GraphQL/gRPC), auth, versionamento, tratamento de erro
5. **Arquitetura Frontend** (se aplicável) - Framework, gestão de estado, arquitetura de componente, roteamento
6. **Arquitetura de Integração** - Integrações third-party, fila de mensagem, padrões event-driven
7. **Arquitetura de Segurança** - Auth/autorização, proteção de dados, fronteiras de segurança
8. **Arquitetura de Deployment** - Modelo de deployment, CI/CD, estratégia de ambiente, monitoramento
9. **Registros de Decisão de Arquitetura (ADRs)** - Decisões chave com contexto, opções, trade-offs, racional
10. **Orientação Específica RF/RNF** - Abordagem técnica por requisito funcional, prioridades de implementação, dependências
11. **Padrões e Convenções** - Estrutura de diretório, convenções de nomenclatura, organização de código, teste

**Formato ADR (Breve):**

```markdown
## ADR-001: Usar GraphQL para Todas as APIs

**Status:** Aceito | **Data:** 2025-11-02

**Contexto:** PRD requer consultas flexíveis através de múltiplos épicos

**Decisão:** Usar GraphQL para toda comunicação cliente-servidor

**Opções Consideradas:**

1. REST - Familiar mas requer múltiplos endpoints
2. GraphQL - Consultas flexíveis, curva de aprendizado
3. gRPC - Alta performance, suporte de browser ruim

**Racional:**

- PRD requer busca de dados flexível (Épico 1, 3)
- App mobile precisa de otimização de largura de banda (Épico 2)
- Time tem experiência com GraphQL

**Consequências:**

- Positivo: Consultas flexíveis, versionamento reduzido
- Negativo: Complexidade de cache, risco de consulta N+1
- Mitigação: Usar DataLoader para batching

**Implicações para RFs:**

- RF-001: Gestão de Usuário → Mutações GraphQL
- RF-002: App Mobile → Consultas otimizadas
```

**Exemplo:** Plataforma E-commerce → Monólito + PostgreSQL + Redis + Next.js + GraphQL, com ADRs explicando cada escolha e orientação específica RF/RNF.

**Integração:** Alimenta fluxo `create-epics-and-stories`. Arquitetura fornece o contexto técnico necessário para quebrar RFs/RNFs em épicos e estórias implementáveis. Todos os agentes dev referenciam arquitetura durante implementação Fase 4.

---

### create-epics-and-stories

**Propósito:** Transformar requisitos funcionais e não-funcionais do PRD em estórias "mordíveis" organizadas em épicos funcionais entregáveis. Este fluxo roda APÓS arquitetura para que épicos/estórias sejam informados por decisões técnicas.

**Agente:** PM (Gerente de Produto)

**Quando Usar:**

- Após fluxo de arquitetura completar
- Quando PRD contém RFs/RNFs prontos para quebra de implementação
- Antes da verificação de gate implementation-readiness

**Entradas Chave:**

- PRD (RFs/RNFs) do Planejamento Fase 2
- architecture.md com ADRs e decisões técnicas
- Opcional: Artefatos de design UX

**Por Que Após Arquitetura:**

O fluxo `create-epics-and-stories` roda APÓS arquitetura porque:

1. **Dimensionamento de Estória Informado:** Decisões de arquitetura (escolha de banco, estilo de API, etc.) afetam complexidade da estória
2. **Consciência de Dependência:** Arquitetura revela dependências técnicas entre estórias
3. **Viabilidade Técnica:** Estórias podem ter escopo apropriado conhecendo o stack tecnológico
4. **Consistência:** Todas as estórias alinham com padrões arquiteturais documentados

**Saídas Chave:**

Arquivos de Épico (um por épico) contendo:

1. Objetivo e escopo do épico
2. Estórias de usuário com critérios de aceite
3. Prioridades de estória (P0/P1/P2/P3)
4. Dependências entre estórias
5. Notas técnicas referenciando decisões de arquitetura

**Exemplo:** PRD E-commerce com RF-001 (Registro Usuário), RF-002 (Catálogo Produto) → Épico 1: Gestão Usuário (3 estórias), Épico 2: Display Produto (4 estórias), cada estória referenciando ADRs relevantes.

---

### implementation-readiness

**Propósito:** Validar sistematicamente que planejamento e solução estão completos e alinhados antes da implementação Fase 4. Garante que PRD, arquitetura e épicos são coesos sem lacunas.

**Agente:** Arquiteto

**Quando Usar:**

- **Sempre** antes da Fase 4 para projetos BMad Complex e Enterprise
- Após fluxo `create-epics-and-stories` completar
- Antes do fluxo `sprint-planning`
- Quando stakeholders solicitam verificação de prontidão

**Quando Pular:**

- Quick Flow (sem solução)
- BMad Simple (sem gate check requerido)

**Propósito do Gate Check:**

**Previne:**

- ❌ Arquitetura não endereça todos RFs/RNFs
- ❌ Épicos conflitam com decisões de arquitetura
- ❌ Requisitos ambíguos ou contraditórios
- ❌ Faltando dependências críticas

**Garante:**

- ✅ Alinhamento PRD → Arquitetura → Épicos
- ✅ Todos os épicos têm abordagem técnica clara
- ✅ Sem contradições ou lacunas
- ✅ Time pronto para implementar

**Critérios de Checagem:**

**Completude PRD/GDD:**

- Declaração de problema clara e baseada em evidência
- Métricas de sucesso definidas
- Personas de usuário identificadas
- Requisitos funcionais (RFs) completos
- Requisitos não-funcionais (RNFs) especificados
- Riscos e suposições documentados

**Completude Arquitetura:**

- Arquitetura de sistema definida
- Arquitetura de dados especificada
- Arquitetura de API decidida
- ADRs chave documentados
- Arquitetura de segurança endereçada
- Orientação específica RF/RNF provida
- Padrões e convenções definidos

**Completude Épico/Estória:**

- Todas features do PRD mapeadas para estórias
- Estórias têm critérios de aceite
- Estórias priorizadas (P0/P1/P2/P3)
- Dependências identificadas
- Sequenciamento de estória lógico

**Checagens de Alinhamento:**

- Arquitetura endereça todos RFs/RNFs do PRD
- Épicos alinham com decisões de arquitetura
- Sem contradições entre épicos
- RNFs têm abordagem técnica
- Pontos de integração claros

**Lógica de Decisão do Gate:**

**✅ APROVADO**

- Todos critérios críticos atendidos
- Lacunas menores aceitáveis com plano documentado
- **Ação:** Proceda para Fase 4

**⚠️ PREOCUPAÇÕES**

- Alguns critérios não atendidos mas não bloqueadores
- Lacunas identificadas com caminho de resolução claro
- **Ação:** Proceda com cautela, enderece lacunas em paralelo

**❌ REPROVADO**

- Lacunas críticas ou contradições
- Arquitetura faltando decisões chave
- Épicos conflitam com PRD/arquitetura
- **Ação:** BLOQUEIE Fase 4, resolva problemas primeiro

**Saídas Chave:**

**implementation-readiness.md** contendo:

1. Resumo Executivo (APROVADO/PREOCUPAÇÕES/REPROVADO)
2. Avaliação de Completude (pontuações para PRD, Arquitetura, Épicos)
3. Avaliação de Alinhamento (PRD↔Arquitetura, Arquitetura↔Épicos/Estórias, consistência cross-épico)
4. Avaliação de Qualidade (qualidade estória, dependências, riscos)
5. Lacunas e Recomendações (lacunas críticas/menores, remediação)
6. Decisão do Gate com racional
7. Próximos Passos

**Exemplo:** Plataforma E-commerce → PREOCUPAÇÕES ⚠️ devido à falta de arquitetura de segurança e gateway de pagamento indefinido. Recomendação: Completar seção de segurança e adicionar ADR de gateway de pagamento antes de proceder.

---

## Integração com Planejamento e Implementação

### Fluxo Planejamento → Solução

**Quick Flow:**

```
Planejamento (tech-spec por PM)
  → Pular Solução
  → Fase 4 (Implementação)
```

**Método BMad:**

```
Planejamento (prd por PM - RFs/RNFs apenas)
  → Opcional: create-ux-design (Designer UX)
  → architecture (Arquiteto)
  → create-epics-and-stories (PM)
  → implementation-readiness (Arquiteto)
  → Fase 4 (Implementação)
```

**Enterprise:**

```
Planejamento (prd por PM - RFs/RNFs apenas)
  → Opcional: create-ux-design (Designer UX)
  → architecture (Arquiteto)
  → Opcional: security-architecture (Arquiteto, futuro)
  → Opcional: devops-strategy (Arquiteto, futuro)
  → create-epics-and-stories (PM)
  → implementation-readiness (Arquiteto)
  → Fase 4 (Implementação)
```

**Nota sobre TEA (Arquiteto de Teste):** TEA é totalmente operacional com 8 fluxos de trabalho através de todas as fases. TEA valida testabilidade de arquitetura durante revisões de Fase 3 mas não tem um fluxo de solução dedicado. O setup primário do TEA ocorre na Fase 2 (`*framework`, `*ci`, `*test-design`) e execução de testes na Fase 4 (`*atdd`, `*automate`, `*test-review`, `*trace`, `*nfr-assess`).

**Nota:** Enterprise usa o mesmo planejamento e arquitetura que Método BMad. A única diferença são fluxos estendidos opcionais adicionados APÓS arquitetura mas ANTES de create-epics-and-stories.

### Handoff Solução → Implementação

**Documentos Produzidos:**

1. **architecture.md** → Guia todos os agentes dev durante implementação
2. **ADRs** (em architecture) → Referenciados por agentes para decisões técnicas
3. **Arquivos de Épico** (de create-epics-and-stories) → Quebra de trabalho em unidades implementáveis
4. **implementation-readiness.md** → Confirma prontidão para Fase 4

**Como Implementação Usa Solução:**

- **sprint-planning** - Carrega arquitetura e arquivos de épico para organização de sprint
- **dev-story** - Referencia decisões de arquitetura e ADRs
- **code-review** - Valida se código segue padrões arquiteturais

---

## Melhores Práticas

### 1. Torne Decisões Explícitas

Não deixe escolhas de tecnologia implícitas. Documente decisões com racional em ADRs para que agentes entendam contexto.

### 2. Foque em Conflitos de Agente

O trabalho primário da arquitetura é prevenir implementações conflitantes. Foque em preocupações transversais.

### 3. Use ADRs para Decisões Chave

Toda escolha de tecnologia significativa deve ter um ADR explicando "por que", não apenas "o que".

### 4. Mantenha Prático

Não super-arquiteture projetos simples. Projetos BMad Simples precisam de arquitetura simples.

### 5. Rode Gate Check Antes da Implementação

Pegar problemas de alinhamento na solução é 10× mais rápido do que descobri-los no meio da implementação.

### 6. Itere Arquitetura

Documentos de arquitetura são vivos. Atualize-os conforme aprende durante a implementação.

---

## Guia de Decisão

### Quick Flow

- **Planejamento:** tech-spec (PM)
- **Solução:** Pular inteiramente
- **Implementação:** sprint-planning → dev-story

### Método BMad

- **Planejamento:** prd (PM) - cria RFs/RNFs apenas, NÃO épicos
- **Solução:** Opcional UX → architecture (Arquiteto) → create-epics-and-stories (PM) → implementation-readiness (Arquiteto)
- **Implementação:** sprint-planning → create-story → dev-story

### Enterprise

- **Planejamento:** prd (PM) - cria RFs/RNFs apenas (mesmo que Método BMad)
- **Solução:** Opcional UX → architecture (Arquiteto) → Opcional fluxos estendidos (security-architecture, devops-strategy) → create-epics-and-stories (PM) → implementation-readiness (Arquiteto)
- **Implementação:** sprint-planning → create-story → dev-story

**Diferença Chave:** Enterprise adiciona fluxos estendidos opcionais APÓS arquitetura mas ANTES de create-epics-and-stories. Tudo o mais é idêntico ao Método BMad.

**Nota:** TEA (Arquiteto de Teste) opera através de todas as fases e valida testabilidade de arquitetura mas não é um fluxo específico de Fase 3. Veja [Guia de Arquitetura de Teste](./test-architecture.md) para integração de ciclo de vida completo do TEA.

---

## Anti-Padrões Comuns

### ❌ Pulando Arquitetura para Projetos Complexos

"Arquitetura nos atrasa, vamos só começar a codar."
**Resultado:** Conflitos de agente, design inconsistente, retrabalho massivo

### ❌ Super-Engenharia de Projetos Simples

"Deixe-me projetar esta feature simples como um sistema distribuído."
**Resultado:** Tempo desperdiçado, super-engenharia, paralisia de análise

### ❌ Arquitetura Guiada por Template

"Preencha todas as seções deste template de arquitetura."
**Resultado:** Teatro de documentação, sem decisões reais tomadas

### ❌ Pulando Gate Check

"PRD e arquitetura parecem bons o suficiente, vamos começar."
**Resultado:** Lacunas descobertas no meio do sprint, tempo de implementação desperdiçado

### ✅ Abordagem Correta

- Use arquitetura para Método BMad e Enterprise (ambos obrigatórios)
- Foque em decisões, não volume de documentação
- Enterprise: Adicione fluxos estendidos opcionais (teste/segurança/devops) após arquitetura
- Sempre rode gate check antes da implementação

---

## Documentação Relacionada

- [Fase 2: Fluxos de Trabalho de Planejamento](./workflows-planning.md) - Fase anterior
- [Fase 4: Fluxos de Trabalho de Implementação](./workflows-implementation.md) - Próxima fase
- [Sistema Adaptativo à Escala](./scale-adaptive-system.md) - Entendendo trilhas
- [Guia de Agentes](./agents-guide.md) - Referência completa de agente

---

## Solução de Problemas

**P: Eu sempre preciso de arquitetura?**
R: Não. Quick Flow pula. Método BMad e Enterprise ambos requerem.

**P: Como sei se preciso de arquitetura?**
R: Se você escolheu trilha Método BMad ou Enterprise no planejamento (workflow-init), você precisa de arquitetura para prevenir conflitos de agente.

**P: Qual a diferença entre arquitetura e tech-spec?**
R: Tech-spec é focado em implementação para mudanças simples. Arquitetura é design de sistema para projetos multi-épico complexos.

**P: Posso pular gate check?**
R: Apenas para Quick Flow. Método BMad e Enterprise ambos requerem gate check antes da Fase 4.

**P: E se gate check falhar?**
R: Resolva as lacunas identificadas (seções de arquitetura faltando, requisitos conflitantes) e re-execute gate check.

**P: Quanto tempo arquitetura deve levar?**
R: Método BMad: 1-2 dias para arquitetura. Enterprise: 2-3 dias total (1-2 dias arquitetura + 0.5-1 dia fluxos estendidos opcionais). Se demorar mais, você pode estar super-documentando.

**P: ADRs precisam ser perfeitos?**
R: Não. ADRs capturam decisões chave com racional. Devem ser concisos (1 página max por ADR).

**P: Posso atualizar arquitetura durante implementação?**
R: Sim! Arquitetura é viva. Atualize-a conforme aprende. Use fluxo `correct-course` para mudanças significativas.

---

_Solução Fase 3 - Decisões técnicas antes da implementação._
