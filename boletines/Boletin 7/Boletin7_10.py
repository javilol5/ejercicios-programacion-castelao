#  10 Tenta escribir un método,
#     que dado un obxecto da clase str conte diferentes tipos de caracteres.
#     En particular, o método deberá imprimir o número de letras,
#     díxitos e espazos en branco da cadea.
#     Tenta facer un programa que escriba o cálculo da cadea:
#     «Ola, son alumno de DAM1, e son programador desde o 2025».

string = "Ola, son alumno de DAM1, e son programador desde o 2025"

string = string.lower()

vocales = 0
consonantes = 0
espacios = 0
numeros = 0
caracteres = 0

lasvocales = "aeiou"
lasconsonantes = "bcdfghjklmnpqrstvwxyz"
lasespacios = " "
lasnumeros = "0123456789"

for char in string:
    if char in lasvocales:
        vocales += 1
    elif char in lasconsonantes:
        consonantes += 1
    elif char in lasespacios:
        espacios += 1
    elif char in lasnumeros:
        numeros += 1
    else:
        caracteres += 1
print("Vocales:",vocales)
print("Consonantes:",consonantes)
print("Espacios:",espacios)
print("Numeros:",numeros)
print("Caracteres especiales:",caracteres)


