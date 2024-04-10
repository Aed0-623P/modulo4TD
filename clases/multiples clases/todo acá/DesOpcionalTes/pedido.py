from te import Tea


def main():
    sabor = int(
        input(
            "Ingrese el número correspondiente al sabor:\n1. Té negro\n2. Té verde\n3. Infusión de hierbas\n"
        )
    )
    formato = int(input("Ingrese el formato deseado (300 gr o 500 gr):\n"))

    tea = Tea()
    preparation_time, recommendation = tea.get_preparation_and_recommendation(sabor)
    price = tea.get_price(formato)

    sabores = {1: "Té negro", 2: "Té verde", 3: "Infusión de hierbas"}
    formats = {300: "300 gr", 500: "500 gr"}

    print("Detalle del pedido:")
    print("Sabor del té:", sabores[sabor])
    print("Formato:", formats[formato])
    print("Precio: $", price)
    print("Tiempo de preparación:", preparation_time, "minutos")
    print("Recomendación de consumo:", recommendation)


if __name__ == "__main__":
    main()
