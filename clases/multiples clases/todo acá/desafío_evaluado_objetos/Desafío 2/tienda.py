from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    def __init__(self, n_tienda: str, delivery: int):
        self.n_tienda = n_tienda
        self.delivery = delivery
        self.productos = []

    @abstractmethod
    def venta(self):
        pass

    @abstractmethod
    def lista(self):
        pass

    def ingresar(self):
        nombre = input("Ingrese nombre del producto: ").title()
        precio = int(input("Ingrese precio del producto: "))
        stock = int(input("Ingrese stock del producto: "))
        producto_existente = self.buscar_producto(nombre)
        if producto_existente:
            producto_existente.stock += stock
        else:
            producto = Producto(nombre, precio, stock)
            self.productos.append(producto)
        print("Producto ingresado")

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

class Restaurante(Tienda):
    def __init__(self, n_tienda: str, delivery: int):
        super().__init__(n_tienda, delivery)

    def venta(self):
        print("Vender productos restaurante")
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Precio individual: {producto.precio}")

    def lista(self):
        print("Listando productos en restaurante")
        print("###        ###")
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Stock: {0}  \n")

class Supermercado(Tienda):
    def __init__(self, n_tienda: str, delivery: int):
        super().__init__(n_tienda, delivery)

    def venta(self):
        nombre = input("Ingrese nombre del producto: ")
        cantidad = int(input("Ingrese cantidad requerida: "))
        producto = self.buscar_producto(nombre)
        if producto:
            if cantidad <= producto.stock:
                producto.stock -= cantidad
                print(f"Nombre: {producto.nombre}, Precio individual: {producto.precio}, Cantidad{cantidad}")
            elif producto.stock < 10:
                print("Pocos productos disponibles")
            else:
                print("No hay suficiente stock")
        else:
            print("Producto no encontrado")

    def lista(self):
        print("Listando productos en supermercado")
        print("###        ###")
        for producto in self.productos:
            if producto.stock < 10:
                print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock} - Pocos productos disponibles")
            else:
                print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}")

class Farmacia(Tienda):
    def __init__(self, n_tienda: str, delivery: int):
        super().__init__(n_tienda, delivery)

    def venta(self):
        nombre = input("Ingrese nombre del producto: ")
        cantidad = int(input("Ingrese cantidad requerida: "))
        producto = self.buscar_producto(nombre)
        if producto:
            if cantidad <= producto.stock:
                if cantidad <= 3:
                    producto.stock -= cantidad
                    print("Venta realizada en farmacia")
                else:
                    print("No se puede vender más de 3 unidades de un producto en farmacia")
            else:
                print("No hay suficiente stock")
        else:
            print("Producto no encontrado")

    def lista(self):
        print("Listando productos en farmacia")
        print("###        ###")
        for producto in self.productos:
            if producto.precio > 15000:
                print(f"Nombre: {producto.nombre}, Precio: {producto.precio} - Envío gratis al solicitar este producto")
            else:
                print(f"Nombre: {producto.nombre}, Precio: {producto.precio}")


