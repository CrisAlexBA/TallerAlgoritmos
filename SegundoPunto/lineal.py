def busqueda_lineal(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i  # Devuelve el índice donde se encontró
    return -1  # No se encontró
