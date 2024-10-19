#Basado en: https://www.geeksforgeeks.org/binary-search/ 
#Funcion: Recorrer un arreglo ordenado dividiendo constantemente hasta encontrar objetivo
def busqueda_binaria(arr, objetivo):
    #Inicializar indices de izquierda y derecha
    izquierda, derecha = 0, len(arr) - 1
    
    # El bucle se ejecuta mientras la izquierda no sobrepase a la derecha
    while izquierda <= derecha:
        # Calculamos el punto medio (índice) de la sección actual
        medio = (izquierda + derecha) // 2

        # Si el valor en la posición media es igual al objetivo, retornamos el índice
        if arr[medio] == objetivo:
            return medio
        
        # Si el valor en la posición media es menor que el objetivo,
        # movemos el límite izquierdo al siguiente del medio (descartamos la mitad izquierda)
        elif arr[medio] < objetivo:
            izquierda = medio + 1

        # Si el valor en la posición media es mayor que el objetivo,
        # movemos el límite derecho al anterior del medio (descartamos la mitad derecha)
        else:
            derecha = medio - 1
    # Si no encontramos el objetivo en el array, devolvemos -1
    return -1 
