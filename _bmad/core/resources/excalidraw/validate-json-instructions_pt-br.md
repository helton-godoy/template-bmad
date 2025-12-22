Instruções de validação JSON

## Objecto

Validar arquivos Excalidraw JSON após salvar para capturar erros de sintaxe (perdendo vírgulas, parênteses, citações).

## Como validar

Use o processamento JSON incorporado Node.js para validar o arquivo:

```bash
node -e "JSON.parse(require('fs').readFileSync('FILE_PATH', 'utf8')); console.log('✓ Valid JSON')"

```

Substituir o `FILE_PATH` pelo caminho real do ficheiro.

## Códigos de saída

- Código de saída 0 = JSON válido
- Código de saída 1 = JSON inválido (erro de sintaxe)

## Resultado do Erro

Se inválido, o Node.js irá produzir:

- Mensagem de erro com descrição
- Posição no arquivo onde ocorreu o erro
- Informação de linha e coluna (se disponível)

## Erros e correções comuns

### Falta o Comando

```
SyntaxError: Expected ',' or '}' after property value

```

**Fix:** Adicionar vírgula após o valor da propriedade

### Falta o Bracket/Brace

```
SyntaxError: Unexpected end of JSON input

```

**Fix:** Adicionar o suporte de fecho em falta `]` ou braçadeira `}`

### Extra Comma (Trailing)

```
SyntaxError: Unexpected token ,

```

**Fix:** Remover a vírgula que se segue antes de `]` ou `}`

### Citação em falta

```
SyntaxError: Unexpected token

```

**Fix:** Adicionar o valor da citação em falta

## Integração do fluxo de trabalho

Após salvar um arquivo Excalidraw, execute a validação:

1. Salve o arquivo
2. Executar: `node -e "JSON.parse(require('fs').readFileSync('{{save_location}}', 'utf8')); console.log('✓ Valid JSON')"`
3. Se a validação falhar:
- Leia a mensagem de erro para linha/posição
- Abra o arquivo nesse local
- Corrigir o erro de sintaxe
- Salvar e revalidar
4. Repita até que a validação passe

## Regra crítica

**NEVER delete o arquivo devido a erros de validação - sempre corrigir o erro de sintaxe no local relatado.**
