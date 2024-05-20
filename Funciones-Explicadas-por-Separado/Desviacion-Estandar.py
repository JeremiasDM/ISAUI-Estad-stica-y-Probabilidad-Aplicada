"""""
La desviación estándar mide la dispersión de los datos respecto a la media. 
Se calcula como la raíz cuadrada de la varianza.
"""""

def calcular_desviacion_estandar(data):
    mean = calcular_media(data)  # Calcula la media de data
    variance = sum((x - mean) ** 2 for x in data) / len(data)  # Calcula la varianza como el promedio de las diferencias al cuadrado respecto a la media
    return variance ** 0.5  # Retorna la raíz cuadrada de la varianza

"""""
- mean = calcular_media(data): Calcula la media de los datos.
- variance = sum((x - mean) ** 2 for x in data) / len(data): Calcula la varianza.
- return variance ** 0.5: Retorna la raíz cuadrada de la varianza, que es la desviación estándar.
"""""