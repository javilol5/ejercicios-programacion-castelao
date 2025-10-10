# generar contraseña aleatoria de entre 6 y 12 caracteres

import random
'''
num = int(input("Ingresa un numero entre 6 y 12: "))
passwd = ''

if 6 <= num <= 12:
    while num != 0:
        passwd += chr(random.randint(33, 126))
        num -= 1
    print(passwd)
else:
    print("El numero ingresado no es correcto")
'''

num = random.randint(6, 12)
print(num)
passwd = ''
while num != 0:
    passwd += chr(random.randint(33, 126))
    num -= 1
print(passwd)