# Criar Fluxograma - Lista de Verificação de Validação

## Estrutura do elemento

- [ ] Todas as formas com etiquetas têm `groupIds`
- [ ] Todos os elementos de texto têm `containerId` apontando para a forma pai
- [ ] Largura do texto calculada corretamente (sem corte)
- [ ] Conjunto de alinhamento de texto (`textAlign` + `verticalAlign`)

## Disposição e alinhamento

- [ ] Todos os elementos ligados à grelha 20px
- [ ] Espaçamento consistente entre elementos (mínimo 60px)
- [ ] Alinhamento vertical mantido para a direção do fluxo
- [ ] Sem elementos sobrepostos

## Ligações

- [ ] Todas as setas têm `startBinding` e `endBinding`
- [ ] `boundElements` array atualizado em formas conectadas
- [ ] Tipos de setas apropriados (para a frente, cotovelo para trás/para cima)
- [ ] Gap definido para 10 para todas as ligações

## Tema e Styling

- [ ] Cores do tema aplicadas de forma consistente
- [ ] Todas as formas usam a cor de preenchimento primária do tema
- [ ] Todas as bordas usam a cor do acento do tema
- [ ] A cor do texto é legível (# 1e1e1e)

## Composição

- Contagem de elementos abaixo de 50
- [ ] Componentes da biblioteca referenciados sempre que possível
- [ ] Sem definições de elementos duplicados

## Qualidade da saída

- [ ] Sem elementos com `isDeleted: true`
- O JSON é válido.
- [ ] Arquivo salvo para corrigir a localização

## Requisitos funcionais

- [ ] Ponto inicial claramente marcado
- [ ] Ponto final claramente marcado
- [ ] Todos os passos do processo marcados
- Os pontos de decisão utilizam formas de diamante
- [ ] A direção do fluxo é clara e lógica
