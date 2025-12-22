#!/usr/bin/env python3
"""
Script de validação da instalação do BMAD Translation System
Verifica se todas as dependências e componentes estão funcionando corretamente
"""

import sys
import os
import subprocess
import importlib
from pathlib import Path
from typing import Dict, List, Tuple


def check_python_version() -> Tuple[bool, str]:
    """Verifica a versão do Python."""
    version = sys.version_info
    if version >= (3, 8):
        return True, f"Python {version.major}.{version.minor}.{version.micro}"
    else:
        return False, f"Python {version.major}.{version.minor}.{version.micro} (mínimo: 3.8)"


def check_package(package_name: str, import_name: str = None) -> Tuple[bool, str]:
    """
    Verifica se um pacote Python está instalado.
    
    Args:
        package_name: Nome do pacote para exibição
        import_name: Nome para importação (se diferente)
        
    Returns:
        Tuple de (instalado, versão/detalhe)
    """
    import_name = import_name or package_name
    
    try:
        module = importlib.import_module(import_name)
        
        # Tenta obter versão
        version = getattr(module, '__version__', None)
        if version is None:
            version = getattr(module, 'VERSION', None)
        if version is None:
            version = "desconhecida"
        
        return True, f"{package_name} v{version}"
        
    except ImportError:
        return False, f"{package_name} não encontrado"
    except Exception as e:
        return False, f"{package_name}: erro - {e}"


