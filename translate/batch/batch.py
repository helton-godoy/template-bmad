#!/usr/bin/env python3
"""
Batch Translator - Tradução rápida com Argos + proteções
"""

import sys
import time
from pathlib import Path
from typing import List, Optional

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from bmad_translate.core.translator import BMADTranslator

class BatchTranslator:
    """Tradutor em batch usando Argos base com todas as proteções"""
    
    def __init__(self):
        self.translator = BMADTranslator()
    
    def discover_files(self, base_dir: str) -> List[Path]:
        """Descobre arquivos MD para traduzir"""
        base_path = Path(base_dir)
        return sorted([
            f for f in base_path.glob("*.md") 
            if not f.name.endswith("_pt-br.md")
        ])
    
    def translate_all(self, files: List[Path] = None, base_dir: str = None, 
                     protect: bool = True, verbose: bool = False):
        """Traduz todos os arquivos"""
        
        if files is None and base_dir:
            files = self.discover_files(base_dir)
        
        if not files:
            print("❌ Nenhum arquivo encontrado")
            return 1
        
        print("="*70)
        print("TRADUÇÃO EM BATCH - Argos com Proteções")
        print("="*70)
        print(f"\nArquivos: {len(files)}")
        print(f"Proteções: {'✅ ATIVAS' if protect else '⚠️  DESATIVADAS'}")
        print(f"Tempo estimado: ~{len(files) * 5}s (~{len(files) * 5 / 60:.1f} min)\n")
        
        for i, f in enumerate(files[:5], 1):
            print(f"  {i}. {f.name}")
        if len(files) > 5:
            print(f"  ... e mais {len(files) - 5} arquivos")
        
        response = input("\nContinuar? (s/n): ")
        if response.lower() != 's':
            print("❌ Cancelado")
            return 1
        
        success_count = 0
        failed_count = 0
        total_time = 0
        
        for i, file_path in enumerate(files, 1):
            print(f"\n{'='*70}")
            print(f"[{i}/{len(files)}] {file_path.name}")
            print(f"{'='*70}")
            
            start = time.time()
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if verbose:
                    print(f"📏 Tamanho: {len(content)} chars")
                print(f"⏳ Traduzindo...")
                
                translated = self.translator._translate_text(content, protect=protect)
                
                output_path = file_path.parent / f"{file_path.stem}_pt-br{file_path.suffix}"
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(translated)
                
                elapsed = time.time() - start
                total_time += elapsed
                
                print(f"✅ Concluído em {elapsed:.1f}s")
                print(f"💾 Salvo: {output_path.name}")
                success_count += 1
                
            except Exception as e:
                print(f"❌ Erro: {e}")
                failed_count += 1
            
            if i < len(files):
                time.sleep(0.5)
        
        # Relatório
        print(f"\n\n{'='*70}")
        print("RELATÓRIO FINAL")
        print(f"{'='*70}")
        print(f"✅ Sucesso: {success_count}/{len(files)}")
        print(f"❌ Falhas: {failed_count}/{len(files)}")
        print(f"⏱️  Tempo: {total_time:.1f}s ({total_time/60:.1f} min)")
        print(f"⚡ Média: {total_time/len(files):.1f}s/arquivo")
        
        if success_count == len(files):
            print(f"\n🎉 TODOS OS {len(files)} ARQUIVOS TRADUZIDOS!")
        
        return 0 if failed_count == 0 else 1


if __name__ == "__main__":
    translator = BatchTranslator()
    base_dir = Path(__file__).parent.parent.parent / "_bmad/bmm/docs"
    sys.exit(translator.translate_all(base_dir=str(base_dir), protect=True))


