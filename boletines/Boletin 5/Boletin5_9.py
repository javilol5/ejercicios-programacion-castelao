#  9 Calcula a cantidade de números negativos, positivos e ceros que hai nun grupo de 10 números enteiros.

def main():

    negnum = 0
    ceronum = 0
    posnum = 0
    x = 0
    while x < 10:
        num = int(input("Ingresa número " + str(x+1) +":"))
        x += 1


        num = int(num)
        if num == 0:
            ceronum += 1
        elif num > 0:
            posnum += 1
        else:
            negnum += 1
    print("Hay",posnum,"números positivos")
    print("Hay",ceronum, "ceros")
    print("Hay",negnum,"números negativos")

if __name__ == "__main__":
    main()