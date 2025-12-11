# 4. Escribe unha clase Conta para representar unha conta bancaria. Os datos da conta son:
# Atributos : 
# Nome do cliente. 
# Número de conta.
# Tipo de interese.
# Saldo.

# A clase conterá os seguintes métodos:
# Método inicializador.
# Métodos setters/ getters para asignar e obter os datos da conta.
# Establecer as propiedades de forma que só se poida acceder os atributos mediante os métodos adicados a elo (geters e seters).
# Métodos de ingreso. Un ingreso consiste en aumentar o saldo na cantidade que se indique. 
# Métodos de reintegro. Un reintegro consiste en diminuír o saldo nunha cantidade. A cantidade non pode ser negativa. 
# Método transferencia que permita pasar diñeiro dunha conta a outra Exemplo de uso do método transferencia:
#  contaOrigen.transferencia( contaDestino, importe),  que indica que queremos facer unha transferencia desde contaOrigen a contaDestino do importe indicado.
# Proba o funcionamento da clase Conta na clase principal.

class Conta:
    def __init__(self, nombre, ncuenta, interes, saldo):
        self.__nombre = nombre
        self.__ncuenta = ncuenta
        self.__interes = interes
        self.__saldo = saldo
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setNCuenta(self, ncuenta):
        self.__ncuenta = ncuenta
    def setInteres(self, interes):
        self.__interes = interes
    def setSaldo(self, saldo):
        self.__saldo = saldo
    
    def getNombre(self):
        return self.__nombre
    def getNCuenta(self):
        return self.__ncuenta
    def getInteres(self):
        return self.__interes
    def getSaldo(self):
        return self.__saldo
    

    def ingreso(self, cantidade):
        self.__saldo += cantidade

    def reintegro(self, cantidade):
        if cantidade > 0:
            self.__saldo -= cantidade
    
    def transferencia(self, contaDestino, importe):
        if self.__saldo >= importe:
            if isinstance(contaDestino, Conta):
                self.__saldo -= importe
                contaDestino.ingreso(importe)



cuenta1 = Conta("a",1,1,100)
cuenta2 = Conta("b",2,2,1000)

cuenta1.ingreso(200)
print(cuenta1.getSaldo())
cuenta2.reintegro(300)
print(cuenta2.getSaldo())
cuenta2.transferencia(cuenta1,500)
print(cuenta1.getSaldo())
print(cuenta2.getSaldo())
