#  5 Conta as vocais e as consoantes do String “Python Python Python”. Ollo cos espazos!

string = "Python Python Python"

string = string.lower()

vocales = 0
consonantes = 0
espacios = 0
caracteres = 0

lasvocales = "aeiou"
lasconsonantes = "bcdfghjklmnpqrstvwxyz"
lasespacios = " "

for char in string:
    if char in lasvocales:
        vocales += 1
    elif char in lasconsonantes:
        consonantes += 1
    elif char in lasespacios:
        espacios += 1
    else:
        caracteres += 1
print("Vocales:",vocales)
print("Consonantes:",consonantes)
print("Espacios:",espacios)
print("Caracteres especiales:",caracteres)

