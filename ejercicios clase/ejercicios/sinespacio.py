#quitar espacios antes y despues sin usar stim ni strip

frase = str(input("Ingresa una frase: "))
while frase[0] == " ":
    frase = frase[1:]
frase = frase[::-1]
while frase[0] == " ":
    frase = frase[1:]
frase = frase[::-1]
print(frase)