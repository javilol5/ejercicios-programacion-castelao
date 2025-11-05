#  4 Escribir un programa que almacene as asignaturas dun curso
#  (por exemplo Matemáticas, Física, Química, Historia e Língua) nunha lista,
#  pregunte o usuario a nota que sacou en cada asignatura e elimine da lista as asignaturas aprobadas.
#  O fin, o programa debe mostrar por pantalla as asignaturas que o usuario ten que repetir.

materias = [ 'Matemáticas', 'Física', 'Química', 'Historia','Língua']
materias_suspensas = []
notas = []
i = 0
for n in materias:
    nota =int(input("Cuanto sacastes en " + n + "? "))
    if nota < 5:
        notas.append(nota)
        materias_suspensas.append(n)

for m in materias_suspensas:
    print(materias_suspensas[i], notas[i])
    i += 1