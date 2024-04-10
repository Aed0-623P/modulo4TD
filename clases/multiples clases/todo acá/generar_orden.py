from orden_compra import OrdenCompra


oc = OrdenCompra()  #oc = instancia de orden de compra
oc.nueva_orden() #metodo nueva orden
oc.identificador = int(input("ingrese el identificador de la OC: \n")) #valor en metodo
oc.total_productos = int(input("Ingrese total de productos: \n")) #valor en metodo
#oc.monto = int(input("Ingrese monto: \n")) #valor en metodo #reemplazo futuro

monto = int(input("Ingrese monto: \n"))
oc.asigna_monto(monto)

#if oc.monto > 20000:                            #checkear si el monto ingresado es valido para un descuento
#    oc.codigo_descuento = "20PORCIENTO"
#elif oc.monto > 10000:
#    oc.codigo_descuento = "10PORCIENTO"         #check ingresado a la clase

print(oc.codigo_descuento)