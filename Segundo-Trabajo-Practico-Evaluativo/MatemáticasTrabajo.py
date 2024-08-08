import statistics
import math

def convertir_tiempo_a_decimal(tiempo):
    """
    Convertir tiempo en formato HH:MM a decimal
    """
    horas, minutos = map(int, tiempo.split(':'))
    return horas + minutos / 60

def calcular_cuartiles(datos):
    """
    Calcular cuartiles de una lista de datos
    """
    return (
        statistics.quantiles(datos, n=4, method='inclusive')[0],
        statistics.median(datos),
        statistics.quantiles(datos, n=4, method='inclusive')[2]
    )

def calcular_medidas(datos, opciones):
    """
    Calcular medidas estadísticas de una lista de datos
    """
    resultados = {}
    if 1 in opciones:
        resultados['Media'] = statistics.mean(datos)
    if 2 in opciones:
        resultados['Mediana'] = statistics.median(datos)
    if 3 in opciones:
        moda = statistics.multimode(datos)
        # Si todos los elementos son moda, significa que no hay moda
        if len(moda) == len(datos):
            resultados['Moda'] = "No hay moda"
        else:
            resultados['Moda'] = moda
    if 4 in opciones:
        cuartiles = calcular_cuartiles(datos)
        resultados['Cuartiles'] = cuartiles
    if 5 in opciones:
        resultados['Rango'] = max(datos) - min(datos)
    if 6 in opciones:
        resultados['Varianza'] = statistics.variance(datos)
    if 7 in opciones:
        resultados['Desviación estándar'] = statistics.stdev(datos)
    return resultados

def mostrar_resultados(resultados):
    """
    Mostrar resultados de las medidas estadísticas
    """
    print("\nResultados:")
    for medida, valor in resultados.items():
        if isinstance(valor, list):  # Caso especial para la moda, que puede tener múltiples valores
            print(f"{medida}: {', '.join(map(str, valor))}")
        elif isinstance(valor, tuple):  # Caso especial para los cuartiles
            print(f"{medida}: Q1 = {valor[0]:.2f}, Q2 (Mediana) = {valor[1]:.2f}, Q3 = {valor[2]:.2f}")
        else:
            print(f"{medida}: {valor}")

def menu_estadistica_descriptiva():
    """
    Menú de estadística descriptiva
    """
    print("Estadística descriptiva")
    print("1. Media")
    print("2. Mediana")
    print("3. Moda")
    print("4. Cuartiles")
    print("5. Rango")
    print("6. Varianza")
    print("7. Desviación estándar")
    opciones = input("Ingrese las opciones separadas por comas: ")
    opciones = [int(x) for x in opciones.split(',')]
    datos = input("Ingrese los datos separados por comas: ")
    datos = [float(x) for x in datos.split(',')]
    resultados = calcular_medidas(datos, opciones)
    mostrar_resultados(resultados)

def calcular_probabilidad_binomial(n, p, x):
    """
    Calcular probabilidad binomial
    """
    # Calcula el número de combinaciones de n elementos tomados de x en x usando la fórmula combinatoria: n! / (x! * (n - x)!)
    combinaciones = math.comb(n, x)
    
    # Calcula la probabilidad de tener exactamente x éxitos. Esto es p elevado a la x.
    probabilidad_exitos = p ** x
    
    # Calcula la probabilidad de tener exactamente n - x fracasos. Esto es (1 - p) elevado a (n - x).
    probabilidad_fracasos = (1 - p) ** (n - x)
    
    # Multiplica las combinaciones por las probabilidades de éxitos y fracasos para obtener la probabilidad final.
    probabilidad = combinaciones * probabilidad_exitos * probabilidad_fracasos
    
    return probabilidad  # Devuelve la probabilidad binomial calculada

def calcular_probabilidad_acumulada_binomial(n, p, x):
    """
    Calcular la probabilidad acumulada binomial
    """
    probabilidad_acumulada = 0  # Inicializa la probabilidad acumulada en 0
    # Suma las probabilidades individuales de 0 a x éxitos
    for i in range(x + 1):
        probabilidad_acumulada += calcular_probabilidad_binomial(n, p, i)
    return probabilidad_acumulada  # Devuelve la probabilidad acumulada

