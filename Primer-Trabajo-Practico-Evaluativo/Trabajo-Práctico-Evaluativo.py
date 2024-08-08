# Función para convertir tiempo decimal a formato "hh:mm"
def convertir_decimal_a_tiempo(decimal):
    horas = int(decimal)
    minutos = int((decimal - horas) * 60)
    return f"{horas:02d}:{minutos:02d}"

# Función para calcular la media
def calcular_media(data, es_tiempo=False):
    media = sum(data) / len(data)  # Suma de todos los datos dividido por el número de datos
    return convertir_decimal_a_tiempo(media) if es_tiempo else media

# Función para calcular la mediana
def calcular_mediana(data, es_tiempo=False):
    n = len(data)  # Número de elementos en data
    data_sorted = sorted(data)  # Ordena la lista data
    mid = n // 2  # Encuentra el índice del punto medio
    if n % 2 == 0:
        mediana = (data_sorted[mid - 1] + data_sorted[mid]) / 2  # Promedio de dos elementos medios para listas de tamaño par
    else:
        mediana = data_sorted[mid]  # Elemento medio para listas de tamaño impar
    return convertir_decimal_a_tiempo(mediana) if es_tiempo else mediana

# Función para calcular la moda
def calcular_moda(data, es_tiempo=False):
    frecuencias = {}  # Diccionario para almacenar la frecuencia de cada elemento
    for valor in data:
        if valor in frecuencias:
            frecuencias[valor] += 1  # Incrementa la cuenta para el valor existente
        else:
            frecuencias[valor] = 1  # Inicia la cuenta para un nuevo valor
    
    max_frecuencia = max(frecuencias.values())  # Encuentra la frecuencia más alta
    modas = [key for key, value in frecuencias.items() if value == max_frecuencia]  # Encuentra todos los valores con esa frecuencia máxima

    if len(modas) == len(frecuencias):
        return None  # Si todos los valores tienen la misma frecuencia, no hay moda
    
    if es_tiempo:
        modas = [convertir_decimal_a_tiempo(moda) for moda in modas]
    
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
def calcular_rango(data, es_tiempo=False):
    rango = max(data) - min(data)  # Retorna la diferencia entre el máximo y mínimo valor
    return convertir_decimal_a_tiempo(rango) if es_tiempo else rango

# Función para calcular cuartiles
def calcular_cuartil(data, cuartil, es_tiempo=False):
    data_sorted = sorted(data)  # Ordena los datos
    index = int(cuartil * (len(data) - 1) / 100)  # Calcula el índice del cuartil
    cuartil_val = data_sorted[index]  # Retorna el valor en ese índice
    return convertir_decimal_a_tiempo(cuartil_val) if es_tiempo else cuartil_val

