# 2 Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius.
#   Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.

def main():

    tempF = int(input("Ingrese Cantidad de Grados Fº "))
    tempC = (5/9)*(tempF-32)
    print(tempC)

if __name__ == "__main__":
    main()