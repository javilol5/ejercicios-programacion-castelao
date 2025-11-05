#Fai o algoritmo e programa que calcule o soldo bruto e líquido, a percibir por unha persoa. 
# Para iso hai que ter en conta, que o soldo total inclúe os seguintes conceptos:
#
#Soldo 	fixo. 	
# 	
#Comisión: 	5% sobre importe total de vendas
# 	
#Quilometraxe: 	2 € por km
# 	
#Dietas: 	30 € por día de desprazamento.
#
#
#Para calcular o soldo líquido debemos descontarlle ao soldo bruto:
#I.R.P.F. = 18 % do soldo total.
# 	
#Retención a seguridade social : 36 €.

def main():

    SueldoFijo = int(input("Cuanto es el sueldo Fijo? "))
    Ventas = int(input("Cuanto dinero gano en ventas? "))
    Km = int(input("Cuanto kilometros recorrio? "))
    DiasDieta = int(input("Cuantos dias se comió fuera? "))

    Comision = Ventas * 0.05
    Km = Km * 2
    Dietas = DiasDieta * 30

    Bruto = SueldoFijo + Comision + Km + Dietas

    Irpf = Bruto * 0.18
    SS = 36

    Liquido = Bruto - Irpf - SS

    print("Esto es el sueldo Bruto: ", Bruto)
    print("Esto es el sueldo Liquido: ", Liquido)