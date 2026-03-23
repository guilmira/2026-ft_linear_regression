# ----- 1. Parámetros obtenidos de train.py
intercept = 8348.3484  # eu
slope = -0.01995241    # eu/km

# ----- 2. Función de predicción
def calculate_price(distance_km, slope, intercept):
    price_eu = slope * distance_km + intercept
    return price_eu

# ----- 3. Pedir al usuario la distancia
try:
    distance_input = input("Introduce la distancia del coche (km): ")
    distance_km = float(distance_input)
except ValueError:
    print("Error: Debes introducir un número.")
    exit(1)

# ----- 4. Calcular precio estimado
predicted_price = calculate_price(distance_km, slope, intercept)

# ----- 5. Mostrar resultado con unidades
print(f"Precio estimado: {predicted_price:.2f} (eu)")