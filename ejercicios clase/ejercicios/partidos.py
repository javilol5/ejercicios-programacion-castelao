class Partido:
    def __init__(self, equipo1, equipo2, puntuacion_equipo1, puntuacion_equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.puntuacion_equipo1 = puntuacion_equipo1
        self.puntuacion_equipo2 = puntuacion_equipo2

    def guardar_en_archivo(self):
        linea = f"{self.equipo1} {self.equipo2} ({self.puntuacion_equipo1}-{self.puntuacion_equipo2})"

        with open("resultados.txt", "a", encoding="utf-8") as archivo:
            archivo.write(linea + "\n")


def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Añadir partido")
    print("2. Mostrar partido")
    print("3. Modificar partido")
    print("4. Salir")


def pedir_partido():
    equipo1 = input("Introduce el nombre del equipo 1: ").capitalize()
    equipo2 = input("Introduce el nombre del equipo 2: ").capitalize()

    puntuacion_equipo1 = int(input("Puntuación del equipo 1: "))
    puntuacion_equipo2 = int(input("Puntuación del equipo 2: "))

    partido = Partido(
        equipo1,
        equipo2,
        puntuacion_equipo1,
        puntuacion_equipo2
    )

    partido.guardar_en_archivo()
    print("Partido guardado correctamente.")

def mostrar_partido():
    try:
        with open("resultados.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            if not lineas:
                print("No hay partidos guardados.")
            else:
                print("\n--- PARTIDOS GUARDADOS ---")
                for linea in lineas:
                    print(linea.strip())

    except FileNotFoundError:
        print("El archivo no existe todavía.")

def modificar_partido():
    try:
        with open("resultados.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("No hay partidos para modificar.")
            return

        print("\n--- PARTIDOS ---")
        for i in range(len(lineas)):
            print(f"{i + 1}. {lineas[i].strip()}")

        indice = int(input("Elige el número del partido a modificar: ")) - 1

        if indice < 0 or indice >= len(lineas):
            print("Número inválido.")
            return

        linea = lineas[indice].strip()
        partes = linea.split(" ")
        equipo1 = partes[0]
        equipo2 = partes[1]
        resultado = partes[2].replace("(", "").replace(")", "")
        puntuacion_equipo1, puntuacion_equipo2 = resultado.split("-")

        print("\nPartido seleccionado:")
        print(f"{equipo1} {equipo2} ({puntuacion_equipo1}-{puntuacion_equipo2})")

        print("\n¿Qué quieres modificar?")
        print("1. Equipo: " + equipo1 + ' ')
        print("2. Equipo: " + equipo2 + ' ')
        print("3. Puntuación equipo: " + puntuacion_equipo1 + ' ')
        print("4. Puntuación equipo: " + puntuacion_equipo2 + ' ')

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            equipo1 = input("Nuevo nombre del equipo: " + equipo1 + ' ').capitalize()
        elif opcion == 2:
            equipo2 = input("Nuevo nombre del equipo: " + equipo2 + ' ').capitalize()
        elif opcion == 3:
            puntuacion_equipo1 = input("Nueva puntuación del equipo: " + puntuacion_equipo1 + ' ')
        elif opcion == 4:
            puntuacion_equipo2 = input("Nueva puntuación del equipo: " + puntuacion_equipo2 + ' ')
        else:
            print("Opción no válida.")
            return

        nueva_linea = f"{equipo1} {equipo2} ({puntuacion_equipo1}-{puntuacion_equipo2})\n"
        lineas[indice] = nueva_linea

        with open("resultados.txt", "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas)

        print("Partido modificado correctamente.")
        print(nueva_linea)

    except FileNotFoundError:
        print("El archivo no existe.")
    except ValueError:
        print("Entrada inválida.")


def main():
    opcion = 0

    while opcion != 4:
        mostrar_menu()
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            pedir_partido()
        elif opcion == 2:
            mostrar_partido()
        elif opcion == 3:
            modificar_partido()
        elif opcion == 4:
            print("Saliendo del programa...")
        else:
            print("Opción no válida.")


main()