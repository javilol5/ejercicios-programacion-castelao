#  5   Escribir un programa que reciba un número n por parámetro e imprima os primeiros n números triangulares, xunto co seu índice.
#  Os números triangulares obteñense mediante a suma dos números naturales dende 1 ata n.
#  É dicir, si se piden os primeros 5 números triangulares, o programa debe imprimir:

def main():

    num = int(input("Escribe un numero: "))
    if num < 0:
        print("No se admiten numeros negativos")
    else:
        i = 1
        sol = 0
        while i <= num:
            sol += i
            print(i, "-", sol)
            i += 1

if __name__ == "__main__":
    main()