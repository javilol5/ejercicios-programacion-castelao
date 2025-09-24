#  6 Escribir un programa que tome unha cantidade m de valores ingresados polo usuario,
#  a cada un lle calcule o factorial e imprima o resultado xunto co número de orden correspondiente.









##Solucion de ChatGPT

# Función para calcular o factorial
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Cantidade de valores a introducir
m = int(input("Cantos valores queres introducir? "))

for i in range(1, m + 1):
    valor = int(input(f"Introduce o valor #{i}: "))
    fact = factorial(valor)
    print(f"{i}) O factorial de {valor} é {fact}")