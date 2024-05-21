# Función para convertir el tiempo en formato "hh:mm" a minutos
def convertir_tiempo_a_minutos(tiempo_str):
    horas, minutos = map(int, tiempo_str.split(':'))  # Separa horas y minutos, y los convierte a enteros
    return horas * 60 + minutos  # Convierte todo el tiempo a minutos

# Función para calcular la media
def calcular_media(data):
    return sum(data) / len(data)  # Suma de todos los datos dividido por el número de datos

# Función para calcular la mediana
def calcular_mediana(data):
    n = len(data)  # Número de elementos en data
    data_sorted = sorted(data)  # Ordena la lista data
    mid = n // 2  # Encuentra el índice del punto medio
    if n % 2 == 0:
        return (data_sorted[mid - 1] + data_sorted[mid]) / 2  # Promedio de dos elementos medios para listas de tamaño par
    else:
        return data_sorted[mid]  # Elemento medio para listas de tamaño impar

# Función para calcular la moda
def calcular_moda(data):
    frecuencias = {}  # Diccionario para almacenar la frecuencia de cada elemento
    for valor in data:
        if valor in frecuencias:
            frecuencias[valor] += 1  # Incrementa la cuenta para el valor existente
        else:
            frecuencias[valor] = 1  # Inicia la cuenta para un nuevo valor
    
    max_frecuencia = max(frecuencias.values())  # Encuentra la frecuencia más alta
    modas = [key for key, value in frecuencias.items() if value == max_frecuencia]  # Encuentra todos los valores con esa frecuencia máxima

    return modas

# Función para calcular la desviación estándar
def calcular_desviacion_estandar(data):
    mean = calcular_media(data)  # Calcula la media de data
    variance = sum((x - mean) ** 2 for x in data) / len(data)  # Calcula la varianza como el promedio de las diferencias al cuadrado respecto a la media
    return variance ** 0.5  # Retorna la raíz cuadrada de la varianza

# Función para calcular la varianza
def calcular_varianza(data):
    mean = calcular_media(data)  # Calcula la media de los datos
    return sum((x - mean) ** 2 for x in data) / len(data)  # Retorna la varianza

# Función para calcular el rango
def calcular_rango(data):
    return max(data) - min(data)  # Retorna la diferencia entre el máximo y mínimo valor

# Función para calcular cuartiles
def calcular_cuartil(data, cuartil):
    data_sorted = sorted(data)  # Ordena los datos
    index = cuartil * (len(data) - 1) // 100  # Calcula el índice del cuartil
    return data_sorted[index]  # Retorna el valor en ese índice

while True:
    # Preguntar al usuario por la categoría de los datos
    print("Seleccione la categoría de los datos:")
    print("1. Peso (Kg, Libras, etc)")
    print("2. Distancia (Metros, Pies, etc)")
    print("3. Tiempo (Horas, Minutos, Segundos)")
    print("4. Precios")
    categoria = input("Ingrese el número de la categoría: ")

    unidad = ""
    data = []
    if categoria == "1":
        unidad = input("Ingrese la unidad de peso (por ejemplo, Kg, Libras): ")
        data = sorted(list(map(float, input(f"Ingrese los datos en {unidad} separados por espacios: ").split())))
    elif categoria == "2":
        unidad = input("Ingrese la unidad de distancia (por ejemplo, Metros, Pies): ")
        data = sorted(list(map(float, input(f"Ingrese los datos en {unidad} separados por espacios: ").split())))
    elif categoria == "3":
        print("Seleccione la unidad de tiempo:")
        print("1. Horas (hh:mm)")
        print("2. Minutos")
        print("3. Segundos")
        unidad_tiempo = input("Ingrese el número de la unidad de tiempo: ")

        if unidad_tiempo == "1":
            unidad = "minutos"
            print("Ingrese los tiempos en formato 'hh:mm', separados por espacios.")
            data = sorted(list(map(convertir_tiempo_a_minutos, input("Ingrese los tiempos: ").split())))
        elif unidad_tiempo == "2":
            unidad = "minutos"
            data = sorted(list(map(float, input(f"Ingrese los tiempos en {unidad} separados por espacios: ").split())))
        elif unidad_tiempo == "3":
            unidad = "segundos"
            data = sorted(list(map(float, input(f"Ingrese los tiempos en {unidad} separados por espacios: ").split())))
        else:
            print("Unidad de tiempo no válida. Saliendo del programa.")
            exit()
    elif categoria == "4":
        unidad = input("Ingrese la moneda (por ejemplo, USD, EUR): ")
        data = sorted(list(map(float, input(f"Ingrese los datos en {unidad} separados por espacios: ").split())))
    else:
        print("Categoría no válida. Saliendo del programa.")
        exit()

    # Preguntar al usuario qué estadísticas desea ver
    print("Seleccione las estadísticas que desea ver (puede seleccionar varias separadas por comas):")
    print("1. Media")
    print("2. Mediana")
    print("3. Moda")
    print("4. Desviación Estándar")
    print("5. Varianza")
    print("6. Rango")
    print("7. Cuartiles (Q1, Q2, Q3)")
    print("8. Todas las opciones")
    opciones = input("Ingrese los números de las estadísticas que desea ver: ").split(',')

    # Mostrar las estadísticas seleccionadas
    if "1" in opciones or "8" in opciones:
        print(f"La Media de este conjunto es: {calcular_media(data)} {unidad}")
    if "2" in opciones or "8" in opciones:
        print(f"La Mediana de este conjunto es: {calcular_mediana(data)} {unidad}")
    if "3" in opciones or "8" in opciones:
        modas = calcular_moda(data)
        if len(modas) == 1:
            print(f"La Moda de este conjunto es: {modas[0]} {unidad}")
        else:
            print(f"Las Modas de este conjunto son: {', '.join(map(str, modas))} {unidad}")
    if "4" in opciones or "8" in opciones:
        print(f"La Desviación Estándar de este conjunto es: {calcular_desviacion_estandar(data)} {unidad}")
    if "5" in opciones or "8" in opciones:
        print(f"La Varianza de este conjunto es: {calcular_varianza(data)} {unidad}")
    if "6" in opciones or "8" in opciones:
        print(f"El Rango de este conjunto es: {calcular_rango(data)} {unidad}")
    if "7" in opciones or "8" in opciones:
        print(f"Q1: {calcular_cuartil(data, 25)} {unidad}")
        print(f"Q2: {calcular_cuartil(data, 50)} {unidad}")  # La mediana
        print(f"Q3: {calcular_cuartil(data, 75)} {unidad}")

    # Preguntar al usuario si desea introducir nuevos datos
    nueva_ejecucion = input("¿Desea introducir nuevos datos? (s/n): ").lower()
    if nueva_ejecucion != 's':
        break

print("Programa finalizado.")
