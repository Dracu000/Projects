numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
if numero2 == 0:
    print("Error: No se puede dividir por cero.")
else:
    resultado = numero1 / numero2
    print("El resultado de la división es:", resultado)