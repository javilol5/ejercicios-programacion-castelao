#quitar espacios antes y despues sin usar stim ni strip

frase = str(input("Ingresa una frase: "))
i = 0
while frase[i] == " ":
    frase = frase[1:]
frase = frase[::-1]
while frase[i] == " ":
    frase = frase[1:]
frase = frase[::-1]
print(frase)