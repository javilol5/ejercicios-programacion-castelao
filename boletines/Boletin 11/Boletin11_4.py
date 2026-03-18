#Crea a aplicación que permita gardar e recuperar os datos dos clientes dunha empresa.
# Para o cal, defina a clase Cliente, que teña os atributos:
#id, identificador de cliente
#nome
#teléfono
#
#	Os obxectos Cliente se recollerán nunha lista.
#	A aplicación terá un menú que posibilitará as seguintes opcións:
#Engadir novo cliente
#Modificar datos
#Dar de baixa clientes.
#Listar os clientes.
#	A información se gardará nun ficheiro binario, que cargará en memoria o iniciar o programa e se gardará en disco, actualizado o rematar.



import os
import pickle

RUTA_BASE = os.path.dirname(os.path.abspath(__file__))
FICHEIRO = os.path.join(RUTA_BASE, "cliente.dat")

class Cliente:
    def __init__(self, id, nome, tel):
        self.id = id
        self.nome = nome
        self.tel = tel

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Teléfono: {self.tel}"


def cargar_clientes():
    if os.path.exists(FICHEIRO):
        try:
            with open(FICHEIRO, "rb") as f:
                return pickle.load(f)
        except EOFError:
            return []
    return []

def engadir_cliente(clientes):
    id = input("ID del cliente: ")
    nome = input("Nombre del cliente: ")
    tel = input("Telefono del cliente: ")

    cliente = Cliente(id, nome, tel)
    clientes.append(cliente)
    gardar_clientes(clientes)
    print("Cliente engadida.\n")

def gardar_clientes(clientes):
    with open(FICHEIRO, "wb") as f:
        pickle.dump(clientes, f)

def listar_clientes(clientes):
    if len(clientes) == 0:
        print("Non hai cliente.\n")
    else:
        for i in range(len(clientes)):
            print(f"Tarefa {i + 1}")
            print(clientes[i])

def baixa_cliente(clientes):
    listar_clientes(clientes)
    pos = int(input("Número da cliente a borrar: ")) - 1

    if 0 <= pos < len(clientes):
        clientes.pop(pos)
        gardar_clientes(clientes)
        print("Cliente borrada.\n")
    else:
        print("Opción non válida.\n")


def modificar_datos(clientes):
    listar_clientes(clientes)
    pos = int(input("Número da cliente a modificar: ")) - 1

    if 0 <= pos < len(clientes):
        clientes[pos].id = input("Novo ID: ")
        clientes[pos].nome = input("Novo nome: ")
        clientes[pos].tel = input("Novo telefono: ")

        gardar_clientes(clientes)
        print("Cliente modificada.\n")
    else:
        print("Opción non válida.\n")

def menu():
    print("XESTOR DE CLIENTE")
    print("1. Engadir novo cliente")
    print("2. Modificar datos")
    print("3. Dar de baixa clientes")
    print("4. Listar os clientes")
    print("5. Saír")


def main():
    clientes = cargar_clientes()
    opcion = 0

    while opcion != 5:
        menu()
        opcion = int(input("Escolle unha opción: "))
        print()

        if opcion == 1:
            engadir_cliente(clientes)
        elif opcion == 2:
            modificar_datos(clientes)
        elif opcion == 3:
            baixa_cliente(clientes)
        elif opcion == 4:
            listar_clientes(clientes)
        elif opcion == 5:
            print("Saíndo do programa.")
        else:
            print("Opción non válida.\n")


main()