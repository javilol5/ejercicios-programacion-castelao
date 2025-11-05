#9 Escribir unha función empaquetar para unha lista,
#  onde empaquetar significa indicar a repetición de valores consecutivos mediante unha tupla (valor, cantidade de repeticións). 
# Por exemplo, empaquetar ([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devoltar [(1, 3) , (3, 1) , (5, 1), (1, 2), (3, 2)].
def empaquetar(lista):
    if not lista:
        return []

    empaquetada = []
    actual = lista[0]
    i = 1

    for num in lista[1:]:
        if num == actual:
            i += 1
        else:
            empaquetada.append((actual, i))
            actual = num
            i = 1

    empaquetada.append((actual, i))

    return empaquetada

# Exemplo de uso
lista = [1, 1, 1, 3, 5, 1, 1, 3, 3]
resultado = empaquetar(lista)
print(resultado)
# Saída: [(1, 3), (3, 1), (5, 1), (1, 2), (3, 2)]