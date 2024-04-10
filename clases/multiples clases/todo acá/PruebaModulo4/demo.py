from campaña import Campaña
from anuncio import Anuncio
from datetime import datetime


campana = Campaña("campaña 1", datetime.now(), datetime.now())
video = Anuncio("Video", "instream", 1920, 1080, 30)
campana.lista_anuncios.append(video)


try:
    nuevo_nombre = input("nombre campaña: ")
    nuevo_tipo = input("tipo campaña: ")


    campana.set_nombre(nuevo_nombre)
    campana.lista_anuncios[0].set_sub_tipo(nuevo_tipo)

except Exception as e:
    with open("error.log", "w") as error_file:
        error_file.write(f"Error: {str(e)}\n")