# 12 Escribir funcións que dada unha cadea e un caracter:
#  a) Reemplace tódolos espazos polo caracter. Ex: ‘meu arquivo de texto.txt’ e ‘\_’ debería devoltar ‘meu\_arquivo\_de\_texto.txt’
#  b) Inserte o caracter entre cada letra da cadea. Ex: ‘separar’ e ‘,’ debería devolver s,e,p,a,r,a,r
#  c) Reemplace tódolos díxitos na cadea polo caracter. Ex: súa clave é: 1540 e ‘X’ debería devotar súa clave é: XXXX
#  d) Inserte o caracter cada 3 díxitos na cadea. Ex. 2552552550 e ‘.’ debería devoltar 255.255.255.0

texto = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
caracter = "@3#"
def reemplazar_espacios(texto,caracter):
    texto = texto.replace(" ",caracter)
    return texto

def insertar_entre_caracter(texto,caracter):
    sol = ""
    for char in texto:
        sol += char
        sol += caracter
    return sol[:-1]

def reemplazar_caracter(texto,caracter):
    sol = ""
    for char in texto:
        sol += caracter
    return sol

def insertar_cada_tres(texto,caracter):
    sol = ""
    i = 1
    for char in texto:
        if i % 3 == 0:
            sol += char
            sol += caracter
        else:
            sol += char
        i += 1
    return sol

print(reemplazar_espacios(texto,caracter))
print(insertar_entre_caracter(texto,caracter))
print(reemplazar_caracter(texto,caracter))
print(insertar_cada_tres(texto,caracter))