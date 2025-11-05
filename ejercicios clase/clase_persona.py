class Persona:
    def __init__(self, nombre, edad, dni, direccion, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.direccion = direccion
        self.nacionalidad = nacionalidad

    def aCadea(self):
        return (f"Nombre: {self.nombre}\n"
                f"Edad: {self.edad}\n"
                f"DNI: {self.dni}\n"
                f"Dirección: {self.direccion}\n"
                f"Nacionalidad: {self.nacionalidad}")

    def comprobarEdade(self, edad):
        if edad >= 120 or edad < 0:
            return "Edad invalida"
        else:
            return "Edad valida"

    def comprobarDni(self, dni):
        tabla = [
            "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"
        ]
        num_dni = dni[:-1]
        numletra = int(num_dni) % 23
        letra = tabla[numletra]

        if len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isalpha() and dni[-1] == letra:
            return f"DNI valido: {dni}\n"

p1 = Persona("Xoán López", 22, "12345678Z", "Rúa Nova 15, Santiago", "Galega")

print(p1.aCadea())
print(p1.comprobarEdade(p1.edad))
print(p1.comprobarDni(p1.dni))