# 15 Escribir unha función que dada unha cadea de caracteres, devolte:
#  a) A primeira letra de cada palabra. Por exemplo, 	si recibe Universal Serial Bus debe devoltar USB.
#  b) Unha cadea coa primeira letra de cada palabra en maiúsculas. Por exemplo, se recibe república arxentina, debe devoltar, República Argentina.
#  c) As palabras que comecen coa letra A. Por exemplo, si recibe Antes de abrir, debe devoltar, Antes abrir.

cadena = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"

def primera_letra_cada_palabra(cadena):
    cadena = cadena.split()
    sol = ""
    for palabra in cadena:
        sol += palabra[0]

    return sol

def primera_letra_cada_palabra_mayus(cadena):
    cadena = cadena.split()
    sol = ""
    for palabra in cadena:
        sol += palabra[0].upper()

    return sol

def palabras_empiezan_por_i(cadena):
    inicio = "iI"
    cadena = cadena.split()
    sol = ""
    for palabra in cadena:
        if palabra[0] in inicio:
            sol += palabra
            sol += " "
    return sol[:-1]

print(primera_letra_cada_palabra(cadena))
print(primera_letra_cada_palabra_mayus(cadena))
print(palabras_empiezan_por_i(cadena))