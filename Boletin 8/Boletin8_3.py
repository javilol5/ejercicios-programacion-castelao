#3 Escribir unha función que reciba unha tupla con nomes e para cada nome imprima unha mensaxe ‘Estimado don/dona Nome’
def nombres(tupla_nombres):
    for nombre in tupla_nombres:
        print(f'Estimado don/dona {nombre}')

# Ejemplo de uso
nombres(("Ana", "Luis", "María", "Carlos"))
