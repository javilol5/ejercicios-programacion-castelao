# 11 Escribir un programa que pregunte por unha mostra de números, 
# separados por comas, os garde nunha lista e mostre por pantalla a súa media e desviación típica.

nums = input("Ingresa numeros separados por ',': ")
lista = []
for n in nums.split(","):
    lista.append(float(n))

media = sum(lista) / len(lista)

desviacion = sum((x - media)**2 for x in lista)

desviaciones = 0
for x in lista:
    desviaciones += (x - media) ** 2
desviacion_tipica = (desviaciones / len(lista)) ** 0.5

print("Media: ", media)
print("Desviación típica: ",desviacion_tipica)