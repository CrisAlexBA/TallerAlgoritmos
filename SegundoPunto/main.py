import time
import matplotlib.pyplot as plt  # Para graficar los resultados
from cargarArreglo import cargar_arreglo_desde_archivo
from generarArreglo import generar_y_guardar_arreglo  # Importar la función para generar el arreglo
from lineal import busqueda_lineal
from lineal_limitado import busqueda_lineal_limitada
from binario import busqueda_binaria
from porSaltos import busqueda_por_saltos

# Función para medir el tiempo de ejecución del algoritmo de Burbuja
def medir_busqueda_lineal(nombre_archivo):
    arreglo = cargar_arreglo_desde_archivo(nombre_archivo)
    tiempo_inicio = time.time()
    r = busqueda_lineal(arreglo, 60671341)
    print(f"tiempo 1: {r}")
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    return tiempo_total

# Función para medir el tiempo de ejecución del algoritmo de Quicksort
def medir_lineal_limitada(nombre_archivo):
    arreglo = cargar_arreglo_desde_archivo(nombre_archivo)
    tiempo_inicio = time.time()
    r = busqueda_lineal_limitada(arreglo, 60671341, len(arreglo))
    print(f"tiempo 2: {r}")
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    return tiempo_total


#Funcion para medir el tiempo de ejecución del algoritmo de Stooge sort
def medir_busqueda_binaria(nombre_archivo):
    arreglo = cargar_arreglo_desde_archivo(nombre_archivo)
    tiempo_inicio = time.time()
    r = busqueda_binaria(arreglo, 60671341)
    print(f"tiempo 3: {r}")
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    return tiempo_total

#Funcion para medir el tiempo de ejecución del algoritmo de Pigeonhole sort
def medir_busqueda_porSaltos(nombre_archivo):
    arreglo = cargar_arreglo_desde_archivo(nombre_archivo)
    tiempo_inicio = time.time()
    r = busqueda_por_saltos(arreglo, 60671341)
    print(f"tiempo 4: {r}")
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
    tamano = 1000000  # Cambiar a 100000 o 1000000 para otras pruebas

    # Generar y guardar el arreglo en un archivo
    #generar_y_guardar_arreglo(tamano, nombre_archivo)

    # Ejecutar las pruebas y obtener los tiempos
    tiempos = []
    
    tiempo_lineal = medir_busqueda_lineal(nombre_archivo)
    tiempos.append(("Busqueda lineal ", tiempo_lineal))

    tiempo_limitada = medir_lineal_limitada(nombre_archivo)
    tiempos.append(("Busqueda lineal limitada ", tiempo_limitada))

    tiempo_binaria = medir_busqueda_binaria(nombre_archivo)
    tiempos.append(("Busqueda binaria ", tiempo_binaria))

    tiempo_porSaltos = medir_busqueda_porSaltos(nombre_archivo)
    tiempos.append(("Busqueda por saltos ", tiempo_porSaltos))
#-----------------------------------------------------------------------


    # Agregar más algoritmos aquí si los tienes implementados

    # Ordenar los tiempos de mayor a menor
    tiempos_ordenados = sorted(tiempos, key=lambda x: x[1], reverse=True)

    # Guardar los tiempos en un archivo de texto
    guardar_tiempos(tiempos_ordenados)

    # Graficar los tiempos
    graficar_tiempos(tiempos_ordenados)

if __name__ == "__main__":
    main()
