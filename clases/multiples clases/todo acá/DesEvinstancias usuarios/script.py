import json
from usuario import Usuario

lista_usuarios = []


def manejar_excepcion(excepcion, linea):
    with open("error.log", "a") as archivo_error:
        archivo_error.write(f"Error al procesar la línea: {linea}\n")
        archivo_error.write(f"Tipo de error: {excepcion.__class__.__name__}\n")
        archivo_error.write(f"Descripción del error: {str(excepcion)}\n")
        archivo_error.write("=" * 50 + "\n")


with open("usuarios.txt", "r") as archivo:
    for linea in archivo:
        try:
            datos_usuario = json.loads(linea.strip())
            usuario = Usuario(
                nombre=datos_usuario.get("nombre", ""),
                apellido=datos_usuario.get("apellido", ""),
                email=datos_usuario.get("email", ""),
                genero=datos_usuario.get("genero", ""),
            )
            lista_usuarios.append(usuario)
        except json.JSONDecodeError as e:
            manejar_excepcion(e, linea)
        except Exception as e:
            manejar_excepcion(e, linea)
