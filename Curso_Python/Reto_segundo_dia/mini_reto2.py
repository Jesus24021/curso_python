# Mini Reto1: simular una variable ideal acumulativa
#Simula el kilometraje de un auto de cada 20 km durante un viaje de 100 km 
#imprime los datos con el formato JSON cada segundo
import json 
import time 

distancia_total = 100
paso = 20
consumo_por_tramo = 1 

consumo_acumulado = 0 


for km in range(
    paso, distancia_total + 1, paso):
    consumo_acumulado += consumo_por_tramo

    registro ={
        "Kilometraje": km,
        "consumo_gasolina_litros": consumo_acumulado
    }

    print(json.dumps(registro, indent=4))

