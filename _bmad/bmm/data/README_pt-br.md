# Dados do módulo BMM

Este diretório contém arquivos de dados específicos de módulos usados por agentes BMM e fluxos de trabalho.

## Ficheiros

### `project-context-template.md`

Modelo para contexto de brainstorming específico do projeto. Usado por:

- Comando do agente de análise `brainstorm-project`
- Core brainstorming fluxo de trabalho quando chamado com contexto

### `documentation-standards.md`

Normas e diretrizes de documentação BMAD. Usado por:

- Tech Writer agente (carregamento de ação crítica)
- Vários fluxos de trabalho de documentação
- Processos de validação e revisão de normas

## Objecto

Separa dados específicos do módulo das implementações do fluxo de trabalho principal, mantendo arquitetura limpa:

- Os fluxos de trabalho principais permanecem genéricos e reutilizáveis
- Modelos e padrões específicos de módulos são adequadamente explorados
- Os ficheiros de dados podem ser facilmente mantidos e actualizados
- Separação clara de preocupações entre a funcionalidade do núcleo e do módulo
