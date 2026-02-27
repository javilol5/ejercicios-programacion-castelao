import csv
import os

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def guardar_en_archivo(self):
        linea = f"{self.nombre},{self.cantidad},{self.precio}"

        with open("datos.csv", "a", encoding="utf-8") as archivo:
            archivo.write(linea + "\n")


def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Añadir producto")
    print("2. Mostrar productos")
    print("3. Modificar producto")
    print("4. Importar productos .csv")
    print("5. Borrar producto")
    print("6. Salir")

def sumar_producto():
    nombre = input("Introduce el nombre del producto: ").capitalize()
    cantidad = int(input("Introduce la cantidad del producto: "))
    precio = round(float(input("Introduce el precio del producto: ")), 2)

    producto = Producto(nombre, cantidad, precio)

    producto.guardar_en_archivo()
    print("Producto guardado correctamente.")

def mostrar_producto():
    try:
        with open("datos.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            if not lineas:
                print("No hay productos guardados.")
            else:
                print("\n--- PRODUCTOS GUARDADOS ---")
                print("\n Nombre   Cantidad   Precio")
                for linea in lineas:
                    print(linea.strip())

    except FileNotFoundError:
        print("El archivo no existe todavía.")

def modificar_producto():
    try:
        with open("datos.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("No hay productos para modificar.")
            return

        print("\n--- PRODUCTOS ---")
        print("\nNombre   Cantidad   Precio")
        for i in range(len(lineas)):
            print(f"{lineas[i].strip()}")

        indice = int(input("Elige el numero del producto a modificar: "))-1

        if indice < 0:
            print("Numero inválido.")
            return

        linea = lineas[indice].strip()
        partes = linea.split(',')
        nombre = partes[0]
        cantidad = partes[1]
        precio = partes[2]

        print("\nProducto seleccionado:")
        print(f"{nombre}   {cantidad}   {precio}")

        print("\n¿Qué quieres modificar?")
        print("1. Cantidad: " + cantidad + ' ')
        print("2. Precio: " + precio + ' ')
        print("0. Salir")

        opcion = int(input("Elige una opción: "))
        if opcion == 0:
            print("Parar de modificar")
        elif opcion == 1:
            cantidad = int(input("Nueva cantidad de: " + nombre + ' '))
        elif opcion == 2:
            precio = int(input("Nuevo precio de: " + nombre + ' '))
        else:
            print("Opción no válida.")
            return

        nueva_linea = f"{nombre}   {cantidad}   {precio}\n"
        lineas[indice] = nueva_linea

        with open("datos.csv", "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas)

        print("Producto modificado correctamente.")
        print(nueva_linea)

    except FileNotFoundError:
        print("El archivo no existe.")
    except ValueError:
        print("Entrada inválida.")

def importar_producto():
    entrada = input("Introduce el nombre de un archivo CSV o datos (nombre,cantidad,precio): ").strip()

    # archivo CSV existente
    if os.path.isfile(entrada) and entrada.endswith(".csv"):
        try:
            with open(entrada, "r", encoding="utf-8") as csvfile:
                lector = csv.reader(csvfile)
                primera_fila = True

                with open("datos.csv", "a", encoding="utf-8") as archivo:
                    for fila in lector:

                        if primera_fila and not fila[1].isdigit():
                            primera_fila = False
                            continue

                        if len(fila) != 3:
                            continue

                        nombre = fila[0].capitalize()
                        cantidad = fila[1]
                        precio = fila[2]

                        linea = f"{nombre}   {cantidad}   {precio}"
                        archivo.write(linea + "\n")

            print("Datos importados desde el archivo CSV.")

        except Exception:
            print("Error al importar el archivo CSV.")

    #línea de datos
    else:
        try:
            partes = entrada.split(",")

            if len(partes) != 3:
                print("Formato incorrecto.")
                return

            nombre = partes[0].capitalize()
            cantidad = partes[1]
            precio = partes[2]

            with open("datos.csv", "a", encoding="utf-8") as archivo:
                archivo.write(f"{nombre}   {cantidad}   {precio}\n")

            print("Producto añadido correctamente.")

        except Exception:
            print("Error al añadir el producto.")

def borrar_producto():
    try:
        with open("datos.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("No hay productos para borrar.")
            return

        print("\n--- PRODUCTOS ---")
        print("\nNombre   Cantidad   Precio")
        for i in range(len(lineas)):
            print(f"{i + 1}. {lineas[i].strip()}")

        indice = int(input("Elige el numero del producto a borrar: ")) - 1

        if indice < 0:
            print("Nunero inválido.")
            return

        producto_borrado = lineas.pop(indice)

        with open("datos.csv", "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas)

        print(f"Producto borrado correctamente: {producto_borrado.strip()}")

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
            sumar_producto()
        elif opcion == 2:
            mostrar_producto()
        elif opcion == 3:
            modificar_producto()
        elif opcion == 4:
            importar_producto()
        elif opcion == 5:
            borrar_producto()
        elif opcion == 6:
            print("Saliendo del programa...")
        else:
            print("Opción no válida.")


main()