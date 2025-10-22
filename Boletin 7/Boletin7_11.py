# 11 Escribir funcións que dada unha cadena de caracteres:
#  a) Imprima os dous primeiros caracteres.
#  b) Imprima os tres últimos caracteres.
#  c) Imprima dita cadea cada dous caracteres.Ex.: recta debería imprimir rca
#  d) Imprima a cadea nun sentido e en sentido inverso.Ex: reflexo imprime reflexooxelfer.

palabra = "Palabra"

def dos_primeros(palabra):
    return palabra[:2]

def tres_ultimos(palabra):
    return palabra[-2:]

def cada_dos(palabra):
    sol = ""
    i = 1
    for char in palabra:
        if i % 2 != 0:
            sol += char
        i += 1
    return sol

def normal_inverso(palabra):
    return palabra + palabra[::-1]



print(dos_primeros(palabra))
print(tres_ultimos(palabra))
print(cada_dos(palabra))
print(normal_inverso(palabra))