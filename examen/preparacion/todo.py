# ============================================================
# ÍNDICE COMPLETO ORDENADO POR TEMAS (USAR CTRL + F)
# ============================================================


# ============================================================
# 🟦 1. PYTHON BÁSICO
# ============================================================

# VARIABLES
# TIPOS DE DATOS
# CASTING

# STRINGS — MÉTODOS
# STRINGS — SLICING
# STRINGS — FORMATEO

# LISTAS — MÉTODOS
# LISTAS — RECORRER
# LISTAS — COMPREHENSION

# TUPLAS — INMUTABILIDAD
# TUPLAS — DESEMPAQUETADO

# DICCIONARIOS — MÉTODOS
# DICCIONARIOS — RECORRER

# SETS — OPERACIONES

# IF / ELSE / ELIF
# OPERADORES LÓGICOS

# FOR
# WHILE
# BREAK / CONTINUE
# RANGE

# FUNCIONES — PARÁMETROS
# FUNCIONES — RETURN
# FUNCIONES — *ARGS / **KWARGS
# FUNCIONES — RECURSIVIDAD

# TRY / EXCEPT
# TRY / EXCEPT / FINALLY
# RAISE — LANZAR EXCEPCIONES

# FICHEROS — LECTURA
# FICHEROS — ESCRITURA
# FICHEROS — CSV
# FICHEROS — GUARDAR OBJETOS


# ============================================================
# 🟦 2. PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# ============================================================

# CLASES
# OBJETOS
# MÉTODOS
# CONSTRUCTORES (__init__)
# ENCAPSULACIÓN
# HERENCIA
# POLIMORFISMO
# COMPOSICIÓN
# RELACIONES ENTRE CLASES


# ============================================================
# 🟦 3. SISTEMAS DE BIBLIOTECAS (MUY COMÚN EN EXÁMENES)
# ============================================================

# Biblioteca municipal
# Biblioteca escolar
# Biblioteca digital
# Biblioteca de arte
# Biblioteca de videojuegos
# Biblioteca de música
# Biblioteca de películas
# Biblioteca de cursos
# Biblioteca de libros antiguos
# Biblioteca de recetas
# Biblioteca de eventos
# Biblioteca de conferencias
# Biblioteca de documentos empresariales


# ============================================================
# 🟦 4. SISTEMAS DE CURSOS / EDUCACIÓN
# ============================================================

# Cursos online
# Cursos presenciales
# Cursos con módulos y lecciones
# Cursos con exámenes
# Cursos con certificados
# Cursos con tareas y entregas
# Cursos con foros y mensajes
# Universidad completa


# ============================================================
# 🟦 5. SISTEMAS DE EMPRESAS / NEGOCIOS
# ============================================================

# Empresa con empleados y departamentos
# Empresa con proyectos y tareas
# Empresa con nóminas
# Empresa de transporte
# Empresa de envíos
# Empresa de reparaciones
# Empresa de logística
# Empresa de alquiler de vehículos
# Empresa de productos y proveedores
# Empresa de restauración de libros antiguos


# ============================================================
# 🟦 6. SISTEMAS DE TIENDAS / INVENTARIOS
# ============================================================

# Tienda online
# Tienda con categorías
# Tienda con proveedores
# Inventario multialmacén
# Inventario con reposición automática
# Centro comercial
# Sistema de pedidos
# Facturación


# ============================================================
# 🟦 7. SISTEMAS DE RESTAURANTES / HOSTELERÍA
# ============================================================

# Restaurante con mesas y pedidos
# Restaurante con cocina
# Restaurante con facturas
# Hotel completo
# Red de hoteles


# ============================================================
# 🟦 8. SISTEMAS DE SALUD / CLÍNICAS / VETERINARIA
# ============================================================

# Clínica médica
# Hospital con diagnósticos
# Veterinaria con citas
# Veterinaria con tratamientos


# ============================================================
# 🟦 9. SISTEMAS DE TRANSPORTE / LOGÍSTICA
# ============================================================

# Aerolínea completa
# Empresa de transporte
# Empresa de envíos
# Logística con rutas
# Logística con informes
# Envíos con estados
# Rutas y vehículos


# ============================================================
# 🟦 10. SISTEMAS DE EVENTOS / OCIO
# ============================================================

# Conferencias con charlas
# Eventos con aforo
# Tickets con prioridad
# Sistema de entradas


# ============================================================
# 🟦 11. SISTEMAS TÉCNICOS / AVANZADOS
# ============================================================

# Árbol binario de búsqueda
# Colisiones 2D
# Colas paralelas
# Logs rotativos
# Motor de plantillas
# Versionador con rollback
# Dependencias con detección de ciclos
# Métricas
# Configuración tipo INI


# ============================================================
# 🟦 12. PACKS DE EJERCICIOS LARGOS (ÍNDICE GENERAL)
# ============================================================

# PACK 1 — Ejercicios combinados avanzados
# PACK 2 — Mini‑proyectos
# PACK 3 — Ejercicios largos avanzados
# PACK 4 — Ejercicios largos diferentes
# PACK 5 — Ejercicios muy completos
# PACK 6 — Nivel examen
# PACK 7 — Probables en examen
# PACK 8 — Distintos
# PACK 9 — Extra
# PACK 10 — Adicionales
# PACK 11 — Nuevos
# PACK 12 — Recientes
# PACK 13 — Conferencias, cursos, tiendas, hospital, etc.

# ============================================================
# TEMA 1 — BUCLES
# ============================================================

# EJERCICIO 1 — Pares del 100 al 0
for n in range(100, -1, -2):
    print(n)

# EJERCICIO 2 — Suma del 1 al 100
suma = 0
for n in range(1, 101):
    suma += n
print(suma)

# EJERCICIO 3 — Contar negativos introducidos
neg = 0
n = float(input("Número (0 para salir): "))
while n != 0:
    if n < 0:
        neg += 1
    n = float(input("Número (0 para salir): "))
print(neg)

# EJERCICIO 4 — Tabla de multiplicar
num = int(input("Número: "))
for i in range(1, 11):
    print(num * i)

# EJERCICIO 5 — Contar pares entre 1 y 100
pares = 0
for n in range(1, 101):
    if n % 2 == 0:
        pares += 1
print(pares)

# EJERCICIO 6 — Sumar números hasta superar 200
suma = 0
while suma <= 200:
    suma += float(input("Número: "))
print(suma)

# EJERCICIO 7 — Mostrar números del 50 al 0
for n in range(50, -1, -1):
    print(n)

# EJERCICIO 8 — Mayor de 10 números
mayor = None
for _ in range(10):
    n = float(input("Número: "))
    if mayor is None or n > mayor:
        mayor = n
print(mayor)

# EJERCICIO 9 — Contar números mayores de 50
cont = 0
for _ in range(10):
    if float(input("Número: ")) > 50:
        cont += 1
print(cont)

# EJERCICIO 10 — Media de 5 números
suma = 0
for _ in range(5):
    suma += float(input("Número: "))
print(suma / 5)

# EJERCICIO 11 — Impares del 1 al 50
for n in range(1, 51, 2):
    print(n)

# EJERCICIO 12 — Contraseña con 3 intentos
pwd = "python"
for i in range(3):
    if input("Contraseña: ") == pwd:
        print("Correcta")
        break
else:
    print("Bloqueado")

# EJERCICIO 13 — Contar múltiplos de 3
cont = 0
for n in range(1, 101):
    if n % 3 == 0:
        cont += 1
print(cont)

# EJERCICIO 14 — Mostrar números hasta negativo
n = float(input("Número: "))
while n >= 0:
    print(n)
    n = float(input("Número: "))

# EJERCICIO 15 — Cuadrados del 1 al 20
for n in range(1, 21):
    print(n ** 2)

# EJERCICIO 16 — Cuenta atrás
for n in range(10, 0, -1):
    print(n)
print("¡Despegue!")

# EJERCICIO 17 — Suma de 10 números
suma = 0
for _ in range(10):
    suma += float(input("Número: "))
print(suma)

# EJERCICIO 18 — Recorrer string
for letra in "Python":
    print(letra)

# EJERCICIO 19 — Múltiplos de 5 hasta 30
for n in range(1, 31):
    if n % 5 == 0:
        print(n)

# EJERCICIO 20 — Factorial del 5
total = 1
for n in range(1, 6):
    total *= n
print(total)

# EJERCICIO 21 — Múltiplos de 7 hasta 50
for n in range(1, 51):
    if n % 7 == 0:
        print(n)

# EJERCICIO 22 — Par o impar del 1 al 20
for n in range(1, 21):
    print(n, "par" if n % 2 == 0 else "impar")

# EJERCICIO 23 — Triángulo creciente
for n in range(1, 11):
    print("*" * n)

# EJERCICIO 24 — Triángulo decreciente
for n in range(10, 0, -1):
    print("*" * n)

# EJERCICIO 25 — Sumar hasta número negativo
suma = 0
n = float(input("Número: "))
while n >= 0:
    suma += n
    n = float(input("Número: "))
print(suma)

# EJERCICIO 26 — Múltiplos de 4 y 6
for n in range(1, 101):
    if n % 4 == 0 and n % 6 == 0:
        print(n)

# EJERCICIO 27 — Cubos del 1 al 10
for n in range(1, 11):
    print(n ** 3)

# EJERCICIO 28 — Números que terminan en 5
for n in range(1, 101):
    if str(n).endswith("5"):
        print(n)

# EJERCICIO 29 — Saltar 5, 10 y 15
for n in range(1, 21):
    if n not in (5, 10, 15):
        print(n)

# EJERCICIO 30 — Doble bucle (matriz 5x5)
for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)

# ============================================================
# TEMA 2 — LISTAS
# ============================================================

# EJERCICIO 1 — Añadir 5 nombres a una lista
nombres = []
for _ in range(5):
    nombres.append(input("Nombre: "))
print(nombres)

# EJERCICIO 2 — Contar cuántas veces aparece un número
lista = [1, 2, 3, 2, 4, 2, 5]
print(lista.count(2))

# EJERCICIO 3 — Eliminar duplicados
lista = [1, 2, 2, 3, 4, 4, 5]
lista = list(set(lista))
print(lista)

# EJERCICIO 4 — Sumar todos los elementos
lista = [10, 20, 30, 40]
print(sum(lista))

# EJERCICIO 5 — Crear lista con números pares del 1 al 50
pares = [n for n in range(1, 51) if n % 2 == 0]
print(pares)

# EJERCICIO 6 — Buscar un producto en la lista
lista = ["pan", "leche", "huevos"]
producto = input("Producto: ")
print("Está" if producto in lista else "No está")

# EJERCICIO 7 — Invertir una lista sin reverse()
lista = [1, 2, 3, 4, 5]
print(lista[::-1])

# EJERCICIO 8 — Filtrar números mayores de 10
lista = [5, 12, 3, 20, 7]
print([n for n in lista if n > 10])

# EJERCICIO 9 — Multiplicar cada elemento por 2
lista = [1, 2, 3]
print([n * 2 for n in lista])

# EJERCICIO 10 — Obtener índices donde aparece un valor
lista = [1, 2, 3, 2, 4, 2]
indices = [i for i, v in enumerate(lista) if v == 2]
print(indices)

# EJERCICIO 11 — Ordenar una lista
lista = [5, 3, 8, 1]
lista.sort()
print(lista)

# EJERCICIO 12 — Insertar un elemento en posición concreta
lista = [1, 2, 3]
lista.insert(1, 99)
print(lista)

# EJERCICIO 13 — Eliminar por índice
lista = [10, 20, 30]
lista.pop(1)
print(lista)

# EJERCICIO 14 — Crear lista de cuadrados del 1 al 10
print([n * n for n in range(1, 11)])

# EJERCICIO 15 — Sumar solo los pares de una lista
lista = [1, 2, 3, 4, 5, 6]
print(sum(n for n in lista if n % 2 == 0))

# EJERCICIO 16 — Lista de longitudes de palabras
palabras = ["python", "java", "c++"]
print([len(p) for p in palabras])

# EJERCICIO 17 — Eliminar todos los ceros
lista = [0, 1, 0, 2, 0, 3]
print([n for n in lista if n != 0])

# EJERCICIO 18 — Reemplazar negativos por 0
lista = [-5, 3, -1, 7]
print([0 if n < 0 else n for n in lista])

# EJERCICIO 19 — Concatenar dos listas
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# EJERCICIO 20 — Repetir lista 3 veces
lista = [1, 2]
print(lista * 3)

# EJERCICIO 21 — Lista de números del 1 al 20 saltando de 3 en 3
print(list(range(1, 21, 3)))

# EJERCICIO 22 — Eliminar el último elemento
lista = [1, 2, 3, 4]
lista.pop()
print(lista)

# EJERCICIO 23 — Convertir lista de strings a mayúsculas
lista = ["hola", "python", "dam"]
print([s.upper() for s in lista])

# EJERCICIO 24 — Lista con números impares del 1 al 30
print([n for n in range(1, 31) if n % 2 != 0])

# EJERCICIO 25 — Lista de divisores de un número
num = 12
print([n for n in range(1, num + 1) if num % n == 0])

# EJERCICIO 26 — Lista de palabras que empiezan por 'a'
palabras = ["ana", "python", "avion", "casa"]
print([p for p in palabras if p.startswith("a")])

# EJERCICIO 27 — Lista de números entre 1 y 100 que terminan en 7
print([n for n in range(1, 101) if str(n).endswith("7")])

# EJERCICIO 28 — Lista de números entre 1 y 50 que no son múltiplos de 3
print([n for n in range(1, 51) if n % 3 != 0])

# EJERCICIO 29 — Lista de pares e impares por separado
lista = [1, 2, 3, 4, 5, 6]
pares = [n for n in lista if n % 2 == 0]
impares = [n for n in lista if n % 2 != 0]
print(pares, impares)

# EJERCICIO 30 — Lista de 10 números introducidos por el usuario
lista = []
for _ in range(10):
    lista.append(float(input("Número: ")))
print(lista)

# ============================================================
# TEMA 3 — TUPLAS
# ============================================================

# EJERCICIO 1 — Crear tupla con 5 números
t = (1, 2, 3, 4, 5)
print(t)

# EJERCICIO 2 — Desempaquetado de tupla
a, b, c, d, e = t
print(a, b, c, d, e)

# EJERCICIO 3 — Función que devuelve una tupla
def datos():
    return "Ana", 20, "España"
print(datos())

# EJERCICIO 4 — Contar cuántas veces aparece un valor
t = (1, 2, 2, 3, 4, 2)
print(t.count(2))

# EJERCICIO 5 — Convertir tupla a lista
t = (1, 2, 3)
lista = list(t)
print(lista)

# EJERCICIO 6 — Obtener índice de un elemento
t = ("a", "b", "c", "d")
print(t.index("c"))

# EJERCICIO 7 — Comprobar si un elemento está en la tupla
t = (10, 20, 30)
print(20 in t)

# EJERCICIO 8 — Tupla de strings
t = ("python", "java", "c++")
print(t)

# EJERCICIO 9 — Sumar dos tuplas
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

# EJERCICIO 10 — Repetir tupla 3 veces
t = (1, 2)
print(t * 3)

# EJERCICIO 11 — Longitud de una tupla
t = (1, 2, 3, 4)
print(len(t))

# EJERCICIO 12 — Máximo y mínimo
t = (5, 1, 9, 3)
print(max(t), min(t))

# EJERCICIO 13 — Ordenar tupla
t = (5, 3, 8, 1)
print(tuple(sorted(t)))

# EJERCICIO 14 — Crear tupla con números del 1 al 10
t = tuple(range(1, 11))
print(t)

# EJERCICIO 15 — Tupla con mezcla de tipos
t = ("Ana", 20, 1.75, True)
print(t)

# EJERCICIO 16 — Acceder al último elemento
t = (1, 2, 3, 4)
print(t[-1])

# EJERCICIO 17 — Slicing de tupla
t = (1, 2, 3, 4, 5, 6)
print(t[1:4])

# EJERCICIO 18 — Tupla de caracteres de una palabra
t = tuple("Python")
print(t)

# EJERCICIO 19 — Crear tupla con números pares del 1 al 20
t = tuple(n for n in range(1, 21) if n % 2 == 0)
print(t)

# EJERCICIO 20 — Crear tupla con cuadrados del 1 al 10
t = tuple(n * n for n in range(1, 11))
print(t)

# EJERCICIO 21 — Concatenar tupla con sí misma
t = (1, 2, 3)
print(t + t)

# EJERCICIO 22 — Repetir elementos según su valor
t = (1, 2, 3)
print(tuple(n for n in t for _ in range(n)))

# EJERCICIO 23 — Convertir lista de listas en tupla de tuplas
lista = [[1, 2], [3, 4]]
t = tuple(tuple(x) for x in lista)
print(t)

# EJERCICIO 24 — Crear tupla con números que terminan en 5
t = tuple(n for n in range(1, 101) if str(n).endswith("5"))
print(t)

# EJERCICIO 25 — Crear tupla con divisores de un número
num = 12
t = tuple(n for n in range(1, num + 1) if num % n == 0)
print(t)

# EJERCICIO 26 — Tupla con palabras que empiezan por vocal
palabras = ("ana", "python", "uva", "casa", "oso")
t = tuple(p for p in palabras if p[0] in "aeiou")
print(t)

# EJERCICIO 27 — Tupla con números no múltiplos de 3
t = tuple(n for n in range(1, 31) if n % 3 != 0)
print(t)

# EJERCICIO 28 — Tupla con longitudes de palabras
palabras = ("python", "java", "c++")
t = tuple(len(p) for p in palabras)
print(t)

# EJERCICIO 29 — Tupla con números del 1 al 20 en orden inverso
t = tuple(range(20, 0, -1))
print(t)

# EJERCICIO 30 — Tupla con pares e impares por separado
numeros = (1, 2, 3, 4, 5, 6)
pares = tuple(n for n in numeros if n % 2 == 0)
impares = tuple(n for n in numeros if n % 2 != 0)
print(pares, impares)

# ============================================================
# TEMA 4 — STRINGS
# ============================================================

# EJERCICIO 1 — Invertir una cadena
texto = "Python"
print(texto[::-1])

# EJERCICIO 2 — Contar vocales
texto = "programacion"
vocales = sum(1 for c in texto if c in "aeiou")
print(vocales)

# EJERCICIO 3 — Quitar espacios al inicio y final
texto = "  hola mundo  "
print(texto.strip())

# EJERCICIO 4 — Reemplazar letras
print("java java".replace("a", "e"))

# EJERCICIO 5 — Convertir frase en lista de palabras
frase = "Python es genial"
print(frase.split())

# EJERCICIO 6 — Comprobar si empieza por "py"
texto = "python"
print(texto.startswith("py"))

# EJERCICIO 7 — Slicing básico
texto = "ABCDEFGHIJK"
print(texto[2:10:2])

# EJERCICIO 8 — Contar palabras en una frase
frase = "hola que tal estas"
print(len(frase.split()))

# EJERCICIO 9 — Convertir a mayúsculas
print("hola".upper())

# EJERCICIO 10 — Convertir a minúsculas
print("HOLA".lower())

# EJERCICIO 11 — Quitar vocales
texto = "programacion"
print("".join(c for c in texto if c not in "aeiou"))

# EJERCICIO 12 — Repetir string
print("ha" * 5)

# EJERCICIO 13 — Comprobar si es numérico
print("12345".isdigit())

# EJERCICIO 14 — Reemplazar espacios por guiones
print("hola mundo python".replace(" ", "-"))

# EJERCICIO 15 — Contar cuántas veces aparece una letra
texto = "banana"
print(texto.count("a"))

# EJERCICIO 16 — Obtener la primera palabra
frase = "Python es divertido"
print(frase.split()[0])

# EJERCICIO 17 — Obtener la última palabra
print(frase.split()[-1])

# EJERCICIO 18 — Convertir cada palabra a mayúsculas
frase = "python es genial"
print([p.upper() for p in frase.split()])

# EJERCICIO 19 — Comprobar si contiene una palabra
frase = "me gusta programar en python"
print("python" in frase)

# EJERCICIO 20 — Reemplazar todas las vocales por "*"
texto = "programacion"
print("".join("*" if c in "aeiou" else c for c in texto))

# EJERCICIO 21 — Mostrar caracteres con su índice
texto = "Python"
for i, c in enumerate(texto):
    print(i, c)

# EJERCICIO 22 — Invertir cada palabra de una frase
frase = "hola mundo python"
print(" ".join(p[::-1] for p in frase.split()))

# EJERCICIO 23 — Contar mayúsculas
texto = "PyThOn"
print(sum(1 for c in texto if c.isupper()))

# EJERCICIO 24 — Contar minúsculas
print(sum(1 for c in texto if c.islower()))

# EJERCICIO 25 — Eliminar números de un string
texto = "a1b2c3d4"
print("".join(c for c in texto if not c.isdigit()))

# EJERCICIO 26 — Dejar solo números
print("".join(c for c in texto if c.isdigit()))

# EJERCICIO 27 — Alternar mayúsculas y minúsculas
texto = "python"
print("".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(texto)))

# EJERCICIO 28 — Comprobar si es palíndromo
texto = "radar"
print(texto == texto[::-1])

# EJERCICIO 29 — Insertar guiones entre caracteres
texto = "python"
print("-".join(texto))

# EJERCICIO 30 — Contar cuántas palabras empiezan por vocal
frase = "ana estudia en una universidad"
print(sum(1 for p in frase.split() if p[0] in "aeiou"))

# ============================================================
# TEMA 5 — PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# ============================================================

# EJERCICIO 1 — Clase Persona con método saludar
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre}"

p = Persona("Ana", 20)
print(p.saludar())


# EJERCICIO 2 — Clase Coche con velocidad máxima usando property
class Coche:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, v):
        if v > 120:
            v = 120
        self._velocidad = v

c = Coche(200)
print(c.velocidad)


# EJERCICIO 3 — Clase Animal y Perro (herencia)
class Animal:
    def sonido(self):
        return "Sonido"

class Perro(Animal):
    def sonido(self):
        return "Guau"

print(Perro().sonido())


# EJERCICIO 4 — Clase con contador de objetos
class Contador:
    total = 0
    def __init__(self):
        Contador.total += 1

a = Contador()
b = Contador()
print(Contador.total)


# EJERCICIO 5 — Método estático
class Matematicas:
    @staticmethod
    def sumar(a, b):
        return a + b

print(Matematicas.sumar(5, 7))


# EJERCICIO 6 — Composición (Coche con Motor)
class Motor:
    def arrancar(self):
        return "Motor encendido"

class Coche2:
    def __init__(self):
        self.motor = Motor()

c = Coche2()
print(c.motor.arrancar())


# EJERCICIO 7 — Setter con validación (nota 0-10)
class Alumno:
    def __init__(self, nota):
        self.nota = nota

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, n):
        if n < 0 or n > 10:
            raise ValueError("Nota inválida")
        self._nota = n

a = Alumno(8)
print(a.nota)


# EJERCICIO 8 — Clase Libro con __str__
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

    def __str__(self):
        return f"Libro: {self.titulo}"

print(Libro("Python"))


# EJERCICIO 9 — Clase Agenda con lista interna
class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir(self, nombre):
        self.contactos.append(nombre)

ag = Agenda()
ag.añadir("Ana")
print(ag.contactos)


# EJERCICIO 10 — Método de clase
class Ejemplo:
    contador = 0

    @classmethod
    def incrementar(cls):
        cls.contador += 1

Ejemplo.incrementar()
Ejemplo.incrementar()
print(Ejemplo.contador)


# EJERCICIO 11 — Clase con método privado
class Secreto:
    def __oculto(self):
        return "Secreto"

    def mostrar(self):
        return self.__oculto()

s = Secreto()
print(s.mostrar())


# EJERCICIO 12 — Clase Producto con varios atributos
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

p = Producto("Pan", 1.20)
print(p.nombre, p.precio)


# EJERCICIO 13 — Clase Usuario con validación de edad
class Usuario:
    def __init__(self, nombre, edad):
        if edad < 0:
            raise ValueError("Edad inválida")
        self.nombre = nombre
        self.edad = edad

u = Usuario("Ana", 22)
print(u.nombre)


# EJERCICIO 14 — Clase Rectángulo con área
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

r = Rectangulo(4, 5)
print(r.area())


# EJERCICIO 15 — Clase CuentaBancaria con depósito y retiro
class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad

c = CuentaBancaria(100)
c.depositar(50)
c.retirar(30)
print(c.saldo)


# EJERCICIO 16 — Clase Estudiante con promedio
class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)

e = Estudiante("Ana", [5, 7, 9])
print(e.promedio())


# EJERCICIO 17 — Clase Punto con distancia entre puntos
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro):
        return ((self.x - otro.x)**2 + (self.y - otro.y)**2)**0.5

p1 = Punto(0, 0)
p2 = Punto(3, 4)
print(p1.distancia(p2))


