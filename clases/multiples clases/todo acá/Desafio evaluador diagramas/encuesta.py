class Encuesta:
    def __init__(self, list_preg=list) -> None:
        self.list_preg = []
        pass


class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, edad: int) -> None:
        super().__init__()
        self.edad = edad


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, region: int) -> None:
        super().__init__()
        self.region = region
