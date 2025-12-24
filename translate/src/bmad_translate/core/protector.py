"""
Proteção de conteúdo para o sistema de tradução BMAD
"""

import re
import yaml
from typing import Dict, List, Tuple, Any
from pathlib import Path


class ContentProtector:
    """Protege conteúdo técnico durante a tradução."""
    
    def __init__(self, settings=None):
        """
        Inicializa o protetor de conteúdo.
        
        Args:
            settings: Configurações do sistema
        """
        self.settings = settings
        self.placeholders = {}
        self.patterns = self._load_protection_patterns()
        
    def _load_protection_patterns(self) -> List[Dict[str, str]]:
        """Carrega os padrões de proteção do arquivo YAML."""
        try:
            # Tenta carregar do arquivo de configuração
            current_dir = Path(__file__).parent.parent.parent.parent
            patterns_path = current_dir / "config" / "protection_patterns.yaml"
            
            if patterns_path.exists():
                with open(patterns_path, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    patterns = []
                    
                    # Extrai todos os padrões do YAML
                    for category in data.get('protection_patterns', {}).values():
                        if isinstance(category, list):
                            patterns.extend(category)
                        elif isinstance(category, dict) and 'pattern' in category:
                            patterns.append(category)
                    
                    return patterns
            
        except Exception:
            # Fallback para padrões hardcoded em caso de erro
            pass
            
        # Padrões fallback
        return [
            {'pattern': r'(?s)^---\n.*?\n---', 'description': 'Frontmatter YAML'},
            {'pattern': r'```[\s\S]*?```', 'description': 'Blocos de código'},
            {'pattern': r'`[^`\n]+`', 'description': 'Código inline'},
            {'pattern': r'<[^>]+>', 'description': 'Tags XML/HTML'},
            {'pattern': r'\{%.*?%\}', 'description': 'Liquid Tags'},
            {'pattern': r'@_[\w/.-]+', 'description': 'Caminhos BMAD'},
            {'pattern': r'https?://[^\s]+', 'description': 'URLs'},
        ]
    
    def protect_content(self, content: str) -> str:
        """
        Protege o conteúdo substituindo padrões técnicos por placeholders.
        
        Args:
            content: Conteúdo a ser protegido
            
        Returns:
            Conteúdo protegido com placeholders
        """
        self.placeholders = {}
        protected_content = content
        count = 0
        
        for pattern_info in self.patterns:
            pattern = pattern_info['pattern']
            
            try:
                matches = re.finditer(pattern, protected_content, re.MULTILINE)
                
                # Processa de trás para frente para não alterar índices
                for match in reversed(list(matches)):
                    span = match.span()
                    original = protected_content[span[0]:span[1]]
                    # Formato robusto que sobrevive à tradução: Letras + Números + Letras
                    key = f"BMADPROTECT{count:03d}END"
                    self.placeholders[key] = original
                    self.placeholders[count] = original  # Armazena com índice numérico também
                    
                    protected_content = (
                        protected_content[:span[0]] + key + protected_content[span[1]:]
                    )
                    count += 1
                    
            except re.error as e:
                # Ignora padrões inválidos e continua
                continue
                
        return protected_content
    
    def restore_content(self, protected_text: str) -> str:
        """
        Restaura os placeholders originais no texto protegido.
        
        Args:
            protected_text: Texto com placeholders
            
        Returns:
            Texto restaurado com conteúdo original
        """
        def replace_match(match):
            try:
                idx = int(match.group(1))
                # Tenta recuperar pelo índice numérico
                if idx in self.placeholders:
                    return self.placeholders[idx]
            except (ValueError, KeyError):
                pass
            return match.group(0)
        
        # Loop para resolver placeholders aninhados (ex: placeholder dentro de placeholder)
        current_text = protected_text
        for _ in range(10): # Limite de recursão para evitar loops infinitos
            # Regex para pegar o novo formato, tolerando espaços que o tradutor possa adicionar
            # Ex: BMADPROTECT 000 END
            new_text = re.sub(r'BMADPROTECT\s*(\d+)\s*(?:END|End|end)', replace_match, current_text)
            
            if new_text == current_text:
                return current_text
                
            current_text = new_text
            
        return current_text
    
    def get_placeholder_count(self) -> int:
        """Retorna o número de placeholders criados."""
        return len(self.placeholders)
    
    def get_placeholders(self) -> Dict[str, str]:
        """Retorna os dicionários de placeholders."""
        return self.placeholders.copy()
    
    def clear_placeholders(self) -> None:
        """Limpa os placeholders armazenados."""
        self.placeholders.clear()
    
    def add_custom_pattern(self, pattern: str, description: str = "") -> None:
        """
        Adiciona um padrão de proteção personalizado.
        
        Args:
            pattern: Regex pattern
            description: Descrição do padrão
        """
        self.patterns.append({
            'pattern': pattern,
            'description': description
        })
    
    def remove_pattern(self, pattern: str) -> bool:
        """
        Remove um padrão de proteção.
        
        Args:
            pattern: Pattern a ser removido
            
        Returns:
            True se removido, False se não encontrado
        """
        for i, pattern_info in enumerate(self.patterns):
            if pattern_info.get('pattern') == pattern:
                del self.patterns[i]
                return True
        return False
    
    def get_patterns(self) -> List[Dict[str, str]]:
        """Retorna a lista de padrões de proteção."""
        return self.patterns.copy()
    
    def validate_patterns(self) -> List[str]:
        """
        Valida todos os padrões de proteção.
        
        Returns:
            Lista de padrões inválidos
        """
        invalid_patterns = []
        
        for i, pattern_info in enumerate(self.patterns):
            pattern = pattern_info.get('pattern', '')
            try:
                re.compile(pattern)
            except re.error as e:
                invalid_patterns.append(f"Padrão {i}: {pattern} - Erro: {e}")
                
        return invalid_patterns
    
    def protect_frontmatter_only(self, content: str) -> Tuple[str, str]:
        """
        Protege apenas o frontmatter de um documento Markdown.
        
        Args:
            content: Conteúdo do documento
            
        Returns:
            Tuple de (conteúdo protegido, frontmatter original)
        """
        frontmatter_match = re.search(r'^\s*---\n(.*?)\n---', content, re.DOTALL)
        
        if frontmatter_match:
            frontmatter_original = frontmatter_match.group(0)
            frontmatter_key = f"__BMAD_FRONTMATTER__"
            
            self.placeholders[frontmatter_key] = frontmatter_original
            protected_content = content.replace(frontmatter_original, frontmatter_key, 1)
            
            return protected_content, frontmatter_original
        
        return content, ""
    
    def restore_frontmatter(self, content: str, frontmatter_original: str) -> str:
        """
        Restaura o frontmatter original.
        
        Args:
            content: Conteúdo com frontmatter protegido
            frontmatter_original: Frontmatter original
            
        Returns:
            Conteúdo com frontmatter restaurado
        """
        frontmatter_key = f"__BMAD_FRONTMATTER__"
        if frontmatter_key in self.placeholders:
            return content.replace(frontmatter_key, frontmatter_original, 1)
        return content
    
    def __repr__(self) -> str:
        """Representação string do objeto."""
        return f"ContentProtector(patterns={len(self.patterns)}, placeholders={len(self.placeholders)})"
