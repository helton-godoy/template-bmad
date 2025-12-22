#!/bin/bash
# Environment Variables - Configurações globais

# Diretórios
export BMAD_TRANSLATE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export BMAD_SCRIPTS_DIR="$BMAD_TRANSLATE_ROOT/scripts"
export BMAD_DATA_DIR="$BMAD_TRANSLATE_ROOT/data"
export BMAD_CONFIG_DIR="$BMAD_TRANSLATE_ROOT/config"

# Estado
export BMAD_STATE_FILE="$BMAD_DATA_DIR/state/execution_state.json"
export BMAD_CACHE_DIR="$BMAD_DATA_DIR/cache"
export BMAD_LOGS_DIR="$BMAD_DATA_DIR/logs"
export BMAD_REPORTS_DIR="$BMAD_DATA_DIR/reports"

# Locks
export BMAD_LOCK_DIR="/tmp/bmad_translate_locks"
export BMAD_LOCK_TIMEOUT=300  # 5 minutos

# Cache
export BMAD_CACHE_MAX_AGE=86400  # 24 horas

# Tradução
export BMAD_SOURCE_LANG="en"
export BMAD_TARGET_LANG="pt"
export BMAD_TRANSLATE_PATTERN="*_pt-br.md"

# Validação
export BMAD_VALIDATION_TIMEOUT=3600  # 1 hora

# Logging
export BMAD_LOG_LEVEL="INFO"
export BMAD_LOG_FORMAT="[%(asctime)s] %(levelname)s: %(message)s"

# Python
export PYTHONPATH="$BMAD_SCRIPTS_DIR:$PYTHONPATH"

echo "✅ Variáveis de ambiente BMAD carregadas"
