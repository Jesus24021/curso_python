import time
import json
import random
from colorama import Fore, Style, init

init(autoreset= True)

km_totales = 0
consumo_ideal = 0
consumo_real = 0

tramo_desviacion = random.randint(3,5)
print(f"{Fore.YELLOW} La desviacion ocurrirà en el tramo: {tramo_desviacion}")

for tramo in range(1,6):
    km_totales += 20
    consumo_ideal += 1

    if tramo < tramo_desviacion:
        consumo = 1
        color = Style.RESET_ALL
    else:
        consumo = 1.5
        color = Fore.RED

    consumo_real += consumo

    datos = {
        "tramo": tramo,
        "km_recorridos": km_totales,
        "consumo_ideal_litros": consumo_ideal,
        "consumo_real_litros": round(consumo_real, 2)
    }

    print(color + f"Tramo {tramo} -> {json.dumps(datos)}")
    time.sleep(1)