class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    # mostrar los stats del pj
    @property
    def estado(self):
        return (f"NOMBRE: {self.nombre}       NIVEL:      {self.nivel} EXPERCIENCIA:      {self.experiencia}")

    # setter para cambiar valores
    @estado.setter
    def estado(self, experiencia):
        nXp = self.experiencia + experiencia
        # subir nivel
        while nXp >= 100:
            self.nivel += 1
            nXp -= 100

        # if nXp = 0,  lvl+1
        while nXp < 0:
            if self.nivel > 0:
                nXp += 100
                self.nivel <= 1
            else:
                nXp = 0
            self.experiencia = nXp

    # sobrecarga menor que
    def __lt__(self, other):
        return self.nivel < other.nivel

    # sobrecarga mayor que
    def __gt__(self, other):
        return self.nivel > other.nivel

    #sobrecarga igual que
    def __eq__(self, other):
        return self.nivel == other.nivel

    # probabilidades de ganar, comparando nivel de player v enemy
    def prob_win(self, other):
        if self > other:
            return 0.33
        elif self < other:
            return 0.66
        else:
            return 0.5
        
    #Que pasa en el enfrentamiento
    @staticmethod
    def battle(probabilidad):
        return float(input(f"""Con tu nivel actual tienes {probabilidad}% de ganarle al orco.\n
Si ganas, ganarás 50 puntoas de experiencia y el orco perderá 30.\n
Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n
1. Atacar
2. Huir
"""))