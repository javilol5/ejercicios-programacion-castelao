class Deportista:
    def __init__(self, deporte:str, clube:str, licencia:int):
        self.setDeporte(deporte)
        self.setClube(clube)
        self.setLicencia(licencia)

    def setDeporte(self, deporte:str):
        self.deporte = deporte
    def setClube(self, clube:str):
        self.clube = clube
    def setLicencia(self, licencia: str):
        ano_actual = 2026

        if len(licencia) != 13:
            raise ValueError("A licenza debe ter 13 caracteres")

        ano = licencia[:4]
        deporte = licencia[4:7]
        numero = licencia[7:]

        if not ano.isdigit() or int(ano) != ano_actual:
            raise ValueError("Ano da licenza incorrecto")

        if not deporte.isalpha():
            raise ValueError("Abreviatura do deporte incorrecta")

        if not numero.isdigit():
            raise ValueError("Número de licenza incorrecto")

        self.licencia = licencia

    def getDeporte(self):
        return self.deporte
    def getClube(self):
        return self.clube
    def getLicencia(self):
        return self.licencia
