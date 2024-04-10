class Pelota:
    # metodo constructor, esto va a chocar con todas las instrucciones más adelante
#    def __init__(self, color: str, tamanio=20, material="plástico"):
#        self.color = "blanco"
#        self.tamanio = 20
#        self.material = "plástico"
    #si matas el metodo constructor todas las funciones inferioren van a correr

    #getter
#    @property
#    def color_y_material(self):
#        return f"Pelota{self.color} de {self.material}"
    

    forma = "redondeada"

    posiciones = [3, 0, 2, 1, 0]

    @staticmethod
    def crear_rebote():
        return [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

    @staticmethod
    def imprimir_posiciones():
        Pelota.crear_rebote()
        print(Pelota.posiciones)

    # metodos no estaticos adelante

    def asigna_color(self, nuevo_color: str):  # asigna color
        self.color = nuevo_color

    def lee_color(self):  # lee el color de la pelota
        print("el color de esta pelota es{}\n".format(self.color))

    def lee_color_local_y_atributo(self, color_local: str):
        color = color_local  # la variable color solo existe en el alcance del método
        # metodo instancia llama a otro metodo
        self.lee_color()
        print("el color {} NO es el color de ESTA pelota\n".format(color))

    def lee_color_y_forma(self):
        print("el color de esta pelota es {}\n".format(self.color))
        print("la forma de esta pelota es{}\n".format(self.forma))

    def inicia_color(self):  # modificar con __setattr__
        self.color = ""


print(
    Pelota.crear_rebote()
)  # instancia de crear Pelota y llamar al metodo estático crear_rebote
Pelota.imprimir_posiciones()  # checkear el metodo estatico de crear rebote comparando con clase pelota y print

pelota_multicolor = Pelota()  # instancia multicolor
pelota_multicolor.asigna_color(" rojo")  # asigna rojo
pelota_multicolor.lee_color()  # lee colores asignados
pelota_multicolor.asigna_color(" verde")  # asigna verde
pelota_multicolor.lee_color_local_y_atributo(
    "amarillo"
)  # lee color previo y atributo a ingresar, omite el rojo por que fue reemplazado por verde

pelota_de_andy = Pelota()  # instancia de andy
pelota_de_andy.inicia_color()  # crea atributo
pelota_de_andy.color = " amarillo"  # asigna valor al atributo
pelota_de_andy.lee_color()  # leer color


# p = Pelota("Amarillo", 16,"plástico")         #choca con multicolor por que Pelota() no tiene los 3 valores
