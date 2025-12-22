"""
BMAD Translation System

Um sistema completo de tradução offline para documentação BMAD
com suporte a Markdown, YAML, JSON e TOML.
"""

__version__ = "2.0.0"
__author__ = "BMAD Team"
__description__ = "Sistema de tradução offline para documentação BMAD"

from .core.translator import BMADTranslator
from .core.refiner import BMADRefiner
from .core.protector import ContentProtector
from .core.validator import FileValidator

__all__ = [
    "BMADTranslator",
    "BMADRefiner", 
    "ContentProtector",
    "FileValidator"
]
