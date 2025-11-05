#5 Modificar as funcións anteriores para que teñan en conta o xénero do destinatario,
#  para elo, deberán recibir unha tupla de tuplas, 
# contendo o nome e o xénero, adaptando a mensaxe con ‘don’ ou ‘dona’ dependendo deste.

def nombres(tupla):
    for i in tupla:
        if i[1] == 'H':
            print(f'Hola don {i[0]}')
        elif i[1] == 'M':
            print(f'Hola dona {i[0]}')

# Ejemplo de uso
nombres((("Ana", "M"), ("Luis", "H"), ("María", "M"), ("Carlos", "H")))
