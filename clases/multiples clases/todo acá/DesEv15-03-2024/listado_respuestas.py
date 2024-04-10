from usuario import RealizarEncuesta

class List_Respuestas(RealizarEncuesta):
    def __init__(self, list_preg=list) -> None:
        super().__init__(list_preg)
        list_preg = []