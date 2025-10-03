#  5 Escribir un programa que almacene o abecedario nunha lista,
#  e cree outra lista a partir dela,
#  onde non aparezan as letras que ocupen posicións múltiplos de 3,
#  e mostre por pantalla a lista resultante.

abecedario = [chr(i) for i in range(97, 123)]
abecedario_sin_multiplos_de_tres = []
t = 1
for l in abecedario:
    if t % 3 != 0:
        abecedario_sin_multiplos_de_tres.append(l)
    t += 1
print(abecedario_sin_multiplos_de_tres)

