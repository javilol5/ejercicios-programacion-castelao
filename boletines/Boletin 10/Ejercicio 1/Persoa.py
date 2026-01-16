class Persoa:
    def __init__(self, nombre:str, direccion:str, dni:str):
        self.setNome(nombre)
        self.setDireccion(direccion)
        self.setDni(dni)

    def setNome(self, nombre):
        self.nombre = nombre

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setDni(self, dni):
        tabla = [
            "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C",
            "K", "E"
        ]

        if len(dni) != 9:
            raise ValueError("DniNonValido")

        dninum = int(dni[:-1])
        dnilet = dni[-1].upper()

        if tabla[dninum % 23] != dnilet:
            raise ValueError("DNI incorrecto")

        self.dni = dni


    def getNome(self):
        return self.nombre
    def getDireccion(self):
        return self.direccion
    def getDni(self):
        return self.dni