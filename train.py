import csv

# ----- 1. Leer datos
distance = []
price = []

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # saltar cabecera
    for row in reader:
        distance.append(float(row[0]))  # km
        price.append(float(row[1]))     # eu
# uso float por lo que pueda venir en un dataset en la eva.

m = len(distance)
print("Numero de datos:", m)

# ----- 2. Inicializar parametros
intercept = 0
slope = 0
learning_rate = 1e-10
iterations = 50000

# ----- 3. Función de predicción
def calculate_price(distance_km, slope, intercept):
    price_eu = slope * distance_km + intercept
    return price_eu

# ----- 4. Entrenamiento
for iteration in range(iterations):

    sum_error = 0
    sum_error_distance = 0

    for i in range(m):
        dist = distance[i]       # km
        real_price = price[i]    # eu

        prediction = calculate_price(dist, slope, intercept)
        error = prediction - real_price

        sum_error += error
        sum_error_distance += error * dist

    tmp_intercept = learning_rate * (1/m) * sum_error
    tmp_slope = learning_rate * (1/m) * sum_error_distance

    new_intercept = intercept - tmp_intercept
    new_slope = slope - tmp_slope

    intercept = new_intercept
    slope = new_slope

    # ----- 1. Iteration
    print(f"\n#----- {iteration+1}. Iteration")
    print(f"intercept: {intercept:.4f} (eu)")
    print(f"slope: {slope:.8f} (eu/km)")