class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def setNombre(self, nombre):
        self.__nombre = nombre
    def setPrecio(self, precio):
        self.__precio = precio
    def setStock(self, stock):
        self.__stock = stock

    def getNombre(self):
        return self.__nombre
    def getPrecio(self):
        return self.__precio
    def getStock(self):
        return self.__stock

    def anadirPedido(self, cantidad):
        if cantidad > 0 and cantidad <= self.__stock:
            self.__stock -= cantidad
            return True
        return False

    def incrementarStock(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad




class Cliente:
    def __init__(self, nombre, email, direccion, cp):
        self.__nombre = nombre
        self.__email = email
        self.__direccion = direccion
        self.__cp = cp

    def setNombre(self, nombre):
        self.__nombre = nombre
    def setEmail(self, email):
        self.__email = email
    def setDireccion(self, direccion):
        self.__direccion = direccion
    def setCp(self, cp):
        self.__cp = cp

    def getNombre(self):
        return self.__nombre
    def getEmail(self):
        return self.__email
    def getDireccion(self):
        return self.__direccion
    def getCp(self):
        return self.__cp



class Pedido:
    def __init__(self, cesta, cliente, fecha):
        self.__cesta = cesta
        self.__cliente = cliente
        self.__fecha = fecha


    def setCesta(self, cesta):
        self.__cesta = cesta
    def setCliente(self, cliente):
        self.__cliente = cliente
    def setFecha(self, fecha):
        self.__fecha = fecha

    def getCesta(self):
        return self.__cesta
    def getCliente(self):
        return self.__cliente
    def getFecha(self):
        return self.__fecha

    def eliminarProducto(self, producto):
        #for p, c in self.__cesta:
        #    if p != producto:
        #        self.__cesta = (p, c)

        self.__cesta = [(p, c) for p, c in self.__cesta if p != producto]

    def añadirProducto(self, producto, cantidad):
        if producto.anadirPedido(cantidad):
            self.__cesta.append((producto, cantidad))
            return True
        return False

    def calcularPrecioTotal(self):
        total = 0
        for producto, cantidad in self.__cesta:
            total += producto.getPrecio() * cantidad
        return total

    def calcularIVA(self):
        return self.calcularPrecioTotal() * (21 / 100)

    def mostrarCesta(self):
        print("----- CESTA DEL PEDIDO -----")
        for producto, cantidad in self.__cesta:
            print(f"{producto.getNombre()} x{cantidad} -> {producto.getPrecio()} €/ud")
        print("-----------------------------")
        print(f"Total sin IVA: {self.calcularPrecioTotal()} €")
        print(f"IVA: {self.calcularIVA():.2f} €")
        print(f"Total con IVA: {self.calcularPrecioTotal() + self.calcularIVA():.2f} €")
        print()






producto1 = Producto("Leche", 3, 7)
producto2 = Producto("Pan", 1, 12)
producto3 = Producto("Huevos", 2, 14)
cliente1 = Cliente("Pepe", "pepe@gmail.com", "Su casa", 12345)
pedido1 = Pedido([], cliente1, "11/12/13")
pedido2 = Pedido([], cliente1, "11/12/17")

pedido1.añadirProducto(producto1, 5)
pedido1.añadirProducto(producto2, 3)
pedido1.añadirProducto(producto3, 12)
pedido1.añadirProducto(producto1, 1)
pedido1.mostrarCesta()

#pedido2.añadirProducto(producto3, 2)
#pedido2.añadirProducto(producto2, 1)
#pedido2.mostrarCesta()