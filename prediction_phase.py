#Fase 1: prediccion. Necesita que la regresion lineal esté calculada

# ----- 1. Intentar leer theta.txt
theta_file = 'theta.txt'
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

# ----- 2. Función de predicción
def calculate_price(distance_km, slope, intercept):
    price_eu = slope * distance_km + intercept
    return price_eu

# ----- 3. Inputs
try:
    distance_input = input("Introduce la distancia del coche (km, >0): ")
    distance_km = float(distance_input)
    if distance_km <= 0:
        print("La distancia debe ser mayor que 0.")
        exit(1)
except ValueError:
    print("Error: Debes introducir un número.")
    exit(1)

# ----- 4. Calcular precio
predicted_price = calculate_price(distance_km, slope, intercept)

# ----- 5. Mostrar resultado con unidades
if not theta_set:
    print("Aviso: no tenemos la regresión lineal. Para valores con sentido, entrena el modelo")
print(f"Precio estimado: {predicted_price:.2f} (eu)")