class Equipo:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__ganhados = 0
        self.__perdidos = 0
        self.__empatados = 0

    def get_nome(self) -> str:
        return self.__nome

    def get_ganhados(self) -> int:
        return self.__ganhados

    def get_perdidos(self) -> int:
        return self.__perdidos

    def get_empatados(self) -> int:
        return self.__empatados

    def add_victoria(self) -> None:
        self.__ganhados += 1

    def add_perdido(self) -> None:
        self.__perdidos += 1

    def add_empate(self) -> None:
        self.__empatados += 1

    def get_puntos(self) -> int:
        return self.__ganhados * 3 + self.__empatados

    def get_encontros_xogados(self) -> int:
        return self.__ganhados + self.__perdidos + self.__empatados

    def __str__(self):
        return (
            f"{self.__nome} - "
            f"V: {self.__ganhados} "
            f"E: {self.__empatados} "
            f"D: {self.__perdidos} "
            f"(Puntos: {self.get_puntos()})"
        )


# -------------------------------------------------------------

class TorneoXestor:
    def __init__(self, nome_torneo: str, num_max_equipos: int):
        self.__nome_torneo = nome_torneo
        self.__num_max_equipos = num_max_equipos
        self.__equipos = [None] * num_max_equipos
        self.__num_equipos = 0

    def rexistrar_equipo(self, equipo: Equipo) -> bool:
        # Evitar equipos duplicados
        for e in self.__equipos:
            if e is not None and e.get_nome() == equipo.get_nome():
                return False

        if self.__num_equipos < self.__num_max_equipos:
            self.__equipos[self.__num_equipos] = equipo
            self.__num_equipos += 1
            return True

        return False

    def consultar_equipo(self, nome: str):
        for equipo in self.__equipos:
            if equipo is not None and equipo.get_nome() == nome:
                return equipo
        return None

    def rexistrar_resultado(self, nome_equipo: str, resultado: str) -> bool:
        equipo = self.consultar_equipo(nome_equipo)

        if equipo is None:
            return False

        if resultado == "V":
            equipo.add_victoria()
        elif resultado == "E":
            equipo.add_empate()
        elif resultado == "D":
            equipo.add_perdido()
        else:
            return False

        return True

    def mostrar_clasificacion(self):
        equipos_validos = []

        for e in self.__equipos:
            if e is not None:
                equipos_validos.append(e)

        equipos_ordenados = sorted(
            equipos_validos,
            key=lambda e: e.get_puntos(),
            reverse=True
        )

        print("CLASIFICACIÓN:")
        for e in equipos_ordenados:
            print(e)

    def estadisticas_torneo(self):
        total_partidos = 0

        for e in self.__equipos:
            if e is not None:
                total_partidos += e.get_encontros_xogados()

        print(f"Torneo: {self.__nome_torneo}")
        print(f"Equipos inscritos: {self.__num_equipos}")
        print(f"Partidos xogados no total: {total_partidos}")

    def sair(self):
        print("Saíndo do xestor do torneo...")


# -------------------------------------------------------------
# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    torneo = TorneoXestor("Torneo Escolar", 3)

    e1 = Equipo("Madrid")
    e2 = Equipo("Barça")
    e3 = Equipo("Valencia")

    torneo.rexistrar_equipo(e1)
    torneo.rexistrar_equipo(e2)
    torneo.rexistrar_equipo(e3)

    torneo.rexistrar_resultado("Madrid", "V")
    torneo.rexistrar_resultado("Barça", "E")
    torneo.rexistrar_resultado("Valencia", "D")
    torneo.rexistrar_resultado("Madrid", "V")

    torneo.mostrar_clasificacion()
    torneo.estadisticas_torneo()