class DimensionError(Exception):
    def __init__(self, mensaje=None, dimension=None, maximo=None) -> None:
        super().__init__()
        self._mensaje = mensaje
        self._dimension = dimension
        self._maximo = maximo

    @property
    def mensaje(self):
        return self._mensaje

    @mensaje.setter
    def mensaje(self, value):
        self._mensaje = value

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, value):
        self._dimension = value

    @property
    def maximo(self):
        return self._maximo

    @maximo.setter
    def maximo(self, value):
        self._maximo = value

    def __str__(self) -> str:
        if self.mensaje and not self.dimension and not self.maximo:
            return super().__str__()
        else:
            return f"MENSAJE CLASE DIMENSION ERROR: {self.mensaje}"