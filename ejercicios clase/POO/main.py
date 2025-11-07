from punto import Punto
from circulo import Circulo
from persona import Persoa





p1 = Punto(2, 3)
p2 = Punto(9, 1)

print(p1.toString())
print(p2)












print(p1.x)

manuel = Persoa ( "Manuel",dni="00000000T", nacionalidad="Española",direccion="Su casa",edad=18)
manuela = Persoa ( "Manuela",dni="00000000T", nacionalidad="Española",direccion="Su casa",edad=21)
print(manuel)
print(manuela == manuel)
print(manuela > manuel)
print(manuela < manuel)