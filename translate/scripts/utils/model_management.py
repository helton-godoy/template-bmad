#!/usr/bin/env python3
"""
Script de preparação de modelos de tradução
Baixa e instala os modelos necessários para o BMAD Translation System
"""

import sys
import os
import logging
from pathlib import Path

# Adiciona o src ao path para importar módulos
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

try:
    import argostranslate.package
    import language_tool_python
except ImportError as e:
    print(f"Erro: Dependência não encontrada - {e}")
    print("Instale as dependências com: pip install -r requirements.txt")
    sys.exit(1)


def setup_logging():
    """Configura logging para o script."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def download_argos_models(from_code='en', to_code='pt'):
    """
    Baixa e instala modelos Argos Translate.
    
    Args:
        from_code: Código do idioma de origem
        to_code: Código do idioma de destino
    """
    print(f"[Argos] Atualizando índice de pacotes...")
    argostranslate.package.update_package_index()
    
    available_packages = argostranslate.package.get_available_packages()
    installed_packages = argostranslate.package.get_installed_packages()
    
    # Verifica se o pacote já está instalado
    is_installed = any(
        p.from_code == from_code and p.to_code == to_code 
        for p in installed_packages
    )
    
    if is_installed:
        print(f"[Argos] Modelo {from_code}->{to_code} já está instalado.")
        return True
    
    # Procura pacote direto
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code,
            available_packages
        ), None
    )
    
    if package_to_install:
        print(f"[Argos] Baixando modelo {from_code}->{to_code}... Isso pode demorar.")
        try:
            pkg_path = package_to_install.download()
            argostranslate.package.install_from_path(pkg_path)
            print(f"[Argos] Instalação concluída.")
            return True
        except Exception as e:
            print(f"[Erro] Falha ao baixar/instalar modelo: {e}")
            return False
    else:
        print(f"[Erro] Não foi encontrado pacote para {from_code}->{to_code}")
        return False


def download_languagetool_server():
    """Baixa e configura o servidor LanguageTool."""
    print("[LanguageTool] Verificando/baixando servidor local Java...")
    
    try:
        # Ao instanciar a classe, ele verifica se o .jar existe; se não, baixa
        tool = language_tool_python.LanguageTool('pt-BR')
        tool.close()
        print("[LanguageTool] Servidor pronto.")
        return True
    except Exception as e:
        print(f"[Erro] Falha ao configurar LanguageTool: {e}")
        print("Certifique-se que instalou o Java (sudo apt install default-jre).")
        return False


def verify_installation():
    """Verifica se as dependências estão corretamente instaladas."""
    print("\n--- VERIFICANDO INSTALAÇÃO ---")
    
    # Verifica Argos Translate
    try:
        argostranslate.package.update_package_index()
        installed = argostranslate.package.get_installed_packages()
        if installed:
            print(f"✓ Argos Translate: {len(installed)} pacotes instalados")
            for pkg in installed:
                print(f"  - {pkg.from_code}->{pkg.to_code}")
        else:
            print("✗ Argos Translate: Nenhum pacote instalado")
    except Exception as e:
        print(f"✗ Argos Translate: Erro - {e}")
    
    # Verifica LanguageTool
    try:
        tool = language_tool_python.LanguageTool('pt-BR')
        tool.close()
        print("✓ LanguageTool: Funcionando")
    except Exception as e:
        print(f"✗ LanguageTool: Erro - {e}")
    
    # Verifica Java
    try:
        import subprocess
        result = subprocess.run(['java', '-version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stderr or result.stdout
            print(f"✓ Java: {version.strip()}")
        else:
            print("✗ Java: Não encontrado")
    except FileNotFoundError:
        print("✗ Java: Não encontrado no PATH")
    except Exception as e:
        print(f"✗ Java: Erro - {e}")


def main():
    """Função principal do script."""
    print("--- PREPARAÇÃO DE MODELOS BMAD TRANSLATE ---")
    setup_logging()
    
    success = True
    
    # Download de modelos Argos Translate
    if not download_argos_models('en', 'pt'):
        success = False
    
    # Configuração do LanguageTool
    if not download_languagetool_server():
        success = False
    
    # Verificação final
    verify_installation()
    
    if success:
        print("\n--- PREPARAÇÃO CONCLUÍDA COM SUCESSO ---")
        print("Os modelos estão prontos para uso!")
        return 0
    else:
        print("\n--- PREPARAÇÃO CONCLUÍDA COM ERROS ---")
        print("Verifique os erros acima e tente novamente.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
