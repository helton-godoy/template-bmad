# Desenho de Teste e Avaliação de Risco - Lista de Verificação de Validação

## Pré-requisitos

- [ ] Contagem da história com critérios claros de aceitação
- [ ] PRD ou documentação épica disponível
- [ ] Documentos de arquitectura disponíveis (opcional)
- [ ] Os requisitos são testáveis e inequívocos

## Passos do processo

### Passo 1: Carregando o Contexto

- [ ] PRD.md leitura e requisitos extraídos
- [ ] Epics.md ou documentação épica específica carregada
- [ ] Marcação da história com critérios de aceitação analisados
- [ ] Documentos de arquitectura revistos (se disponíveis)
- [ ] Cobertura de teste existente analisada
- [ ] Fragmentos de base de conhecimento carregados (governança de risco, probabilidade-impacto, níveis de ensaio, prioridades de ensaio)

### Etapa 2: Avaliação de risco

- [ ] Riscos genuínos identificados (não apenas características)
- [ ] Riscos classificados por categoria (TEC/SEC/PERF/DATA/BUS/OPS)
- [ ] Probabilidade marcada (1-3 para cada risco)
- [ ] Impacto registado (1-3 para cada risco)
- [ ] Escore de risco calculado (probabilidade × impacto)
- [ ] Riscos de elevada prioridade (pontuação ≥6)
- [ ] Planos de atenuação definidos para riscos de elevada prioridade
- [ ] Proprietários designados para cada mitigação
- [ ] Prazos fixados para mitigação
- Risco residual documentado

### Etapa 3: Desenho da cobertura

- [ ] Critérios de aceitação divididos em cenários atómicos
- [ ] Níveis de ensaio seleccionados (E2E/API/Componente/Unit)
- [ ] Nenhuma cobertura duplicada entre os níveis
- [ ] Níveis prioritários atribuídos (P0/P1/P2/P3)
- [ ] Os cenários P0 satisfazem critérios rigorosos (núcleo dos blocos + risco elevado + ausência de solução alternativa)
- [ ] Dados pré-requisitos identificados
- [ ] Requisitos de ferramentas documentados
- [ ] Ordem de execução definida (fumo → P0 → P1 → P2/P3)

### Passo 4: Geração de resultados

- [ ] Matriz de avaliação de risco criada
- [ ] Matriz de cobertura criada
- Ordem de execução documentada
- [ ] Estimativas dos recursos calculadas
- [ ] Critérios da porta de qualidade definidos
- [ ] Ficheiro de saída gravado para corrigir a localização
- [ ] O ficheiro de saída usa a estrutura do modelo

## Validação de Saída

### Matriz de avaliação de risco

- [ ] Todos os riscos têm IDs únicos (R-001, R-002, etc.)
- [ ] Cada risco tem categoria atribuída
- [ ] Os valores de probabilidade são 1, 2 ou 3
- [ ] Os valores de impacto são 1, 2 ou 3
- [ ] Pontuações calculadas correctamente (P × I)
- [ ] Riscos de alta prioridade (≥6) claramente assinalados
- [ ] Estratégias de atenuação específicas e acionáveis

### Matriz de cobertura

- [ ] Todos os requisitos mapeados para os níveis de ensaio
Prioridades atribuídas a todos os cenários
- [ ] Relação de risco documentada
- [ ] Contagens de teste realistas
- [ ] Proprietários atribuídos quando aplicável
- [ ] Nenhuma cobertura duplicada (mesma conduta em múltiplos níveis)

### Ordem de Execução

- [ ] Testes de fumo definidos (alvo < 5 min)
- [ ] Testes P0 listados (< 10 min alvo)
- [ ] Testes P1 listados (alvo < 30 min)
- [ ] Ensaios P2/P3 listados (alvo < 60 minutos)
- [ ] Ordem otimiza para feedback rápido

### Estimativas de recursos

- [ ] P0 horas calculadas (contagem × 2 horas)
- [ ] P1 horas calculadas (contagem × 1 hora)
- [ ] P2 horas calculadas (contagem × 0,5 horas)
- [ ] P3 horas calculadas (contagem × 0,25 horas)
- [ ] Total de horas somadas
- [ ] Estimativa de dias fornecida (horas / 8)
- [ ] As estimativas incluem tempo de instalação

### Critérios da porta de qualidade

- [ ] P0 limite de taxa de passagem definido (deve ser de 100%)
- [ ] Limite da taxa de passagem P1 definido (normalmente ≥95%)
- [ ] Complemento de redução de alto risco necessário
- [ ] Alvos de cobertura especificados (≥80% recomendados)

## Controlos de qualidade

### Avaliação baseada em provas

- [ ] Avaliação de risco baseada em provas documentadas
- [ ] Nenhuma especulação sobre o impacto das empresas
- [ ] Suposições claramente documentadas
- [ ] Clarificações solicitadas sempre que necessário
- [ ] Dados históricos referenciados quando disponíveis

### Precisão na classificação de risco

- [ ] Os riscos de TECH são questões de arquitectura/integração
- [ ] Riscos SEC são vulnerabilidades de segurança
- [ ] Os riscos de perf são preocupações de desempenho/escalabilidade
- [ ] Riscos de dados são questões de integridade dos dados
- [ ] Riscos de BUS são impactos das empresas/receitas
- [ ] Os riscos da OPS são questões de implantação/operação

### Precisão de atribuição prioritária

- [ ] P0: Realmente bloqueia a funcionalidade do núcleo
- [ ] P0: Alto risco (escore ≥6)
- [ ] P0: Nenhuma solução existe
- [ ] P1: Importante mas não bloqueando
- [ ] P2/P3: Casos bonitos para ter ou bordar

### Seleção do nível de teste

- [ ] E2E usado apenas para caminhos críticos
- [ ] Testes API cobrem lógica complexa de negócios
- [ ] Testes de componentes para interações com IU
- [ ] Testes unitários para casos de bordas e algoritmos
- [ ] Sem cobertura redundante

## Pontos de Integração

### Integração com a Base de Conhecimento

- [ ] risk-governance.md consultado
- [ ] probability-impact.md aplicado
- [ ] test-levels-framework.md referenciado
- [ ] test-priorities-matrix.md utilizado
- [ ] Fragmentos adicionais carregados conforme necessário

### Integração do Ficheiro de Estado

- [ ] bmm-workflow-status.md existe
- [ ] Design de teste logado em Progresso de Qualidade e Teste
- [ ] Número épico e âmbito documentado
- [ ] Hora de conclusão gravada

### Dependências do fluxo de trabalho

- [ ] Pode prosseguir para `atdd` fluxo de trabalho com cenários P0
- [ ] Pode prosseguir para `automate` fluxo de trabalho com plano de cobertura completo
- [ ] Avaliação de risco informa `gate` workflow criteria
- [ ] Integra a sagacidade