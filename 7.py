# Suma de números hasta que se ingrese 0
suma = 0
numero = int(input("Ingrese un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número (0 para terminar): "))
print("La suma total es:", suma)
