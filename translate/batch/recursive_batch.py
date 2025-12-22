#!/usr/bin/env python3
"""
Batch Tradutor Recursivo
Traduz todos os MD em uma árvore de diretórios
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from bmad_translate.core.translator import BMADTranslator

def translate_tree(base_dir: str, protect: bool = True):
    """Traduz recursivamente todos os MD"""
    
    base_path = Path(base_dir)
    files = sorted([
        f for f in base_path.rglob("*.md") 
        if not f.name.endswith("_pt-br.md")
    ])
    
    if not files:
        print("❌ Nenhum arquivo encontrado")
        return 1
    
    print("="*70)
    print(f"TRADUÇÃO RECURSIVA - {base_dir}")
    print("="*70)
    print(f"\nArquivos: {len(files)}")
    print(f"Proteções: ✅ ATIVAS")
    print(f"Tempo estimado: ~{len(files) * 7}s (~{len(files) * 7 / 60:.1f} min)\n")
    
    # Mostra primeiros arquivos
    for i, f in enumerate(files[:10], 1):
        rel_path = f.relative_to(base_path)
        print(f"  {i}. {rel_path}")
    if len(files) > 10:
        print(f"  ... e mais {len(files) - 10} arquivos")
    
    response = input("\nContinuar? (s/n): ")
    if response.lower() != 's':
        print("❌ Cancelado")
        return 1
    
    translator = BMADTranslator()
    success_count = 0
    failed_count = 0
    total_time = 0
    
    print()
    for i, file_path in enumerate(files, 1):
        rel_path = file_path.relative_to(base_path)
        print(f"[{i}/{len(files)}] {rel_path}...", end=' ')
        
        start = time.time()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            translated = translator._translate_text(content, protect=protect)
            
            output_path = file_path.parent / f"{file_path.stem}_pt-br{file_path.suffix}"
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(translated)
            
            elapsed = time.time() - start
            total_time += elapsed
            success_count += 1
            
            print(f"✅ {elapsed:.1f}s")
            
        except Exception as e:
            print(f"❌ {e}")
            failed_count += 1
        
        time.sleep(0.3)
    
    # Relatório
    print(f"\n\n{'='*70}")
    print("RELATÓRIO FINAL RECURSIVO")
    print(f"{'='*70}")
    print(f"✅ Sucesso: {success_count}/{len(files)}")
    print(f"❌ Falhas: {failed_count}/{len(files)}")
    print(f"⏱️  Tempo: {total_time:.1f}s ({total_time/60:.1f} min)")
    print(f"⚡ Média: {total_time/len(files):.1f}s/arquivo")
    
    if success_count == len(files):
        print(f"\n🎉 TODOS OS {len(files)} ARQUIVOS TRADUZIDOS!")
    
    return 0 if failed_count == 0 else 1

if __name__ == "__main__":
    base_dir = Path(__file__).parent.parent.parent / "_bmad/bmm/workflows"
    sys.exit(translate_tree(str(base_dir), protect=True))
