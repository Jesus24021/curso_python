#Reto 5:(Dificil)

# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en
#  la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=", " if i < n - 1 else "\n")
        a, b = b, a + b

fibonacci(50)