# Mini Reto1: imprimir una simulacion con pausa Y JSON
#Simula el kilometraje de un auto de cada 20 km durante un viaje de 100 km 
#imprime los datos con el formato JSON cada segundo


import json 
import time

distancia_total = 100
paso = 20

datos_viaje = []

for km in range(paso, distancia_total + 1, paso):
    registro = {"kilometraje": km, "estado": "En camino"}
    datos_viaje.append(registro)

    print(json.dumps(registro, indent=4))

    time.sleep(1)

final = {"kilometraje": distancia_total, "estado": "Has llegado a tu destino"}
print(json.dumps(final, indent=4))

