#3. Temos a seguinte clase Coche:
#class Coche:
#def __init__(self):
#self.velocidade =0
#
#
#Engade a clase Coche os seguintes métodos:
#getVelocidade() . Este método devolve a velocidade actual
#acelerar (valor). Este método incrementa a velocidade na cantidade valor.
#frenar (menos). Este método diminue a velocidade na cantidade menos.
#Crea unha clase Boletin 9_3 para comprobar que o programa execútase ben, dandolle os valores que precises.

class Coche:
    def __init__(self):
        self.velocidade = 0

    def getVelocidade(self):
        return self.velocidade
    
    def acelerar(self, valor):
        self.velocidade += valor
    
    def frenar(self, menos):
        self.velocidade -= menos


car1 = Coche()
car1.acelerar(3)
print(car1.getVelocidade())