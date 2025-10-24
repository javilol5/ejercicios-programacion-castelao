# 13 Modificar as funcións anteriores,
#    para que reciban un parámetro que indique a cantidade máxima de reemplazos ou insercións a realizar.


texto = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
caracter = "@3#"

def reemplazar_espacios(texto, caracter, max_accions):
    sol = ""
    cont = 0
    for char in texto:
        if char == " " and cont < max_accions:
            sol += caracter
            cont += 1
        else:
            sol += char
    return sol


def insertar_entre_caracter(texto, caracter, max_accions):
    sol = ""
    cont = 0
    for i in range(len(texto)):
        sol += texto[i]
        if i < len(texto) - 1:
            if cont < max_accions:
                sol += caracter
                cont += 1
            else:
                sol += ""
    return sol


def reemplazar_caracter(texto, caracter, max_accions):
    sol = ""
    cont = 0
    for char in texto:
        if cont < max_accions:
            sol += caracter
            cont += 1
        else:
            sol += char
    return sol


def insertar_cada_tres(texto, caracter, max_accions):
    sol = ""
    cont = 0
    i = 1
    for char in texto:
        sol += char
        if i % 3 == 0 and i != len(texto) and cont < max_accions:
            sol += caracter
            cont += 1
        i += 1
    return sol

print(reemplazar_espacios(texto,caracter,3))
print(insertar_entre_caracter(texto,caracter,8))
print(reemplazar_caracter(texto,caracter,2))
print(insertar_cada_tres(texto,caracter,4))