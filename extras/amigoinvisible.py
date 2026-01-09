import random
class AmigoInvisible:
    def __init__(self):
        self.__nombres = []

    def setNombre(self, nombre):
        nombre = nombre.capitalize()
        self.__nombres.append(nombre)

    def getNombres(self):
        return self.__nombres

    def tocar(self):
        if len(self.__nombres) < 2:
            return []

        origen = []
        for n in self.__nombres:
            origen.append(n)

        destino = []
        for n in self.__nombres:
            destino.append(n)

        random.shuffle(destino)

        while True:
            valido = True
            i = 0
            while i < len(origen):
                if origen[i] == destino[i]:
                    valido = False
                    break
                i = i + 1

            if valido:
                break

            random.shuffle(destino)

        resultado = []
        i = 0
        while i < len(origen):
            pareja = [origen[i], destino[i]]
            resultado.append(pareja)
            i = i + 1

        return resultado

    def bonito(self):
        parejas = self.tocar()
        if len(parejas) == 0:
            print("No hay suficientes participantes.")
            return

        i = 0
        while i < len(parejas):
            print(parejas[i][0] + " → " + parejas[i][1])
            #print("\n" * 20)
            i = i + 1



if __name__ == "__main__":
    c1 = AmigoInvisible()
    c1.setNombre("Pablo")
    c1.setNombre("María")
    c1.setNombre("Pedro")
    c1.setNombre("juan")
    c1.setNombre("gabriela")
    c1.setNombre("hugo")
    c1.setNombre("carlos")
    c1.setNombre("adrian")
    c1.setNombre("fernando")
    c1.setNombre("sabela")

#    print(c1.getNombres())
#    print(c1.tocar())
    print(c1.bonito())
