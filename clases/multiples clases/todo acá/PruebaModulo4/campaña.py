from datetime import datetime
from anuncio import Anuncio
from error import LargoExcedidoException

class Campaña:
    def __init__(self, nombre: str, fecha_inicio: datetime, fecha_termino: datetime) -> None:
        if len(nombre) > 250: raise LargoExcedidoException() 
        else: self.__nombre = nombre 
        self.__fecha_inicio = fecha_inicio         #instrucciones poco claras
        self.__fecha_termino = fecha_termino       #ambos sin getter página 3 punto 3
        self.lista_anuncios = []

    @property
    def lista_anuncios(self):                      #solo getter lista_anuncios, sin setter
        return self.lista_anuncios
    
    @set_fecha_inicio.setter
    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    @set_fecha_termino.setter
    def set_fecha_termino(self, fecha_termino):
        self.__fecha_termino = fecha_termino

    def __str__(self):
        anuncios_count = {}
        for anuncio in self.lista_anuncios:
            anuncio_type = anuncio.sub_tipo
            if anuncio_type in anuncios_count:
                anuncios_count[anuncio_type] += 1
            else:
                anuncios_count[anuncio_type] = 1
        
        anuncios_str = ", ".join([f"{count} {anuncio_type}" for anuncio_type, count in anuncios_count.items()])
        
        anuncios_list = "\n".join([str(anuncio) for anuncio in self.lista_anuncios])

        return f"Nombre de la campaña: {self.__nombre}\nCantidad de campañas: {anuncios_str}\nAnuncios:\n{anuncios_list}"