while True:
    # Preguntar al usuario por la categoría de los datos
    print("Seleccione la categoría de los datos:")
    print("1. Peso (Kg, g, Libras, oz)")
    print("2. Longitud (Metros, cm, Km, ft, in)")
    print("3. Volumen (L, mL, gal)")
    print("4. Tiempo (Horas, Minutos, Segundos)")
    print("5. Temperatura (°C, °F, K)")
    categoria = input("Ingrese el número de la categoría: ")

    unidad = ""
    data = []
    es_tiempo = False  # Bandera para indicar si los datos son tiempos

    if categoria == "1":
        print("Seleccione la unidad de peso:")
        print("1. Kilogramos (Kg)")
        print("2. Gramos (g)")
        print("3. Libras (lb)")
        print("4. Onzas (oz)")
        unidad_peso = input("Ingrese el número de la unidad de peso: ")

        if unidad_peso == "1":
            unidad = "Kg"
        elif unidad_peso == "2":
            unidad = "g"
        elif unidad_peso == "3":
            unidad = "lb"
        elif unidad_peso == "4":
            unidad = "oz"
        else:
            print("Unidad de peso no válida. Saliendo del programa.")
            exit()
        data = sorted(list(map(float, input(f"Ingrese los datos en {unidad} separados por espacios: ").split())))
        
    elif categoria == "2":
        print("Seleccione la unidad de longitud:")
        print("1. Metros (m)")
        print("2. Centímetros (cm)")
        print("3. Kilómetros (Km)")
        print("4. Pies (ft)")
        print("5. Pulgadas (in)")
        unidad_longitud = input("Ingrese el número de la unidad de longitud: ")

        if unidad_longitud == "1":
            unidad = "m"
        elif unidad_longitud == "2":
            unidad = "cm"
        elif unidad_longitud == "3":
            unidad = "Km"
        elif unidad_longitud == "4":
            unidad = "ft"
        elif unidad_longitud == "5":
            unidad = "in"
        else:
            print("Unidad de longitud no válida. Saliendo del programa.")
            exit()
        data = sorted(list(map(float, input(f"Ingrese los datos en {unidad} separados por espacios: ").split())))
        
    elif categoria == "3":
        print("Seleccione la unidad de volumen:")
        print("1. Litros (L)")
        print("2. Mililitros (mL)")
        print("3. Galones (gal)")
        unidad_volumen = input("Ingrese el número de la unidad de volumen: ")

        if unidad_volumen == "1":
            unidad = "L"
        elif unidad_volumen == "2":
            unidad = "mL"
        elif unidad_volumen == "3":
            unidad = "gal"
        else:
            print("Unidad de volumen no válida. Saliendo del programa.")
            exit()
        data = sorted(list(map(float, input(f"Ingrese los datos en {unidad} separados por espacios: ").split())))
        
    elif categoria == "4":
        print("Seleccione la unidad de tiempo:")
        print("1. Horas (hh:mm)")
        print("2. Minutos")
        print("3. Segundos")
        unidad_tiempo = input("Ingrese el número de la unidad de tiempo: ")

        if unidad_tiempo == "1":
            unidad = "hh:mm"
            print("Ingrese los tiempos en formato 'hh:mm', separados por espacios.")
            data = sorted(list(map(convertir_tiempo_a_decimal, input("Ingrese los tiempos: ").split())))
            es_tiempo = True
        elif unidad_tiempo == "2":
            unidad = "minutos"
            data = sorted(list(map(float, input(f"Ingrese los tiempos en {unidad} separados por espacios: ").split())))
        elif unidad_tiempo == "3":
            unidad = "segundos"
            data = sorted(list(map(float, input(f"Ingrese los tiempos en {unidad} separados por espacios: ").split())))
        else:
            print("Unidad de tiempo no válida. Saliendo del programa.")
            exit()
            
    elif categoria == "5":
        print("Seleccione la unidad de temperatura:")
        print("1. Grados Celsius (°C)")
        print("2. Grados Fahrenheit (°F)")
        print("3. Kelvin (K)")
        unidad_temperatura = input("Ingrese el número de la unidad de temperatura: ")

        if unidad_temperatura == "1":
            unidad = "°C"
        elif unidad_temperatura == "2":
            unidad = "°F"
        elif unidad_temperatura == "3":
            unidad = "K"
        else:
            print("Unidad de temperatura no válida. Saliendo del programa.")
            exit()
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
        print(f"La Media de este conjunto es: {calcular_media(data, es_tiempo)} {unidad}")
    if "2" in opciones or "8" in opciones:
        print(f"La Mediana de este conjunto es: {calcular_mediana(data, es_tiempo)} {unidad}")
    if "3" in opciones or "8" in opciones:
        modas = calcular_moda(data, es_tiempo)
        if modas is None:
            print(f"No hay una moda absoluta en este conjunto.")
        elif len(modas) == 1:
            print(f"La Moda de este conjunto es: {modas[0]} {unidad}")
        else:
            print(f"Las Modas de este conjunto son: {', '.join(map(str, modas))} {unidad}")
    if "4" in opciones or "8" in opciones:
        print(f"La Desviación Estándar de este conjunto es: {calcular_desviacion_estandar(data)} {unidad}")
    if "5" in opciones or "8" in opciones:
        print(f"La Varianza de este conjunto es: {calcular_varianza(data)} {unidad}")
    if "6" in opciones or "8" in opciones:
        print(f"El Rango de este conjunto es: {calcular_rango(data, es_tiempo)} {unidad}")
    if "7" in opciones or "8" in opciones:
        print(f"Q1: {calcular_cuartil(data, 25, es_tiempo)} {unidad}")
        print(f"Q2: {calcular_cuartil(data, 50, es_tiempo)} {unidad}")  # La mediana
        print(f"Q3: {calcular_cuartil(data, 75, es_tiempo)} {unidad}")

    # Preguntar al usuario si desea introducir nuevos datos
    nueva_ejecucion = input("¿Desea introducir nuevos datos? (si/no): ").lower()
    if nueva_ejecucion != 'si':
        break

print("El Programa ha finalizado. Gracias por utilizar nuestro programa.")