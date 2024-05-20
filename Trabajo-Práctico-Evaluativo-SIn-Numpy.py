def calcular_media(data):
    return sum(data) / len(data)

def calcular_mediana(data):
    n = len(data)
    data_sorted = sorted(data)
    mid = n // 2
    if n % 2 == 0:
        return (data_sorted[mid - 1] + data_sorted[mid]) / 2
    else:
        return data_sorted[mid]

def calcular_moda(data):
    frecuencias = {}
    for valor in data:
        if valor in frecuencias:
            frecuencias[valor] += 1
        else:
            frecuencias[valor] = 1
    max_freq = max(frecuencias.values())
    modas = [key for key, value in frecuencias.items() if value == max_freq]
    return modas

def calcular_desviacion_estandar(data):
    media = calcular_media(data)
    variance = sum((x - media) ** 2 for x in data) / len(data)
    return variance ** 0.5

def calcular_varianza(data):
    media = calcular_media(data)
    return sum((x - media) ** 2 for x in data) / len(data)

def calcular_rango(data):
    return max(data) - min(data)

def calcular_percentil(data, percentil):
    data_sorted = sorted(data)
    k = (len(data) - 1) * (percentil / 100)
    f = int(k)
    c = k - f
    if f + 1 < len(data_sorted):
        return data_sorted[f] + (data_sorted[f + 1] - data_sorted[f]) * c
    return data_sorted[f]

# Preguntar al usuario por la categoría de los datos
print("Seleccione la categoría de los datos:")
print("1. Peso (Kg, Libras, etc)")
print("2. Distancia (Metros, Pies, etc)")
print("3. Tiempo (Horas, Minutos, Segundos, etc)")
print("4. Precios")
categoria = input("Ingrese el número de la categoría: ")

unidad = ""
if categoria == "1":
    unidad = input("Ingrese la unidad de peso (por ejemplo, Kg, Libras): ")
elif categoria == "2":
    unidad = input("Ingrese la unidad de distancia (por ejemplo, Metros, Pies): ")
elif categoria == "3":
    unidad = input("Ingrese la unidad de tiempo (por ejemplo, Horas, Minutos, Segundos): ")
elif categoria == "4":
    unidad = input("Ingrese la moneda (por ejemplo, USD, EUR): ")
else:
    print("Categoría no válida. Saliendo del programa.")
    exit()

data = sorted(list(map(float, input(f"Ingrese los datos en {unidad} separados por espacios: ").split())))

print("Seleccione las estadísticas que desea ver (puede seleccionar varias separadas por comas):")
print("1. Media")
print("2. Mediana")
print("3. Moda")
print("4. Desviación Estándar")
print("5. Varianza")
print("6. Rango")
print("7. Cuartiles (Q1, Q2, Q3)")
opciones = input("Ingrese los números de las estadísticas que desea ver: ").split(',')

opciones_estadisticas = {
    '1': calcular_media,
    '2': calcular_mediana,
    '3': calcular_moda,
    '4': calcular_desviacion_estandar,
    '5': calcular_varianza,
    '6': calcular_rango,
    '7': lambda d: [calcular_percentil(d, 25), calcular_percentil(d, 50), calcular_percentil(d, 75)]
}

for opcion in opciones:
    resultado = opciones_estadisticas[opcion](data)
    if opcion == '7':
        print(f"Q1: {resultado[0]} {unidad}, Q2 (Mediana): {resultado[1]} {unidad}, Q3: {resultado[2]} {unidad}")
    elif opcion == '3':
        if len(resultado) == 1:
            print(f"La Moda de este conjunto es: {resultado[0]} {unidad}")
        else:
            print(f"Las Modas de este conjunto son: {', '.join(map(str, resultado))} {unidad}")
    else:
        print(f"La {'Media' if opcion == '1' else 'Mediana' if opcion == '2' else 'Desviación Estándar' if opcion == '4' else 'Varianza' if opcion == '5' else 'Rango' if opcion == '6' else ''} de este conjunto es: {resultado} {unidad}")

