#crear un programa que sume cuanto dinero hay en cada caja de un supermercado
#cuanto dinero hay en cada caja
#cuanto dinero hay total
#imprimir cuanto hay de cada tipo en cada caja
#imprimir cuanto hay de cada tipo en total

def dinero_en_caja(tupla):
    for cajas in tupla:
        sum = 0
        caja = cajas[1:]
        for bill in caja:
            sum += bill[0]*bill[1]
        print("Dinero Total de la caja",cajas[0],sum,"€")

def dinero_en_cajas_total(tupla):
    sum = 0
    for cajas in tupla:
        caja = cajas[1:]
        for bill in caja:
            sum += bill[0]*bill[1]
    print("Dinero total de todas las cajas:",sum,"€")

def cantidad_tipos_billetes(tupla):
    for cajas in tupla:
        caja = cajas[1:]
        contadores = {
            500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0,
            2: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0
        }

        for billete in caja:
            valor, cantidad = billete
            contadores[valor] += cantidad

        print("Caja",cajas[0])
        for valor in contadores:
            if valor >= 5:
                tipo = "Billetes"
            else:
                tipo = "Monedas"
            print(contadores[valor],tipo,"de",valor)
        print("-----")

def cantidad_tipos_billetes_total(tupla):
    contadores = {
        500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0,
        2: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0
    }
    for cajas in tupla:
        caja = cajas[1:]
        for valor,cantidad in caja:
            contadores[valor] += cantidad

    print("Cantidad total de todas las cajas")
    for valor in contadores:
        if valor >= 5:
            tipo = "Billetes"
        else:
            tipo = "Monedas"
        print(contadores[valor],tipo,"de",valor)





#USO

t1 = [["1",[50,2],[20,3],[10,8],[5,13],[2,6],[1,4],[0.5,8]],["2",[100,3],[50,4],[20,6],[10,2],[5,21],[2,19],[1,2],[0.5,9]],["3",[20,8],[10,1],[5,2],[2,4],[1,9],[0.5,4]]]
t2 = [["1",[500,1],[200,0],[100,2],[50,1],[20,7],[10,5],[5,4],[2,8],[1,3],[0.5,6]],["2",[50,2],[20,10],[10,0],[5,6],[2,2],[1,1],[0.5,3]]]
t3 = [["2",[200,1],[100,1],[50,0],[20,4],[10,7],[5,2],[2,5],[1,6],[0.5,2],[0.2,10]],["4",[50,3],[20,2],[10,3],[5,8],[2,0],[1,4],[0.5,1]],["6",[20,1],[10,2],[5,5],[2,3],[1,0]]]
t4 = [["8",[100,0],[50,5],[20,3],[10,9],[5,0],[2,7],[1,2],[0.5,4],[0.1,20]],["9",[50,1],[20,6],[10,4],[5,2],[2,1],[1,8]],["15",[20,2],[10,0],[5,1],[2,2],[1,1],[0.5,5]]]

print(dinero_en_caja(t1))
print(dinero_en_cajas_total(t1))
print(cantidad_tipos_billetes(t1))
print(cantidad_tipos_billetes_total(t1))

print(dinero_en_caja(t2))
print(dinero_en_cajas_total(t2))
print(cantidad_tipos_billetes(t2))
print(cantidad_tipos_billetes_total(t2))

print(dinero_en_caja(t3))
print(dinero_en_cajas_total(t3))
print(cantidad_tipos_billetes(t3))
print(cantidad_tipos_billetes_total(t3))

print(dinero_en_caja(t4))
print(dinero_en_cajas_total(t4))
print(cantidad_tipos_billetes(t4))
print(cantidad_tipos_billetes_total(t4))
