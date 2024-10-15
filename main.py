import time
from bubble_sort import bubble_sort  # Importa la función del archivo bubble_sort.py
from generate_array import generate_array  # Importa la función para generar los datos
from ordenamiento_quicksort import quicksort

# Función para medir el tiempo de ejecución del algoritmo de burbuja
def measure_bubble_sort(size):
    # Generar el arreglo de tamaño dado
    array = generate_array(size)
    
    # Medir el tiempo antes de ejecutar el algoritmo
    start_time = time.time()
    print(f"entro al metodo")
    # Ejecutar el algoritmo de burbuja
    bubble_sort(array)
    
    # Medir el tiempo después de ejecutar el algoritmo
    end_time = time.time()
    
    # Calcular el tiempo total de ejecución
    total_time = end_time - start_time
    return total_time

size = 100000  # Cambiar por 100000 o 1000000 para otras pruebas
time_taken = measure_bubble_sort(size)
print(f"Tiempo de ejecución para Bubble Sort con {size} elementos: {time_taken:.6f} segundos")

