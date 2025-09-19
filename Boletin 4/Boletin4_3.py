#3. Utiliza o operador ternario para calcular o valor absoluto dun número que se solicita o usuario por teclado.

def main():
  num = int(input("Introduce numero: "))

  if num > 0:
    print(num)
  elif num < 0:
    print(-num)
  else:
    print(0)

if __name__ == "__main__":
    main()