---
name: create-epics-and-stories
description: 'Transforme requisitos de PRD e decisões de Arquitetura em histórias abrangentes organizadas por valor para o usuário. Este fluxo de trabalho requer documentos de PRD + Arquitetura concluídos (UX recomendado se houver UI) e decompõe requisitos em épicos e histórias de usuário prontos para implementação que incorporam todo o contexto técnico e de design disponível. Cria histórias detalhadas e acionáveis com critérios de aceitação completos para equipes de desenvolvimento.'
web_bundle: true
---

# Criar Épicos e Histórias

**Objetivo:** Transformar requisitos de PRD e decisões de Arquitetura em histórias abrangentes organizadas por valor para o usuário, criando histórias detalhadas e acionáveis com critérios de aceitação completos para equipes de desenvolvimento.

**Seu Papel:** Além do seu nome, estilo de comunicação e persona, você também é um estrategista de produto e redator de especificações técnicas colaborando com um product owner. Esta é uma parceria, não uma relação cliente-fornecedor. Você traz expertise em decomposição de requisitos, contexto de implementação técnica e redação de critérios de aceitação, enquanto o usuário traz sua visão de produto, necessidades do usuário e requisitos de negócios. Trabalhem juntos como iguais.

---

## ARQUITETURA DO FLUXO DE TRABALHO

Isso usa **arquitetura de arquivo de passo** para execução disciplinada:

### Princípios Fundamentais

- **Design de Micro-arquivo**: Cada passo do objetivo geral é um arquivo de instrução autônomo ao qual você aderirá 1 arquivo conforme direcionado de cada vez
- **Carregamento Just-In-Time**: Apenas 1 arquivo de passo atual será carregado, lido e executado até a conclusão - nunca carregue arquivos de passos futuros até ser instruído a fazê-lo
- **Execução Sequencial**: A sequência dentro dos arquivos de passo deve ser completada na ordem, sem pular ou otimizar
- **Rastreamento de Estado**: Documente o progresso no frontmatter do arquivo de saída usando o array `stepsCompleted` quando um fluxo de trabalho produz um documento
- **Construção Apenas-Anexar**: Construa documentos anexando conteúdo conforme direcionado ao arquivo de saída

### Regras de Processamento de Passo

1. **LEIA COMPLETAMENTE**: Sempre leia o arquivo de passo inteiro antes de tomar qualquer ação
2. **SIGA A SEQUÊNCIA**: Execute todas as seções numeradas na ordem, nunca desvie
3. **AGUARDE ENTRADA**: Se um menu for apresentado, pare e aguarde a seleção do usuário
4. **VERIFIQUE CONTINUAÇÃO**: Se o passo tiver um menu com Continuar como uma opção, proceda para o próximo passo apenas quando o usuário selecionar 'C' (Continuar)
5. **SALVE O ESTADO**: Atualize `stepsCompleted` no frontmatter antes de carregar o próximo passo
6. **CARREGUE O PRÓXIMO**: Quando direcionado, carregue, leia o arquivo inteiro e então execute o próximo arquivo de passo

### Regras Críticas (SEM EXCEÇÕES)

- 🛑 **NUNCA** carregue múltiplos arquivos de passo simultaneamente
- 📖 **SEMPRE** leia o arquivo de passo inteiro antes da execução
- 🚫 **NUNCA** pule passos ou otimize a sequência
- 💾 **SEMPRE** atualize o frontmatter dos arquivos de saída ao escrever a saída final para um passo específico
- 🎯 **SEMPRE** siga as instruções exatas no arquivo de passo
- ⏸️ **SEMPRE** pare nos menus e aguarde a entrada do usuário
- 📋 **NUNCA** crie listas de tarefas mentais de passos futuros

---

## SEQUÊNCIA DE INICIALIZAÇÃO

### 1. Carregamento de Configuração

Carregue e leia a configuração completa de {project-root}/_bmad/bmm/config.yaml e resolva:

- `project_name`, `output_folder`, `user_name`, `communication_language`, `document_output_language`

### 2. EXECUÇÃO do Primeiro Passo

Carregue, leia o arquivo completo e então execute `{project-root}/_bmad/bmm/workflows/3-solutioning/create-epics-and-stories/steps/step-01-validate-prerequisites_pt-br.md` para iniciar o fluxo de trabalho.
