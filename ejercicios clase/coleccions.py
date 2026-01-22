









s = { 10, 15.5, "Vinte"}
s = set([20,30,40])
print(type(s))
print(s)
#print(s[1]) no funciona

s.add(40)
s.add(50)
s.update([80,90,70])
s.remove(70)

print(s)


fs = frozenset([3,4,5,6])
print(fs)
#fs.add(7) no se puede

print(fs.union(s))
print(s.intersection(fs))

elementoAleatorio = s.pop()
print(elementoAleatorio)


#comrpobaacion mas rapido q listas
n = {1,2,3,4,5}
print(3 in n)

#Achega de elementos unicos
l2 = [1,2,3,4,5]
l3 = [2,3,4]
print(set(l2)-set(l3))






# Condicional multiple match case

x = 40

if x == 10:
    print ("X e 10")
elif x == 20:
    print("X e 20")
elif x == 30:
    print("X e 30")

match x:
    case 10:
        print ("X e 10")
    case 20:
        print ("X e 20")
    case 30:
        print ("X e 30")
    case _:
        print("X non e 10, 20 ou 30")

match x:
    case 10|20|30:
        print (f"X e {x}")
    case _:
        print("X non e 10, 20 ou 30")

y = 20
match x:
    case 10 if y % 2 == 0:
        print("X e 10 e Y divisible entre 2")
    case 10:
        print("X e 10 e Y non divisible entre 2")
    case _:
        print ("Opcion desconocida")


l = [2, 3, 5]

match l:
    case (x, y):
        print (f"Coleccion con dous elementos {x}, {y}")
    case (x, y, z):
        print (f"Coleccion con los elementos {x}, {y}, {z}")
    case _:
        print ("Formato desconocido")

persoa = {"nome" : "Manuel" , "curso": "Dam"}


match persoa:
    case {"nome":nome,"curso":curso}:
        print (f"Nome : {nome}, Curso : {curso}.")
    case {"nome":nome}:
        print(f"Nome : {nome}")
    case _:
        print ("Formato desconocido")

class Figura:
    pass

class Circulo(Figura):
    def __init__(self, r):
        self.r = r

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

f = Circulo(15)

match f:
    case Circulo(r):
        print (f"Circulo con radio = {r}")
    case Rectangulo(ancho, alto):
        print(f"Rectangulo con ancho = {ancho}, alto = {alto}")
    case _:
        print ("Formato desconocido")




























