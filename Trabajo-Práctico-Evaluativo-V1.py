import numpy as np

def calcular_moda(data):
    frecuencias = {}
    for valor in data:
        if valor in frecuencias:
            frecuencias[valor] += 1
        else:
            frecuencias[valor] = 1
    moda = max(frecuencias, key=frecuencias.get)
    return moda

data = [18, 20, 30, 40, 50]

print("La Media de este conjunto es: ", np.mean(data))
print("La Mediana de este conjunto es: ", np.median(data))

moda = calcular_moda(data)
if list(data).count(moda) > 1:
    print("La Moda de este conjunto es: ", moda)
else:
    print("No hay una moda única en este conjunto de datos")

print("La Desviacion Estandar de este conjunto es: ", np.std(data))
print("La Variancia de Este Conjunto es: ", np.var(data))
print("El Rango de este conjunto es: ", np.max(data) - np.min(data))

print("Q1 (25th percentile): ", np.percentile(data, 25))
print("Q2 (50th percentile): ", np.percentile(data, 50))
print("Q3 (75th percentile): ", np.percentile(data, 75))
