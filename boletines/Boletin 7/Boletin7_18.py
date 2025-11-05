# 18 Escribir funcións que dadas dúas cadeas de caracteres:
#  a) Indique si a segunda cadea é unha subcadea da primeira. Por exemplo, ‘cadea’ é unha subcadea de ‘subcadea’.
#  b) Devolva a que sexa anterior en orden alfábetico. Por exemplo, se recibe ‘kde' e ‘gnome’ debe devoltar ‘gnome’.

cadena1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
cadena2 = "dummy text"

def cadena_en_subcadena(cadena1,cadena2):
    return cadena2 in cadena1

def antes_alfabetico(cadena1,cadena2):
    c1 = cadena1[0]
    c2 = cadena2[0]
    if c1 < c2:
        return cadena2
    if c2 > c1:
        return cadena1


print(cadena_en_subcadena(cadena1,cadena2))
print(antes_alfabetico(cadena1,cadena2))