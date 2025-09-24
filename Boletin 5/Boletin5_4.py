#  4  Escribir un programa que imprima tódolos números pares entre dous números que se lle pidan o usuario.

def main():

    num1 = int(input("Ingrese primer numero: "))
    num2 = int(input("Ingrese segundo numero: "))
    x = num1
    while num1 <= num2:
        if num1 % 2 == 0:
            print(num1)
        num1 += 1

if __name__ == "__main__":
    main()