def calcular_probabilidad_poisson(l, x):
    """
    Calcular probabilidad de Poisson
    """
    # Calcula l^x (l elevado a la x), donde l es la tasa promedio de eventos y x es el número de eventos observados.
    tasa_a_la_x = l ** x
    
    # Calcula e^(-l), donde e es el número de Euler (aproximadamente 2.71828). Esto calcula la probabilidad de que ocurran 0 eventos en el intervalo.
    e_a_la_menos_l = math.e ** -l
    
    # Calcula el factorial de x, que es el número de permutaciones de x elementos.
    x_factorial = math.factorial(x)
    
    # Divide la multiplicación de tasa_a_la_x y e_a_la_menos_l por x_factorial para obtener la probabilidad.
    probabilidad = (tasa_a_la_x * e_a_la_menos_l) / x_factorial
    
    return probabilidad  # Devuelve la probabilidad de Poisson calculada

def calcular_probabilidad_acumulada_poisson(l, x):
    """
    Calcular la probabilidad acumulada de Poisson
    """
    probabilidad_acumulada = 0  # Inicializa la probabilidad acumulada en 0
    # Suma las probabilidades individuales de 0 a x eventos
    for i in range(x + 1):
        probabilidad_acumulada += calcular_probabilidad_poisson(l, i)
    return probabilidad_acumulada  # Devuelve la probabilidad acumulada

def calcular_probabilidad_hipergeometrica(N, K, n, x):
    """
    Calcular probabilidad hipergeométrica
    """
    # Calcula el número de formas de elegir x éxitos de K éxitos disponibles usando la función math.comb.
    combinaciones_exitos = math.comb(K, x)
    
    # Calcula el número de formas de elegir n - x fracasos de N - K fracasos disponibles.
    combinaciones_fracasos = math.comb(N - K, n - x)
    
    # Calcula el número de formas de elegir n elementos de N elementos.
    combinaciones_totales = math.comb(N, n)
    
    # Multiplica combinaciones de éxitos y fracasos, y divide por las combinaciones totales para obtener la probabilidad.
    probabilidad = (combinaciones_exitos * combinaciones_fracasos) / combinaciones_totales
    
    return probabilidad  # Devuelve la probabilidad hipergeométrica calculada

def calcular_probabilidad_acumulada_hipergeometrica(N, K, n, x):
    """
    Calcular la probabilidad acumulada hipergeométrica
    """
    probabilidad_acumulada = 0  # Inicializa la probabilidad acumulada en 0
    # Suma las probabilidades individuales de 0 a x éxitos en la muestra
    for i in range(x + 1):
        probabilidad_acumulada += calcular_probabilidad_hipergeometrica(N, K, n, i)
    return probabilidad_acumulada  # Devuelve la probabilidad acumulada

def calcular_probabilidad_gaussiana(mu, sigma, x):
    """
    Calcular densidad de probabilidad gaussiana
    """
    # Calcula el factor de normalización (1 / (sigma * sqrt(2 * pi))). Este factor asegura que el área bajo la curva sea 1.
    factor_normalizacion = 1 / (sigma * math.sqrt(2 * math.pi))
    
    # Calcula la parte exponencial de la fórmula. Esta parte mide cuán lejos está x de la media mu, en unidades de sigma.
    exponente = -((x - mu) ** 2) / (2 * sigma ** 2)
    
    # Calcula la función exponencial de math.exp para el exponente calculado. math.exp devuelve e elevado a la potencia del argumento.
    probabilidad_exponencial = math.exp(exponente)
    
    # Multiplica el factor de normalización por la parte exponencial para obtener la densidad de probabilidad.
    probabilidad = factor_normalizacion * probabilidad_exponencial
    
    return probabilidad  # Devuelve la densidad de probabilidad gaussiana calculada

