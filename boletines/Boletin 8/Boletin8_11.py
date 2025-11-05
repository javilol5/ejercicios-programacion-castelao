#11 Pregado de un texto.
# Escribir unha función que reciba un texto e unha lonxitude e devolva unha lista de cadeas de como máximo esa lonxitude. 
# As líñas deben cortarse correctamente nos espazos (sen cortar as palabras).

def pregado_texto(texto, lonxitude):

    texto = texto.split()
    counter = 0
    resultado = []
    linea_actual = ""
    for palabra in texto:
        if (len(palabra) + counter) <= lonxitude:
            linea_actual += palabra + " "
            counter += len(palabra) + 1
        else:
            resultado.append(linea_actual.strip())
            linea_actual = palabra + " "
            counter = len(palabra) + 1
    resultado.append(linea_actual.strip())
    return resultado

# Exemplo de uso
texto = "Este é un exemplo de texto que será pregado en liñas de lonxitude específica."
lonxitude = 20
resultado = pregado_texto(texto, lonxitude)
print(resultado)