#  3 Utiliza o programa anterior para xerar unha táboa de conversión de temperaturas, dende 0º F ata 120º F, de 10 en 10.

def main():

    tempF = 0
    while tempF <= 120:

        tempC = (5/9)*(tempF-32)
        print(tempF,"en Fahrenheit, son",tempC,"en Celsius")
        tempF += 10

if __name__ == "__main__":
    main()