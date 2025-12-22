# Orientações para a criação de elementos excalidraw

## Cálculo da Largura do Texto

Para elementos de texto dentro das formas (marcas):

```
text_width = (text.length × fontSize × 0.6) + 20

```

Redonda para 10 mais próximo para alinhamento da rede.

## Regras de agrupamento de elementos

**CRITICAL:** Ao criar formas com rótulos:

1. Gerar IDs únicos:
- BMADPROTECT031FEND para a forma
- BMADPROTECT030FEND para o texto
- `group-id` para o grupo

2. O elemento da forma deve ter:
- `groupIds: [group-id]`
- `boundElements: [{type: "text", id: text-id}]`

3. O elemento texto deve ter:
- `containerId: shape-id`
- `groupIds: [group-id]` (mesma forma)
- `textAlign: "center"`
- `verticalAlign: "middle"`
- `width: calculated_width`

## Alinhamento da grelha

- Ligar todas as coordenadas `x`, BMADPROTECT020End para 20px grid
BMADPROTECT032end BMADPROTECT019end
- Espaço entre elementos: 60px mínimo

## Criação de Setas

### Setas retas

Usar para fluxo dianteiro (da esquerda para a direita, de cima para baixo):

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

### Setas de cotovelo

Uso para fluxo para cima, fluxo para trás ou roteamento complexo:

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

### Actualizar as Formas Ligadas

Depois de criar seta, atualizar `boundElements` em ambas as formas conectadas:

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

- **Shapes**: `backgroundColor` from theme primary fill
- **Borders**: `strokeColor` do acento do tema
- **Texto**: `strokeColor` = "#1e1e1e" (texto escuro)
- **Arrows**: `strokeColor` do acento do tema

## Lista de Verificação de Validação

Antes de gravar, verifique:

- [ ] Todas as formas com etiquetas têm `groupIds`
- [ ] Todos os elementos de texto têm `containerId` apontando para a forma pai
- [ ] Largura do texto calculada corretamente (sem corte)
- [ ] Conjunto de alinhamento de texto (`textAlign` + `verticalAlign`)
- [ ] Todos os elementos ligados à grelha 20px
- [ ] Todas as setas têm `startBinding` e `endBinding`
- [ ] `boundElements` array atualizado em formas conectadas
- [ ] Cores do tema aplicadas de forma consistente
- [ ] Nenhum meta- dados ou histórico no resultado final
- [ ] Todos os IDs são únicos

## Optimização

Remover do resultado final:

- `appState` object
- `files` object (a menos que as imagens utilizadas)
- Todos os elementos com `isDeleted: true`
- Itens de biblioteca não usados
- Histórico da versão
