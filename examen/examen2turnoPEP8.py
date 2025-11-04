#1
#
#def verificar_contrasena(lista_usuarios):
#    nombre = str(input("Ingresa tu nombre: "))
#    contrasena = str(input("Ingresa tu contraseña: "))
#    for usuario in lista_usuarios:
#        return nombre == usuario[0] and contrasena == usuario[1]
#
#test1 = [["nome1", "contrasinal1"], ["nome2", "contrasinal2"]]
#print(verificar_contrasena(test1))

#2
#
#def contar_caracteres(contrasena):
#    return len(contrasinal) > 8
#
#test1 = "1234abcd"
#test2 = "1234"
#test3 = "1234567890"
#print(contar_caracteres(test1))
#print(contar_caracteres(test2))
#print(contar_caracteres(test3))

#3
#
#def verificar_mayusculas(contrasena):
#    tiene_mayuscula = False
#    for caracter in contrasena:
#        if caracter == caracter.upper():
#            tiene_mayuscula = True
#
#    return tiene_mayuscula
#
#test1 = "abcd"
#test2 = "Abcd"
#test3 = "aBcD"
#print(verificar_mayusculas(test1))
#print(verificar_mayusculas(test2))
#print(verificar_mayusculas(test3))


#4
#
#def verificar_numero(contrasena):
#    tiene_numero = False
#    for caracter in contrasena:
#        if caracter.isdigit():
#            tiene_numero = True
#
#    return tiene_numero
#
#test1 = "abcd1"
#test2 = "A2cd"
#test3 = "aBcd"
#test4 = "a1b2"
#print(verificar_numero(test1))
#print(verificar_numero(test2))
#print(verificar_numero(test3))
#print(verificar_numero(test4))


#5

#def verificar_caracter_especial(contrasena):
#    caracteres_especiales = "!@#$%&*_."
#    tiene_caracter = False
#    for caracter in contrasena:
#        if caracter in caracteres_especiales:
#            tiene_caracter = True
#
#    return tiene_caracter
#
#test1 = "abcd1"
#test2 = "A2!d"
#test3 = "#Bcd"
#test4 = "a1%&"
#print(verificar_caracter_especial(test1))
#print(verificar_caracter_especial(test2))
#print(verificar_caracter_especial(test3))
#print(verificar_caracter_especial(test4))


#6
"""
def contrasena_valida():
    nombre = str(input("Ingresa tu nombre: "))
    contrasena = str(input("Ingresa tu contraseña: "))
    datos_usuario = [nombre, contrasena]
    usuarios = []
    caracteres_especiales = ["!","@","#","$","%","&","*","_","."]
    es_valida = False
    tiene_digito = False
    tiene_mayuscula = False
    tiene_caracter_especial = False
    while not es_valida and contrasena != "":
        if len(contrasena) >= 8:
            for caracter in contrasena:
                if caracter.isdigit():
                    tiene_digito = True
                elif caracter in caracteres_especiales:
                    tiene_caracter_especial = True
                elif caracter == caracter.upper() and not caracter.isdigit():
                    tiene_mayuscula = True
            es_valida = tiene_digito and tiene_caracter_especial and tiene_mayuscula
        else:
            print(False)
            print("Contraseña inválida")
            print("Numero:", tiene_digito)
            print("Caracteres:", tiene_caracter_especial)
            print("Mayus:", tiene_mayuscula)
            contrasena = str(input("Ingresa tu contraseña: "))

    usuarios.append(datos_usuario)
    return True

print(contrasena_valida())"""