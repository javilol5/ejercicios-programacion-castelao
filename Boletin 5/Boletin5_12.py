# 12 Codifica un programa que lea o soldo de cada un dos traballadores dunha empresa
#    e obteña o número deles que ganan entre 1000 e 1750 €, 
#    ámbolos dous incluídos e, a porcentaxe de traballadores que ganan menos de 1000 €. 
#    Tendo en conta que non se coñece con antelación o numero de traballadores da empresa 
#    e non se admiten os soldos negativos (utiliza como condición de fin un soldo 0).

#Sin saber numero exacto de trabajadores

def main():

    masmil = 0
    menosmil = 0
    x = 1
    sueldo = int(input("Ingrese sueldo " + str(x) + " (0 para terminar): "))
    while sueldo != 0:
        if 1000 <= sueldo <= 1750:
            masmil += 1
            x += 1
        elif 0 < sueldo < 1000:
             menosmil += 1
             x += 1
        elif sueldo == 0:
            print("Fin")
        else:
            print("Sueldo invalido")
        sueldo = int(input("Ingrese sueldo " + str(x) + " (0 para terminar): "))
    print("Sueldos entre 1000 y 1750: ", masmil)
    print("Porcentaje de sueldos por debajo de 1000: ", round((menosmil*100/(x-1)),2), "%")

if __name__ == "__main__":
    main()



#Sabiendo numero exacto de trabajadores
#
#def main():
#
#    masmil = 0
#    menosmil = 0
#    x = 1
#    numtrabajadores = int(input("Ingrese la cantidad de trabajadores: "))
#    for persona in range(1, numtrabajadores + 1):
#        sueldo = int(input("Ingrese sueldo "+str(x)+": "))
#        x += 1
#        if 1000 <= sueldo <= 1750:
#            masmil += 1
#        elif 0 < sueldo < 1000:
#             menosmil += 1
#        else:
#            print("Sueldo invalido")
#    print("Sueldos entre 1000 y 1750: ", masmil)
#    print("Porcentaje de sueldos por debajo de 1000: ", round((menosmil*100/numtrabajadores),2), "%")
#
#if __name__ == "__main__":
#    main()