#5- Escribe un programa que lea o valor dunha distancia en millas mariñas e a pase a metros ( 1 milla mariña = 1852 m ).
#Codifica o programa correspondente para executar o programa

def main():
    millas = int(input("Introduce distancia en Millas: "))
    metromillas = 1852
    print(f"{(round((millas*metromillas),2))} m")
if __name__ == "__main__":
    main()