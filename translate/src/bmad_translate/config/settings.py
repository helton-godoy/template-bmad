"""
Configurações do sistema de tradução BMAD
"""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional


class Settings:
    """Gerencia as configurações do sistema de tradução BMAD."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Inicializa as configurações.
        
        Args:
            config_path: Caminho para o arquivo de configuração YAML
        """
        self.config_path = config_path or self._get_default_config_path()
        self._settings = self._load_settings()
        
    def _get_default_config_path(self) -> str:
        """Retorna o caminho padrão do arquivo de configuração."""
        # Tenta encontrar o config相对于 o diretório do pacote
        current_dir = Path(__file__).parent.parent.parent.parent
        config_path = current_dir / "config" / "default_settings.yaml"
        
        if config_path.exists():
            return str(config_path)
        
        # Fallback para config relativo ao diretório de trabalho
        return "config/default_settings.yaml"
    
    def _load_settings(self) -> Dict[str, Any]:
        """Carrega as configurações do arquivo YAML."""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo de configuração não encontrado: {self.config_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Erro ao processar arquivo YAML: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Obtém um valor de configuração usando notação de ponto.
        
        Args:
            key: Chave de configuração (ex: 'translation.target_language')
            default: Valor padrão se a chave não for encontrada
            
        Returns:
            Valor da configuração ou default
        """
        keys = key.split('.')
        value = self._settings
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
                
        return value
    
    def get_translation_settings(self) -> Dict[str, Any]:
        """Retorna as configurações de tradução."""
        return self.get('translation', {})
    
    def get_supported_extensions(self) -> List[str]:
        """Retorna as extensões de arquivo suportadas."""
        return self.get('supported_extensions', [])
    
    def get_skip_directories(self) -> List[str]:
        """Retorna os diretórios a ignorar."""
        return self.get('skip_directories', [])
    
    def get_translatable_keys(self) -> List[str]:
        """Retorna as chaves que podem ser traduzidas."""
        return self.get('translatable_keys', [])
    
    def get_security_settings(self) -> Dict[str, Any]:
        """Retorna as configurações de segurança."""
        return self.get('security', {})
    
    def get_logging_settings(self) -> Dict[str, Any]:
        """Retorna as configurações de logging."""
        return self.get('logging', {})
    
    def get_performance_settings(self) -> Dict[str, Any]:
        """Retorna as configurações de performance."""
        return self.get('performance', {})
    
    def get_target_language(self) -> str:
        """Retorna o idioma de destino."""
        return self.get('translation.target_language', 'pt')
    
    def get_output_suffix(self) -> str:
        """Retorna o sufixo para arquivos traduzidos."""
        return self.get('translation.output_suffix', '_pt-br')
    
    def get_max_text_length(self) -> int:
        """Retorna o tamanho máximo do texto por tradução."""
        return self.get('translation.max_text_length', 5000)
    
    def get_safe_chunk_size(self) -> int:
        """Retorna o tamanho ideal do batch para o tradutor."""
        return self.get('translation.safe_chunk_size', 3000)
    
    def get_allowed_base_dir(self) -> Optional[str]:
        """Retorna o diretório base permitido."""
        return self.get('security.allowed_base_dir')
    
    def is_path_validation_enabled(self) -> bool:
        """Verifica se a validação de path está habilitada."""
        return self.get('security.enable_path_validation', True)
    
    def is_input_sanitization_enabled(self) -> bool:
        """Verifica se a sanitização de input está habilitada."""
        return self.get('security.enable_input_sanitization', True)
    
    def is_cache_enabled(self) -> bool:
        """Verifica se o cache está habilitado."""
        return self.get('performance.enable_cache', True)
    
    def get_cache_size_mb(self) -> int:
        """Retorna o tamanho máximo do cache em MB."""
        return self.get('performance.cache_size_mb', 100)
    
    def get_translation_timeout(self) -> int:
        """Retorna o timeout para operações de tradução."""
        return self.get('performance.translation_timeout', 30)
    
    def get_max_retries(self) -> int:
        """Retorna o número máximo de tentativas."""
        return self.get('performance.max_retries', 3)
    
    def update_setting(self, key: str, value: Any) -> None:
        """
        Atualiza um valor de configuração.
        
        Args:
            key: Chave de configuração (ex: 'translation.target_language')
            value: Novo valor
        """
        keys = key.split('.')
        config = self._settings
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
            
        config[keys[-1]] = value
    
    def save_settings(self, path: Optional[str] = None) -> None:
        """
        Salva as configurações atuais em um arquivo YAML.
        
        Args:
            path: Caminho para salvar o arquivo (opcional)
        """
        save_path = path or self.config_path
        
        try:
            with open(save_path, 'w', encoding='utf-8') as f:
                yaml.dump(self._settings, f, default_flow_style=False, 
                         allow_unicode=True, indent=2)
        except Exception as e:
            raise IOError(f"Erro ao salvar configurações: {e}")
    
    def reload(self) -> None:
        """Recarrega as configurações do arquivo."""
        self._settings = self._load_settings()
    
    def __repr__(self) -> str:
        """Representação string do objeto."""
        return f"Settings(config_path='{self.config_path}')"
