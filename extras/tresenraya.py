#crear juego tres en raya
import random

juego = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def mostrar_tablero():
    print(f"{juego[0][0]} | {juego[0][1]} | {juego[0][2]}")
    print("--+---+--")
    print(f"{juego[1][0]} | {juego[1][1]} | {juego[1][2]}")
    print("--+---+--")
    print(f"{juego[2][0]} | {juego[2][1]} | {juego[2][2]}")

def hay_ganador(jugador):
    for fila in juego:
        if fila == [jugador, jugador, jugador]:
            return True

    for c in range(3):
        if juego[0][c] == juego[1][c] == juego[2][c] == jugador:
            return True

    if juego[0][0] == juego[1][1] == juego[2][2] == jugador:
        return True
    if juego[0][2] == juego[1][1] == juego[2][0] == jugador:
        return True

    return False

def posiciones_libres():
    libres = []
    for f in range(3):
        for c in range(3):
            if juego[f][c] == " ":
                libres.append((f, c))
    return libres

movimientos = 0

while True:
    mostrar_tablero()
    print("Tu turno (X). Indica fila y columna (1, 2 o 3).")

    fila = int(input("Fila: "))
    columna = int(input("Columna: "))

    fila -= 1
    columna -= 1

    if juego[fila][columna] != " ":
        print("Esa casilla ya está ocupada. Intenta otra vez.")
        continue

    juego[fila][columna] = "X"
    movimientos += 1

    if hay_ganador("X"):
        mostrar_tablero()
        print("¡Has ganado!")
        break

    if movimientos == 9:
        mostrar_tablero()
        print("¡Empate!")
        break

    libres = posiciones_libres()
    fila_maquina, columna_maquina = random.choice(libres)
    juego[fila_maquina][columna_maquina] = "O"
    movimientos += 1

    if hay_ganador("O"):
        mostrar_tablero()
        print("La máquina ha ganado.")
        break
