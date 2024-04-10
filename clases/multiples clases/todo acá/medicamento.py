class Medicamento():
    IVA = 0.18
    def __init__(self, nombre: str, stock: int = 0):
        self.nombre = nombre
        self.stock = stock
        self.precio_bruto = 0
        self.precio_final = 0.0
        self.descuento = 0.0
        
    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0
    
    @property
    def precio(self):
        return self.precio_final

    @precio.setter
    def precio(self, precio_bruto: int):
        if self.validar_mayor_a_cero(precio_bruto):
            self.precio_bruto = precio_bruto
            self.precio_final = precio_bruto + precio_bruto * self.IVA
        if self.precio_final >= 10000 and self.precio_final < 20000:
            self.descuento = 0.1
        elif self.precio_final >= 20000:
            self.descuento = 0.2
        if self.descuento:
            self.precio_final *= 1 - self.descuento
# Este es el método que se debe agregar
    def __eq__(self, other):
        return self.nombre.lower() == other.nombre.lower()
    
    def __iadd__(self, other):
        if self == other:
            self.stock += other.stock
        return self

#    def asigna_precio(self,precio_entregado:int): #instancia donde entregan valor del producto
#        es_valido = self.validar_mayor_a_cero(precio_entregado) #se checkea en una variable local con el static method
#        if es_valido:
#            self.precio = precio_entregado #asignar variable precio para el check true
#            self.descuento = 0.0
#            if self.precio >= 10000 and self.precio < 20000:
#                self.descuento = 0.1
#            elif self.precio >= 20000 and self.precio <30000:
#                self.descuento = 0.2
#            elif self.precio >= 30000:
#                self.descuento = 0.3
#        else:
#            print("el precio {} no es un precio válido".format(precio_entregado))
