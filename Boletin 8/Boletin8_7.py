#7 Dada unha lista de números enteiros e un enteiro k, escribir unha función que:
#Devolte tres listas, unha cos menores, outra cos maiores e outra cos iguais a k.
#Devolte unha lista con aqueles que son múltiplos de k.

def maiores(nums,k):
    
    mas = []
    menos = []
    igual = []

    for n in nums:
        if n > k:
            mas.append(n)
        elif n < k:
            menos.append(n)
        elif n == k:
            igual.append(n)
    
    return mas,menos,igual




# Ejemplo de uso
k = 4
lista = maiores([1,2,3,4,5,6,7,8,9],k)
mas,menos,igual=lista
print(mas, "son mayores a",k)
print(menos,"son menores a",k)
print(igual,"son iguales a",k)