# Factorial de un número 

numero = int(input("Ingrese un número: "))
factorial = 1
contador = 1

while contador <= numero:
    factorial *= contador
    contador += 1

print(f"El factorial de {numero} es {factorial}")
