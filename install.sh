#!/bin/bash

# Nombre del entorno virtual
FOLDER_NAME="venv"

# Comprobar que el script se ejecute con source
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "This script must be sourced. Use: . ${0}" >&2
  exit 1
fi

# Actualizar repositorios y asegurarse de tener Python y pip
sudo apt update
sudo apt install -y python3 python3-venv python3-pip

# Crear entorno virtual si no existe
if [ ! -d "$FOLDER_NAME" ]; then
  python3 -m venv $FOLDER_NAME
  echo "Virtual environment '$FOLDER_NAME' created."
fi

# Activar el entorno virtual
source $FOLDER_NAME/bin/activate

# Instalar paquetes desde requirements.txt si existe
if [ -f "requirements.txt" ]; then
  python3 -m pip install --upgrade pip
  python3 -m pip install -r requirements.txt
else
  echo "No requirements.txt found. Skipping package installation."
fi