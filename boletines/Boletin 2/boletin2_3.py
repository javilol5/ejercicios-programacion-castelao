#3- Crea un algoritmo que cambie euros a dólares (O cambio pídese por teclado).
# Codifica o programa, correspondente, para executar o programa co nome boletin2_3  

def main():
    euros = int(input("Introduce cantidad en Euros: "))
    euroadolar = 1.1774
    print(f"{(round((euros*euroadolar),2))}$")
if __name__ == "__main__":
    main()