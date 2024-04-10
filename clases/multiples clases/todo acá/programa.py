from medicamento import Medicamento

#nombre = input("Ingrese nombre del medicamento: \n")
#stock = int(input("ingrese stock del medicamento: \n"))
#precio_bruto = int(input("Ingrese precio bruto del medicamento: \n"))

#m1 = Medicamento(nombre, stock)
#m1.precio = precio_bruto

#print(f"El precio bruto del medicamento es {m1.nombre} es {m1.precio_bruto}")

#if m1.descuento:
#    print(f"Tiene un descuento de {m1.descuento*100}%")

#print(f"El precio final del medicamento es {m1.precio_final}")


opcion_ingreso = int(input("¿Desea agregar un medicamento?"
"\n1. Sí\n2. No\n"))
ingresados = []

while opcion_ingreso == 1:
    nombre = input("\nIngrese nombre del medicamento:\n")
    stock = int(input("\nIngrese stock del medicamento:\n"))
    m = Medicamento(nombre, stock)
    if m in ingresados:
        indice = ingresados.index(m)
        ingresados[indice] += m
    else:
        ingresados.append(m)
        precio_bruto = int(input("\nIngrese precio bruto del medicamento:\n"))
        m.precio = precio_bruto
    print(f"\n***** DATOS MEDICAMENTO {m.nombre} *****")
    print(f"PRECIO BRUTO: ${m.precio_bruto}")
    if m.descuento:
        print(f"DESCUENTO: {m.descuento*100}%")
        print(f"PRECIO FINAL: ${m.precio_final}")
        print(f"STOCK: {m.stock}")
        print(f"\nLa farmacia cuenta con {len(ingresados)} medicamento(s)\n")

opcion_ingreso = int(input("¿Desea agregar un medicamento?"
"\n1. Sí\n2. No\n"))