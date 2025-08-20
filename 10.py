# Piedra, papel o tijeras - 5 Puntos
import random
jugando = True

while jugando:
    print("\n1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")
    
    usuario = int(input("Elige: "))
    computadora = random.randint(1, 3)
    
    if usuario == 4:
        jugando = False
        print("¡Gracias por jugar!")
    elif 1 <= usuario <= 3:
        opciones = ["", "Piedra", "Papel", "Tijera"]
        print(f"Tú: {opciones[usuario]} vs Computadora: {opciones[computadora]}")
        
        if usuario == computadora:
            print("¡Empate!")
        elif (usuario == 1 and computadora == 3) or \
             (usuario == 2 and computadora == 1) or \
             (usuario == 3 and computadora == 2):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")
    else:
        print("Opción inválida")