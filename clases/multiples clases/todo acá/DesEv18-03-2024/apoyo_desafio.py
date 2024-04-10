from error import DimensionError

class Foto:
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.ancho = ancho
        self.alto = alto
        self.ruta = ruta  # el archivo original traía ruta = ruta, lo cambié por self.ruta = ruta

    @property
    def ancho(self) -> int:
        return self._ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho < 1 or ancho > 2500:
            raise DimensionError("MENSAJE DE LA INSTANCIA FOTO ANCHO", ancho, 2500)
        else:
            self._ancho = ancho

    @property
    def alto(self) -> int:
        return self._alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto < 1 or alto > 2500:
            raise DimensionError("MENSAJE DE LA INSTANCIA FOTO ALTO", alto, 2500)
        else:
            self._alto = alto

f = Foto(2500, 50, "saludos")
try:
    print(f.ancho)
    print(f.alto)
    print(f.ruta)
except DimensionError as e:
    print(e)