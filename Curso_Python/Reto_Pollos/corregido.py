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

import time # Sirve patra hacer pausas
import json # permite mostrar los datos de manera ordenada
import random # se usa para obtener numero de manera aleatoria
from colorama import Fore, Style, init # Sirve para colorear el texto de la consola

init()

def reto_pollos(): # Creando la funcion
    peso_inicio = 42 # Declarando las variables a ocupar
    dias_totales = 39
    peso_ideal = 3500
    incremento_ideal_diario = (peso_ideal - peso_inicio) / (dias_totales)
    #El calculo de cuanto tiene que incrementar el peso cada dia
    while True: #Ayuda a que el proceso se repita N veces
        print("\n--- Nueva Simulación ---")
        peso_ideal = peso_inicio
        peso_actual = peso_inicio

        # Random se usa para que de un numero al azar entre 8 y 39 
        dia_desviacion = random.randint(8, dias_totales)
        #Muestra en verde el dia de la desviacion
        print(Fore.GREEN + f"\nDía de desviación: {dia_desviacion}\n")

        desviacion_aplicada = False

        for dia in range(1, dias_totales + 1):
            peso_ideal += incremento_ideal_diario #El peso va subiendo desde el principio

            if dia == dia_desviacion +1 and not desviacion_aplicada:
                factor_desviacion = random.uniform(0.6, 0.85)  # entre 60% y 85%
                incremento_actual = incremento_ideal_diario * factor_desviacion
                desviacion_aplicada = True
            elif desviacion_aplicada:
                incremento_actual = incremento_ideal_diario * factor_desviacion
            else:
                incremento_actual = incremento_ideal_diario #Si no llega la desviacion sigue normal

            peso_actual += incremento_actual
            
            datos_dia = {#Guarda el peso ideal y el peso real del día en un formato ordenado JSON
                "peso_ideal": round(peso_ideal, 2),
                "peso_actual": round(peso_actual, 2)
            }

            if dia >= dia_desviacion:
                print(Fore.RED + f"Día {dia} -> {json.dumps(datos_dia)}")
            else:
                print(Fore.WHITE + f"Día {dia} -> {json.dumps(datos_dia)}")

            time.sleep(1)

reto_pollos()   