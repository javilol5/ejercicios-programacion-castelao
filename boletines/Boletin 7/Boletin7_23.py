# 23 Crear a función que permíta realizar un analisis simple de texto.
#    O analizador ten  a función de contar palabras, 
#    caracteres e encontrar a palabra mais longa. 
#    Mostrar os resultados por pantalla.

def analizar_texto(texto):
    palabras = texto.split()
    num_palabras = len(palabras)
    num_caracteres = len(texto)
    palabra_mas_larga = ""
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    
    print("Número de palabras:",num_palabras)
    print("Número de caracteres:",num_caracteres)
    print("Palabra más larga:",palabra_mas_larga)

texto1 = "Este es un ejemplo de análisis de texto para contar palabras y caracteres."
texto2 = "Otra prueba con diferentes palabras y longitudes."
texto3 = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor."
texto4 = "Python es un lenguaje de programación versátil y poderoso."

print(analizar_texto(texto1))
print(analizar_texto(texto2))
print(analizar_texto(texto3))
print(analizar_texto(texto4))