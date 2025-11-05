# 22 Escribe a función que permita formatear de nomes.
#    A función ten que eliminar os espazos en branco e poñer en maiúsculas o primeiro caracter do nome e apelido pasado como parámetro. 
#    Finalmente retornará unha cadea co nome e apelidos co formato solicitado.




def formatear_nombre(nombre_completo):
    nombre_completo = nombre_completo.strip()
    partes = nombre_completo.split()
    partes_unidas = ""
    for parte in partes:
        partes_unidas += parte.capitalize() + " "
    return partes_unidas.strip()

nombre1 = "   juan perez lopez   "
nombre2 = "maria gonzalez"
nombre3 = "  ana    martinez  "

print(formatear_nombre(nombre1))
print(formatear_nombre(nombre2))
print(formatear_nombre(nombre3))