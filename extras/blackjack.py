#Crear juego blackjack

import random

juego = [
    [" "," "],
    [" "," "]
    ]

cartas = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
cartas_bonitas = ["🂡","🂢","🂣","🂤","🂥","🂦","🂧","🂨","🂩","🂪","🂫","🂭","🂮",
#                  "🃁","🃂","🃃","🃄","🃅","🃆","🃇","🃈","🃉","🃊","🃋","🃍","🃎",
#                  "🂱","🂲","🂳","🂴","🂵","🂶","🂷","🂸","🂹","🂺","🂻","🂽","🂾",
#                  "🃑","🃒","🃓","🃔","🃕","🃖","🃗","🃘","🃙","🃚","🃛","🃝","🃞"
                  ]

diseño = {
    1 : "🂡",
    2 : "🂢",
    3 : "🂣",
    4 : "🂤",
    5 : "🂥",
    6 : "🂦",
    7 : "🂧",
    8 : "🂨",
    9 : "🂩",
    10 : "🂪",
    11 : "🂫",
    12 : "🂭",
    13 : "🂮"
}


carta = random.choice(cartas)

def valor_carta(carta):
    carta = random.choice(cartas)
    if carta in ["J︎","Q︎","K︎"]:
        return 10
    elif carta in ["A"]:
        return 11
    else:
        return int(carta)

def mano_dealer():
    mano = []
    mano.append(random.choice(cartas))
    mano.append(random.choice(cartas))
    return mano

def mano_jugador():
    mano = []
    mano.append(random.choice(cartas))
    mano.append(random.choice(cartas))
    return mano

def tablero(mano_jugador, mano_dealer):
    print("Mano del dealer: ")
    print(" ".join(mano_dealer))
    print()
    print("Mano del jugador: ")
    print(" ".join(mano_jugador))
    print()

def bust(mano_jugador):
    total = sum(valor_carta(carta) for carta in mano_jugador)
    return total > 21

def blackjack(mano_jugador):
    return sum(valor_carta(carta) for carta in mano_jugador) == 21

def ganador(mano_jugador, mano_dealer):
    total_jugador = sum(valor_carta(carta) for carta in mano_jugador)
    total_dealer = sum(valor_carta(carta) for carta in mano_dealer)
    if total_jugador > total_dealer:
        return "Jugador gana"
    elif total_jugador < total_dealer:
        return "Dealer gana"
    else:
        return "Empate"

def pedir_carta(mano_jugador):
    mano_jugador.append(random.choice(cartas))
    return mano_jugador

def pedir_dealer(mano_dealer):
    while sum(valor_carta(carta) for carta in mano_dealer) < 17:
        mano_dealer.append(random.choice(cartas))
    return mano_dealer

print(tablero(mano_jugador(), mano_dealer()))

while True:
    opcion = input("¿Quieres pedir carta? (s/n): ")

    if opcion == "s":
        pedir_carta(mano_jugador())
        tablero(mano_jugador(), mano_dealer())

        if bust(mano_jugador()):
            print("Te pasaste de 21. Pierdes.")
            break

        if blackjack(mano_jugador()):
            print("¡Blackjack! Ganaste.")
            break

    elif opcion == "n":
        pedir_dealer(mano_dealer())
        tablero(mano_jugador(), mano_dealer())
        print(ganador(mano_jugador(), mano_dealer()))
        break

    else:
        print("Opción no válida, escribe 's' o 'n'.")

print(cartas_bonitas)
print(diseño)