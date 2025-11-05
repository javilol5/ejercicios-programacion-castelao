# 16 Escribir funcións que dada unha cadea de caracteres:
#  a) Devolva soamente as letras consonantes. Por exemplo, se recibe ‘algoritmos’ ou ‘logaritmos’ debe devolver ‘lgrtms’.
#  b) Devolva soamente as letras vogais. Por exemplo, se recibe ‘sen 	consonantes’ debe devoltar ‘e ooae’.
#  c) Substitúa cada vogal pola súa seguinte vogal. Por exemplo, se recibe ‘vestiario’ debe devoltar ‘vostoerou’.

cadena = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"

def solo_consonantes(cadena):
    consonantes = ("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    sol = ""
    for char in cadena:
        if char in consonantes:
            sol += char
    return sol

def solo_vocales(cadena):
    vocales = "aeiouAEIOU"
    sol = ""
    for char in cadena:
        if char in vocales:
            sol += char
    return sol

def siguente_vocal(cadena):
    vocales = "aeiouAEIOU"
    vocal = {"a":"e",
             "e":"i",
             "i":"o",
             "o":"u",
             "u":"a",
             "A":"E",
             "E":"I",
             "I":"O",
             "O":"U",
             "U":"A"}
    sol = ""
    for char in cadena:
        if char in vocales:
            sol += vocal[char]
        else:
            sol += char
    return sol

print(solo_consonantes(cadena))
print(solo_vocales(cadena))
print(siguente_vocal(cadena))