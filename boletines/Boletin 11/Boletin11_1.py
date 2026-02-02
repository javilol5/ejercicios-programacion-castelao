#1 Crear un programa xestor de notas persoais, que permita ao usuario gardar e consultar notas.
#O usuario pode engadir unha nova nota (texto libre).
#
#As notas gárdanse nun ficheiro de texto (notas.txt), unha por liña.
#
#O programa pode listar todas as notas gardadas.
#
#O usuario pode buscar notas que conteñan unha palabra clave.


import os

RUTA_BASE = os.path.dirname(os.path.abspath(__file__))
RUTA_NOTAS = os.path.join(RUTA_BASE, "notas_ejercicio_1.txt")


def engadir_nota():
    nota = input("Escribe una nota: ")
    with open(RUTA_NOTAS, "a", encoding="utf-8") as ficheiro:
        ficheiro.write(nota + "\n")
    print("Nota gardada correctamente.\n")


def listar_notas():
    try:
        with open(RUTA_NOTAS, "r", encoding="utf-8") as ficheiro:
            notas = ficheiro.readlines()

        if len(notas) == 0:
            print("No hay ninguna nota guardada.\n")
        else:
            print("Notas guardadas:")
            for i in range(len(notas)):
                print(f"{i + 1}. {notas[i].strip()}")
            print()
    except FileNotFoundError:
        print("No existe notas.\n")


def buscar_notas():
    palabra = input("Introducir a palabra clave: ")
    encontradas = False

    try:
        with open(RUTA_NOTAS, "r", encoding="utf-8") as ficheiro:
            for liña in ficheiro:
                if palabra.lower() in liña.lower():
                    print(liña.strip())
                    encontradas = True

        if not encontradas:
            print("No se encontraron notas con esa palabra.\n")
        else:
            print()
    except FileNotFoundError:
        print("No existe notas.\n")


def menu():
    print("GESTOR DE NOTAS PERSONALES")
    print("1. Añadir nota")
    print("2. Listar notas")
    print("3. Buscar notas")
    print("4. Salir")


def main():
    opcion = 0
    while opcion != 4:
        menu()
        opcion = int(input("Elige unha opcion: "))
        print()

        if opcion == 1:
            engadir_nota()
        elif opcion == 2:
            listar_notas()
        elif opcion == 3:
            buscar_notas()
        elif opcion == 4:
            print("Fin del programa.")
        else:
            print("Opcion no valida.\n")


main()
