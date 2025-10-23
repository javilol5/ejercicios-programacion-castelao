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


if sum_mano_dealer > 21:
    print("El jugador gana.")
elif sum_mano_dealer < sum_mano_jugador and sum_mano_dealer <= 21 and sum_mano_jugador <= 21:
    print("El jugador gana.")
elif sum_mano_dealer > sum_mano_jugador and sum_mano_dealer <= 21 and sum_mano_jugador <= 21:
    print("El dealer gana.")
else:
    print("Empate.")

jugador_bonito = []
dealer_bonito = []

for carta in mano_jugador:
    if carta == "A":
        jugador_bonito.append(diseño[1])
    elif carta == "2":
        jugador_bonito.append(diseño[2])
    elif carta == "3":
        jugador_bonito.append(diseño[3])
    elif carta == "4":
        jugador_bonito.append(diseño[4])
    elif carta == "5":
        jugador_bonito.append(diseño[5])
    elif carta == "6":
        jugador_bonito.append(diseño[6])
    elif carta == "7":
        jugador_bonito.append(diseño[7])
    elif carta == "8":
        jugador_bonito.append(diseño[8])
    elif carta == "9":
        jugador_bonito.append(diseño[9])
    elif carta == "10":
        jugador_bonito.append(diseño[10])
    elif carta == "J":
        jugador_bonito.append(diseño[11])
    elif carta == "Q":
        jugador_bonito.append(diseño[12])
    elif carta == "K":
        jugador_bonito.append(diseño[13])

for carta in mano_dealer:
    if carta == "A":
        dealer_bonito.append(diseño[1])
    elif carta == "2":
        dealer_bonito.append(diseño[2])
    elif carta == "3":
        dealer_bonito.append(diseño[3])
    elif carta == "4":
        dealer_bonito.append(diseño[4])
    elif carta == "5":
        dealer_bonito.append(diseño[5])
    elif carta == "6":
        dealer_bonito.append(diseño[6])
    elif carta == "7":
        dealer_bonito.append(diseño[7])
    elif carta == "8":
        dealer_bonito.append(diseño[8])
    elif carta == "9":
        dealer_bonito.append(diseño[9])
    elif carta == "10":
        dealer_bonito.append(diseño[10])
    elif carta == "J":
        dealer_bonito.append(diseño[11])
    elif carta == "Q":
        dealer_bonito.append(diseño[12])
    elif carta == "K":
        dealer_bonito.append(diseño[13])

print()
print("Mano del dealer: ")
#print(mano_dealer)
print(sum_mano_dealer)
print("".join(dealer_bonito))
print()
print("Mano del jugador: ")
print(sum_mano_jugador)
print("".join(jugador_bonito))
print()