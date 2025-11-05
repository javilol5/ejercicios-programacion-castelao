#  8   Modificar o programa anterior para que poida xerar fichas dun xogo que pode ter números de 0 a n.

def main():
    maxnum = int(input("Ingresa numero maximo posible: ")) + 1
    for n1 in range(maxnum):
        for n2 in range(n1,maxnum):
            print(n1,"|",n2)
        print("-----")

if __name__ == "__main__":
    main()