def busqueda_binaria(arr, objetivo):
    izquierda, derecha = 0, len(arr) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1  # No se encontró
