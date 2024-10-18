from quicksort import quickSort  # Importa la función Quicksort desde otro archivo
import random

# Función para generar un arreglo de números aleatorios y guardarlo en un archivo
def generar_y_guardar_arreglo(tamano, nombre_archivo):
    with open(nombre_archivo, 'w') as f:
        for _ in range(tamano):
            numero = random.randint(10000000, 99999999)  # Genera número de 8 dígitos
            f.write(f"{numero}\n")
    print(f"Arreglo de {tamano} números generado y guardado en {nombre_archivo}")

# Función para ordenar el arreglo de mayor a menor usando Quicksort
def ordenar_con_quicksort(arreglo):
    arreglo_ordenado = quickSort(arreglo)
    print("Arreglo ordenado de mayor a menor usando Quicksort.")
    return arreglo_ordenado

# Función para guardar el arreglo ordenado en un archivo
def guardar_arreglo_ordenado(arreglo, nombre_archivo):
    with open(f"ordenado_{nombre_archivo}", 'w') as f:
        for numero in arreglo:
            f.write(f"{numero}\n")
    print(f"Arreglo ordenado guardado en 'ordenado_{nombre_archivo}'")
