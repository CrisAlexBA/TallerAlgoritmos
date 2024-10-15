import random

# Función para generar un arreglo de números aleatorios de 8 dígitos
def generate_array(size):
    return [random.randint(10000000, 99999999) for _ in range(size)]
