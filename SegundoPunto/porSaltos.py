import math

def busqueda_por_saltos(arr, objetivo):
    # n es el tamaño del array (cantidad de elementos)
    n = len(arr)

    # Calculamos el tamaño del salto, que es la raíz cuadrada de n.
    # Este valor es el bloque que se salta en cada iteración.
    salto = int(math.sqrt(n)) 
    # Variable que lleva el índice del bloque anterior (previo al salto actual)
    prev = 0
    
    # Salta bloques hasta encontrar el intervalo donde podría estar el objetivo
    while arr[min(salto, n) - 1] < objetivo:
        prev = salto
        salto += int(math.sqrt(n))

        # Si el salto supera el tamaño del array, el objetivo no está presente
        if prev >= n:
            return -1 
    
    # Realizamos una búsqueda lineal dentro del bloque donde podría estar el objetivo.
    for i in range(prev, min(salto, n)):
        # Si encontramos el objetivo en este bloque, retornamos su índice
        if arr[i] == objetivo:
            return i
    
    return -1  # No se encontró
