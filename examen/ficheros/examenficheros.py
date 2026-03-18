#Examen 18-mar-2026 Javier Casal González
#1
#Unha empresa do sector pesqueiro, ten una flota de barcos
#Os barcos se caracterizan polos: metros de eslora, toneladas de carga, calado, potencia, velocidade (en nós), consumo medio por dia (l/dia), nome, matriculo, numero tripulantes
#Estes barcos podense clasificar en 2 tipos: 1. Extractores: adicanse a pescar segundo distintas artes (arrastre, cerco, etc). 2. Auxiliares: son buques que permiten asistir a recoller a pesca en alta mar dos extractores nas suas campañas de varios meses nos oceanos
#Os barcos pesqueiros teñen cámaras, estas poden ser ou frigorificas, ou conxeladoras. Estas cámaras teñen a sua capacidade definida en metros cubicos
#Todoslos barcos auxiliares están provistos de camaras conxeladoras. Dentro dos barcos auxiliares hai un subtipo que ten compartimentos de fuel, con unha capacidade determinada en litros. Estes barcos teñen a funcion de reencher depositos dos barcos extractores an alta mar
# Realizar a codificacion das clases necesarias para poder modelar un barco auxiliar provisto de compartimento para transporte de fuel
#Ter en conta que as clases so poden permitir introducir datos validos nas suas variables (non permitido o acceso directo a elas) e deixará consultar e cambiar calquera deses datos menos o nome e a matricula
#Ademais, os obxectos instanciados, teñen que ter obrigatoriamente dous métodos: 1. __str__() 2. calculo_custe_consumo(dias:int, prezo:float) -> float devolta o custe do fuel en euros por litro (float). Este custe se calcula multiplicando o consumo medio (litros/dia) polo numero de dias de campaña e prezo do fuel (€/l)


class Barco:
    def __init__(self, eslora, toneladas_carga, calado, potencia, velocidade, consumo_medio, nome, matricula, num_tripulantes):

        self.set_eslora(eslora)
        self.set_toneladas_carga(toneladas_carga)
        self.set_calado(calado)
        self.set_potencia(potencia)
        self.set_velocidade(velocidade)
        self.set_consumo_medio(consumo_medio)
        self.__nome = nome
        self.__matricula = matricula
        self.set_num_tripulantes(num_tripulantes)


    def get_eslora(self):
        return self.__eslora
    def get_toneladas_carga(self):
        return self.__toneladas_carga
    def get_calado(self):
        return self.__calado
    def get_potencia(self):
        return self.__potencia
    def get_velocidade(self):
        return self.__velocidade
    def get_consumo_medio(self):
        return self.__consumo_medio
    def get_nome(self):
        return self.__nome
    def get_matricula(self):
        return self.__matricula
    def get_num_tripulantes(self):
        return self.__num_tripulantes

    def set_eslora(self, eslora):
        if eslora > 0:
            self.__eslora = eslora
        else:
            raise ValueError("Cantidad invalida")

    def set_toneladas_carga(self, toneladas_carga):
        if toneladas_carga >= 0:
            self.__toneladas_carga = toneladas_carga
        else:
            raise ValueError("Cantidad invalida")

    def set_calado(self, calado):
        if calado > 0:
            self.__calado = calado
        else:
            raise ValueError("Cantidad invalida")

    def set_potencia(self, potencia):
        if potencia > 0:
            self.__potencia = potencia
        else:
            raise ValueError("Cantidad invalida")

    def set_velocidade(self, velocidade):
        if velocidade >= 0:
            self.__velocidade = velocidade
        else:
            raise ValueError("Cantidad invalida")

    def set_consumo_medio(self, consumo):
        if consumo >= 0:
            self.__consumo_medio = consumo
        else:
            raise ValueError("Cantidad invalida")

    def set_num_tripulantes(self, num_tripulantes):
        if num_tripulantes > 0:
            self.__num_tripulantes = num_tripulantes
        else:
            raise ValueError("Cantidad invalida")

    # Metodos obligatorios
    def calculo_custe_consumo(self, dias: int, prezo: float) -> float:
        if dias < 0 or prezo < 0:
            raise ValueError("Datos invalidos")
        return self.__consumo_medio * dias * prezo

    def calculo_facturacion(self, prezo, millas, porcentaxe_ocupado):
        facturacion = prezo * millas * porcentaxe_ocupado/100
        return facturacion

    def __str__(self):
        return f"Barco\nNome: {self.__nome}\nMatricula: {self.__matricula}\nEslora: {self.__eslora}\nToneladas de carga: {self.__toneladas_carga}\nCalado: {self.__calado}\nPotencia: {self.__potencia}\nVelocidade: {self.__velocidade}\nConsumo medio: {self.__consumo_medio}\nNumero de tripulantes: {self.__num_tripulantes}"

class BarcoAuxiliar(Barco):
    def __init__(self, eslora, toneladas_carga, calado, potencia, velocidade, consumo_medio, nome, matricula, num_tripulantes, capacidade_conxelacion):

        super().__init__(eslora, toneladas_carga, calado, potencia, velocidade, consumo_medio, nome, matricula, num_tripulantes)

        self.set_capacidade_conxelacion(capacidade_conxelacion)

    def get_capacidade_conxelacion(self):
        return self.__capacidade_conxelacion

    def set_capacidade_conxelacion(self, capacidade):
        if capacidade > 0:
            self.__capacidade_conxelacion = capacidade
        else:
            raise ValueError("Cantidad invalida")

    def __str__(self):
        return f"Auxiliar: {super().__str__()} "


