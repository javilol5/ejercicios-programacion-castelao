#1. Crea unha clase chamada Libro que conteña os seguintes atributos:
#titulo
#autor
#ano
#numPaginas
#valoracion
#
#
#A clase debe de ter o metodo de inicialización.
#Establecer os métodos de acceso para todos os atributos (geters).
#Crear os métodos de asignación dos atributos (seters)
#Establecer as propiedades de forma que só se poida acceder os atributos mediante os métodos adicados a elo (geters e seters).
#Codificar o metodo amosarLibro, que devolte unha cadea e visualiza tódalas característica dun libro.
#Crear unha clase Principal co metodo main. Crear un libro con cada construtor e mostrar por consola a súa información.



class Libro:
    def __init__(self, titulo, autor, ano, numpaginas, valoracion):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__numPaginas = numpaginas
        self.__valoracion = valoracion

    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getAno(self):
        return self.__ano
    def getNumPaginas(self):
        return self.__numPaginas
    def getValoracion(self):
        return self.__valoracion

    def setTitulo(self, titulo):
        self.__titulo = titulo
    def setAutor(self, autor):
        self.__autor = autor
    def setAno(self, ano):
        self.__ano = ano
    def setNumPaginas(self, numPaginas):
        self.__numPaginas = numPaginas
    def setValoracion(self, valoracion):
        self.__valoracion = valoracion

    def amosarLibro(self):
        return self.__titulo + ' ' + self.__autor + ' ' + str(self.__ano) + ' ' + str(self.__numPaginas) + ' ' + str(self.__valoracion)





