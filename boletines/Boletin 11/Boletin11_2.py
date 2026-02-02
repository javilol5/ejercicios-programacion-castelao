#2 Ler un ficheiro de texto e contar cantas veces aparece cada palabra.
#Solicita ao usuario o nome dun ficheiro .txt.
#
#Mostra a frecuencia de cada palabra (ignorando maiúsculas/minúsculas e signos de puntuación).
#
#Gárdase un resumo nun novo ficheiro resumo_palabras.txt.


import os

RUTA_BASE = os.path.dirname(os.path.abspath(__file__))


def contar_palabras():
    nome_ficheiro = (input("Introduce el nombre del fichero .txt: ")+".txt").strip()
    ruta_ficheiro = os.path.join(RUTA_BASE, nome_ficheiro)

    frecuencia_palabras = {}

    try:
        with open(ruta_ficheiro, "r", encoding="utf-8") as ficheiro:
            for linea in ficheiro:
                palabras = linea.strip().split()
                for palabra in palabras:
                    palabra_limpia = ''.join(
                        char for char in palabra if char.isalnum()).lower()
                    if palabra_limpia:
                        if palabra_limpia in frecuencia_palabras:
                            frecuencia_palabras[palabra_limpia] += 1
                        else:
                            frecuencia_palabras[palabra_limpia] = 1

        print("Frecuencia de palabras:")
        for palabra, frecuencia in frecuencia_palabras.items():
            print(f"{palabra}: {frecuencia}")

        ruta_resumo = os.path.join(RUTA_BASE, "resumen_palabras.txt")
        with open(ruta_resumo, "w", encoding="utf-8") as resumo_ficheiro:
            for palabra, frecuencia in frecuencia_palabras.items():
                resumo_ficheiro.write(f"{palabra}: {frecuencia}\n")

        print(f"\nResumen guardado en {ruta_resumo}\n")

    except FileNotFoundError:
        print("El fichero no existe.\n")

contar_palabras()