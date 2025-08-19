# Calculadora simple con menú

opcion = 0
while opcion != 5:
    print("\n1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if 1 <= opcion <= 4:
        num1 = float(input("Primer número: "))
        num2 = float(input("Segundo número: "))
        
        if opcion == 1:
            print("Resultado:", num1 + num2)
        elif opcion == 2:
            print("Resultado:", num1 - num2)
        elif opcion == 3:
            print("Resultado:", num1 * num2)
        elif opcion == 4:
            if num2 != 0:
                print("Resultado:", num1 / num2)
            else:
                print("Error: No se puede dividir por cero")
    elif opcion != 5:
        print("Opción inválida")
