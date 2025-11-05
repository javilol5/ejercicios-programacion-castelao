# 20 Escribir as seguintes funcións que fagan o seguinte:
#  a) Recibindo unha cadea de caracteres e un caracter,
#     retorne unha nova cadea formada exclusivamente polo novo caracter.
#     Esta nova cadea tera a lonxitude da cadea pasada por parámetro.
#  b) Recibindo unha cadea de caracteres e un caracter,
#     a función terá que comprobar si o caracter está na cadea.
#     A función retornará un String no que aparezan guións e o caracter na posición ou posicións onde coincida na cadea.

cadena = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
caracter = "$"

def cadena_caracter(cadena,caracter):
    sol = ""
    for char in cadena:
        sol += caracter
    return sol

def caracter_en_cadena(cadena,caracter):
    sol = ""
    for char in cadena:
        if char == caracter:
            sol += caracter
        else:
            sol += "_"
    return sol

print(cadena_caracter(cadena,caracter))
print(caracter_en_cadena(cadena,caracter))