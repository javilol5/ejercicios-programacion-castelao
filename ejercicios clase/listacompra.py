#crear una lista de la compra
#  1 añadir productos
#  2 eliminar producot
#  3 mostrar la lista
#  4 salir


# Diccionario de artículos con emojis

emojis_articulos = {
    "leche": "🥛",
    "pan": "🍞",
    "huevos": "🥚",
    "manzanas": "🍎",
    "plátanos": "🍌",
    "naranjas": "🍊",
    "agua": "💧",
    "café": "☕",
    "té": "🍵",
    "queso": "🧀",
    "jamón": "🥓",
    "pollo": "🍗",
    "carne": "🥩",
    "pescado": "🐟",
    "arroz": "🍚",
    "pasta": "🍝",
    "tomates": "🍅",
    "lechuga": "🥬",
    "patatas": "🥔",
    "cebolla": "🧅",
    "ajo": "🧄",
    "aceite": "🫒",
    "sal": "🧂",
    "azúcar": "🍬",
    "galletas": "🍪",
    "chocolate": "🍫",
    "yogur": "🍶",
    "mantequilla": "🧈",
    "helado": "🍦",
    "pizza": "🍕",
    "cerveza": "🍺",
    "vino": "🍷",
    "refresco": "🥤",
    "detergente": "🧴",
    "papel higiénico": "🧻",
    "champú": "🧼",
    "jabón": "🫧",
    "cepillo de dientes": "🪥",
    "pasta de dientes": "🦷",
}


# Funciones para cada acción

def anhadir_producto(lista_compra):
    producto = input("Escribe el producto a añadir: ").lower()
    lista_compra.append(producto)
    return lista_compra

def eliminar_producto(lista_compra):
    producto = input("Escribe el producto a eliminar: ").lower()
    if producto in lista_compra:
        lista_compra.remove(producto)
        print(producto, "se ha eliminado")
    else:
        print("El producto no esta en la lista")
    return lista_compra

def mostrar_lista(lista_compra):
    print("\n🛒✨ TU LISTA DE LA COMPRA ✨🛒")
    print("====================================")

    if not lista_compra:
        print("🚫 La lista está vacía.")
    else:
        longitudes = []                                     #
        for producto in lista_compra:                       #   pilla la longitud
            emoji = emojis_articulos.get(producto, "🧾")    #    de el articulo mas largo
            texto = f"{emoji} {producto.capitalize()}"      #   para poner la "|" del final
            longitudes.append(len(texto))                   #   siempre a la misma altura
        ancho_max = max(longitudes) + 2                     #

    for i, producto in enumerate(lista_compra, start=1):
            emoji = emojis_articulos.get(producto, "🧾")
            texto = f"{emoji} {producto.capitalize()}"
            print(f"| {i}. | {texto.ljust(ancho_max)}|")

    print("====================================\n")

def menu():
    print("\n--- MENÚ ---")
    print("1 para añadir productos")
    print("2 para eliminar productos")
    print("3 para mostrar lista")
    print("4 para salir")
    return int(input("Elige una opcion: "))

def lista_compra_programa():
    lista_compra = ['leche','huevos','chocolate']

    while True:
        opcion = menu()

        if opcion == 1:
            lista_compra = anhadir_producto(lista_compra)

        elif opcion == 2:
            lista_compra = eliminar_producto(lista_compra)

        elif opcion == 3:
            mostrar_lista(lista_compra)

        elif opcion == 4:
            print("👋 Saliendo del programa.")
            break

        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# Ejecutar programa
lista_compra_programa()