#!/bin/bash
# Lock System - Previne execuções simultâneas

LOCK_DIR="/tmp/bmad_translate_locks"
mkdir -p "$LOCK_DIR"

acquire_lock() {
    local lock_name="${1:-default}"
    local lock_file="$LOCK_DIR/${lock_name}.lock"
    local timeout="${2:-300}"  # 5 minutos padrão
    
    # Verificar se lock existe
    if [ -f "$lock_file" ]; then
        local existing_pid=$(cat "$lock_file")
        
        # Verificar se processo ainda está ativo
        if kill -0 "$existing_pid" 2>/dev/null; then
            # Verificar idade do lock
            local lock_age=$(($(date +%s) - $(stat -c %Y "$lock_file")))
            
            if [ $lock_age -gt $timeout ]; then
                echo "⚠️  Lock órfão detectado (idade: ${lock_age}s), removendo..."
                rm -f "$lock_file"
            else
                echo "❌ Operação '$lock_name' já em execução (PID: $existing_pid)"
                echo "   Aguarde ou use --force para forçar"
                return 1
            fi
        else
            echo "🧹 Limpando lock órfão (processo $existing_pid não existe)"
            rm -f "$lock_file"
        fi
    fi
    
    # Criar lock
    echo $$ > "$lock_file"
    echo "🔒 Lock adquirido: $lock_name (PID: $$)"
    
    # Configurar limpeza automática
    trap "release_lock '$lock_name'" EXIT INT TERM
    
    return 0
}

release_lock() {
    local lock_name="${1:-default}"
    local lock_file="$LOCK_DIR/${lock_name}.lock"
    
    if [ -f "$lock_file" ]; then
        local lock_pid=$(cat "$lock_file")
        if [ "$lock_pid" = "$$" ]; then
            rm -f "$lock_file"
            echo "🔓 Lock liberado: $lock_name"
        fi
    fi
}

check_lock() {
    local lock_name="${1:-default}"
    local lock_file="$LOCK_DIR/${lock_name}.lock"
    
    if [ -f "$lock_file" ]; then
        local existing_pid=$(cat "$lock_file")
        if kill -0 "$existing_pid" 2>/dev/null; then
            echo "🔒 Lock ativo: $lock_name (PID: $existing_pid)"
            return 0
        else
            echo "🔓 Lock inativo: $lock_name"
            return 1
        fi
    else
        echo "🔓 Sem lock: $lock_name"
        return 1
    fi
}

# Limpeza de locks antigos
cleanup_old_locks() {
    local max_age="${1:-3600}"  # 1 hora padrão
    
    echo "🧹 Limpando locks antigos (> ${max_age}s)..."
    
    find "$LOCK_DIR" -name "*.lock" -type f 2>/dev/null | while read lock_file; do
        local lock_age=$(($(date +%s) - $(stat -c %Y "$lock_file")))
        
        if [ $lock_age -gt $max_age ]; then
            local lock_pid=$(cat "$lock_file" 2>/dev/null)
            if ! kill -0 "$lock_pid" 2>/dev/null; then
                echo "  Removendo: $(basename "$lock_file") (idade: ${lock_age}s, PID morto: $lock_pid)"
                rm -f "$lock_file"
            fi
        fi
    done
}

# Exportar funções
export -f acquire_lock
export -f release_lock
export -f check_lock
export -f cleanup_old_locks
