#!/bin/bash
# Tradutor Paralelo - Usa GNU parallel para máxima velocidade
# Ganho: ~4x mais rápido (em CPU de 4 cores)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
BASE_DIR="${1:-_bmad}"

# Detecta número de cores
CORES=$(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 4)
MAX_JOBS=$((CORES > 1 ? CORES - 1 : 1))  # Deixa 1 core livre

echo "🚀 Tradutor Paralelo"
echo "="*70
echo "Cores disponíveis: $CORES"
echo "Jobs paralelos: $MAX_JOBS"
echo "Diretório base: $BASE_DIR"
echo ""

# Verifica se GNU parallel está instalado
if ! command -v parallel &> /dev/null; then
    echo "❌ GNU parallel não encontrado!"
    echo "Instale com: sudo apt install parallel"
    exit 1
fi

# Exporta PYTHONPATH
export PYTHONPATH="$PROJECT_ROOT/translate/src:$PYTHONPATH"

# Função para traduzir um arquivo
translate_file() {
    local file="$1"
    local output="${file%.md}_pt-br.md"
    
    # Pula se já existe (a menos que forçado)
    if [ -f "$output" ] && [ -z "$FORCE" ]; then
        echo "⏭️  ${file##*/} (já existe)"
        return 0
    fi
    
    # Traduz usando Python inline
    python3 <<EOF
import sys
sys.path.insert(0, '$PROJECT_ROOT/translate/src')
from bmad_translate.core.translator import BMADTranslator

translator = BMADTranslator()
try:
    with open('$file', 'r', encoding='utf-8') as f:
        content = f.read()
    
    translated = translator._translate_text(content, protect=True)
    
    with open('$output', 'w', encoding='utf-8') as f:
        f.write(translated)
    
    print('✅ ${file##*/}')
except Exception as e:
    print(f'❌ ${file##*/}: {e}', file=sys.stderr)
    sys.exit(1)
EOF
}

# Exporta função para parallel
export -f translate_file
export PROJECT_ROOT
export FORCE

#Descobre arquivos para traduzir
echo "📍 Descobrindo arquivos..."
FILES=$(find "$BASE_DIR" -name "*.md" ! -name "*_pt-br.md" -type f)
TOTAL=$(echo "$FILES" | wc -l)

if [ "$TOTAL" -eq 0 ]; then
    echo "✅ Nenhum arquivo para traduzir!"
    exit 0
fi

echo "📊 Total de arquivos: $TOTAL"
echo ""
echo "📍 Iniciando tradução paralela..."
echo ""

# Traduz em paralelo com barra de progresso
echo "$FILES" | parallel --bar --jobs "$MAX_JOBS" translate_file {}

echo ""
echo "🎉 Tradução paralela concluída!"
echo "📊 Total: $TOTAL arquivos"
