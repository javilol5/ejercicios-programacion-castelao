#4- Deseña un ordinograma que lea 2 números e calcule a suma, despois a resta, a continuación o produto e por último o cociente.
# Amosa o resultado de cada operación. De seguido codifica o programa correspondente
#
#
#Inicio
#  ↓
#[ Ler número 1 → num1 ]
#  ↓
#[ Ler número 2 → num2 ]
#  ↓
#[ suma ← num1 + num2 ]
#  ↓
#[ resta ← num1 - num2 ]
#  ↓
#[ produto ← num1 * num2 ]
#  ↓
#[ Se num2 ≠ 0 ]
#    ↓ Sí                         ↓ Non
#[ cociente ← num1 / num2 ]   [ Mensaxe: "Erro: división por cero" ]
#  ↓
#[ Amosar suma ]
#  ↓
#[ Amosar resta ]
#  ↓
#[ Amosar produto ]
#  ↓
#[ Amosar cociente ou erro ]
#  ↓
#Fin

def main():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))


    suma = num1 + num2
    resta = num1 - num2
    producto = num1 * num2


    print(f"Suma:     {suma}")
    print(f"Resta:    {resta}")
    print(f"Producto:  {producto}")


    if num2 != 0:
        cociente = num1 / num2
        print(f"Cociente: {cociente}")
    else:
        print("Error, no se puede dividir entre cero")
if __name__ == "__main__":
    main()