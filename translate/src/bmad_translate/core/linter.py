
import yaml
import re
from typing import List, Dict, Any, Optional

class Linter:
    """
    Sistema de verificação de qualidade para arquivos traduzidos.
    Suporta YAML, Markdown e (futuramente) TOML/CSV.
    """
    
    @staticmethod
    def check_yaml(content: str) -> List[str]:
        """
        Verifica a validade da sintaxe YAML.
        
        Returns:
            Lista de mensagens de erro (vazia se válido).
        """
        errors = []
        try:
            yaml.safe_load(content)
        except yaml.YAMLError as e:
            errors.append(f"Erro de sintaxe YAML: {str(e)}")
        return errors

    @staticmethod
    def check_markdown(content: str) -> List[str]:
        """
        Verifica problemas comuns em Markdown.
        
        Returns:
            Lista de avisos/erros.
        """
        errors = []
        
        # 1. Verifica consistência de Frontmatter
        if content.startswith('---'):
            end_fm = content.find('---', 3)
            if end_fm == -1:
                errors.append("Frontmatter não fechado corretamente (falta '---').")
            else:
                fm_content = content[3:end_fm]
                errors.extend([f"Frontmatter: {e}" for e in Linter.check_yaml(fm_content)])
        
        # 2. Verifica formatação de listas aninhadas (indentação suspeita)
        # Ex: Detectar - Text com 3 espaços (pode estar desalinhado)
        # lines = content.split('\n')
        # for i, line in enumerate(lines):
        #    if re.match(r'^\s{1,3}- ', line): # Indentação ímpar/estranha?
        #        pass # Complexo de validar sem contexto
        
        # 3. Verifica blocos de código não fechados
        code_blocks = content.count('```')
        if code_blocks % 2 != 0:
            errors.append("Número ímpar de delimitadores de bloco de código (```). Possível bloco não fechado.")
            
        # 4. Verifica negrito/itálico quebrado (ex: ** text **) - O tradutor corrige, mas o linter avisa se falhar
        if re.search(r'\*\*\s+.*?\*\*', content) or re.search(r'\*\*.+?\s+\*\*', content):
             errors.append("Espaçamento inválido em negrito detectado (ex: '** texto**').")

        return errors

    @staticmethod
    def lint_file(filepath: str, content: str) -> Dict[str, List[str]]:
        """
        Executa linter baseado na extensão do arquivo.
        """
        errors = []
        if filepath.endswith('.md') or filepath.endswith('.markdown'):
            errors.extend(Linter.check_markdown(content))
        elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
            errors.extend(Linter.check_yaml(content))
        
        return {'file': filepath, 'errors': errors}
