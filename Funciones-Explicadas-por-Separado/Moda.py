"""""
La moda es el valor o valores que aparecen con más frecuencia en el conjunto de datos. 
Puede haber más de una moda.
"""""
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

"""""
- frecuencias = {}: Inicializa un diccionario vacío para almacenar la frecuencia de cada elemento.
- for valor in data:: Itera sobre cada elemento en data.
- if valor in frecuencias:: Comprueba si el elemento ya existe en el diccionario.
- frecuencias[valor] += 1: Si existe, incrementa su frecuencia.
- else: frecuencias[valor] = 1: Si no existe, inicia su frecuencia en 1.
- max_frecuencia = max(frecuencias.values()): Obtiene la frecuencia más alta en el diccionario.
- modas = [key for key, value in frecuencias.items() if value == max_frecuencia]: Crea una lista de todos los elementos que tienen la frecuencia más alta.
- return modas: Retorna la lista de modas.
"""""
