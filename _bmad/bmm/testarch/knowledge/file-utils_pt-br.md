# Utilitários de Arquivo

## Princípio

Leia e valide arquivos (CSV, XLSX, PDF, ZIP) com parsing automático, resultados type-safe e manipulação de download. Simplifique operações de arquivo em testes Playwright com suporte a formato integrado e helpers de validação.

## Motivação

Testar operações de arquivo no Playwright requer boilerplate:

- Manipulação de download manual
- Bibliotecas de parsing externas para cada formato
- Sem helpers de validação
- Resultados type-unsafe
- Manipulação de caminho repetitiva

O módulo `file-utils` fornece:

- **Auto-parsing**: CSV, XLSX, PDF, ZIP automaticamente parseados
- **Manipulação de download**: Função única para downloads disparados por UI ou API
- **Type-safe**: Interfaces TypeScript para resultados parseados
- **Helpers de validação**: Contagem de linha, verificações de cabeçalho, validação de conteúdo
- **Suporte a formato**: Suporte a múltiplas planilhas (XLSX), extração de texto (PDF), extração de arquivo (ZIP)

## Exemplos de Padrões

### Exemplo 1: Download de CSV Disparado por UI

**Contexto**: Usuário clica botão, CSV baixa, valida conteúdo.

**Implementação**:

```typescript
import { handleDownload, readCSV } from '@seontechnologies/playwright-utils/file-utils';
import path from 'node:path';

const DOWNLOAD_DIR = path.join(__dirname, '../downloads');

test('deve baixar e validar CSV', async ({ page }) => {
  const downloadPath = await handleDownload({
    page,
    downloadDir: DOWNLOAD_DIR,
    trigger: () => page.click('[data-testid="export-csv"]'),
  });

  const { content } = await readCSV({ filePath: downloadPath });

  // Validar cabeçalhos
  expect(content.headers).toEqual(['ID', 'Nome', 'Email', 'Cargo']);

  // Validar dados
  expect(content.data).toHaveLength(10);
  expect(content.data[0]).toMatchObject({
    ID: expect.any(String),
    Nome: expect.any(String),
    Email: expect.stringMatching(/@/),
  });
});
```

**Pontos Chave**:

- `handleDownload` aguarda download, retorna caminho do arquivo
- `readCSV` auto-parseia para `{ headers, data }`
- Acesso type-safe ao conteúdo parseado
- Limpe downloads no `afterEach`

### Exemplo 2: XLSX com Múltiplas Planilhas

**Contexto**: Arquivo Excel com múltiplas planilhas (ex: Resumo, Detalhes, Erros).

**Implementação**:

```typescript
import { readXLSX } from '@seontechnologies/playwright-utils/file-utils';

test('deve ler XLSX multi-planilha', async () => {
  const downloadPath = await handleDownload({
    page,
    downloadDir: DOWNLOAD_DIR,
    trigger: () => page.click('[data-testid="export-xlsx"]'),
  });

  const { content } = await readXLSX({ filePath: downloadPath });

  // Acessar planilhas específicas
  const summarySheet = content.sheets.find((s) => s.name === 'Resumo');
  const detailsSheet = content.sheets.find((s) => s.name === 'Detalhes');

  // Validar resumo
  expect(summarySheet.data).toHaveLength(1);
  expect(summarySheet.data[0].TotalRecords).toBe('150');

  // Validar detalhes
  expect(detailsSheet.data).toHaveLength(150);
  expect(detailsSheet.headers).toContain('TransactionID');
});
```

**Pontos Chave**:

- Array `sheets` com propriedades `name` e `data`
- Acesse planilhas por nome
- Cada planilha tem seus próprios cabeçalhos e dados
- Iteração de planilha type-safe

### Exemplo 3: Extração de Texto de PDF

**Contexto**: Validar se relatório PDF contém conteúdo esperado.

**Implementação**:

