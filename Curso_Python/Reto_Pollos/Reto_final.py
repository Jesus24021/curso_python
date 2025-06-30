#Simulaciòn de incremento del peso de pollos
#Tu tarea consiste en generar una desviacion en el peso actual del pollo. 
#El programa debera elegir un dia aleatorio de desviacion en el incremento de peso apartir del dia 8 al 39,
#  provocando que no llegue al peso ideal al dia 39.
#Deberàs tener en cuenta lo siguiente: 
#1. Al dia 1 el peso, ya sea actual o ideal siempre sera 42 g.
#2. Al dia 39, el peso ideal debe ser de 3500 g, mientras que el peso actual debe ser menor por la desviacion 
# generada y además tener lógica con los dato.
#Al llegar al día 39, el programa debe regresar al día 1 y volver a generar los datos.
#Los datos generados deben imprimirse en consola en formato JSON.
#  Día x ->  {
#        "peso_ideal": peso_ideal,
#        "peso_actual": peso_actual
#    }
#El día de desviación del peso actual debe ser aleatorio entre el día 8 y 39 
#El programa debe imprimir el dia de desviación
#El programa debe imprimir los datos a partir del día de desviación en rojo
#Cada expresión de peso por dia debe tener un retardo de 1 segundo time.sleep(1)

import time
import json
import random
from colorama import Fore, Style, init

init(autoreset= True)

def reto_pollos():
    peso_inicio = 49
    dias_totales = 39
    peso_ideal_final = 3500
    incremento_ideal_diario = (peso_ideal_final - peso_inicio) / (dias_totales)

    while True:
        print("\n--- Nueva Simulación ---")
        peso_ideal = peso_inicio
        peso_actual = peso_inicio

        # Día aleatorio de desviación entre el 8 y el 39
        dia_desviacion = random.randint(8, dias_totales)
        print(Fore.GREEN + f"\nDía de desviación: {dia_desviacion}\n")

        desviacion_aplicada = False

        for dia in range(1, dias_totales + 1):
            peso_ideal += incremento_ideal_diario

            if dia >= dia_desviacion and not desviacion_aplicada:
                factor_desviacion = random.uniform(0.6, 0.85)  # entre 60% y 85%
                incremento_actual = incremento_ideal_diario * factor_desviacion
                desviacion_aplicada = True
            elif desviacion_aplicada:
                incremento_actual = incremento_ideal_diario * factor_desviacion
            else:
                incremento_actual = incremento_ideal_diario

            peso_actual += incremento_actual

            datos_dia = {
                "peso_ideal": round(peso_ideal, 2),
                "peso_actual": round(peso_actual, 2)
            }

            if dia >= dia_desviacion:
                print(Fore.RED + f"Día {dia} -> {json.dumps(datos_dia)}")
            else:
                print(Fore.WHITE + f"Día {dia} -> {json.dumps(datos_dia)}")

            time.sleep(1)

reto_pollos()    