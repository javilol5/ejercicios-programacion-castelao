#11 Escribir unha función que reciba duas matrices e devolte o produto.
#Pregado de un texto. 
# Escribir unha función que reciba un texto e unha lonxitude e devolva unha lista de cadeas de como máximo esa lonxitude. 
# As líñas deben cortarse correctamente nos espazos (sen cortar as palabras).

def mult_matrices(matriz1, matriz2):

    mult=[]
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
resultado = mult_matrices(matriz_a, matriz_b)
print(resultado)