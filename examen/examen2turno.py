#1
#
#def contraseña(nombres):
#    nom = str(input("Ingresa tu nombre: "))
#    cont = str(input("Ingresa tu contraseña: "))
#    for nombre in nombres:
#        return nom == nombre[0] and cont == nombre[1]
#
#t1 = [["nome1", "contrasinal1"], ["nome2", "contrasinal2"]]
#print(contraseña(t1))

#2
#
#def contar_caracteres(contrasianal):
#    return len(contrasinal) > 8
#
#t1 = "1234abcd"
#t2 = "1234"
#t3 = "1234567890"
#print(contar_caracteres(t1))
#print(contar_caracteres(t2))
#print(contar_caracteres(t3))

#3
#
#def ver_mayusculas(contrasinal):
#    valido = False
#    for char in contrasinal:
#        if char == char.upper():
#            valido = True
#
#    return valido
#
#t1 = "abcd"
#t2 = "Abcd"
#t3 = "aBcD"
#print(ver_mayusculas(t1))
#print(ver_mayusculas(t2))
#print(ver_mayusculas(t3))


#4
#
#def ver_numero(contrasinal):
#    valido = False
#    for char in contrasinal:
#        if char.isdigit():
#            valido = True
#
#    return valido
#
#t1 = "abcd1"
#t2 = "A2cd"
#t3 = "aBcd"
#t4 = "a1b2"
#print(ver_numero(t1))
#print(ver_numero(t2))
#print(ver_numero(t3))
#print(ver_numero(t4))


#5

#def ver_caracter(contrasinal):
#    caracter_especial = "!@#$%&*_."
#    valido = False
#    for char in contrasinal:
#        if char in caracter_especial:
#            valido = True
#
#    return valido
#
#t1 = "abcd1"
#t2 = "A2!d"
#t3 = "#Bcd"
#t4 = "a1%&"
#print(ver_caracter(t1))
#print(ver_caracter(t2))
#print(ver_caracter(t3))
#print(ver_caracter(t4))


#6

def contraseña_valida():
    nom = str(input("Ingresa tu nombre: "))
    cont = str(input("Ingresa tu contraseña: "))
    nome_cont = [nom, cont]
    nome_contrasinal = []
    caracteres = ["!","@","#","$","%","&","*","_","."]
    valido = False
    digit = False
    mayus = False
    carac = False
    while valido == False and cont != "":
        if len(cont) >= 8:
            for char in cont:
                if char.isdigit():
                    digit = True
                elif char in caracteres:
                    carac = True
                elif char == char.upper():
                    mayus = True
            valido = (digit and carac and mayus)
        else:
            print(False)
            print("Contraseña invalida")
            print("Numero:", digit)
            print("Caracteres:", carac)
            print("Mayus:", mayus)
            cont = str(input("Ingresa tu contraseña: "))

    nome_contrasinal.append(nome_cont)
    return True

print(contraseña_valida())
