#!/usr/bin/env python3
"""
Batch Translator - Traduz apenas arquivos pendentes (com cache)
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from bmad_translate.core.translator import BMADTranslator

# Importa cache manager
sys.path.insert(0, str(Path(__file__).parent.parent))
from cache.cache_manager import TranslationCache

def translate_pending_files(base_dir="_bmad"):
    """Traduz apenas arquivos pendentes"""
    
    cache = TranslationCache()
    translator = BMADTranslator()
    
    # Descobre pendentes
    pending = cache.discover_pending_files(base_dir)
    
    if not pending:
        print("✅ Nenhum arquivo pendente!")
        return 0
    
    print("="*70)
    print("TRADUÇÃO DE ARQUIVOS PENDENTES (com cache)")
    print("="*70)
    print(f"\nArquivos pendentes: {len(pending)}")
    print(f"Tempo estimado: ~{len(pending) * 6}s (~{len(pending) * 6 / 60:.1f} min)\n")
    
    # Mostra primeiros
    for i, f in enumerate(pending[:10], 1):
        print(f"  {i}. {Path(f).name}")
    if len(pending) > 10:
        print(f"  ... e mais {len(pending) - 10} arquivos")
    
    response = input("\nContinuar? (s/n): ")
    if response.lower() != 's':
        print("❌ Cancelado")
        return 1
    
    success = 0
    failed = 0
    total_time = 0
    
    print()
    for i, filepath in enumerate(pending, 1):
        rel_path = Path(filepath).relative_to(base_dir) if base_dir in filepath else Path(filepath).name
        print(f"[{i}/{len(pending)}] {rel_path}...", end=' ')
        
        start = time.time()
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            translated = translator._translate_text(content, protect=True)
            
            output_path = filepath.replace('.md', '_pt-br.md')
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(translated)
            
            # Marca no cache
            cache.mark_translated(filepath)
            
            elapsed = time.time() - start
            total_time += elapsed
            success += 1
            
            print(f"✅ {elapsed:.1f}s")
            
        except Exception as e:
            print(f"❌ {e}")
            failed += 1
        
        time.sleep(0.3)
    
    # Relatório
    print(f"\n\n{'='*70}")
    print("RELATÓRIO FINAL")
    print(f"{'='*70}")
    print(f"✅ Sucesso: {success}/{len(pending)}")
    print(f"❌ Falhas: {failed}/{len(pending)}")
    print(f"⏱️  Tempo: {total_time:.1f}s ({total_time/60:.1f} min)")
    if len(pending) > 0:
        print(f"⚡ Média: {total_time/len(pending):.1f}s/arquivo")
    print(f"💾 Cache atualizado: {cache.stats()['total_cached']} arquivos")
    
    if success == len(pending):
        print(f"\n🎉 TODOS OS {len(pending)} ARQUIVOS TRADUZIDOS!")
    
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(translate_pending_files())
