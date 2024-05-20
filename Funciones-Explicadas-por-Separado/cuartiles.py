"""""
Los cuartiles son valores que dividen el conjunto de datos en cuatro partes iguales. Q1 es el cuartil 25%, Q2 es la mediana, y Q3 es el cuartil 75%.
"""""
def calcular_cuartil(data, cuartil):
    data_sorted = sorted(data)  # Ordena los datos
    index = cuartil * (len(data) - 1) // 100  # Calcula el índice del cuartil
    return data_sorted[index]  # Retorna el valor en ese índice

"""""
data_sorted = sorted(data): Ordena la lista data.
index = cuartil * (len(data) - 1) // 100: Calcula el índice que corresponde al porcentaje del cuartil deseado.
return data_sorted[index]: Retorna el valor en la posición calculada.
"""""