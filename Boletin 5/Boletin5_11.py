# 11 Codifica un programa que solicite un número e visualice a táboa de multiplicar dese número.
#  O programa seguirá pedindo números ata que o usuario pulse o número cero.

def main():

    x = 1
    num = int(input("ingrese numero: "))
    while num != 0:
        while x <=10:
            print(num,"x",x,"=",num*x)
            x += 1
        x = 0
        num = int(input("ingrese numero: "))
    else:
        print(0)

if __name__ == "__main__":
    main()