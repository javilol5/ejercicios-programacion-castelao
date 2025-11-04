from time import time

passwd = input("Ingresa Contraseña: ")
start = time()
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
caracteres = "!@#$%^&*()=?-+*_"
chars = letras + nums + caracteres

guess = []

for val in range(12):
    a = [i for i in chars]
    for y in range(val):
        a = [x + i for i in chars for x in a]
    guess += a
    if passwd in guess:
        break

print(f"{passwd=} : {len(guess)} intentos")
print(f"Tiempo: {str(time() - start)} segundos")