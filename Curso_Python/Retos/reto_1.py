import random
#Pedir un dato al usuario 

nombre = input("Dame tu nombre:" )
nombre1 = nombre[:2]
apellido = input("Dame tu apellido:" )
apellido1 = apellido[:2]
ano_nac = input("Dame tu año de nacimiento:" )

ano_nac1 = ano_nac[2:4]

aleatorio = str (random.randint(0,9999))

resultado_final = nombre1 + apellido1 + ano_nac1 + aleatorio

#Muestra
print(f'Resultado final: {resultado_final}')
