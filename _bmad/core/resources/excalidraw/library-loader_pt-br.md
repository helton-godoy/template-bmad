# Carregador de Biblioteca Externa

**Estatus:** Titulara do lugar para o futuro implementation

## Objecto

Carregar arquivos .excalidrawlib externos de <https://libraries.excalidraw.com> ou fontes personalizadas.

## Planned Capacidades

- Carregar bibliotecas por URL
- Carregar bibliotecas de arquivos locais
- Mesclar várias bibliotecas
- Filtrar componentes da biblioteca
- Bibliotecas carregadas em cache

## Referência da API

Irá documentar como usar:

- `importLibrary(url)` - Carregar biblioteca a partir de URL
- `loadSceneOrLibraryFromBlob()` - Carregar a partir do ficheiro
- `mergeLibraryItems()` - Combine bibliotecas

## Exemplo de Uso

```yaml

# Future workflow.yaml structure
libraries:
  - url: 'https://libraries.excalidraw.com/libraries/...'
    filter: ['aws', 'cloud']
  - path: '{project-root}/_data/custom-library.excalidrawlib'

```

## Implementation Notas

Isso será desenvolvido quando os agentes precisarem aproveitar o extenso ecossistema de bibliotecas disponível no <https://libraries.excalidraw.com>.

Existem centenas de bibliotecas de componentes pré- construídas para:

- Ícones AWS/Cloud
- Componentes UI/UX
- Diagramas de negócios
- Formas de mapas mentais
- Planos de piso
- E muito mais...

## Configuração do usuário

Future: Users poderá configurar bibliotecas favoritas em sua configuração BMAD para carregamento automático.
