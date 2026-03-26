# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: guilmira <guilmira@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 16:27:56 by guilmira          #+#    #+#              #
#    Updated: 2026/03/26 12:33:56 by guilmira         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#Basic Makefile, learning purposes
VIRTUAL_ENV_NAME = virtual
#--------------------------------------------------------------------------------------------------------------VERSION
PYTHON_OS= python3 #cambiar si el OS tiene otro nombre para el interprete de python (usar v3)
#--------------------------------------------------------------------------------------------------------------SOURCES
SRC1 = prediction_phase.py
SRC2 = training_phase.py
SRC3 = plot_phase.py
DEPS = matplotlib pandas
#--------------------------------------------------------------------------------------------------------------RULES
#Sobre test
#test + CONDITION = TRUE OR FALSE
#test -d = la CONDITION es si existe o no el directorio

all: install help

install:
	@test -d $(VIRTUAL_ENV_NAME) || $(PYTHON_OS) -m venv $(VIRTUAL_ENV_NAME)

help:
	@echo "Comandos para activar y desactivar el entorno virtual del proyecto:"
	@echo "Para activar: 		 'source $(VIRTUAL_ENV_NAME)/bin/activate'"
	@echo "Para desactivar: 	 'deactivate' para salir"

deps:
	@test -d $(VIRTUAL_ENV_NAME) || { echo "No existe el entorno virtual. Ejecuta 'make install' primero."; exit 1; }
	@test "$$VIRTUAL_ENV" = "$(PWD)/$(VIRTUAL_ENV_NAME)" || { echo "No estás dentro del entorno virtual. Haz 'make help' primero y activa el entorno"; exit 1; }
	pip install --upgrade --quiet $(DEPS)

bonus: deps
	$(PYTHON_OS) $(SRC3)
	
run:
	@test -d $(VIRTUAL_ENV_NAME) || { echo "No existe el entorno virtual. Ejecuta 'make install' primero."; exit 1; }
	@test "$$VIRTUAL_ENV" = "$(PWD)/$(VIRTUAL_ENV_NAME)" || { echo "No estás dentro del entorno virtual. Haz 'make help' primero y activa el entorno"; exit 1; }
	$(PYTHON_OS) $(SRC2)
	$(PYTHON_OS) $(SRC1)

clean:
	@rm -rf __pycache__
	@rm -rf theta.txt result.png
	
fclean: clean
	@rm -rf $(VIRTUAL_ENV_NAME)
