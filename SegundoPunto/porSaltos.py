import math

def busqueda_por_saltos(arr, objetivo):
    n = len(arr)
    salto = int(math.sqrt(n))  # Tamaño del salto
    prev = 0
    
    # Salta bloques hasta encontrar el intervalo donde podría estar el objetivo
    while arr[min(salto, n) - 1] < objetivo:
        prev = salto
        salto += int(math.sqrt(n))
        if prev >= n:
            return -1  # El objetivo no está presente
    
    # Búsqueda lineal dentro del bloque donde podría estar el objetivo
    for i in range(prev, min(salto, n)):
        if arr[i] == objetivo:
            return i
    
    return -1  # No se encontró
