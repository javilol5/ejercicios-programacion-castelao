# 10 Deseña un programa que calcule o área dun rectángulo cuxa base e altura pides por teclado.
# Asegúrate que estes valores sexan positivos, para eso valida os datos.

def main():
    
    a = int(input("Ingresa altura: "))
    b = int(input("Ingresa base: "))

    if a < 0 or b < 0:
        print("datos invalidos")
    else:
        print(b*a)

if __name__ == "__main__":
    main()