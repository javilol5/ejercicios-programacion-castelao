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