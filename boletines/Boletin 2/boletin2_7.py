#Realiza o ordinograma e despois codifica un programa que reciba como dato de entrada o valor dunha temperatura 
# expresada en graos centígrados e calcule o seu equivalente en graos Fahrenheit e graos Kelvin.
#
#Inicio
#  ↓
#[ Ler temperatura_C ]
#  ↓
#[ temperatura_F ← (temperatura_C × 9/5) + 32 ]
#  ↓
#[ temperatura_K ← temperatura_C + 273.15 ]
#  ↓
#[ Amosar temperatura_F ]
#  ↓
#[ Amosar temperatura_K ]
#  ↓
#Fin

def main():
    tempC = int(input("Ingrese Cantidad de Grados º "))
    tempF = (tempC * 9 / 5) + 32
    tempK = tempC + 273.15
    print(tempF)
    print(tempK)

if __name__ == "__main__":
    main()