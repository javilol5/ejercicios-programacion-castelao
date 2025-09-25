#  6 Escribir un programa que tome unha cantidade m de valores ingresados polo usuario,
#  a cada un lle calcule o factorial e imprima o resultado xunto co número de orden correspondiente.

def main():

    x = 1
    numeros = []
    num = int(input("Ingrese numero " + str(x) + " (0 para terminar): "))
    numeros.append(num)
    while num != 0:
        num = int(input("Ingrese numero " + str(x+1) + " (0 para terminar): "))
        numeros.append(num)
    else:
        numeros = numeros[:-1]
        for n in numeros:
            factorial = 1
            for i in range(1, n+1):
                factorial *= i
            print("Factorial de", n, "es",factorial)


if __name__ == "__main__":
    main()
