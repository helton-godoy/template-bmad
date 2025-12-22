# Utilitários de Ficheiros

## Princípio

Leia e valide arquivos (CSV, XLSX, PDF, ZIP) com análise automática, resultados seguros de tipo e manuseio de download. Simplifique as operações de arquivos em testes Playwright com suporte de formato embutido e ajudantes de validação.

## Racional

Teste de operações de arquivos em Playwright requer caldeira:

- Manipulação manual de download
- Bibliotecas de análise externa para cada formato
- Nenhum ajudante de validação
- Resultados não seguros
- Tratamento do caminho repetitivo

O módulo `file-utils` fornece:

- **Auto-parsing**: CSV, XLSX, PDF, ZIP automaticamente analisado
- **Download handling**: function único para downloads com interface ou API
- **Type-safe**: Interfaces TypeScript para resultados analisados
- **Validation helpers**: Contagem de linhas, verificação de cabeçalhos, validação de conteúdo
- **Suporte ao formato**: Suporte a múltiplas folhas (XLSX), extração de texto (PDF), extração de arquivos (ZIP)

## Exemplos de padrões

### Exemplo 1: Transferência de CSV por IU

**Contexto**: Botão de cliques do usuário, downloads CSV, validar conteúdo.

**Implementation**:

```typescript
import { handleDownload, readCSV } from '@seontechnologies/playwright-utils/file-utils';
import path from 'node:path';

const DOWNLOAD_DIR = path.join(__dirname, '../downloads');

test('should download and validate CSV', async ({ page }) => {
  const downloadPath = await handleDownload({
    page,
    downloadDir: DOWNLOAD_DIR,
    trigger: () => page.click('[data-testid="export-csv"]'),
  });

  const { content } = await readCSV({ filePath: downloadPath });

  // Validate headers
  expect(content.headers).toEqual(['ID', 'Name', 'Email', 'Role']);

  // Validate data
  expect(content.data).toHaveLength(10);
  expect(content.data[0]).toMatchObject({
    ID: expect.any(String),
    Name: expect.any(String),
    Email: expect.stringMatching(/@/),
  });
});

```

**Pontos-chave**

- `handleDownload` espera para download, retorna o caminho do arquivo
- `readCSV` auto- análise para `{ headers, data }`
- Acesso seguro ao conteúdo analisado
- Limpar downloads no `afterEach`

### Exemplo 2: XLSX com múltiplas folhas

**Contexto**: ficheiro Excel com várias folhas (por exemplo, Resumo, Detalhes, Erros).

**Implementation**:

```typescript
import { readXLSX } from '@seontechnologies/playwright-utils/file-utils';

test('should read multi-sheet XLSX', async () => {
  const downloadPath = await handleDownload({
    page,
    downloadDir: DOWNLOAD_DIR,
    trigger: () => page.click('[data-testid="export-xlsx"]'),
  });

  const { content } = await readXLSX({ filePath: downloadPath });

  // Access specific sheets
  const summarySheet = content.sheets.find((s) => s.name === 'Summary');
  const detailsSheet = content.sheets.find((s) => s.name === 'Details');

  // Validate summary
  expect(summarySheet.data).toHaveLength(1);
  expect(summarySheet.data[0].TotalRecords).toBe('150');

  // Validate details
  expect(detailsSheet.data).toHaveLength(150);
  expect(detailsSheet.headers).toContain('TransactionID');
});

```

**Pontos-chave**

- `sheets` array com propriedades `name` e `data`
- Folhas de acesso pelo nome
- Cada folha tem seus próprios cabeçalhos e dados
- Iteração à folha de segurança

### Exemplo 3: Extração de Texto PDF

**Contexto**: Validar relatório PDF contém conteúdo esperado.

**Implementation**:

```typescript
import { readPDF } from '@seontechnologies/playwright-utils/file-utils';

test('should validate PDF report', async () => {
  const downloadPath = await handleDownload({
    page,
    downloadDir: DOWNLOAD_DIR,
    trigger: () => page.click('[data-testid="download-report"]'),
  });

  const { content } = await readPDF({ filePath: downloadPath });

  // content.text is extracted text from all pages
  expect(content.text).toContain('Financial Report Q4 2024');
  expect(content.text).toContain('Total Revenue:');

  // Validate page count
  expect(content.numpages).toBeGreaterThan(10);
});

```

**Pontos-chave**

- `content.text` contém todo o texto extraído
- `content.numpages` para contagem de páginas
- PDF analisa documentos de várias páginas
- Procure frases específicas

### Exemplo 4: Validação do arquivo ZIP

**Contexto**: Validar ZIP contém arquivos esperados e extrair arquivo específico.

**Implementation**:

```typescript
import { readZIP } from '@seontechnologies/playwright-utils/file-utils';

test('should validate ZIP archive', async () => {
  const downloadPath = await handleDownload({
    page,
    downloadDir: DOWNLOAD_DIR,
    trigger: () => page.click('[data-testid="download-backup"]'),
  });

  const { content } = await readZIP({ filePath: downloadPath });

  // Check file list
  expect(content.files).toContain('data.csv');
  expect(content.files).toContain('config.json');
  expect(content.files).toContain('readme.txt');

  // Read specific file from archive
  const configContent = content.zip.readAsText('config.json');
  const config = JSON.parse(configContent);

  expect(config.version).toBe('2.0');
});

```

**Pontos-chave**

- `content.files` lista todos os arquivos no arquivo
- `content.zip.readAsText()` extrai arquivos específicos
- Validar arquivo s