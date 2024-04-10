from tienda import *
import sys

while True:
    print("Seleccione el tipo de tienda:")
    print("1. Restaurante")
    print("2. Supermercado")
    print("3. Farmacia")
    print("4. Salir")
    
    choice_tienda = input("Seleccione una opción: ")

    if choice_tienda == "1":
        n_rest = input("Ingrese nombre del Restaurante: ")
        p_del1 = int(input("Ingrese valor delivery: "))
        restaurante = Restaurante(n_rest, p_del1)
        while True:
            print("\nMenu:")
            print("1. Ingresar producto")
            print("2. Ver lista de productos")
            print("3. Comprar producto")
            print("4. Salir")
            choice = input("Seleccione una opción: ")
            if choice == "1":
                restaurante.ingresar()
            elif choice == "2":
                restaurante.lista()
            elif choice == "3":
                restaurante.venta()
            elif choice == "4":
                sys.exit()
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    elif choice_tienda == "2":
        n_super = input("Ingrese nombre del Supermercado: ")
        p_del2 = int(input("Ingrese valor delivery: "))
        supermercado = Supermercado(n_super, p_del2)
        while True:
            print("\nMenu:")
            print("1. Ingresar producto")
            print("2. Ver lista de productos")
            print("3. Comprar producto")
            print("4. Salir")
            choice = input("Seleccione una opción: ")
            if choice == "1":
                supermercado.ingresar()
            elif choice == "2":
                supermercado.lista()
            elif choice == "3":
                supermercado.venta()
            elif choice == "4":
                sys.exit()
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    elif choice_tienda == "3":
        n_farm = input("Ingrese nombre de la Farmacia: ")
        p_del3 = int(input("Ingrese valor delivery: "))
        farmacia = Farmacia(n_farm, p_del3)
        while True:
            print("\nMenu:")
            print("1. Ingresar producto")
            print("2. Ver lista de productos")
            print("3. Comprar producto")
            print("4. Salir")
            choice = input("Seleccione una opción: ")
            if choice == "1":
                farmacia.ingresar()
            elif choice == "2":
                farmacia.lista()
            elif choice == "3":
                farmacia.venta()
            elif choice == "4":
                sys.exit()
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    elif choice_tienda == "4":
        sys.exit()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
