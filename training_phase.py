import csv
import sys


intercept_norm = 0
slope_norm = 0
# ----- 0. parámetros ajustables
learning_rate = 1e-2    # velocidad de aprendizaje
iterations = 1000   # número de iteraciones

# ----- 1. lectura de datos
distance = []
price = []

try:
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # saltar cabecera
        for row in reader:
            if len(row) < 2:  # fila incompleta
                continue
            try:
                dist = float(row[0])
                pr = float(row[1])
                distance.append(dist)
                price.append(pr)
            except ValueError:
                # fila con datos no numeros
                continue
except FileNotFoundError:
    print("Error: data.csv no existe.")
    sys.exit(1)

m = len(distance)
if m == 0:
    print("Error: El .csv no tiene datos.")
    sys.exit(1)

print("Número de datos:", m)

# ----- 2. normalizar para estabilizar gradient descent (evitar explosion de valores)
# Se tienen que normalizar los datos porque si no los datos mucho mayores de distance dominan.
# La formula de la pendiente no se actualizaria correctamente
mean_distance = sum(distance) / m
mean_price = sum(price) / m

distance_scaled = [(d - mean_distance) / 100000 for d in distance]
price_scaled = [(p - mean_price) / 10000 for p in price]

# ----- 3. función de predicción (en datos normalizados)
def calculate_price(distance_km, slope, intercept):
    return slope * distance_km + intercept

# ----- 4. entrenamiento con normalización
for iteration in range(iterations):

    sum_error = 0
    sum_error_distance = 0

    for i in range(m):
        dist = distance_scaled[i]       # km normalizados
        real_price = price_scaled[i]    # precio nomralizado

        prediction = calculate_price(dist, slope_norm, intercept_norm)
        error = prediction - real_price

        sum_error += error
        sum_error_distance += error * dist

    tmp_intercept = learning_rate * (1/m) * sum_error
    tmp_slope = learning_rate * (1/m) * sum_error_distance

    # actualizar simultaneo
    intercept_norm -= tmp_intercept
    slope_norm -= tmp_slope

    # -----  iterando y printeando
    if (iteration+1) % 100 == 0 or iteration == 0:
        # convertir a escala real para imprimir
        slope_real = slope_norm / 100000 * 10000  # porque dividimos distance y price
        intercept_real = intercept_norm * 10000 + mean_price - slope_real * mean_distance
        print(f"\n#----- {iteration+1}. Iteration")
        print(f"intercept: {intercept_real:.4f} (eu)")
        print(f"slope: {slope_real:.8f} (eu/km)")