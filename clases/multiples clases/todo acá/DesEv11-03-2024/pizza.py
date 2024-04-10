class PizzaMaker():
    def val_elemento(self,val_txt:str): 
        ingredients = ["tomate", "aceitunas", "champiñones", "pollo",
                       "vacuno", "carne vegetal", "tradicional", "delgada"]
        if val_txt in ingredients:            
            return True
        else:
            return False
    #elementos para la pizza
    def pedido(self): #mucho cuidado en inputear en singular o plural
        prote = input("Ingrese ingrediente proteico, puede ser pollo, vacuno o carne vegetal: \n").lower()
        veggie1 = input("Ingrese el primer ingrediente vegetal puede ser tomate, aceitunas o champiñones: \n").lower()
        veggie2 = input("Ingrese el segundo ingrediente vegetal puede ser tomate, aceitunas o champiñones: \n").lower()
        masa = input("Ingrese tipo de masa, delgada o tradicional: \n").lower()        
        if all(self.val_elemento(ingrediente) for ingrediente in [prote, veggie1, veggie2, masa]):
            print(f"Rica pizza de {prote}, {veggie1}, {veggie2} y {masa}")
        else:
            print(f"Pizza no válida")