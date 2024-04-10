class Alternativa:
    def __init__(self, cont: str, ayuda: str) -> None:
        self.cont = cont
        self.ayuda = ayuda

    @property
    def contenido(self):
        return self.contenido

    @contenido.setter
    def contenido(self, cont):
        self._contenido = cont

    @property
    def help(self):
        return self.help

    @help.setter
    def contenido(self, cont):
        self.help = cont

    def most_alt(self):
        return self.cont, self.ayuda
