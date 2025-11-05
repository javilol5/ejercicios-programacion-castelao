#  2 Escribir un programa que pregunte o usuario os números gañadores da lotería primitiva,
#  os almacene nunha lista e os muestre por pantalla ordenados de menor a maior.

primitiva = []
complemento = []
reintegro = []
n=1
for i in range(0,6):
    primitiva.append(int(input("Ingresa el numero " + str(n) + " de la primitiva: ")))
    n += 1
complemento.append(int(input("Ingresa el numero complemento: ")))
reintegro.append(int(input("Ingresa el numero reintegro: ")))
primitiva.sort()
print("P:", primitiva, "C:", complemento, "R:", reintegro)