#1- Un almacén clasifica os seus produtos segundo a seguinte táboa de vendas anuais:
#Vendas anuais			Artigo de consumo
#< = 100 produtos			baixo
#>100 e < = 500			medio
#> 500 e < = 1000			alto
#> 1000 				primeira necesidade
#Coñecido o nome do artigo e as vendas anuais. Indicar de que tipo é.

def main():
    nombre = str(input("Ingrese nombre de producto "))
    ventas = int(input("Ingrese cantidad de ventas anuales "))
    consumo = ""
    if ventas <= 100:
        consumo = "Baja"
    elif ventas <= 500:
        consumo = "Media"
    elif ventas <= 1000:
        consumo = "Alta"
    else:
        ventas = "de Primera Necesidad"
    
    print("El producto", nombre, "tiene una prioridad", consumo)

if __name__ == "__main__":
    main()