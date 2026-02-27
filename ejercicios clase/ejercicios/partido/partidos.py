import csv
import os

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
    print("4. Importar archivo .csv")
    print("5. Borrar partido")
    print("6. Salir")


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

def importar_datos():
    entrada = input("Introduce el nombre de un archivo CSV o datos (equipo1,equipo2,p1,p2): ").strip()

    # archivo CSV existente
    if os.path.isfile(entrada) and entrada.endswith(".csv"):
        try:
            with open(entrada, "r", encoding="utf-8") as csvfile:
                lector = csv.reader(csvfile)
                primera_fila = True

                with open("resultados.txt", "a", encoding="utf-8") as archivo:
                    for fila in lector:

                        if primera_fila and not fila[2].isdigit():
                            primera_fila = False
                            continue

                        if len(fila) != 4:
                            continue

                        equipo1 = fila[0]
                        equipo2 = fila[1]
                        p1 = fila[2]
                        p2 = fila[3]

                        linea = f"{equipo1} {equipo2} ({p1}-{p2})"
                        archivo.write(linea + "\n")

            print("Datos importados desde el archivo CSV.")

        except Exception:
            print("Error al importar el archivo CSV.")

    #línea de datos
    else:
        try:
            partes = entrada.split(",")

            if len(partes) != 4:
                print("Formato incorrecto.")
                return

            equipo1 = partes[0]
            equipo2 = partes[1]
            p1 = partes[2]
            p2 = partes[3]

            with open("resultados.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"{equipo1} {equipo2} ({p1}-{p2})\n")

            print("Partido añadido correctamente.")

        except Exception:
            print("Error al añadir el partido.")

def borrar_partido():
    try:
        with open("resultados.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("No hay partidos para borrar.")
            return

        print("\n--- PARTIDOS ---")
        for i in range(len(lineas)):
            print(f"{i + 1}. {lineas[i].strip()}")

        indice = int(input("Elige el número del partido a borrar: ")) - 1

        if indice < 0 or indice >= len(lineas):
            print("Número inválido.")
            return

        partido_borrado = lineas.pop(indice)

        with open("resultados.txt", "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas)

        print(f"Partido borrado correctamente: {partido_borrado.strip()}")

    except FileNotFoundError:
        print("El archivo no existe.")
    except ValueError:
        print("Entrada inválida. Introduce un número.")

def main():
    opcion = 0

    while opcion != 6:
        mostrar_menu()
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            pedir_partido()
        elif opcion == 2:
            mostrar_partido()
        elif opcion == 3:
            modificar_partido()
        elif opcion == 4:
            importar_datos()
        elif opcion == 5:
            borrar_partido()
        elif opcion == 6:
            print("Saliendo del programa...")
        else:
            print("Opción no válida.")


main()