#!/usr/bin/env python3
"""
Validation Tool - Detecta problemas em arquivos traduzidos
Identifica: tags malformadas, linhas truncadas, estruturas quebradas
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

class TranslationValidator:
    """Validador de traduções com detecção de problemas comuns"""
    
    def __init__(self):
        self.issues = []
        self.checks = {
            'truncated_lines': self.check_truncated_lines,
            'broken_tags': self.check_broken_tags,
            'incomplete_links': self.check_incomplete_links,
            'unmatched_brackets': self.check_unmatched_brackets,
            'broken_code_blocks': self.check_broken_code_blocks,
        }
    
    def check_truncated_lines(self, filepath: str, content: str) -> List[Dict]:
        """Detecta linhas que parecem truncadas"""
        issues = []
        lines = content.split('\n')
        
        # Padrões suspeitos de truncamento
        truncation_patterns = [
            (r'\(Usar$', 'Linha termina com "(Usar" - provavelmente truncada'),
            (r'<item[^>]*\)$', 'Tag <item> parece incompleta'),
            (r'<[^>]*$', 'Tag XML/HTML incompleta no final da linha'),
            (r'\[[^\]]*$', 'Link Markdown incompleto'),
            (r'\*\*[^*]*$', 'Negrito não fechado no final da linha'),
        ]
        
        for i, line in enumerate(lines, 1):
            for pattern, message in truncation_patterns:
                if re.search(pattern, line.strip()):
                    issues.append({
                        'file': filepath,
                        'line': i,
                        'type': 'truncated_line',
                        'severity': 'high',
                        'message': message,
                        'content': line.strip()[:100]
                    })
        
        return issues
    
    def check_broken_tags(self, filepath: str, content: str) -> List[Dict]:
        """Detecta tags XML/HTML mal formadas"""
        issues = []
        lines = content.split('\n')
        
        # Padrão para tags incompletas
        incomplete_tag_pattern = r'<(\w+)[^>]*(?<![/>])$'
        
        for i, line in enumerate(lines, 1):
            # Tag que não fecha
            if re.search(incomplete_tag_pattern, line):
                issues.append({
                    'file': filepath,
                    'line': i,
                    'type': 'broken_tag',
                    'severity': 'high',
                    'message': 'Tag XML/HTML não fechada corretamente',
                    'content': line.strip()[:100]
                })
            
            # Tag <item> sem fechamento >
            if '<item' in line and not '>' in line.split('<item')[-1]:
                issues.append({
                    'file': filepath,
                    'line': i,
                    'type': 'broken_item_tag',
                    'severity': 'critical',
                    'message': 'Tag <item> sem fechamento >',
                    'content': line.strip()[:100]
                })
        
        return issues
    
    def check_incomplete_links(self, filepath: str, content: str) -> List[Dict]:
        """Detecta links Markdown incompletos"""
        issues = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Link sem fechamento
            if re.search(r'\[([^\]]+)$', line):
                issues.append({
                    'file': filepath,
                    'line': i,
                    'type': 'incomplete_link',
                    'severity': 'medium',
                    'message': 'Link Markdown sem fechamento ]',
                    'content': line.strip()[:100]
                })
            
            # Link sem URL
            if re.search(r'\]\s*$', line) and '[' in line:
                issues.append({
                    'file': filepath,
                    'line': i,
                    'type': 'link_without_url',
                    'severity': 'medium',
                    'message': 'Link sem URL (expected ](url))',
                    'content': line.strip()[:100]
                })
        
        return issues
    
    def check_unmatched_brackets(self, filepath: str, content: str) -> List[Dict]:
        """Detecta parênteses/colchetes não balanceados"""
        issues = []
        
        # Conta parênteses e colchetes
        open_paren = content.count('(')
        close_paren = content.count(')')
        open_brack = content.count('[')
        close_brack = content.count(']')
        
        if open_paren != close_paren:
            issues.append({
                'file': filepath,
                'line': 0,
                'type': 'unmatched_parentheses',
                'severity': 'low',
                'message': f'Parênteses desbalanceados: {open_paren} abertos vs {close_paren} fechados',
                'content': f'Diff: {open_paren - close_paren}'
            })
        
        if open_brack != close_brack:
            issues.append({
                'file': filepath,
                'line': 0,
                'type': 'unmatched_brackets',
                'severity': 'low',
                'message': f'Colchetes desbalanceados: {open_brack} abertos vs {close_brack} fechados',
                'content': f'Diff: {open_brack - close_brack}'
            })
        
        return issues
    
    def check_broken_code_blocks(self, filepath: str, content: str) -> List[Dict]:
        """Detecta blocos de código não fechados"""
        issues = []
        
        # Conta blocos de código
        triple_backticks = content.count('```')
        
        if triple_backticks % 2 != 0:
            issues.append({
                'file': filepath,
                'line': 0,
                'type': 'unclosed_code_block',
                'severity': 'high',
                'message': f'Bloco de código não fechado (``` count: {triple_backticks})',
                'content': f'Total: {triple_backticks} (should be even)'
            })
        
        return issues
    
    def validate_file(self, filepath: str) -> List[Dict]:
        """Valida um arquivo e retorna lista de problemas"""
        try:
            content = Path(filepath).read_text(encoding='utf-8')
        except Exception as e:
            return [{
                'file': filepath,
                'line': 0,
                'type': 'read_error',
                'severity': 'critical',
                'message': f'Erro ao ler arquivo: {e}',
                'content': ''
            }]
        
        all_issues = []
        
        for check_name, check_func in self.checks.items():
            issues = check_func(filepath, content)
            all_issues.extend(issues)
        
        return all_issues
    
    def validate_directory(self, base_dir: str = "_bmad") -> Dict:
        """Valida todos os arquivos traduzidos em um diretório"""
        translated_files = list(Path(base_dir).rglob("*_pt-br.md"))
        
        all_issues = []
        files_with_issues = set()
        
        for filepath in translated_files:
            issues = self.validate_file(str(filepath))
            if issues:
                all_issues.extend(issues)
                files_with_issues.add(str(filepath))
        
        return {
            'total_files': len(translated_files),
            'files_with_issues': len(files_with_issues),
            'total_issues': len(all_issues),
            'issues': all_issues,
            'files': list(files_with_issues)
        }
    
    def generate_report(self, results: Dict, output_file: str = None):
        """Gera relatório de validação"""
        lines = []
        
        lines.append("# Relatório de Validação de Traduções\n")
        lines.append(f"**Total de arquivos:** {results['total_files']}\n")
        lines.append(f"**Arquivos com problemas:** {results['files_with_issues']}\n")
        lines.append(f"**Total de problemas:** {results['total_issues']}\n\n")
        
        if results['total_issues'] == 0:
            lines.append("✅ **Nenhum problema encontrado!**\n")
        else:
            lines.append("---\n\n")
            
            # Agrupa por arquivo
            by_file = {}
            for issue in results['issues']:
                file = issue['file']
                if file not in by_file:
                    by_file[file] = []
                by_file[file].append(issue)
            
            # Ordena por severidade
            severity_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
            
            for file in sorted(by_file.keys()):
                issues = sorted(by_file[file], key=lambda x: severity_order.get(x['severity'], 999))
                
                rel_path = Path(file).relative_to(Path.cwd()) if Path.cwd() in Path(file).parents else file
                lines.append(f"## [{rel_path}](file:///{Path(file).absolute()})\n\n")
                lines.append(f"**Problemas:** {len(issues)}\n\n")
                
                for issue in issues:
                    severity_emoji = {'critical': '🔴', 'high': '🟠', 'medium': '🟡', 'low': '⚪'}
                    emoji = severity_emoji.get(issue['severity'], '❔')
                    
                    lines.append(f"### {emoji} {issue['type'].replace('_', ' ').title()}\n\n")
                    if issue['line'] > 0:
                        lines.append(f"**Linha:** {issue['line']}\n")
                    lines.append(f"**Severidade:** {issue['severity']}\n")
                    lines.append(f"**Mensagem:** {issue['message']}\n\n")
                    
                    if issue['content']:
                        lines.append(f"```\n{issue['content']}\n```\n\n")
        
        report = ''.join(lines)
        
        if output_file:
            Path(output_file).write_text(report, encoding='utf-8')
            print(f"✅ Relatório salvo em: {output_file}")
        else:
            print(report)
        
        return report

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Validador de traduções')
    parser.add_argument('-d', '--dir', default='_bmad', help='Diretório base')
    parser.add_argument('-f', '--file', help='Arquivo específico para validar')
    parser.add_argument('-o', '--output', help='Arquivo de saída para relatório')
    parser.add_argument('--fix', action='store_true', help='Tentar corrigir automaticamente')
    
    args = parser.parse_args()
    
    validator = TranslationValidator()
    
    if args.file:
        issues = validator.validate_file(args.file)
        results = {
            'total_files': 1,
            'files_with_issues': 1 if issues else 0,
            'total_issues': len(issues),
            'issues': issues,
            'files': [args.file] if issues else []
        }
    else:
        results = validator.validate_directory(args.dir)
    
    validator.generate_report(results, args.output)
    
    # Sumário no terminal
    print(f"\n{'='*70}")
    print("SUMÁRIO DE VALIDAÇÃO")
    print(f"{'='*70}")
    print(f"Arquivos analisados: {results['total_files']}")
    print(f"Arquivos com problemas: {results['files_with_issues']}")
    print(f"Total de problemas: {results['total_issues']}")
    
    if results['total_issues'] > 0:
        print(f"\n⚠️  {results['files_with_issues']} arquivo(s) requer(em) atenção!")
        return 1
    else:
        print(f"\n✅ Todos os arquivos estão OK!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
