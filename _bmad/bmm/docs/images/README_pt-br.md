# Manutenção do Diagrama de Fluxo de Trabalho

## Regenerando SVG de Excalidraw

Quando você editar `workflow-method-greenfield.excalidraw`, regenerar o SVG:

1. Abra <https://excalidraw.com/>
2. Carregar o arquivo `.excalidraw`
3. Clique no menu (☰) → Exportar imagem → SVG
4. **Definir "Scale" para 1x** (por omissão é 2x)
5. Clique em "Exportar"
6. Salvar como `workflow-method-greenfield.svg`
7. **Validar as alterações** (ver abaixo)
8. Commit ambos os arquivos juntos

**Importante:**

- Utilize sempre **escala 1x** para manter dimensões consistentes
- Ferramentas export automatizadas (`excalidraw-to-svg`) estão quebradas - use manual export only

## Validação Visual

Após regenerar o SVG, valide que ele renderiza corretamente:

```bash
./tools/validate-svg-changes.sh path/to/workflow-method-greenfield.svg

```

Este script:

- Verifica as dependências necessárias (Playwright, ImageMagick)
- Instala o dramaturgo localmente, se necessário (sem poluição package.json)
- Muda o SVG antigo contra o novo usando renderização precisa do navegador
- Compara pixel- a- pixel e gera uma imagem diff
- Saída de um prompt para análise visual de IA (colar em Gemini/Claude)

**Limiar**: <0,01% de diferença é aceitável (variações anti-aliasing)
