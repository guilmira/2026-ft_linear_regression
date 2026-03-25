# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    prediction_phase.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: guilmira <guilmira@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 16:28:05 by guilmira          #+#    #+#              #
#    Updated: 2026/03/25 16:33:51 by guilmira         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


#Fase 1: prediccion. Necesita que la regresion lineal esté calculada

# ----- Función de predicción
def calculate_price(distance_km, slope, intercept):
    price_eu = slope * distance_km + intercept
    return price_eu

# ----- Función de printeo
def print_result(theta_set, predicted_price):
    if not theta_set:
       print("Aviso: no tenemos la regresión lineal. Para valores con sentido, entrena el modelo")
    
    if predicted_price < 0:
        print("Aviso: la regresion arroja valores negativos. Esperado debido a valor de la pendiente negativa. No utilizar")
    else:   
        print(f"Precio estimado: {predicted_price:.2f} (eu)")

def prize_prediction():

    # ----- 1. Leer archivo
    theta_file = 'theta.txt' #hardcode
    theta_set = False  # por defecto

    try:
        with open(theta_file, 'r') as f:
            lines = f.readlines()
            if len(lines) < 2:
                print("theta.txt no adecuado. Se usan valores por defecto.")
                intercept = 0
                slope = 0
            else:
                intercept = float(lines[0].strip())
                slope = float(lines[1].strip())
                theta_set = True
    except FileNotFoundError:
        # si no existe el archivo
        intercept = 0
        slope = 0
    except ValueError:
        # si los datos no son válidos
        print("theta.txt no adecuado. Se usan valores por defecto.")
        intercept = 0
        slope = 0

    # ----- 2. Inputs
    try:
        distance_input = input("Introduce la distancia del coche (km, >0): ")
        distance_km = float(distance_input)
        if distance_km <= 0:
            print("La distancia debe ser mayor que 0.")
            return
    except ValueError:
        print("Error: Debes introducir un número.")
        return

    # ----- 3. Calcular y printear
    predicted_price = calculate_price(distance_km, slope, intercept)
    print_result(theta_set, predicted_price)

if __name__ == '__main__' :
    prize_prediction()