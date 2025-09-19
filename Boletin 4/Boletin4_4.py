#4. Escribe un programa que solicite o usuario un número comprendido entre 1 e 99.
# O programa ten que mostralo con letras, por exemplo, para o 56, mostrará: “Cincuenta e seis”.

def main():
  num = int(input("Introduce un numero entre 1 y 99: "))

  cero_a_vente = {
    0: "",
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve",
    10: "diez",
    11: "once",
    12: "doce",
    13: "trece",
    14: "catorce",
    15: "quince",
    16: "dieciseis",
    17: "diecisiete",
    18: "dieciocho",
    19: "diecinueve"
  }

  decenas = {
    2: "veinti",
    3: "treinta",
    4: "cuarenta",
    5: "cincuenta",
    6: "sesenta",
    7: "setenta",
    8: "ochenta",
    9: "noventa"
  }

  if num < 1 or num > 99:
      print("Numero incorrecto")
  else:
      if num < 20:
        print(cero_a_vente[num])
      else:
        num = str(num)
        primernum = int(num[0])
        segundonum = int(num[1])
        if segundonum == 0:
          print(decenas[primernum],cero_a_vente[segundonum])
        else:
          print(decenas[primernum],"y",cero_a_vente[segundonum])

if __name__ == "__main__":
    main()