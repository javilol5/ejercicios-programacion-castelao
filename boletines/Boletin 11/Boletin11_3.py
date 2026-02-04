#3 Crear unha aplicación para anotar tarefas para facer. 
#A tarefa terá unha data, hora, duración, Nome da tarefa, descrición,  estado (feita, non feita).
#Para iso crear unha clase Tarefa que manexe os datos relacionados coa tarefa.  
#O usuario poderá facer as seguintes operacións:

#Agregar unha nova tarefa.
#
#Borrar unha tarefa.
#
#Modificar unha tarefa.
#
#Listar o listado de tarefas. 
#
#As tarefas se gardarán nun ficheiro binario chamado tarefas.dat.



import os
import pickle

RUTA_BASE = os.path.dirname(os.path.abspath(__file__))
FICHEIRO = os.path.join(RUTA_BASE, "tarefas.dat")



class Tarefa:
    def __init__(self, data, hora, duracion, nome, descricion, estado):
        self.data = data
        self.hora = hora
        self.duracion = duracion
        self.nome = nome
        self.descricion = descricion
        self.estado = estado

    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Data: {self.data} Hora: {self.hora}\n"
            f"Duración: {self.duracion}\n"
            f"Descrición: {self.descricion}\n"
            f"Estado: {self.estado}\n"
        )



def cargar_tarefas():
    if os.path.exists(FICHEIRO):
        with open(FICHEIRO, "rb") as f:
            return pickle.load(f)
    return []


def gardar_tarefas(tarefas):
    with open(FICHEIRO, "wb") as f:
        pickle.dump(tarefas, f)


def engadir_tarefa(tarefas):
    data = input("Data: ")
    hora = input("Hora: ")
    duracion = input("Duración: ")
    nome = input("Nome da tarefa: ")
    descricion = input("Descrición: ")
    estado = input("Estado (feita / non feita): ")

    tarefa = Tarefa(data, hora, duracion, nome, descricion, estado)
    tarefas.append(tarefa)
    gardar_tarefas(tarefas)
    print("Tarefa engadida.\n")


def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Non hai tarefas.\n")
    else:
        for i in range(len(tarefas)):
            print(f"Tarefa {i + 1}")
            print(tarefas[i])


def borrar_tarefa(tarefas):
    listar_tarefas(tarefas)
    pos = int(input("Número da tarefa a borrar: ")) - 1

    if 0 <= pos < len(tarefas):
        tarefas.pop(pos)
        gardar_tarefas(tarefas)
        print("Tarefa borrada.\n")
    else:
        print("Opción non válida.\n")


def modificar_tarefa(tarefas):
    listar_tarefas(tarefas)
    pos = int(input("Número da tarefa a modificar: ")) - 1

    if 0 <= pos < len(tarefas):
        tarefas[pos].data = input("Nova data: ")
        tarefas[pos].hora = input("Nova hora: ")
        tarefas[pos].duracion = input("Nova duración: ")
        tarefas[pos].nome = input("Novo nome: ")
        tarefas[pos].descricion = input("Nova descrición: ")
        tarefas[pos].estado = input("Novo estado: ")

        gardar_tarefas(tarefas)
        print("Tarefa modificada.\n")
    else:
        print("Opción non válida.\n")


def menu():
    print("XESTOR DE TAREFAS")
    print("1. Engadir tarefa")
    print("2. Borrar tarefa")
    print("3. Modificar tarefa")
    print("4. Listar tarefas")
    print("5. Saír")


def main():
    tarefas = cargar_tarefas()
    opcion = 0

    while opcion != 5:
        menu()
        opcion = int(input("Escolle unha opción: "))
        print()

        if opcion == 1:
            engadir_tarefa(tarefas)
        elif opcion == 2:
            borrar_tarefa(tarefas)
        elif opcion == 3:
            modificar_tarefa(tarefas)
        elif opcion == 4:
            listar_tarefas(tarefas)
        elif opcion == 5:
            print("Saíndo do programa.")
        else:
            print("Opción non válida.\n")


main()