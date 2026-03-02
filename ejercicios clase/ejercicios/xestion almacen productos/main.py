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
    print("6. Operaciones")
    print("0. Salir")

def sumar_producto():
    nombre = input("Introduce el nombre del producto: ").capitalize()
    cantidad = int(input("Introduce la cantidad del producto: "))
    precio = float(input("Introduce el precio del producto: "))

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
                print(f"{'ID':<5}{'Nombre':<15}{'Cantidad':>10}{'Precio':>10}")
                print(f"{'--':<5}{'------':<15}{'--------':>10}{'------':>10}")
                for indice, linea in enumerate(lineas, start=1):
                    nombre, cantidad, precio = linea.strip().split(",")

                    precio = round(float(precio), 2)

                    print(f"{indice:<5}{nombre:<15}{cantidad:>10}{precio:>10.2f}")

    except FileNotFoundError:
        print("El archivo no existe todavía.")

def modificar_producto():
    try:
        with open("datos.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("No hay productos para modificar.")
            return

        else:
            mostrar_producto()

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

                        producto = Producto(nombre, cantidad, precio)

                        producto.guardar_en_archivo()

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
            producto = Producto(nombre, cantidad, precio)

            producto.guardar_en_archivo()

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

        mostrar_producto()

        indice = int(input("Elige el numero del producto a borrar: ")) - 1

        if indice < 0:
            print("Cancelado.")
            return

        producto_borrado = lineas.pop(indice)

        with open("datos.csv", "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas)

        print(f"Producto borrado correctamente: {producto_borrado.strip()}")

    except FileNotFoundError:
        print("El archivo no existe.")
    except ValueError:
        print("Entrada inválida. Introduce un número.")

def menu_operaciones():
    opcion = 999
    while opcion != 0:

        print("\n--- MENÚ OPERACIONES---")
        print("1. Aumentar stock producto")
        print("2. Disminuir stock producto")
        print("3. Calcular stock almacen")
        print("4. Calcular costo cantidad producto")
        print("5. Calcular costo producto")
        print("6. Calcular costo almacen")
        print("0. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            aumentar_stock()
        elif opcion == 2:
            disminuir_stock()
        elif opcion == 3:
            calcular_stock()
        elif opcion == 4:
            calcular_precio_cantidad_producto()
        elif opcion == 5:
            calcular_precio_producto()
        elif opcion == 6:
            calcular_precio_almacen()
        elif opcion == 0:
            print("Saliendo del programa...")
        else:
            print("Opción no válida.")

def aumentar_stock():

    try:
        with open("datos.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("No hay productos para modificar.")
            return

        mostrar_producto()

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

        stock = int(input("Cuanto stock aumenta: "))
        cantidad = int(cantidad)
        cantidad += stock

        nueva_linea = f"{nombre},{cantidad},{precio}\n"
        lineas[indice] = nueva_linea

        producto = Producto(nombre, cantidad, precio)

        with open("datos.csv", "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas)

        print("Producto modificado correctamente.")
        print(nueva_linea)

    except FileNotFoundError:
        print("El archivo no existe.")
    except ValueError:
        print("Entrada inválida.")


def disminuir_stock():
    try:
        with open("datos.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("No hay productos para modificar.")
            return

        mostrar_producto()

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

        stock = int(input("Cuanto stock aumenta: "))
        cantidad = int(cantidad)
        cantidad -= stock

        nueva_linea = f"{nombre},{cantidad},{precio}\n"
        lineas[indice] = nueva_linea

        producto = Producto(nombre, cantidad, precio)

        with open("datos.csv", "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas)

        print("Producto modificado correctamente.")
        print(nueva_linea)

    except FileNotFoundError:
        print("El archivo no existe.")
    except ValueError:
        print("Entrada inválida.")


def calcular_stock():
    try:
        with open("datos.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("No hay productos para calcular.")
            return

        total = 0

        for linea in lineas:
            linea = linea.strip()
            partes = linea.split(",")

            cantidad = int(partes[1])
            total += cantidad

        print(f"\nStock total disponible: {total}")

    except FileNotFoundError:
        print("El archivo no existe.")
    except ValueError:
        print("Entrada inválida.")

def calcular_precio_cantidad_producto():
    try:
        with open("datos.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("No hay productos para calcular.")
            return

        mostrar_producto()

        indice = int(input("Elige el numero del producto para calcular: "))-1

        if indice < 0 or indice >= len(lineas):
            print("Numero inválido.")
            return

        linea = lineas[indice].strip()
        partes = linea.split(',')
        nombre = partes[0]
        cantidad = int(partes[1])
        precio = float(partes[2])


        print("\nProducto seleccionado:")
        print(f"{nombre}   {cantidad}   {precio}")

        mult = int(input("Cuantidad de productos a calcular: "))

        if mult > cantidad or mult <= 0:
            print("cantidad invalida")
        else:
            total = mult * precio
            print(f"Precio total por {mult} unidades: {total:.2f} €")


    except FileNotFoundError:
        print("El archivo no existe.")
    except ValueError:
        print("Entrada inválida.")

def calcular_precio_producto():

    try:
        with open("datos.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("No hay productos para calcular.")
            return

        mostrar_producto()

        indice = int(input("Elige el numero del producto para calcular: "))-1

        if indice < 0 or indice >= len(lineas):
            print("Numero inválido.")
            return

        linea = lineas[indice].strip()
        partes = linea.split(',')
        nombre = partes[0]
        cantidad = int(partes[1])
        precio = float(partes[2])


        print("\nProducto seleccionado:")
        print(f"{nombre}   {cantidad}   {precio}")


        total = cantidad * precio
        print(f"Precio total por {cantidad} unidades: {total:.2f} €")


    except FileNotFoundError:
        print("El archivo no existe.")
    except ValueError:
        print("Entrada inválida.")

def calcular_precio_almacen():
    try:
        with open("datos.csv", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("No hay productos para calcular.")
            return

        mostrar_producto()

        total = 0

        for linea in lineas:
            linea = linea.strip()
            partes = linea.split(",")

            cantidad = int(partes[1])
            precio = float(partes[2])
            sumar = cantidad * precio
            total += sumar

        print(f"\nStock total disponible: {total:.2f} €")

    except FileNotFoundError:
        print("El archivo no existe.")
    except ValueError:
        print("Entrada inválida.")



def main():
    opcion = 999

    while opcion != 0:
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
            menu_operaciones()
        elif opcion == 0:
            print("Saliendo del programa...")
        else:
            print("Opción no válida.")


main()