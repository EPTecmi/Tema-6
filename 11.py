# Adivina el número (1-10)
import random
secreto = random.randint(1, 10)
intento = 0

while intento != secreto:
    intento = int(input("Adivina el número (1-10): "))
    if intento < secreto:
        print("Más alto!")
    elif intento > secreto:
        print("Más bajo!")
print("¡Correcto!")
