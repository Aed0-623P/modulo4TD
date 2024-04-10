from te import Tea

te1 = Tea()
te2 = Tea()

type_te1 = type(te1)
type_te2 = type(te2)

print("Tipo de objeto para tea1:", type_te1)
print("Tipo de objeto para tea2:", type_te2)

if type_te1 == type_te2:
    print("Ambos objetos son del mismo tipo.")
else:
    print("Los objetos no son del mismo tipo.")
