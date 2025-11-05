#Baseándote nesta información, elixe a letra a partir da numeración da seguinte táboa:
#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22	
#T R W A G M Y F P D X  B  N  J  Z  S  Q  V  H  L  C  K  E	
#
#Deseña unha aplicación na que, dado un número de DNI, calcule a letra que lle corresponde.
#  Observa que un número de 8 díxitos entra dentro do rango dun tipo int.

def main():
  dni = int(input("Introduce DNI sin letra: "))

  tabla = [
    "T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"
    ]

  numletra = dni % 23

  letra = tabla[numletra]

  print(f"El DNI completo es: {dni}{letra}")

if __name__ == "__main__":
    main()