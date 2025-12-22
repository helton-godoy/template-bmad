.PHONY: help status install clean test validate analyze fix pipeline docs

# Configurações
PYTHON := python3
SCRIPTS_DIR := translate/scripts
CONFIG_DIR := translate/config
DATA_DIR := translate/data

# Cores para output
GREEN := \033[0;32m
YELLOW := \033[1;33m
RED := \033[0;31m
NC := \033[0m # No Color

##@ Geral

help: ## Mostra esta mensagem de ajuda
	@echo "╔══════════════════════════════════════════════════════════════╗"
	@echo "║         BMAD Translation - Comandos Disponíveis              ║"
	@echo "╚══════════════════════════════════════════════════════════════╝"
	@echo ""
	@awk 'BEGIN {FS = ":.*##"; printf "\nUso:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

status: ## Mostra status do projeto de tradução
	@echo "$(GREEN)📊 Status do Projeto$(NC)"
	@$(PYTHON) $(SCRIPTS_DIR)/utils/bmad_translate_status.py

##@ Instalação e Configuração

install: ## Instala dependências e configura ambiente
	@echo "$(GREEN)📦 Instalando dependências...$(NC)"
	@$(PYTHON) $(SCRIPTS_DIR)/validation/00_validate_installation.py
	@echo "$(GREEN)✅ Instalação concluída$(NC)"

env: ## Carrega variáveis de ambiente
	@echo "$(GREEN)⚙️  Carregando variáveis de ambiente...$(NC)"
	@bash -c "source $(CONFIG_DIR)/environment_vars.sh && env | grep BMAD_"

warmup: ## Aquece modelos de tradução
	@echo "$(GREEN)🔥 Aquecendo modelos...$(NC)"
	@$(PYTHON) $(SCRIPTS_DIR)/utils/model_management.py

##@ Validação

validate: ## Executa validação completa
	@echo "$(GREEN)🔍 Executando validação...$(NC)"
	@$(PYTHON) $(SCRIPTS_DIR)/validation/02_validate_translations.py

validate-install: ## Valida instalação de dependências
	@echo "$(GREEN)🔍 Validando instalação...$(NC)"
	@$(PYTHON) $(SCRIPTS_DIR)/validation/00_validate_installation.py

##@ Análise

analyze: ## Analisa traduções (estatísticas)
	@echo "$(GREEN)📊 Analisando traduções...$(NC)"
	@$(PYTHON) $(SCRIPTS_DIR)/analysis/analyze_translations.py stats

analyze-report: ## Gera relatório completo de análise
	@echo "$(GREEN)📄 Gerando relatório...$(NC)"
	@$(PYTHON) $(SCRIPTS_DIR)/analysis/analyze_translations.py report -o $(DATA_DIR)/reports/analysis_report.md
	@echo "$(GREEN)✅ Relatório salvo em: $(DATA_DIR)/reports/analysis_report.md$(NC)"

analyze-csv: ## Gera CSV de pares de tradução
	@echo "$(GREEN)📊 Gerando CSV...$(NC)"
	@$(PYTHON) $(SCRIPTS_DIR)/analysis/analyze_translations.py csv -o $(DATA_DIR)/reports/translation_pairs.csv
	@echo "$(GREEN)✅ CSV salvo em: $(DATA_DIR)/reports/translation_pairs.csv$(NC)"

unprocessed: ## Lista arquivos não processados
	@echo "$(GREEN)📋 Arquivos não processados:$(NC)"
	@$(PYTHON) $(SCRIPTS_DIR)/utils/state_manager.py unprocessed

##@ Correção

fix: ## Executa correções automáticas (apenas arquivos não processados)
	@echo "$(YELLOW)⚠️  Correções automáticas ainda não implementadas$(NC)"
	@echo "$(YELLOW)   Aguarde implementação dos scripts em correction/auto/$(NC)"

fix-all: ## Força correção de todos os arquivos
	@echo "$(YELLOW)⚠️  Correções automáticas ainda não implementadas$(NC)"

##@ Pipelines

pipeline: ## Executa pipeline completo de correção
	@echo "$(YELLOW)⚠️  Pipeline completo ainda não implementado$(NC)"
	@echo "$(YELLOW)   Aguarde implementação em correction/pipelines/pipeline_full.sh$(NC)"

pipeline-dry: ## Executa pipeline em modo dry-run (sem modificar arquivos)
	@echo "$(YELLOW)⚠️  Pipeline ainda não implementado$(NC)"

##@ Estado e Cache

state-reset: ## Reseta estado (use com cuidado!)
	@echo "$(RED)⚠️  ATENÇÃO: Isso vai resetar todo o estado!$(NC)"
	@read -p "Tem certeza? [y/N] " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		rm -f $(DATA_DIR)/state/execution_state.json; \
		echo "$(GREEN)✅ Estado resetado$(NC)"; \
	else \
		echo "$(YELLOW)❌ Operação cancelada$(NC)"; \
	fi

cache-clean: ## Limpa cache antigo (>24h)
	@echo "$(GREEN)🧹 Limpando cache antigo...$(NC)"
	@find $(DATA_DIR)/cache -type f -mtime +1 -delete 2>/dev/null || true
	@echo "$(GREEN)✅ Cache limpo$(NC)"

locks-clean: ## Limpa locks órfãos
	@echo "$(GREEN)🧹 Limpando locks órfãos...$(NC)"
	@bash -c "source $(SCRIPTS_DIR)/utils/lock_system.sh && cleanup_old_locks 3600"
	@echo "$(GREEN)✅ Locks limpos$(NC)"

##@ Documentação

docs: ## Gera documentação automática
	@echo "$(GREEN)📚 Gerando documentação...$(NC)"
	@echo "$(YELLOW)⚠️  Geração automática de docs ainda não implementada$(NC)"

docs-view: ## Abre documentação principal
	@echo "$(GREEN)📖 Abrindo documentação...$(NC)"
	@cat translate/docs/README.md

##@ Testes

test: ## Executa testes de validação
	@echo "$(GREEN)🧪 Executando testes...$(NC)"
	@$(PYTHON) -m pytest tests/ -v

test-state: ## Testa sistema de estado
	@echo "$(GREEN)🧪 Testando sistema de estado...$(NC)"
	@$(PYTHON) $(SCRIPTS_DIR)/utils/state_manager.py status
	@echo "$(GREEN)✅ Sistema de estado funcionando$(NC)"

test-locks: ## Testa sistema de locks
	@echo "$(GREEN)🧪 Testando sistema de locks...$(NC)"
	@bash -c "source $(SCRIPTS_DIR)/utils/lock_system.sh && check_lock test_lock"
	@echo "$(GREEN)✅ Sistema de locks funcionando$(NC)"

##@ Limpeza

clean: ## Limpa arquivos temporários
	@echo "$(GREEN)🧹 Limpando arquivos temporários...$(NC)"
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type f -name "*~" -delete 2>/dev/null || true
	@echo "$(GREEN)✅ Limpeza concluída$(NC)"

clean-all: clean cache-clean locks-clean ## Limpeza completa (temp + cache + locks)
	@echo "$(GREEN)✅ Limpeza completa concluída$(NC)"

##@ Desenvolvimento

dev-setup: install warmup ## Setup completo para desenvolvimento
	@echo "$(GREEN)✅ Setup de desenvolvimento concluído$(NC)"

dev-status: status unprocessed ## Status detalhado para desenvolvimento
	@echo ""
	@echo "$(GREEN)📊 Cache:$(NC)"
	@ls -lh $(DATA_DIR)/cache/ 2>/dev/null || echo "  Vazio"
	@echo ""
	@echo "$(GREEN)📝 Logs recentes:$(NC)"
	@ls -lht $(DATA_DIR)/logs/ | head -5 2>/dev/null || echo "  Nenhum log"

##@ Informações

version: ## Mostra versões dos componentes
	@echo "$(GREEN)📦 Versões:$(NC)"
	@echo "  Python: $$($(PYTHON) --version)"
	@echo "  Bash: $$BASH_VERSION"
	@echo ""
	@echo "$(GREEN)📋 Scripts:$(NC)"
	@cat $(CONFIG_DIR)/script_versions.yaml | grep "version:" | head -1

info: ## Mostra informações do projeto
	@echo "╔══════════════════════════════════════════════════════════════╗"
	@echo "║              BMAD Translation Project Info                   ║"
	@echo "╚══════════════════════════════════════════════════════════════╝"
	@echo ""
	@echo "$(GREEN)📁 Estrutura:$(NC)"
	@echo "  Scripts: $$(find $(SCRIPTS_DIR) -name '*.py' -o -name '*.sh' | wc -l) arquivos"
	@echo "  Configs: $$(ls $(CONFIG_DIR) | wc -l) arquivos"
	@echo ""
	@echo "$(GREEN)📊 Estado:$(NC)"
	@$(PYTHON) $(SCRIPTS_DIR)/utils/state_manager.py status
	@echo ""
	@echo "$(GREEN)📚 Documentação:$(NC)"
	@echo "  README: translate/docs/README.md"
	@echo "  Walkthrough: .gemini/antigravity/brain/.../walkthrough.md"
