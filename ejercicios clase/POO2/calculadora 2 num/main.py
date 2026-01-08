from calculadora import Calculadora

calculo1 = Calculadora("1", "2", "+")
print(calculo1.calcular())
calculo2 = Calculadora("1", "2", "-")
print(calculo2.calcular())
calculo3 = Calculadora("1", "2", "*")
print(calculo3.calcular())
calculo4 = Calculadora("1", "0", "/")
print(calculo4.calcular())