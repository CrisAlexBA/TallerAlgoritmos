def busqueda_lineal_limitada(arr, objetivo, k):
    for i in range(min(k, len(arr))):
        if arr[i] == objetivo:
            return i
    return -1  # No se encontró en los primeros 'k' elementos
