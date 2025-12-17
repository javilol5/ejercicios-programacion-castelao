from datetime import datetime

class Persona:
    def __init__(self, nombre, dni, nuss, tel, xornadaini, xornadafin):
        self._nombre = nombre
        self._dni = dni
        self._nuss = nuss
        self._tel = tel
        self._xornadaini = xornadaini
        self._xornadafin = xornadafin

    def setNombre(self, nombre):
        self._nombre = nombre
    def setDni(self, dni):
        self._dni = dni
    def setNuss(self, nuss):
        self._nuss = nuss
    def setTel(self, tel):
        self._tel = tel
    def setXornadaini(self, xornadaini):
        self._xornadaini = xornadaini
    def setXornadafin(self, xornadafin):
        self._xornadafin = xornadafin

    def getNombre(self):
        return self._nombre
    def getDni(self):
        return self._dni
    def getNuss(self):
        return self._nuss
    def getTel(self):
        return self._tel
    def getXornadaini(self):
        return self._xornadaini
    def getXornadafin(self):
        return self._xornadafin

    def validarNuss(self):
        if len(self._nuss) == 14:
            if self._nuss[2] == "/" and self._nuss[11] == "/":
                numnuss = self._nuss.replace("/", "")
                numvalidos = 0
                for num in numnuss:
                    if num.isdigit():
                        numvalidos += 1
                if numvalidos == 12:
                    return True
                else:
                    self._nuss = "00/00000000/00"
        else:
            self._nuss = "00/00000000/00"


    def telefonoValido(self):
        if len(self._tel) != 15:
            return False
        if self._tel[0] != "+" or self._tel[3] != " " or self._tel[7] != " " or self._tel[11] != " ":
            return False
        num_telefono = self._tel[1:14].replace(" ", "")
        for num in num_telefono:
            if not num.isdigit():
                return False
        return True

    def duracionXornada(self):
        if self._xornadaini is None or self._xornadafin is None:
            return 0
        else:
            duracion = self._xornadafin - self._xornadaini
            return int(duracion.total_seconds() // 60)

    def __eq__(self, otro):
        if not isinstance(otro, Persona):
            return False
        return self._dni == otro._dni


#propiedades ocuiltas self._nombre
#usar __eq__
#comrpobar nuss
#comprobar num tel
#calcualr minutos xornada        datetime
#xornada laboral