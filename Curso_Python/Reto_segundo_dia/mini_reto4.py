# Importamos el módulo 'time' para usar funciones de tiempo como sleep()
import time

# Importamos el módulo 'json' para convertir datos a formato JSON
import json

# Importamos el módulo 'random' para generar números aleatorios
import random

# Inicializamos la variable para llevar la cuenta de kilómetros totales recorridos
km_totales = 0

# Inicializamos la variable para el consumo ideal de combustible (1 litro cada 20 km)
consumo_ideal = 0

# Inicializamos la variable para el consumo real de combustible (puede variar)
consumo_real = 0

# Generamos un número aleatorio entre 3 y 5 para determinar en qué tramo ocurrirá una desviación
# randint incluye ambos extremos (3 y 5 son posibles)
tramo_desviacion = random.randint(3, 5)

# Mostramos un mensaje indicando en qué tramo ocurrirá la desviación
# Usamos un emoji para hacerlo más visual (🚨 = alarma/advertencia)
print(f"🚨 La desviación ocurrirá en el tramo: {tramo_desviacion}")

# Iniciamos un bucle que recorrerá los 5 tramos del viaje (de 1 a 5)
for tramo in range(1, 6):
    # Sumamos 20 km al total recorrido en cada tramo
    km_totales += 20

    # Sumamos 1 litro al consumo ideal (1 litro cada 20 km)
    consumo_ideal += 1

    # Verificamos si estamos antes o después del tramo de desviación
    if tramo < tramo_desviacion:
        # Antes de la desviación: consumo normal (1 litro)
        consumo = 1
    else:
        # Desde el tramo de desviación en adelante: consumo aumentado (1.5 litros)
        consumo = 1.5

    # Sumamos el consumo actual al consumo real total
    consumo_real += consumo

    # Creamos un diccionario con todos los datos importantes del tramo
    datos = {
        "tramo": tramo,  # Número del tramo actual (1-5)
        "km_recorridos": km_totales,  # Distancia total acumulada
        "consumo_ideal_litros": consumo_ideal,  # Consumo teórico perfecto
        "consumo_real_litros": round(consumo_real, 2)  # Consumo real con 2 decimales
    }

    # Imprimimos los datos del tramo formateados como JSON
    print(f"Tramo {tramo} -> {json.dumps(datos)}")

    # Pausamos la ejecución por 1 segundo para simular el paso del tiempo
    time.sleep(1)