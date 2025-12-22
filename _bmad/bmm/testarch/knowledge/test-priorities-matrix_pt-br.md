<!-- Powered by BMAD-CORE™ -->

# Matriz de Prioridades de Teste

Guia para priorizar cenários de teste baseados em risco, criticidade e impacto empresarial.

## Níveis prioritários

### P0 - Crítico (Teste Mústico)

**Criteria:**

- Funcionalidade de impacto de receita
- Caminhos críticos de segurança
- Operações de integridade de dados
- Requisitos de conformidade regulamentar
- Funcionalidade anteriormente quebrada (prevenção de regressão)

**Exemplos:**

- Processamento de pagamentos
- Autenticação/autorização
- Criação/deleção de dados do utilizador
- Cálculos financeiros
- Conformidade GDPR/privacidade

**Requisitos de ensaio:**

- Cobertura abrangente a todos os níveis
- Ambos caminhos felizes e infelizes
- Casos de borda e cenários de erro
- Desempenho sob carga

### P1 - Alta (prova)

**Criteria:**

- Principais viagens de utilizadores
- Características usadas frequentemente
- Características com lógica complexa
- Pontos de integração entre sistemas
- Características que afetam a experiência do usuário

**Exemplos:**

- Fluxo de registro do usuário
- Funcionalidade de busca
- Dados import/export
- Sistemas de notificação
- Exibições do painel

**Requisitos de ensaio:**

- Caminhos felizes primários necessários
- Cenários de erro chave
- Casos críticos de borda
- Validação básica do desempenho

### P2 - Meio (Nice to Test)

**Criteria:**

- Características secundárias
- Funcionalidade de administração
- Elementos de comunicação
- Opções de configuração
- IU polonês e estética

**Exemplos:**

- Painéis de configurações de administração
- Geração de relatórios
- Personalização do tema
- Documentação de ajuda
- Rastreio de análise

**Requisitos de ensaio:**

- Feliz cobertura do caminho
- Tratamento básico de erros
- Pode adiar casos de borda

### P3 - Baixo (Teste se o tempo permitir)

**Criteria:**

- Características raramente utilizadas
- Boa funcionalidade
- Questões cosméticas
- Optimizações não críticas

**Exemplos:**

- Preferências avançadas
- Suporte ao recurso Legado
- Características experimentais
- Utilitários de depuração

**Requisitos de ensaio:**

- Apenas testes de fumo
- Pode confiar em testes manuais
- Limitações conhecidas do documento

## Ajustamentos prioritários baseados no risco

### Aumentar a prioridade quando:

- Alto impacto do usuário (afeta > 50% dos usuários)
- Alto impacto financeiro (>$10K perda potencial)
- Potencial de vulnerabilidade à segurança
- Cumprimento/requisitos legais
- Problemas relatados pelo cliente
- Complexo implementation (>500 LOC)
- Várias dependências do sistema

### Diminuir Prioridade Quando:

- Bandeira de recurso protegida
- Lançamento gradual planned
- Monitorização forte no local
- Fácil capacidade de retrocesso
- métricas de baixo uso
- Simples implementation
- Componente bem isolado

## Cobertura do ensaio por prioridade

| Priority | Unit Coverage | Integration Coverage | E2E Coverage       |
| -------- | ------------- | -------------------- | ------------------ |
| P0       | >90%          | >80%                 | All critical paths |
| P1       | >80%          | >60%                 | Main happy paths   |
| P2       | >60%          | >40%                 | Smoke tests        |
| P3       | Best effort   | Best effort          | Manual only        |

## Regras de atribuição prioritárias

1. **Comece com o impacto do negócio** - O que acontece se isto falhar?
2. **Considere probabilidade** - Quão provável é o fracasso?
3. **Factor na detecção** - Saberíamos se falhou?
4. **Conta para valorização** - Podemos corrigi-lo rapidamente?

## Árvore de decisão prioritária

```
Is it revenue-critical?
├─ YES → P0
└─ NO → Does it affect core user journey?
    ├─ YES → Is it high-risk?
    │   ├─ YES → P0
    │   └─ NO → P1
    └─ NO → Is it frequently used?
        ├─ YES → P1
        └─ NO → Is it customer-facing?
            ├─ YES → P2
            └─ NO → P3

```

## Ordem de Execução de Teste

1. Execute testes P0 primeiro (falha rápido em questões críticas)
2. Executar testes P1 segundo (funcionalidade núcleo)
3. Execute testes P2 se o tempo permitir
4. Testes de P3 apenas em ciclos de regressão completos

## Ajuste contínuo

Rever e ajustar as prioridades com base em:

- Padrões de incidentes de produção
- feedback do usuário e reclamações
- Análise de uso
- Histórico de falhas de teste
- Mudanças nas prioridades comerciais

---

## Classificação Prioritária Automatizada

### Exemplo: Calculadora de Prioridade (Automação Baseada em Risco)

«``typescript
// src/testing/priority-calculator.ts

export type Priority = 'P0' .

export type PriorityFactors = {
  revenueImpact: 'critical' | 'high' | 'medium' | 'low' | 'none';
  userImpact: 'all' | 'majority' | 'some' | 'few' | 'minimal';
  securityRisk: boolean;
  complianceRequired: boolean;
  previousFailure: boolean;
  complexity: 'high' | 'medium' | 'low';
  usage: 'frequent' | 'regular' | 'occasional' | 'rare';
};

/**
* Calcular a prioridade do teste com base em múltiplos fatores
* Espelha a árvore de decisão prioritária com critérios objetivos
*/
BMADPROTECT008end BMADPROTECT007end calculePriority(factores: PriorityFactors): Priority BMADPROTECT014end = factors;

// P0: Receita crítica, segurança ou conformidade
if (revenueImpact === 'crítico' segurançaRisco de conformidadeRequisito de conformidade (previousFailure && resourceImpact === 'alto')) {
    return 'P0';
  }

// P0: Alta receita + alta comple