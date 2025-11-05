#4 Escribir unha función que reciba unha tupla con nomes, unha posición de orixen p e unha cantidade n,
#  e imprima a mensaxe anterior (exercicio 3) para os n nombres que se encontran a partires da posición p.

def nombres(tupla_nombres, p, n):
    for nombre in tupla_nombres[p:p+n]:
        print(f'Estimado don/dona {nombre}')

# Ejemplo de uso
nombres(("Ana", "Luis", "María", "Carlos", "Sofía", "Javier"), 2, 3)