# EJERCICIO 18 — Clase Empleado con aumento de sueldo
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def aumentar(self, porcentaje):
        self.sueldo += self.sueldo * porcentaje / 100

emp = Empleado("Ana", 1000)
emp.aumentar(10)
print(emp.sueldo)


# EJERCICIO 19 — Clase Fracción con suma
class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def sumar(self, otra):
        num = self.num * otra.den + otra.num * self.den
        den = self.den * otra.den
        return Fraccion(num, den)

f1 = Fraccion(1, 2)
f2 = Fraccion(1, 3)
res = f1.sumar(f2)
print(res.num, res.den)


# EJERCICIO 20 — Clase Persona con __eq__
class Persona2:
    def __init__(self, dni):
        self.dni = dni

    def __eq__(self, otro):
        return self.dni == otro.dni

print(Persona2("123") == Persona2("123"))


# EJERCICIO 21 — Clase Caja con volumen
class Caja:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volumen(self):
        return self.a * self.b * self.c

print(Caja(2, 3, 4).volumen())


# EJERCICIO 22 — Clase Temporizador con cuenta atrás
class Temporizador:
    def __init__(self, tiempo):
        self.tiempo = tiempo

    def tick(self):
        if self.tiempo > 0:
            self.tiempo -= 1

t = Temporizador(5)
t.tick()
print(t.tiempo)


# EJERCICIO 23 — Clase Persona con nombre completo
class Persona3:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

print(Persona3("Ana", "López").nombre_completo())


# EJERCICIO 24 — Clase Termómetro con límites
class Termometro:
    def __init__(self, temp):
        self.temp = temp

    def subir(self, grados):
        self.temp += grados

    def bajar(self, grados):
        self.temp -= grados

t = Termometro(20)
t.subir(5)
print(t.temp)


# EJERCICIO 25 — Clase Carrito con productos
class Carrito:
    def __init__(self):
        self.productos = []

    def agregar(self, p):
        self.productos.append(p)

car = Carrito()
car.agregar("Pan")
print(car.productos)


