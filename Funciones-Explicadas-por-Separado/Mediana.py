"""""
La mediana es el valor medio en un conjunto de datos ordenados. 
Si el número de datos es impar, es el número en la posición central. 
Si es par, es el promedio de los dos números centrales.
"""""
def calcular_mediana(data):
    n = len(data)  # Número de elementos en data
    data_sorted = sorted(data)  # Ordena la lista data
    mid = n // 2  # Encuentra el índice del punto medio
    if n % 2 == 0:
        return (data_sorted[mid - 1] + data_sorted[mid]) / 2  # Promedio de dos elementos medios para listas de tamaño par
    else:
        return data_sorted[mid]  # Elemento medio para listas de tamaño impar

"""""
- n = len(data): Obtiene la cantidad de elementos en data.
- data_sorted = sorted(data): Ordena la lista data.
- mid = n // 2: Calcula el índice del valor medio.
- if n % 2 == 0:: Comprueba si la cantidad de datos es par.
- return (data_sorted[mid - 1] + data_sorted[mid]) / 2: Si es par, retorna el promedio de los dos valores centrales.
- else: return data_sorted[mid]: Si es impar, retorna el valor central directamente.
"""""