class Producto:
    def __init__(self, nombre: str, stock: int, precio: int):
        self.nombre = nombre
        self.stock = stock
        self.precio = precio

class Restaurante:
    def __init__(self):
        self._stock = 0
        self.productos = []

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        print("Warning: Cannot change stock of a restaurant.")

    def agregar_producto(self, producto: Producto):
        if producto.nombre in [p.nombre for p in self.productos]:
            existing_product = next(p for p in self.productos if p.nombre == producto.nombre)
            existing_product.stock += producto.stock
        else:
            self.productos.append(producto)

class Supermercado:
    def __init__(self):
        self.stock = 0
        self.productos = []

    def agregar_producto(self, producto: Producto):
        if producto.nombre in [p.nombre for p in self.productos]:
            existing_product = next(p for p in self.productos if p.nombre == producto.nombre)
            existing_product.stock += producto.stock
        else:
            self.productos.append(producto)

        if producto.stock < 10:
            print("Pocos productos disponibles")

class Farmacia:
    def __init__(self):
        self.stock = 0
        self.productos = []

    def agregar_producto(self, producto: Producto):
        if len(self.productos) < 3:
            print("No se pueden agregar más productos a la farmacia")
            return
        self.productos.append(producto)
        if producto.precio >= 15000:
            print("Envío gratis al solicitar este producto")