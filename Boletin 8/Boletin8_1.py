#1 Escribir unha función que reciba unha tupla de elementos e indique si se encontran ordeados de menor a maior ou non.
def esta_ordenada(tupla):
    ordenada = True
    for i in range(len(tupla) - 1):
        if tupla[i] > tupla[i + 1]:
            ordenada = False

    return ordenada

# Ejemplo de uso
t1 = (1, 3, 9, 8)
t2 = (1, 3, 89, 700)

print(esta_ordenada(t1))
print(esta_ordenada(t2))


