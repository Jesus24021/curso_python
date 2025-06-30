
#Descripcion:
#Saldo inicial: El cajero comenzara con un saldo predefinido de $1,000.00
#Opcion "Consultar saldo": Mostrara el saldo actual del usuario
#Opcion depositar (solicitar al usuario ingresar la cantidad a depositar, validar la cantidad que sea positiva,
#sumara la cantidad al saldo actual)
#opcion Retirar solicitar al usuario la cantidad a retirar. validar que la cantidad sea positiva y no exceda el saldo disponoible
#restar la cantidad del saldo actual. 
#opcion salir terminara la ejcucion


def cajero():
    saldo = 1000  # Saldo inicial predefinido
    while True:
        print("\n=== MENÚ DEL CAJERO AUTOMÁTICO ===")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            print(f"Su saldo actual es: ${saldo:.2f}")
        
        elif opcion == "2":
            try:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                if cantidad > 0:
                    saldo += cantidad
                    print(f"Depósito exitoso. Su nuevo saldo es: ${saldo:.2f}")
                else:
                    print("La cantidad debe ser positiva.")
            except ValueError:
                print("Entrada no válida. Ingrese un número.")
        
        elif opcion == "3":
            try:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                if cantidad > 0:
                    if cantidad <= saldo:
                        saldo -= cantidad
                        print(f"Retiro exitoso. Su nuevo saldo es: ${saldo:.2f}")
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("La cantidad debe ser positiva.")
            except ValueError:
                print("Entrada no válida. Ingrese un número.")
        
        elif opcion == "4":
            print("Gracias por usar el cajero. ¡Hasta pronto!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")


cajero()