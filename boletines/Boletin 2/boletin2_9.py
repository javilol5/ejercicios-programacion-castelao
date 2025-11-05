#Realiza un algoritmo e codifica o programa correspondente que lea,
#  dende o teclado, unha cantidade enteira en euros e amose, por pantalla, o 	
# seu desglose en billetes de 100, 20, 5 e moedas de 1 €.

def main():
    resultado = int(input("Cuanto dinero tienes? "))

    b100 = resultado // 100
    resultado = resultado % 100
    
    b20 = resultado // 20
    resultado = resultado % 20
    
    b5 = resultado // 5
    resultado = resultado % 5
    
    b1 = resultado // 1
    resultado = resultado % 1
    
    print("Billetes de 100 €:", b100)
    print("Billetes de 20 €: ", b20)
    print("Billetes de 5 €: ", b5)
    print("Moedas de 1 €: ", b1)

if __name__ == "__main__":
    main()