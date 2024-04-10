from medicamento import Medicamento  #importar clase de medicamento.py

primer_medicamento = Medicamento()  #primera instancia de clase

#solicitar precio a validar
precio = int(input("ingrese precio a validar:\n"))

#llamar a la clase para validar

es_valido = Medicamento.validar_mayor_a_cero(precio)

if es_valido:
    print("el precio ingresado es valido")
else:
    print("el precio ingresado no es valido")

m1 = Medicamento()  
m2 = Medicamento()

if m1.IVA == m2.IVA and m1.descuento == m2.descuento:  #checkear si instancia m1 es igual que m2, ambas de clase medicamento
    print("Todas las instancias tienen igual descuento e IVA")
    print("El valor del IVA es: ", Medicamento.IVA)
    print("El valor del descuento es:", Medicamento.descuento)

medicamento_nuevo = Medicamento()  #nueva instancia para checkear un precio valido
precio2 = int(input("ingrese el precio del medicamento\n")) #asignar variable
medicamento_nuevo.asigna_precio(precio2) #asignar a instancia