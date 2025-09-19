#1- Codifica un programa que solicite un número por teclado e que saque un mensaxe que diga
#  “É un número positivo”, sempre que cumpra esa condición.

def main():
  num = int(input("Introduce un numero "))

  if num >= 0:
    print("Es un numero positivo")
  else:
    print("Es un numero negativo")

if __name__ == "__main__":
    main()