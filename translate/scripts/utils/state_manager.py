#!/usr/bin/env python3
"""
State Manager - Gerenciamento de estado persistente para prevenir loops
"""

import json
import hashlib
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class StateManager:
    """Gerencia estado de execuções para prevenir loops"""
    
    def __init__(self, state_file: str = "translate/data/state/execution_state.json"):
        self.state_file = Path(state_file)
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        self.state = self._load_state()
    
    def _load_state(self) -> Dict:
        """Carrega estado do arquivo"""
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"⚠️  Estado corrompido, criando novo")
                return self._create_empty_state()
        return self._create_empty_state()
    
    def _create_empty_state(self) -> Dict:
        """Cria estado vazio"""
        return {
            "version": "1.0.0",
            "last_updated": datetime.now().isoformat(),
            "files_processed": {},
            "script_executions": {},
            "validation_results": {}
        }
    
    def _save_state(self):
        """Salva estado no arquivo"""
        self.state["last_updated"] = datetime.now().isoformat()
        with open(self.state_file, 'w', encoding='utf-8') as f:
            json.dump(self.state, f, indent=2, ensure_ascii=False)
    
    def _calculate_checksum(self, file_path: Path) -> str:
        """Calcula checksum SHA256 de arquivo"""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    def is_file_processed(self, file_path: Path) -> bool:
        """Verifica se arquivo já foi processado"""
        file_str = str(file_path)
        
        if file_str not in self.state["files_processed"]:
            return False
        
        # Verificar se checksum mudou
        current_checksum = self._calculate_checksum(file_path)
        stored_checksum = self.state["files_processed"][file_str].get("checksum")
        
        return current_checksum == stored_checksum
    
    def mark_file_processed(self, file_path: Path, scripts_applied: List[str]):
        """Marca arquivo como processado"""
        file_str = str(file_path)
        checksum = self._calculate_checksum(file_path)
        
        self.state["files_processed"][file_str] = {
            "checksum": checksum,
            "processed_at": datetime.now().isoformat(),
            "status": "completed",
            "scripts_applied": scripts_applied
        }
        self._save_state()
    
    def was_script_executed_recently(self, script_name: str, hours: int = 1) -> bool:
        """Verifica se script foi executado recentemente"""
        if script_name not in self.state["script_executions"]:
            return False
        
        last_run = self.state["script_executions"][script_name].get("last_run")
        if not last_run:
            return False
        
        last_run_dt = datetime.fromisoformat(last_run)
        threshold = datetime.now() - timedelta(hours=hours)
        
        return last_run_dt > threshold
    
    def mark_script_executed(self, script_name: str, files_affected: int):
        """Marca script como executado"""
        if script_name not in self.state["script_executions"]:
            self.state["script_executions"][script_name] = {
                "run_count": 0
            }
        
        self.state["script_executions"][script_name].update({
            "last_run": datetime.now().isoformat(),
            "run_count": self.state["script_executions"][script_name]["run_count"] + 1,
            "files_affected": files_affected
        })
        self._save_state()
    
    def get_unprocessed_files(self, pattern: str = "*_pt-br.md") -> List[Path]:
        """Retorna lista de arquivos não processados"""
        base_dir = Path("_bmad")
        all_files = list(base_dir.rglob(pattern))
        
        return [f for f in all_files if not self.is_file_processed(f)]
    
    def get_status_report(self) -> Dict:
        """Gera relatório de status"""
        total_files = len(list(Path("_bmad").rglob("*_pt-br.md")))
        processed_files = len(self.state["files_processed"])
        
        return {
            "total_files": total_files,
            "processed_files": processed_files,
            "pending_files": total_files - processed_files,
            "progress_percentage": (processed_files / total_files * 100) if total_files > 0 else 0,
            "last_updated": self.state["last_updated"],
            "recent_executions": self._get_recent_executions(hours=24)
        }
    
    def _get_recent_executions(self, hours: int = 24) -> List[Dict]:
        """Retorna execuções recentes"""
        threshold = datetime.now() - timedelta(hours=hours)
        recent = []
        
        for script, data in self.state["script_executions"].items():
            last_run = data.get("last_run")
            if last_run:
                last_run_dt = datetime.fromisoformat(last_run)
                if last_run_dt > threshold:
                    recent.append({
                        "script": script,
                        "last_run": last_run,
                        "files_affected": data.get("files_affected", 0)
                    })
        
        return sorted(recent, key=lambda x: x["last_run"], reverse=True)

# Uso em scripts
if __name__ == "__main__":
    import sys
    
    state = StateManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "status":
            report = state.get_status_report()
            print(f"📊 Progresso: {report['processed_files']}/{report['total_files']} ({report['progress_percentage']:.1f}%)")
            print(f"⏰ Última atualização: {report['last_updated']}")
            
        elif command == "unprocessed":
            files = state.get_unprocessed_files()
            print(f"📋 Arquivos não processados: {len(files)}")
            for f in files[:10]:
                print(f"  - {f}")
            if len(files) > 10:
                print(f"  ... e mais {len(files) - 10} arquivos")
