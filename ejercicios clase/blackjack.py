#Crear juego blackjack

import random

juego = [
    [" "," "],
    [" "," "]
    ]

cartas = ["A♣︎","2♣︎","3♣︎","4♣︎","5♣︎","6♣︎","7♣︎","8♣︎","9♣︎","10♣︎","J♣︎","Q♣︎","K♣︎",
          "A♦︎","2♦︎","3♦︎","4♦︎","5♦︎","6♦︎","7♦︎","8♦︎","9♦︎","10♦︎","J♦︎","Q♦︎","K♦︎",
          "A♥︎","2♥︎","3♥︎","4♥︎","5♥︎","6♥︎","7♥︎","8♥︎","9♥︎","10♥︎","J♥︎","Q♥︎","K♥︎",
          "A♠︎","2♠︎","3♠︎","4♠︎","5♠︎","6♠︎","7♠︎","8♠︎","9♠︎","10♠︎","J♠︎","Q♠︎","K♠︎"]

carta = random.choice(cartas)

def valor_carta(carta):
    if carta in ["J♣︎","Q♣︎","K♣︎","J♦︎","Q♦︎","K♦︎","J♥︎","Q♥︎","K♥︎","J♠︎","Q♠︎","K♠︎"]:
        return 10
    elif carta in ["A♣︎","A♦︎","A♥︎","A♠︎"]:
        return 11
    else:
        return int(carta[:-2])

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

print(tablero(mano_jugador(), mano_dealer()))