class Pelota():

    def __init__(self):      #, color: str, material: str
        #self.color = color
        #self.tamanio = int
        #self.material = material
        self.tamanio_pelota = 1
    
    @property
    def color_y_material(self):
        return f"Pelota {self.color} de {self.material}"
    
    @property
    def tamanio(self):
        return self.tamanio_pelota
    
    @tamanio.setter
    def tamanio(self, tamanio: int):
        self.tamanio_pelota = tamanio if tamanio > 0 else 1
    
    

#p = Pelota("Amarilla", "plastico")
#print(p.color_y_material)

p2 = Pelota()   
print(p2.tamanio)
p2.tamanio = 0
print(p2.tamanio)
