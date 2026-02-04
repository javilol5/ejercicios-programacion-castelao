#Javier Casal Gonzalez


# Descripcion xeral:
# queremos desenvolver un pequeno sistema para xestionar xogos simples entre varios xogadores. O programa estara organizado en 3 modulos:
# 1 xogador.py : conten a clase Xogador, 2 partida.py : conten a clase Partida, 3 game_guess.py: conten o programa principal, 4 xogadorNonExisteError.py: define o un tipo de erro
#


#1
# Clase Xogador:
# Atributos: __nome (verificar str): nome identificador do xogador. Es privado y no modificable tras la creacion del objeto.        __puntuacion: puntuacion actual del jugador. Es privado
# Constuctor: Recibe unicamente el nombre (str) e inicializa la puntuacion a 0
# Metodos publicos: get_Nome que devuleve el nombre del jugador, get_Puntuacion que devuelve la puntuacion actual, set_puntos suma puntos a puntuacion xogador
#metodos especiais: __str__




class Xogador:
    def __init__(self, nome):
        self.set_Nome(nome)
        self.__puntuacion = 0

    def set_Nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome do xogador debe ser unha cadea de texto (str)")
        else:
            self.__nome = nome

    def set_Puntos(self, p: int):
        if not isinstance(p, int):
            raise TypeError("Os puntos deben ser un número enteiro")
        else:
            self.__puntuacion += p

    def get_Nome(self):
        return self.__nome

    def get_Puntuacion(self):
        return self.__puntuacion

    def __str__(self):
        return f"{self.__nome} - Puntos: {self.get_Puntuacion()}"

    def __repr__(self):
        return self.__str__()




#casos de uso
'''
x1 = Xogador("pablo")
print(x1.set_Nome(123))
print(x1.get_Nome())
print(x1.get_Puntuacion())
x1.set_Puntos(2)
print(x1.get_Puntuacion())
print(x1.__str__())
'''







#2
# clase partida,
#Atributos: __xogadores (list[Xogador | None]): lista de participantes, __num_max_xogadores (int) : atributo que server para definir o numero maximo de xogadores que se pode crear para cada partida podese consultar o valor pero non se pode modificar, __num_xogadores (int): atributo que rexistra o numero de xogadores engadidos na lista non pode sobrepasar o __num_max_xogadores
#Contructor: recibe o numero maximo de xogadores ( num_xogadores (int)) e crea unha lista valeira
#metodos publicos: get_Xogador(nome: str) -> Xogador | None: retorna o xogador co nome indicado ou None se non existe, add_Xogador(xogador:Xogador -> int: engade un novo xogador a lista e retorna o indice onde foi colocado e se o xogador xa existe ou non hay posicions libre retorna -1, get_Xogadores()-> list[Xogador|None]: retorna a lista de xogadores, add_puntos_a_Xogador(nome_e_puntos: str) -> engade puntos ao xogador e recibe un (str) co nome do xogador e os puntos separados por un espazo ' ' ou un guion e retorna o total de puntos tras a suma ou lanza unha excepcion si o xogador non existe,  get_Xogador_con_min_puntos(numero:int) -> Xogador | None : retorna o primeiro Xogador na lista que teña como minimo numero puntos, ou None se ningun xogador acada esa puntuacion
class Partida:
    def __init__(self, num_xogadores):
        self.__num_max_xogadores = num_xogadores
        self.__xogadores = []
        self.__num_xogadores = len(self.__xogadores)



    def get_Xogador(self, nome):
        for xogador in self.__xogadores:
            if xogador.get_Nome() == nome:
                return xogador
        return None

    def get_Xogadores(self):
        return self.__xogadores

    def get_Xogador_con_min_puntos(self, numero):
        for xogador in self.__xogadores:
            if xogador is not None and xogador.get_Puntuacion() >= numero:
                return xogador
        return None

    def get_num_max_Xogadores(self):
        return self.__num_max_xogadores

    def add_Xogador(self, xogador):
        if not isinstance(xogador, Xogador):
            return -1
        for x in self.__xogadores:
            if x is not None and x.get_Nome() == xogador.get_Nome():
                return -1
        if len(self.__xogadores) >= self.__num_max_xogadores:
            return -1
        else:
            self.__xogadores.append(xogador)

    def add_puntos_a_Xogador(self, nome_e_puntos: str):
        if "-" in nome_e_puntos:
            partes = nome_e_puntos.split("-")
        else:
            partes = nome_e_puntos.split(" ")

        if len(partes) != 2:
            raise ValueError("Formato incorrecto")

        nome = partes[0]
        puntos = int(partes[1])

        xogador = self.get_Xogador(nome)
        if xogador is None:
            raise XogadorNonExisteError(f"O xogador '{nome}' no existe")

        xogador.set_Puntos(puntos)
        return xogador.get_Puntuacion()



