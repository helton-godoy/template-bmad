# Criar Diagrama - Lista de Verificação de Validação

## Estrutura do elemento

- [ ] Todos os componentes com etiquetas têm `groupIds`
- [ ] Todos os elementos de texto têm `containerId` apontando para o componente pai
- [ ] Largura do texto calculada corretamente (sem corte)
- [ ] Alinhamento de texto apropriado para o tipo de diagrama

## Disposição e alinhamento

- [ ] Todos os elementos ligados à grelha 20px
- [ ] Espaçamento de componentes consistente (40px/60px)
- [ ] Alinhamento hierárquico mantido
- [ ] Sem elementos sobrepostos

## Ligações

- [ ] Todas as setas têm `startBinding` e `endBinding`
- [ ] `boundElements` array atualizado em componentes conectados
- [ ] Roteamento de setas evita sobreposições
- [ ] Tipos de relacionamento claramente indicados

## Notação e Normas

- [ ] Segue a norma de notação especificada (UML/ERD/etc)
- [ ] Símbolos usados corretamente
- [ ] Cardinalidade/multiplicidade mostrada onde necessário
- [ ] Etiquetas e anotações claras

## Tema e Styling

- [ ] Cores do tema aplicadas de forma consistente
- [ ] Tipos de componentes visualmente distinguíveis
- [ ] O texto é legível
- Aparência profissional

## Qualidade da saída

- Contagem de elementos abaixo de 80
- [ ] Sem elementos com `isDeleted: true`
- O JSON é válido.
- [ ] Arquivo salvo para corrigir a localização
