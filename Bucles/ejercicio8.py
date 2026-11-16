numero = int(input("Introduce un numero"))
# Haremos que se muestre en pantalla un triangulo rectangulo
for i in range(1, numero * 2, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()