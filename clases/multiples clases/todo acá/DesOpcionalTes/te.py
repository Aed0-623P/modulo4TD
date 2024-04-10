class Tea:
    FORMATO_300GR_PRECIO = 3000
    FORMATO_500GR_PRECIO = 5000

    @staticmethod
    def get_preparation_and_recommendation(sabor):
        if sabor == 1:
            return 3, "Se recomienda consumir al desayuno."
        elif sabor == 2:
            return 5, "Se recomienda consumir al medio día."
        elif sabor == 3:
            return 6, "Se recomienda consumir al atardecer."

    @staticmethod
    def get_price(formato):
        if formato == 300:
            return Tea.FORMATO_300GR_PRECIO
        elif formato == 500:
            return Tea.FORMATO_500GR_PRECIO
