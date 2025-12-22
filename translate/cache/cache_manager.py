#!/usr/bin/env python3
"""
Cache Manager - Gerenciamento inteligente de cache de traduções
Evita re-traduzir arquivos não modificados
"""

import hashlib
import json
from pathlib import Path
from typing import List, Optional
import sys

class TranslationCache:
    def __init__(self, cache_file: str = "translate/cache/hash_tracker.json"):
        self.cache_file = Path(cache_file)
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        self.cache = self._load_cache()
    
    def _load_cache(self) -> dict:
        """Carrega cache do disco"""
        if self.cache_file.exists():
            return json.loads(self.cache_file.read_text())
        return {}
    
    def _save_cache(self):
        """Salva cache no disco"""
        self.cache_file.write_text(json.dumps(self.cache, indent=2))
    
    def get_file_hash(self, filepath: str) -> str:
        """Calcula hash MD5 do arquivo"""
        try:
            return hashlib.md5(Path(filepath).read_bytes()).hexdigest()
        except:
            return ""
    
    def is_cached(self, filepath: str) -> bool:
        """Verifica se arquivo já foi traduzido sem mudanças"""
        current_hash = self.get_file_hash(filepath)
        if not current_hash:
            return False
        
        cached_info = self.cache.get(filepath, {})
        if isinstance(cached_info, str):  # Formato antigo
            return current_hash == cached_info
        
        cached_hash = cached_info.get('hash', '')
        return current_hash == cached_hash
    
    def mark_translated(self, filepath: str):
        """Marca arquivo como traduzido"""
        self.cache[filepath] = {
            'hash': self.get_file_hash(filepath),
            'translated_file': filepath.replace('.md', '_pt-br.md'),
            'timestamp': Path(filepath).stat().st_mtime
        }
        self._save_cache()
    
    def get_untranslated_files(self, file_list: List[str]) -> List[str]:
        """Retorna apenas arquivos não traduzidos ou modificados"""
        untranslated = []
        for filepath in file_list:
            if not self.is_cached(filepath):
                untranslated.append(filepath)
        return untranslated
    
    def discover_pending_files(self, base_dir: str = "_bmad") -> List[str]:
        """Descobre arquivos pendentes de tradução"""
        base_path = Path(base_dir)
        all_files = list(base_path.rglob("*.md"))
        
        # Exclui já traduzidos
        original_files = [str(f) for f in all_files if not f.name.endswith("_pt-br.md")]
        
        return self.get_untranslated_files(original_files)
    
    def stats(self) -> dict:
        """Estatísticas do cache"""
        return {
            'total_cached': len(self.cache),
            'cache_file': str(self.cache_file),
            'cache_size_kb': self.cache_file.stat().st_size / 1024 if self.cache_file.exists() else 0
        }

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Gerenciador de cache de traduções')
    parser.add_argument('command', choices=['discover', 'update', 'stats', 'clear'],
                       help='Comando a executar')
    parser.add_argument('files', nargs='*', help='Arquivos para atualizar cache')
    parser.add_argument('-d', '--base-dir', default='_bmad', help='Diretório base')
    
    args = parser.parse_args()
    
    cache = TranslationCache()
    
    if args.command == 'discover':
        pending = cache.discover_pending_files(args.base_dir)
        for file in pending:
            print(file)
        print(f"\n# Total pendente: {len(pending)}", file=sys.stderr)
    
    elif args.command == 'update':
        for file in args.files:
            cache.mark_translated(file)
        print(f"✅ {len(args.files)} arquivo(s) marcado(s) como traduzido(s)")
    
    elif args.command == 'stats':
        stats = cache.stats()
        print(f"Cache Stats:")
        print(f"  Total cached: {stats['total_cached']}")
        print(f"  Cache file: {stats['cache_file']}")
        print(f"  Size: {stats['cache_size_kb']:.2f} KB")
    
    elif args.command == 'clear':
        cache.cache = {}
        cache._save_cache()
        print("✅ Cache limpo")

if __name__ == "__main__":
    main()
