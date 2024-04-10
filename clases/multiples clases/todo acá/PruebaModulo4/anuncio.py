from abc import ABC, abstractmethod
from error import SubTipoInvalidoException


class Anuncio(ABC):
    def __init__(self, alto: int, ancho: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self.__alto = alto if alto > 0 else 1
        self.__ancho = ancho if ancho > 0 else 1
        self.__url_archivo = url_archivo                    #instrucciones poco claras en página uno punto 2
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        self.__alto = alto

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo

    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, url_clic):
        self.__url_clic = url_clic

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, tipo):
            tipo_valido = ("instream", "outstream", "tradicional", "native", "facebook", "linkedin")
            if isinstance(tipo, tuple) and all(item in tipo_valido for item in tipo):
                self.__sub_tipo = tipo
            else:
                raise SubTipoInvalidoException

    @abstractmethod
    def mostrar_formatos():
        print("PLACEHOLDER MOSTRAR FORMATOS")
        print(f"DEBE DEVOLVER ALGO COMO\n FORMATO 1:\n ======= \n -Subtipo {sub_tipo}\n")

    def comprimir_anuncio():
        print("PLACEHOLDER COMPRIMIR ANUNCIO")

    def redimensionar_anuncio():
        print("PLACEHOLDER REDIMENSIONAR ANUNCIO")




class Video(Anuncio):
    def __init__(self,formato,sub_tipo,ancho,alto,duracion):
        super().__init__(alto, ancho, "", "", sub_tipo)
        formato = "Video"
        self.formato = formato
        self.sub_tipo = ("instream", "outstream")
        self.__ancho = 1  # valor fijo
        self.__alto = 1  # valor fijo
        self.__duracion = duracion if duracion > 0 else 5

    def comprimir_anuncio():
        return "COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN"

    def redimensionar_anuncio():
        return "RECORTE DE VIDEO NO IMPLEMENTADO AÚN"


class Display(Anuncio):
    def __init__(self,formato,sub_tipo) -> None:
        self.formato = "Display"
        self.sub_tipo = ("tradicional", "native")

    def comprimir_anuncio():
        return "COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN"

    def redimensionar_anuncio():
        return "RECORTE DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN"


class Social(Anuncio):
    def __init__(self,formato,sub_tipo) -> None:
        self.formato = "Social"
        self.sub_tipo = ("facebook", "linkedin")

    def comprimir_anuncio():
        return "COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN"

    def redimensionar_anuncio():
        return "RECORTE DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN"