def check_java() -> Tuple[bool, str]:
    """Verifica se Java está instalado."""
    try:
        result = subprocess.run(
            ['java', '-version'], 
            capture_output=True, 
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            version_info = result.stderr or result.stdout
            return True, f"Java {version_info.strip()}"
        else:
            return False, "Java não encontrado"
            
    except FileNotFoundError:
        return False, "Java não encontrado no PATH"
    except subprocess.TimeoutExpired:
        return False, "Java: timeout ao verificar versão"
    except Exception as e:
        return False, f"Java: erro - {e}"


def check_argos_models() -> Tuple[bool, str]:
    """Verifica se os modelos Argos Translate estão instalados."""
    try:
        import argostranslate.package
        installed = argostranslate.package.get_installed_packages()
        
        if installed:
            models = [f"{pkg.from_code}->{pkg.to_code}" for pkg in installed]
            return True, f"Modelos: {', '.join(models)}"
        else:
            return False, "Nenhum modelo Argos instalado"
            
    except ImportError:
        return False, "Argos Translate não instalado"
    except Exception as e:
        return False, f"Argos Translate: erro - {e}"


def check_languagetool() -> Tuple[bool, str]:
    """Verifica se LanguageTool está funcionando."""
    try:
        import language_tool_python
        
        # Tenta instanciar
        tool = language_tool_python.LanguageTool('pt-PT')
        tool.close()
        return True, "LanguageTool funcionando"
        
    except ImportError:
        return False, "LanguageTool não instalado"
    except Exception as e:
        return False, f"LanguageTool: erro - {e}"


def check_file_structure() -> List[Tuple[bool, str]]:
    """Verifica a estrutura de arquivos do projeto."""
    base_path = Path(__file__).parent.parent
    checks = []
    
    # Diretórios essenciais
    essential_dirs = [
        'src/bmad_translate',
        'config',
        'scripts',
        'tests',
        'data'
    ]
    
    for dir_path in essential_dirs:
        full_path = base_path / dir_path
        if full_path.exists() and full_path.is_dir():
            checks.append((True, f"Diretório {dir_path}/ existe"))
        else:
            checks.append((False, f"Diretório {dir_path}/ não encontrado"))
    
    # Arquivos de configuração
    essential_files = [
        'config/default_settings.yaml',
        'config/protection_patterns.yaml',
        'config/language_mappings.yaml',
        'requirements.txt'
    ]
    
    for file_path in essential_files:
        full_path = base_path / file_path
        if full_path.exists() and full_path.is_file():
            checks.append((True, f"Arquivo {file_path} existe"))
        else:
            checks.append((False, f"Arquivo {file_path} não encontrado"))
    
    # Módulos Python
    essential_modules = [
        'src/bmad_translate/__init__.py',
        'src/bmad_translate/core/__init__.py',
        'src/bmad_translate/config/__init__.py'
    ]
    
    for module_path in essential_modules:
        full_path = base_path / module_path
        if full_path.exists():
            checks.append((True, f"Módulo {module_path} existe"))
        else:
            checks.append((False, f"Módulo {module_path} não encontrado"))
    
    return checks


def check_permissions() -> List[Tuple[bool, str]]:
    """Verifica permissões de escrita em diretórios importantes."""
    base_path = Path(__file__).parent.parent
    checks = []
    
    # Verifica permissão de escrita
    test_dirs = ['data/logs', 'data/cache', 'data/models']
    
    for dir_path in test_dirs:
        full_path = base_path / dir_path
        
        # Tenta criar diretório se não existir
        try:
            full_path.mkdir(parents=True, exist_ok=True)
            
            # Tenta escrever um arquivo de teste
            test_file = full_path / '.permission_test'
            test_file.write_text('test')
            test_file.unlink()
            
            checks.append((True, f"Permissão de escrita em {dir_path}/ OK"))
            
        except PermissionError:
            checks.append((False, f"Sem permissão de escrita em {dir_path}/"))
        except Exception as e:
            checks.append((False, f"Erro ao verificar permissões em {dir_path}: {e}"))
    
    return checks


def run_comprehensive_check():
    """Executa verificação completa da instalação."""
    print("🔍 VALIDAÇÃO COMPLETA DA INSTALAÇÃO")
    print("=" * 50)
    
    all_good = True
    
    # Verificação do Python
    print("\n🐍 Python:")
    python_ok, python_info = check_python_version()
    status = "✓" if python_ok else "✗"
    print(f"  {status} {python_info}")
    if not python_ok:
        all_good = False
    
    # Verificação de Java
    print("\n☕ Java:")
    java_ok, java_info = check_java()
    status = "✓" if java_ok else "✗"
    print(f"  {status} {java_info}")
    if not java_ok:
        all_good = False
    
    # Verificação de pacotes Python
    print("\n📦 Pacotes Python:")
    packages = [
        ('argostranslate', 'argostranslate'),
        ('language-tool-python', 'language_tool_python'),
        ('PyYAML', 'yaml'),
        ('tomli', 'tomli'),
        ('langdetect', 'langdetect'),
        ('tqdm', 'tqdm')
    ]
    
    for display_name, import_name in packages:
        pkg_ok, pkg_info = check_package(display_name, import_name)
        status = "✓" if pkg_ok else "✗"
        print(f"  {status} {pkg_info}")
        if not pkg_ok:
            all_good = False
    
    # Verificação dos modelos
    print("\n🤖 Modelos de Tradução:")
    argos_ok, argos_info = check_argos_models()
    status = "✓" if argos_ok else "✗"
    print(f"  {status} {argos_info}")
    if not argos_ok:
        all_good = False
    
    lt_ok, lt_info = check_languagetool()
    status = "✓" if lt_ok else "✗"
    print(f"  {status} {lt_info}")
    if not lt_ok:
        all_good = False
    
    # Verificação da estrutura de arquivos
    print("\n📁 Estrutura de Arquivos:")
    file_checks = check_file_structure()
    for check_ok, check_info in file_checks:
        status = "✓" if check_ok else "✗"
        print(f"  {status} {check_info}")
        if not check_ok:
            all_good = False
    
    # Verificação de permissões
    print("\n🔐 Permissões:")
    perm_checks = check_permissions()
    for check_ok, check_info in perm_checks:
        status = "✓" if check_ok else "✗"
        print(f"  {status} {check_info}")
        if not check_ok:
            all_good = False
    
    # Resumo
    print("\n" + "=" * 50)
    if all_good:
        print("🎉 INSTALAÇÃO PERFEITA!")
        print("Todos os componentes estão funcionando corretamente.")
        print("\nPróximos passos:")
        print("1. Execute: python scripts/warmup_models.py")
        print("2. Teste: python -m bmad_translate.cli --help")
        return 0
    else:
        print("❌ PROBLEMAS DETECTADOS!")
        print("Alguns componentes precisam de atenção.")
        print("\nSoluções sugeridas:")
        
        if not python_ok:
            print("- Instale Python 3.8+")
        if not java_ok:
            print("- Instale Java Runtime Environment")
        if not argos_ok:
            print("- Execute: python scripts/warmup_models.py")
        if not lt_ok:
            print("- Verifique instalação do Java e LanguageTool")
        
        for check_ok, check_info in file_checks:
            if not check_ok:
                print(f"- {check_info}")
        
        return 1


def main():
    """Função principal."""
    try:
        return run_comprehensive_check()
    except KeyboardInterrupt:
        print("\n\n⚠️ Validação interrompida pelo usuário.")
        return 1
    except Exception as e:
        print(f"\n\n💥 Erro inesperado na validação: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
