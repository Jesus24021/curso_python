import time
import json
import random # Se importa random para aleatorio

km_totales = 0
consumo_ideal = 0

tramo_desviacion = random.randint(3, 5)
print(f"🚨 La desviación ocurrirá en el tramo: {tramo_desviacion}")#Este es el unico cambio <===============================

for tramo in range(1, 6):
    km_totales += 20
    consumo_ideal += 1

    datos = {
        "tramo": tramo,
        "km_recorridos": km_totales,
        "consumo_ideal_litros": consumo_ideal
    }
    print(f"Tramo {tramo} -> {json.dumps(datos)}")
    time.sleep(1)