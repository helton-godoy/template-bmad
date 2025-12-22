# Sprint Planning Lista de Verificação de Validação

## Validação Principal

### Verificação completa da cobertura

- [ ] Cada épico encontrado em arquivos épicos\*.md aparece no sprint-status.yaml
- [ ] Cada história encontrada em arquivos épicos\*.md aparece no sprint-status.yaml
- [ ] Cada épico tem uma entrada retrospectiva correspondente
- [ ] Nenhum item no sprint-status.yaml que não exista em arquivos épicos

### Verificação de análise

Compare arquivos épicos com o sprint-status.yaml gerado:

```
Epic Files Contains:                Sprint Status Contains:
✓ Epic 1                            ✓ epic-1: [status]
  ✓ Story 1.1: User Auth              ✓ 1-1-user-auth: [status]
  ✓ Story 1.2: Account Mgmt           ✓ 1-2-account-mgmt: [status]
  ✓ Story 1.3: Plant Naming           ✓ 1-3-plant-naming: [status]
                                      ✓ epic-1-retrospective: [status]
✓ Epic 2                            ✓ epic-2: [status]
  ✓ Story 2.1: Personality Model      ✓ 2-1-personality-model: [status]
  ✓ Story 2.2: Chat Interface         ✓ 2-2-chat-interface: [status]
                                      ✓ epic-2-retrospective: [status]

```

### Verificação final

- [ ] Número total de jogos épicos
- [ ] Total de correspondências de histórias
- [ ] Todos os itens estão na ordem esperada (epic, histórias, retrospectiva)
