import random
import os

# ====== CONFIGURACIÓN DE CARTAS ======

cartas = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

diseño = {
    "A": "🂡",
    "2": "🂢",
    "3": "🂣",
    "4": "🂤",
    "5": "🂥",
    "6": "🂦",
    "7": "🂧",
    "8": "🂨",
    "9": "🂩",
    "10": "🂪",
    "J": "🂫",
    "Q": "🂭",
    "K": "🂮",
    "?": "🂠"
}

manos_blackjack = [
    ["A","10"],["A","J"],["A","Q"],["A","K"],
    ["10","A"],["J","A"],["Q","A"],["K","A"]
]

# ====== FUNCIONES ======

def limpiar_pantalla():
    """Limpia la consola para mejor visualización."""
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_mano_bonita(mano, jugador):
    """Muestra las cartas bonitas (emojis grandes) en una línea."""
    print(f"\n{'='*40}")
    print(f"      🃏 Mano del {jugador} 🃏")
    print(" ".join(diseño[c] for c in mano))
    print("="*40)

def valor_mano(mano):
    """Calcula el valor total de una mano de blackjack."""
    total = 0
    ases = 0
    for carta in mano:
        if carta in ["J", "Q", "K"]:
            total += 10
        elif carta == "A":
            total += 11
            ases += 1
        else:
            total += int(carta)

    # Ajustar ases si pasa de 21
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

# ====== INICIO DEL JUEGO ======

mano_jugador = [random.choice(cartas), random.choice(cartas)]
mano_dealer = [random.choice(cartas)]

limpiar_pantalla()
mostrar_mano_bonita(mano_dealer + ["?"], "dealer")
mostrar_mano_bonita(mano_jugador, "jugador")

# ====== TURNO DEL JUGADOR ======

while True:
    valor_jugador = valor_mano(mano_jugador)
    if valor_jugador > 21:
        print("\n💥 Te pasaste de 21. Pierdes.")
        break
    if mano_jugador in manos_blackjack:
        print("\n🎉 ¡Blackjack! Ganaste.")
        break

    print("\nOpciones:")
    print("👉 (P) Pedir carta")
    print("👉 (D) Doblar")
    print("👉 (S) Plantarse")
    opcion = input("Elige una opción: ").upper()

    if opcion == "P":
        mano_jugador.append(random.choice(cartas))
        limpiar_pantalla()
        mostrar_mano_bonita(mano_dealer + ["?"], "dealer")
        mostrar_mano_bonita(mano_jugador, "jugador")
        continue

    elif opcion == "D":
        mano_jugador.append(random.choice(cartas))
        valor_jugador = valor_mano(mano_jugador)
        limpiar_pantalla()
        mostrar_mano_bonita(mano_dealer + ["?"], "dealer")
        mostrar_mano_bonita(mano_jugador, "jugador")
        if valor_jugador > 21:
            print("\n💥 Te pasaste de 21. Pierdes.")
        break

    elif opcion == "S":
        print("\n🛑 Te plantas.")
        break

    else:
        print("\n⚠️ Opción no válida, escribe 'P', 'D' o 'S'.")

# ====== TURNO DEL DEALER ======

while valor_mano(mano_dealer) < 17:
    mano_dealer.append(random.choice(cartas))

# ====== RESULTADOS ======

limpiar_pantalla()
mostrar_mano_bonita(mano_dealer, "dealer")
mostrar_mano_bonita(mano_jugador, "jugador")

puntos_jugador = valor_mano(mano_jugador)
puntos_dealer = valor_mano(mano_dealer)

print(f"\nPuntos del dealer: {puntos_dealer}")
print(f"Puntos del jugador: {puntos_jugador}")

if puntos_jugador > 21:
    print("\n💀 Te pasaste. Pierdes.")
elif puntos_dealer > 21:
    print("\n🏆 El dealer se pasa. ¡Ganas!")
elif puntos_jugador > puntos_dealer:
    print("\n🥇 ¡Ganas la partida!")
elif puntos_jugador < puntos_dealer:
    print("\n😞 El dealer gana.")
else:
    print("\n🤝 Empate.")
