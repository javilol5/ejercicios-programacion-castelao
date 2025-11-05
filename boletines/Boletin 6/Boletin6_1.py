#  1 Escribir un programa que almacene as asignaturas dun curso (por exemplo Matemáticas,
#  Física, Química, Historia e Língua) nunha lista,
#  pregunte o usuario a nota que sacou en cada asignatura,
#  e despois as mostre por pantalla co mensaxe
#  En <asignatura> sacaches <nota>
#  onde <asignatura> é cada unha das asignaturas da lista
#  e <nota> cada unha das correspondentes notas introducidas polo usuario.

materias = [ 'Matemáticas', 'Física', 'Química', 'Historia','Língua']
notas = []
i = 0
for n in materias:
    nota =int(input("Cuanto sacastes en " + n + "? "))
    notas.append(nota)
for m in materias:
    print(materias[i], notas[i])
    i += 1