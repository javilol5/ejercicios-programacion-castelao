#Verificar que una fecha sea valida en el formato dd/mm/aaaa

fecha = str(input("Escribe fecha: "))
sol = ''
solfecha = fecha.strip()
diasmes = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

print(solfecha)
if len(solfecha) == 10:
    if solfecha[2] == "/" and solfecha[5] == "/":
        splitfecha = solfecha.split("/")
        valido = True
        for num in splitfecha:
            try:
                int(num)
            except ValueError:
                valido = False
                break
        if valido:
            dia = int(splitfecha[0])
            mes = int(splitfecha[1])
            ano = int(splitfecha[2])
        print(dia)
        print(mes)
        print(ano)
        print(splitfecha)
        if dia > 31 or mes > 12:
            sol = "formato no valido"
        else:

            if ano % 4 != 0 and dia > diasmes[mes]:
                sol = "formato no valido"
            else:
                diasmes[2] = 29
                if dia > diasmes[mes]:
                    sol = "formato no valido"
                else:
                    sol = "formato valido"
    else:
        sol = "formato no valido"
else:
    sol = "formato no valido"
print(sol)