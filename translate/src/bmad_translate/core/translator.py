"""
Módulo principal de tradução do sistema BMAD
"""

import os
import re
import sys
import tempfile
import shutil
import logging
import yaml
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass

# Importação condicional do TOML
if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

try:
    import tomli_w
except ImportError:
    tomli_w = None

import argostranslate.package
import argostranslate.translate

from .protector import ContentProtector
from ..config.settings import Settings


@dataclass
class TranslationResult:
    """Resultado de uma operação de tradução."""
    success: bool
    source_file: str
    target_file: str
    error_message: Optional[str] = None
    placeholders_count: int = 0
    content_length: int = 0


class _IndentDumper(yaml.SafeDumper):
    """Dumper personalizado para forçar indentação em listas YAML."""
    def increase_indent(self, flow=False, indentless=False):
        return super(_IndentDumper, self).increase_indent(flow, False)


class BMADTranslator:
    """Tradutor principal do sistema BMAD."""
    
    def __init__(self, settings: Optional[Settings] = None):
        """
        Inicializa o tradutor BMAD.
        
        Args:
            settings: Configurações do sistema
        """
        self.settings = settings or Settings()
        self.protector = ContentProtector(self.settings)
        self.logger = self._setup_logging()
        self._argos_initialized = False
        
    def _setup_logging(self) -> logging.Logger:
        """Configura o logging seguro."""
        logger = logging.getLogger(__name__)
        
        if not logger.handlers:
            log_settings = self.settings.get_logging_settings()
            
            logger.setLevel(getattr(logging, log_settings.get('level', 'INFO')))
            
            # Handler para arquivo
            log_file = log_settings.get('main_log_file', 'data/logs/translation.log')
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setFormatter(logging.Formatter(
                log_settings.get('format', '%(asctime)s - %(levelname)s - %(message)s')
            ))
            logger.addHandler(file_handler)
            
            # Handler para console
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter(
                '%(levelname)s: %(message)s'
            ))
            logger.addHandler(console_handler)
            
            # Filtro de segurança
            if log_settings.get('enable_secure_filter', True):
                logger.addFilter(self._secure_filter)
        
        return logger
    
    def _secure_filter(self, record: logging.LogRecord) -> bool:
        """Filtra informações sensíveis dos logs."""
        message = record.getMessage().lower()
        sensitive_patterns = [
            '/etc/', '/usr/', '/var/', '/home/', '/root/',
            'password', 'secret', 'key', 'token', 'auth'
        ]
        
        for pattern in sensitive_patterns:
            if pattern in message:
                record.msg = "Informação sensível removida do log"
                break
        
        return True
    
    def _ensure_argos_initialized(self) -> None:
        """Garante que o Argos Translate está inicializado."""
        if not self._argos_initialized:
            self.logger.info("Verificando pacotes de idioma Argos Translate...")
            argostranslate.package.update_package_index()
            
            available_packages = argostranslate.package.get_available_packages()
            installed_packages = argostranslate.package.get_installed_packages()
            
            target_lang = self.settings.get_target_language()
            
            # Verifica se o pacote en->target está instalado
            is_installed = any(
                p.from_code == 'en' and p.to_code == target_lang 
                for p in installed_packages
            )
            
            if not is_installed:
                self.logger.info(f"Instalando pacote de idioma English -> {target_lang}...")
                try:
                    package_to_install = next(
                        filter(
                            lambda x: x.from_code == 'en' and x.to_code == target_lang,
                            available_packages
                        )
                    )
                    pkg_path = package_to_install.download()
                    argostranslate.package.install_from_path(pkg_path)
                    self.logger.info("Pacote de idioma instalado com sucesso.")
                except StopIteration:
                    self.logger.error(f"Pacote de idioma en->{target_lang} não encontrado.")
                    raise RuntimeError(f"Pacote en->{target_lang} não disponível")
            else:
                self.logger.info("Pacote de idioma já instalado.")
            
            self._argos_initialized = True
    
    def _validate_path(self, filepath: str) -> str:
        """Valida se o caminho está dentro do diretório permitido."""
        if self.settings.is_path_validation_enabled():
            allowed_base = self.settings.get_allowed_base_dir() or os.getcwd()
            
            if not filepath:
                raise ValueError("Caminho vazio não é permitido")
            
            # Resolve caminhos reais, prevenindo symlinks
            abs_path = os.path.realpath(filepath)
            abs_base = os.path.realpath(allowed_base)
            
            # Verifica se o caminho está dentro da base permitida
            try:
                common = os.path.commonpath([abs_base, abs_path])
            except ValueError:
                raise ValueError("Caminho em drive diferente não autorizado")
            
            if common != abs_base:
                self.logger.error(f"Tentativa de Path Traversal: {filepath}")
                raise ValueError(f"Acesso negado: {filepath} fora de {allowed_base}")
            
            # Verifica se é um arquivo regular
            if not os.path.isfile(abs_path):
                raise ValueError(f"Caminho não é um arquivo regular: {filepath}")
            
            return abs_path
        
        return filepath
    
    def _sanitize_input(self, text: str) -> str:
        """Sanitiza entrada mantendo integridade do conteúdo."""
        if not text:
            return ""
        
        max_length = self.settings.get_max_text_length()
        
        # Limita tamanho
        if len(text) > max_length:
            self.logger.warning(f"Texto truncado: {len(text)} > {max_length}")
            text = text[:max_length]
        
        # Remove apenas caracteres de controle que podem causar falhas
        return text.replace('\0', '')
    
    def _translate_text(self, text: str, from_lang: str = 'en', to_lang: str = None, protect: bool = False) -> str:
        """
        Traduz texto usando Argos Translate.
        
        Args:
            text: Texto a traduzir
            from_lang: Idioma origem
            to_lang: Idioma destino
            protect: Se True, aplica proteção de conteúdo antes da tradução
        """
        if not text.strip():
            return ""
        
        if to_lang is None:
            to_lang = self.settings.get_target_language()
        
        # Sanitiza entrada
        if self.settings.is_input_sanitization_enabled():
            safe_text = self._sanitize_input(text)
        else:
            safe_text = text
        
        if not safe_text:
            return text

        # Aplica proteção se solicitado
        if protect:
            safe_text = self.protector.protect_content(safe_text)
        
        try:
            # Prepara conteúdo: Substitui marcadores de Markdown por caracteres de citação raros
            # para garantir que o tradutor os trate como limites de frase/palavra e não pontuação descartável.
            # Bold: "**text**" -> "«text»"
            # Italic: "*text*" -> "‹text›"
            
            # PROTEÇÃO: Títulos Markdown (#, ##, ###, etc.)
            # Argos Translate remove hashtags, então precisamos protegê-los
            # Substitui "# Título" por "[H1] Título", "## Título" por "[H2] Título", etc.
            # IMPORTANTE: Usar colchetes [] pois Argos os preserva (Unicode ⟨⟩ é removido)
            header_replacements = {}
            def protect_headers(match):
                level = len(match.group(1))  # Número de hashtags
                header_replacements[f"[H{level}]"] = match.group(1)  # Salva os hashtags originais
                return f"[H{level}] {match.group(2)}"  # [H1] Título (com espaço após marcador)
            
            prepped_text = re.sub(r'^(#{1,6})\s+(.+)$', protect_headers, safe_text, flags=re.MULTILINE)
            
            # PROTEÇÃO: Emojis Unicode
            # Argos Translate REMOVE emojis e quebra formatação adjacente
            # Substitui emojis por placeholders [EMJ0], [EMJ1], etc.
            emoji_map = {}
            emoji_count = 0
            
            # Regex para emojis Unicode comuns
            # Ranges: emoticons, símbolos, pictogramas, transporte, etc.
            EMOJI_PATTERN = r'[\U0001F300-\U0001F9FF\u2600-\u27BF\U0001F1E0-\U0001F1FF]'
            
            def protect_emoji(match):
                nonlocal emoji_count
                emoji = match.group(0)
                placeholder = f"[EMJ{emoji_count}]"
                emoji_map[placeholder] = emoji
                emoji_count += 1
                return placeholder
            
            prepped_text = re.sub(EMOJI_PATTERN, protect_emoji, prepped_text)
            
            # PROTEÇÃO: Tabelas Markdown
            # Argos Translate remove pipes | e destrói tabelas
            # Detecta e protege linhas de tabela inteiras
            table_lines = {}
            table_count = 0
            
            def protect_table_line(match):
                nonlocal table_count
                line = match.group(0)
                placeholder = f"[TBL{table_count}]"
                table_lines[placeholder] = line
                table_count += 1
                return placeholder
            
            # Regex para linhas de tabela Markdown (contém pipes)
            # Protege linhas que começam/terminam com | ou contêm | como delimitadores
            prepped_text = re.sub(r'^\s*\|.+\|\s*$', protect_table_line, prepped_text, flags=re.MULTILINE)
            
            
            # Bold (** ou __)
            # Captura o conteúdo dentro dos marcadores e substitui por guillemets
            prepped_text = re.sub(r'(\*\*|__)(?=[^\s])(.+?)(?<=[^\s])\1', r'«\2»', prepped_text)
            
            # Italic (* ou _) - Evita listas (*)
            # Usa lookbehind negativo para não pegar asteriscos que iniciam listas
            prepped_text = re.sub(r'(?<!\*)\b(\*|_)(?=[^\s])(.+?)(?<=[^\s])\1', r'‹\2›', prepped_text)
            
            # Garante que o Argos está inicializado
            self._ensure_argos_initialized()
            
            # Tradução offline direta
            translated = argostranslate.translate.translate(prepped_text, from_lang, to_lang)
            
            # Restaura os títulos ([H1] -> #, [H2] -> ##, etc.)
            def restore_headers(match):
                marker_level = match.group(1)  # H1, H2, etc. (sem colchetes)
                content = match.group(2)  # Título traduzido
                marker_key = f"[{marker_level}]"  # Adiciona colchetes para busca no dict
                hashes = header_replacements.get(marker_key, '#')  # Recupera hashtags originais
                return f"{hashes} {content}"
            
            translated = re.sub(r'\[(H\d)\]\s*(.+)$', restore_headers, translated, flags=re.MULTILINE)
            
            # Restaura os emojis ([EMJ0] -> emoji, [EMJ1] -> emoji, etc.)
            for placeholder, emoji in emoji_map.items():
                translated = translated.replace(placeholder, emoji)
            
            
            # Restaura as tabelas ([TBL0] -> linha de tabela original)
            for placeholder, table_line in table_lines.items():
                translated = translated.replace(placeholder, table_line)
            
            # Restaura os marcadores de Markdown dos guillemets
            # Italic: "‹text›" -> "*text*"
            # Bold: "«text»" -> "**text**"
            
            # Restaura itálico primeiro para evitar conflito com negrito
            translated = re.sub(r'‹(.+?)›', r'*\1*', translated)
            # Restaura negrito
            translated = re.sub(r'«(.+?)»', r'**\1**', translated)

            # Restaura proteção se foi aplicada
            if protect:
                translated = self.protector.restore_content(translated)
            
            # Correções finais de espaçamento Markdown
            translated = self._fix_markdown_spacing(translated)
            
            return translated
            
        except Exception as e:
            self.logger.error(f"Erro ao traduzir: {str(e)}")
            # Se falhar, tenta restaurar placeholders do original se protected
            if protect:
                return self.protector.restore_content(safe_text) 
            return text  # Fallback para original em erro
    

    def _fix_markdown_spacing(self, text: str) -> str:
        """Corrige espaçamentos inválidos gerados na tradução de Markdown."""
        
        # Restaura formatação de negrito/itálico que pode ter ganho espaços
        # Ex: "** texto **" -> "**texto**" (estratégia de padding reverso)
        # Handle bold (** or __)
        # IMPORTANTE: Não capturar entre DIFERENTES pares de **, apenas DENTRO de um par
        # Usa negative lookahead para garantir que não há ** no meio do conteúdo
        # CRÍTICO: Usar [ \t]+ em vez de \s+ para NÃO capturar quebras de linha (\n)
        text = re.sub(r'(\*\*|__)[ \t]+([^\s*](?:(?!\*\*|__).)*?[^\s*])[ \t]+\1', r'\1\2\1', text)
        # Handle italic (* or _) - cuidado para não pegar listas
        # Regex seguro para itálico: não começa com espaço/quebra de linha se for *
        text = re.sub(r'([^\s*])(\*|_)\s+([^\s].*?)\s+\2', r'\1\2\3\2', text)
        
        # Corrige abertura de negrito com espaço extra: (espaço)** (espaço) -> (espaço)**
        # Ex: " ** texto" -> " **texto"
        text = re.sub(r'(?:^|(?<=\s))\*\*\s+', '**', text)
        
        # Corrige fechamento de negrito com espaço extra antes de pontuação ou fim de linha
        # Ex: "texto **." -> "texto**."  ou "texto **  " -> "texto** "
        # IMPORTANTE: NÃO remover espaço se for seguido de texto normal ou outro negrito
        # CRÍTICO: Usar [ ]+ em vez de \s+ para NÃO capturar quebras de linha (\n)
        text = re.sub(r'(?<=\S)[ ]+\*\*(?=[.,!?:;]|$|\*\*)', '**', text)
        
        # Corrige links Markdown: [ texto](link ) -> [texto](link)
        text = re.sub(r'\[\s+(.*?)\s+\]', r'[\1]', text)
        
        # Corrige itálico (apenas _ para evitar quebrar listas com *)
        text = re.sub(r'_\s+(.*?)_', r'_\1_', text)
        text = re.sub(r'_(.*?)\s+_', r'_\1_', text)
        
        # Corrige espaçamento de listas: "  -  Item" -> "  - Item"
        # Garante conservação da indentação anterior e espaço único após o marcador
        text = re.sub(r'(\n|^)(\s*)([-*])\s+', r'\1\2\3 ', text)
        
        # Corrige espaçamento de títulos: "##  Texto" -> "## Texto"
        text = re.sub(r'^(#+)\s{2,}', r'\1 ', text, flags=re.MULTILINE)
        
        # Garante linha vazia antes de títulos (evita colagem com texto anterior)
        # Ex: "Texto\n# Título" -> "Texto\n\n# Título"
        text = re.sub(r'([^\n])\n(#+\s)', r'\1\n\n\2', text)
        
        # Garante linha vazia antes de blocos de código
        text = re.sub(r'([^\n])\n(```)', r'\1\n\n\2', text)

        # Corrige espaçamento de títulos quebrados pelo tradutor: "# # Título" -> "## Título"
        # Captura sequências de hashes separados por espaços no início da linha
        # Ex: "## # " -> "### "
        def fix_hashes(match):
            return match.group(1).replace(' ', '') + ' '
            
        text = re.sub(r'(?m)^(#(?:\s*#)+)(?=\s)', fix_hashes, text)
        
        # Garante espaço após os hashes normalizados se faltar
        text = re.sub(r'^(#+)([^#\s])', r'\1 \2', text, flags=re.MULTILINE)
        
        # Garante APENAS UM espaço após os hashes ("##  Titulo" -> "## Titulo")
        text = re.sub(r'^(#+)\s+', r'\1 ', text, flags=re.MULTILINE)

        return text

    def _process_markdown_file(self, filepath: str) -> TranslationResult:
        """Processa um arquivo Markdown."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except (IOError, OSError) as e:
            return TranslationResult(
                success=False,
                source_file=filepath,
                target_file="",
                error_message=f"Erro ao ler arquivo: {e}"
            )
        
        # Processa frontmatter separadamente
        frontmatter_match = re.search(r'^\s*---\n(.*?)\n---', content, re.DOTALL)
        
        if frontmatter_match:
            fm_text = frontmatter_match.group(0)
            fm_body = frontmatter_match.group(1)
            
            try:
                fm_data = yaml.safe_load(fm_body)
                
                # Traduz apenas campos selecionados
                translatable_keys = self.settings.get_translatable_keys()
                for key in translatable_keys:
                    if key in fm_data and isinstance(fm_data[key], str):
                        # Usa proteção para valores do frontmatter
                        fm_data[key] = self._translate_text(fm_data[key], protect=True)
                
                # Reconstrói o frontmatter
                new_fm = '---\n' + yaml.dump(
                    fm_data, 
                    Dumper=_IndentDumper, 
                    allow_unicode=True, 
                    default_flow_style=False, 
                    sort_keys=False
                ).strip() + '\n---'
                
                # Remove o frontmatter original do conteúdo para processar apenas o corpo
                # Isso é crucial para não misturar os escopos de proteção
                body_content = content[len(fm_text):]
                
                return self._translate_content_with_batches(body_content, filepath, prepend_content=new_fm)

            except Exception as e:
                self.logger.warning(f"Falha ao processar frontmatter: {e}")
        
        # Se não houve frontmatter ou falhou, processa tudo
        return self._translate_content_with_batches(content, filepath)
    
    def _translate_content_with_batches(self, content: str, filepath: str, prepend_content: str = "") -> TranslationResult:
        """Traduz conteúdo usando smart batching."""
        # 1. Proteção
        # Nota: protect_content limpa os placeholders anteriores, por isso o frontmatter
        # deve ser processado separadamente e passado via prepend_content
        protected_content = self.protector.protect_content(content)
        placeholders_count = self.protector.get_placeholder_count()
        
        # 2. Tradução com smart batching
        paragraphs = protected_content.split('\n\n')
        translated_paragraphs = []
        
        current_batch = []
        current_size = 0
        chunk_size = self.settings.get_safe_chunk_size()
        
        def process_batch():
            nonlocal current_batch
            if not current_batch:
                return
            
            batch_text = "\n\n".join(current_batch)
            translated_batch = self._translate_text(batch_text)
            
            if translated_batch:
                translated_paragraphs.append(translated_batch)
            else:
                # Falha total no batch, mantém original
                translated_paragraphs.extend(current_batch)
            
            current_batch = []
        
        for paragraph in paragraphs:
            if not paragraph.strip():
                if current_batch:
                    process_batch()
                    current_size = 0
                translated_paragraphs.append(paragraph)
                continue
            
            # Verifica se o parágrafo tem conteúdo traduzível
            has_content = self._has_translatable_content(paragraph)
            
            if not has_content:
                if current_batch:
                    process_batch()
                    current_size = 0
                translated_paragraphs.append(paragraph)
            else:
                # Adiciona ao batch
                if current_size + len(paragraph) > chunk_size:
                    process_batch()
                    current_size = 0
                
                current_batch.append(paragraph)
                current_size += len(paragraph)
        
        # Processa o que sobrou
        if current_batch:
            process_batch()
        
        translated_content = '\n\n'.join(translated_paragraphs)
        
        # 3. Restauração
        # Nota: fix_markdown_spacing deve vir por último para corrigir artefatos pós-restauração
        restored = self.protector.restore_content(translated_content)
        final_content = prepend_content + self._fix_markdown_spacing(restored)
        
        # 4. Salvar com escrita atômica
        return self._save_atomic(filepath, final_content, placeholders_count)
    
    def _has_translatable_content(self, paragraph: str) -> bool:
        """Verifica se o parágrafo tem conteúdo traduzível."""
        placeholders = self.protector.get_placeholders()
        
        for line in paragraph.split('\n'):
            line = line.strip()
            if line and line not in placeholders.values() and '__BMAD_P_' not in line:
                return True
        
        return False
    
    def _save_atomic(self, filepath: str, content: str, placeholders_count: int) -> TranslationResult:
        """Salva arquivo de forma atômica."""
        name, ext = os.path.splitext(filepath)
        suffix = self.settings.get_output_suffix()
        new_filepath = f"{name}{suffix}{ext}"
        
        try:
            # Escreve em arquivo temporário primeiro
            with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8', suffix=ext) as tmp:
                tmp.write(content)
                tmp.flush()
                
                # Move arquivo temporário para o destino (operação atômica)
                shutil.move(tmp.name, new_filepath)
            
            # Valida YAML se for arquivo YAML
            if new_filepath.endswith('.yaml'):
                try:
                    with open(new_filepath, 'r', encoding='utf-8') as f:
                        yaml.safe_load(f)
                    self.logger.info(f"Salvo e validado: {os.path.basename(new_filepath)}")
                except yaml.YAMLError as e:
                    self.logger.error(f"YAML inválido gerado: {e}")
                    return TranslationResult(
                        success=False,
                        source_file=filepath,
                        target_file=new_filepath,
                        error_message=f"YAML inválido: {e}",
                        placeholders_count=placeholders_count,
                        content_length=len(content)
                    )
            else:
                self.logger.info(f"Salvo: {os.path.basename(new_filepath)}")
            
            return TranslationResult(
                success=True,
                source_file=filepath,
                target_file=new_filepath,
                placeholders_count=placeholders_count,
                content_length=len(content)
            )
            
        except Exception as e:
            self.logger.error(f"Erro ao salvar arquivo {os.path.basename(new_filepath)}: {e}")
            return TranslationResult(
                success=False,
                source_file=filepath,
                target_file=new_filepath,
                error_message=f"Erro ao salvar: {e}",
                placeholders_count=placeholders_count,
                content_length=len(content)
            )
    
    def _process_yaml_file(self, filepath: str) -> TranslationResult:
        """Processa arquivo YAML de forma estruturada."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if not data:
                return TranslationResult(
                    success=True,
                    source_file=filepath,
                    target_file="",
                    error_message="Arquivo YAML vazio"
                )
            
            translated_data = self._recursive_translate_data(data)
            
            name, ext = os.path.splitext(filepath)
            suffix = self.settings.get_output_suffix()
            new_filepath = f"{name}{suffix}{ext}"
            
            with open(new_filepath, 'w', encoding='utf-8') as f:
                yaml.safe_dump(translated_data, f, allow_unicode=True, sort_keys=False)
            
            return TranslationResult(
                success=True,
                source_file=filepath,
                target_file=new_filepath,
                content_length=len(str(translated_data))
            )
            
        except Exception as e:
            return TranslationResult(
                success=False,
                source_file=filepath,
                target_file="",
                error_message=f"Erro ao processar YAML: {e}"
            )
    
    def _process_json_file(self, filepath: str) -> TranslationResult:
        """Processa arquivo JSON."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Tenta carregar, se falhar tenta limpar comentários
            try:
                data = json.loads(content)
            except json.JSONDecodeError:
                clean_content = self._strip_json_comments(content)
                data = json.loads(clean_content)
            
            if not data:
                return TranslationResult(
                    success=True,
                    source_file=filepath,
                    target_file="",
                    error_message="Arquivo JSON vazio"
                )
            
            translated_data = self._recursive_translate_data(data)
            
            name, ext = os.path.splitext(filepath)
            suffix = self.settings.get_output_suffix()
            new_filepath = f"{name}{suffix}{ext}"
            
            with open(new_filepath, 'w', encoding='utf-8') as f:
                json.dump(translated_data, f, ensure_ascii=False, indent=2)
            
            return TranslationResult(
                success=True,
                source_file=filepath,
                target_file=new_filepath,
                content_length=len(str(translated_data))
            )
            
        except Exception as e:
            return TranslationResult(
                success=False,
                source_file=filepath,
                target_file="",
                error_message=f"Erro ao processar JSON: {e}"
            )
    
    def _process_toml_file(self, filepath: str) -> TranslationResult:
        """Processa arquivo TOML."""
        if tomli_w is None:
            return TranslationResult(
                success=False,
                source_file=filepath,
                target_file="",
                error_message="Biblioteca tomli_w não instalada"
            )
        
        try:
            with open(filepath, 'rb') as f:
                data = tomllib.load(f)
            
            if not data:
                return TranslationResult(
                    success=True,
                    source_file=filepath,
                    target_file="",
                    error_message="Arquivo TOML vazio"
                )
            
            translated_data = self._recursive_translate_data(data)
            
            name, ext = os.path.splitext(filepath)
            suffix = self.settings.get_output_suffix()
            new_filepath = f"{name}{suffix}{ext}"
            
            with open(new_filepath, 'wb') as f:
                tomli_w.dump(translated_data, f)
            
            return TranslationResult(
                success=True,
                source_file=filepath,
                target_file=new_filepath,
                content_length=len(str(translated_data))
            )
            
        except Exception as e:
            return TranslationResult(
                success=False,
                source_file=filepath,
                target_file="",
                error_message=f"Erro ao processar TOML: {e}"
            )
    
    def _recursive_translate_data(self, data: Any) -> Any:
        """Percorre recursivamente a estrutura e traduz chaves permitidas."""
        translatable_keys = self.settings.get_translatable_keys()
        
        if isinstance(data, dict):
            new_data = {}
            for k, v in data.items():
                if k in translatable_keys and isinstance(v, str):
                    self.logger.info(f"Traduzindo chave '{k}'")
                    # Usa proteção para valores de campos estruturados
                    new_data[k] = self._translate_text(v, protect=True)
                else:
                    new_data[k] = self._recursive_translate_data(v)
            return new_data
        elif isinstance(data, list):
            return [self._recursive_translate_data(item) for item in data]
        else:
            return data
    
    def _strip_json_comments(self, content: str) -> str:
        """Remove comentários estilo C de JSONC."""
        # Remove comentários de bloco
        content = re.sub(r'/\*[\s\S]*?\*/', '', content)
        
        # Remove comentários de linha
        lines = content.split('\n')
        clean_lines = []
        for line in lines:
            if '//' in line:
                if 'http://' in line or 'https://' in line:
                    clean_lines.append(line)
                    continue
                
                parts = line.split('//')
                clean_lines.append(parts[0])
            else:
                clean_lines.append(line)
        
        return '\n'.join(clean_lines)
    
    def collect_files(self, base_dir: str = '.') -> List[str]:
        """Coleta arquivos respeitando as configurações."""
        collected = []
        skip_dirs = set(self.settings.get_skip_directories())
        extensions = tuple(self.settings.get_supported_extensions())
        suffix = self.settings.get_output_suffix()
        
        for root, dirs, files in os.walk(base_dir):
            # Remove diretórios ignorados in-place para podar a árvore
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            
            for f in files:
                if (f.endswith(extensions) and 
                    not f.endswith(f"{suffix}{os.path.splitext(f)[1]}")):
                    collected.append(os.path.join(root, f))
        
        return collected
    
    def translate_file(self, filepath: str) -> TranslationResult:
        """
        Traduz um único arquivo.
        
        Args:
            filepath: Caminho do arquivo a ser traduzido
            
        Returns:
            Resultado da tradução
        """
        try:
            # Valida caminho
            validated_path = self._validate_path(filepath)
            
            # Determina o tipo de arquivo
            ext = os.path.splitext(validated_path)[1].lower()
            
            self.logger.info(f"Processando: {os.path.basename(validated_path)}")
            
            if ext in ['.yaml', '.yml']:
                return self._process_yaml_file(validated_path)
            elif ext in ['.json', '.jsonc']:
                return self._process_json_file(validated_path)
            elif ext == '.toml':
                return self._process_toml_file(validated_path)
            else:
                return self._process_markdown_file(validated_path)
                
        except Exception as e:
            self.logger.error(f"Erro ao processar arquivo {filepath}: {e}")
            return TranslationResult(
                success=False,
                source_file=filepath,
                target_file="",
                error_message=str(e)
            )
    
    def translate_directory(self, base_dir: str = '.') -> List[TranslationResult]:
        """
        Traduz todos os arquivos em um diretório.
        
        Args:
            base_dir: Diretório base para tradução
            
        Returns:
            Lista de resultados da tradução
        """
        files = self.collect_files(base_dir)
        
        if not files:
            self.logger.info("Nenhum arquivo compatível encontrado.")
            return []
        
        self.logger.info(f"Encontrados {len(files)} arquivos. Iniciando tradução...")
        
        results = []
        for f in files:
            result = self.translate_file(f)
            results.append(result)
        
        return results
    
    def __repr__(self) -> str:
        """Representação string do objeto."""
        return f"BMADTranslator(target_lang='{self.settings.get_target_language()}')"