class BarcoAuxiliarFuel(BarcoAuxiliar):
    def __init__(self, eslora, toneladas_carga, calado, potencia, velocidade, consumo_medio, nome, matricula, num_tripulantes, capacidade_conxelacion, capacidade_fuel):

        super().__init__(eslora, toneladas_carga, calado, potencia, velocidade, consumo_medio, nome, matricula, num_tripulantes, capacidade_conxelacion)

        self.set_capacidade_fuel(capacidade_fuel)

    def get_capacidade_fuel(self):
        return self.__capacidade_fuel

    def set_capacidade_fuel(self, capacidade):
        if capacidade > 0:
            self.__capacidade_fuel = capacidade
        else:
            raise ValueError("Cantidad invalida")

    def __str__(self):
        return f"{super().__str__()}\nFuel: {self.__capacidade_fuel} "



'''
barco = BarcoAuxiliarFuel( 30, 200, 5, 1500, 20, 500,"Barco1", "ABC123", 15, 1000, 50000)

custe = barco.calculo_custe_consumo(30, 1.5)

print("SUPUESTO 1")
print(barco)
print()
print("Custe total:", custe, "€")
print()
'''



#2
#Codoficar o script que permita ler un ficheiro de tipo csv coa descricion dos asentos dunha liña aérea.
#O ficheiro tne como cabeceira os nomes das propiedades da clase e os campos o contido das seguintes liñas, separados por comas.
#A clase é a que se mostra a continuacion

import csv

class Asento:
    def __init__(self, numero: str, clase: str):
        self.numero = numero
        self.clase = clase
        self.ocupado = False
        self.pasaxeiro = None

    def leer_csv(self):
        asientos = []
        with open("asentos.csv", newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                numero = fila["numero"]
                clase = fila["clase"]
                asiento = Asento(numero, clase)
                asientos.append(asiento)
        print(f"Archivo .csv leído: {asientos}")
        return asientos

    def mostrar_csv(self):
        lista = []
        try:
            with open("asentos.csv", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()

                if not lineas:
                    print("No hay pasajeros guardados.")
                else:

                    for linea in lineas:
                        numero, clase, ocupado, pasaxeiro = linea.strip().split(",")

                        persona = (numero,clase,ocupado,pasaxeiro)
                        lista.append(persona)
                    return lista

        except FileNotFoundError:
            print("El archivo no existe todavía.")


    def __str__(self):
        return f"Asento: {self.numero} {self.clase}"

    def __abs__(self):
        return f"Asento: {self.numero} {self.clase}"

'''
asento = Asento(1,"business")
asento2 = Asento(2,"business")
print(Asento.leer_csv(asento))
print("SUPOSTO 2")

print(Asento.mostrar_csv(asento))
'''


#3
#Codifica o programa que permita xestionar os asentos dun avion. O programa permitira crear, buscar e ocupar un asento.
#Para crear os asentos o programa creara unha lista e solicitara o numero de asentos do avion, creando un numero igual de obxectos Asento cua propiedade ocupado igual a False. O programa reservará un 10% das prazas (os primeiros asentos) a "business", 20% seguintes prazas a "preferente", e o resto a "turista. Hay que ter en conta que o asento con numero 13 se ingorará (non se creará)
#O programa tera as seguintes opcion:
#Crecion dos asentos libres
#Achega na lista o primeri asento que estea libre da clase de viaxeiro que se lle especifique( turista, preferente, business), mostrando por pantalla o numero
#Ocupacion dun asento por un pasaxeiro dun asento libre, rexistrando o seu nome no asento correspondente

def crear_asentos(num_asentos):
    lista = []

    num_business = int(num_asentos * 0.10)
    num_preferente = int(num_asentos * 0.20)

    contador = 1

    while len(lista) < num_asentos:
        if contador == 13:
            contador += 1
            continue

        if len(lista) < num_business:
            clase = "business"
        elif len(lista) < num_business + num_preferente:
            clase = "preferente"
        else:
            clase = "turista"
        añadir = [contador,clase,False,None]
        lista.append(añadir)
        contador += 1
    return lista

def buscar_asento_libre(lista, clase):
    for asento in lista:
        if asento[1] == clase and not asento.ocupado:
            return asento
        else:
            return None

def ocupar_asento(lista, numero, nome_pasaxeiro):
    for asento in lista:
        print(asento[0])
        if asento[0] == numero:
            if asento[2] == False:
                asento[2] = True
                asento[3] = nome_pasaxeiro
                print("asignado")

        else:
            print("no asignado")

    print("Asento non atopado")
    return None

print("SUPOSTO 3")
asentos = crear_asentos(10)
print(asentos)

ocupar_asento(asentos, 2, "Ana Pérez")










#4
#Escribir un script que premita ler dende un ficheiro a ocupacion dun voo dun avion dunha compañia aérea. Cada liña estara representada por una liña co seguinte formato:
#"Asento: nnn clase nomeViaxeiro|libre"
#Onde:
#"nnn" e o numero de asento
#"clase" e a clase do viaxeiro (turista, preferente, business)
#"nomeviaxeiro|libre", pode aparecer o "nomeViaxeiro" si o asento esta ocupado, e "libre" si esta libre o asento
# Ler o ficheiro e cos datos extradiso de cada liña crear un obxecto Asento e engadilos a unha lista
#


def ler_ocupacion(ruta_ficheiro):
    lista = []

    with open(ruta_ficheiro, encoding='utf-8') as f:
        for liña in f:
            liña = liña.strip()

            # Eliminar "Asento:"
            contido = liña.replace("Asento:", "").strip()

            partes = contido.split()

            numero = partes[0]
            clase = partes[1]
            estado = " ".join(partes[2:])

            asento = Asento(numero, clase)

            if estado != "libre":
                asento.ocupado = True
                asento.pasaxeiro = estado

            lista.append(asento)

    return lista