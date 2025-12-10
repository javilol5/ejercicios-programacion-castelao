#2. Implementa unha clase consumo, que forma parte da centralita electrónica dun coche e ten as seguintes características :
#Atributos :
#km kilómetros percorridos polo coche
#litros Litros de combustible consumidos
#vMed velocidade media
#pGas Prezo da gasolina
#
#Metodos :
#Un metodo que inicializa os valores dos atributos
#getTempo Indica o tempo empregado en realizar a viaxe
#consumoMedio consumo medio do vehículo (en litros cada 100 km )
#consumoEuros consumo medio (en € cada 100 km )
#setKms modifica o valor dos km
#setLitros actualiza a cantidade de litros
#setvMed actualiza o valor da vMed
#setPGas actualiza o valor do pGas
#Na clase principal :
#Crea un obxecto, de tipo consumo.
#Dalle a litros o valor 50 e a prezo da gasolina 1.57
#Crea un obxecto, tipo consumo, utilizando o constructor con tódolos parámetros
#Visualiza, a través do 2º obxecto, o consumo medio
#Varia o valor dos litros consumidos do 2º obxecto.
#Visualiza a velocidade media do 2º obxecto


class Consumo:
    def __init__(self, km, litros, vmed, pgas):
        self.km = km
        self.litros = litros
        self.vmed = vmed
        self.pgas = pgas

    def setKm(self, km):
        self.km = km
    def setLitros(self, litros):
        self.litros = litros
    def setVmed(self, vmed):
        self.vmed = vmed
    def setPgas(self, pgas):
        self.pgas = pgas

    def getKm(self):
        return self.km
    def getLitros(self):
        return self.litros
    def getVmed(self):
        return self.vmed
    def getPgas(self):
        return self.pgas

