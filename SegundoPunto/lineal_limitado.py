#Busqueda Lineal Limitada
#Si objetivo esta en la lista devuelve su posicion, de lo contratio retorna -1, recorre un numero limitado de indices

#Funcion del algoritmo: se recorren uno a uno los elementos de la lista hasta el indice k y los compara con objetivo
def busqueda_lineal_limitada(arr, objetivo, k):
    for i in range(min(k, len(arr))):
        if arr[i] == objetivo:
            return i
    return -1  # No se encontró en los primeros 'k' elementos
