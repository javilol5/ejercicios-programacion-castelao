#3- Codificar o programa que o teclear un número por teclado, 
# mostre por consola o signo “ + “ se o número é positivo, o signo “ –“ se é negativo e “ 0 “ se é cero.

def main():
  num = int(input("Introduce un numero: "))

  if num == 0:
    print('0')
  elif num > 0:
    print('+')
  else:
    print('-')

if __name__ == "__main__":
    main()