#casos de uso
'''
p1 = Partida(4)
p1.add_Xogador(Xogador("pablo"))
print(p1.get_Xogador("pablo"))
print(p1.get_Xogadores())
p1.add_Xogador(Xogador("mario"))
p1.add_Xogador(Xogador("pedro"))
p1.add_Xogador(Xogador("carla"))
print(p1.get_Xogadores())
print(p1.get_num_max_Xogadores())
print(p1.get_Xogador_con_min_puntos(2))
p1.add_puntos_a_Xogador("pablo-3")
print(p1.get_Xogador_con_min_puntos(2))
print(p1.get_Xogadores())
print(p1.get_Xogador("pablo"))
print(p1.get_num_max_Xogadores())
'''

class XogadorNonExisteError(Exception):
    def __init__(self, mensaxe="O xogador non existe"):
        super().__init__(mensaxe)


#3
#Clase XogoImpostor - Programa Principal
#debe realizar lo siguente 1- solicitar por teclado o numero de xogadores, 2- crear un obxecto Partida con ese numero de xogadores, 3-solicitar o nome de cada xogador, crear o obxecto Xogador correspondente e engadilo a Partida, 4- Entrar en un buble principal no que de forma repetida: solicite o nome do xogador que se vai anotar puntuacion, Solicite os puntos conseguidos nesa xogada, Engade os puntos ao xogador correspondente mediante o metodo exeitado de Partida, O bucle remata cando algun xogador acade como minimo 50 puntos 5- Tras rematar o buble, mostrar: A puntuacion final de todolos xogadores, O gañador do xogo(o xogador que primeiro alcanzou os 50 puntos). Notas debe validar que o nome introducido corresponde a un xogador existente, debe validar que os puntos introducidos son un numero enteiro positivo

class XogoImpostor:
    def __init__(self):
        self.partida = None
        self.ganador = None

    def iniciar_partida(self):
        while True:
            try:
                num_xogadores = int(input("Introduce o numero de xogadores: "))
                if num_xogadores > 6:#self.partida.get_num_max_Xogadores()
                    print(f"La cantidad maxima de jugadores es {self.partida.get_num_max_Xogadores()}")
                    False
                elif num_xogadores > 0:
                    break
                else:
                    print("Debe ser un numero entero positivo.")
            except ValueError:
                print("Dato invalido. Introduce un numero entero.")

        self.partida = Partida(num_xogadores)

        for i in range(num_xogadores):
            while True:
                nome = input(f"Nome do xogador {i + 1}: ")
                if nome == "":
                    print("Nombre invalido. No puede estara vacio")
                    continue

                xogador = Xogador(nome)
                indice = self.partida.add_Xogador(xogador)
                if indice != -1:
                    break
                print("Ya existe alguien con ese nombre. Introduce otro nombre.")

        while self.ganador is None:
            nome = input("Nome do xogador que anota puntos: ")

            xogador = self.partida.get_Xogador(nome)
            print (xogador)
            if xogador is None:
                print("Jugador inexistente. Introduce otro nombre.")
                continue

            try:
                puntos = int(input("Puntos conseguidos: "))
                if puntos <= 0:
                    print("Puntos invalidos. No pueden ser Negativos")
                    continue
            except ValueError:
                print("Puntos invalidos. Tiene que ser entero valido")
                continue

            try:
                total = self.partida.add_puntos_a_Xogador(f"{nome} {puntos}")
                print(f"Puntuacion de {nome}: {total}")

                if total >= 50:
                    self.ganador = xogador

            except XogadorNonExisteError as error:
                print(error)

        print("\n FIN XOGO")
        print("Puntuación final:")
        for xog in self.partida.get_Xogadores():
            if xog is not None:
                print(xog)
        print(f"\n Gañador do xogo: {self.ganador.get_Nome()}")

if __name__ == "__main__":
    xogo = XogoImpostor()
    xogo.iniciar_partida()


#se pueden poner mas jugadores de los permitidos, y se queda en un bucle infinito