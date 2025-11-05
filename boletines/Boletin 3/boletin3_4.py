#4- Coñecidos, o nome e o peso de dúas persoas, 
# o programa escribirá por consola os datos da persoa que pesa máis e a diferenza de peso entre elas.

def main():
  np1 = str(input("Introduce el nombre de persona 1: "))
  pp1 = int(input("Introduce el peso de persona 1: "))
  np2 = str(input("Introduce el nombre de persona 2: "))
  pp2 = int(input("Introduce el peso de persona 2: "))

  if pp1 > pp2:
    print("Gana", np1, "que pesa", pp1, "y le saca", pp1 - pp2, "kg a", np2)
  else:
    print("Gana", np2, "que pesa", pp2, "y le saca", pp2 - pp1, "kg a", np1)

if __name__ == "__main__":
    main()