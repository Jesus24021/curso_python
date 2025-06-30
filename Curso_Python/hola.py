# Este programa realiza el detalle de la compra, el codigo pedira al usuario su nomnbre, el producto a comprar, 
# y la cantidad. En caso de que el usuario requiere agregar mas productos se preguntara, de lo contrario se imprime el detalle. 
def get_order():
    """Gets order details from the user."""
    client_name = input("Ingrese el nombre del cliente: ")
    products = []

    while True:

        product_name = input("Ingrese el nombre del producto: ")
        quantity = int(input("Ingrese la cantidad: "))

        if quantity <= 0:
            print("Cantidad inválida. Por favor, ingrese una cantidad mayor a 0.")
            continue
        else:
            products.append({'producto': product_name, 'cantidad': quantity})

        add_another = input("¿Desea agregar otro producto? (si/no): ").lower()
        if add_another != 'si':
            break

    print("\nResumen de la compra:")
    print(f"Cliente: {client_name}")
    print("Productos:")
    for item in products:
        print(f"  - Producto: {item['producto']}, Cantidad: {item['cantidad']}")

get_order()