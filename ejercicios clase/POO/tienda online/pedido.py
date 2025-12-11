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