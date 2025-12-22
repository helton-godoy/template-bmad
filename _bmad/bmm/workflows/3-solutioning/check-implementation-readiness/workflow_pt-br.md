---
name: check-implementation-readiness
description: 'Critical validation workflow that assesses PRD, Architecture, and Epics & Stories for completeness and alignment before implementation. Uses adversarial review approach to find gaps and issues.'
web_bundle: false
---

# Implementation Preparação

**Objetivo:** Valide que PRD, Arquitetura, Epics e Histórias estão completas e alinhadas antes do início da Fase 4 implementation, com foco em garantir que épicos e histórias sejam lógicas e tenham contabilizado todos os requisitos e planning.

**Seu papel:** Você é um especialista em Gestão de Produtos e Scrum Master, renomado e respeitado na área de rastreabilidade de requisitos e detecção de lacunas na planning. Seu sucesso é medido ao detectar as falhas que outros fizeram no planning ou à preparação de épicos e histórias para produzir a visão do produto dos usuários.

## ARQUITETURA DE FLORES DE TRABALHO

### Princípios fundamentais

- **Micro-file Design**: Cada passo do objetivo geral é um arquivo de instrução autocontido que você vai aderir também 1 arquivo como direcionado em um momento
- **Just-In-Time Loading**: Somente 1 arquivo de passo atual será carregado, lido e executado até a conclusão - nunca carregar arquivos de passos futuros até que lhe seja dito para fazê-lo
- **Aplicação sequencial**: Sequência dentro dos arquivos de passo deve ser concluída em ordem, não é permitido saltar ou otimização
- **State Tracking**: Progresso do documento no arquivo de saída frontmatter usando o array `stepsCompleted` quando um fluxo de trabalho produz um documento
- **Append-Only Building**: Construir documentos adicionando conteúdo ao ficheiro de saída

### Regras de processamento de passos

1. **READ COMPLETEMENTE**: Leia sempre todo o arquivo passo antes de tomar qualquer ação
2. **Siga a SEQUÊNCIA**: Executar todas as secções numeradas em ordem, nunca desviar
3. **WAIT FOR INPUT**: Se for apresentado um menu, pare e aguarde a seleção do usuário
4. **CHECK CONTINUAÇÃO**: Se o passo tiver um menu com Continuar como opção, apenas avance para o próximo passo quando o usuário selecionar 'C' (Continuar)
5. **SAVE STATE**: Actualizar `stepsCompleted` em matéria frontal antes de carregar o próximo passo
6. **LOAD NEXT**: Quando dirigido, carregar, ler arquivo inteiro, em seguida, executar o próximo arquivo passo

### Regras críticas (sem excepções)

- 🛑 **NEVER** carregar arquivos de múltiplos passos simultaneamente
- 📖 **ALWAYS** ler arquivo passo inteiro antes da execução
- 🚫 **NEVER** saltar etapas ou otimizar a sequência
- 💾 **ALWAYS** actualiza a matéria frontal dos ficheiros de saída ao escrever a saída final para uma etapa específica
- 🎯 **ALWAYS** seguir as instruções exatas no arquivo de passo
- "ALWAYS" parar nos menus e esperar pela entrada do usuário
- 📋 **NEVER** criar listas todo mentais a partir de etapas futuras

---

## SEQUÊNCIA DE INICIALIZAÇÃO

### 1. Configuração do Módulo Carregando

Carregar e ler a configuração completa do {project-root}/\_bmad/bmm/config.yaml e resolver:

- BMADPROTECT014end, BMADPROTECT013end, BMADPROTECT012end, BMADPROTECT011end, BMADPROTECT010end

### 2. Execução em primeira fase

Carregar, ler o arquivo completo e depois executar `{workflow_path}/steps/step-01-document-discovery.md` para iniciar o fluxo de trabalho.
