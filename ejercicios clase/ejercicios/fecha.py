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
        if 1 <= mes <= 12 and 1 <= dia:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                diasmes[2] = 29

            if dia <= diasmes[mes]:
                match mes:
                    case 1:
                        sol = "enero"
                    case 2:
                        sol = "febrero"
                    case 3:
                        sol = "marzo"
                    case 4:
                        sol = "abril"
                    case 5:
                        sol = "mayo"
                    case 6:
                        sol = "junio"
                    case 7:
                        sol = "julio"
                    case 8:
                        sol = "agosto"
                    case 9:
                        sol = "septiembre"
                    case 10:
                        sol = "octubre"
                    case 11:
                        sol = "noviembre"
                    case 12:
                        sol = "diciembre"


print(sol)