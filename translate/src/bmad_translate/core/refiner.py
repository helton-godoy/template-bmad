"""
Módulo de refinamento de tradução do sistema BMAD
"""

import os
import re
import logging
from typing import List, Optional, Dict, Any
from pathlib import Path

try:
    from langdetect import detect, LangDetectException
    LANGDETECT_AVAILABLE = True
except ImportError:
    LANGDETECT_AVAILABLE = False

try:
    import language_tool_python
    LANGUAGETOOL_AVAILABLE = True
except ImportError:
    LANGUAGETOOL_AVAILABLE = False

from ..config.settings import Settings


class BMADRefiner:
    """Refinador de traduções usando LanguageTool."""
    
    def __init__(self, settings: Optional[Settings] = None):
        """
        Inicializa o refinador.
        
        Args:
            settings: Configurações do sistema
        """
        self.settings = settings or Settings()
        self.logger = self._setup_logging()
        self._language_tool = None
        self._technical_terms = self._load_technical_terms()
        
    def _setup_logging(self) -> logging.Logger:
        """Configura o logging para o refinador."""
        logger = logging.getLogger(f"{__name__}.refiner")
        
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
    
    def _load_technical_terms(self) -> List[str]:
        """Carrega termos técnicos que não devem ser corrigidos."""
        # Tenta carregar do arquivo de configuração de idiomas
        try:
            current_dir = Path(__file__).parent.parent.parent.parent
            lang_config_path = current_dir / "config" / "language_mappings.yaml"
            
            if lang_config_path.exists():
                import yaml
                with open(lang_config_path, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    
                    # Extrai termos técnicos do idioma alvo
                    target_lang = self.settings.get_target_language()
                    refinement_settings = data.get('refinement_settings', {})
                    lang_settings = refinement_settings.get(target_lang, {})
                    exceptions = lang_settings.get('exceptions', {})
                    
                    return exceptions.get('technical_terms', [])
        
        except Exception:
            # Fallback para termos hardcoded
            pass
        
        # Lista padrão de termos técnicos
        return [
            "workflow", "stakeholder", "backlog", "sprint", "scrum",
            "kanban", "devops", "pipeline", "repository", "branch",
            "merge", "commit", "pull", "request", "issue", "ticket",
            "deployment", "release", "hotfix", "feature", "bugfix"
        ]
    
    def _ensure_language_tool(self) -> bool:
        """Garante que o LanguageTool está inicializado."""
        if not LANGUAGETOOL_AVAILABLE:
            self.logger.error("LanguageTool não disponível. Instale com: pip install language-tool-python")
            return False
        
        if self._language_tool is None:
            target_lang = self.settings.get_target_language()
            
            # Mapeamento de idiomas para LanguageTool
            lang_mapping = {
                'pt': 'pt-PT',
                'es': 'es-ES',
                'fr': 'fr',
                'de': 'de',
                'it': 'it'
            }
            
            lt_lang = lang_mapping.get(target_lang, 'pt-PT')
            
            try:
                self.logger.info(f"Inicializando LanguageTool para idioma: {lt_lang}")
                self._language_tool = language_tool_python.LanguageTool(lt_lang)
                return True
                
            except Exception as e:
                self.logger.error(f"Falha ao inicializar LanguageTool: {e}")
                self.logger.error("Certifique-se que Java está instalado: sudo apt install default-jre")
                return False
        
        return True
    
    def _detect_english_residual(self, text: str) -> bool:
        """
        Detecta se o texto contém inglês residual.
        
        Args:
            text: Texto para analisar
            
        Returns:
            True se detectar inglês, False caso contrário
        """
        if not LANGDETECT_AVAILABLE:
            # Fallback simples: verifica palavras comuns em inglês
            english_words = ['the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for']
            words = text.lower().split()
            english_count = sum(1 for word in words if word in english_words)
            return english_count > len(words) * 0.3
        
        try:
            # Detecta apenas se tiver mais de 3 palavras para evitar falsos positivos
            if len(text.split()) > 3:
                detected = detect(text)
                return detected == 'en'
        except LangDetectException:
            pass
        
        return False
    
    def _translate_residual_english(self, text: str) -> str:
        """
        Traduz texto residual em inglês.
        
        Args:
            text: Texto para traduzir
            
        Returns:
            Texto traduzido ou original se falhar
        """
        try:
            # Usa o tradutor principal se disponível
            from .translator import BMADTranslator
            
            translator = BMADTranslator(self.settings)
            return translator._translate_text(text, 'en', self.settings.get_target_language())
            
        except Exception as e:
            self.logger.warning(f"Falha na tradução residual: {e}")
            return text
    
    def _contains_technical_terms(self, text: str) -> bool:
        """
        Verifica se o texto contém termos técnicos.
        
        Args:
            text: Texto para analisar
            
        Returns:
            True se contiver termos técnicos
        """
        text_lower = text.lower()
        return any(term.lower() in text_lower for term in self._technical_terms)
    
    def _is_structured_line(self, line: str) -> bool:
        """
        Verifica se a linha tem estrutura que não deve ser alterada.
        
        Args:
            line: Linha para analisar
            
        Returns:
            True se for linha estruturada
        """
        stripped = line.strip()
        
        # Headers Markdown
        if stripped.startswith('#'):
            return True
        
        # Listas
        if stripped.startswith(('-', '*', '+')):
            return True
        
        # Listas numeradas
        if re.match(r'^\s*\d+\.', stripped):
            return True
        
        # Blockquotes
        if stripped.startswith('>'):
            return True
        
        # Links e imagens
        if stripped.startswith(('!', '[')):
            return True
        
        # HTML puro
        if stripped.startswith('<') and stripped.endswith('>'):
            return True
        
        # URLs
        if stripped.startswith(('http://', 'https://', 'www.', 'ftp://', 'mailto:')):
            return True
        
        return False
    
    def _should_refine_line(self, line: str) -> bool:
        """
        Determina se uma linha deve ser refinada.
        
        Args:
            line: Linha para analisar
            
        Returns:
            True se deve ser refinada
        """
        stripped = line.strip()
        
        # Ignora linhas vazias
        if not stripped:
            return False
        
        # Ignora linhas estruturadas
        if self._is_structured_line(line):
            return False
        
        # Ignora se tiver termos técnicos
        if self._contains_technical_terms(stripped):
            return False
        
        # Ignora linhas muito curtas (provavelmente código ou marcação)
        if len(stripped) <= 5:
            return False
        
        return True
    
    def _apply_grammar_correction(self, text: str) -> str:
        """
        Aplica correção gramatical usando LanguageTool.
        
        Args:
            text: Texto para corrigir
            
        Returns:
            Texto corrigido ou original se falhar
        """
        if not self._ensure_language_tool():
            return text
        
        try:
            corrected = self._language_tool.correct(text)
            
            # Verifica se a correção não alterou drasticamente o texto
            if abs(len(corrected) - len(text)) <= len(text) * 0.4:
                return corrected
            else:
                self.logger.warning("Correção gramatical alterou drasticamente o texto, mantendo original")
                return text
                
        except Exception as e:
            self.logger.warning(f"Falha na correção gramatical: {e}")
            return text
    
    def refine_text(self, text: str) -> str:
        """
        Refina um texto traduzido.
        
        Args:
            text: Texto para refinar
            
        Returns:
            Texto refinado
        """
        if not text.strip():
            return text
        
        # Passo 1: Detecta e traduz inglês residual
        if self._detect_english_residual(text):
            self.logger.info("Detectado inglês residual, aplicando tradução...")
            text = self._translate_residual_english(text)
        
        # Passo 2: Aplica correção gramatical se apropriado
        if self._should_refine_line(text):
            text = self._apply_grammar_correction(text)
        
        return text
    
    def refine_file(self, filepath: str) -> bool:
        """
        Refina um arquivo traduzido.
        
        Args:
            filepath: Caminho do arquivo para refinar
            
        Returns:
            True se o arquivo foi modificado, False caso contrário
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            new_lines = []
            in_frontmatter = False
            in_codeblock = False
            frontmatter_sep_count = 0
            modified = False
            
            for i, line in enumerate(lines):
                stripped = line.strip()
                
                # Frontmatter (YAML no topo)
                if i == 0 and stripped == '---':
                    in_frontmatter = True
                    frontmatter_sep_count += 1
                    new_lines.append(line)
                    continue
                
                if in_frontmatter:
                    if stripped == '---':
                        frontmatter_sep_count += 1
                        if frontmatter_sep_count == 2:
                            in_frontmatter = False
                    new_lines.append(line)
                    continue
                
                # Codeblocks
                if stripped.startswith('```'):
                    in_codeblock = not in_codeblock
                    new_lines.append(line)
                    continue
                
                if in_codeblock:
                    new_lines.append(line)
                    continue
                
                # Processa linha
                original_line = line
                refined_line = line
                
                if self._should_refine_line(stripped):
                    # Passo A: Tenta traduzir inglês residual
                    if self._detect_english_residual(stripped):
                        try:
                            refined_line = self._translate_residual_english(stripped)
                            refined_line += '\n' if line.endswith('\n') else ''
                        except Exception:
                            refined_line = original_line
                    
                    # Passo B: Aplica correção gramatical
                    if refined_line and len(stripped) > 5:
                        try:
                            corrected = self._apply_grammar_correction(stripped)
                            if corrected:
                                refined_line = corrected + '\n' if line.endswith('\n') else ''
                        except Exception:
                            pass
                
                if refined_line != original_line:
                    modified = True
                    new_lines.append(refined_line)
                else:
                    new_lines.append(original_line)
            
            # Salva se modificado
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.writelines(new_lines)
                self.logger.info(f"Arquivo refinado: {os.path.basename(filepath)}")
                return True
            else:
                self.logger.debug(f"Arquivo não necessitou refinamento: {os.path.basename(filepath)}")
                return False
                
        except Exception as e:
            self.logger.error(f"Erro ao refinar arquivo {filepath}: {e}")
            return False
    
    def refine_directory(self, base_dir: str = '.') -> Dict[str, bool]:
        """
        Refina todos os arquivos em um diretório.
        
        Args:
            base_dir: Diretório base para refinamento
            
        Returns:
            Dicionário com resultados por arquivo
        """
        results = {}
        suffix = self.settings.get_output_suffix()
        
        # Procura apenas arquivos já traduzidos
        for root, dirs, files in os.walk(base_dir):
            skip_dirs = set(self.settings.get_skip_directories())
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            
            for file in files:
                if file.endswith(('.md', '.markdown')) and suffix in file:
                    filepath = os.path.join(root, file)
                    try:
                        modified = self.refine_file(filepath)
                        results[filepath] = modified
                    except Exception as e:
                        self.logger.error(f"Erro ao processar {filepath}: {e}")
                        results[filepath] = False
        
        modified_count = sum(1 for modified in results.values() if modified)
        total_count = len(results)
        
        self.logger.info(f"Refinamento concluído: {modified_count}/{total_count} arquivos modificados")
        
        return results
    
    def close(self) -> None:
        """Fecha recursos do LanguageTool."""
        if self._language_tool:
            try:
                self._language_tool.close()
                self._language_tool = None
            except Exception as e:
                self.logger.warning(f"Erro ao fechar LanguageTool: {e}")
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
    
    def __repr__(self) -> str:
        """Representação string do objeto."""
        status = "inicializado" if self._language_tool else "não inicializado"
        return f"BMADRefiner(target_lang='{self.settings.get_target_language()}', status='{status}')"
