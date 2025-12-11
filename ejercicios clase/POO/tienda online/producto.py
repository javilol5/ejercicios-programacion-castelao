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