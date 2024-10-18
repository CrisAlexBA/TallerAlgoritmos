import random

# Función para generar un arreglo de números aleatorios y guardarlos en un archivo
def generar_y_guardar_arreglo(tamano, nombre_archivo):
    try:
        # Abrimos el archivo con permisos de escritura
        with open(nombre_archivo, 'w') as f:
            for _ in range(tamano):
                # Generar un número aleatorio de 8 dígitos
                numero = random.randint(10000000, 99999999)
                # Escribir el número en el archivo
                f.write(f"{numero}\n")
        print(f"Arreglo de {tamano} números generado y guardado en {nombre_archivo}")
    except OSError as e:
        # Manejar cualquier error relacionado con el archivo
        print(f"Error al generar el archivo: {e}")
