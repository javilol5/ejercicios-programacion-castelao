#  7 Escribir un programa que pida o usuario unha palabra e mostre por pantalla o número de veces que conten cada vogal.

palabra = str(input("Ingresa una palabra: "))

a = 0
e = 0
i = 0
o = 0
u = 0

for l in palabra:
    if l == "a":
        a += 1
    elif l == "e":
        e += 1
    elif l == "i":
        i += 1
    elif l == "o":
        o += 1
    elif l == "u":
        u += 1
print(palabra , "tiene" , a , "a," , e , "e, " , i , "i, " , o , "o, " , u , "u")