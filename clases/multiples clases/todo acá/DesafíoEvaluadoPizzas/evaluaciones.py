from pizza import PizzaMaker

#punto 5.a
print(PizzaMaker.pedido, PizzaMaker.val_elemento)

#punto 5.b, las salsas no estan incluidas en el indice, siempre va a fallar el programa aquí...
salsas = ["salsa de tomate", "salsa bbq"]
if PizzaMaker.val_elemento("salsa de tomate", salsas):
    print("salsa en metodo")
else:
    print("salsa no en el metodo")

#punto 5.c,d y e, creo, no entiendo bien el enunciado d y e. 
hambre = PizzaMaker()
hambre.pedido()