# EJERCICIO 26 — Clase Cuenta con transferencia
class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def transferir(self, otra, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            otra.saldo += cantidad

c1 = Cuenta(100)
c2 = Cuenta(50)
c1.transferir(c2, 30)
print(c1.saldo, c2.saldo)


# EJERCICIO 27 — Clase Alumno con aprobado/suspenso
class Alumno2:
    def __init__(self, nota):
        self.nota = nota

    def aprobado(self):
        return self.nota >= 5

print(Alumno2(7).aprobado())


# EJERCICIO 28 — Clase Reloj con avance de hora
class Reloj:
    def __init__(self, hora):
        self.hora = hora

    def avanzar(self):
        self.hora = (self.hora + 1) % 24

r = Reloj(23)
r.avanzar()
print(r.hora)


# EJERCICIO 29 — Clase Inventario con búsqueda
class Inventario:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.append(item)

    def buscar(self, item):
        return item in self.items

inv = Inventario()
inv.agregar("Teclado")
print(inv.buscar("Teclado"))


# EJERCICIO 30 — Clase Banco con varias cuentas
class Banco:
    def __init__(self):
        self.cuentas = []

    def agregar(self, cuenta):
        self.cuentas.append(cuenta)

b = Banco()
b.agregar(Cuenta(100))
print(len(b.cuentas))

# ============================================================
# TEMA 6 — EXCEPCIONES
# ============================================================

# EJERCICIO 1 — División segura
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error: división entre cero")

# EJERCICIO 2 — Validar número entero
while True:
    try:
        n = int(input("Número entero: "))
        break
    except ValueError:
        print("Error: no es un entero")

# EJERCICIO 3 — Excepción personalizada
class MesError(Exception):
    pass

def validar_mes(m):
    if m < 1 or m > 12:
        raise MesError("Mes inválido")

# EJERCICIO 4 — raise manual
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Prohibido dividir entre cero")
    return a / b

# EJERCICIO 5 — Bloque finally
try:
    print(10 / 2)
finally:
    print("Fin del programa")

# EJERCICIO 6 — Múltiples except
try:
    x = int("hola")
except ValueError:
    print("Error: no se puede convertir")

# EJERCICIO 7 — try dentro de while
while True:
    try:
        edad = int(input("Edad: "))
        break
    except:
        print("Edad inválida")

# EJERCICIO 8 — Convertir string a número
try:
    n = float("abc")
except:
    print("No se puede convertir")

# EJERCICIO 9 — Abrir fichero inexistente
try:
    open("noexiste.txt")
except FileNotFoundError:
    print("Archivo no encontrado")

# EJERCICIO 10 — Índice fuera de rango
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError:
    print("Índice inválido")

# EJERCICIO 11 — Clave inexistente en diccionario
try:
    d = {"a": 1}
    print(d["b"])
except KeyError:
    print("Clave no encontrada")

# EJERCICIO 12 — Tipo incorrecto
try:
    print(5 + "hola")
except TypeError:
    print("Tipos incompatibles")

# EJERCICIO 13 — Convertir lista a entero
try:
    int([1, 2, 3])
except:
    print("No se puede convertir")

# EJERCICIO 14 — Validar mes con raise
def validar_mes2(m):
    if m < 1 or m > 12:
        raise ValueError("Mes fuera de rango")

# EJERCICIO 15 — Leer número positivo
while True:
    try:
        n = int(input("Número positivo: "))
        if n < 0:
            raise ValueError
        break
    except:
        print("Error: debe ser positivo")

# EJERCICIO 16 — División con varios errores
try:
    a = int(input("A: "))
    b = int(input("B: "))
    print(a / b)
except ValueError:
    print("Debes escribir números")
except ZeroDivisionError:
    print("No se puede dividir entre cero")

# EJERCICIO 17 — Conversión segura a float
def convertir_float(x):
    try:
        return float(x)
    except:
        return None

print(convertir_float("3.14"))
print(convertir_float("abc"))

# EJERCICIO 18 — Leer archivo con manejo de errores
try:
    with open("archivo.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("No existe el archivo")

# EJERCICIO 19 — Forzar excepción personalizada
class ErrorEdad(Exception):
    pass

def validar_edad(e):
    if e < 0:
        raise ErrorEdad("Edad negativa")

# EJERCICIO 20 — Manejar error de conversión
try:
    n = int("12a")
except:
    print("Conversión inválida")

# EJERCICIO 21 — Manejar error de división múltiple
try:
    x = 10
    y = int(input("Divisor: "))
    print(x / y)
except Exception as e:
    print("Error:", e)

# EJERCICIO 22 — Validar contraseña con excepción
def validar_pwd(p):
    if len(p) < 5:
        raise ValueError("Contraseña demasiado corta")

try:
    validar_pwd("abc")
except ValueError as e:
    print(e)

# EJERCICIO 23 — Leer número entre 1 y 10
while True:
    try:
        n = int(input("Número 1-10: "))
        if not 1 <= n <= 10:
            raise ValueError
        break
    except:
        print("Número inválido")

# EJERCICIO 24 — Manejar error en lista vacía
try:
    lista = []
    print(lista[0])
except IndexError:
    print("La lista está vacía")

# EJERCICIO 25 — Manejar error en división de strings
try:
    print("hola" / 2)
except:
    print("Operación inválida")

# EJERCICIO 26 — Validar email simple
def validar_email(e):
    if "@" not in e:
        raise ValueError("Email inválido")

try:
    validar_email("correo.com")
except ValueError as e:
    print(e)

# EJERCICIO 27 — Manejar error en conversión de booleano
try:
    print(bool("Truee"))
except:
    print("Error booleano")

# EJERCICIO 28 — Manejar error en acceso a atributo
class A:
    pass

a = A()
try:
    print(a.x)
except AttributeError:
    print("Atributo inexistente")

# EJERCICIO 29 — Manejar error en suma de tipos
try:
    print([1, 2] + 3)
except:
    print("No se pueden sumar esos tipos")

# EJERCICIO 30 — Manejar error en int(None)
try:
    int(None)
except:
    print("No se puede convertir None")

# ============================================================
# TEMA 7 — FICHEROS
# ============================================================

# EJERCICIO 1 — Escribir en un fichero
with open("datos.txt", "w", encoding="utf-8") as f:
    f.write("Hola mundo\n")

# EJERCICIO 2 — Leer un fichero completo
with open("datos.txt", "r", encoding="utf-8") as f:
    print(f.read())

# EJERCICIO 3 — Añadir texto a un fichero
with open("datos.txt", "a", encoding="utf-8") as f:
    f.write("Nueva línea añadida\n")

# EJERCICIO 4 — Leer línea a línea
with open("datos.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())

# EJERCICIO 5 — Crear fichero si no existe (modo a+)
with open("nuevo.txt", "a+", encoding="utf-8") as f:
    f.write("Creado automáticamente\n")

# EJERCICIO 6 — Guardar lista con pickle
import pickle
lista = ["A", "B", "C"]
with open("lista.dat", "wb") as f:
    pickle.dump(lista, f)

# EJERCICIO 7 — Leer lista con pickle
try:
    with open("lista.dat", "rb") as f:
        datos = pickle.load(f)
        print(datos)
except FileNotFoundError:
    print("No existe el archivo")

# EJERCICIO 8 — Contar líneas de un fichero
with open("datos.txt", "r", encoding="utf-8") as f:
    print(len(f.readlines()))

# EJERCICIO 9 — Copiar contenido de un fichero a otro
with open("datos.txt", "r", encoding="utf-8") as f1, open("copia.txt", "w", encoding="utf-8") as f2:
    f2.write(f1.read())

# EJERCICIO 10 — Escribir lista en un fichero
lista = ["uno", "dos", "tres"]
with open("lista.txt", "w", encoding="utf-8") as f:
    for item in lista:
        f.write(item + "\n")

# EJERCICIO 11 — Leer lista desde fichero
with open("lista.txt", "r", encoding="utf-8") as f:
    lista = [linea.strip() for linea in f]
print(lista)

# EJERCICIO 12 — Buscar palabra en un fichero
with open("datos.txt", "r", encoding="utf-8") as f:
    for linea in f:
        if "Hola" in linea:
            print("Encontrado")

# EJERCICIO 13 — Contar caracteres de un fichero
with open("datos.txt", "r", encoding="utf-8") as f:
    print(len(f.read()))

# EJERCICIO 14 — Escribir números del 1 al 10 en un fichero
with open("numeros.txt", "w", encoding="utf-8") as f:
    for n in range(1, 11):
        f.write(str(n) + "\n")

# EJERCICIO 15 — Leer números y sumarlos
with open("numeros.txt", "r", encoding="utf-8") as f:
    print(sum(int(linea) for linea in f))

# EJERCICIO 16 — Crear fichero vacío
open("vacio.txt", "w").close()

# EJERCICIO 17 — Escribir diccionario en fichero
d = {"nombre": "Ana", "edad": 20}
with open("diccionario.txt", "w", encoding="utf-8") as f:
    for k, v in d.items():
        f.write(f"{k}:{v}\n")

# EJERCICIO 18 — Leer diccionario desde fichero
dic = {}
with open("diccionario.txt", "r", encoding="utf-8") as f:
    for linea in f:
        k, v = linea.strip().split(":")
        dic[k] = v
print(dic)

# EJERCICIO 19 — Escribir 100 números en un fichero
with open("cien.txt", "w", encoding="utf-8") as f:
    for n in range(1, 101):
        f.write(str(n) + "\n")

# EJERCICIO 20 — Leer solo las primeras 5 líneas
with open("cien.txt", "r", encoding="utf-8") as f:
    for _ in range(5):
        print(f.readline().strip())

# EJERCICIO 21 — Contar cuántas líneas contienen una palabra
cont = 0
with open("datos.txt", "r", encoding="utf-8") as f:
    for linea in f:
        if "Hola" in linea:
            cont += 1
print(cont)

# EJERCICIO 22 — Escribir lista de números al cuadrado
with open("cuadrados.txt", "w", encoding="utf-8") as f:
    for n in range(1, 21):
        f.write(str(n*n) + "\n")

# EJERCICIO 23 — Leer fichero y mostrar solo líneas pares
with open("datos.txt", "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, start=1):
        if i % 2 == 0:
            print(linea.strip())

# EJERCICIO 24 — Guardar varias listas con pickle
listas = [[1,2,3], ["a","b","c"], [True, False]]
with open("listas.dat", "wb") as f:
    pickle.dump(listas, f)

# EJERCICIO 25 — Leer varias listas con pickle
with open("listas.dat", "rb") as f:
    print(pickle.load(f))

# EJERCICIO 26 — Escribir texto en mayúsculas
with open("mayus.txt", "w", encoding="utf-8") as f:
    f.write("hola mundo".upper())

# EJERCICIO 27 — Leer fichero y contar dígitos
with open("datos.txt", "r", encoding="utf-8") as f:
    texto = f.read()
print(sum(c.isdigit() for c in texto))

# EJERCICIO 28 — Escribir nombres y luego leerlos ordenados
with open("nombres.txt", "w", encoding="utf-8") as f:
    f.write("Ana\nLuis\nPedro\nMaria\n")

with open("nombres.txt", "r", encoding="utf-8") as f:
    nombres = sorted(linea.strip() for linea in f)
print(nombres)

# EJERCICIO 29 — Duplicar contenido de un fichero
with open("datos.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

with open("duplicado.txt", "w", encoding="utf-8") as f:
    f.write(contenido * 2)

# EJERCICIO 30 — Crear fichero con números aleatorios
import random
with open("aleatorios.txt", "w", encoding="utf-8") as f:
    for _ in range(20):
        f.write(str(random.randint(1, 100)) + "\n")

# ============================================================
# TEMA 8 — EJERCICIOS INTEGRADORES
# ============================================================

# EJERCICIO 1 — Contar palabras de un fichero
with open("texto.txt", "w", encoding="utf-8") as f:
    f.write("hola mundo hola python")

with open("texto.txt", "r", encoding="utf-8") as f:
    palabras = f.read().split()
print("Número de palabras:", len(palabras))


# EJERCICIO 2 — Guardar números en lista y calcular media
numeros = []
for _ in range(5):
    numeros.append(float(input("Número: ")))
print("Media:", sum(numeros) / len(numeros))


# EJERCICIO 3 — Leer fichero y contar líneas no vacías
with open("texto.txt", "r", encoding="utf-8") as f:
    print(sum(1 for linea in f if linea.strip() != ""))


# EJERCICIO 4 — Clase Persona y guardar nombres en fichero
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

personas = [Persona("Ana"), Persona("Luis"), Persona("Pedro")]

with open("personas.txt", "w", encoding="utf-8") as f:
    for p in personas:
        f.write(p.nombre + "\n")


# EJERCICIO 5 — Leer números de fichero y mostrar pares
with open("nums.txt", "w") as f:
    f.write("1\n2\n3\n4\n5\n6\n")

with open("nums.txt", "r") as f:
    for linea in f:
        n = int(linea)
        if n % 2 == 0:
            print(n)


# EJERCICIO 6 — Agenda simple con diccionario y fichero
agenda = {"Ana": "1234", "Luis": "5678"}

with open("agenda.txt", "w") as f:
    for nombre, tel in agenda.items():
        f.write(f"{nombre}:{tel}\n")


# EJERCICIO 7 — Leer agenda y buscar contacto
with open("agenda.txt", "r") as f:
    contactos = dict(linea.strip().split(":") for linea in f)

nombre = input("Buscar: ")
print(contactos.get(nombre, "No encontrado"))


# EJERCICIO 8 — Contar vocales en cada línea de un fichero
with open("texto.txt", "r") as f:
    for linea in f:
        print(sum(1 for c in linea if c in "aeiou"))


# EJERCICIO 9 — Clase Producto y lista de productos
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

productos = [
    Producto("Pan", 1.2),
    Producto("Leche", 0.9),
    Producto("Huevos", 2.5)
]

for p in productos:
    print(p.nombre, p.precio)


# EJERCICIO 10 — Guardar objetos Producto en pickle
import pickle
with open("productos.dat", "wb") as f:
    pickle.dump(productos, f)


# EJERCICIO 11 — Leer objetos Producto desde pickle
with open("productos.dat", "rb") as f:
    lista = pickle.load(f)
    for p in lista:
        print(p.nombre, p.precio)


# EJERCICIO 12 — Validar número con excepciones
while True:
    try:
        n = int(input("Número entre 1 y 10: "))
        if not 1 <= n <= 10:
            raise ValueError
        break
    except:
        print("Número inválido")


# EJERCICIO 13 — Contar cuántas palabras empiezan por vocal
frase = input("Frase: ")
print(sum(1 for p in frase.split() if p[0].lower() in "aeiou"))


# EJERCICIO 14 — Crear fichero con cuadrados del 1 al 20
with open("cuadrados.txt", "w") as f:
    for n in range(1, 21):
        f.write(str(n*n) + "\n")


# EJERCICIO 15 — Leer fichero y mostrar solo números mayores de 50
with open("nums2.txt", "w") as f:
    for n in range(1, 101):
        f.write(str(n) + "\n")

with open("nums2.txt", "r") as f:
    for linea in f:
        if int(linea) > 50:
            print(linea.strip())


# EJERCICIO 16 — Clase Cuenta con transferencia entre cuentas
class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def transferir(self, otra, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            otra.saldo += cantidad

c1 = Cuenta(100)
c2 = Cuenta(50)
c1.transferir(c2, 30)
print(c1.saldo, c2.saldo)


# EJERCICIO 17 — Leer fichero y contar dígitos
with open("texto.txt", "r") as f:
    texto = f.read()
print(sum(c.isdigit() for c in texto))


# EJERCICIO 18 — Crear lista de palabras únicas de un fichero
with open("texto.txt", "r") as f:
    palabras = f.read().split()
print(list(set(palabras)))


# EJERCICIO 19 — Guardar notas de alumnos y calcular media
notas = []
for _ in range(5):
    notas.append(float(input("Nota: ")))
print("Media:", sum(notas) / len(notas))


# EJERCICIO 20 — Clase Alumno con aprobado/suspenso y guardar en fichero
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobado(self):
        return self.nota >= 5

alumnos = [
    Alumno("Ana", 7),
    Alumno("Luis", 4),
    Alumno("Pedro", 9)
]

with open("alumnos.txt", "w") as f:
    for a in alumnos:
        f.write(f"{a.nombre}:{'Aprobado' if a.aprobado() else 'Suspenso'}\n")

# ============================================================
# TEMA 9 — EJERCICIOS INTEGRADORES AVANZADOS
# ============================================================

# EJERCICIO 1 — Sistema de login con 3 intentos, bloqueo y log en fichero
USUARIO_CORRECTO = "admin"
PWD_CORRECTA = "1234"

intentos = 3
with open("login_log.txt", "a", encoding="utf-8") as log:
    while intentos > 0:
        u = input("Usuario: ")
        p = input("Contraseña: ")
        if u == USUARIO_CORRECTO and p == PWD_CORRECTA:
            print("Acceso permitido")
            log.write("LOGIN OK\n")
            break
        else:
            intentos -= 1
            print("Credenciales incorrectas. Intentos restantes:", intentos)
            log.write("LOGIN FAIL\n")
    else:
        print("Usuario bloqueado")
        log.write("USUARIO BLOQUEADO\n")


# EJERCICIO 2 — Gestión de inventario con clases, búsqueda y guardado en fichero
class Producto:
    def __init__(self, codigo, nombre, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def buscar(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def guardar(self, ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            for p in self.productos:
                f.write(f"{p.codigo};{p.nombre};{p.stock}\n")

inv = Inventario()
inv.agregar(Producto("P1", "Teclado", 10))
inv.agregar(Producto("P2", "Ratón", 5))
inv.guardar("inventario.txt")
p = inv.buscar("P2")
if p:
    print(p.nombre, p.stock)


# EJERCICIO 3 — Leer inventario desde fichero y reconstruir objetos
class Producto2:
    def __init__(self, codigo, nombre, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock

productos = []
with open("inventario.txt", "r", encoding="utf-8") as f:
    for linea in f:
        codigo, nombre, stock = linea.strip().split(";")
        productos.append(Producto2(codigo, nombre, int(stock)))

for p in productos:
    print(p.codigo, p.nombre, p.stock)


# EJERCICIO 4 — Sistema de notas con media, máximo, mínimo y aprobado/suspenso
class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def media(self):
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        return self.media() >= 5

alumnos = [
    Alumno("Ana", [5, 7, 9]),
    Alumno("Luis", [3, 4, 2]),
    Alumno("Marta", [9, 9, 10])
]

for a in alumnos:
    print(a.nombre, "MEDIA:", a.media(), "APROBADO" if a.aprobado() else "SUSPENSO")


# EJERCICIO 5 — Cajero automático simple con menú, saldo y control de errores
saldo = 1000.0
while True:
    print("1) Ingresar\n2) Retirar\n3) Consultar\n4) Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        try:
            cantidad = float(input("Cantidad a ingresar: "))
            if cantidad <= 0:
                raise ValueError
            saldo += cantidad
        except:
            print("Cantidad inválida")
    elif opcion == "2":
        try:
            cantidad = float(input("Cantidad a retirar: "))
            if cantidad <= 0 or cantidad > saldo:
                raise ValueError
            saldo -= cantidad
        except:
            print("Operación no válida")
    elif opcion == "3":
        print("Saldo actual:", saldo)
    elif opcion == "4":
        break
    else:
        print("Opción incorrecta")


# EJERCICIO 6 — Analizador de texto: frecuencia de palabras, ordenadas por frecuencia
from collections import Counter

with open("texto_largo.txt", "w", encoding="utf-8") as f:
    f.write("python java python c c++ python java dam dam python\n")

with open("texto_largo.txt", "r", encoding="utf-8") as f:
    palabras = f.read().split()

frecuencias = Counter(palabras)
for palabra, freq in frecuencias.most_common():
    print(palabra, "→", freq)


# EJERCICIO 7 — Sistema de tareas con clases, estados y guardado en pickle
import pickle

class Tarea:
    def __init__(self, titulo, hecha=False):
        self.titulo = titulo
        self.hecha = hecha

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def añadir(self, titulo):
        self.tareas.append(Tarea(titulo))

    def marcar_hecha(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].hecha = True

    def guardar(self, ruta):
        with open(ruta, "wb") as f:
            pickle.dump(self.tareas, f)

    def cargar(self, ruta):
        with open(ruta, "rb") as f:
            self.tareas = pickle.load(f)

g = GestorTareas()
g.añadir("Estudiar POO")
g.añadir("Hacer ejercicios")
g.marcar_hecha(0)
g.guardar("tareas.dat")
g2 = GestorTareas()
g2.cargar("tareas.dat")
for t in g2.tareas:
    print(t.titulo, t.hecha)


# EJERCICIO 8 — Validación de CSV con manejo de errores por línea
with open("datos_csv.txt", "w", encoding="utf-8") as f:
    f.write("Ana;20\nLuis;abc\nMarta;30\n")

with open("datos_csv.txt", "r", encoding="utf-8") as f:
    for linea in f:
        nombre, edad_str = linea.strip().split(";")
        try:
            edad = int(edad_str)
            print(nombre, edad)
        except ValueError:
            print("Línea inválida:", linea.strip())


# EJERCICIO 9 — Simulación de cola de atención con listas y bucles
cola = ["Ana", "Luis", "Marta", "Pedro"]
while cola:
    actual = cola.pop(0)
    print("Atendiendo a:", actual)


# EJERCICIO 10 — Juego de adivinar número con intentos y log de resultados
import random

secreto = random.randint(1, 100)
intentos = 0
with open("juego_log.txt", "a", encoding="utf-8") as log:
    while True:
        try:
            n = int(input("Adivina (1-100): "))
            intentos += 1
            if n < 1 or n > 100:
                raise ValueError
            if n < secreto:
                print("Demasiado pequeño")
            elif n > secreto:
                print("Demasiado grande")
            else:
                print("¡Acertaste en", intentos, "intentos!")
                log.write(f"ACIERTO en {intentos} intentos\n")
                break
        except:
            print("Entrada inválida")
            log.write("ERROR DE ENTRADA\n")


# EJERCICIO 11 — Sistema de reservas con clases y comprobación de disponibilidad
class Reserva:
    def __init__(self, nombre, dia):
        self.nombre = nombre
        self.dia = dia

class Restaurante:
    def __init__(self):
        self.reservas = []

    def reservar(self, nombre, dia):
        for r in self.reservas:
            if r.dia == dia and r.nombre == nombre:
                return False
        self.reservas.append(Reserva(nombre, dia))
        return True

    def mostrar(self):
        for r in self.reservas:
            print(r.nombre, r.dia)

rest = Restaurante()
print(rest.reservar("Ana", "Lunes"))
print(rest.reservar("Ana", "Lunes"))
rest.mostrar()


# EJERCICIO 12 — Procesar log de errores y agrupar por tipo
with open("errores.log", "w", encoding="utf-8") as f:
    f.write("ERROR: Fichero no encontrado\n")
    f.write("WARNING: Memoria alta\n")
    f.write("ERROR: Permiso denegado\n")
    f.write("INFO: Inicio del sistema\n")

contadores = {"ERROR": 0, "WARNING": 0, "INFO": 0}
with open("errores.log", "r", encoding="utf-8") as f:
    for linea in f:
        for tipo in contadores:
            if linea.startswith(tipo):
                contadores[tipo] += 1

print(contadores)


# EJERCICIO 13 — Mini sistema de usuarios con registro y login en fichero
def registrar_usuario(usuario, pwd):
    with open("usuarios.txt", "a", encoding="utf-8") as f:
        f.write(f"{usuario};{pwd}\n")

def comprobar_login(usuario, pwd):
    try:
        with open("usuarios.txt", "r", encoding="utf-8") as f:
            for linea in f:
                u, p = linea.strip().split(";")
                if u == usuario and p == pwd:
                    return True
    except FileNotFoundError:
        return False
    return False

registrar_usuario("admin", "1234")
print(comprobar_login("admin", "1234"))
print(comprobar_login("admin", "0000"))


# EJERCICIO 14 — Analizar fichero y mostrar las 3 palabras más largas
with open("texto_largo2.txt", "w", encoding="utf-8") as f:
    f.write("python programación orientada a objetos excepciones ficheros listas tuplas strings\n")

with open("texto_largo2.txt", "r", encoding="utf-8") as f:
    palabras = f.read().split()

palabras_ordenadas = sorted(palabras, key=len, reverse=True)
print(palabras_ordenadas[:3])


# EJERCICIO 15 — Sistema de tickets con IDs autoincrementales
class Ticket:
    contador = 0
    def __init__(self, descripcion):
        Ticket.contador += 1
        self.id = Ticket.contador
        self.descripcion = descripcion

tickets = []
tickets.append(Ticket("Error en login"))
tickets.append(Ticket("Pantalla en blanco"))
for t in tickets:
    print(t.id, t.descripcion)


# EJERCICIO 16 — Simulación de carrito de compra con total y descuento
class ProductoCarrito:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.items = []

    def agregar(self, producto):
        self.items.append(producto)

    def total(self):
        return sum(p.precio for p in self.items)

    def total_con_descuento(self, porcentaje):
        return self.total() * (1 - porcentaje / 100)

c = Carrito()
c.agregar(ProductoCarrito("Teclado", 20))
c.agregar(ProductoCarrito("Ratón", 10))
print(c.total(), c.total_con_descuento(10))


# EJERCICIO 17 — Validar formato simple de fecha (dd/mm/aaaa)
def validar_fecha(fecha):
    try:
        partes = fecha.split("/")
        if len(partes) != 3:
            return False
        d, m, a = map(int, partes)
        if not (1 <= d <= 31 and 1 <= m <= 12 and a > 0):
            return False
        return True
    except:
        return False

print(validar_fecha("10/02/2024"))
print(validar_fecha("99/99/0000"))


# EJERCICIO 18 — Sistema de logs con niveles y escritura en fichero
class Logger:
    def __init__(self, ruta):
        self.ruta = ruta

    def log(self, nivel, mensaje):
        with open(self.ruta, "a", encoding="utf-8") as f:
            f.write(f"{nivel}: {mensaje}\n")

logger = Logger("sistema.log")
logger.log("INFO", "Inicio")
logger.log("ERROR", "Fallo en módulo X")


# EJERCICIO 19 — Procesar fichero de números y generar otro con solo los primos
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

with open("numeros_grandes.txt", "w") as f:
    for n in range(1, 101):
        f.write(str(n) + "\n")

with open("numeros_grandes.txt", "r") as f_in, open("primos.txt", "w") as f_out:
    for linea in f_in:
        n = int(linea)
        if es_primo(n):
            f_out.write(str(n) + "\n")


# EJERCICIO 20 — Sistema de biblioteca con préstamo de libros
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.prestado = False

class Biblioteca:
    def __init__(self):
        self.libros = []

    def añadir(self, libro):
        self.libros.append(libro)

    def prestar(self, titulo):
        for l in self.libros:
            if l.titulo == titulo and not l.prestado:
                l.prestado = True
                return True
        return False

    def mostrar(self):
        for l in self.libros:
            print(l.titulo, "PRESTADO" if l.prestado else "DISPONIBLE")

b = Biblioteca()
b.añadir(Libro("Python"))
b.añadir(Libro("Java"))
b.prestar("Python")
b.mostrar()

# ============================================================
# TEMA 10 — EJERCICIOS INTEGRADORES EXTREMOS
# ============================================================

# EJERCICIO 1 — Analizador de logs: agrupar por fecha, severidad y contar eventos
from collections import defaultdict

with open("log_sistema.txt", "w") as f:
    f.write("2024-01-01;ERROR;Fallo en módulo X\n")
    f.write("2024-01-01;INFO;Inicio correcto\n")
    f.write("2024-01-02;WARNING;Memoria alta\n")
    f.write("2024-01-01;ERROR;Permiso denegado\n")

eventos = defaultdict(lambda: defaultdict(int))
with open("log_sistema.txt") as f:
    for linea in f:
        fecha, tipo, _ = linea.strip().split(";")
        eventos[fecha][tipo] += 1

print(eventos)


# EJERCICIO 2 — Sistema de usuarios con hashing simple y persistencia
import hashlib

def hash_pwd(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def registrar(usuario, pwd):
    with open("usuarios_hash.txt", "a") as f:
        f.write(f"{usuario};{hash_pwd(pwd)}\n")

def login(usuario, pwd):
    h = hash_pwd(pwd)
    with open("usuarios_hash.txt") as f:
        for linea in f:
            u, hp = linea.strip().split(";")
            if u == usuario and hp == h:
                return True
    return False

registrar("admin", "1234")
print(login("admin", "1234"))
print(login("admin", "0000"))


# EJERCICIO 3 — Sistema de reservas con solapamiento de horas
class Reserva:
    def __init__(self, sala, inicio, fin):
        self.sala = sala
        self.inicio = inicio
        self.fin = fin

class GestorReservas:
    def __init__(self):
        self.reservas = []

    def reservar(self, sala, inicio, fin):
        for r in self.reservas:
            if r.sala == sala and not (fin <= r.inicio or inicio >= r.fin):
                return False
        self.reservas.append(Reserva(sala, inicio, fin))
        return True

g = GestorReservas()
print(g.reservar("A", 10, 12))
print(g.reservar("A", 11, 13))
print(g.reservar("A", 12, 14))


# EJERCICIO 4 — Procesar CSV grande y generar estadísticas
with open("ventas.csv", "w") as f:
    f.write("producto;precio;cantidad\n")
    f.write("teclado;20;3\nraton;10;5\nmonitor;100;1\n")

total = 0
with open("ventas.csv") as f:
    next(f)
    for linea in f:
        prod, precio, cant = linea.strip().split(";")
        total += float(precio) * int(cant)
print(total)


# EJERCICIO 5 — Clase Matriz con suma, multiplicación y transpuesta
class Matriz:
    def __init__(self, datos):
        self.datos = datos

    def suma(self, otra):
        return Matriz([[self.datos[i][j] + otra.datos[i][j]
                        for j in range(len(self.datos[0]))]
                        for i in range(len(self.datos))])

    def transpuesta(self):
        return Matriz(list(map(list, zip(*self.datos))))

    def multiplicar(self, otra):
        res = []
        for i in range(len(self.datos)):
            fila = []
            for j in range(len(otra.datos[0])):
                fila.append(sum(self.datos[i][k] * otra.datos[k][j]
                                for k in range(len(otra.datos))))
            res.append(fila)
        return Matriz(res)

m1 = Matriz([[1,2],[3,4]])
m2 = Matriz([[5,6],[7,8]])
print(m1.multiplicar(m2).datos)


# EJERCICIO 6 — Sistema de biblioteca con préstamos, devoluciones y multas
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.prestado = False
        self.dias = 0

class Biblioteca:
    def __init__(self):
        self.libros = []

    def añadir(self, libro):
        self.libros.append(libro)

    def prestar(self, titulo):
        for l in self.libros:
            if l.titulo == titulo and not l.prestado:
                l.prestado = True
                l.dias = 0
                return True
        return False

    def pasar_dia(self):
        for l in self.libros:
            if l.prestado:
                l.dias += 1

    def multa(self, titulo):
        for l in self.libros:
            if l.titulo == titulo:
                return max(0, l.dias - 7) * 0.5

b = Biblioteca()
b.añadir(Libro("Python"))
b.prestar("Python")
for _ in range(10):
    b.pasar_dia()
print(b.multa("Python"))


# EJERCICIO 7 — Analizador de JSON manual sin librerías
with open("datos.json", "w") as f:
    f.write('{"nombre":"Ana","edad":20,"activo":true}')

with open("datos.json") as f:
    texto = f.read()

texto = texto.replace("{","").replace("}","").replace('"',"")
pares = texto.split(",")
dic = {}
for p in pares:
    k, v = p.split(":")
    if v == "true":
        v = True
    elif v == "false":
        v = False
    elif v.isdigit():
        v = int(v)
    dic[k] = v

print(dic)


# EJERCICIO 8 — Sistema de colas con prioridad
import heapq

cola = []
heapq.heappush(cola, (1, "Urgente"))
heapq.heappush(cola, (3, "Normal"))
heapq.heappush(cola, (2, "Media"))

while cola:
    print(heapq.heappop(cola))


# EJERCICIO 9 — Cifrado César configurable
def cifrar(texto, despl):
    res = ""
    for c in texto:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            res += chr(base + (ord(c) - base + despl) % 26)
        else:
            res += c
    return res

print(cifrar("Hola Mundo", 5))


# EJERCICIO 10 — Sistema de logs rotativos (crea nuevo fichero al superar tamaño)
import os

def escribir_log(mensaje):
    if os.path.exists("log.txt") and os.path.getsize("log.txt") > 50:
        os.rename("log.txt", "log_old.txt")
    with open("log.txt", "a") as f:
        f.write(mensaje + "\n")

for i in range(20):
    escribir_log(f"Evento {i}")


# EJERCICIO 11 — Simulación de hilos (sin threading): turnos alternos
turno = 0
for i in range(10):
    if turno == 0:
        print("Hilo A ejecuta")
        turno = 1
    else:
        print("Hilo B ejecuta")
        turno = 0


# EJERCICIO 12 — Sistema de votación con control de duplicados
votos = {}
while True:
    nombre = input("Votar (FIN para terminar): ")
    if nombre == "FIN":
        break
    if nombre in votos:
        print("Ya has votado")
    else:
        votos[nombre] = True

print("Total votos:", len(votos))


# EJERCICIO 13 — Analizador de texto: top 5 palabras más largas sin repetir
with open("texto3.txt", "w") as f:
    f.write("python programación estructuras excepciones concurrencia asincronía")

with open("texto3.txt") as f:
    palabras = set(f.read().split())

print(sorted(palabras, key=len, reverse=True)[:5])


# EJERCICIO 14 — Sistema de pagos con validación de tarjeta
def validar_tarjeta(num):
    num = num.replace(" ", "")
    if not num.isdigit():
        return False
    suma = 0
    inv = num[::-1]
    for i, d in enumerate(inv):
        n = int(d)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        suma += n
    return suma % 10 == 0

print(validar_tarjeta("4539 1488 0343 6467"))


# EJERCICIO 15 — Sistema de configuración con lectura y escritura tipo INI
def leer_ini(ruta):
    config = {}
    with open(ruta) as f:
        for linea in f:
            if "=" in linea:
                k, v = linea.strip().split("=")
                config[k] = v
    return config

def escribir_ini(ruta, dic):
    with open(ruta, "w") as f:
        for k, v in dic.items():
            f.write(f"{k}={v}\n")

escribir_ini("config.ini", {"modo":"oscuro","volumen":"80"})
print(leer_ini("config.ini"))


# EJERCICIO 16 — Sistema de mensajería con cola FIFO y persistencia
from collections import deque

mensajes = deque()
mensajes.append("Hola")
mensajes.append("¿Qué tal?")
mensajes.append("Adiós")

with open("mensajes.txt", "w") as f:
    while mensajes:
        f.write(mensajes.popleft() + "\n")


# EJERCICIO 17 — Mini ORM: convertir objetos a líneas y viceversa
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def guardar_usuarios(ruta, lista):
    with open(ruta, "w") as f:
        for u in lista:
            f.write(f"{u.nombre};{u.edad}\n")

def cargar_usuarios(ruta):
    res = []
    with open(ruta) as f:
        for linea in f:
            n, e = linea.strip().split(";")
            res.append(Usuario(n, int(e)))
    return res

guardar_usuarios("usuarios2.txt", [Usuario("Ana",20), Usuario("Luis",30)])
for u in cargar_usuarios("usuarios2.txt"):
    print(u.nombre, u.edad)


# EJERCICIO 18 — Sistema de colisiones en un plano 2D
class Objeto:
    def __init__(self, x, y, tamaño):
        self.x = x
        self.y = y
        self.tamaño = tamaño

def colision(a, b):
    return abs(a.x - b.x) < a.tamaño and abs(a.y - b.y) < a.tamaño

o1 = Objeto(10, 10, 5)
o2 = Objeto(12, 13, 5)
print(colision(o1, o2))


# EJERCICIO 19 — Motor de reglas: ejecutar acciones según condiciones
reglas = [
    ("temperatura > 30", "Encender aire"),
    ("temperatura < 10", "Encender calefacción"),
]

temperatura = 35
for condicion, accion in reglas:
    if eval(condicion):
        print(accion)


# EJERCICIO 20 — Sistema de backups incrementales
import shutil
import os

def backup(origen, destino):
    if not os.path.exists(destino):
        os.makedirs(destino)
    archivos = os.listdir(origen)
    for a in archivos:
        ruta_o = os.path.join(origen, a)
        ruta_d = os.path.join(destino, a)
        if not os.path.exists(ruta_d):
            shutil.copy(ruta_o, ruta_d)

os.makedirs("carpeta_origen", exist_ok=True)
with open("carpeta_origen/archivo.txt", "w") as f:
    f.write("Hola")

backup("carpeta_origen", "carpeta_backup")

# ============================================================
# TEMA 11 — EJERCICIOS INTEGRADORES ULTRA
# ============================================================

# EJERCICIO 1 — Grafo no dirigido con lista de adyacencia y búsqueda en anchura (BFS)
from collections import deque

class Grafo:
    def __init__(self):
        self.adj = {}

    def añadir_arista(self, u, v):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)

    def bfs(self, inicio):
        visitados = set([inicio])
        cola = deque([inicio])
        orden = []
        while cola:
            nodo = cola.popleft()
            orden.append(nodo)
            for vecino in self.adj.get(nodo, []):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return orden

g = Grafo()
g.añadir_arista("A", "B")
g.añadir_arista("A", "C")
g.añadir_arista("B", "D")
g.añadir_arista("C", "D")
print(g.bfs("A"))


# EJERCICIO 2 — Dijkstra simple en grafo ponderado (sin librerías externas)
import math

class GrafoPonderado:
    def __init__(self):
        self.adj = {}

    def añadir_arista(self, u, v, w):
        self.adj.setdefault(u, []).append((v, w))
        self.adj.setdefault(v, []).append((u, w))

    def dijkstra(self, origen):
        dist = {n: math.inf for n in self.adj}
        dist[origen] = 0
        visitados = set()
        while len(visitados) < len(self.adj):
            nodo = min((n for n in self.adj if n not in visitados), key=lambda x: dist[x])
            visitados.add(nodo)
            for vecino, peso in self.adj[nodo]:
                if dist[nodo] + peso < dist[vecino]:
                    dist[vecino] = dist[nodo] + peso
        return dist

gp = GrafoPonderado()
gp.añadir_arista("A", "B", 4)
gp.añadir_arista("A", "C", 2)
gp.añadir_arista("B", "C", 1)
gp.añadir_arista("B", "D", 5)
gp.añadir_arista("C", "D", 8)
print(gp.dijkstra("A"))


# EJERCICIO 3 — Sistema de plugins con carga dinámica de funciones desde fichero
def cargar_plugins(ruta):
    funciones = {}
    with open(ruta, "r", encoding="utf-8") as f:
        codigo = f.read()
    contexto = {}
    exec(codigo, contexto)
    for k, v in contexto.items():
        if callable(v):
            funciones[k] = v
    return funciones

with open("plugins.py", "w", encoding="utf-8") as f:
    f.write("def saludar(nombre):\n")
    f.write("    return f'Hola {nombre}'\n")

plugins = cargar_plugins("plugins.py")
print(plugins["saludar"]("Antuan"))


# EJERCICIO 4 — Intérprete mínimo de expresiones aritméticas (+, -, *, /) con pila
def evaluar(expr):
    tokens = expr.split()
    pila = []
    for t in tokens:
        if t.isdigit():
            pila.append(int(t))
        else:
            b = pila.pop()
            a = pila.pop()
            if t == "+":
                pila.append(a + b)
            elif t == "-":
                pila.append(a - b)
            elif t == "*":
                pila.append(a * b)
            elif t == "/":
                pila.append(a / b)
    return pila[0]

print(evaluar("3 4 + 2 * 7 -"))  # (3+4)*2-7


# EJERCICIO 5 — Sistema de eventos con suscriptores (patrón observer básico)
class Evento:
    def __init__(self):
        self.subs = []

    def suscribir(self, f):
        self.subs.append(f)

    def emitir(self, dato):
        for f in self.subs:
            f(dato)

def manejador1(x):
    print("M1:", x)

def manejador2(x):
    print("M2:", x * 2)

e = Evento()
e.suscribir(manejador1)
e.suscribir(manejador2)
e.emitir(10)


# EJERCICIO 6 — Sistema de caché LRU muy simple
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.datos = OrderedDict()

    def get(self, clave):
        if clave not in self.datos:
            return None
        self.datos.move_to_end(clave)
        return self.datos[clave]

    def put(self, clave, valor):
        if clave in self.datos:
            self.datos.move_to_end(clave)
        self.datos[clave] = valor
        if len(self.datos) > self.capacidad:
            self.datos.popitem(last=False)

c = LRUCache(2)
c.put("a", 1)
c.put("b", 2)
c.get("a")
c.put("c", 3)
print(c.datos)


# EJERCICIO 7 — Parser de configuración tipo JSON a diccionario (sin json)
def parse_simple_json(texto):
    texto = texto.strip()
    texto = texto[1:-1]
    partes = texto.split(",")
    res = {}
    for p in partes:
        k, v = p.split(":")
        k = k.strip().strip('"')
        v = v.strip()
        if v.startswith('"') and v.endswith('"'):
            v = v.strip('"')
        elif v.isdigit():
            v = int(v)
        elif v in ("true", "false"):
            v = v == "true"
        res[k] = v
    return res

print(parse_simple_json('{"nombre":"Ana","edad":21,"activo":true}'))


# EJERCICIO 8 — Sistema de colas de trabajo con reintentos y log de errores
from collections import deque

trabajos = deque(["t1", "t2", "t3"])
intentos = {}

while trabajos:
    t = trabajos.popleft()
    intentos[t] = intentos.get(t, 0) + 1
    try:
        if t == "t2" and intentos[t] < 3:
            raise ValueError("Fallo temporal")
        print("Ejecutado:", t)
    except Exception as e:
        print("Error en", t, "→", e)
        if intentos[t] < 3:
            trabajos.append(t)


# EJERCICIO 9 — Evaluador de expresiones booleanas con variables usando eval de forma controlada
def eval_bool(expr, contexto):
    permitido = {"True": True, "False": False, "and": True, "or": True, "not": True}
    for k in contexto:
        permitido[k] = contexto[k]
    return eval(expr, {"__builtins__": None}, permitido)

ctx = {"x": True, "y": False}
print(eval_bool("x and not y", ctx))


# EJERCICIO 10 — Árbol binario de búsqueda con inserción y búsqueda
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq:
                self._insertar(nodo.izq, valor)
            else:
                nodo.izq = Nodo(valor)
        else:
            if nodo.der:
                self._insertar(nodo.der, valor)
            else:
                nodo.der = Nodo(valor)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if not nodo:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self._buscar(nodo.izq, valor)
        return self._buscar(nodo.der, valor)

abb = ABB()
for n in [5, 3, 7, 2, 4, 6, 8]:
    abb.insertar(n)
print(abb.buscar(4), abb.buscar(10))


# EJERCICIO 11 — Programador de tareas con prioridad y tiempo estimado
import heapq

class Tarea:
    def __init__(self, prioridad, tiempo, nombre):
        self.prioridad = prioridad
        self.tiempo = tiempo
        self.nombre = nombre

    def __lt__(self, other):
        return self.prioridad < other.prioridad

cola = []
heapq.heappush(cola, Tarea(2, 5, "Compilar"))
heapq.heappush(cola, Tarea(1, 2, "Guardar"))
heapq.heappush(cola, Tarea(3, 10, "Backup"))

while cola:
    t = heapq.heappop(cola)
    print(t.nombre, t.prioridad, t.tiempo)


# EJERCICIO 12 — Sistema de versiones de documentos con historial
class Documento:
    def __init__(self, texto=""):
        self.historial = [texto]

    def editar(self, nuevo_texto):
        self.historial.append(nuevo_texto)

    def deshacer(self):
        if len(self.historial) > 1:
            self.historial.pop()

    def actual(self):
        return self.historial[-1]

doc = Documento("v1")
doc.editar("v2")
doc.editar("v3")
doc.deshacer()
print(doc.actual())


# EJERCICIO 13 — Motor de plantillas muy simple con {{variable}}
def render(plantilla, contexto):
    res = plantilla
    for k, v in contexto.items():
        res = res.replace("{{" + k + "}}", str(v))
    return res

print(render("Hola {{nombre}}, nota: {{nota}}", {"nombre": "Antuan", "nota": 10}))


# EJERCICIO 14 — Sistema de permisos por roles
class UsuarioRol:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

PERMISOS = {
    "admin": {"leer", "escribir", "borrar"},
    "user": {"leer"},
}

def puede(usuario, accion):
    return accion in PERMISOS.get(usuario.rol, set())

u1 = UsuarioRol("Ana", "admin")
u2 = UsuarioRol("Luis", "user")
print(puede(u1, "borrar"), puede(u2, "borrar"))


# EJERCICIO 15 — Sistema de colas encadenadas (pipeline de procesamiento)
from collections import deque

entrada = deque(["dato1", "dato2", "dato3"])
procesada = deque()
salida = deque()

while entrada:
    x = entrada.popleft()
    procesada.append(x.upper())

while procesada:
    x = procesada.popleft()
    salida.append(f"[OK] {x}")

print(list(salida))


# EJERCICIO 16 — Compresor muy simple: RLE (Run-Length Encoding)
def comprimir_rle(texto):
    if not texto:
        return ""
    res = []
    actual = texto[0]
    cont = 1
    for c in texto[1:]:
        if c == actual:
            cont += 1
        else:
            res.append(actual + str(cont))
            actual = c
            cont = 1
    res.append(actual + str(cont))
    return "".join(res)

print(comprimir_rle("aaabbbccccdd"))


# EJERCICIO 17 — Descompresor RLE simple
def descomprimir_rle(texto):
    res = ""
    letra = ""
    num = ""
    for c in texto:
        if c.isalpha():
            if letra and num:
                res += letra * int(num)
                num = ""
            letra = c
        else:
            num += c
    if letra and num:
        res += letra * int(num)
    return res

print(descomprimir_rle("a3b3c4d2"))


# EJERCICIO 18 — Sistema de métricas: registrar tiempos y calcular media y máximo
class Metricas:
    def __init__(self):
        self.valores = []

    def registrar(self, v):
        self.valores.append(v)

    def media(self):
        return sum(self.valores) / len(self.valores) if self.valores else 0

    def maximo(self):
        return max(self.valores) if self.valores else 0

m = Metricas()
for v in [0.1, 0.5, 0.2, 1.0]:
    m.registrar(v)
print(m.media(), m.maximo())


# EJERCICIO 19 — Sistema de dependencias: orden topológico simple
def orden_topologico(grafo):
    visitado = set()
    res = []

    def dfs(n):
        if n in visitado:
            return
        visitado.add(n)
        for v in grafo.get(n, []):
            dfs(v)
        res.append(n)

    for nodo in grafo:
        dfs(nodo)
    res.reverse()
    return res

g = {
    "compilar": ["analizar"],
    "analizar": ["descargar"],
    "descargar": [],
}
print(orden_topologico(g))


# EJERCICIO 20 — Mini motor de reglas de descuento para carrito
class Carrito2:
    def __init__(self):
        self.items = []

    def agregar(self, nombre, precio):
        self.items.append((nombre, precio))

    def total(self):
        return sum(p for _, p in self.items)

    def total_con_reglas(self, reglas):
        total = self.total()
        for r in reglas:
            total = r(self.items, total)
        return total

def regla_descuento_3_items(items, total):
    if len(items) >= 3:
        return total * 0.9
    return total

def regla_producto_caro(items, total):
    if any(p > 100 for _, p in items):
        return total - 10
    return total

car = Carrito2()
car.agregar("Teclado", 20)
car.agregar("Ratón", 10)
car.agregar("Monitor", 150)
print(car.total(), car.total_con_reglas([regla_descuento_3_items, regla_producto_caro]))

# ============================================================
# TEMA 12 — EJERCICIOS INTEGRADORES ULTRA++
# ============================================================

# EJERCICIO 1 — Sistema de módulos cargados dinámicamente con dependencias
import importlib

with open("mod_a.py", "w") as f:
    f.write("def run(): return 'A ejecutado'\n")

with open("mod_b.py", "w") as f:
    f.write("def run(): return 'B ejecutado'\n")

def cargar_modulos(lista):
    cargados = {}
    for nombre in lista:
        mod = importlib.import_module(nombre)
        cargados[nombre] = mod.run()
    return cargados

print(cargar_modulos(["mod_a", "mod_b"]))


# EJERCICIO 2 — Sistema de colas con prioridad múltiple y reordenamiento dinámico
import heapq

cola = []
heapq.heappush(cola, (3, "Tarea baja"))
heapq.heappush(cola, (1, "Tarea alta"))
heapq.heappush(cola, (2, "Tarea media"))

while cola:
    print(heapq.heappop(cola))


# EJERCICIO 3 — Motor de reglas condicionales con ejecución encadenada
reglas = [
    ("x > 10", "x = x - 5"),
    ("x % 2 == 0", "x = x // 2"),
    ("x < 5", "x = x + 20"),
]

x = 17
for cond, accion in reglas:
    if eval(cond):
        exec(accion)
print(x)


# EJERCICIO 4 — Sistema de archivos virtual en memoria (árbol)
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = {}

class FS:
    def __init__(self):
        self.root = Nodo("/")

    def mkdir(self, ruta):
        actual = self.root
        for parte in ruta.strip("/").split("/"):
            actual = actual.hijos.setdefault(parte, Nodo(parte))

    def ls(self, ruta):
        actual = self.root
        for parte in ruta.strip("/").split("/"):
            actual = actual.hijos.get(parte, None)
            if actual is None:
                return []
        return list(actual.hijos.keys())

fs = FS()
fs.mkdir("/usr/local/bin")
print(fs.ls("/usr/local"))


# EJERCICIO 5 — Sistema de logs con niveles, filtros y exportación
class Logger:
    def __init__(self):
        self.logs = []

    def log(self, nivel, msg):
        self.logs.append((nivel, msg))

    def filtrar(self, nivel):
        return [m for n, m in self.logs if n == nivel]

l = Logger()
l.log("INFO", "Inicio")
l.log("ERROR", "Fallo")
l.log("INFO", "Cargando módulo")
print(l.filtrar("INFO"))


# EJERCICIO 6 — Máquina de estados finitos
class FSM:
    def __init__(self, estado_inicial):
        self.estado = estado_inicial
        self.trans = {}

    def añadir(self, estado, evento, nuevo_estado):
        self.trans.setdefault(estado, {})[evento] = nuevo_estado

    def enviar(self, evento):
        self.estado = self.trans[self.estado].get(evento, self.estado)

fsm = FSM("inicio")
fsm.añadir("inicio", "login", "menu")
fsm.añadir("menu", "logout", "inicio")
fsm.enviar("login")
fsm.enviar("logout")
print(fsm.estado)


# EJERCICIO 7 — Sistema de caché con expiración por tiempo (simulado)
import time

class Cache:
    def __init__(self):
        self.datos = {}

    def set(self, clave, valor, ttl):
        self.datos[clave] = (valor, time.time() + ttl)

    def get(self, clave):
        if clave not in self.datos:
            return None
        valor, exp = self.datos[clave]
        if time.time() > exp:
            del self.datos[clave]
            return None
        return valor

c = Cache()
c.set("x", 100, 1)
time.sleep(1.1)
print(c.get("x"))


# EJERCICIO 8 — Árbol general con recorrido DFS y BFS
from collections import deque

class NodoG:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

root = NodoG("A")
root.hijos = [NodoG("B"), NodoG("C")]
root.hijos[0].hijos = [NodoG("D"), NodoG("E")]

def dfs(n):
    res = [n.valor]
    for h in n.hijos:
        res += dfs(h)
    return res

def bfs(n):
    cola = deque([n])
    res = []
    while cola:
        x = cola.popleft()
        res.append(x.valor)
        cola.extend(x.hijos)
    return res

print(dfs(root))
print(bfs(root))


# EJERCICIO 9 — Sistema de tareas con dependencias y ejecución ordenada
deps = {
    "compilar": ["analizar"],
    "analizar": ["descargar"],
    "descargar": [],
}

orden = []
visitado = set()

def resolver(t):
    if t in visitado:
        return
    visitado.add(t)
    for d in deps[t]:
        resolver(d)
    orden.append(t)

for t in deps:
    resolver(t)

print(orden)


# EJERCICIO 10 — Motor de plantillas con bloques y variables
def render(plantilla, ctx):
    for k, v in ctx.items():
        plantilla = plantilla.replace("{{" + k + "}}", str(v))
    return plantilla

print(render("Hola {{nombre}}, total: {{total}}€", {"nombre": "Antuan", "total": 99}))


# EJERCICIO 11 — Sistema de colisiones en 2D con bounding boxes
class Obj:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

def colision(a, b):
    return not (a.x + a.w < b.x or b.x + b.w < a.x or
                a.y + a.h < b.y or b.y + b.h < a.y)

o1 = Obj(0, 0, 10, 10)
o2 = Obj(5, 5, 10, 10)
print(colision(o1, o2))


# EJERCICIO 12 — Sistema de versiones con rollback múltiple
class Versionador:
    def __init__(self):
        self.hist = []

    def commit(self, estado):
        self.hist.append(estado)

    def rollback(self, n):
        for _ in range(n):
            if self.hist:
                self.hist.pop()

    def actual(self):
        return self.hist[-1] if self.hist else None

v = Versionador()
v.commit("v1")
v.commit("v2")
v.commit("v3")
v.rollback(2)
print(v.actual())


# EJERCICIO 13 — Sistema de colas paralelas con balanceo
from collections import deque

colas = [deque(), deque(), deque()]
tareas = ["A","B","C","D","E","F","G"]

for i, t in enumerate(tareas):
    colas[i % len(colas)].append(t)

print([list(c) for c in colas])


# EJERCICIO 14 — Motor de expresiones matemáticas con variables
def eval_expr(expr, ctx):
    return eval(expr, {"__builtins__": None}, ctx)

print(eval_expr("a*b + c", {"a": 3, "b": 4, "c": 5}))


# EJERCICIO 15 — Sistema de inventario con búsqueda avanzada
class Item:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

items = [
    Item("Teclado", 20, "periferico"),
    Item("Ratón", 10, "periferico"),
    Item("Monitor", 150, "pantalla"),
]

res = [i.nombre for i in items if i.precio > 15 and i.categoria == "periferico"]
print(res)


# EJERCICIO 16 — Sistema de logs con rotación por número de líneas
def rotar_log(ruta, max_lineas):
    with open(ruta, "r") as f:
        lineas = f.readlines()
    if len(lineas) > max_lineas:
        with open(ruta + ".old", "w") as f:
            f.writelines(lineas)
        open(ruta, "w").close()

with open("rotar.txt", "w") as f:
    for i in range(20):
        f.write(f"Línea {i}\n")

rotar_log("rotar.txt", 10)


# EJERCICIO 17 — Árbol de expresiones matemáticas
class NodoExpr:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

def eval_arbol(n):
    if not n.izq and not n.der:
        return int(n.valor)
    a = eval_arbol(n.izq)
    b = eval_arbol(n.der)
    if n.valor == "+": return a + b
    if n.valor == "-": return a - b
    if n.valor == "*": return a * b
    if n.valor == "/": return a / b

arbol = NodoExpr("*", NodoExpr("+", NodoExpr("3"), NodoExpr("4")), NodoExpr("2"))
print(eval_arbol(arbol))


# EJERCICIO 18 — Sistema de colas con tiempo de llegada y prioridad
import heapq, time

cola = []
t0 = time.time()

def push(prio, dato):
    heapq.heappush(cola, (prio, time.time() - t0, dato))

push(2, "medio")
push(1, "alto")
push(3, "bajo")

while cola:
    print(heapq.heappop(cola))


# EJERCICIO 19 — Sistema de dependencias con detección de ciclos
grafo = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"],
}

visit = set()
pila = set()
ciclo = False

def dfs(n):
    global ciclo
    if n in pila:
        ciclo = True
        return
    if n in visit:
        return
    visit.add(n)
    pila.add(n)
    for v in grafo[n]:
        dfs(v)
    pila.remove(n)

for n in grafo:
    dfs(n)

print("Ciclo:", ciclo)


# EJERCICIO 20 — Sistema de colas de impresión con prioridad y tamaño
import heapq

class Trabajo:
    def __init__(self, prio, tamaño, nombre):
        self.prio = prio
        self.tamaño = tamaño
        self.nombre = nombre

    def __lt__(self, other):
        return (self.prio, self.tamaño) < (other.prio, other.tamaño)

cola = []
heapq.heappush(cola, Trabajo(2, 50, "Doc1"))
heapq.heappush(cola, Trabajo(1, 100, "Doc2"))
heapq.heappush(cola, Trabajo(1, 20, "Doc3"))

while cola:
    t = heapq.heappop(cola)
    print(t.nombre, t.prio, t.tamaño)

# ============================================================
# TEMA 13 — EJERCICIOS AVANZADOS DE JUGADORES, PARTIDOS Y LIGAS
# ============================================================

# EJERCICIO 1 — Clase Jugador con puntos, asistencias y valoración
class Jugador:
    def __init__(self, nombre, puntos, asistencias):
        self.nombre = nombre
        self.puntos = puntos
        self.asistencias = asistencias

    def valoracion(self):
        return self.puntos * 2 + self.asistencias

j = Jugador("Ana", 20, 5)
print(j.nombre, j.valoracion())


# EJERCICIO 2 — Clase Partido con dos equipos y ganador automático
class Partido:
    def __init__(self, equipo1, equipo2, puntos1, puntos2):
        self.e1 = equipo1
        self.e2 = equipo2
        self.p1 = puntos1
        self.p2 = puntos2

    def ganador(self):
        if self.p1 > self.p2:
            return self.e1
        elif self.p2 > self.p1:
            return self.e2
        return "Empate"

p = Partido("A", "B", 80, 75)
print(p.ganador())


# EJERCICIO 3 — Clase Árbitro con registro de faltas
class Arbitro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.faltas = 0

    def pitar(self):
        self.faltas += 1

a = Arbitro("Luis")
a.pitar()
a.pitar()
print(a.faltas)


# EJERCICIO 4 — Liga con lista de partidos y cálculo de victorias por equipo
class Liga:
    def __init__(self):
        self.partidos = []

    def añadir(self, partido):
        self.partidos.append(partido)

    def victorias(self, equipo):
        cont = 0
        for p in self.partidos:
            if p.ganador() == equipo:
                cont += 1
        return cont

l = Liga()
l.añadir(Partido("A", "B", 3, 1))
l.añadir(Partido("A", "C", 2, 5))
l.añadir(Partido("A", "B", 7, 6))
print(l.victorias("A"))


# EJERCICIO 5 — Jugador con historial de partidos y media de puntos
class Jugador2:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

    def añadir_partido(self, puntos):
        self.historial.append(puntos)

    def media(self):
        return sum(self.historial) / len(self.historial) if self.historial else 0

j = Jugador2("Pedro")
j.añadir_partido(10)
j.añadir_partido(20)
j.añadir_partido(30)
print(j.media())


# EJERCICIO 6 — Equipo con plantilla y cálculo de valoración total
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def añadir(self, jugador):
        self.jugadores.append(jugador)

    def valor_total(self):
        return sum(j.valoracion() for j in self.jugadores)

e = Equipo("Tigres")
e.añadir(Jugador("Ana", 10, 3))
e.añadir(Jugador("Luis", 15, 2))
print(e.valor_total())


# EJERCICIO 7 — Árbitro que registra tarjetas amarillas y rojas
class Arbitro2:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amarillas = 0
        self.rojas = 0

    def tarjeta(self, tipo):
        if tipo == "A":
            self.amarillas += 1
        elif tipo == "R":
            self.rojas += 1

arb = Arbitro2("Carlos")
arb.tarjeta("A")
arb.tarjeta("R")
print(arb.amarillas, arb.rojas)


# EJERCICIO 8 — Liga con clasificación ordenada por victorias
class Liga2:
    def __init__(self):
        self.partidos = []

    def añadir(self, p):
        self.partidos.append(p)

    def clasificacion(self):
        equipos = {}
        for p in self.partidos:
            g = p.ganador()
            if g != "Empate":
                equipos[g] = equipos.get(g, 0) + 1
        return sorted(equipos.items(), key=lambda x: x[1], reverse=True)

l2 = Liga2()
l2.añadir(Partido("A", "B", 5, 3))
l2.añadir(Partido("C", "A", 2, 7))
l2.añadir(Partido("B", "C", 1, 1))
print(l2.clasificacion())


# EJERCICIO 9 — Jugador con estadísticas avanzadas (rebotes, robos, pérdidas)
class Jugador3:
    def __init__(self, nombre, pts, reb, rob, per):
        self.nombre = nombre
        self.pts = pts
        self.reb = reb
        self.rob = rob
        self.per = per

    def eficiencia(self):
        return self.pts + self.reb + self.rob - self.per

j3 = Jugador3("Marta", 20, 10, 3, 2)
print(j3.eficiencia())


# EJERCICIO 10 — Partido con árbitro asignado
class Partido2:
    def __init__(self, e1, e2, arb):
        self.e1 = e1
        self.e2 = e2
        self.arb = arb

p2 = Partido2("A", "B", Arbitro("Luis"))
print(p2.arb.nombre)


# EJERCICIO 11 — Liga que guarda resultados en fichero
class LigaFichero:
    def __init__(self, ruta):
        self.ruta = ruta
        self.partidos = []

    def añadir(self, p):
        self.partidos.append(p)

    def guardar(self):
        with open(self.ruta, "w") as f:
            for p in self.partidos:
                f.write(f"{p.e1};{p.e2};{p.p1};{p.p2}\n")

lf = LigaFichero("liga.txt")
lf.añadir(Partido("A","B",3,1))
lf.guardar()


# EJERCICIO 12 — Cargar partidos desde fichero y reconstruir objetos
partidos = []
with open("liga.txt") as f:
    for linea in f:
        e1, e2, p1, p2 = linea.strip().split(";")
        partidos.append(Partido(e1, e2, int(p1), int(p2)))

print(len(partidos))


# EJERCICIO 13 — Árbitro que evalúa comportamiento de jugadores
class Arbitro3:
    def __init__(self, nombre):
        self.nombre = nombre
        self.faltas_jugador = {}

    def falta(self, jugador):
        self.faltas_jugador[jugador] = self.faltas_jugador.get(jugador, 0) + 1

arb3 = Arbitro3("Mario")
arb3.falta("Ana")
arb3.falta("Ana")
print(arb3.faltas_jugador)


# EJERCICIO 14 — Equipo con máximo anotador
class Equipo2:
    def __init__(self):
        self.jugadores = []

    def añadir(self, j):
        self.jugadores.append(j)

    def max_anotador(self):
        return max(self.jugadores, key=lambda x: x.puntos)

eq = Equipo2()
eq.añadir(Jugador("Ana", 10, 2))
eq.añadir(Jugador("Luis", 25, 1))
print(eq.max_anotador().nombre)


# EJERCICIO 15 — Liga con promedio de puntos por equipo
class Liga3:
    def __init__(self):
        self.partidos = []

    def añadir(self, p):
        self.partidos.append(p)

    def promedio(self, equipo):
        pts = []
        for p in self.partidos:
            if p.e1 == equipo:
                pts.append(p.p1)
            if p.e2 == equipo:
                pts.append(p.p2)
        return sum(pts)/len(pts) if pts else 0

l3 = Liga3()
l3.añadir(Partido("A","B",10,5))
l3.añadir(Partido("A","C",20,15))
print(l3.promedio("A"))


# EJERCICIO 16 — Jugador con historial de equipos (transferencias)
class Jugador4:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def fichar(self, equipo):
        self.equipos.append(equipo)

j4 = Jugador4("Carlos")
j4.fichar("A")
j4.fichar("B")
print(j4.equipos)


# EJERCICIO 17 — Árbitro que genera informe en fichero
class ArbitroInforme:
    def __init__(self, nombre):
        self.nombre = nombre
        self.faltas = []

    def registrar(self, jugador, tipo):
        self.faltas.append((jugador, tipo))

    def informe(self, ruta):
        with open(ruta, "w") as f:
            for j, t in self.faltas:
                f.write(f"{j};{t}\n")

arb_inf = ArbitroInforme("Pepe")
arb_inf.registrar("Ana","A")
arb_inf.informe("informe.txt")


# EJERCICIO 18 — Liga con detección de empates
class LigaEmpates:
    def __init__(self):
        self.partidos = []

    def añadir(self, p):
        self.partidos.append(p)

    def empates(self):
        return sum(1 for p in self.partidos if p.ganador() == "Empate")

le = LigaEmpates()
le.añadir(Partido("A","B",1,1))
le.añadir(Partido("A","C",2,2))
print(le.empates())


# EJERCICIO 19 — Jugador con ranking basado en múltiples estadísticas
class JugadorRank:
    def __init__(self, nombre, pts, ast, reb):
        self.nombre = nombre
        self.pts = pts
        self.ast = ast
        self.reb = reb

    def ranking(self):
        return self.pts*3 + self.ast*2 + self.reb

jr = JugadorRank("Ana", 10, 5, 7)
print(jr.ranking())


# EJERCICIO 20 — Liga con MVP (jugador con mayor valoración total)
class LigaMVP:
    def __init__(self):
        self.jugadores = []

    def añadir(self, j):
        self.jugadores.append(j)

    def mvp(self):
        return max(self.jugadores, key=lambda x: x.valoracion())

lm = LigaMVP()
lm.añadir(Jugador("Ana", 10, 3))
lm.añadir(Jugador("Luis", 20, 1))
print(lm.mvp().nombre)

# ============================================================
# TEMA 14 — EJERCICIOS AVANZADOS DE SISTEMAS Y GESTIÓN
# ============================================================

# EJERCICIO 1 — Clase Usuario con roles y permisos
class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

PERMISOS = {
    "admin": {"crear", "borrar", "editar"},
    "user": {"leer"},
}

def puede(u, accion):
    return accion in PERMISOS.get(u.rol, set())

u1 = Usuario("Ana", "admin")
u2 = Usuario("Luis", "user")
print(puede(u1, "borrar"), puede(u2, "borrar"))


# EJERCICIO 2 — Clase Producto con IVA y precio final
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def precio_final(self):
        return self.precio * 1.21

p = Producto("Teclado", 20)
print(p.precio_final())


# EJERCICIO 3 — Factura con lista de productos y total
class Factura:
    def __init__(self):
        self.items = []

    def añadir(self, producto, cantidad):
        self.items.append((producto, cantidad))

    def total(self):
        return sum(p.precio_final() * c for p, c in self.items)

f = Factura()
f.añadir(Producto("Ratón", 10), 2)
print(f.total())


# EJERCICIO 4 — Biblioteca con préstamo y devolución
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.prestado = False

class Biblioteca:
    def __init__(self):
        self.libros = []

    def añadir(self, libro):
        self.libros.append(libro)

    def prestar(self, titulo):
        for l in self.libros:
            if l.titulo == titulo and not l.prestado:
                l.prestado = True
                return True
        return False

b = Biblioteca()
b.añadir(Libro("Python"))
print(b.prestar("Python"))


# EJERCICIO 5 — Empresa con empleados y cálculo de nómina total
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

class Empresa:
    def __init__(self):
        self.empleados = []

    def añadir(self, e):
        self.empleados.append(e)

    def nomina(self):
        return sum(e.sueldo for e in self.empleados)

emp = Empresa()
emp.añadir(Empleado("Ana", 1200))
emp.añadir(Empleado("Luis", 1500))
print(emp.nomina())


# EJERCICIO 6 — Sistema de reservas (salas y horarios)
class Reserva:
    def __init__(self, sala, inicio, fin):
        self.sala = sala
        self.inicio = inicio
        self.fin = fin

class GestorReservas:
    def __init__(self):
        self.reservas = []

    def reservar(self, sala, inicio, fin):
        for r in self.reservas:
            if r.sala == sala and not (fin <= r.inicio or inicio >= r.fin):
                return False
        self.reservas.append(Reserva(sala, inicio, fin))
        return True

g = GestorReservas()
print(g.reservar("A", 10, 12))
print(g.reservar("A", 11, 13))


# EJERCICIO 7 — Inventario con búsqueda por nombre
class Inventario:
    def __init__(self):
        self.items = []

    def añadir(self, p):
        self.items.append(p)

    def buscar(self, nombre):
        return [i for i in self.items if nombre.lower() in i.nombre.lower()]

inv = Inventario()
inv.añadir(Producto("Teclado", 20))
inv.añadir(Producto("Teclado mecánico", 50))
print(inv.buscar("teclado"))


# EJERCICIO 8 — Curso con alumnos y nota media
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

class Curso:
    def __init__(self):
        self.alumnos = []

    def añadir(self, a):
        self.alumnos.append(a)

    def media(self):
        return sum(a.nota for a in self.alumnos) / len(self.alumnos)

c = Curso()
c.añadir(Alumno("Ana", 8))
c.añadir(Alumno("Luis", 6))
print(c.media())


# EJERCICIO 9 — Pedido con varios productos y cálculo del total
class Pedido:
    def __init__(self):
        self.lineas = []

    def añadir(self, producto, cantidad):
        self.lineas.append((producto, cantidad))

    def total(self):
        return sum(p.precio * c for p, c in self.lineas)

ped = Pedido()
ped.añadir(Producto("USB", 5), 3)
print(ped.total())


# EJERCICIO 10 — Sistema de login con bloqueo tras 3 fallos
class Login:
    def __init__(self, usuario, pwd):
        self.usuario = usuario
        self.pwd = pwd
        self.intentos = 0
        self.bloqueado = False

    def entrar(self, u, p):
        if self.bloqueado:
            return False
        if u == self.usuario and p == self.pwd:
            return True
        self.intentos += 1
        if self.intentos >= 3:
            self.bloqueado = True
        return False

l = Login("admin", "1234")
print(l.entrar("admin", "0000"))
print(l.entrar("admin", "0000"))
print(l.entrar("admin", "0000"))


# EJERCICIO 11 — Sistema de tickets con prioridad
import heapq

class Ticket:
    def __init__(self, prio, desc):
        self.prio = prio
        self.desc = desc

    def __lt__(self, other):
        return self.prio < other.prio

cola = []
heapq.heappush(cola, Ticket(2, "Error menor"))
heapq.heappush(cola, Ticket(1, "Error grave"))
print(heapq.heappop(cola).desc)


# EJERCICIO 12 — Sistema de mensajería con historial
class Chat:
    def __init__(self):
        self.msgs = []

    def enviar(self, usuario, texto):
        self.msgs.append((usuario, texto))

    def historial(self):
        return self.msgs

ch = Chat()
ch.enviar("Ana", "Hola")
ch.enviar("Luis", "Qué tal")
print(ch.historial())


# EJERCICIO 13 — Sistema de configuración tipo INI
class Config:
    def __init__(self):
        self.datos = {}

    def set(self, k, v):
        self.datos[k] = v

    def get(self, k):
        return self.datos.get(k)

cfg = Config()
cfg.set("modo", "oscuro")
print(cfg.get("modo"))


# EJERCICIO 14 — Carrito con descuento por cantidad
class Carrito:
    def __init__(self):
        self.items = []

    def añadir(self, p, c):
        self.items.append((p, c))

    def total(self):
        t = sum(p.precio * c for p, c in self.items)
        if t > 100:
            t *= 0.9
        return t

car = Carrito()
car.añadir(Producto("Monitor", 120), 1)
print(car.total())


# EJERCICIO 15 — Sistema de logs con niveles
class Logger:
    def __init__(self):
        self.logs = []

    def log(self, nivel, msg):
        self.logs.append((nivel, msg))

    def filtrar(self, nivel):
        return [m for n, m in self.logs if n == nivel]

log = Logger()
log.log("INFO", "Inicio")
log.log("ERROR", "Fallo")
print(log.filtrar("ERROR"))


# EJERCICIO 16 — Sistema de colas FIFO
from collections import deque

cola = deque()
cola.append("Tarea1")
cola.append("Tarea2")
print(cola.popleft())


# EJERCICIO 17 — Sistema de versiones con rollback
class Versionador:
    def __init__(self):
        self.hist = []

    def commit(self, estado):
        self.hist.append(estado)

    def rollback(self):
        if self.hist:
            self.hist.pop()

    def actual(self):
        return self.hist[-1] if self.hist else None

v = Versionador()
v.commit("v1")
v.commit("v2")
v.rollback()
print(v.actual())


# EJERCICIO 18 — Sistema de dependencias simple
deps = {
    "compilar": ["analizar"],
    "analizar": ["descargar"],
    "descargar": [],
}

orden = []
visit = set()

def resolver(t):
    if t in visit:
        return
    visit.add(t)
    for d in deps[t]:
        resolver(d)
    orden.append(t)

for t in deps:
    resolver(t)

print(orden)


# EJERCICIO 19 — Sistema de colisiones 2D
class Objeto:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

def colision(a, b):
    return not (a.x + a.w < b.x or b.x + b.w < a.x or
                a.y + a.h < b.y or b.y + b.h < a.y)

o1 = Objeto(0,0,10,10)
o2 = Objeto(5,5,10,10)
print(colision(o1,o2))


# EJERCICIO 20 — Sistema de colas de impresión con prioridad y tamaño
class Trabajo:
    def __init__(self, prio, tamaño, nombre):
        self.prio = prio
        self.tamaño = tamaño
        self.nombre = nombre

    def __lt__(self, other):
        return (self.prio, self.tamaño) < (other.prio, other.tamaño)

cola_imp = []
heapq.heappush(cola_imp, Trabajo(1, 50, "Doc1"))
heapq.heappush(cola_imp, Trabajo(1, 20, "Doc2"))
print(heapq.heappop(cola_imp).nombre)

# ============================================================
# TEMA 15 — EJERCICIOS COMBINADOS AVANZADOS
# ============================================================

# EJERCICIO 1 — Sistema de usuarios con login, bloqueo y guardado en fichero
class Usuario:
    def __init__(self, nombre, pwd):
        self.nombre = nombre
        self.pwd = pwd
        self.intentos = 0
        self.bloqueado = False

    def login(self, n, p):
        if self.bloqueado:
            return False
        if n == self.nombre and p == self.pwd:
            return True
        self.intentos += 1
        if self.intentos >= 3:
            self.bloqueado = True
        return False

u = Usuario("admin", "1234")
with open("logins.txt", "w") as f:
    for intento in ["0000", "1111", "1234"]:
        ok = u.login("admin", intento)
        f.write(f"{intento}:{ok}\n")


# EJERCICIO 2 — Empresa con empleados, departamentos y cálculo de sueldos por departamento
class Empleado:
    def __init__(self, nombre, sueldo, dept):
        self.nombre = nombre
        self.sueldo = sueldo
        self.dept = dept

class Empresa:
    def __init__(self):
        self.empleados = []

    def añadir(self, e):
        self.empleados.append(e)

    def total_dept(self, dept):
        return sum(e.sueldo for e in self.empleados if e.dept == dept)

emp = Empresa()
emp.añadir(Empleado("Ana", 1200, "IT"))
emp.añadir(Empleado("Luis", 1500, "IT"))
emp.añadir(Empleado("Marta", 1000, "HR"))
print(emp.total_dept("IT"))


# EJERCICIO 3 — Sistema de cursos con alumnos, notas y guardado en CSV
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

class Curso:
    def __init__(self):
        self.alumnos = []

    def añadir(self, a):
        self.alumnos.append(a)

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for a in self.alumnos:
                f.write(f"{a.nombre};{a.nota}\n")

c = Curso()
c.añadir(Alumno("Ana", 8))
c.añadir(Alumno("Luis", 6))
c.guardar("curso.csv")


# EJERCICIO 4 — Cargar curso desde CSV y calcular media
alumnos = []
with open("curso.csv") as f:
    for linea in f:
        n, nota = linea.strip().split(";")
        alumnos.append(Alumno(n, float(nota)))
print(sum(a.nota for a in alumnos) / len(alumnos))


# EJERCICIO 5 — Inventario con productos, stock y reposición automática
class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock

class Inventario:
    def __init__(self):
        self.items = []

    def añadir(self, p):
        self.items.append(p)

    def reponer(self, minimo, cantidad):
        for p in self.items:
            if p.stock < minimo:
                p.stock += cantidad

inv = Inventario()
inv.añadir(Producto("USB", 2))
inv.añadir(Producto("Monitor", 10))
inv.reponer(5, 10)
print([(p.nombre, p.stock) for p in inv.items])


# EJERCICIO 6 — Sistema de pedidos con validación de stock
class Pedido:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def procesar(self):
        if self.producto.stock >= self.cantidad:
            self.producto.stock -= self.cantidad
            return True
        return False

p = Pedido(inv.items[0], 5)
print(p.procesar())


# EJERCICIO 7 — Biblioteca con préstamos, devoluciones y registro en fichero
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.prestado = False

class Biblioteca:
    def __init__(self):
        self.libros = []

    def añadir(self, l):
        self.libros.append(l)

    def prestar(self, titulo):
        for l in self.libros:
            if l.titulo == titulo and not l.prestado:
                l.prestado = True
                return True
        return False

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for l in self.libros:
                f.write(f"{l.titulo};{l.prestado}\n")

b = Biblioteca()
b.añadir(Libro("Python"))
b.prestar("Python")
b.guardar("biblioteca.txt")


# EJERCICIO 8 — Cargar biblioteca desde fichero
libros = []
with open("biblioteca.txt") as f:
    for linea in f:
        t, p = linea.strip().split(";")
        l = Libro(t)
        l.prestado = (p == "True")
        libros.append(l)
print([(l.titulo, l.prestado) for l in libros])


# EJERCICIO 9 — Sistema de tickets con prioridad y registro de tiempo
import heapq, time

class Ticket:
    def __init__(self, prio, desc):
        self.prio = prio
        self.desc = desc
        self.t = time.time()

    def __lt__(self, other):
        return (self.prio, self.t) < (other.prio, other.t)

cola = []
heapq.heappush(cola, Ticket(2, "Error menor"))
heapq.heappush(cola, Ticket(1, "Error grave"))
print(heapq.heappop(cola).desc)


# EJERCICIO 10 — Sistema de configuración con lectura y escritura tipo INI
class Config:
    def __init__(self):
        self.datos = {}

    def set(self, k, v):
        self.datos[k] = v

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for k, v in self.datos.items():
                f.write(f"{k}={v}\n")

    def cargar(self, ruta):
        with open(ruta) as f:
            for linea in f:
                k, v = linea.strip().split("=")
                self.datos[k] = v

cfg = Config()
cfg.set("modo", "oscuro")
cfg.guardar("config.ini")
cfg2 = Config()
cfg2.cargar("config.ini")
print(cfg2.datos)


# EJERCICIO 11 — Sistema de colas con reintentos y log de errores
from collections import deque

tareas = deque(["A", "B", "C"])
intentos = {}

with open("errores.txt", "w") as log:
    while tareas:
        t = tareas.popleft()
        intentos[t] = intentos.get(t, 0) + 1
        try:
            if t == "B" and intentos[t] < 3:
                raise ValueError("Fallo temporal")
            print("OK:", t)
        except Exception as e:
            log.write(f"{t}:{e}\n")
            if intentos[t] < 3:
                tareas.append(t)


# EJERCICIO 12 — Sistema de versiones con historial y rollback múltiple
class Versionador:
    def __init__(self):
        self.hist = []

    def commit(self, estado):
        self.hist.append(estado)

    def rollback(self, n):
        for _ in range(n):
            if self.hist:
                self.hist.pop()

    def actual(self):
        return self.hist[-1] if self.hist else None

v = Versionador()
v.commit("v1")
v.commit("v2")
v.commit("v3")
v.rollback(2)
print(v.actual())


# EJERCICIO 13 — Sistema de dependencias con detección de ciclos
grafo = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"],
}

visit = set()
pila = set()
ciclo = False

def dfs(n):
    global ciclo
    if n in pila:
        ciclo = True
        return
    if n in visit:
        return
    visit.add(n)
    pila.add(n)
    for v in grafo[n]:
        dfs(v)
    pila.remove(n)

for n in grafo:
    dfs(n)

print("Ciclo:", ciclo)


# EJERCICIO 14 — Sistema de logs rotativos por tamaño
import os

def escribir_log(msg):
    if os.path.exists("log.txt") and os.path.getsize("log.txt") > 50:
        os.rename("log.txt", "log_old.txt")
    with open("log.txt", "a") as f:
        f.write(msg + "\n")

for i in range(20):
    escribir_log(f"Evento {i}")


# EJERCICIO 15 — Motor de plantillas con variables
def render(plantilla, ctx):
    for k, v in ctx.items():
        plantilla = plantilla.replace("{{" + k + "}}", str(v))
    return plantilla

print(render("Hola {{nombre}}", {"nombre": "Antuan"}))


# EJERCICIO 16 — Sistema de colisiones 2D
class Objeto:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

def colision(a, b):
    return not (a.x + a.w < b.x or b.x + b.w < a.x or
                a.y + a.h < b.y or b.y + b.h < a.y)

o1 = Objeto(0,0,10,10)
o2 = Objeto(5,5,10,10)
print(colision(o1,o2))


# EJERCICIO 17 — Sistema de colas paralelas con balanceo
from collections import deque

colas = [deque(), deque(), deque()]
tareas = ["A","B","C","D","E","F","G"]

for i, t in enumerate(tareas):
    colas[i % len(colas)].append(t)

print([list(c) for c in colas])


# EJERCICIO 18 — Sistema de métricas con media y máximo
class Metricas:
    def __init__(self):
        self.valores = []

    def registrar(self, v):
        self.valores.append(v)

    def media(self):
        return sum(self.valores)/len(self.valores)

    def maximo(self):
        return max(self.valores)

m = Metricas()
for v in [1,5,3,10]:
    m.registrar(v)
print(m.media(), m.maximo())


# EJERCICIO 19 — Árbol binario de búsqueda con inserción y búsqueda
class Nodo:
    def __init__(self, v):
        self.v = v
        self.izq = None
        self.der = None

class ABB:
    def __init__(self):
        self.r = None

    def insertar(self, v):
        if not self.r:
            self.r = Nodo(v)
        else:
            self._ins(self.r, v)

    def _ins(self, n, v):
        if v < n.v:
            if n.izq:
                self._ins(n.izq, v)
            else:
                n.izq = Nodo(v)
        else:
            if n.der:
                self._ins(n.der, v)
            else:
                n.der = Nodo(v)

    def buscar(self, v):
        return self._bus(self.r, v)

    def _bus(self, n, v):
        if not n:
            return False
        if v == n.v:
            return True
        if v < n.v:
            return self._bus(n.izq, v)
        return self._bus(n.der, v)

abb = ABB()
for n in [5,3,7,2,4,6,8]:
    abb.insertar(n)
print(abb.buscar(4))


# EJERCICIO 20 — Sistema de impresión con prioridad y tamaño
import heapq

class Trabajo:
    def __init__(self, prio, tamaño, nombre):
        self.prio = prio
        self.tamaño = tamaño
        self.nombre = nombre

    def __lt__(self, other):
        return (self.prio, self.tamaño) < (other.prio, other.tamaño)

cola_imp = []
heapq.heappush(cola_imp, Trabajo(1, 50, "Doc1"))
heapq.heappush(cola_imp, Trabajo(1, 20, "Doc2"))
print(heapq.heappop(cola_imp).nombre)

# ============================================================
# EJERCICIO 1 — SISTEMA DE GESTIÓN DE CURSOS COMPLETO
# ============================================================

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def añadir_nota(self, n):
        self.notas.append(n)

    def media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0


class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.alumnos = []

    def matricular(self, alumno):
        self.alumnos.append(alumno)

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            f.write(f"Curso:{self.nombre}\n")
            f.write(f"Profesor:{self.profesor.nombre}\n")
            for a in self.alumnos:
                notas = ",".join(map(str, a.notas))
                f.write(f"{a.nombre};{notas}\n")

    def cargar(self, ruta):
        with open(ruta) as f:
            next(f)
            next(f)
            for linea in f:
                n, notas = linea.strip().split(";")
                a = Alumno(n)
                if notas:
                    for x in notas.split(","):
                        a.añadir_nota(float(x))
                self.alumnos.append(a)

    def top(self):
        return max(self.alumnos, key=lambda x: x.media())


p = Profesor("Ana")
c = Curso("Python", p)
a1 = Alumno("Luis"); a1.añadir_nota(8); a1.añadir_nota(9)
a2 = Alumno("Marta"); a2.añadir_nota(5); a2.añadir_nota(7)
c.matricular(a1); c.matricular(a2)
c.guardar("curso.txt")

c2 = Curso("Python", p)
c2.cargar("curso.txt")
print(c2.top().nombre)

# ============================================================
# EJERCICIO 2 — EMPRESA COMPLETA CON DEPARTAMENTOS Y NÓMINAS
# ============================================================

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo


class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def añadir(self, e):
        self.empleados.append(e)

    def total(self):
        return sum(e.sueldo for e in self.empleados)


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.depts = []

    def añadir_dept(self, d):
        self.depts.append(d)

    def nomina_total(self):
        return sum(d.total() for d in self.depts)

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for d in self.depts:
                for e in d.empleados:
                    f.write(f"{d.nombre};{e.nombre};{e.sueldo}\n")

    def cargar(self, ruta):
        with open(ruta) as f:
            for linea in f:
                dept, nom, su = linea.strip().split(";")
                d = next((x for x in self.depts if x.nombre == dept), None)
                if not d:
                    d = Departamento(dept)
                    self.depts.append(d)
                d.añadir(Empleado(nom, float(su)))


e = Empresa("Tech")
d1 = Departamento("IT")
d1.añadir(Empleado("Ana", 1200))
d1.añadir(Empleado("Luis", 1500))
e.añadir_dept(d1)
e.guardar("empresa.txt")

e2 = Empresa("Tech")
e2.cargar("empresa.txt")
print(e2.nomina_total())

# ============================================================
# EJERCICIO 3 — BIBLIOTECA COMPLETA CON MULTAS
# ============================================================

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre


class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.prestado = False
        self.dias = 0


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.prestamos = {}

    def añadir(self, libro):
        self.libros.append(libro)

    def prestar(self, usuario, titulo):
        for l in self.libros:
            if l.titulo == titulo and not l.prestado:
                l.prestado = True
                self.prestamos[usuario.nombre] = l
                return True
        return False

    def pasar_dia(self):
        for l in self.libros:
            if l.prestado:
                l.dias += 1

    def multa(self, usuario):
        l = self.prestamos.get(usuario.nombre)
        if not l:
            return 0
        return max(0, l.dias - 7) * 0.5


b = Biblioteca()
b.añadir(Libro("Python"))
u = Usuario("Ana")
b.prestar(u, "Python")
for _ in range(10):
    b.pasar_dia()
print(b.multa(u))

# ============================================================
# EJERCICIO 4 — SISTEMA DE PEDIDOS COMPLETO
# ============================================================

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


class Inventario:
    def __init__(self):
        self.items = []

    def añadir(self, p):
        self.items.append(p)

    def buscar(self, nombre):
        for p in self.items:
            if p.nombre == nombre:
                return p
        return None


class Pedido:
    def __init__(self):
        self.lineas = []

    def añadir(self, producto, cantidad):
        if producto.stock < cantidad:
            raise ValueError("Stock insuficiente")
        producto.stock -= cantidad
        self.lineas.append((producto, cantidad))

    def total(self):
        return sum(p.precio * c for p, c in self.lineas)


class Factura:
    def __init__(self, pedido):
        self.pedido = pedido

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for p, c in self.pedido.lineas:
                f.write(f"{p.nombre};{c};{p.precio}\n")
            f.write(f"TOTAL;{self.pedido.total()}\n")


inv = Inventario()
inv.añadir(Producto("USB", 5, 10))
inv.añadir(Producto("Monitor", 120, 3))

ped = Pedido()
ped.añadir(inv.buscar("USB"), 4)
ped.añadir(inv.buscar("Monitor"), 1)

f = Factura(ped)
f.guardar("factura.txt")
print(ped.total())

# ============================================================
# EJERCICIO 5 — SISTEMA DE RESERVAS COMPLETO
# ============================================================

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre


class Reserva:
    def __init__(self, usuario, sala, inicio, fin):
        self.usuario = usuario
        self.sala = sala
        self.inicio = inicio
        self.fin = fin


class GestorReservas:
    def __init__(self):
        self.reservas = []

    def reservar(self, usuario, sala, inicio, fin):
        for r in self.reservas:
            if r.sala == sala and not (fin <= r.inicio or inicio >= r.fin):
                return False
        self.reservas.append(Reserva(usuario, sala, inicio, fin))
        return True

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for r in self.reservas:
                f.write(f"{r.usuario.nombre};{r.sala};{r.inicio};{r.fin}\n")

    def cargar(self, ruta):
        with open(ruta) as f:
            for linea in f:
                u, s, i, fn = linea.strip().split(";")
                self.reservas.append(Reserva(Usuario(u), s, int(i), int(fn)))


g = GestorReservas()
u1 = Usuario("Ana")
g.reservar(u1, "Sala1", 10, 12)
g.reservar(u1, "Sala1", 12, 14)
g.guardar("reservas.txt")

g2 = GestorReservas()
g2.cargar("reservas.txt")
print(len(g2.reservas))

# ============================================================
# EJERCICIO 1 — TIENDA ONLINE COMPLETA
# ============================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []


class Tienda:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, p):
        self.productos.append(p)

    def buscar(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None


class Pedido:
    def __init__(self, usuario):
        self.usuario = usuario
        self.lineas = []

    def añadir(self, producto, cantidad):
        if producto.stock < cantidad:
            raise ValueError("Stock insuficiente")
        producto.stock -= cantidad
        self.lineas.append((producto, cantidad))

    def total(self):
        return sum(p.precio * c for p, c in self.lineas)


class Factura:
    def __init__(self, pedido):
        self.pedido = pedido

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            f.write(f"Usuario:{self.pedido.usuario.nombre}\n")
            for p, c in self.pedido.lineas:
                f.write(f"{p.codigo};{p.nombre};{c};{p.precio}\n")
            f.write(f"TOTAL;{self.pedido.total()}\n")


t = Tienda()
t.añadir_producto(Producto("P1", "USB", 5, 10))
t.añadir_producto(Producto("P2", "Monitor", 120, 3))

u = Usuario("Ana")
ped = Pedido(u)
ped.añadir(t.buscar("P1"), 4)
ped.añadir(t.buscar("P2"), 1)

f = Factura(ped)
f.guardar("factura_tienda.txt")
print(ped.total())

# ============================================================
# EJERCICIO 2 — UNIVERSIDAD COMPLETA
# ============================================================

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}

    def poner_nota(self, asignatura, nota):
        self.notas[asignatura] = nota

    def media(self):
        return sum(self.notas.values()) / len(self.notas) if self.notas else 0


class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre


class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.alumnos = []

    def matricular(self, alumno):
        self.alumnos.append(alumno)

    def media_asignatura(self):
        notas = [a.notas.get(self.nombre, 0) for a in self.alumnos]
        return sum(notas) / len(notas) if notas else 0

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            f.write(f"Asignatura:{self.nombre}\n")
            f.write(f"Profesor:{self.profesor.nombre}\n")
            for a in self.alumnos:
                f.write(f"{a.nombre};{a.notas.get(self.nombre, 0)}\n")

    def cargar(self, ruta):
        with open(ruta) as f:
            next(f)
            next(f)
            for linea in f:
                n, nota = linea.strip().split(";")
                a = Alumno(n)
                a.poner_nota(self.nombre, float(nota))
                self.alumnos.append(a)


p = Profesor("Carlos")
a = Asignatura("Programación", p)

al1 = Alumno("Ana"); al1.poner_nota("Programación", 8)
al2 = Alumno("Luis"); al2.poner_nota("Programación", 6)

a.matricular(al1)
a.matricular(al2)
a.guardar("asignatura.txt")

a2 = Asignatura("Programación", p)
a2.cargar("asignatura.txt")
print(a2.media_asignatura())

# ============================================================
# EJERCICIO 3 — BIBLIOTECA DIGITAL COMPLETA
# ============================================================

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []


class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.prestado = False
        self.dias = 0


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.prestamos = {}

    def añadir(self, libro):
        self.libros.append(libro)

    def prestar(self, usuario, titulo):
        for l in self.libros:
            if l.titulo == titulo and not l.prestado:
                l.prestado = True
                self.prestamos[usuario.nombre] = l
                usuario.historial.append(f"Prestado:{titulo}")
                return True
        return False

    def pasar_dia(self):
        for l in self.libros:
            if l.prestado:
                l.dias += 1

    def devolver(self, usuario):
        l = self.prestamos.get(usuario.nombre)
        if not l:
            return 0
        multa = max(0, l.dias - 7) * 0.5
        l.prestado = False
        l.dias = 0
        usuario.historial.append(f"Devuelto:{l.titulo}")
        del self.prestamos[usuario.nombre]
        return multa

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for l in self.libros:
                f.write(f"{l.titulo};{l.prestado};{l.dias}\n")

    def cargar(self, ruta):
        with open(ruta) as f:
            for linea in f:
                t, p, d = linea.strip().split(";")
                l = Libro(t)
                l.prestado = (p == "True")
                l.dias = int(d)
                self.libros.append(l)


b = Biblioteca()
b.añadir(Libro("Python"))
u = Usuario("Ana")
b.prestar(u, "Python")
for _ in range(10):
    b.pasar_dia()
print(b.devolver(u))

# ============================================================
# EJERCICIO 4 — RESTAURANTE COMPLETO
# ============================================================

class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


class Reserva:
    def __init__(self, cliente, mesa, hora):
        self.cliente = cliente
        self.mesa = mesa
        self.hora = hora


class Restaurante:
    def __init__(self):
        self.mesas = []
        self.reservas = []

    def añadir_mesa(self, m):
        self.mesas.append(m)

    def reservar(self, cliente, personas, hora):
        for m in self.mesas:
            if not m.ocupada and m.capacidad >= personas:
                m.ocupada = True
                r = Reserva(cliente, m, hora)
                self.reservas.append(r)
                return True
        return False

    def liberar(self, mesa):
        mesa.ocupada = False

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for r in self.reservas:
                f.write(f"{r.cliente.nombre};{r.mesa.numero};{r.hora}\n")


rest = Restaurante()
rest.añadir_mesa(Mesa(1, 4))
rest.añadir_mesa(Mesa(2, 2))

c = Cliente("Ana")
rest.reservar(c, 2, "20:00")
rest.guardar("reservas_rest.txt")
print(len(rest.reservas))

# ============================================================
# EJERCICIO 5 — GESTIÓN DE PROYECTOS COMPLETA
# ============================================================

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre


class Tarea:
    def __init__(self, nombre, horas):
        self.nombre = nombre
        self.horas = horas
        self.estado = "pendiente"
        self.empleado = None


class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def añadir_tarea(self, t):
        self.tareas.append(t)

    def asignar(self, tarea, empleado):
        tarea.empleado = empleado

    def completar(self, tarea):
        tarea.estado = "completada"

    def horas_totales(self):
        return sum(t.horas for t in self.tareas)

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for t in self.tareas:
                emp = t.empleado.nombre if t.empleado else "None"
                f.write(f"{t.nombre};{t.horas};{t.estado};{emp}\n")


p = Proyecto("App Móvil")
t1 = Tarea("Diseño", 10)
t2 = Tarea("Backend", 30)
p.añadir_tarea(t1)
p.añadir_tarea(t2)

e = Empleado("Ana")
p.asignar(t1, e)
p.completar(t1)

p.guardar("proyecto.txt")
print(p.horas_totales())

# ============================================================
# EJERCICIO 1 — BIBLIOTECA MUNICIPAL COMPLETA
# ============================================================

class Usuario:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.historial = []


class Libro:
    def __init__(self, codigo, titulo, categoria):
        self.codigo = codigo
        self.titulo = titulo
        self.categoria = categoria
        self.prestado = False
        self.dias = 0


class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.libros = []
        self.prestamos = {}

    def registrar_usuario(self, u):
        self.usuarios.append(u)

    def añadir_libro(self, l):
        self.libros.append(l)

    def buscar_libro(self, texto):
        return [l for l in self.libros if texto.lower() in l.titulo.lower()]

    def prestar(self, dni, codigo):
        u = next((x for x in self.usuarios if x.dni == dni), None)
        l = next((x for x in self.libros if x.codigo == codigo), None)
        if not u or not l or l.prestado:
            return False
        l.prestado = True
        self.prestamos[dni] = l
        u.historial.append(f"Prestado:{l.titulo}")
        return True

    def pasar_dia(self):
        for l in self.libros:
            if l.prestado:
                l.dias += 1

    def devolver(self, dni):
        l = self.prestamos.get(dni)
        if not l:
            return 0
        multa = max(0, l.dias - 7) * 0.5
        l.prestado = False
        l.dias = 0
        del self.prestamos[dni]
        return multa

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for l in self.libros:
                f.write(f"{l.codigo};{l.titulo};{l.categoria};{l.prestado};{l.dias}\n")

    def cargar(self, ruta):
        with open(ruta) as f:
            for linea in f:
                c, t, cat, p, d = linea.strip().split(";")
                l = Libro(c, t, cat)
                l.prestado = (p == "True")
                l.dias = int(d)
                self.libros.append(l)


b = Biblioteca()
b.registrar_usuario(Usuario("111A", "Ana"))
b.añadir_libro(Libro("L1", "Python Básico", "Programación"))
b.prestar("111A", "L1")
for _ in range(10):
    b.pasar_dia()
print(b.devolver("111A"))

# ============================================================
# EJERCICIO 2 — HOTEL COMPLETO
# ============================================================

class Cliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Habitacion:
    def __init__(self, numero, capacidad, precio):
        self.numero = numero
        self.capacidad = capacidad
        self.precio = precio
        self.ocupada = False


class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias


class Hotel:
    def __init__(self):
        self.habitaciones = []
        self.reservas = []

    def añadir_habitacion(self, h):
        self.habitaciones.append(h)

    def reservar(self, cliente, personas, dias):
        for h in self.habitaciones:
            if not h.ocupada and h.capacidad >= personas:
                h.ocupada = True
                r = Reserva(cliente, h, dias)
                self.reservas.append(r)
                return True
        return False

    def checkout(self, cliente):
        for r in self.reservas:
            if r.cliente.dni == cliente.dni:
                r.habitacion.ocupada = False
                total = r.habitacion.precio * r.dias
                self.reservas.remove(r)
                return total
        return 0

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for r in self.reservas:
                f.write(f"{r.cliente.dni};{r.habitacion.numero};{r.dias}\n")


h = Hotel()
h.añadir_habitacion(Habitacion(101, 2, 50))
h.añadir_habitacion(Habitacion(102, 4, 80))

c = Cliente("111A", "Ana")
h.reservar(c, 2, 3)
print(h.checkout(c))

# ============================================================
# EJERCICIO 3 — BIBLIOTECA DE MÚSICA COMPLETA
# ============================================================

class Cancion:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion


class Album:
    def __init__(self, nombre, artista):
        self.nombre = nombre
        self.artista = artista
        self.canciones = []

    def añadir(self, c):
        self.canciones.append(c)

    def duracion_total(self):
        return sum(c.duracion for c in self.canciones)


class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.temas = []

    def añadir(self, c):
        self.temas.append(c)

    def duracion(self):
        return sum(c.duracion for c in self.temas)


class BibliotecaMusical:
    def __init__(self):
        self.albums = []

    def añadir_album(self, a):
        self.albums.append(a)

    def buscar(self, texto):
        res = []
        for a in self.albums:
            if texto.lower() in a.nombre.lower() or texto.lower() in a.artista.lower():
                res.append(a)
        return res

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for a in self.albums:
                for c in a.canciones:
                    f.write(f"{a.nombre};{a.artista};{c.titulo};{c.duracion}\n")


bm = BibliotecaMusical()
al = Album("Greatest Hits", "Queen")
al.añadir(Cancion("Bohemian Rhapsody", 6))
al.añadir(Cancion("Don't Stop Me Now", 3))
bm.añadir_album(al)
print(al.duracion_total())

# ============================================================
# EJERCICIO 4 — CURSOS ONLINE COMPLETOS
# ============================================================

class Leccion:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion


class Modulo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lecciones = []

    def añadir(self, l):
        self.lecciones.append(l)

    def duracion(self):
        return sum(l.duracion for l in self.lecciones)


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.modulos = []
        self.progreso = {}

    def añadir_modulo(self, m):
        self.modulos.append(m)

    def matricular(self, alumno):
        self.progreso[alumno] = 0

    def avanzar(self, alumno, minutos):
        self.progreso[alumno] += minutos

    def duracion_total(self):
        return sum(m.duracion() for m in self.modulos)


c = Curso("Python Avanzado")
m1 = Modulo("POO")
m1.añadir(Leccion("Clases", 10))
m1.añadir(Leccion("Herencia", 15))
c.añadir_modulo(m1)

c.matricular("Ana")
c.avanzar("Ana", 20)
print(c.progreso["Ana"])

# ============================================================
# EJERCICIO 5 — EMPRESA DE ENVÍOS COMPLETA
# ============================================================

class Cliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Paquete:
    def __init__(self, codigo, peso):
        self.codigo = codigo
        self.peso = peso


class Envio:
    def __init__(self, cliente, paquete, destino):
        self.cliente = cliente
        self.paquete = paquete
        self.destino = destino
        self.estado = "pendiente"


class EmpresaEnvios:
    def __init__(self):
        self.envios = []

    def registrar_envio(self, e):
        self.envios.append(e)

    def cambiar_estado(self, codigo, nuevo):
        for e in self.envios:
            if e.paquete.codigo == codigo:
                e.estado = nuevo

    def pendientes(self):
        return [e for e in self.envios if e.estado == "pendiente"]

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for e in self.envios:
                f.write(f"{e.cliente.dni};{e.paquete.codigo};{e.paquete.peso};{e.destino};{e.estado}\n")


cli = Cliente("111A", "Ana")
paq = Paquete("P1", 2.5)
env = Envio(cli, paq, "Madrid")

emp = EmpresaEnvios()
emp.registrar_envio(env)
emp.cambiar_estado("P1", "en tránsito")
print(len(emp.pendientes()))

# ============================================================
# EJERCICIO 1 — CLÍNICA MÉDICA COMPLETA
# ============================================================

class Paciente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.historial = []


class Medico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad


class Cita:
    def __init__(self, paciente, medico, fecha, motivo):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.motivo = motivo


class Clinica:
    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.citas = []

    def registrar_paciente(self, p):
        self.pacientes.append(p)

    def registrar_medico(self, m):
        self.medicos.append(m)

    def pedir_cita(self, dni, medico_nombre, fecha, motivo):
        p = next((x for x in self.pacientes if x.dni == dni), None)
        m = next((x for x in self.medicos if x.nombre == medico_nombre), None)
        if not p or not m:
            return False
        c = Cita(p, m, fecha, motivo)
        self.citas.append(c)
        p.historial.append(f"Cita:{fecha}:{motivo}")
        return True

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for c in self.citas:
                f.write(f"{c.paciente.dni};{c.medico.nombre};{c.fecha};{c.motivo}\n")

    def cargar(self, ruta):
        with open(ruta) as f:
            for linea in f:
                dni, med, fecha, motivo = linea.strip().split(";")
                p = next((x for x in self.pacientes if x.dni == dni), None)
                m = next((x for x in self.medicos if x.nombre == med), None)
                if p and m:
                    self.citas.append(Cita(p, m, fecha, motivo))


cl = Clinica()
cl.registrar_paciente(Paciente("111A", "Ana"))
cl.registrar_medico(Medico("Dr. Luis", "Cardiología"))
cl.pedir_cita("111A", "Dr. Luis", "2025-01-10", "Revisión")
cl.guardar("citas.txt")
print(len(cl.citas))

# ============================================================
# EJERCICIO 2 — BIBLIOTECA DE PELÍCULAS COMPLETA
# ============================================================

class Pelicula:
    def __init__(self, codigo, titulo, director, año):
        self.codigo = codigo
        self.titulo = titulo
        self.director = director
        self.año = año
        self.valoraciones = []

    def valorar(self, nota):
        self.valoraciones.append(nota)

    def media(self):
        return sum(self.valoraciones)/len(self.valoraciones) if self.valoraciones else 0


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vistas = []


class Videoteca:
    def __init__(self):
        self.peliculas = []
        self.usuarios = []

    def añadir_pelicula(self, p):
        self.peliculas.append(p)

    def registrar_usuario(self, u):
        self.usuarios.append(u)

    def ver(self, usuario, codigo):
        u = next((x for x in self.usuarios if x.nombre == usuario), None)
        p = next((x for x in self.peliculas if x.codigo == codigo), None)
        if u and p:
            u.vistas.append(p)
            return True
        return False

    def recomendar(self, usuario):
        u = next((x for x in self.usuarios if x.nombre == usuario), None)
        if not u:
            return None
        vistas = {p.codigo for p in u.vistas}
        no_vistas = [p for p in self.peliculas if p.codigo not in vistas]
        if not no_vistas:
            return None
        return max(no_vistas, key=lambda x: x.media())

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for p in self.peliculas:
                notas = ",".join(map(str, p.valoraciones))
                f.write(f"{p.codigo};{p.titulo};{p.director};{p.año};{notas}\n")


v = Videoteca()
p1 = Pelicula("P1", "Matrix", "Wachowski", 1999)
p1.valorar(10); p1.valorar(9)
v.añadir_pelicula(p1)
v.registrar_usuario(Usuario("Ana"))
v.ver("Ana", "P1")
print(p1.media())

# ============================================================
# EJERCICIO 3 — TALLER MECÁNICO COMPLETO
# ============================================================

class Cliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Vehiculo:
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo


class Reparacion:
    def __init__(self, vehiculo, descripcion, coste):
        self.vehiculo = vehiculo
        self.descripcion = descripcion
        self.coste = coste


class Taller:
    def __init__(self):
        self.clientes = []
        self.vehiculos = []
        self.reparaciones = []

    def registrar_cliente(self, c):
        self.clientes.append(c)

    def registrar_vehiculo(self, v):
        self.vehiculos.append(v)

    def reparar(self, matricula, descripcion, coste):
        v = next((x for x in self.vehiculos if x.matricula == matricula), None)
        if not v:
            return False
        r = Reparacion(v, descripcion, coste)
        self.reparaciones.append(r)
        return True

    def factura(self, matricula):
        return sum(r.coste for r in self.reparaciones if r.vehiculo.matricula == matricula)

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for r in self.reparaciones:
                f.write(f"{r.vehiculo.matricula};{r.descripcion};{r.coste}\n")


t = Taller()
t.registrar_cliente(Cliente("111A", "Ana"))
t.registrar_vehiculo(Vehiculo("1234ABC", "Seat Ibiza"))
t.reparar("1234ABC", "Cambio aceite", 50)
t.reparar("1234ABC", "Frenos", 120)
print(t.factura("1234ABC"))

# ============================================================
# EJERCICIO 4 — BIBLIOTECA DE CURSOS COMPLETA
# ============================================================

class Leccion:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion


class Modulo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lecciones = []

    def añadir(self, l):
        self.lecciones.append(l)

    def duracion(self):
        return sum(l.duracion for l in self.lecciones)


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.modulos = []
        self.progreso = {}

    def añadir_modulo(self, m):
        self.modulos.append(m)

    def matricular(self, alumno):
        self.progreso[alumno] = 0

    def avanzar(self, alumno, minutos):
        self.progreso[alumno] += minutos

    def duracion_total(self):
        return sum(m.duracion() for m in self.modulos)


c = Curso("Python", "Carlos")
m = Modulo("POO")
m.añadir(Leccion("Clases", 10))
m.añadir(Leccion("Herencia", 15))
c.añadir_modulo(m)
c.matricular("Ana")
c.avanzar("Ana", 20)
print(c.progreso["Ana"])

# ============================================================
# EJERCICIO 5 — ALMACÉN Y ENVÍOS COMPLETO
# ============================================================

class Producto:
    def __init__(self, codigo, nombre, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock


class Almacen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def añadir(self, p):
        self.productos.append(p)

    def mover(self, codigo, cantidad, destino):
        p = next((x for x in self.productos if x.codigo == codigo), None)
        if not p or p.stock < cantidad:
            return False
        p.stock -= cantidad
        destino.recibir(codigo, cantidad)
        return True

    def recibir(self, codigo, cantidad):
        p = next((x for x in self.productos if x.codigo == codigo), None)
        if p:
            p.stock += cantidad
        else:
            self.productos.append(Producto(codigo, "Desconocido", cantidad))


a1 = Almacen("Central")
a2 = Almacen("Secundario")

a1.añadir(Producto("P1", "USB", 10))
a1.mover("P1", 5, a2)
print([(p.codigo, p.stock) for p in a1.productos])
print([(p.codigo, p.stock) for p in a2.productos])

# ============================================================
# EJERCICIO 1 — BIBLIOTECA ESCOLAR COMPLETA
# ============================================================

class Persona:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Libro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
        self.dias = 0


class Biblioteca:
    def __init__(self):
        self.personas = []
        self.libros = []
        self.prestamos = {}

    def registrar_persona(self, p):
        self.personas.append(p)

    def añadir_libro(self, l):
        self.libros.append(l)

    def buscar(self, texto):
        return [l for l in self.libros if texto.lower() in l.titulo.lower()]

    def prestar(self, dni, codigo):
        p = next((x for x in self.personas if x.dni == dni), None)
        l = next((x for x in self.libros if x.codigo == codigo), None)
        if not p or not l or l.prestado:
            return False
        l.prestado = True
        self.prestamos[dni] = l
        return True

    def pasar_dia(self):
        for l in self.libros:
            if l.prestado:
                l.dias += 1

    def devolver(self, dni):
        l = self.prestamos.get(dni)
        if not l:
            return 0
        multa = max(0, l.dias - 7) * 0.5
        l.prestado = False
        l.dias = 0
        del self.prestamos[dni]
        return multa

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for l in self.libros:
                f.write(f"{l.codigo};{l.titulo};{l.autor};{l.prestado};{l.dias}\n")

    def cargar(self, ruta):
        with open(ruta) as f:
            for linea in f:
                c, t, a, p, d = linea.strip().split(";")
                l = Libro(c, t, a)
                l.prestado = (p == "True")
                l.dias = int(d)
                self.libros.append(l)


b = Biblioteca()
b.registrar_persona(Persona("111A", "Ana"))
b.añadir_libro(Libro("L1", "Python Básico", "Guido"))
b.prestar("111A", "L1")
for _ in range(10):
    b.pasar_dia()
print(b.devolver("111A"))

# ============================================================
# EJERCICIO 2 — RESTAURANTE COMPLETO CON COCINA
# ============================================================

class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Pedido:
    def __init__(self, mesa):
        self.mesa = mesa
        self.platos = []

    def añadir(self, plato):
        self.platos.append(plato)

    def total(self):
        return sum(p.precio for p in self.platos)


class Restaurante:
    def __init__(self):
        self.mesas = []
        self.platos = []
        self.pedidos = []

    def añadir_mesa(self, m):
        self.mesas.append(m)

    def añadir_plato(self, p):
        self.platos.append(p)

    def reservar(self, personas):
        for m in self.mesas:
            if not m.ocupada and m.capacidad >= personas:
                m.ocupada = True
                return m
        return None

    def pedir(self, mesa, plato_nombre):
        p = next((x for x in self.platos if x.nombre == plato_nombre), None)
        if not p:
            return False
        ped = next((x for x in self.pedidos if x.mesa == mesa), None)
        if not ped:
            ped = Pedido(mesa)
            self.pedidos.append(ped)
        ped.añadir(p)
        return True

    def factura(self, mesa):
        ped = next((x for x in self.pedidos if x.mesa == mesa), None)
        if not ped:
            return 0
        mesa.ocupada = False
        return ped.total()


r = Restaurante()
r.añadir_mesa(Mesa(1, 4))
r.añadir_plato(Plato("Pasta", 10))
r.añadir_plato(Plato("Pizza", 12))

m = r.reservar(2)
r.pedir(m, "Pasta")
r.pedir(m, "Pizza")
print(r.factura(m))

# ============================================================
# EJERCICIO 3 — EMPRESA DE TRANSPORTE COMPLETA
# ============================================================

class Conductor:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Vehiculo:
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo


class Envio:
    def __init__(self, codigo, destino, peso):
        self.codigo = codigo
        self.destino = destino
        self.peso = peso
        self.estado = "pendiente"
        self.conductor = None
        self.vehiculo = None


class EmpresaTransporte:
    def __init__(self):
        self.conductores = []
        self.vehiculos = []
        self.envios = []

    def registrar_conductor(self, c):
        self.conductores.append(c)

    def registrar_vehiculo(self, v):
        self.vehiculos.append(v)

    def registrar_envio(self, e):
        self.envios.append(e)

    def asignar(self, codigo, dni, matricula):
        e = next((x for x in self.envios if x.codigo == codigo), None)
        c = next((x for x in self.conductores if x.dni == dni), None)
        v = next((x for x in self.vehiculos if x.matricula == matricula), None)
        if e and c and v:
            e.conductor = c
            e.vehiculo = v
            return True
        return False

    def cambiar_estado(self, codigo, estado):
        e = next((x for x in self.envios if x.codigo == codigo), None)
        if e:
            e.estado = estado

    def pendientes(self):
        return [e for e in self.envios if e.estado == "pendiente"]


emp = EmpresaTransporte()
emp.registrar_conductor(Conductor("111A", "Ana"))
emp.registrar_vehiculo(Vehiculo("1234ABC", "Furgoneta"))
env = Envio("E1", "Madrid", 10)
emp.registrar_envio(env)
emp.asignar("E1", "111A", "1234ABC")
emp.cambiar_estado("E1", "en tránsito")
print(len(emp.pendientes()))

# ============================================================
# EJERCICIO 4 — CURSOS PRESENCIALES COMPLETOS
# ============================================================

class Alumno:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.notas = []
        self.asistencia = 0


class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.alumnos = []

    def matricular(self, a):
        self.alumnos.append(a)

    def registrar_asistencia(self, dni):
        a = next((x for x in self.alumnos if x.dni == dni), None)
        if a:
            a.asistencia += 1

    def poner_nota(self, dni, nota):
        a = next((x for x in self.alumnos if x.dni == dni), None)
        if a:
            a.notas.append(nota)

    def media(self):
        todas = [n for a in self.alumnos for n in a.notas]
        return sum(todas)/len(todas) if todas else 0


p = Profesor("Carlos")
c = Curso("Python", p)
a1 = Alumno("111A", "Ana")
a2 = Alumno("222B", "Luis")
c.matricular(a1)
c.matricular(a2)
c.registrar_asistencia("111A")
c.poner_nota("111A", 8)
c.poner_nota("222B", 6)
print(c.media())

# ============================================================
# EJERCICIO 5 — INVENTARIO MULTIALMACÉN COMPLETO
# ============================================================

class Producto:
    def __init__(self, codigo, nombre, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock


class Almacen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def añadir(self, p):
        self.productos.append(p)

    def buscar(self, codigo):
        return next((x for x in self.productos if x.codigo == codigo), None)

    def mover(self, codigo, cantidad, destino):
        p = self.buscar(codigo)
        if not p or p.stock < cantidad:
            return False
        p.stock -= cantidad
        destino.recibir(codigo, cantidad)
        return True

    def recibir(self, codigo, cantidad):
        p = self.buscar(codigo)
        if p:
            p.stock += cantidad
        else:
            self.productos.append(Producto(codigo, "Desconocido", cantidad))


a1 = Almacen("Central")
a2 = Almacen("Secundario")

a1.añadir(Producto("P1", "USB", 10))
a1.mover("P1", 5, a2)
print([(p.codigo, p.stock) for p in a1.productos])
print([(p.codigo, p.stock) for p in a2.productos])

# ============================================================
# EJERCICIO 1 — BIBLIOTECA COMPLETA CON RESERVAS Y MULTAS
# ============================================================

class Usuario:
    def __init__(self, dni, nombre, tipo):
        self.dni = dni
        self.nombre = nombre
        self.tipo = tipo
        self.historial = []


class Libro:
    def __init__(self, codigo, titulo, categoria):
        self.codigo = codigo
        self.titulo = titulo
        self.categoria = categoria
        self.prestado = False
        self.reservado_por = None
        self.dias = 0


class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.libros = []
        self.prestamos = {}

    def registrar_usuario(self, u):
        self.usuarios.append(u)

    def añadir_libro(self, l):
        self.libros.append(l)

    def buscar(self, texto):
        return [l for l in self.libros if texto.lower() in l.titulo.lower()]

    def reservar(self, dni, codigo):
        u = next((x for x in self.usuarios if x.dni == dni), None)
        l = next((x for x in self.libros if x.codigo == codigo), None)
        if not u or not l or l.reservado_por:
            return False
        l.reservado_por = u
        return True

    def prestar(self, dni, codigo):
        u = next((x for x in self.usuarios if x.dni == dni), None)
        l = next((x for x in self.libros if x.codigo == codigo), None)
        if not u or not l or l.prestado:
            return False
        if l.reservado_por and l.reservado_por != u:
            return False
        l.prestado = True
        l.reservado_por = None
        self.prestamos[dni] = l
        u.historial.append(f"Prestado:{l.titulo}")
        return True

    def pasar_dia(self):
        for l in self.libros:
            if l.prestado:
                l.dias += 1

    def devolver(self, dni):
        l = self.prestamos.get(dni)
        if not l:
            return 0
        multa = max(0, l.dias - 7) * 0.5
        l.prestado = False
        l.dias = 0
        del self.prestamos[dni]
        return multa

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for l in self.libros:
                f.write(f"{l.codigo};{l.titulo};{l.categoria};{l.prestado};{l.dias}\n")


b = Biblioteca()
b.registrar_usuario(Usuario("111A", "Ana", "alumno"))
b.añadir_libro(Libro("L1", "Python Básico", "Programación"))
b.reservar("111A", "L1")
b.prestar("111A", "L1")
for _ in range(10):
    b.pasar_dia()
print(b.devolver("111A"))

# ============================================================
# EJERCICIO 2 — EMPRESA COMPLETA CON PROYECTOS Y NÓMINAS
# ============================================================

class Empleado:
    def __init__(self, dni, nombre, sueldo):
        self.dni = dni
        self.nombre = nombre
        self.sueldo = sueldo


class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def añadir(self, e):
        self.empleados.append(e)

    def coste(self):
        return sum(e.sueldo for e in self.empleados)


class Tarea:
    def __init__(self, nombre, horas):
        self.nombre = nombre
        self.horas = horas
        self.empleado = None
        self.estado = "pendiente"


class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def añadir_tarea(self, t):
        self.tareas.append(t)

    def asignar(self, tarea, empleado):
        tarea.empleado = empleado

    def completar(self, tarea):
        tarea.estado = "completada"

    def horas_totales(self):
        return sum(t.horas for t in self.tareas)


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.depts = []
        self.proyectos = []

    def añadir_dept(self, d):
        self.depts.append(d)

    def añadir_proyecto(self, p):
        self.proyectos.append(p)

    def nomina_total(self):
        return sum(d.coste() for d in self.depts)


e = Empresa("TechCorp")
d1 = Departamento("IT")
d1.añadir(Empleado("111A", "Ana", 1500))
d1.añadir(Empleado("222B", "Luis", 1800))
e.añadir_dept(d1)

p = Proyecto("App Móvil")
t1 = Tarea("Diseño", 10)
t2 = Tarea("Backend", 30)
p.añadir_tarea(t1)
p.añadir_tarea(t2)
p.asignar(t1, d1.empleados[0])
p.completar(t1)
e.añadir_proyecto(p)

print(e.nomina_total(), p.horas_totales())

# ============================================================
# EJERCICIO 3 — HOTEL COMPLETO CON FACTURACIÓN
# ============================================================

class Cliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Habitacion:
    def __init__(self, numero, capacidad, precio):
        self.numero = numero
        self.capacidad = capacidad
        self.precio = precio
        self.ocupada = False


class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias


class Hotel:
    def __init__(self):
        self.habitaciones = []
        self.reservas = []

    def añadir_habitacion(self, h):
        self.habitaciones.append(h)

    def reservar(self, cliente, personas, dias):
        for h in self.habitaciones:
            if not h.ocupada and h.capacidad >= personas:
                h.ocupada = True
                r = Reserva(cliente, h, dias)
                self.reservas.append(r)
                return True
        return False

    def checkout(self, cliente):
        for r in self.reservas:
            if r.cliente.dni == cliente.dni:
                r.habitacion.ocupada = False
                total = r.habitacion.precio * r.dias
                self.reservas.remove(r)
                return total
        return 0


h = Hotel()
h.añadir_habitacion(Habitacion(101, 2, 50))
h.añadir_habitacion(Habitacion(102, 4, 80))

c = Cliente("111A", "Ana")
h.reservar(c, 2, 3)
print(h.checkout(c))

# ============================================================
# EJERCICIO 4 — CURSOS COMPLETOS CON PROGRESO
# ============================================================

class Leccion:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion


class Modulo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lecciones = []

    def añadir(self, l):
        self.lecciones.append(l)

    def duracion(self):
        return sum(l.duracion for l in self.lecciones)


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.modulos = []
        self.progreso = {}

    def añadir_modulo(self, m):
        self.modulos.append(m)

    def matricular(self, alumno):
        self.progreso[alumno] = 0

    def avanzar(self, alumno, minutos):
        self.progreso[alumno] += minutos

    def duracion_total(self):
        return sum(m.duracion() for m in self.modulos)


c = Curso("Python", "Carlos")
m = Modulo("POO")
m.añadir(Leccion("Clases", 10))
m.añadir(Leccion("Herencia", 15))
c.añadir_modulo(m)
c.matricular("Ana")
c.avanzar("Ana", 20)
print(c.progreso["Ana"])

# ============================================================
# EJERCICIO 5 — EMPRESA DE ENVÍOS COMPLETA
# ============================================================

class Cliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Paquete:
    def __init__(self, codigo, peso):
        self.codigo = codigo
        self.peso = peso


class Envio:
    def __init__(self, cliente, paquete, destino):
        self.cliente = cliente
        self.paquete = paquete
        self.destino = destino
        self.estado = "pendiente"


class EmpresaEnvios:
    def __init__(self):
        self.envios = []

    def registrar_envio(self, e):
        self.envios.append(e)

    def cambiar_estado(self, codigo, nuevo):
        for e in self.envios:
            if e.paquete.codigo == codigo:
                e.estado = nuevo

    def pendientes(self):
        return [e for e in self.envios if e.estado == "pendiente"]

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for e in self.envios:
                f.write(f"{e.cliente.dni};{e.paquete.codigo};{e.peso};{e.destino};{e.estado}\n")


cli = Cliente("111A", "Ana")
paq = Paquete("P1", 2.5)
env = Envio(cli, paq, "Madrid")

emp = EmpresaEnvios()
emp.registrar_envio(env)
emp.cambiar_estado("P1", "en tránsito")
print(len(emp.pendientes()))

# ============================================================
# EJERCICIO 1 — BIBLIOTECA DE VIDEOJUEGOS COMPLETA
# ============================================================

class Usuario:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.historial = []


class Videojuego:
    def __init__(self, codigo, titulo, plataforma):
        self.codigo = codigo
        self.titulo = titulo
        self.plataforma = plataforma
        self.prestado = False
        self.reservado_por = None
        self.dias = 0


class BibliotecaJuegos:
    def __init__(self):
        self.usuarios = []
        self.juegos = []
        self.prestamos = {}

    def registrar_usuario(self, u):
        self.usuarios.append(u)

    def añadir_juego(self, j):
        self.juegos.append(j)

    def buscar(self, texto):
        return [j for j in self.juegos if texto.lower() in j.titulo.lower()]

    def reservar(self, dni, codigo):
        u = next((x for x in self.usuarios if x.dni == dni), None)
        j = next((x for x in self.juegos if x.codigo == codigo), None)
        if not u or not j or j.reservado_por:
            return False
        j.reservado_por = u
        return True

    def prestar(self, dni, codigo):
        u = next((x for x in self.usuarios if x.dni == dni), None)
        j = next((x for x in self.juegos if x.codigo == codigo), None)
        if not u or not j or j.prestado:
            return False
        if j.reservado_por and j.reservado_por != u:
            return False
        j.prestado = True
        j.reservado_por = None
        self.prestamos[dni] = j
        u.historial.append(f"Prestado:{j.titulo}")
        return True

    def pasar_dia(self):
        for j in self.juegos:
            if j.prestado:
                j.dias += 1

    def devolver(self, dni):
        j = self.prestamos.get(dni)
        if not j:
            return 0
        multa = max(0, j.dias - 5) * 1
        j.prestado = False
        j.dias = 0
        del self.prestamos[dni]
        return multa


b = BibliotecaJuegos()
b.registrar_usuario(Usuario("111A", "Ana"))
b.añadir_juego(Videojuego("G1", "Zelda", "Switch"))
b.reservar("111A", "G1")
b.prestar("111A", "G1")
for _ in range(7):
    b.pasar_dia()
print(b.devolver("111A"))

# ============================================================
# EJERCICIO 2 — AEROLÍNEA COMPLETA
# ============================================================

class Pasajero:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Avion:
    def __init__(self, codigo, capacidad):
        self.codigo = codigo
        self.capacidad = capacidad


class Vuelo:
    def __init__(self, codigo, avion, origen, destino):
        self.codigo = codigo
        self.avion = avion
        self.origen = origen
        self.destino = destino
        self.reservas = []


class Aerolinea:
    def __init__(self):
        self.pasajeros = []
        self.vuelos = []

    def registrar_pasajero(self, p):
        self.pasajeros.append(p)

    def añadir_vuelo(self, v):
        self.vuelos.append(v)

    def reservar(self, dni, codigo_vuelo):
        p = next((x for x in self.pasajeros if x.dni == dni), None)
        v = next((x for x in self.vuelos if x.codigo == codigo_vuelo), None)
        if not p or not v:
            return False
        if len(v.reservas) >= v.avion.capacidad:
            return False
        v.reservas.append(p)
        return True

    def cancelar(self, dni, codigo_vuelo):
        v = next((x for x in self.vuelos if x.codigo == codigo_vuelo), None)
        if not v:
            return False
        v.reservas = [p for p in v.reservas if p.dni != dni]
        return True

    def ocupacion(self, codigo_vuelo):
        v = next((x for x in self.vuelos if x.codigo == codigo_vuelo), None)
        if not v:
            return 0
        return len(v.reservas) / v.avion.capacidad * 100


a = Aerolinea()
a.registrar_pasajero(Pasajero("111A", "Ana"))
v = Vuelo("V1", Avion("A1", 2), "Madrid", "Roma")
a.añadir_vuelo(v)
a.reservar("111A", "V1")
print(a.ocupacion("V1"))

# ============================================================
# EJERCICIO 3 — BIBLIOTECA DE RECETAS COMPLETA
# ============================================================

class Ingrediente:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad


class Receta:
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria
        self.ingredientes = []

    def añadir(self, ing):
        self.ingredientes.append(ing)


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.favoritos = []

    def marcar_favorito(self, receta):
        self.favoritos.append(receta)


class Recetario:
    def __init__(self):
        self.recetas = []

    def añadir_receta(self, r):
        self.recetas.append(r)

    def buscar(self, texto):
        return [r for r in self.recetas if texto.lower() in r.nombre.lower()]

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for r in self.recetas:
                ings = ",".join(i.nombre for i in r.ingredientes)
                f.write(f"{r.nombre};{r.categoria};{ings}\n")


rec = Recetario()
r = Receta("Tortilla", "Huevos")
r.añadir(Ingrediente("Huevo", 3))
r.añadir(Ingrediente("Patata", 2))
rec.añadir_receta(r)
print(rec.buscar("tor")[0].nombre)

# ============================================================
# EJERCICIO 4 — LIBROS DIGITALES COMPLETOS
# ============================================================

class LibroDigital:
    def __init__(self, codigo, titulo, tamaño):
        self.codigo = codigo
        self.titulo = titulo
        self.tamaño = tamaño
        self.descargas = 0


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []


class BibliotecaDigital:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def registrar_usuario(self, u):
        self.usuarios.append(u)

    def añadir_libro(self, l):
        self.libros.append(l)

    def descargar(self, usuario, codigo):
        u = next((x for x in self.usuarios if x.nombre == usuario), None)
        l = next((x for x in self.libros if x.codigo == codigo), None)
        if not u or not l:
            return False
        l.descargas += 1
        u.historial.append(l.titulo)
        return True

    def top_descargas(self):
        return max(self.libros, key=lambda x: x.descargas)


bd = BibliotecaDigital()
bd.registrar_usuario(Usuario("Ana"))
bd.añadir_libro(LibroDigital("L1", "Python", 5))
bd.descargar("Ana", "L1")
print(bd.top_descargas().titulo)

# ============================================================
# EJERCICIO 5 — EMPRESA DE REPARACIONES COMPLETA
# ============================================================

class Cliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Tecnico:
    def __init__(self, nombre):
        self.nombre = nombre


class Pieza:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Reparacion:
    def __init__(self, cliente, tecnico, descripcion):
        self.cliente = cliente
        self.tecnico = tecnico
        self.descripcion = descripcion
        self.piezas = []

    def añadir_pieza(self, p):
        self.piezas.append(p)

    def total(self):
        return sum(p.precio for p in self.piezas)


class EmpresaReparaciones:
    def __init__(self):
        self.reparaciones = []

    def registrar(self, r):
        self.reparaciones.append(r)

    def total_cliente(self, dni):
        return sum(r.total() for r in self.reparaciones if r.cliente.dni == dni)


c = Cliente("111A", "Ana")
t = Tecnico("Luis")
r = Reparacion(c, t, "Pantalla rota")
r.añadir_pieza(Pieza("Pantalla", 80))
r.añadir_pieza(Pieza("Tornillos", 5))

emp = EmpresaReparaciones()
emp.registrar(r)
print(emp.total_cliente("111A"))

# ============================================================
# EJERCICIO 1 — BIBLIOTECA DE ARTE COMPLETA
# ============================================================

class Artista:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais


class Obra:
    def __init__(self, codigo, titulo, artista, año):
        self.codigo = codigo
        self.titulo = titulo
        self.artista = artista
        self.año = año


class Exposicion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.obras = []
        self.visitantes = []

    def añadir_obra(self, obra):
        self.obras.append(obra)

    def registrar_visita(self, visitante):
        self.visitantes.append(visitante)

    def total_visitas(self):
        return len(self.visitantes)


class Visitante:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Museo:
    def __init__(self):
        self.artistas = []
        self.obras = []
        self.exposiciones = []

    def registrar_artista(self, a):
        self.artistas.append(a)

    def registrar_obra(self, o):
        self.obras.append(o)

    def crear_exposicion(self, e):
        self.exposiciones.append(e)

    def buscar_obra(self, texto):
        return [o for o in self.obras if texto.lower() in o.titulo.lower()]

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for o in self.obras:
                f.write(f"{o.codigo};{o.titulo};{o.artista.nombre};{o.año}\n")


m = Museo()
a = Artista("Picasso", "España")
m.registrar_artista(a)
o = Obra("O1", "Guernica", a, 1937)
m.registrar_obra(o)
e = Exposicion("Arte Moderno")
e.añadir_obra(o)
e.registrar_visita(Visitante("111A", "Ana"))
m.crear_exposicion(e)
print(e.total_visitas())

# ============================================================
# EJERCICIO 2 — DOCUMENTOS EMPRESARIALES COMPLETOS
# ============================================================

class Empleado:
    def __init__(self, dni, nombre, rol):
        self.dni = dni
        self.nombre = nombre
        self.rol = rol


class Documento:
    def __init__(self, codigo, titulo, categoria):
        self.codigo = codigo
        self.titulo = titulo
        self.categoria = categoria
        self.historial = []


class SistemaDocumentos:
    def __init__(self):
        self.documentos = []
        self.empleados = []
        self.permisos = {
            "admin": {"leer", "escribir", "borrar"},
            "user": {"leer"}
        }

    def registrar_empleado(self, e):
        self.empleados.append(e)

    def añadir_documento(self, d):
        self.documentos.append(d)

    def puede(self, empleado, accion):
        return accion in self.permisos.get(empleado.rol, set())

    def leer(self, dni, codigo):
        e = next((x for x in self.empleados if x.dni == dni), None)
        d = next((x for x in self.documentos if x.codigo == codigo), None)
        if not e or not d or not self.puede(e, "leer"):
            return False
        d.historial.append(f"{e.nombre} leyó {d.titulo}")
        return True

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for d in self.documentos:
                f.write(f"{d.codigo};{d.titulo};{d.categoria}\n")


s = SistemaDocumentos()
e = Empleado("111A", "Ana", "admin")
s.registrar_empleado(e)
d = Documento("D1", "Informe", "Finanzas")
s.añadir_documento(d)
s.leer("111A", "D1")
print(d.historial)

# ============================================================
# EJERCICIO 3 — CENTRO COMERCIAL COMPLETO
# ============================================================

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.ventas = []

    def añadir_producto(self, p):
        self.productos.append(p)

    def vender(self, codigo, cliente):
        p = next((x for x in self.productos if x.codigo == codigo), None)
        if not p:
            return False
        self.ventas.append((cliente, p))
        return True

    def total_ventas(self):
        return sum(p.precio for _, p in self.ventas)


class Cliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class CentroComercial:
    def __init__(self):
        self.tiendas = []

    def añadir_tienda(self, t):
        self.tiendas.append(t)

    def buscar_producto(self, texto):
        res = []
        for t in self.tiendas:
            for p in t.productos:
                if texto.lower() in p.nombre.lower():
                    res.append((t.nombre, p))
        return res


cc = CentroComercial()
t = Tienda("Electrónica")
t.añadir_producto(Producto("P1", "USB", 5))
cc.añadir_tienda(t)
c = Cliente("111A", "Ana")
t.vender("P1", c)
print(t.total_ventas())

# ============================================================
# EJERCICIO 4 — CURSOS ONLINE COMPLETOS CON EXÁMENES
# ============================================================

class Leccion:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion


class Modulo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lecciones = []
        self.examen = None

    def añadir_leccion(self, l):
        self.lecciones.append(l)

    def asignar_examen(self, examen):
        self.examen = examen

    def duracion(self):
        return sum(l.duracion for l in self.lecciones)


class Examen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}

    def poner_nota(self, alumno, nota):
        self.notas[alumno] = nota


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.modulos = []
        self.progreso = {}

    def añadir_modulo(self, m):
        self.modulos.append(m)

    def matricular(self, alumno):
        self.progreso[alumno] = 0

    def avanzar(self, alumno, minutos):
        self.progreso[alumno] += minutos

    def media_examenes(self, alumno):
        notas = []
        for m in self.modulos:
            if m.examen and alumno in m.examen.notas:
                notas.append(m.examen.notas[alumno])
        return sum(notas)/len(notas) if notas else 0


c = Curso("Python")
m = Modulo("POO")
m.añadir_leccion(Leccion("Clases", 10))
m.asignar_examen(Examen("Examen POO"))
c.añadir_modulo(m)
c.matricular("Ana")
m.examen.poner_nota("Ana", 9)
print(c.media_examenes("Ana"))

# ============================================================
# EJERCICIO 5 — LOGÍSTICA COMPLETA CON RUTAS
# ============================================================

class Conductor:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Vehiculo:
    def __init__(self, matricula, modelo, capacidad):
        self.matricula = matricula
        self.modelo = modelo
        self.capacidad = capacidad


class Ruta:
    def __init__(self, origen, destino, distancia):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia


class Envio:
    def __init__(self, codigo, peso, ruta):
        self.codigo = codigo
        self.peso = peso
        self.ruta = ruta
        self.estado = "pendiente"
        self.conductor = None
        self.vehiculo = None


class Logistica:
    def __init__(self):
        self.conductores = []
        self.vehiculos = []
        self.envios = []

    def registrar_conductor(self, c):
        self.conductores.append(c)

    def registrar_vehiculo(self, v):
        self.vehiculos.append(v)

    def registrar_envio(self, e):
        self.envios.append(e)

    def asignar(self, codigo, dni, matricula):
        e = next((x for x in self.envios if x.codigo == codigo), None)
        c = next((x for x in self.conductores if x.dni == dni), None)
        v = next((x for x in self.vehiculos if x.matricula == matricula), None)
        if e and c and v and e.peso <= v.capacidad:
            e.conductor = c
            e.vehiculo = v
            return True
        return False

    def cambiar_estado(self, codigo, estado):
        e = next((x for x in self.envios if x.codigo == codigo), None)
        if e:
            e.estado = estado

    def pendientes(self):
        return [e for e in self.envios if e.estado == "pendiente"]


log = Logistica()
log.registrar_conductor(Conductor("111A", "Ana"))
log.registrar_vehiculo(Vehiculo("1234ABC", "Furgo", 100))
r = Ruta("Madrid", "Sevilla", 500)
env = Envio("E1", 50, r)
log.registrar_envio(env)
log.asignar("E1", "111A", "1234ABC")
print(len(log.pendientes()))

# ============================================================
# EJERCICIO 1 — CURSOS COMPLETOS CON CERTIFICADOS
# ============================================================

class Leccion:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion


class Modulo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lecciones = []
        self.examen = None

    def añadir_leccion(self, l):
        self.lecciones.append(l)

    def asignar_examen(self, examen):
        self.examen = examen

    def duracion(self):
        return sum(l.duracion for l in self.lecciones)


class Examen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}

    def poner_nota(self, alumno, nota):
        self.notas[alumno] = nota


class Certificado:
    def __init__(self, alumno, curso):
        self.alumno = alumno
        self.curso = curso


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.modulos = []
        self.progreso = {}
        self.certificados = []

    def añadir_modulo(self, m):
        self.modulos.append(m)

    def matricular(self, alumno):
        self.progreso[alumno] = 0

    def avanzar(self, alumno, minutos):
        self.progreso[alumno] += minutos

    def duracion_total(self):
        return sum(m.duracion() for m in self.modulos)

    def media_examenes(self, alumno):
        notas = []
        for m in self.modulos:
            if m.examen and alumno in m.examen.notas:
                notas.append(m.examen.notas[alumno])
        return sum(notas)/len(notas) if notas else 0

    def generar_certificado(self, alumno):
        if self.media_examenes(alumno) >= 5:
            self.certificados.append(Certificado(alumno, self.nombre))
            return True
        return False


c = Curso("Python", "Carlos")
m = Modulo("POO")
m.añadir_leccion(Leccion("Clases", 10))
m.asignar_examen(Examen("Examen POO"))
c.añadir_modulo(m)
c.matricular("Ana")
m.examen.poner_nota("Ana", 8)
print(c.generar_certificado("Ana"))

# ============================================================
# EJERCICIO 2 — ALQUILER DE VEHÍCULOS COMPLETO
# ============================================================

class Cliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.historial = []


class Vehiculo:
    def __init__(self, matricula, modelo, precio_dia):
        self.matricula = matricula
        self.modelo = modelo
        self.precio_dia = precio_dia
        self.alquilado = False
        self.dias = 0


class Alquiler:
    def __init__(self, cliente, vehiculo, dias):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.dias = dias


class EmpresaAlquiler:
    def __init__(self):
        self.clientes = []
        self.vehiculos = []
        self.alquileres = []

    def registrar_cliente(self, c):
        self.clientes.append(c)

    def añadir_vehiculo(self, v):
        self.vehiculos.append(v)

    def alquilar(self, dni, matricula, dias):
        c = next((x for x in self.clientes if x.dni == dni), None)
        v = next((x for x in self.vehiculos if x.matricula == matricula), None)
        if not c or not v or v.alquilado:
            return False
        v.alquilado = True
        v.dias = dias
        self.alquileres.append(Alquiler(c, v, dias))
        c.historial.append(f"Alquilado:{v.modelo}")
        return True

    def devolver(self, dni):
        a = next((x for x in self.alquileres if x.cliente.dni == dni), None)
        if not a:
            return 0
        multa = max(0, a.vehiculo.dias - 7) * 10
        total = a.vehiculo.precio_dia * a.vehiculo.dias + multa
        a.vehiculo.alquilado = False
        self.alquileres.remove(a)
        return total


emp = EmpresaAlquiler()
emp.registrar_cliente(Cliente("111A", "Ana"))
emp.añadir_vehiculo(Vehiculo("1234ABC", "Seat Ibiza", 30))
emp.alquilar("111A", "1234ABC", 10)
print(emp.devolver("111A"))

# ============================================================
# EJERCICIO 3 — GESTIÓN DE PRODUCTOS Y PROVEEDORES COMPLETA
# ============================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre


class Pedido:
    def __init__(self, proveedor):
        self.proveedor = proveedor
        self.lineas = []

    def añadir(self, producto, cantidad):
        self.lineas.append((producto, cantidad))

    def total(self):
        return sum(p.precio * c for p, c in self.lineas)


class Factura:
    def __init__(self, pedido):
        self.pedido = pedido

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for p, c in self.pedido.lineas:
                f.write(f"{p.codigo};{p.nombre};{c};{p.precio}\n")
            f.write(f"TOTAL;{self.pedido.total()}\n")


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir(self, p):
        self.productos.append(p)

    def buscar(self, codigo):
        return next((x for x in self.productos if x.codigo == codigo), None)


inv = Inventario()
inv.añadir(Producto("P1", "USB", 5, 10))
prov = Proveedor("TechPro")
ped = Pedido(prov)
ped.añadir(inv.buscar("P1"), 5)
f = Factura(ped)
f.guardar("factura.txt")
print(ped.total())

# ============================================================
# EJERCICIO 4 — VETERINARIA COMPLETA
# ============================================================

class Dueño:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Mascota:
    def __init__(self, codigo, nombre, especie):
        self.codigo = codigo
        self.nombre = nombre
        self.especie = especie
        self.historial = []


class Veterinario:
    def __init__(self, nombre):
        self.nombre = nombre


class Cita:
    def __init__(self, mascota, vet, motivo):
        self.mascota = mascota
        self.vet = vet
        self.motivo = motivo


class Veterinaria:
    def __init__(self):
        self.mascotas = []
        self.vets = []
        self.citas = []

    def registrar_mascota(self, m):
        self.mascotas.append(m)

    def registrar_vet(self, v):
        self.vets.append(v)

    def pedir_cita(self, codigo, vet_nombre, motivo):
        m = next((x for x in self.mascotas if x.codigo == codigo), None)
        v = next((x for x in self.vets if x.nombre == vet_nombre), None)
        if not m or not v:
            return False
        c = Cita(m, v, motivo)
        self.citas.append(c)
        m.historial.append(f"Cita:{motivo}")
        return True


vet = Veterinaria()
vet.registrar_mascota(Mascota("M1", "Luna", "Perro"))
vet.registrar_vet(Veterinario("Dr. Luis"))
vet.pedir_cita("M1", "Dr. Luis", "Vacuna")
print(vet.citas[0].motivo)

# ============================================================
# EJERCICIO 5 — EVENTOS COMPLETOS CON AFORO
# ============================================================

class Usuario:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Evento:
    def __init__(self, codigo, nombre, aforo):
        self.codigo = codigo
        self.nombre = nombre
        self.aforo = aforo
        self.entradas = []

    def vender(self, usuario):
        if len(self.entradas) >= self.aforo:
            return False
        self.entradas.append(usuario)
        return True

    def ocupacion(self):
        return len(self.entradas) / self.aforo * 100


class SistemaEventos:
    def __init__(self):
        self.eventos = []

    def añadir_evento(self, e):
        self.eventos.append(e)

    def buscar(self, texto):
        return [e for e in self.eventos if texto.lower() in e.nombre.lower()]


s = SistemaEventos()
e = Evento("E1", "Concierto Rock", 2)
s.añadir_evento(e)
u = Usuario("111A", "Ana")
e.vender(u)
print(e.ocupacion())

# ============================================================
# EJERCICIO 1 — EMPRESA COMPLETA CON PROYECTOS Y TAREAS
# ============================================================

class Empleado:
    def __init__(self, dni, nombre, puesto):
        self.dni = dni
        self.nombre = nombre
        self.puesto = puesto


class Tarea:
    def __init__(self, codigo, descripcion, horas):
        self.codigo = codigo
        self.descripcion = descripcion
        self.horas = horas
        self.estado = "pendiente"
        self.empleado = None


class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def añadir_tarea(self, t):
        self.tareas.append(t)

    def asignar(self, codigo, empleado):
        t = next((x for x in self.tareas if x.codigo == codigo), None)
        if t:
            t.empleado = empleado

    def completar(self, codigo):
        t = next((x for x in self.tareas if x.codigo == codigo), None)
        if t:
            t.estado = "completada"

    def horas_totales(self):
        return sum(t.horas for t in self.tareas)


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.proyectos = []

    def registrar_empleado(self, e):
        self.empleados.append(e)

    def crear_proyecto(self, p):
        self.proyectos.append(p)

    def informe(self):
        return [(p.nombre, p.horas_totales()) for p in self.proyectos]


emp = Empresa("TechCorp")
emp.registrar_empleado(Empleado("111A", "Ana", "Programadora"))
p = Proyecto("App Móvil")
p.añadir_tarea(Tarea("T1", "Diseño", 10))
p.añadir_tarea(Tarea("T2", "Backend", 30))
p.asignar("T1", emp.empleados[0])
p.completar("T1")
emp.crear_proyecto(p)
print(emp.informe())

# ============================================================
# EJERCICIO 2 — BIBLIOTECA DE LIBROS ANTIGUOS COMPLETA
# ============================================================

class LibroAntiguo:
    def __init__(self, codigo, titulo, año):
        self.codigo = codigo
        self.titulo = titulo
        self.año = año
        self.historial = []


class Restaurador:
    def __init__(self, nombre):
        self.nombre = nombre


class Reparacion:
    def __init__(self, libro, restaurador, descripcion, coste):
        self.libro = libro
        self.restaurador = restaurador
        self.descripcion = descripcion
        self.coste = coste


class Archivo:
    def __init__(self):
        self.libros = []
        self.reparaciones = []

    def registrar_libro(self, l):
        self.libros.append(l)

    def registrar_reparacion(self, r):
        self.reparaciones.append(r)
        r.libro.historial.append(r.descripcion)

    def coste_total(self, codigo):
        return sum(r.coste for r in self.reparaciones if r.libro.codigo == codigo)


a = Archivo()
l = LibroAntiguo("L1", "Códice Antiguo", 1500)
a.registrar_libro(l)
r = Restaurador("Luis")
rep = Reparacion(l, r, "Restauración de páginas", 200)
a.registrar_reparacion(rep)
print(a.coste_total("L1"))

# ============================================================
# EJERCICIO 3 — CURSOS PRESENCIALES COMPLETOS
# ============================================================

class Alumno:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.asistencia = 0
        self.notas = []


class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.alumnos = []

    def matricular(self, a):
        self.alumnos.append(a)

    def registrar_asistencia(self, dni):
        a = next((x for x in self.alumnos if x.dni == dni), None)
        if a:
            a.asistencia += 1

    def poner_nota(self, dni, nota):
        a = next((x for x in self.alumnos if x.dni == dni), None)
        if a:
            a.notas.append(nota)

    def media(self):
        todas = [n for a in self.alumnos for n in a.notas]
        return sum(todas)/len(todas) if todas else 0


p = Profesor("Carlos")
c = Curso("Python", p)
a1 = Alumno("111A", "Ana")
a2 = Alumno("222B", "Luis")
c.matricular(a1)
c.matricular(a2)
c.registrar_asistencia("111A")
c.poner_nota("111A", 8)
c.poner_nota("222B", 6)
print(c.media())

# ============================================================
# EJERCICIO 4 — VIDEOTECA COMPLETA CON RECOMENDACIONES
# ============================================================

class Pelicula:
    def __init__(self, codigo, titulo, director):
        self.codigo = codigo
        self.titulo = titulo
        self.director = director
        self.valoraciones = []

    def valorar(self, nota):
        self.valoraciones.append(nota)

    def media(self):
        return sum(self.valoraciones)/len(self.valoraciones) if self.valoraciones else 0


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vistas = []


class Videoteca:
    def __init__(self):
        self.peliculas = []
        self.usuarios = []

    def añadir_pelicula(self, p):
        self.peliculas.append(p)

    def registrar_usuario(self, u):
        self.usuarios.append(u)

    def ver(self, usuario, codigo):
        u = next((x for x in self.usuarios if x.nombre == usuario), None)
        p = next((x for x in self.peliculas if x.codigo == codigo), None)
        if u and p:
            u.vistas.append(p)
            return True
        return False

    def recomendar(self, usuario):
        u = next((x for x in self.usuarios if x.nombre == usuario), None)
        if not u:
            return None
        vistas = {p.codigo for p in u.vistas}
        no_vistas = [p for p in self.peliculas if p.codigo not in vistas]
        if not no_vistas:
            return None
        return max(no_vistas, key=lambda x: x.media())


v = Videoteca()
p1 = Pelicula("P1", "Matrix", "Wachowski")
p1.valorar(10); p1.valorar(9)
v.añadir_pelicula(p1)
v.registrar_usuario(Usuario("Ana"))
v.ver("Ana", "P1")
print(p1.media())

# ============================================================
# EJERCICIO 5 — EMPRESA DE ENVÍOS COMPLETA
# ============================================================

class Cliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Paquete:
    def __init__(self, codigo, peso):
        self.codigo = codigo
        self.peso = peso


class Ruta:
    def __init__(self, origen, destino, distancia):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia


class Envio:
    def __init__(self, cliente, paquete, ruta):
        self.cliente = cliente
        self.paquete = paquete
        self.ruta = ruta
        self.estado = "pendiente"


class EmpresaEnvios:
    def __init__(self):
        self.envios = []

    def registrar_envio(self, e):
        self.envios.append(e)

    def cambiar_estado(self, codigo, nuevo):
        for e in self.envios:
            if e.paquete.codigo == codigo:
                e.estado = nuevo

    def pendientes(self):
        return [e for e in self.envios if e.estado == "pendiente"]

    def total_km(self):
        return sum(e.ruta.distancia for e in self.envios)


cli = Cliente("111A", "Ana")
paq = Paquete("P1", 2.5)
ruta = Ruta("Madrid", "Sevilla", 500)
env = Envio(cli, paq, ruta)

emp = EmpresaEnvios()
emp.registrar_envio(env)
emp.cambiar_estado("P1", "en tránsito")
print(emp.total_km())

# ============================================================
# EJERCICIO 1 — GESTIÓN DE EMPLEADOS Y TURNOS COMPLETA
# ============================================================

class Empleado:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.fichajes = []


class Turno:
    def __init__(self, nombre, hora_inicio, hora_fin):
        self.nombre = nombre
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin


class Fichaje:
    def __init__(self, empleado, hora_entrada, hora_salida):
        self.empleado = empleado
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida

    def horas(self):
        return self.hora_salida - self.hora_entrada


class Empresa:
    def __init__(self):
        self.empleados = []
        self.turnos = []
        self.fichajes = []

    def registrar_empleado(self, e):
        self.empleados.append(e)

    def crear_turno(self, t):
        self.turnos.append(t)

    def fichar(self, dni, entrada, salida):
        e = next((x for x in self.empleados if x.dni == dni), None)
        if not e:
            return False
        f = Fichaje(e, entrada, salida)
        e.fichajes.append(f)
        self.fichajes.append(f)
        return True

    def horas_totales(self, dni):
        e = next((x for x in self.empleados if x.dni == dni), None)
        if not e:
            return 0
        return sum(f.horas() for f in e.fichajes)


emp = Empresa()
emp.registrar_empleado(Empleado("111A", "Ana"))
emp.fichar("111A", 8, 16)
emp.fichar("111A", 9, 17)
print(emp.horas_totales("111A"))

# ============================================================
# EJERCICIO 2 — TIENDA COMPLETA CON CATEGORÍAS Y FACTURAS
# ============================================================

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre


class Producto:
    def __init__(self, codigo, nombre, precio, stock, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria


class Carrito:
    def __init__(self):
        self.lineas = []

    def añadir(self, producto, cantidad):
        if producto.stock < cantidad:
            return False
        producto.stock -= cantidad
        self.lineas.append((producto, cantidad))
        return True

    def total(self):
        return sum(p.precio * c for p, c in self.lineas)


class Pedido:
    def __init__(self, carrito):
        self.carrito = carrito


class Factura:
    def __init__(self, pedido):
        self.pedido = pedido

    def guardar(self, ruta):
        with open(ruta, "w") as f:
            for p, c in self.pedido.carrito.lineas:
                f.write(f"{p.codigo};{p.nombre};{c};{p.precio}\n")
            f.write(f"TOTAL;{self.pedido.carrito.total()}\n")


cat = Categoria("Electrónica")
p = Producto("P1", "USB", 5, 10, cat)
car = Carrito()
car.añadir(p, 3)
ped = Pedido(car)
f = Factura(ped)
print(car.total())

# ============================================================
# EJERCICIO 3 — RED DE HOTELES COMPLETA
# ============================================================

class Cliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Habitacion:
    def __init__(self, numero, capacidad, precio):
        self.numero = numero
        self.capacidad = capacidad
        self.precio = precio
        self.ocupada = False


class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def añadir_habitacion(self, h):
        self.habitaciones.append(h)

    def reservar(self, cliente, personas, dias):
        for h in self.habitaciones:
            if not h.ocupada and h.capacidad >= personas:
                h.ocupada = True
                r = Reserva(cliente, h, dias)
                self.reservas.append(r)
                return True
        return False

    def ingresos(self):
        return sum(r.habitacion.precio * r.dias for r in self.reservas)


h = Hotel("SolMar")
h.añadir_habitacion(Habitacion(101, 2, 50))
h.añadir_habitacion(Habitacion(102, 4, 80))
c = Cliente("111A", "Ana")
h.reservar(c, 2, 3)
print(h.ingresos())

# ============================================================
# EJERCICIO 4 — CURSOS COMPLETOS CON TAREAS Y ENTREGAS
# ============================================================

class Alumno:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.entregas = {}


class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre


class Tarea:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.notas = {}


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.alumnos = []
        self.tareas = []

    def matricular(self, a):
        self.alumnos.append(a)

    def añadir_tarea(self, t):
        self.tareas.append(t)

    def entregar(self, dni, codigo_tarea, archivo):
        a = next((x for x in self.alumnos if x.dni == dni), None)
        t = next((x for x in self.tareas if x.codigo == codigo_tarea), None)
        if a and t:
            a.entregas[codigo_tarea] = archivo
            return True
        return False

    def poner_nota(self, dni, codigo_tarea, nota):
        t = next((x for x in self.tareas if x.codigo == codigo_tarea), None)
        if t:
            t.notas[dni] = nota

    def media(self):
        todas = [n for t in self.tareas for n in t.notas.values()]
        return sum(todas)/len(todas) if todas else 0


p = Profesor("Carlos")
c = Curso("Python", p)
a = Alumno("111A", "Ana")
c.matricular(a)
t = Tarea("T1", "Ejercicio POO")
c.añadir_tarea(t)
c.entregar("111A", "T1", "solucion.py")
c.poner_nota("111A", "T1", 9)
print(c.media())

# ============================================================
# EJERCICIO 5 — LOGÍSTICA COMPLETA CON INFORMES
# ============================================================

class Conductor:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Vehiculo:
    def __init__(self, matricula, modelo, capacidad):
        self.matricula = matricula
        self.modelo = modelo
        self.capacidad = capacidad


class Ruta:
    def __init__(self, origen, destino, km):
        self.origen = origen
        self.destino = destino
        self.km = km


class Envio:
    def __init__(self, codigo, peso, ruta):
        self.codigo = codigo
        self.peso = peso
        self.ruta = ruta
        self.estado = "pendiente"
        self.conductor = None
        self.vehiculo = None


class Logistica:
    def __init__(self):
        self.envios = []
        self.conductores = []
        self.vehiculos = []

    def registrar_conductor(self, c):
        self.conductores.append(c)

    def registrar_vehiculo(self, v):
        self.vehiculos.append(v)

    def registrar_envio(self, e):
        self.envios.append(e)

    def asignar(self, codigo, dni, matricula):
        e = next((x for x in self.envios if x.codigo == codigo), None)
        c = next((x for x in self.conductores if x.dni == dni), None)
        v = next((x for x in self.vehiculos if x.matricula == matricula), None)
        if e and c and v and e.peso <= v.capacidad:
            e.conductor = c
            e.vehiculo = v
            return True
        return False

    def informe_km(self):
        return sum(e.ruta.km for e in self.envios)


log = Logistica()
log.registrar_conductor(Conductor("111A", "Ana"))
log.registrar_vehiculo(Vehiculo("1234ABC", "Furgo", 100))
r = Ruta("Madrid", "Valencia", 350)
env = Envio("E1", 50, r)
log.registrar_envio(env)
log.asignar("E1", "111A", "1234ABC")
print(log.informe_km())

# ============================================================
# EJERCICIO 1 — CURSOS COMPLETOS CON EVALUACIONES Y CERTIFICADOS
# ============================================================

class Leccion:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion


class Modulo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lecciones = []
        self.examen = None

    def añadir_leccion(self, l):
        self.lecciones.append(l)

    def asignar_examen(self, examen):
        self.examen = examen

    def duracion(self):
        return sum(l.duracion for l in self.lecciones)


class Examen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}

    def poner_nota(self, alumno, nota):
        self.notas[alumno] = nota


class Certificado:
    def __init__(self, alumno, curso):
        self.alumno = alumno
        self.curso = curso


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.modulos = []
        self.progreso = {}
        self.certificados = []

    def añadir_modulo(self, m):
        self.modulos.append(m)

    def matricular(self, alumno):
        self.progreso[alumno] = 0

    def avanzar(self, alumno, minutos):
        self.progreso[alumno] += minutos

    def duracion_total(self):
        return sum(m.duracion() for m in self.modulos)

    def media_examenes(self, alumno):
        notas = []
        for m in self.modulos:
            if m.examen and alumno in m.examen.notas:
                notas.append(m.examen.notas[alumno])
        return sum(notas)/len(notas) if notas else 0

    def generar_certificado(self, alumno):
        if self.media_examenes(alumno) >= 5:
            self.certificados.append(Certificado(alumno, self.nombre))
            return True
        return False


c = Curso("Python", "Carlos")
m = Modulo("POO")
m.añadir_leccion(Leccion("Clases", 10))
m.asignar_examen(Examen("Examen POO"))
c.añadir_modulo(m)
c.matricular("Ana")
m.examen.poner_nota("Ana", 8)
print(c.generar_certificado("Ana"))

# ============================================================
# EJERCICIO 2 — RESTAURANTE COMPLETO CON COCINA Y FACTURAS
# ============================================================

class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Pedido:
    def __init__(self, mesa):
        self.mesa = mesa
        self.platos = []

    def añadir(self, plato):
        self.platos.append(plato)

    def total(self):
        return sum(p.precio for p in self.platos)


class Restaurante:
    def __init__(self):
        self.mesas = []
        self.platos = []
        self.pedidos = []

    def añadir_mesa(self, m):
        self.mesas.append(m)

    def añadir_plato(self, p):
        self.platos.append(p)

    def reservar(self, personas):
        for m in self.mesas:
            if not m.ocupada and m.capacidad >= personas:
                m.ocupada = True
                return m
        return None

    def pedir(self, mesa, plato_nombre):
        p = next((x for x in self.platos if x.nombre == plato_nombre), None)
        if not p:
            return False
        ped = next((x for x in self.pedidos if x.mesa == mesa), None)
        if not ped:
            ped = Pedido(mesa)
            self.pedidos.append(ped)
        ped.añadir(p)
        return True

    def factura(self, mesa):
        ped = next((x for x in self.pedidos if x.mesa == mesa), None)
        if not ped:
            return 0
        mesa.ocupada = False
        return ped.total()


r = Restaurante()
r.añadir_mesa(Mesa(1, 4))
r.añadir_plato(Plato("Pasta", 10))
r.añadir_plato(Plato("Pizza", 12))

m = r.reservar(2)
r.pedir(m, "Pasta")
r.pedir(m, "Pizza")
print(r.factura(m))

# ============================================================
# EJERCICIO 3 — LOGÍSTICA COMPLETA CON RUTAS Y ESTADOS
# ============================================================

class Conductor:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Vehiculo:
    def __init__(self, matricula, modelo, capacidad):
        self.matricula = matricula
        self.modelo = modelo
        self.capacidad = capacidad


class Ruta:
    def __init__(self, origen, destino, km):
        self.origen = origen
        self.destino = destino
        self.km = km


class Envio:
    def __init__(self, codigo, peso, ruta):
        self.codigo = codigo
        self.peso = peso
        self.ruta = ruta
        self.estado = "pendiente"
        self.conductor = None
        self.vehiculo = None


class Logistica:
    def __init__(self):
        self.envios = []
        self.conductores = []
        self.vehiculos = []

    def registrar_conductor(self, c):
        self.conductores.append(c)

    def registrar_vehiculo(self, v):
        self.vehiculos.append(v)

    def registrar_envio(self, e):
        self.envios.append(e)

    def asignar(self, codigo, dni, matricula):
        e = next((x for x in self.envios if x.codigo == codigo), None)
        c = next((x for x in self.conductores if x.dni == dni), None)
        v = next((x for x in self.vehiculos if x.matricula == matricula), None)
        if e and c and v and e.peso <= v.capacidad:
            e.conductor = c
            e.vehiculo = v
            return True
        return False

    def cambiar_estado(self, codigo, estado):
        e = next((x for x in self.envios if x.codigo == codigo), None)
        if e:
            e.estado = estado

    def informe_km(self):
        return sum(e.ruta.km for e in self.envios)


log = Logistica()
log.registrar_conductor(Conductor("111A", "Ana"))
log.registrar_vehiculo(Vehiculo("1234ABC", "Furgo", 100))
r = Ruta("Madrid", "Valencia", 350)
env = Envio("E1", 50, r)
log.registrar_envio(env)
log.asignar("E1", "111A", "1234ABC")
print(log.informe_km())

# ============================================================
# EJERCICIO 4 — VETERINARIA COMPLETA CON TRATAMIENTOS
# ============================================================

class Dueño:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Mascota:
    def __init__(self, codigo, nombre, especie):
        self.codigo = codigo
        self.nombre = nombre
        self.especie = especie
        self.historial = []


class Veterinario:
    def __init__(self, nombre):
        self.nombre = nombre


class Cita:
    def __init__(self, mascota, vet, motivo):
        self.mascota = mascota
        self.vet = vet
        self.motivo = motivo


class Veterinaria:
    def __init__(self):
        self.mascotas = []
        self.vets = []
        self.citas = []

    def registrar_mascota(self, m):
        self.mascotas.append(m)

    def registrar_vet(self, v):
        self.vets.append(v)

    def pedir_cita(self, codigo, vet_nombre, motivo):
        m = next((x for x in self.mascotas if x.codigo == codigo), None)
        v = next((x for x in self.vets if x.nombre == vet_nombre), None)
        if not m or not v:
            return False
        c = Cita(m, v, motivo)
        self.citas.append(c)
        m.historial.append(f"Cita:{motivo}")
        return True


vet = Veterinaria()
vet.registrar_mascota(Mascota("M1", "Luna", "Perro"))
vet.registrar_vet(Veterinario("Dr. Luis"))
vet.pedir_cita("M1", "Dr. Luis", "Vacuna")
print(vet.citas[0].motivo)

# ============================================================
# EJERCICIO 5 — EVENTOS COMPLETOS CON AFORO Y ESTADÍSTICAS
# ============================================================

class Usuario:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre


class Evento:
    def __init__(self, codigo, nombre, aforo):
        self.codigo = codigo
        self.nombre = nombre
        self.aforo = aforo
        self.entradas = []

    def vender(self, usuario):
        if len(self.entradas) >= self.aforo:
            return False
        self.entradas.append(usuario)
        return True

    def ocupacion(self):
        return len(self.entradas) / self.aforo * 100


class SistemaEventos:
    def __init__(self):
        self.eventos = []

    def añadir_evento(self, e):
        self.eventos.append(e)

    def buscar(self, texto):
        return [e for e in self.eventos if texto.lower() in e.nombre.lower()]


s = SistemaEventos()
e = Evento("E1", "Concierto Rock", 2)
s.añadir_evento(e)
u = Usuario("111A", "Ana")
e.vender(u)
print(e.ocupacion())

# ============================================================
# EJERCICIO 1 — ALQUILER DE PELÍCULAS COMPLETO
# ============================================================

class Cliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.historial = []


class Pelicula:
    def __init__(self, codigo, titulo, categoria):
        self.codigo = codigo
        self.titulo = titulo
        self.categoria = categoria
        self.alquilada = False
        self.dias = 0


class Videoclub:
    def __init__(self):
        self.clientes = []
        self.peliculas = []
        self.alquileres = {}

    def registrar_cliente(self, c):
        self.clientes.append(c)

    def añadir_pelicula(self, p):
        self.peliculas.append(p)

    def alquilar(self, dni, codigo):
        c = next((x for x in self.clientes if x.dni == dni), None)
        p = next((x for x in self.peliculas if x.codigo == codigo), None)
        if not c or not p or p.alquilada:
            return False
        p.alquilada = True
        self.alquileres[dni] = p
        c.historial.append(f"Alquilada:{p.titulo}")
        return True

    def pasar_dia(self):
        for p in self.peliculas:
            if p.alquilada:
                p.dias += 1

    def devolver(self, dni):
        p = self.alquileres.get(dni)
        if not p:
            return 0
        multa = max(0, p.dias - 3) * 2
        p.alquilada = False
        p.dias = 0
        del self.alquileres[dni]
        return multa


v = Videoclub()
v.registrar_cliente(Cliente("111A", "Ana"))
v.añadir_pelicula(Pelicula("P1", "Matrix", "Sci-Fi"))
v.alquilar("111A", "P1")
for _ in range(5):
    v.pasar_dia()
print(v.devolver("111A"))

# ============================================================
# EJERCICIO 2 — CURSOS COMPLETOS CON FOROS Y MENSAJES
# ============================================================

class Mensaje:
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto


class Foro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.mensajes = []

    def publicar(self, mensaje):
        self.mensajes.append(mensaje)

    def borrar(self, indice):
        if 0 <= indice < len(self.mensajes):
            self.mensajes.pop(indice)


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.alumnos = []
        self.foro = Foro(f"Foro de {nombre}")

    def matricular(self, alumno):
        self.alumnos.append(alumno)

    def publicar(self, autor, texto):
        self.foro.publicar(Mensaje(autor, texto))


c = Curso("Python", "Carlos")
c.matricular("Ana")
c.publicar("Ana", "Tengo una duda sobre clases.")
c.publicar("Carlos", "Sube tu código.")
print(len(c.foro.mensajes))

# ============================================================
# EJERCICIO 3 — TIENDA COMPLETA CON PROVEEDORES Y STOCK
# ============================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock_min, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock_min = stock_min
        self.stock = stock


class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre


class Pedido:
    def __init__(self, proveedor):
        self.proveedor = proveedor
        self.lineas = []

    def añadir(self, producto, cantidad):
        self.lineas.append((producto, cantidad))


class Tienda:
    def __init__(self):
        self.productos = []
        self.proveedores = []

    def añadir_producto(self, p):
        self.productos.append(p)

    def añadir_proveedor(self, pr):
        self.proveedores.append(pr)

    def vender(self, codigo, cantidad):
        p = next((x for x in self.productos if x.codigo == codigo), None)
        if not p or p.stock < cantidad:
            return False
        p.stock -= cantidad
        return True

    def reponer(self):
        pedidos = []
        for p in self.productos:
            if p.stock < p.stock_min:
                prov = self.proveedores[0]
                ped = Pedido(prov)
                ped.añadir(p, p.stock_min * 2)
                pedidos.append(ped)
        return pedidos


t = Tienda()
t.añadir_producto(Producto("P1", "USB", 5, 5, 2))
t.añadir_proveedor(Proveedor("TechPro"))
t.vender("P1", 1)
peds = t.reponer()
print(len(peds))

# ============================================================
# EJERCICIO 4 — HOSPITAL COMPLETO CON DIAGNÓSTICOS
# ============================================================

class Paciente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.historial = []


class Medico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad


class Cita:
    def __init__(self, paciente, medico, motivo):
        self.paciente = paciente
        self.medico = medico
        self.motivo = motivo
        self.diagnostico = None


class Hospital:
    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.citas = []

    def registrar_paciente(self, p):
        self.pacientes.append(p)

    def registrar_medico(self, m):
        self.medicos.append(m)

    def pedir_cita(self, dni, medico_nombre, motivo):
        p = next((x for x in self.pacientes if x.dni == dni), None)
        m = next((x for x in self.medicos if x.nombre == medico_nombre), None)
        if not p or not m:
            return False
        c = Cita(p, m, motivo)
        self.citas.append(c)
        return True

    def diagnosticar(self, dni, diag):
        c = next((x for x in self.citas if x.paciente.dni == dni), None)
        if c:
            c.diagnostico = diag
            c.paciente.historial.append(diag)


h = Hospital()
h.registrar_paciente(Paciente("111A", "Ana"))
h.registrar_medico(Medico("Dr. Luis", "Cardiología"))
h.pedir_cita("111A", "Dr. Luis", "Dolor pecho")
h.diagnosticar("111A", "Arritmia leve")
print(h.citas[0].diagnostico)

# ============================================================
# EJERCICIO 5 — CONFERENCIAS COMPLETAS CON CHARLAS
# ============================================================

class Ponente:
    def __init__(self, nombre, tema):
        self.nombre = nombre
        self.tema = tema


class Charla:
    def __init__(self, codigo, titulo, ponente):
        self.codigo = codigo
        self.titulo = titulo
        self.ponente = ponente
        self.asistentes = []

    def asistir(self, usuario):
        self.asistentes.append(usuario)

    def total_asistentes(self):
        return len(self.asistentes)


class Conferencia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.charlas = []

    def añadir_charla(self, c):
        self.charlas.append(c)

    def total_asistentes(self):
        return sum(c.total_asistentes() for c in self.charlas)


p = Ponente("Carlos", "IA")
c = Charla("C1", "Introducción a IA", p)
c.asistir("Ana")
conf = Conferencia("TechDay")
conf.añadir_charla(c)
print(conf.total_asistentes())