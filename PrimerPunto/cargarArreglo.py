# Función para leer un archivo de texto y cargar los números en un arreglo
def cargar_arreglo_desde_archivo(nombre_archivo):
    arreglo = []
    with open(nombre_archivo, 'r') as f:
        for linea in f:
            arreglo.append(int(linea.strip()))  # Convertir cada línea en un número entero
    return arreglo
