class Calculadora:

    def __init__(self, num1, num2, operador):
        self.__setNum1(num1)
        self.__setNum2(num2)
        self.__setOperador(operador)

    def __setNum1(self, num1):
        if num1.isdigit():
            self.__num1 = float(num1)
        else:
            raise ValueError("Numero o operador invalido")

    def __setNum2(self, num2):
        if num2.isdigit():
            self.__num2 = float(num2)
        else:
            raise ValueError("Numero o operador invalido")

    def __setOperador(self, operador):
        if operador in ("/", "*", "-", "+"):
            self.__operador = operador
        else:
            raise ValueError("Numero o operador invalido")


    def getNum1(self):
        return self.__num1
    def getNum2(self):
        return self.__num2
    def getOperador(self):
        return self.__operador

    def calcular(self):
        match self.__operador:
            case "+":
                return self.__num1 + self.__num2
            case "-":
                return self.__num1 - self.__num2
            case "*":
                return self.__num1 * self.__num2
            case "/":
                if self.__num2 != 0:
                    return self.__num1 / self.__num2
                else:
                    division0 = r"""
                                         _.-^^---....,,--
                                     _--                  --_
                                    <                        >)
                                    |                         |
                                     \._                   _./
                                        ```--. . , ; .--'''
                                              | |   |
                                           .-=||  | |=-.
                                           `-=#$%&%$#=-'
                                              | ;  :|
                                     _____.,-#%&$@%#~,._____
                                     NO SE PUEDE DIVIDIR POR 0
                                    """

                    return division0
            case _:
                raise ValueError("Operador no válido")








'''
        #Manuel#
class CalculadoraBinaria:
    def __init__(self, a, b, op):


    def set_a(self, a):
        self.__a = a
    def set_b(self, b):
        self.__b = b

    def operacion(self, op):
        if op == "+":
            return self.__a + self.__b
        elif op == "-":
            return self.__a - self.__b
        elif op == "*":
            return self.__a * self.__b
        elif op == "/":
            return self.__a / self.__b



    


    if __name__=='main':
        c1 = CalculadoraBinaria(2, 3)
        c1.a = 1
        c1.set_a(100)
        c1.__a = 11
        print ( c1.operacion('+'))





'''