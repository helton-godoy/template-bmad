# Diretrizes de Criação de Elementos Excalidraw

## Cálculo da Largura do Texto

Para elementos de texto dentro de formas (rótulos):

```
text_width = (text.length × fontSize × 0.6) + 20
```

Arredonde para o 10 mais próximo para alinhamento na grade.

## Regras de Agrupamento de Elementos

**CRÍTICO:** Ao criar formas com rótulos:

1. Gere IDs únicos:
   - `shape-id` para a forma
   - `text-id` para o texto
   - `group-id` para o grupo

2. O elemento de forma deve ter:
   - `groupIds: [group-id]`
   - `boundElements: [{type: "text", id: text-id}]`

3. O elemento de texto deve ter:
   - `containerId: shape-id`
   - `groupIds: [group-id]` (MESMO que a forma)
   - `textAlign: "center"`
   - `verticalAlign: "middle"`
   - `width: calculated_width`

## Alinhamento na Grade

- Ajuste todas as coordenadas `x`, `y` para a grade de 20px
- Fórmula: `Math.round(value / 20) * 20`
- Espaçamento entre elementos: 60px mínimo

## Criação de Setas

### Setas Retas

Use para fluxo direto (esquerda para direita, topo para baixo):

```json
{
  "type": "arrow",
  "startBinding": {
    "elementId": "source-shape-id",
    "focus": 0,
    "gap": 10
  },
  "endBinding": {
    "elementId": "target-shape-id",
    "focus": 0,
    "gap": 10
  },
  "points": [[0, 0], [distance_x, distance_y]]
}
```

### Setas em Cotovelo

Use para fluxo para cima, fluxo para trás ou roteamento complexo:

```json
{
  "type": "arrow",
  "startBinding": {...},
  "endBinding": {...},
  "points": [
    [0, 0],
    [intermediate_x, 0],
    [intermediate_x, intermediate_y],
    [final_x, final_y]
  ],
  "elbowed": true
}
```

### Atualizar Formas Conectadas

Após criar a seta, atualize `boundElements` em ambas as formas conectadas:

```json
{
  "id": "shape-id",
  "boundElements": [
    { "type": "text", "id": "text-id" },
    { "type": "arrow", "id": "arrow-id" }
  ]
}
```

## Aplicação de Tema

As cores do tema devem ser aplicadas de forma consistente:

- **Formas**: `backgroundColor` do preenchimento primário do tema
- **Bordas**: `strokeColor` do destaque do tema
- **Texto**: `strokeColor` = "#1e1e1e" (texto escuro)
- **Setas**: `strokeColor` do destaque do tema

## Lista de Verificação de Validação

Antes de salvar, verifique:

- [ ] Todas as formas com rótulos têm `groupIds` correspondentes
- [ ] Todos os elementos de texto têm `containerId` apontando para a forma pai
- [ ] Largura do texto calculada corretamente (sem cortes)
- [ ] Alinhamento de texto definido (`textAlign` + `verticalAlign`)
- [ ] Todos os elementos ajustados à grade de 20px
- [ ] Todas as setas têm `startBinding` e `endBinding`
- [ ] Array `boundElements` atualizado nas formas conectadas
- [ ] Cores do tema aplicadas consistentemente
- [ ] Sem metadados ou histórico na saída final
- [ ] Todos os IDs são únicos

## Otimização

Remova da saída final:

- Objeto `appState`
- Objeto `files` (a menos que imagens sejam usadas)
- Todos os elementos com `isDeleted: true`
- Itens de biblioteca não utilizados
- Histórico de versões
