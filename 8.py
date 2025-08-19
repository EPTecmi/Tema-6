# Contador con opcion de reinicio
contador = 0
seguir = True

while seguir:
    print(f"Contador: {contador}")
    opcion = input("¿Incrementar (i), Reiniciar (r) o Salir (s)? ")
    
    if opcion == 'i':
        contador += 1
    elif opcion == 'r':
        contador = 0
        print("¡Contador reiniciado!")
    elif opcion == 's':
        seguir = False
    else:
        print("Opción no válida")

print("Programa terminado")
