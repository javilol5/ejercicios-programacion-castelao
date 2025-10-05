#  4 Elimina os espazos do texto: “Guido Van Rossum creou Python”

string = "Guido Van Rossum creou Python"
sin_espacio = string.split(" ")
print("".join(sin_espacio))
