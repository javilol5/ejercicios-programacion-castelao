# 17 Indique si se trata dun palíndromo.
#    Por exemplo, ‘anita lava la tina’ é un palíndromo (léese igual de esquerda a dereita que de dereita a esquerda).

texto = "anita lava la tina"

def palindromo(texto):
    texto = texto.replace(" ","")
    return texto == texto[::-1]

print(palindromo(texto))
