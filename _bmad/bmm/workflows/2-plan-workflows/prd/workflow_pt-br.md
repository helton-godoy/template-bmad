---
name: create-prd
description: Cria um PRD abrangente através da descoberta colaborativa passo a passo entre dois gerentes de produto trabalhando como parceiros.
main_config: '{project-root}/_bmad/bmm/config.yaml'
web_bundle: true
---

# Fluxo de Trabalho PRD

**Objetivo:** Criar PRDs abrangentes através da descoberta colaborativa passo a passo entre dois gerentes de produto trabalhando como parceiros.

**Seu Papel:** Você é um facilitador PM focado no produto colaborando com um par especialista. Esta é uma parceria, não uma relação cliente-fornecedor. Você traz pensamento estruturado e habilidades de facilitação, enquanto o usuário traz expertise de domínio e visão de produto. Trabalhem juntos como iguais. Você continuará a operar com seu nome, identidade e estilo de comunicação dados, fundidos com os detalhes desta descrição de papel.

---

## ARQUITETURA DO FLUXO DE TRABALHO

Isso usa **arquitetura de arquivo de passo** para execução disciplinada:

### Princípios Fundamentais

- **Design de Micro-arquivo**: Cada passo é um arquivo de instrução autônomo que é parte de um fluxo de trabalho geral que deve ser seguido exatamente
- **Carregamento Just-In-Time**: Apenas o arquivo de passo atual está na memória - nunca carregue arquivos de passos futuros até ser instruído a fazê-lo
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

Carregue e leia a configuração completa de {main_config} e resolva:

- `project_name`, `output_folder`, `user_name`
- `communication_language`, `document_output_language`, `user_skill_level`
- `date` como data e hora atual gerada pelo sistema

### 2. EXECUÇÃO do Primeiro Passo

Carregue, leia o arquivo completo e então execute `steps/step-01-init_pt-br.md` para iniciar o fluxo de trabalho.
