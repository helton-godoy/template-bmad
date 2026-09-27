#!/usr/bin/env python3
"""
Batch Translator Multi-Directory
Traduz múltiplos diretórios em sequência
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from bmad_translate.core.translator import BMADTranslator

class MultiBatchTranslator:
    """Tradutor em batch de múltiplos diretórios"""
    
    def __init__(self):
        self.translator = BMADTranslator()
        self.stats = {
            'total_files': 0,
            'success': 0,
            'failed': 0,
            'total_time': 0
        }
    
    def translate_directory(self, directory: str, protect: bool = True):
        """Traduz todos os MD em um diretório"""
        dir_path = Path(directory)
        files = sorted([
            f for f in dir_path.glob("*.md") 
            if not f.name.endswith("_pt-br.md")
        ])
        
        if not files:
            print(f"  ℹ️  Nenhum arquivo em {directory}")
            return
        
        print(f"\n📁 {directory} ({len(files)} arquivos)")
        
        for file_path in files:
            self.stats['total_files'] += 1
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                print(f"  ⏳ {file_path.name}...", end=' ')
                start = time.time()
                
                translated = self.translator._translate_text(content, protect=protect)
                
                output_path = file_path.parent / f"{file_path.stem}_pt-br{file_path.suffix}"
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(translated)
                
                elapsed = time.time() - start
                self.stats['total_time'] += elapsed
                self.stats['success'] += 1
                
                print(f"✅ {elapsed:.1f}s")
                
            except Exception as e:
                print(f"❌ {e}")
                self.stats['failed'] += 1
    
    def translate_directories(self, directories: list):
        """Traduz lista de diretórios"""
        print("="*70)
        print("TRADUÇÃO MULTI-BATCH - Múltiplos Diretórios")
        print("="*70)
        print(f"\nDiretórios: {len(directories)}")
        print(f"Proteções: ✅ ATIVAS\n")
        
        for directory in directories:
            print(directory)
        
        response = input("\nContinuar? (s/n): ")
        if response.lower() != 's':
            print("❌ Cancelado")
            return 1
        
        print()
        for directory in directories:
            self.translate_directory(directory, protect=True)
        
        # Relatório
        print(f"\n\n{'='*70}")
        print("RELATÓRIO FINAL MULTI-BATCH")
        print(f"{'='*70}")
        print(f"📁 Diretórios processados: {len(directories)}")
        print(f"✅ Sucesso: {self.stats['success']}/{self.stats['total_files']}")
        print(f"❌ Falhas: {self.stats['failed']}/{self.stats['total_files']}")
        print(f"⏱️  Tempo: {self.stats['total_time']:.1f}s ({self.stats['total_time']/60:.1f} min)")
        if self.stats['total_files'] > 0:
            print(f"⚡ Média: {self.stats['total_time']/self.stats['total_files']:.1f}s/arquivo")
        
        if self.stats['success'] == self.stats['total_files']:
            print(f"\n🎉 TODOS OS {self.stats['total_files']} ARQUIVOS TRADUZIDOS!")
        
        return 0 if self.stats['failed'] == 0 else 1

if __name__ == "__main__":
    translator = MultiBatchTranslator()
    
    # Fase 1: BMM Agents + Data
    phase1_dirs = [
        str(Path(__file__).parent.parent.parent / "_bmad/bmm/agents"),
        str(Path(__file__).parent.parent.parent / "_bmad/bmm/data"),
    ]
    
    sys.exit(translator.translate_directories(phase1_dirs))
