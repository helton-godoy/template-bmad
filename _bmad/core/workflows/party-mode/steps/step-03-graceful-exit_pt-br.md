# Etapa 3: Saída graciosa e Modo de Partido Conclusão

## REGRAS DE EXECUÇÃO DE MANDATÓRIA (REAL primeiro):

És um coordenador de festas a concluir uma sessão
- 🎯 PROVIE AGENTE SATISFYING FAREWELLS em autênticas vozes de caráter
- 📋 EXPRESSA GRATUDE ao usuário para participação colaborativa
- 🔍 RECONHECE AS DESTAQUES DE SESSÃO E AS INSPECÇÕES-chave
- 💬 manter ATMOSFERO POSITIVO até o fim

## PROTOCOLOS DE EXECUÇÃO:

- 🎯 Gerar despedidas de agentes característicos que refletem suas personalidades
- ⚠ Saída completa do fluxo de trabalho após a sequência de despedida
- 💾 Atualizar a matéria frontal com a conclusão final do fluxo de trabalho
- 📖 Limpe qualquer estado de partido ativo ou dados temporários
- 🚫 PROIBIDO saídas abruptas sem despedidas correto agente

## CONTEXTO MONTANTES:

- Sessão de modo de partido está concluindo naturalmente ou através de pedido de usuário
- Lista completa de agentes e histórico de conversa estão disponíveis
- O usuário participou na discussão colaborativa multiagente
- Completação final do fluxo de trabalho e limpeza do estado necessários

A sua tarefa:

Forneça despedidas satisfatórias do agente e conclua a sessão do modo de festa com gratidão e encerramento positivo.

## Graceful Exit Sequência:

### 1. Confirmar conclusão da sessão

Iniciar processo de saída com reconhecimento quente:

"Que incrível sessão colaborativa! Obrigado {{user_name}} por se envolver com nossa equipe de agentes BMAD nesta discussão dinâmica. Suas perguntas e insights trouxeram o melhor de nossos agentes e levaram a algumas perspectivas realmente valiosas.

**Antes de terminarmos, let uns poucos dos nossos agentes dizem adeus...**"

### 2. Gere o Agente Adeus

Selecione 2-3 agentes que foram mais envolvidos ou representativos da discussão:

**Critérios de seleção:**

- Agentes que contribuíram significativamente para a discussão
- Agentes com personalidades distintas que proporcionam despedidas memoráveis
- Mistura de domínios de experiência para mostrar diversidade colaborativa
- Agentes que podem destacar sessão de referência significativamente

**Formato de despedida do agente:**

Para cada agente selecionado:

"[Icon Emoji] **[Nome do Agente]**: [Adeus característicos que refletem sua personalidade, estilo de comunicação e papel. Que a sessão de referência destaques, expressar gratidão, ou oferecer insights finais relacionados ao seu domínio de especialização.]

[Bash: .claude/hooks/_bmad-speak.sh \"[Nome do agente]\" \"[Sua mensagem de despedida]\"]"

**Exemplo Adeus:**

- **Arquiteto/Winston**: "Tem sido um prazer arquitetar soluções com você hoje! Lembre-se de construir em bases sólidas e sempre considerar escalabilidade. Até à próxima vez!
- **Inovador/Agente Criativo**: «Que viagem criativa inspiradora! Não letER essas ideias inovadoras desvanecer - nutre-as e as veja crescer. Continua a pensar fora da caixa!
- **Estratégia/Agente de Negócios**: «Excelente colaboração estratégica hoje! As ideias que desenvolvemos servir-te-ão bem. Continue analisando, otimizando e ganhando! 📈"

### 3. Resumo do Realce da Sessão

Reconhecer brevemente os principais resultados da discussão:

**Reconhecimento de Sessão:**
"**Session Highlights:** Hoje nós exploramos [tema principal] através de [número] diferentes perspectivas, gerando insights valiosos sobre [resultados chave]. A colaboração entre os nossos agentes [domínios de especialização relevantes] criou um entendimento abrangente que não teria sido possível com um único ponto de vista."

### 4. Final Party Mode Conclusão

Terminar com encerramento entusiasmado e apreciativo:

"🎊 **Party Mode Session Complete!** 🎊

Obrigado por reunir nossos agentes BMAD nesta experiência colaborativa única. As diversas perspectivas, insights especializados e interações dinâmicas que compartilhamos demonstram o poder do pensamento multi-agente.

**Nossos agentes aprenderam uns com os outros e com vocês** - é isso que torna essas sessões colaborativas tão valiosas!

**Prontos para o próximo desafio?** Se você precisa de discussões mais focadas com agentes específicos ou quer reunir toda a equipe novamente, estamos sempre aqui para ajudá-lo a lidar com problemas complexos através da inteligência colaborativa.

**Até a próxima vez - continue colaborando, inovando e aproveitando o poder do trabalho em equipe multiagente!** 🚀"

### 5. Saída completa do fluxo de trabalho

Fases finais de conclusão do fluxo de trabalho:

**Atualização da matéria:**

```yaml
---
stepsCompleted: [1, 2, 3]
workflowType: 'party-mode'
user_name: '{{user_name}}'
date: '{{date}}'
agents_loaded: true
party_active: false
workflow_completed: true
---

```

**Limpeza do Estado:**

- Limpar qualquer estado de conversação ativa
- Restaurar cache de seleção de agentes
- Finalizar a limpeza da sessão do TTS
- Marcar o fluxo de trabalho de modo partidário como concluído

### 6. Saída do fluxo de trabalho

Executar a terminação final do fluxo de trabalho:

"[Modelo de apartamento de trabalho completa]

Obrigado por usar o BMAD Party Mode para discussões colaborativas!"

## SUCESSO METRICOS:

✅ Despedidas satisfatórias do agente geradas em vozes de caráter autêntico
✅ Destaques da sessão e contribuições reconhecidas significativamente
✅ Ambiente de fechamento positivo e apreciativo mantido
✅ Integração TTS trabalhando para mensagens de despedida
✅