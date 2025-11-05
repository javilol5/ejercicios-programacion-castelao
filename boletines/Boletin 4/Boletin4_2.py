#2- Codifica un programa que, utilizando un menú de opcións, calcule a superficie de distinto tipo de figuras.
#O usuario seleccionará a opción desexada escribindo a opción. Segundo esta, o programa pediralle os datos necesarios para realizar o cálculo, visualizará o resultado .
#No caso de premer unha opción que non teña o menú visualizar unha mensaxe de “Opción incorrecta “.
#
#1…. Cadrado
#2…. Triangulo
#3…. Círculo

def main():

    print("1. Cuadrado")
    print("2. Triangulo")
    print("3. Circulo")

    PI = 3.1416

    opcion = input("Elige la opcion para calcular: ")

    if opcion == "1":
        lado = float(input("Introduce el lado del cuadrado: "))
        area = lado * lado
        print(f"La superficie del cuadrado es {area:.2f}")

    elif opcion == "2":
        base = float(input("Introduce la base del triangulo: "))
        altura = float(input("Introduce la altura del triangulo: "))
        area = (base * altura) / 2
        print(f"La superficie del triangulo es {area:.2f}")

    elif opcion == "3":
        radio = float(input("Introduce el radio de la circunferencia: "))
        area = PI * (radio ** 2)
        print(f"La superficie de la circunferencia es {area:.2f}")

    else:
        print("Opcion incorrecta")

if __name__ == "__main__":
    main()