class Data:
    def __init__(self, day, month, year):
        self.setDia(day)
        self.setMes(month)
        self.setAno(year)

    def setDia(self, day):
        diasmes = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

    def getDia(self):
        return self.__day

    def setMes(self, month):
        if month>0 and month<13 and self.__ano is not None:
            self.__month = month
        else:
            self.__month = None

    def getMes(self):
        return self.__month

    def setAno(self, year):
        if year >= 0:
            self.__year

    def getAno(self):
        return self.__year

    def esValido(self):

        diasmes = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        if self.__day > 31 or self.__month > 12:
            valido = False
        else:
            if self.__year % 4 != 0 and self.__day > diasmes[self.__month]:
                valido = False
            else:
                diasmes[2] = 29
                if self.__day > diasmes[self.__month]:
                    valido = False
                else:
                    valido = True

        if valido == True:
            return "La fecha es: \n\t Dia: " + str(self.__day) + " \n\t Mes: " + str(self.__month) + " \n\t Año: " + str(self.__year)
        else:
            return "La fecha es: \n\t Dia: 1 \n\t Mes: 1 \n\t Año: 1970"