#10 Escribir unha función que reciba duas matrices e devolte a suma.
def sumar_matrices(matriz1, matriz2):
    suma=[]
    for n1, n2 in zip(matriz1, matriz2):
        suma_comb = []
        for i in range(len(n1)):
            suma_comb.append(n1[i] + n2[i])
        suma.append(suma_comb)
    return suma


def mult_matrices(matriz1, matriz2):
    mult = []
    for n1, n2 in zip(matriz1, matriz2):
        mult_comb = []
        for i in range(len(n1)):
            mult_comb.append(n1[i] * n2[i])
        mult.append(mult_comb)
    return mult


# Exemplo de uso
matriz_a = [
    [1, 2, 3],
    [4, 5, 6],      
    [7, 8, 9]
]
matriz_b = [
    [9, 7, 5],
    [3, 4, 1],
    [6, 8, 2]
]
suma_matrices = sumar_matrices(matriz_a, matriz_b)
print(suma_matrices)
# Saída: [[10, 9, 8], [7, 9, 7], [13, 16, 11]]

resultado = mult_matrices(matriz_a, matriz_b)
print(resultado)
# Saída: [[9, 14, 15], [12, 20, 6], [42, 64, 18]]