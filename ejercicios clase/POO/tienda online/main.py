from producto import Producto
from cliente import Cliente
from pedido import Pedido




producto1 = Producto("Leche", 3, 7)
producto2 = Producto("Pan", 1, 12)
producto3 = Producto("Huevos", 2, 14)
cliente1 = Cliente("Pepe", "pepe@gmail.com", "Su casa", 12345)
pedido1 = Pedido([], cliente1, "11/12/13")
pedido2 = Pedido([], cliente1, "11/12/17")

pedido1.añadirProducto(producto1, 5)
pedido1.añadirProducto(producto2, 3)
pedido1.añadirProducto(producto3, 12)
pedido1.mostrarCesta()

pedido2.añadirProducto(producto3, 2)
pedido2.añadirProducto(producto2, 1)
pedido2.mostrarCesta()