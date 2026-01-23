class Data:
    def __init__(self, day, month, year):
        self.__year = None
        self.__month = None
        self.__day = None

        self.setAno(year)
        self.setMes(month)
        self.setDia(day)

    def setDia(self, day):
        if self.__year is None or self.__month is None:
            self.__day = None
            return

        diasmes = {
            1: 31,
            2: 29 if self.eBisiesto(self.__year) else 28,
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

        if 1 <= day <= diasmes[self.__month]:
            self.__day = day
        else:
            self.__day = None




    def getDia(self):
        return self.__day

    def setMes(self, month):
        if self.__year is not None and 1 <= month <= 12:
            self.__month = month
        else:
            self.__month = None

    def getMes(self):
        return self.__month

    def setAno(self, year):
        if year >= 0:
            self.__year = year
        else:
            self.__year = None

    def getAno(self):
        return self.__year

    def eBisiesto(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def __str__(self):
        if self.__day is None or self.__month is None or self.__year is None:
            return "Data inválida"
        return f"A data é {self.__day}/{self.__month}/{self.__year}"
