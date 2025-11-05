#  7 Escribir un programa que imprima por pantalla tódalas fichas de dominó, de unha por liña e sen repetir.

def main():

    for n1 in range(7):
        for n2 in range(n1,7):
            print(n1,"|",n2)
        print("-----")

if __name__ == "__main__":
    main()