from datetime import datetime

#1
#Clase que modele a unha persoa. Os datos que se queren manexar son o nome, o dni e a código postal (5 dixitos). Codificar o método que permita comparar dous obxectos desta clase, e que retornen un booleano indicando si son iguais ou distintos, si o seu dni e igual ou non

class Persoa:
    def __init__(self, nome, dni, codpostal):
        self.__nome = nome
        self.__dni = dni
        self.__codpostal = codpostal


    def getNome(self):
        return self.__nome
    
    def getDni(self):
        return self.__dni
    
    def getCodPostal(self):
        return self.__codpostal

    def setCodPostal(self, codpostal):
        if len(codpostal) != 5 or not codpostal.isdigit():
            self.__codpostal = "00000"
        else:
            self.__codpostal = codpostal

    def mesmaPersoa(self, outra_persoa) -> bool:
        if not isinstance(outra_persoa, Persoa):
            return False
        return self.__dni == outra_persoa.getDni()
'''
persona1 = Persoa("Ana López", "12345678A", "15001")
persona2 = Persoa("Carlos Gómez", "12345678A", "36204")
persona3 = Persoa("María Torres", "98765432B", "15004")

print(persona1.mesmaPersoa(persona2))
print(persona1.mesmaPersoa(persona3))
'''
#2
#Clase que modele a un cliente dunha compañía de telecomunicacións. Os datos que ten que rexistrar esta clase é nome, dni, código postal, teléfono do aboado. A clase non admitira números de teléfonos mal formados e asignará o número +00 000 000 000. Ο formato correcto do teléfono de aboado é o que segue: +nn nnn nnn nnn", onde n e un dixito de 0 a 9.

class Cliente:
    def __init__(self, nome: str, dni: str, codpostal: str, telefono: str):
        self.__nome = nome
        self.__dni = dni
        self.__codpostal = codpostal
        self.setTelefono(telefono)

    def getNome(self):
        return self.__nome
    def getDni(self):
        return self.__dni
    def getCodPostal(self):
        return self.__codpostal
    def getTelefono(self):
        return self.__telefono
    
    def __telefonoValido(self, telefono):
        if len(telefono) != 14:
            return False
        if telefono[0] != "+" or telefono[3] != " " or telefono[7] != " " or telefono[11] != " ":
            return False
        num_telefono = telefono[1:14].replace(" ", "")
        numero = 0
        for num in num_telefono:
            if num.isdigit():
                numero += 1
        if numero != 11:
            return False
        return True
        
    def setTelefono(self, telefono):
        if self.__telefonoValido(telefono):
            self.__telefono = telefono
        else:
            self.__telefono = "+00 000 000 000"
'''
cliente1 = Cliente("Ana López", "12345678A", "15001", "+34 654 789 321")
print(cliente1.getTelefono())

cliente2 = Cliente("Carlos Gómez", "54321678B", "36204", "123456789")
print(cliente2.getTelefono()) 
'''

#3
#Clase que modele a unha persoa. Os datos que se queren manexar son o nome, o dni e a idade. Codificar dous métodos que permitan comparar dous obxectos desta clase: un que compare se son a mesma persoa (se o seu dni é igual) e outro que compare a súa idade (se teñen a mesma idade), retornando un booleano en ambos casos.



class ChamadaTelefonica:
    def __init__(self, telefonocliente, telefonointerlocutor, saínte):
        self.__telefonocliente = telefonocliente
        self.__telefonointerlocutor = telefonointerlocutor
        self.__saínte = saínte
        self.__inicio = None
        self.__fin = None

    def getTelefonoCliente(self):
        return self.__telefonocliente
    def getTelefonoInterlocutor(self):
        return self.__telefonointerlocutor
    def getSaínte(self):
        return self.__saínte
    def getInicio(self):
        return self.__inicio
    def getFin(self):
        return self.__fin

    def setInicio(self, inicio: datetime):
        self.__inicio = inicio
    def setFin(self, fin: datetime):
        self.__fin = fin

    def minutosDuracion(self):
        if self.__inicio is None or self.__fin is None:
            print("Datos invalidos")
        duracion = self.__fin - self.__inicio
        return duracion.total_seconds() / 60

'''
chamada = ChamadaTelefonica("634567890", "612345678", True)

chamada.setInicio(datetime(2025, 12, 12, 9, 0))
chamada.setFin(datetime(2025, 12, 12, 9, 45))

print(chamada.minutosDuracion(), "minutos")
'''

#4
#Clase que manexe as chamadas telefónicas de distintos aboados. A clase terá como propiedade unha lista cos obxectos que rexistran chamadas de distintos clientes. O iniciarse creará a lista baleira. Terá dous métodos: Un para engadir a chamada (obxecto) dun usuario. Outro onde cando se lle pase por parámetro un DNI dun usuario, devolverá o importe total das chamadas saíntes. Isto se calculará como resultado de multiplicar o custe do minuto (0.2 cent€/min) por todo o tempo das chamadas telefónicas do cliente (pode haber varias en distintos días). Importe = 0,0002*minutos

class XestorChamadas:
    def __init__(self):
        self.__chamadas = []

    def engadirChamada(self, chamada):
        self.__chamadas.append(chamada)

    def importeChamadas(self, telefonocliente)
        total_minutos = 0
        for chamada in self.__chamadas:
            if chamada.getSaínte() and chamada.getTelefonoCliente() == telefonocliente:
                total_minutos += chamada.minutosDuracion()
        importe = 0.0002 * total_minutos
        return importe