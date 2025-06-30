#Reto 3:
#Crea un programa se encargue de transformar un número
#decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    return binario

try:
    numero_decimal = int(input("Ingresa un número decimal: "))
    if numero_decimal < 0:
        print("Por favor ingresa un número entero positivo.")
    else:
        resultado_binario = decimal_a_binario(numero_decimal)
        print(f"El número {numero_decimal} en binario es: {resultado_binario}")
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero.")