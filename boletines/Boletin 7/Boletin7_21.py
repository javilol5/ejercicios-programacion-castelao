# 21 Escribe a función que permita validar un contasinal,
#    recibindo o contrasinal como parámetro.
#    O contrasinal ten que cumprir as condicións:
#    de mínimo 8 caracteres,
#    o menos unha maiúscula,
#    unha minúscula e un número.
#    A función ten que retornar un booleano especificando si é válida ou non.

contraseña = "Password1"

def validar_contraseña(contraseña):
    valido = False
    valido1 = False
    valido2 = False
    valido3 = False
    if len(contraseña) >= 8:
        valido = True
    for char in contraseña:
        if char.isupper():
            valido1 = True
        elif char.islower():
            valido2 = True
        elif char.isdigit():
            valido3 = True

    return valido and valido1 and valido2 and valido3

print(validar_contraseña(contraseña))