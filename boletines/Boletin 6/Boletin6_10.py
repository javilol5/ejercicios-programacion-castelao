# 10 Escribir un programa que almacene as matrices
#
#a =	 (1,2,3)  				b = 	(-1,0)
#   	 	(4,5,6)					(0,1)
#								(1,1)
#nunha lista e mostre por pantalla o seu produto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila nunha tupla

a = [(1,2,3),(4,5,6)]
b = [(-1,0),(0,1),(1,1)]

sol = []
for f in a:
    resultado = []
    for j in range(len(b[0])):
        suma = 0
        for i in range(len(f)):
            suma += f[i]*b[i][j]
        resultado.append(suma)
    sol.append(tuple(resultado))

print("El producto de A y B es:", sol)
