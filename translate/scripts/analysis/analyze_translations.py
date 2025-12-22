#!/usr/bin/env python3
"""
Translation Review Helper
Identifica pares de arquivos original→traduzido para revisão manual
"""

import sys
from pathlib import Path
from typing import List, Tuple
import subprocess

class TranslationReviewer:
    """Helper para revisar traduções"""
    
    def __init__(self, base_dir: str = "_bmad"):
        self.base_dir = Path(base_dir)
        self.pairs = []
    
    def find_translation_pairs(self) -> List[Tuple[Path, Path]]:
        """Encontra todos os pares (original, traduzido)"""
        
        # Encontra todos os arquivos traduzidos
        translated_files = sorted(self.base_dir.rglob("*_pt-br.md"))
        
        for translated in translated_files:
            # Deduz o nome do arquivo original
            original_name = translated.name.replace("_pt-br.md", ".md")
            original = translated.parent / original_name
            
            if original.exists():
                self.pairs.append((original, translated))
            else:
                print(f"⚠️  Original não encontrado: {original}")
        
        return self.pairs
    
    def generate_report(self, output_file: str = None):
        """Gera relatório de pares para revisão"""
        
        if not self.pairs:
            self.find_translation_pairs()
        
        report_lines = []
        report_lines.append("# Relatório de Traduções - Pares para Revisão Manual\n")
        report_lines.append(f"**Total de pares:** {len(self.pairs)}\n")
        report_lines.append(f"**Data:** {Path(__file__).stat().st_mtime}\n\n")
        report_lines.append("---\n\n")
        
        # Agrupa por diretório
        by_directory = {}
        for original, translated in self.pairs:
            dir_name = original.parent.relative_to(self.base_dir)
            if dir_name not in by_directory:
                by_directory[dir_name] = []
            by_directory[dir_name].append((original, translated))
        
        # Gera relatório por diretório
        for dir_name in sorted(by_directory.keys()):
            report_lines.append(f"## {dir_name}\n\n")
            report_lines.append(f"**Arquivos:** {len(by_directory[dir_name])}\n\n")
            
            for original, translated in by_directory[dir_name]:
                rel_original = original
                rel_translated = translated
                
                # Tamanhos
                orig_size = original.stat().st_size
                trans_size = translated.stat().st_size
                size_diff = ((trans_size - orig_size) / orig_size * 100) if orig_size > 0 else 0
                
                report_lines.append(f"### {original.name}\n\n")
                report_lines.append(f"- **Original:** [`{rel_original}`](file:///{original.absolute()})\n")
                report_lines.append(f"- **Traduzido:** [`{rel_translated}`](file:///{translated.absolute()})\n")
                report_lines.append(f"- **Tamanho:** {orig_size:,} → {trans_size:,} bytes ({size_diff:+.1f}%)\n")
                report_lines.append(f"- **Diff:** `code --diff {rel_original} {rel_translated}`\n\n")
        
        report_lines.append("\n---\n\n")
        report_lines.append("## Scripts de Revisão Rápida\n\n")
        report_lines.append("### Abrir pares no VS Code para comparação\n\n")
        report_lines.append("```bash\n")
        report_lines.append("# Revisar todos os pares\n")
        for original, translated in self.pairs[:5]:
            report_lines.append(f"code --diff {original} {translated}\n")
        if len(self.pairs) > 5:
            report_lines.append(f"# ... e mais {len(self.pairs) - 5} pares\n")
        report_lines.append("```\n\n")
        
        # Salva ou imprime
        report_content = ''.join(report_lines)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report_content)
            print(f"✅ Relatório salvo em: {output_file}")
        else:
            print(report_content)
        
        return report_content
    
    def generate_csv(self, output_file: str = "translation_pairs.csv"):
        """Gera CSV de pares"""
        
        if not self.pairs:
            self.find_translation_pairs()
        
        import csv
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Original', 'Traduzido', 'Diretório', 'Tamanho Original', 'Tamanho Traduzido', 'Diferença %'])
            
            for original, translated in self.pairs:
                dir_name = original.parent.relative_to(self.base_dir)
                orig_size = original.stat().st_size
                trans_size = translated.stat().st_size
                size_diff = ((trans_size - orig_size) / orig_size * 100) if orig_size > 0 else 0
                
                writer.writerow([
                    str(original),
                    str(translated),
                    str(dir_name),
                    orig_size,
                    trans_size,
                    f"{size_diff:+.1f}"
                ])
        
        print(f"✅ CSV salvo em: {output_file}")
    
    def open_diff(self, index: int = 0):
        """Abre diff de um par específico no VS Code"""
        
        if not self.pairs:
            self.find_translation_pairs()
        
        if index < 0 or index >= len(self.pairs):
            print(f"❌ Índice inválido. Use 0-{len(self.pairs)-1}")
            return
        
        original, translated = self.pairs[index]
        cmd = ['code', '--diff', str(original), str(translated)]
        
        print(f"Abrindo diff: {original.name}")
        subprocess.run(cmd)
    
    def stats(self):
        """Exibe estatísticas"""
        
        if not self.pairs:
            self.find_translation_pairs()
        
        print("="*70)
        print("ESTATÍSTICAS DE TRADUÇÃO")
        print("="*70)
        print(f"Total de pares: {len(self.pairs)}")
        
        # Por diretório
        by_dir = {}
        for original, translated in self.pairs:
            dir_name = str(original.parent.relative_to(self.base_dir))
            by_dir[dir_name] = by_dir.get(dir_name, 0) + 1
        
        print(f"\nPor diretório:")
        for dir_name in sorted(by_dir.keys()):
            print(f"  {dir_name}: {by_dir[dir_name]} arquivos")
        
        # Tamanhos
        total_orig = sum(o.stat().st_size for o, _ in self.pairs)
        total_trans = sum(t.stat().st_size for _, t in self.pairs)
        avg_diff = ((total_trans - total_orig) / total_orig * 100) if total_orig > 0 else 0
        
        print(f"\nTamanho total:")
        print(f"  Original: {total_orig:,} bytes ({total_orig/1024/1024:.1f} MB)")
        print(f"  Traduzido: {total_trans:,} bytes ({total_trans/1024/1024:.1f} MB)")
        print(f"  Diferença: {avg_diff:+.1f}%")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Helper para revisão de traduções',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Exemplos:
  # Gera relatório markdown
  %(prog)s report
  
  # Gera CSV
  %(prog)s csv
  
  # Exibe estatísticas
  %(prog)s stats
  
  # Abre diff do primeiro par
  %(prog)s diff 0
  
  # Lista todos os pares
  %(prog)s list
'''
    )
    
    parser.add_argument('command', choices=['report', 'csv', 'stats', 'diff', 'list'],
                       help='Comando a executar')
    parser.add_argument('index', nargs='?', type=int, default=0,
                       help='Índice do par (para comando diff)')
    parser.add_argument('-o', '--output', help='Arquivo de saída')
    parser.add_argument('-d', '--base-dir', default='_bmad',
                       help='Diretório base (padrão: _bmad)')
    
    args = parser.parse_args()
    
    reviewer = TranslationReviewer(args.base_dir)
    
    if args.command == 'report':
        output = args.output or 'translation_review.md'
        reviewer.generate_report(output)
    
    elif args.command == 'csv':
        output = args.output or 'translation_pairs.csv'
        reviewer.generate_csv(output)
    
    elif args.command == 'stats':
        reviewer.stats()
    
    elif args.command == 'diff':
        reviewer.open_diff(args.index)
    
    elif args.command == 'list':
        pairs = reviewer.find_translation_pairs()
        print(f"Total: {len(pairs)} pares\n")
        for i, (original, translated) in enumerate(pairs):
            print(f"{i:3d}. {original.name}")
            print(f"     → {translated}")

if __name__ == "__main__":
    main()
