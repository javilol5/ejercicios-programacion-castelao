from Persoa import Persoa
from Deportista import Deportista

def main():
    print()
    print("Persoa")
    print()
    try:
        p = Persoa(
            "Ana Pérez",
            "Rúa Maior 10",
            "12345678Z"
        )
        print("Nome:", p.getNome())
        print("Dirección:", p.getDireccion())
        print("DNI:", p.getDni())
    except ValueError as e:
        print("Erro en Persoa:", e)

    print()
    print("Deportista")
    print()
    try:
        d = Deportista(
            "Fútbol",
            "Celta",
            "2026fut123456"
        )
        print("Deporte:", d.getDeporte())
        print("Clube:", d.getClube())
        print("Licenza:", d.getLicencia())
    except ValueError as e:
        print("Erro en Deportista:", e)

    print()
    print("Deportista Error")
    print()
    try:
        d2 = Deportista(
            "Baloncesto",
            "Breogán",
            "2025bal12A456"
        )
    except ValueError as e:
        print("Erro esperado:", e)

if __name__ == "__main__":
    main()