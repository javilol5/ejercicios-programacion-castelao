# 19 Escribir unha función que reciba unha cadea de uns e ceros
#    (é dicir, un número en representación binaria) e devolte o valor decimal correspondente.

cadena = "10100010110110101001010"

def binario_decimal(cadena):
    return int(cadena, 2)

print(binario_decimal(cadena))