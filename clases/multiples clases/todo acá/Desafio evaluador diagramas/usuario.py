from encuesta import Encuesta


class Usuario:
    def __init__(self, correo: str, edad: int, region: int) -> None:
        self._correo = correo
        self._edad = edad
        self._region = region

    @property
    def edit_correo(self):
        return self._correo

    @edit_correo.setter
    def edit_correo(self, correo):
        self._correo = correo

    @property
    def edit_edad(self):
        return self._edad

    @edit_edad.setter
    def edit_edad(self, edad):
        self._edad = edad

    @property
    def edit_region(self):
        return self._region

    @edit_region.setter
    def edit_region(self, region):
        self._region = region


class RealizarEncuesta(Encuesta):
    def __init__(self, list_preg=...) -> None:
        super().__init__(list_preg)
