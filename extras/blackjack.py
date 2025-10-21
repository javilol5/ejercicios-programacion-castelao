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

manos_blackjack = [["A","10"],["A","J"],["A","Q"],["A","K"],["10","A"],["J","A"],["Q","A"],["K","A"]]
mano_jugador = [random.choice(cartas),random.choice(cartas)]
mano_dealer = [random.choice(cartas)]
print("Mano del dealer: ")
print(" ".join(mano_dealer),"?")
print()
print("Mano del jugador: ")
print(" ".join(mano_jugador))
print()



num_mano_jugador = sum(int(10 if carta in ["J","Q","K"] else 11 if carta == "A" else carta) for carta in mano_jugador)
num_mano_dealer = sum(int(10 if carta in ["J","Q","K"] else 11 if carta == "A" else carta) for carta in mano_dealer)

while num_mano_jugador <= 21:
    if mano_jugador in manos_blackjack:
        print("Mano del jugador: ")
        print(" ".join(mano_jugador))
        print()
        print("¡Blackjack! Ganaste.")
        break
    else:
        print("Pedir carta (P) ")
        print("Doblar (D) ")
        print("Plantarse (S) ")
        opcion = input("¿Qué quieres hacer? ").upper()

        if opcion == "P":
            mano_jugador.append(random.choice(cartas))
            print("Mano del jugador: ")
            print(" ".join(mano_jugador))
            print()
            if sum([10 if carta in ["J","Q","K"] else 11 if carta == "A" else int(carta) for carta in mano_jugador]) > 21:
                print("Te pasaste de 21. Pierdes.")
                break

        elif opcion == "D":
            mano_jugador.append(random.choice(cartas))
            print("Mano del jugador: ")
            print(" ".join(mano_jugador))
            print()
            if sum([10 if carta in ["J","Q","K"] else 11 if carta == "A" else int(carta) for carta in mano_jugador]) > 21:
                print("Te pasaste de 21. Pierdes.")
            break

        elif opcion == "S":
            print("Te plantas con: ")
            print(" ".join(mano_jugador))
            print()
            break

        else:
            print("Opción no válida, escribe 'P', 'D' o 'S'.")

while num_mano_dealer < 17:
    mano_dealer.append(random.choice(cartas))
    num_mano_dealer = sum(int(10 if carta in ["J","Q","K"] else 11 if carta == "A" else carta) for carta in mano_dealer)


sum_mano_jugador = 0
sum_mano_dealer = 0

for carta_mano_jugador in mano_jugador:
    if carta_mano_jugador in ["J","Q","K"]:
        sum_mano_jugador += 10
    elif carta_mano_jugador == "A":
        sum_mano_jugador += 11
    else:
        sum_mano_jugador += int(carta_mano_jugador)

for carta_mano_dealer in mano_dealer:
    if carta_mano_dealer in ["J","Q","K"]:
        sum_mano_dealer += 10
    elif carta_mano_dealer == "A":
        sum_mano_dealer += 11
    else:
        sum_mano_dealer += int(carta_mano_dealer)

if sum_mano_dealer > sum_mano_jugador:
    print("El dealer gana.")
elif sum_mano_dealer < sum_mano_jugador:
    print("El jugador gana.")
else:
    print("Empate.")



print()
print("Mano del dealer: ")
print(mano_dealer)
print(sum_mano_dealer)
print()
print("Mano del jugador: ")
print(sum_mano_jugador)
print()





























'''carta = random.choice(cartas)

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
print(diseño)'''