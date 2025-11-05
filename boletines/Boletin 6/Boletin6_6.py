#  6 Escribir un programa que pida o usuario unha palabra e mostre por pantalla si é un palíndromo.

palabra = str(input("Ingrese la palabra: "))
#palabraR = palabra[::-1]
if palabra == palabra[::-1]:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")