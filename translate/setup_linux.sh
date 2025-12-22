#!/bin/bash

# Parar se houver erro
set -e

echo ">>> 1. A atualizar pacotes do sistema..."
sudo apt-get update

echo ">>> 2. A instalar dependências de sistema (Java e Python e Venv)..."
# default-jre é necessário para o language-tool-python rodar localmente
sudo apt-get install -y python3 python3-pip python3-venv default-jre

echo ">>> 3. A criar Ambiente Virtual Python (.venv)..."
if [ ! -d ".venv" ]; then
	python3 -m venv .venv
	echo "Ambiente virtual criado."
else
	echo "Ambiente virtual já existe."
fi

echo ">>> 4. A instalar dependências Python..."
# Ativar o venv
source .venv/bin/activate

# Atualizar pip
pip install --upgrade pip

# Instalar bibliotecas via requirements centralizado
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "Aviso: requirements.txt não encontrado. Instalando deps padrão..."
    pip install argostranslate language-tool-python langdetect pyyaml tqdm tomli tomli-w
fi

echo ">>> 5. A preparar modelos (Download inicial)..."
# Executa o script de warmup existente para baixar os dicionários e servidor LT
if [ -f "scripts/warmup_models.py" ]; then
    python3 scripts/warmup_models.py
else
    echo "Aviso: scripts/warmup_models.py não encontrado."
fi

echo "----------------------------------------------------"
echo "CONCLUÍDO! Para começar a usar, digite:"
echo "source .venv/bin/activate"
echo "----------------------------------------------------"
