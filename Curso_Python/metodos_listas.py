lista = list ([200,400,200000,34,209, True])

cadena = "hola"
#Devuelve la cantidad de una cadena
resultado = len(lista)
#agregando un elemento a una cadena
lista.append(90)

#agregando a la lista en un valor especifico
lista.insert(5,40)

#Agregando varios elementos a la lista
lista.extend([False,2025])
#Eliminando un elemento de la lista por su indice
lista.pop(-1)

#ordenando la lista
lista.sort()

#ordenando la lista si usamos reverse
lista.sort(reverse=True)

#Muestra elemento encontrado
elemento_encontrado = lista.index(209)


#Eliminando todos los datos de la lista

print(elemento_encontrado)