```typescript
import { readPDF } from '@seontechnologies/playwright-utils/file-utils';

test('deve validar relatório PDF', async () => {
  const downloadPath = await handleDownload({
    page,
    downloadDir: DOWNLOAD_DIR,
    trigger: () => page.click('[data-testid="download-report"]'),
  });

  const { content } = await readPDF({ filePath: downloadPath });

  // content.text é o texto extraído de todas as páginas
  expect(content.text).toContain('Relatório Financeiro Q4 2024');
  expect(content.text).toContain('Receita Total:');

  // Validar contagem de páginas
  expect(content.numpages).toBeGreaterThan(10);
});
```

**Pontos Chave**:

- `content.text` contém todo texto extraído
- `content.numpages` para contagem de páginas
- Parsing de PDF lida com documentos multi-página
- Busca por frases específicas

### Exemplo 4: Validação de Arquivo ZIP

**Contexto**: Validar se ZIP contém arquivos esperados e extrair arquivo específico.

**Implementação**:

```typescript
import { readZIP } from '@seontechnologies/playwright-utils/file-utils';

test('deve validar arquivo ZIP', async () => {
  const downloadPath = await handleDownload({
    page,
    downloadDir: DOWNLOAD_DIR,
    trigger: () => page.click('[data-testid="download-backup"]'),
  });

  const { content } = await readZIP({ filePath: downloadPath });

  // Verificar lista de arquivos
  expect(content.files).toContain('data.csv');
  expect(content.files).toContain('config.json');
  expect(content.files).toContain('readme.txt');

  // Ler arquivo específico do arquivo
  const configContent = content.zip.readAsText('config.json');
  const config = JSON.parse(configContent);

  expect(config.version).toBe('2.0');
});
```

**Pontos Chave**:

- `content.files` lista todos arquivos no arquivo
- `content.zip.readAsText()` extrai arquivos específicos
- Valide estrutura do arquivo
- Leia e parseie arquivos individuais do ZIP

### Exemplo 5: Download Disparado por API

**Contexto**: Endpoint de API retorna download de arquivo (não clique de UI).

**Implementação**:

```typescript
test('deve baixar via API', async ({ page, request }) => {
  const downloadPath = await handleDownload({
    page,
    downloadDir: DOWNLOAD_DIR,
    trigger: async () => {
      const response = await request.get('/api/export/csv', {
        headers: { Authorization: 'Bearer token' },
      });

      if (!response.ok()) {
        throw new Error(`Exportação falhou: ${response.status()}`);
      }
    },
  });

  const { content } = await readCSV({ filePath: downloadPath });

  expect(content.data).toHaveLength(100);
});
```

**Pontos Chave**:

- `trigger` pode ser chamada de API async
- API deve retornar cabeçalho `Content-Disposition`
- Ainda precisa de `page` para eventos de download
- Funciona com endpoints autenticados

## Helpers de Validação

```typescript
// Validação CSV
const { isValid, errors } = await validateCSV({
  filePath: downloadPath,
  expectedRowCount: 10,
  requiredHeaders: ['ID', 'Nome', 'Email'],
});

expect(isValid).toBe(true);
expect(errors).toHaveLength(0);
```

## Padrão de Limpeza de Download

```typescript
test.afterEach(async () => {
  // Limpar arquivos baixados
  await fs.remove(DOWNLOAD_DIR);
});
```

## Fragmentos Relacionados

- `overview.md` - Instalação e importações
- `api-request.md` - Downloads disparados por API
- `recurse.md` - Poll para conclusão de geração de arquivo

## Anti-Padrões

**❌ Não limpar downloads:**

```typescript
test('cria arquivo', async () => {
  await handleDownload({ ... })
  // Arquivo deixado na pasta de downloads
})
```

**✅ Limpar após testes:**

```typescript
test.afterEach(async () => {
  await fs.remove(DOWNLOAD_DIR);
});
```
