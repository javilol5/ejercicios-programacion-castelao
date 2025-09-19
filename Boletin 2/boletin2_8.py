#Deseña un programa para o software dunha máquina, que converta una cantidade enteira de diñeiro, 
# que está presentada en billetes de 100, 20, 5 e moedas de 1 €, no seu equivalente en euros.
#  Por exemplo 2 billetes de 100€, 	3 billetes de 20 €, 6 moedas de 1€ visualizaríamos 266 € ).

def main():
    b100 = int(input("Cuantos billetes de 100? "))
    b20 = int(input("Cuantos billetes de 20? "))
    b5 = int(input("Cuantos billetes de 5? "))
    b1 = int(input("Cuantos billetes de 1? "))

    b100 = b100 * 100
    b20 = b20 * 20
    b5 = b5 * 5
    suma = b100 + b20 + b5 + b1
    print(suma)

if __name__ == "__main__":
    main()