# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: guilmira <guilmira@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 16:27:56 by guilmira          #+#    #+#              #
#    Updated: 2026/03/25 16:42:56 by guilmira         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#Basic Makefile, learning purposes

VIRTUAL_ENV_NAME = virtual
#--------------------------------------------------------------------------------------------------------------SOURCES
SRCS1 = 0-prediction_phase.py
SCRS2 = 1-training_phase.py
#--------------------------------------------------------------------------------------------------------------RULES

all: install activate run

install:
	@test -d $(VIRTUAL_ENV_NAME) || python3 -m venv $(VIRTUAL_ENV_NAME)
#solo crea entorno si el entorno no existe

activate:
	source $(VIRTUAL_ENV_NAME)/bin/activate

deactivate:
	deactivate

run:
	deactivate

clean:
