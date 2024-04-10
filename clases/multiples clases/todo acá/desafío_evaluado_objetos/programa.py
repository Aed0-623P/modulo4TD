from producto import *

stores = []

while True:
    store_type = input("Ingrese el tipo de tienda Restaurante, Supermercado, Farmacia o 'salir' para ver la canasta: \n").lower()

    if store_type == "salir":
        break
    if store_type == "restaurante":
        store = Restaurante()
    elif store_type == "supermercado":
        store = Supermercado()
    elif store_type == "farmacia":
        store = Farmacia()

    while True:
        nombre = input("Ingrese el nombre del producto: ")
        stock = int(input("Ingrese la cantidad en stock del producto: "))
        precio = int(input("Ingrese el precio del producto: "))
        producto = Producto(nombre, stock, precio)
        store.agregar_producto(producto)
        
        continuar = input("¿Desea agregar otro producto a la tienda? 1(si) o 2(no): \n")
        if continuar.lower() != "1":
            break
    
    stores.append(store)

while True:
    print("Lista de tiendas:")
    for i, store in enumerate(stores):
        print(f"{i + 1}. {type(store).__name__}")
    opcion = input("Seleccione una tienda para ver los productos (número) o salir para salir: \n")
    if opcion == "salir":
        break
    store_index = int(opcion) - 1
    selected_store = stores[store_index]
    print("Productos disponibles en la tienda:\n")
    for producto in selected_store.productos:
        print(f"Nombre: {producto.nombre}, Stock: {producto.stock}, Precio: {producto.precio}\n")
    accion = input("¿Desea comprar un producto (comprar) o volver al menú principal (volver)?: \n")
    if accion == "comprar":
        producto_comprar = input("Ingrese el nombre del producto que desea comprar: \n")
        for producto in selected_store.productos:
            if producto.nombre == producto_comprar:
                print(f"Ha comprado {producto.nombre} por un valor de {producto.precio}")
                exit()
        else:
            print("Producto no encontrado en la tienda.")
