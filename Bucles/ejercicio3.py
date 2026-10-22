numero = int(input("Introduce un número: "))
# Mostramos todos los numeros impares desde 1º hasta el número ingresado
for i in range(1, numero + 1):
    if i % 2 != 0:
        print(i)