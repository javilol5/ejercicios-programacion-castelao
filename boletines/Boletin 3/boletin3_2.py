#2- Escribe un programa no que se tecleen dous números.
#  Se o primeiro é maior ou igual que o segundo,visualizaremos a resta.
#  En calquera caso visualizaremos a suma.

def main():
  num1 = int(input("Introduce numero 1: "))
  num2 = int(input("Introduce numero 2: "))

  if num1 >= num2:
    print(num1 - num2)
  else:
    print(num1 + num2)

if __name__ == "__main__":
    main()