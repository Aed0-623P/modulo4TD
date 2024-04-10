#checkear error nombre campaña no supere 250 caracteres
#tirar error LargoExcedidoException

class SubTipoInvalidoException(Exception):
    print("Sub tipo de anuncio no válido")

class LargoExcedidoException(Exception):
    def __init__(self, message="El nombre excede los 250 caracteres."):
        self.message = message
        super().__init__(self.message)