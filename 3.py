# Promedio de calificaciones
total = 0
cantidad = 0
nota = float(input("Ingrese una nota (-1 para terminar): "))

while nota != -1:
    total += nota
    cantidad += 1
    nota = float(input("Ingrese otra nota (-1 para terminar): "))

if cantidad > 0:
    promedio = total / cantidad
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron notas")
