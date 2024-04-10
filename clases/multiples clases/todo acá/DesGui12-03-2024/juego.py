import random
from personaje import Personaje

print("¡Bienvenido a Gran Fantasía!\n")

name = input("Por favor indique nombre de su personaje: \n")

# instancia player
p = Personaje(name)
print(p.estado)
print("¡Oh no!,  ¡Ha aparecido un Orco!\n")

# instancia orco
o = Personaje("orco")

# enviar probabilidad de ganar
prob = p.prob_win(o)
opcion_orco = Personaje.battle(prob)

while opcion_orco == 1:
    resultado = "Ganaste" if random.uniform(0,1) < prob else "Perdiste"
    if resultado == "Ganaste":
        (
            """¡Le has ganado al orco felicidades!
        Recibirás 50 puntos de experiencia
        """
        )
        p.estado = 50
        o.estado = -30

    else:
        (
            """¡Oh no!  ¡El orco te ha ganado!
            ¡Has perdido 30 puntos de experiencia!
            """
        )
        p.estado = -30
        o.estado = 50
    print(p.estado)
    print(o.estado)

    prob = p.prob_win(o)
    opcion_orco = Personaje.battle(prob)