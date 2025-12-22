"""
Módulo de validação de arquivos do sistema BMAD
"""

import os
import sys
import yaml
import json
import logging
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Tuple, Union

# Importação condicional do TOML
try:
    if sys.version_info >= (3, 11):
        import tomllib
    else:
        import tomli as tomllib
    TOML_AVAILABLE = True
except ImportError:
    TOML_AVAILABLE = False

from ..config.settings import Settings


@dataclass
class ValidationResult:
    """Resultado de uma validação de arquivo."""
    is_valid: bool
    file_path: str
    file_type: str
    errors: List[str]
    warnings: List[str]
    file_size: int = 0
    encoding: str = "utf-8"


class FileValidator:
    """Validador de arquivos para o sistema BMAD."""
    
    def __init__(self, settings: Optional[Settings] = None):
        """
        Inicializa o validador.
        
        Args:
            settings: Configurações do sistema
        """
        self.settings = settings or Settings()
        self.logger = self._setup_logging()
        
    def _setup_logging(self) -> logging.Logger:
        """Configura o logging para o validador."""
        logger = logging.getLogger(f"{__name__}.validator")
        
        if not logger.handlers:
            log_settings = self.settings.get_logging_settings()
            logger.setLevel(getattr(logging, log_settings.get('level', 'INFO')))
            
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s'
            )
            
            # Handler para console
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
        
        return logger
    
    def _get_file_type(self, filepath: str) -> str:
        """
        Determina o tipo de arquivo baseado na extensão.
        
        Args:
            filepath: Caminho do arquivo
            
        Returns:
            Tipo do arquivo (yaml, json, toml, markdown, unknown)
        """
        ext = Path(filepath).suffix.lower()
        
        type_mapping = {
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.json': 'json',
            '.jsonc': 'json',
            '.toml': 'toml',
            '.md': 'markdown',
            '.markdown': 'markdown'
        }
        
        return type_mapping.get(ext, 'unknown')
    
    def _validate_encoding(self, filepath: str) -> Tuple[bool, str, List[str]]:
        """
        Valida a codificação do arquivo.
        
        Args:
            filepath: Caminho do arquivo
            
        Returns:
            Tuple de (é_válido, codificação, erros)
        """
        errors = []
        encoding = 'utf-8'
        
        try:
            # Tenta ler com UTF-8 primeiro
            with open(filepath, 'r', encoding='utf-8') as f:
                f.read()
            return True, encoding, errors
            
        except UnicodeDecodeError as e:
            errors.append(f"Erro de codificação UTF-8: {e}")
            
            # Tenta detectar outras codificações comuns
            encodings_to_try = ['utf-8-sig', 'latin-1', 'cp1252']
            
            for enc in encodings_to_try:
                try:
                    with open(filepath, 'r', encoding=enc) as f:
                        f.read()
                    encoding = enc
                    errors.append(f"Arquivo usa codificação {enc}, considere converter para UTF-8")
                    return True, encoding, errors
                except UnicodeDecodeError:
                    continue
            
            errors.append("Não foi possível determinar a codificação do arquivo")
            return False, encoding, errors
            
        except Exception as e:
            errors.append(f"Erro ao ler arquivo: {e}")
            return False, encoding, errors
    
    def _validate_yaml(self, filepath: str) -> Tuple[bool, List[str], List[str]]:
        """
        Valida um arquivo YAML.
        
        Args:
            filepath: Caminho do arquivo
            
        Returns:
            Tuple de (é_válido, erros, avisos)
        """
        errors = []
        warnings = []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Validação básica do YAML
            data = yaml.safe_load(content)
            
            if data is None:
                warnings.append("Arquivo YAML está vazio ou contém apenas nulos")
                return True, errors, warnings
            
            # Verifica estrutura comum
            if isinstance(data, dict):
                self._check_yaml_structure(data, warnings)
            
            # Tenta carregar com ruíz para validar sintaxe
            yaml.safe_load(content)
            
        except yaml.YAMLError as e:
            errors.append(f"Erro de sintaxe YAML: {e}")
            return False, errors, warnings
        except Exception as e:
            errors.append(f"Erro ao processar arquivo YAML: {e}")
            return False, errors, warnings
        
        return True, errors, warnings
    
    def _check_yaml_structure(self, data: Dict[str, Any], warnings: List[str]) -> None:
        """
        Verifica estrutura comum em arquivos YAML BMAD.
        
        Args:
            data: Dados YAML parseados
            warnings: Lista de avisos para preencher
        """
        # Verifica campos comuns em manifests
        common_fields = ['path', 'name', 'description', 'type', 'version']
        missing_fields = [field for field in common_fields if field not in data]
        
        if missing_fields and len(missing_fields) < len(common_fields):
            warnings.append(f"Campos comuns ausentes: {', '.join(missing_fields)}")
        
        # Verifica se há chaves com nomes suspeitos
        suspicious_keys = [key for key in data.keys() if ' ' in key or key.startswith('_')]
        if suspicious_keys:
            warnings.append(f"Chaves com nomes suspeitos: {', '.join(suspicious_keys)}")
        
        # Verifica valores muito longos (possíveis erros)
        for key, value in data.items():
            if isinstance(value, str) and len(value) > 1000:
                warnings.append(f"Valor muito longo para chave '{key}' ({len(value)} caracteres)")
    
    def _validate_json(self, filepath: str) -> Tuple[bool, List[str], List[str]]:
        """
        Valida um arquivo JSON.
        
        Args:
            filepath: Caminho do arquivo
            
        Returns:
            Tuple de (é_válido, erros, avisos)
        """
        errors = []
        warnings = []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove comentários se for JSONC
            if filepath.endswith('.jsonc'):
                content = self._strip_json_comments(content)
                warnings.append("Arquivo JSONC contém comentários que serão removidos para validação")
            
            data = json.loads(content)
            
            if data is None:
                warnings.append("Arquivo JSON está vazio ou contém apenas nulos")
                return True, errors, warnings
            
            # Verifica estrutura
            if isinstance(data, dict):
                self._check_json_structure(data, warnings)
            
        except json.JSONDecodeError as e:
            errors.append(f"Erro de sintaxe JSON: {e}")
            return False, errors, warnings
        except Exception as e:
            errors.append(f"Erro ao processar arquivo JSON: {e}")
            return False, errors, warnings
        
        return True, errors, warnings
    
    def _strip_json_comments(self, content: str) -> str:
        """
        Remove comentários de conteúdo JSONC.
        
        Args:
            content: Conteúdo JSONC
            
        Returns:
            Conteúdo JSON limpo
        """
        import re
        
        # Remove comentários de bloco
        content = re.sub(r'/\*[\s\S]*?\*/', '', content)
        
        # Remove comentários de linha (cuidado com URLs)
        lines = content.split('\n')
        clean_lines = []
        
        for line in lines:
            if '//' in line:
                # Preserva URLs
                if 'http://' in line or 'https://' in line:
                    clean_lines.append(line)
                    continue
                
                parts = line.split('//')
                clean_lines.append(parts[0])
            else:
                clean_lines.append(line)
        
        return '\n'.join(clean_lines)
    
    def _check_json_structure(self, data: Dict[str, Any], warnings: List[str]) -> None:
        """
        Verifica estrutura comum em arquivos JSON.
        
        Args:
            data: Dados JSON parseados
            warnings: Lista de avisos para preencher
        """
        # Verifica profundidade excessiva
        max_depth = self._get_json_depth(data)
        if max_depth > 10:
            warnings.append(f"Estrutura muito profunda (nível {max_depth}), pode ser difícil de manter")
        
        # Verifica arrays muito grandes
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, list) and len(value) > 100:
                    warnings.append(f"Array muito grande para chave '{key}' ({len(value)} itens)")
    
    def _get_json_depth(self, obj: Any, current_depth: int = 0) -> int:
        """
        Calcula a profundidade máxima de um objeto JSON.
        
        Args:
            obj: Objeto JSON
            current_depth: Profundidade atual
            
        Returns:
            Profundidade máxima
        """
        if isinstance(obj, dict):
            if not obj:
                return current_depth
            return max(self._get_json_depth(v, current_depth + 1) for v in obj.values())
        elif isinstance(obj, list):
            if not obj:
                return current_depth
            return max(self._get_json_depth(item, current_depth + 1) for item in obj)
        else:
            return current_depth
    
    def _validate_toml(self, filepath: str) -> Tuple[bool, List[str], List[str]]:
        """
        Valida um arquivo TOML.
        
        Args:
            filepath: Caminho do arquivo
            
        Returns:
            Tuple de (é_válido, erros, avisos)
        """
        if not TOML_AVAILABLE:
            return False, ["Biblioteca TOML não disponível"], []
        
        errors = []
        warnings = []
        
        try:
            with open(filepath, 'rb') as f:
                data = tomllib.load(f)
            
            if data is None:
                warnings.append("Arquivo TOML está vazio")
                return True, errors, warnings
            
            # Verifica estrutura básica
            if isinstance(data, dict):
                self._check_toml_structure(data, warnings)
            
        except Exception as e:
            errors.append(f"Erro ao processar arquivo TOML: {e}")
            return False, errors, warnings
        
        return True, errors, warnings
    
    def _check_toml_structure(self, data: Dict[str, Any], warnings: List[str]) -> None:
        """
        Verifica estrutura comum em arquivos TOML.
        
        Args:
            data: Dados TOML parseados
            warnings: Lista de avisos para preencher
        """
        # Verifica seções comuns em configurações
        common_sections = ['package', 'dependencies', 'build-system', 'tool']
        found_sections = [section for section in common_sections if section in data]
        
        if not found_sections:
            warnings.append("Nenhuma seção comum de configuração encontrada")
    
    def _validate_markdown(self, filepath: str) -> Tuple[bool, List[str], List[str]]:
        """
        Valida um arquivo Markdown.
        
        Args:
            filepath: Caminho do arquivo
            
        Returns:
            Tuple de (é_válido, erros, avisos)
        """
        errors = []
        warnings = []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            # Verifica frontmatter
            if lines and lines[0].strip() == '---':
                frontmatter_end = -1
                for i, line in enumerate(lines[1:], 1):
                    if line.strip() == '---':
                        frontmatter_end = i
                        break
                
                if frontmatter_end == -1:
                    errors.append("Frontmatter não fechado")
                else:
                    # Valida o frontmatter como YAML
                    frontmatter_content = '\n'.join(lines[1:frontmatter_end])
                    try:
                        yaml.safe_load(frontmatter_content)
                    except yaml.YAMLError as e:
                        errors.append(f"Erro no frontmatter YAML: {e}")
            
            # Verifica links quebrados (básico)
            self._check_markdown_links(content, warnings)
            
            # Verifica headers
            self._check_markdown_headers(content, warnings)
            
        except Exception as e:
            errors.append(f"Erro ao processar arquivo Markdown: {e}")
            return False, errors, warnings
        
        return True, errors, warnings
    
    def _check_markdown_links(self, content: str, warnings: List[str]) -> None:
        """
        Verifica links em arquivos Markdown.
        
        Args:
            content: Conteúdo do arquivo
            warnings: Lista de avisos para preencher
        """
        import re
        
        # Procura links [text](url)
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        links = re.findall(link_pattern, content)
        
        for text, url in links:
            # Verifica URLs vazias
            if not url.strip():
                warnings.append(f"Link vazio encontrado: [{text}]()")
            
            # Verifica espaços em URLs
            if ' ' in url and not url.startswith(('http://', 'https://')):
                warnings.append(f"URL com espaços: {url}")
    
    def _check_markdown_headers(self, content: str, warnings: List[str]) -> None:
        """
        Verifica headers em arquivos Markdown.
        
        Args:
            content: Conteúdo do arquivo
            warnings: Lista de avisos para preencher
        """
        lines = content.split('\n')
        header_levels = []
        
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('#'):
                level = len(stripped) - len(stripped.lstrip('#'))
                header_levels.append(level)
        
        # Verifica pulos de nível
        for i in range(1, len(header_levels)):
            if header_levels[i] - header_levels[i-1] > 1:
                warnings.append(f"Pulo de nível de header detectado (de h{header_levels[i-1]} para h{header_levels[i]})")
    
    def validate_file(self, filepath: str) -> ValidationResult:
        """
        Valida um arquivo específico.
        
        Args:
            filepath: Caminho do arquivo
            
        Returns:
            Resultado da validação
        """
        if not os.path.exists(filepath):
            return ValidationResult(
                is_valid=False,
                file_path=filepath,
                file_type='unknown',
                errors=['Arquivo não encontrado'],
                warnings=[]
            )
        
        file_type = self._get_file_type(filepath)
        errors = []
        warnings = []
        
        # Validação básica de codificação
        encoding_valid, encoding, enc_errors = self._validate_encoding(filepath)
        errors.extend(enc_errors)
        
        # Obtém tamanho do arquivo
        try:
            file_size = os.path.getsize(filepath)
        except Exception:
            file_size = 0
        
        if not encoding_valid:
            return ValidationResult(
                is_valid=False,
                file_path=filepath,
                file_type=file_type,
                errors=errors,
                warnings=warnings,
                file_size=file_size,
                encoding=encoding
            )
        
        # Validação específica por tipo
        if file_type == 'yaml':
            is_valid, type_errors, type_warnings = self._validate_yaml(filepath)
        elif file_type == 'json':
            is_valid, type_errors, type_warnings = self._validate_json(filepath)
        elif file_type == 'toml':
            is_valid, type_errors, type_warnings = self._validate_toml(filepath)
        elif file_type == 'markdown':
            is_valid, type_errors, type_warnings = self._validate_markdown(filepath)
        else:
            is_valid = True
            type_errors = [f"Tipo de arquivo não suportado para validação: {file_type}"]
            type_warnings = []
        
        errors.extend(type_errors)
        warnings.extend(type_warnings)
        
        return ValidationResult(
            is_valid=is_valid and len(errors) == 0,
            file_path=filepath,
            file_type=file_type,
            errors=errors,
            warnings=warnings,
            file_size=file_size,
            encoding=encoding
        )
    
    def validate_directory(self, base_dir: str = '.') -> List[ValidationResult]:
        """
        Valida todos os arquivos suportados em um diretório.
        
        Args:
            base_dir: Diretório base para validação
            
        Returns:
            Lista de resultados de validação
        """
        results = []
        extensions = tuple(self.settings.get_supported_extensions())
        
        for root, dirs, files in os.walk(base_dir):
            skip_dirs = set(self.settings.get_skip_directories())
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            
            for file in files:
                if file.endswith(extensions):
                    filepath = os.path.join(root, file)
                    try:
                        result = self.validate_file(filepath)
                        results.append(result)
                    except Exception as e:
                        self.logger.error(f"Erro ao validar {filepath}: {e}")
                        results.append(ValidationResult(
                            is_valid=False,
                            file_path=filepath,
                            file_type='unknown',
                            errors=[f"Erro na validação: {e}"],
                            warnings=[]
                        ))
        
        return results
    
    def get_validation_summary(self, results: List[ValidationResult]) -> Dict[str, Any]:
        """
        Gera um resumo dos resultados de validação.
        
        Args:
            results: Lista de resultados de validação
            
        Returns:
            Dicionário com estatísticas
        """
        total_files = len(results)
        valid_files = sum(1 for r in results if r.is_valid)
        total_errors = sum(len(r.errors) for r in results)
        total_warnings = sum(len(r.warnings) for r in results)
        
        # Agrupa por tipo
        by_type = {}
        for result in results:
            file_type = result.file_type
            if file_type not in by_type:
                by_type[file_type] = {'total': 0, 'valid': 0, 'errors': 0}
            
            by_type[file_type]['total'] += 1
            if result.is_valid:
                by_type[file_type]['valid'] += 1
            by_type[file_type]['errors'] += len(result.errors)
        
        return {
            'total_files': total_files,
            'valid_files': valid_files,
            'invalid_files': total_files - valid_files,
            'total_errors': total_errors,
            'total_warnings': total_warnings,
            'success_rate': (valid_files / total_files * 100) if total_files > 0 else 0,
            'by_type': by_type
        }
    
    def __repr__(self) -> str:
        """Representação string do objeto."""
        return f"FileValidator(settings={self.settings is not None})"
