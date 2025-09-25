# 14  Codificar o programa que solicite 10 números por consola e calcule a súa suma.
#     Si o usuario introduce en calquera momento o número 999,
#     deixa de solicitar máis números e presenta o valor da súma acadada ata ese momento.

def main():

    x = 1
    suma = 0
    num = int(input("Ingrese numero " + str(x) + " (999 para terminar): "))
    while num != 999 and x < 10:
        suma += num
        x += 1
        num = int(input("Ingrese numero " + str(x+1) + " (999 para terminar): "))

    print(suma)

if __name__ == "__main__":
    main()