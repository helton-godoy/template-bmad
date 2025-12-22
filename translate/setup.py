"""
Setup do BMAD Translation System
"""

from setuptools import setup, find_packages
from pathlib import Path

# Lê o README para long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding='utf-8') if readme_file.exists() else ""

# Lê requirements.txt para dependências
requirements_file = Path(__file__).parent / "requirements.txt"
install_requires = []

if requirements_file.exists():
    with open(requirements_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                install_requires.append(line)

setup(
    name="bmad-translate",
    version="2.0.0",
    description="Sistema completo de tradução offline para documentação BMAD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="BMAD Team",
    author_email="bmad@example.com",
    url="https://github.com/bmad/bmad-translate",
    project_urls={
        "Bug Tracker": "https://github.com/bmad/bmad-translate/issues",
        "Documentation": "https://github.com/bmad/bmad-translate/wiki",
        "Source Code": "https://github.com/bmad/bmad-translate",
    },
    packages=find_packages(where="src"),
    package_dir="src",
    include_package_data=True,
    package_data={
        "bmad_translate": [
            "config/*.yaml",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Documentation",
    ],
    python_requires=">=3.8",
    install_requires=install_requires,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "bmad-translate=bmad_translate.cli.main:main",
        ],
    },
    keywords="translation, localization, i18n, documentation, bmad, offline, argos-translate, language-tool",
    zip_safe=False,
    license="MIT",
)
