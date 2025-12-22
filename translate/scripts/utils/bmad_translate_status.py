#!/usr/bin/env python3
"""
BMAD Translate Status - Visualização de status do projeto
"""

import sys
from pathlib import Path

# Adicionar diretório utils ao path
sys.path.insert(0, str(Path(__file__).parent))

from state_manager import StateManager
from datetime import datetime

def format_duration(iso_timestamp: str) -> str:
    """Formata duração desde timestamp"""
    dt = datetime.fromisoformat(iso_timestamp)
    delta = datetime.now() - dt
    
    hours = int(delta.total_seconds() // 3600)
    minutes = int((delta.total_seconds() % 3600) // 60)
    
    if hours > 0:
        return f"há {hours}h{minutes}m"
    else:
        return f"há {minutes}m"

def print_status():
    """Imprime status visual"""
    state = StateManager()
    report = state.get_status_report()
    
    # Cabeçalho
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║         BMAD Translation Project - Status Report             ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()
    
    # Progresso Geral
    print("📊 Progresso Geral")
    progress = report['progress_percentage']
    bar_length = 40
    filled = int(bar_length * progress / 100)
    bar = "█" * filled + "░" * (bar_length - filled)
    
    print(f"  [{bar}] {progress:.1f}%")
    print(f"  ✅ Processados: {report['processed_files']}/{report['total_files']}")
    print(f"  ⏳ Pendentes: {report['pending_files']}")
    print()
    
    # Última Validação
    validation = state.state.get("validation_results", {})
    if validation:
        print("🔍 Última Validação")
        last_val = validation.get("last_validation", "Nunca")
        if last_val != "Nunca":
            print(f"  ⏰ Executada: {format_duration(last_val)}")
        else:
            print(f"  ⏰ Executada: {last_val}")
        
        status = "✅ PASSOU" if validation.get("passed") else "❌ FALHOU"
        print(f"  {status}")
        print(f"  📋 Issues: {validation.get('issues_found', 0)}")
        print()
    
    # Últimas Execuções
    recent = report.get('recent_executions', [])
    if recent:
        print("🔧 Últimas Execuções (24h)")
        for exec_info in recent[:5]:
            script = exec_info['script']
            last_run = format_duration(exec_info['last_run'])
            files = exec_info['files_affected']
            print(f"  {script:30s} → {last_run:15s} ({files} arquivos)")
        print()
    
    # Cache
    cache_dir = Path("translate/data/cache")
    if cache_dir.exists():
        cache_files = list(cache_dir.glob("*"))
        print("💾 Cache")
        print(f"  📦 Entradas: {len(cache_files)}")
        print()
    
    # Avisos
    warnings = []
    
    # Verificar arquivos não processados
    if report['pending_files'] > 0:
        warnings.append(f"{report['pending_files']} arquivos pendentes de processamento")
    
    # Verificar validação antiga
    if validation and validation.get("last_validation"):
        last_val_dt = datetime.fromisoformat(validation["last_validation"])
        hours_since = (datetime.now() - last_val_dt).total_seconds() / 3600
        if hours_since > 24:
            warnings.append("Validação não executada há mais de 24h")
    
    if warnings:
        print("⚠️  Avisos")
        for warning in warnings:
            print(f"  • {warning}")
        print()
    else:
        print("✅ Nenhum aviso")
        print()
    
    # Próximas Ações
    print("📝 Próximas Ações Sugeridas")
    
    actions = []
    
    if report['pending_files'] > 0:
        actions.append("Processar arquivos pendentes: ./scripts/correction/pipelines/03_fix.sh")
    
    if not validation or (validation and not validation.get("passed")):
        actions.append("Executar validação: ./scripts/validation/01_validate_structure.sh")
    
    if not recent:
        actions.append("Executar análise: ./scripts/analysis/analyze_translations.py stats")
    
    if not actions:
        actions.append("Tudo em dia! ✨")
    
    for i, action in enumerate(actions, 1):
        print(f"  {i}. {action}")

if __name__ == "__main__":
    print_status()
