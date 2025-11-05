# 14 Escribir unha función que reciba unha cadea que conten un número entero longo e devolte unha cadea co número e as separacións de miles.
#    Por exemplo, se recibe 1234567890, debe devoltar 1.234.567.890

numero = 1234567890

def punto_cada_tres(numero):
    numero = str(numero)
    numero = numero[::-1]
    sol = ""
    i = 0
    for n in numero:
        if i % 3 == 0:
            sol += "."
            sol += n
        else:
            sol += n
        i += 1
    sol = sol[::-1]

    return sol[:-1]

print(punto_cada_tres(numero))