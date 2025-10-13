#Crear juego del ahorcado
import random
palabras = [
    "apple", "table", "chair", "house", "water", "bread", "light", "music", "sport", "plant",
    "fruit", "style", "world", "sleep", "smile", "drink", "dance", "beach", "cloud", "stone",
    "grass", "heart", "brain", "dream", "power", "quiet", "quick", "happy", "magic", "green",
    "black", "white", "brown", "ocean", "river", "earth", "stars", "shine", "sweet", "sugar",
    "spice", "spicy", "honey", "berry", "peach", "mango", "lemon", "grape", "melon", "olive",
    "onion", "pizza", "pasta", "bacon", "cream", "sauce", "toast", "flour", "salad", "steak",
    "sushi", "curry", "bagel", "donut", "fries", "mocha", "latte", "cocoa", "guava", "papaw",
    "pecan", "maple", "cedar", "birch", "sprig", "coral", "shell", "plank", "brush", "cloth",
    "shirt", "pants", "dress", "scarf", "socks", "shoes", "watch", "phone", "cable", "mouse",
    "print", "paper", "ruler", "paint", "color", "azure", "fauna", "flora"
]

palabra = random.choice(palabras)
#print(palabra)
guess = ["_"] * len(palabra)
vida = 9
while "_" in guess:
    print("".join(guess))
    letra = str(input("Ingresa una letra: "))
    if letra in palabra:
        pos = []
        for i in range(len(palabra)):
            if palabra[i] == letra:
                guess[i] = letra
    else:
        if vida > 0:
            print("La letra no esta, tue quedan", vida, "vidas")
        else:
            print("Te quedaste sin vidas")
            guess = palabra
            print("La palabra era: ", guess)
        vida -= 1

print("Ganaste!!! la palabra era: ", "".join(guess))