def calcular_probabilidad_normal_cdf(z):
    """
    Aproximación de la función de distribución acumulativa (CDF) para la distribución normal estándar
    usando la fórmula de Abramowitz y Stegun
    La función de distribución acumulativa para una variable normal estándar 𝑍 (es un valor normalizado que indica cuántas desviaciones estándar un punto 
    de datos está por encima o por debajo de la media de la distribución.) 
    se denota comúnmente como Φ(𝑍) y calcula la probabilidad de que una variable aleatoria normal estándar sea menor o igual a 𝑍.
    La fórmula de Abramowitz y Stegun se basa en una serie de aproximaciones que permiten calcular 
    Φ(𝑍) de manera eficiente.

Para evitar la integración directa, se utiliza una aproximación que involucra la serie de Taylor y polinomios
    """
    # Coeficientes para la aproximación de la CDF normal estándar
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911
    
    # Determina el signo de z
    sign = 1 if z >= 0 else -1
    z = abs(z) / math.sqrt(2.0)
    
    # Calcula la aproximación de la CDF usando una serie de operaciones
    t = 1.0 / (1.0 + p * z)
    y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * math.exp(-z * z)
    
    # Ajusta el resultado según el signo de z
    return 0.5 * (1.0 + sign * y)

def calcular_probabilidad_acumulada_gaussiana(mu, sigma, x):
    """
    Calcular la probabilidad acumulada gaussiana (CDF) usando la aproximación normal estándar
    """
    # Calcula el valor z normalizado
    z = (x - mu) / sigma
    
    # Calcula la probabilidad acumulada usando la función de distribución acumulativa normal estándar
    probabilidad_acumulada = calcular_probabilidad_normal_cdf(z)
    
    return probabilidad_acumulada  # Devuelve la probabilidad acumulada gaussiana

def menu_probabilidad():
    """
    Menú de probabilidad
    """
    print("Probabilidad")
    print("1. Binomial")
    print("2. Poisson")
    print("3. Hipergeométrica")
    print("4. Gaussiana")
    
    # Pide al usuario que elija una opción de distribución
    opcion = int(input("Ingrese la opción: "))
    
    # Pide al usuario que elija entre probabilidad puntual o acumulada
    acumulativa = input("¿Desea calcular la probabilidad acumulada? (s/n): ").lower() == 's'
    
    # Maneja la opción seleccionada por el usuario
    if opcion == 1:
        n = int(input("Ingrese el número de ensayos (n): "))
        p = float(input("Ingrese la probabilidad de éxito (p): "))
        x = int(input("Ingrese el número de éxitos (x): "))
        if acumulativa:
            resultado = calcular_probabilidad_acumulada_binomial(n, p, x)
        else:
            resultado = calcular_probabilidad_binomial(n, p, x)
    elif opcion == 2:
        l = float(input("Ingrese la tasa de llegada (lambda): "))
        x = int(input("Ingrese el número de eventos (x): "))
        if acumulativa:
            resultado = calcular_probabilidad_acumulada_poisson(l, x)
        else:
            resultado = calcular_probabilidad_poisson(l, x)
    elif opcion == 3:
        N = int(input("Ingrese el tamaño de la población (N): "))
        K = int(input("Ingrese el número de elementos favorables (K): "))
        n = int(input("Ingrese el tamaño de la muestra (n): "))
        x = int(input("Ingrese el número de elementos favorables en la muestra (x): "))
        if acumulativa:
            resultado = calcular_probabilidad_acumulada_hipergeometrica(N, K, n, x)
        else:
            resultado = calcular_probabilidad_hipergeometrica(N, K, n, x)
    elif opcion == 4:
        mu = float(input("Ingrese la media (mu): "))
        sigma = float(input("Ingrese la desviación estándar (sigma): "))
        x = float(input("Ingrese el valor (x): "))
        if acumulativa:
            resultado = calcular_probabilidad_acumulada_gaussiana(mu, sigma, x)
        else:
            resultado = calcular_probabilidad_gaussiana(mu, sigma, x)
    else:
        print("Opción inválida")
        return
    
    # Define el tipo de probabilidad calculada y muestra el resultado
    tipo = "acumulada" if acumulativa else "puntual"
    print(f"La probabilidad {tipo} es: {resultado:.4f}")

def main():
    # Bucle principal del programa
    while True:
        print("Menú Principal")
        print("1. Probabilidad")
        print("2. Estadística")
        print("3. Salir")
        
        # Pide al usuario que elija una opción del menú principal
        opcion = int(input("Ingrese la opción: "))
        
        # Maneja la opción seleccionada por el usuario
        if opcion == 1:
            menu_probabilidad()
        elif opcion == 2:
            print("Función no implementada")
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

# Ejecuta la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()


