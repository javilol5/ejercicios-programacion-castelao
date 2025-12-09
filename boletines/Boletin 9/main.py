from Boletin9_1 import Libro


class Principal:
    @staticmethod
    def main():
        libro1 = Libro("titulo1", "autor1", 2000, 112233, 4.5)
        libro2 = Libro('titulo2', 'autor2', 2025, 12345, 8)
        print(libro1.amosarLibro())
        print(libro2.amosarLibro())


if __name__ == "__main__":
    Principal.main()
