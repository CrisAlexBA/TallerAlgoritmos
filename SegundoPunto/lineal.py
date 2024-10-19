# Basado en : https://pythondiario.com/2017/10/algoritmos-de-busqueda-en-python.html
#Busqueda Lineal
#Si objetivo esta en la lista devuelve su posicion, de lo contratio retorna -1

#Funcion del algoritmo: se recorren uno a uno los elementos de la lista y los compara con objetivo
def busqueda_lineal(arr, objetivo):
    for i in range(len(arr)): #El ciclo recorre todos los elementos de la lista, i contiene la posicion en el arreglo
        if arr[i] == objetivo:  #Verifica el valor de cada posicion, si se encuentra objetivo retorna la posicion
            return i  # Devuelve el índice donde se encontró
    return -1  # Si no se encuentra objetivo reotrna -1
