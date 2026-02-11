lista = [1,4,2,5,2,6,2,0,6,12,34,54,3,2,55,13,15,31,42,4]
lista_nueva = []
'''
cero = 0
while len(lista_nueva) != len(lista):
    for n in lista:
        if n == cero:
            lista_nueva.append(n)
    cero += 1

print(lista_nueva)

'''

'''
long = len(lista)

for i in range(long):
    indice_menor = i

    for j in range(i + 1, long):
        if lista[j] < lista[indice_menor]:
            indice_menor = j

    aux = lista[i]
    lista[i] = lista[indice_menor]
    lista[indice_menor] = aux

print(lista)
'''
'''
from random import *

long = len(lista)
intentos = 0
for i in range(long):
    indice_menor = i

    for j in range(i + 1, long):
        if lista[j] < lista[indice_menor]:
            indice_menor = j

    aux = lista[i]
    lista[i] = lista[indice_menor]
    lista[indice_menor] = aux
while shuffle(lista) != lista:
    intentos += 1
    print (intentos)
print(lista)
'''
'''
cp_lista = lista.copy()

while len(lista_nueva) != len(cp_lista):
    l_aux = []
    for n in lista:
        l_aux.append(n)
        if len(l_aux) == 2:
            if l_aux[0] <= l_aux[1]:
                l_aux.pop(l_aux.index(l_aux[1]))
            elif l_aux[0] > l_aux[1]:
                l_aux.pop(l_aux.index(l_aux[0]))
    lista_nueva.append(l_aux[0])
    lista.remove(l_aux[0])

print(lista_nueva)
'''