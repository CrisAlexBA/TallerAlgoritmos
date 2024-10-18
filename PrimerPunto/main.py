import time
import matplotlib.pyplot as plt  # Para graficar los resultados
from burbuja import bubbleSort
from quicksort import quickSort
from stoogeSort import stoogesort
from pigeonholeSort import pigeonhole_sort
from mergeSort import merge_sort
from bitonicSort import sort
from cargarArreglo import cargar_arreglo_desde_archivo
from generarArreglo import generar_y_guardar_arreglo  # Importar la función para generar el arreglo

# Función para medir el tiempo de ejecución del algoritmo de Burbuja
def medir_ordenamiento_burbuja(nombre_archivo):
    arreglo = cargar_arreglo_desde_archivo(nombre_archivo)
    tiempo_inicio = time.time()
    bubbleSort(arreglo)
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    return tiempo_total

# Función para medir el tiempo de ejecución del algoritmo de Quicksort
def medir_quicksort(nombre_archivo):
    arreglo = cargar_arreglo_desde_archivo(nombre_archivo)
    tiempo_inicio = time.time()
    quickSort(arreglo, 0, len(arreglo)-1)
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    return tiempo_total


#Funcion para medir el tiempo de ejecución del algoritmo de Stooge sort
def medir_stoogesort(nombre_archivo):
    arreglo = cargar_arreglo_desde_archivo(nombre_archivo)
    tiempo_inicio = time.time()
    stoogesort(arreglo, 0, len(arreglo)-1)
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    return tiempo_total

#Funcion para medir el tiempo de ejecución del algoritmo de Pigeonhole sort
def medir_pigeonholesort(nombre_archivo):
    arreglo = cargar_arreglo_desde_archivo(nombre_archivo)
    tiempo_inicio = time.time()
    pigeonhole_sort(arreglo)
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    return tiempo_total

#Funcion para medir el tiempo de ejecución del algoritmo de Merge sort
def medir_mergesort(nombre_archivo):
    arreglo = cargar_arreglo_desde_archivo(nombre_archivo)
    tiempo_inicio = time.time()
    merge_sort(arreglo, 0, len(arreglo)-1)
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    return tiempo_total

#Funcion para medir el tiempo de ejecución del algoritmo de Bitonic sort
def medir_bitonicsort(nombre_archivo):
    arreglo = cargar_arreglo_desde_archivo(nombre_archivo)
    tiempo_inicio = time.time()
    sort(arreglo, len(arreglo)-1, 1)
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    return tiempo_total



# Guardar los tiempos en una lista
def guardar_tiempos(tiempos):
    with open("resultados_tiempos.txt", 'w') as f:
        for algoritmo, tiempo in tiempos:
            f.write(f"{algoritmo}: {tiempo:.6f} segundos\n")

# Graficar los tiempos en un gráfico de barras
def graficar_tiempos(tiempos):
    algoritmos = [x[0] for x in tiempos]
    tiempos_ejecucion = [x[1] for x in tiempos]

    plt.barh(algoritmos, tiempos_ejecucion, color='skyblue')
    plt.xlabel('Tiempo de ejecución (segundos)')
    plt.ylabel('Algoritmo de ordenamiento')
    plt.title('Comparación de tiempos de ejecución de algoritmos de ordenamiento')
    plt.gca().invert_yaxis()
    plt.show()

# Función principal para ejecutar los algoritmos y ordenar los tiempos
def main():
    nombre_archivo = 'arreglo_10000.txt'
    tamano = 100000  # Cambiar a 100000 o 1000000 para otras pruebas

    # Generar y guardar el arreglo en un archivo
    generar_y_guardar_arreglo(tamano, nombre_archivo)

    # Ejecutar las pruebas y obtener los tiempos
    tiempos = []
    
    tiempo_burbuja = medir_ordenamiento_burbuja(nombre_archivo)
    tiempos.append(("Ordenamiento Burbuja", tiempo_burbuja))
    
    tiempo_quicksort = medir_quicksort(nombre_archivo)
    tiempos.append(("Quicksort", tiempo_quicksort))

    tiempo_pigeonhole = medir_pigeonholesort(nombre_archivo)
    tiempos.append(("Ordenamiento Pigeonhole", tiempo_pigeonhole))

    tiempo_Merge = medir_mergesort(nombre_archivo)
    tiempos.append(("Ordenamiento Merge", tiempo_Merge))

    tiempo_Bitonic = medir_bitonicsort(nombre_archivo)
    tiempos.append(("Ordenamiento Bitonic", tiempo_Bitonic))
    
    #En lo posible si se va a recorrer el código dejarlo comentado para que de una solución, 
    #de lo contrario tardará mucho en dar respuesta(nunca)
    tiempo_stooge = medir_stoogesort(nombre_archivo)
    tiempos.append(("Ordenamiento Stooge", tiempo_stooge))

#-----------------------------------------------------------------------


    # Agregar más algoritmos aquí si los tienes implementados

    # Ordenar los tiempos de mayor a menor
    tiempos_ordenados = sorted(tiempos, key=lambda x: x[1], reverse=True)

    # Guardar los tiempos en un archivo de texto
#    guardar_tiempos(tiempos_ordenados)

    # Graficar los tiempos
    graficar_tiempos(tiempos_ordenados)

if __name__ == "__main__":
    main()
