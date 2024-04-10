from alternativa import Alternativa


class Preguntas(Alternativa):
    def __init__(self, cont: str, ayuda: str, enunciado: str, apoyo: str) -> None:
        super().__init__(cont, ayuda)
        self._enunciado = enunciado
        self._apoyo = apoyo

    lis_alt = []

    @property
    def enun_texto(self):
        return self._enunciado

    @enun_texto.setter
    def enun_texto(self, enunciado):
        self._enunciado = enunciado

    @property
    def apoyo_pregunta(self):
        return self._apoyo

    @apoyo_pregunta.setter
    def apoyo_pregunta(self, apoyo):
        self._apoyo = apoyo

    def mostrar_pregunta(
        self,
    ):
        print("toda la wea de arriba")
