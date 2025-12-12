from datetime import datetime

#1
#Clase que modele a unha persoa. Os datos que se queren manexar son o nome, o dni e a idade. Codificar o metodo que permita comparar dous obxectos desta clase, e que retornen un booleano indicando si son iguais ou distintos, si o seu dni e igual ou non.
class Persona:
    def __init__(self, nombre, dni, idade):
        self.__nombre = nombre
        self.__dni = dni
        self.__idade = idade

    def setNombre(self, nombre):
        self.__nombre = nombre
    def setDni(self, dni):
        self.__dni = dni
    def setIdade(self, idade):
        self.__idade = idade

    def getNombre(self):
        return self.__nombre
    def getDni(self):
        return self.__dni
    def getIdade(self):
        return self.__idade

    def validarDni(self):
        tabla = [
            "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C",
            "K", "E"
        ]
        if len(self.__dni) == 9:
            dninum = int(self.__dni[0:-1])
            dnilet = self.__dni[-1]

            numtabla = dninum % 23
            if dnilet == tabla[numtabla]:
                return True

    def compararPersona(self, persona_comparar):
        if self.getNombre() == persona_comparar.getNombre() and self.getIdade() == persona_comparar.getIdade() and self.getDni() == persona_comparar.getDni():  #comparo todos los datos de persona1 y persona2 para ver si son tods iguales
            return True

    def compararDNI(self, persona_comparar):
        if self.getDni() == persona_comparar.getDni():
            return True

    def __str__(self):
        return f"{self.__nombre}:{self.__dni}:{self.__idade}"
'''
persona1 = Persona("Pepe", "12345678Z", 18)
persona2 = Persona("Maria", "12345678Z", 19)
persona3 = Persona("Juan", "12345679S", 20)
persona4 = Persona("Pepe", "12345678Z", 18)

print(persona1.compararPersona(persona4))
print(persona2.compararDni(persona1))
print(persona3.compararPersona(persona2))
print(persona4.compararDni(persona3))
'''
#2
#Clase que modele a un empleado. Os datos que ten que rexistrar esta clase e o nome, dni, idade, empresa, NUSS (numnero seguridad social). A clase non admitira NUSS mal formados, e asignara o NUSS '00/00000000/00' en caso de erro. O formato correcto do NUSS e o que segue: 'nn/nnnnnnnn/nn, onde n e un dixito de 0 a 9
class Empleado:
    def __init__(self, nombre, dni, idade, empresa, nuss):
        self.__nombre = nombre
        self.__dni = dni
        self.__idade = idade
        self.__empresa = empresa
        self.__nuss = nuss

    def setNombre(self, nombre):
        self.__nombre = nombre
    def setDni(self, dni):
        self.__dni = dni
    def setIdade(self, idade):
        self.__idade = idade
    def setEmpresa(self, empresa):
        self.__empresa = empresa
    def setNuss(self, nuss):
        self.__nuss = nuss

    def getNombre(self):
        return self.__nombre
    def getDni(self):
        return self.__dni
    def getIdade(self):
        return self.__idade
    def getEmpresa(self):
        return self.__empresa
    def getNuss(self):
        return self.__nuss

    def validarNus(self):
        if len(self.__nuss) == 14:
            if self.__nuss[2] == "/" and self.__nuss[11] == "/":
                numnuss = self.__nuss.replace("/", "")
                numvalidos = 0
                for num in numnuss:
                    if num.isdigit():
                        numvalidos += 1
                if numvalidos == 12:
                    return True
                else:
                    self.__nuss = "00/00000000/00"
        else:
            self.__nuss = "00/00000000/00"

    def __str__(self):
        return f"{self.__nombre}:{self.__dni}:{self.__idade}:{self.__empresa}:{self.__nuss}"


'''
empleado1 = Empleado("Juan", "12345678Z", 18, "Froiz", "0p/12345678/90")

print(empleado1.validarNus())
print(empleado1.getNuss())
'''
#3
#Clase que modele unha xornada laboral. Precisase identificar un empleado, datahoraentrada e datahorasaida para definir a xornada laboral. Para rexistrar a data de entrada e saida utilizar a clase datime. Ademais dos metodos para asignar as propiedades, codificar un metodo que retorne os minutos de traballo que durou a xornada


class Xornada:
    def __init__(self, empleado, datahoraentrada, datahorasaida):
        self.__empleado = empleado
        self.__datahoraentrada = datahoraentrada
        self.__datahorasaida = datahorasaida
        
    def setEmpleado(self, empleado):
        self.__empleado = empleado
    def setHoraEntada(self, datahoraentrada: datetime):
        self.__datahoraentrada = datahoraentrada
    def setHoraSaida(self, datahorasaida: datetime):
        self.__datahorasaida = datahorasaida
        
    def getEmpleado(self):
        return self.__empleado
    def getHoraEntrada(self):
        return self.__datahoraentrada
    def getHoraSaida(self):
        return self.__datahorasaida
    
    def duracionMinutos(self):
        if self.__datahoraentrada is None or self.__datahorasaida is None:
            return 0
        else:
            duracion = self.__datahorasaida - self.__datahoraentrada
            return int(duracion.total_seconds() // 60)


    def __str__(self):
        return f"{self.__empleado}:{self.__datahoraentrada}:{self.__datahorasaida}"



'''
xornada1 = Xornada("Juan",datetime(2025,12,12,8,30), datetime(2025, 12, 12,10,20))
print(xornada1.duracionMinutos())
xornada2 = Xornada("Maria",datetime(2025,12,12,8,30), datetime(2026, 5, 14,21,33))
print(xornada2.duracionMinutos())
'''
#4
#Clase que manexe as xornadas laborais de distintos empleados, A clase tera como popiedade unah lista coas xornadas laborais dos distintos traballadores. O iniciarse creara a lista baleira. Tera un metodo para engadir a xornada (obxecto) dun dia de traballo dun traballador. Se definira un segundo metodo, onde cando se lle pase por parametro un DNI dun traballador, devolvera a suma de todo o tempo en horas, das suas xornadas laborais (pode haber varias en distintos dias)

class XornadaLaboral:
    def __init__(self, dni):
        self.__dni = dni
        self.__xornada = []

    def setDni(self, dni):
        self.__dni = dni

    def getDni(self):
        return self.__dni
    def getXornada(self):
        return self.__xornada

    def engadirXornada(self, dni, entrada:datetime, saida:datetime):

        if saida < entrada:
            print("entrada no puede ser mayor que salida")
        self.__xornada.append((dni, entrada, saida))

    def horasTraballadas(self, dni):
        minutos = 0
        for self.__dni, entrada, saida in self.__xornada:
            if self.__dni == dni:
                duracion = saida - entrada
                minutos += int(duracion.total_seconds() // 60)
        return minutos / 60.0

    def __str__(self):
        return f"{self.__dni}:{self.__xornada}"

'''
xornadalaboral1 = XornadaLaboral("12345678Z")
xornadalaboral2 = XornadaLaboral("12345679S")
print(xornadalaboral1.getDni())
xornadalaboral1.engadirXornada("12345678Z",datetime(2025, 12, 12, 8, 30), datetime(2025, 12, 12, 10, 20))
print(xornadalaboral1.horasTraballadas("12345678Z"))
'''

