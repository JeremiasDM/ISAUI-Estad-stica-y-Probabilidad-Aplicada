"""""
La varianza es el promedio de los cuadrados de las diferencias entre cada valor y la media del conjunto de datos.
"""""
def calcular_varianza(data):
    mean = calcular_media(data)  # Calcula la media de los datos
    return sum((x - mean) ** 2 for x in data) / len(data)  # Retorna la varianza

"""""
mean = calcular_media(data): Calcula la media de los datos.
return sum((x - mean) ** 2 for x in data) / len(data): Suma las diferencias al cuadrado de cada elemento respecto a la media y divide por el número de elementos para obtener la varianza.
"""""